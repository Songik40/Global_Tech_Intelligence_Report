#!/usr/bin/env python3
"""Read-only repository/content/link checks. HTTP reachability is not fact verification."""
import argparse
import concurrent.futures
import datetime as dt
import hashlib
import html
from html.parser import HTMLParser
import ipaddress
import json
from pathlib import Path
import re
import socket
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

KST = dt.timezone(dt.timedelta(hours=9))
MARKER = '<!-- deterministic-post-publication-verification:v1 -->'

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')

def public_url(url):
    p = urllib.parse.urlsplit(url)
    if p.scheme not in ('https', 'http') or not p.hostname or p.username or p.password:
        raise ValueError('Only public HTTP(S) URLs without credentials are allowed')
    if p.port and p.port not in (80, 443):
        raise ValueError('Unsupported URL port')
    addresses = socket.getaddrinfo(p.hostname, p.port or (443 if p.scheme == 'https' else 80))
    if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global for a in addresses):
        raise ValueError('Non-public destination rejected')

class Redirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        public_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def check_url(url):
    result = {'url': url, 'checked_at_utc': now()}
    try:
        public_url(url)
        req = urllib.request.Request(url, headers={'User-Agent': 'GlobalTechReport-LinkVerifier/1.0'})
        with urllib.request.build_opener(Redirect()).open(req, timeout=18) as r:
            body = r.read(2_000_000)
            result.update(status=r.status, final_url=r.url, body_sha256=hashlib.sha256(body).hexdigest())
            text = body.decode('utf-8', errors='replace')
            title = re.search(r'<title[^>]*>(.*?)</title>', text, re.S | re.I)
            result['title'] = html.unescape(re.sub(r'\s+', ' ', title[1])).strip() if title else ''
            result['result'] = 'redirect' if r.url != url else 'reachable'
            if re.search(r'^(access denied|just a moment|robot or human|404|page not found|error)', result['title'], re.I):
                result['result'] = 'blocked_or_error_page'
    except urllib.error.HTTPError as e:
        result.update(status=e.code, final_url=e.url, result='blocked' if e.code in (401, 403, 429) else 'http_error')
    except Exception as e:
        result.update(result='unavailable', error=str(e)[:200])
    return result

class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.unsafe = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            self.images.append(attrs)
        if tag in ('script', 'iframe', 'object', 'embed', 'form') or any(k.lower().startswith('on') for k in attrs):
            self.unsafe.append(tag)

def links(text):
    return set(re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text)) | set(re.findall(r'(?:src|href)=["\']([^"\']+)["\']', text))

def validate_svg(text):
    if '<!DOCTYPE' in text.upper() or '<!ENTITY' in text.upper():
        raise ValueError('SVG entities are not allowed')
    root = ET.fromstring(text)
    if root.tag != '{http://www.w3.org/2000/svg}svg' or not root.get('viewBox'):
        raise ValueError('SVG namespace/viewBox missing')
    for node in root.iter():
        if node.tag.split('}')[-1].lower() in ('script', 'foreignobject', 'image', 'use', 'a', 'style'):
            raise ValueError('Active or external SVG content rejected')
        for key, value in node.attrib.items():
            if key.lower().startswith('on') or 'href' in key.lower() or 'url(' in value.lower():
                raise ValueError('Active/external SVG attribute rejected')
    return root.get('viewBox')

def local_checks(root, paths):
    root = Path(root).resolve()
    errors, images, external, files = [], [], set(), []
    for path in paths:
        file = root / path
        if not file.is_file() or not file.resolve().is_relative_to(root):
            errors.append(f'Missing/unsafe path: {path}')
            continue
        data = file.read_bytes()
        files.append({'path': path, 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)})
        text = data.decode('utf-8')
        if path.endswith('.svg'):
            try:
                images.append({'path': path, 'viewBox': validate_svg(text)})
            except (ValueError, ET.ParseError) as e:
                errors.append(f'{path}: {e}')
            continue
        if '\\n' in text and path in ('README.md', 'reports/README.md'):
            errors.append(f'{path}: literal backslash-n in index')
        parser = Images()
        parser.feed(text)
        if parser.unsafe:
            errors.append(f'{path}: unsafe HTML {parser.unsafe}')
        if re.search(r'!\[[^\]]*\]\(', text):
            errors.append(f'{path}: image must use explicit width-only HTML')
        for img in parser.images:
            width = img.get('width', '')
            if 'height' in img or not width.isdigit() or not any(a <= int(width) <= b for a, b in [(120,240),(320,360),(720,760),(760,820)]):
                errors.append(f'{path}: invalid image dimensions {img}')
            images.append({'path': path, 'image': img})
        for url in links(text):
            p = urllib.parse.urlsplit(html.unescape(url))
            if p.scheme in ('https', 'http'):
                external.add(urllib.parse.urldefrag(html.unescape(url))[0])
            elif p.scheme:
                errors.append(f'{path}: unsupported link scheme {p.scheme}')
            elif p.path:
                dest = (file.parent / urllib.parse.unquote(p.path)).resolve()
                if not dest.is_relative_to(root) or not dest.exists():
                    errors.append(f'{path}: broken local link {url}')
    return {'files': files, 'local_errors': errors, 'images': images}, external

def verify(root, paths, repo=None, sha=None, external=True):
    result, urls = local_checks(root, paths)
    result.update(started_at_utc=now(), head=sha)
    if repo and sha:
        def remote(path):
            req = urllib.request.Request(f'https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(path)}', headers={'User-Agent':'GlobalTechReport/1.0'})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read(2_000_000)
            return {'path':path, 'matches':data == (Path(root)/path).read_bytes(), 'remote_sha256':hashlib.sha256(data).hexdigest()}
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            result['remote_files'] = list(pool.map(remote, paths))
        for f in result['remote_files']:
            if not f['matches']:
                result['local_errors'].append(f"Remote mismatch: {f['path']}")
    if external:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            result['external_links'] = list(pool.map(check_url, sorted(urls)))
    result['finished_at_utc'] = now()
    return result

def ledger_log(result):
    stamp = dt.datetime.fromisoformat(result['finished_at_utc']).astimezone(KST).isoformat()
    out = [f'\n\n## Post-publication review ({stamp[:10]})', '', MARKER, '',
           f'- 실제 검증 완료: **{stamp} KST / {result["finished_at_utc"]} UTC**.',
           f'- 검증한 원격 main 콘텐츠 커밋: `{result["head"]}`.',
           f'- 원격 파일 {len(result.get("remote_files", []))}개를 다시 내려받아 UTF-8 원문과 SHA-256을 대조했다.',
           f'- 내부 경로·SVG XML·본문 이미지 표시 폭 점검 결과: **오류 {len(result["local_errors"])}개**.',
           '- 외부 URL은 GET 요청의 HTTP 상태·최종 URL·페이지 제목을 기록했다. HTTP 200은 사실의 진위나 기사 전체 열람을 보장하지 않는다. 접근 제한은 검증 성공으로 계산하지 않는다.', '',
           '| 파일 | 원격 내용 대조 | SHA-256 |', '|---|---|---|']
    for f in result['files']:
        matches = next((r['matches'] for r in result.get('remote_files', []) if r['path']==f['path']), None)
        out.append(f'| `{f["path"]}` | {"일치" if matches else "미확인/불일치"} | `{f["sha256"]}` |')
    out += ['', '| 외부 URL | 결과 | 최종 URL·제목/제한 |', '|---|---|---|']
    for r in result.get('external_links', []):
        detail = (r.get('final_url','')+' '+r.get('title',r.get('error',''))).replace('|','/')
        out.append(f'| {r["url"]} | {r["result"]} {r.get("status", "")} | {detail} |')
    if result['local_errors']:
        out += ['', '검증 오류:', *['- '+e for e in result['local_errors']]]
    out += ['', '- 이 기록은 위 콘텐츠 커밋에 대한 완료형 점검이다. 이 기록 자체를 추가한 후 최종 HEAD·원장 내용을 별도로 재조회해야 발행 완료를 선언한다.', '']
    return '\n'.join(out)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--root', default='.')
    p.add_argument('--paths', nargs='+', required=True)
    p.add_argument('--repo')
    p.add_argument('--sha')
    p.add_argument('--output', required=True)
    p.add_argument('--no-external', action='store_true')
    args = p.parse_args()
    result = verify(args.root,args.paths,args.repo,args.sha,not args.no_external)
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'head':args.sha,'files':len(result['files']),'errors':result['local_errors'],'links':len(result.get('external_links',[]))},ensure_ascii=False))
    raise SystemExit(bool(result['local_errors']))
