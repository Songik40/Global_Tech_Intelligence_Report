import datetime as dt
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import report_pipeline as p
import verify_report as v

class PublicationBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.patch_root = patch.object(p,'ROOT',self.root)
        self.patch_root.start()
        self.date = dt.datetime.now(p.KST).date().isoformat()
        self.cutoff = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
        ym = self.date[:4]+'/'+self.date[5:7]
        self.report = 'reports/'+ym+'/'+self.date+'.md'
        self.ledger = 'sources/'+ym+'/'+self.date+'.md'
        for path,text in [('README.md','# Main\n'),('reports/README.md','# Reports\n- [old](old.md)\n'),('trends/ai.md','# Existing evidence\n')]:
            (self.root/path).parent.mkdir(parents=True,exist_ok=True)
            (self.root/path).write_text(text)
        front = '\n'.join(['---','date: '+self.date,'story_count: 5','cutoff_utc: '+self.cutoff.isoformat(),
            'cutoff_kst: '+self.cutoff.astimezone(p.KST).isoformat(),
            'coverage_start_utc: '+(self.cutoff-dt.timedelta(hours=24)).isoformat(),'coverage_hours: 24','---'])
        url = 'https://example.com/evidence'
        report = front+'\n'+'\n'.join('## '+str(i)+'. Evidence\n'+url+'\n'+'\n'.join('### '+x+'\nEvidence' for x in ('FACT','ANALYSIS','UNCERTAINTY','WATCH')) for i in range(1,6))
        ledger = front+'\n'+url+'\n분야별 탐색\n한국\n예정 이벤트\n선정\n게시 후 검증\n'
        self.bundle = {'date':self.date,'cutoff_utc':self.cutoff.isoformat(),'base_head':'base',
            'files':[{'path':path,'content':text} for path,text in [(self.report,report),(self.ledger,ledger),('README.md','# Main\n'),('reports/README.md','# Reports\n- [old](old.md)\n'),('assets/'+self.date+'/README.md','# Assets\n')]],
            'stories':[{'domain':p.DOMAINS[i%4],'novelty':'Actual new release','sources':[{'url':url,'grade':'A1','checked_at_utc':self.cutoff.isoformat(),'event_time_utc':self.cutoff.isoformat(),'time_uncertainty':'','access':'read'}],'gap_label':''} for i in range(5)],
            'sweeps':[{'domain':d,'sources_checked':[url],'candidates':[{'title':'candidate','exclusion_reason':''}]} for d in p.DOMAINS]}
        self.git_patch = patch.object(p,'git',return_value='base')
        self.git_patch.start()
    def tearDown(self):
        self.git_patch.stop()
        self.patch_root.stop()
        self.tmp.cleanup()
    def test_valid_bundle_is_data_only(self):
        self.assertEqual(set(p.checked_bundle(self.bundle)),{f['path'] for f in self.bundle['files']})
    def test_model_cannot_write_workflow_or_traverse(self):
        for path in ['.github/workflows/evil.yml','scripts/run.py','methodology/editorial-policy.md','../README.md','assets/'+self.date+'/../../README.md','/tmp/file']:
            self.assertFalse(p.allowed_path(path,self.date),path)
    def test_previous_reports_are_never_overwritten(self):
        self.assertFalse(p.allowed_path('reports/2020/01/2020-01-01.md',self.date))
        target=self.root/self.report
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text('Already published')
        self.assertTrue(p.same_day(self.date))
        self.assertFalse(p.allowed_path(self.report,self.date))
    def test_model_cannot_claim_completed_checks(self):
        self.bundle['files'][1]['content']+='\n'+v.MARKER
        with self.assertRaisesRegex(ValueError,'claim'):
            p.checked_bundle(self.bundle)
    def test_prior_cumulative_evidence_must_be_preserved(self):
        self.bundle['files'].append({'path':'trends/ai.md','content':'Rewritten history'})
        with self.assertRaisesRegex(ValueError,'preserve'):
            p.checked_bundle(self.bundle)
    def test_zero_selected_domain_needs_two_exclusions(self):
        for s in self.bundle['stories']:
            s['domain']=p.DOMAINS[0]
        with self.assertRaisesRegex(ValueError,'two rejected'):
            p.checked_bundle(self.bundle)
    def test_future_evidence_and_fake_primary_access_rejected(self):
        self.bundle['stories'][0]['sources'][0]['event_time_utc']=(self.cutoff+dt.timedelta(minutes=1)).isoformat()
        with self.assertRaisesRegex(ValueError,'after cutoff'):
            p.checked_bundle(self.bundle)
        self.bundle['stories'][0]['sources'][0]['event_time_utc']=''
        self.bundle['stories'][0]['sources'][0]['time_uncertainty']='Time unknown'
        self.bundle['stories'][0]['sources'][0]['access']='blocked'
        with self.assertRaisesRegex(ValueError,'read primary'):
            p.checked_bundle(self.bundle)
    def test_utc_kst_and_coverage_must_agree(self):
        self.bundle['files'][0]['content']=self.bundle['files'][0]['content'].replace((self.cutoff-dt.timedelta(hours=24)).isoformat(),self.cutoff.isoformat())
        with self.assertRaisesRegex(ValueError,'coverage mismatch'):
            p.checked_bundle(self.bundle)
    def test_head_conflict_cannot_mutate_ref(self):
        with patch.object(p,'api',return_value={'object':{'sha':'someone-elses-commit'}}) as api:
            with self.assertRaisesRegex(ValueError,'main changed'):
                p.commit_files({'README.md':'new'},'base','test')
            self.assertEqual(api.call_count,1)
    def test_fast_forward_only_ref_update(self):
        calls=[]
        def api(path,data=None,method=None):
            calls.append((path,data,method))
            if path=='/git/ref/heads/main': return {'object':{'sha':'base'}}
            if path=='/git/commits/base': return {'tree':{'sha':'oldtree'}}
            return {'sha':'created'}
        with patch.object(p,'api',side_effect=api):
            p.commit_files({'README.md':'new'},'base','test')
        self.assertEqual(calls[-1],('/git/refs/heads/main',{'sha':'created','force':False},'PATCH'))
    def test_policy_errors_do_not_retry(self):
        import urllib.error
        error=urllib.error.HTTPError('https://api.openai.com',403,'Forbidden',{},None)
        with patch.dict(os.environ,{'OPENAI_API_KEY':'test-only'}), patch.object(p.urllib.request,'urlopen',side_effect=error) as send:
            with self.assertRaisesRegex(ValueError,'no policy/access-error retries'):
                p.response({})
            self.assertEqual(send.call_count,1)
    def test_refusal_never_produces_a_bundle(self):
        import io
        body={'status':'completed','output':[{'content':[{'type':'refusal','refusal':'No'}]}]}
        with patch.dict(os.environ,{'OPENAI_API_KEY':'test-only'}),patch.object(p.urllib.request,'urlopen',return_value=io.BytesIO(json.dumps(body).encode())):
            with self.assertRaisesRegex(ValueError,'refusal'):
                p.response({})

class ContentSafetyTests(unittest.TestCase):
    def test_svg_script_entities_external_resources_rejected(self):
        good='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect width="10" height="10"/></svg>'
        self.assertEqual(v.validate_svg(good),'0 0 10 10')
        for attack in ['<script>bad()</script>','<image href="https://example.com"/>','<rect onclick="bad()"/>','<style>url(https://example.com)</style>']:
            with self.assertRaises(ValueError):
                v.validate_svg(good.replace('<rect width="10" height="10"/>',attack))
        with self.assertRaises(ValueError):
            v.validate_svg('<!DOCTYPE svg [<!ENTITY x SYSTEM "file:///etc/passwd">]>'+good)
    def test_broken_relative_link_and_height_are_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp,'README.md').write_text('[missing](missing.md)\n<img src="missing.svg" width="800" height="500">')
            result,_=v.local_checks(tmp,['README.md'])
            self.assertTrue(any('broken local link' in e for e in result['local_errors']))
            self.assertTrue(any('dimensions' in e for e in result['local_errors']))
    def test_private_network_and_credentials_not_fetched(self):
        for url in ['file:///etc/passwd','http://user:pass@example.com','http://127.0.0.1','http://169.254.169.254']:
            with self.assertRaises(ValueError):
                v.public_url(url)

if __name__=='__main__':
    unittest.main()
