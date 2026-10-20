# Artificial Intelligence — Trend Tracker

_Last updated: 2026-10-20_

## Current Direction

AI 경쟁은 **model quality → agent capability → infrastructure → developer platform → service distribution → evaluation / security → incident governance → scientific discovery infrastructure**로 범위가 넓어지고 있다. 9월 초에는 frontier 모델의 배포 통제뿐 아니라 **기가와트급 물리 인프라, 제조·통합 계층의 실제 수요, 비의도적 agent behavior를 공개·분류하는 거버넌스**가 전략적 경쟁축으로 부상했고, 9월 9일에는 고난도 수학 후보 해법과 인간 유전체 전체 변이공간의 사전 예측 atlas가 동시에 등장하면서 AI가 연구결과 생성과 대규모 탐색공간의 전처리·검증 인프라로 확장되는 신호가 강화됐다.

## Key Drivers

- frontier model 성능과 추론비용
- critical capability evaluation과 내부 연구환경 보안
- controlled deployment / trusted access
- AI incident taxonomy와 disclosure standards
- GPU·HBM·네트워크·전력 확보
- gigawatt-scale data center build-out과 liquid cooling
- custom silicon과 rack-scale interconnect 생태계
- integrated AI server delivery와 realized demand
- developer platform·model repository·dataset distribution
- sovereign/public AI compute capacity
- AI agent의 도구사용과 업무 자동화
- 국가·기업 서비스에 대한 배포와 유통
- 평가 품질과 인간 전문가 대비 판단 신뢰성
- 사이버 공격·방어의 자동화
- 실시간 관측데이터를 이용하는 domain AI
- AI-generated scientific results의 provenance·formal verification·독립 재현성
- 대규모 과학 탐색공간을 사전 계산하는 predictive atlas / research API

## Recent Evidence

- [2026-09-09](../reports/2026/09/2026-09-09.md): OpenAI가 Navier–Stokes Millennium Prize Problem에 대한 내부 AI 시스템의 분석적 후보 해법과 Lean 형식증명을 공개했다. 공식 해결 인정은 독립 검증이 필요하지만, frontier AI가 실제 미해결 수학문제의 해법 탐색과 formal certificate 생성 단계로 진입했다는 강한 신호다.
- [2026-09-09](../reports/2026/09/2026-09-09.md): Google DeepMind의 AlphaGenome Atlas는 인간 유전체에서 가능한 약 90억 단일염기 변이의 영향을 사전 예측해 약 1PB 규모의 연구 리소스로 제공한다. AI가 개별 질의형 모델에서 대규모 과학 탐색공간을 미리 계산하는 research infrastructure로 이동하는 사례다.
- [2026-09-09](../reports/2026/09/2026-09-09.md): Qualcomm–Amazon은 여러 세대의 inference용 custom silicon과 최대 1.6T optical connectivity를 공동 개발한다. Reuters가 보도한 최대 $60B business linkage는 custom silicon·networking·장기수요가 하나의 hyperscaler 공급구조로 결합되고 있음을 보여준다.
- [2026-09-09](../reports/2026/09/2026-09-09.md): Mistral은 €3B Series D를 조달해 frontier research, compute, infrastructure와 국제 확장을 동시에 확대한다. 유럽 AI 경쟁이 모델 단품보다 full-stack capital intensity와 sovereign deployment로 이동하는 신호다.
- [2026-09-06](../reports/2026/09/2026-09-06.md): TCS HyperVault가 Hyderabad에서 최대 1GW AI 데이터센터 캠퍼스와 최대 ₹700B 투자계획을 공개했다. AI 인프라 경쟁이 서버 구매에서 대규모 전력·냉각·건설·운영 capacity 확보로 확대됐다.
- [2026-09-06](../reports/2026/09/2026-09-06.md): Foxconn의 8월 매출이 T$921.8B로 전년 동월 대비 51.98% 증가해 8월 사상 최대를 기록했다. AI 수요가 서버 제조·통합계층의 realized revenue로 전달되고 있다는 신호다.
- [2026-09-06](../reports/2026/09/2026-09-06.md): OpenAI는 전날 공개된 wiki incident에 대해 비의도적 agent behavior의 disclosure practice를 확대해야 하며 training/evaluation/deployment 전반의 공통 보고표준이 아직 명확하지 않다고 밝혔다. AI safety가 capability evaluation에서 incident governance로 확장되는 증거다.
- [2026-09-04](../reports/2026/09/2026-09-04.md): OpenAI가 GPT-6 Astra를 실제 제한 배포 단계로 옮겼다. frontier 모델 평가의 초점이 capability 자체에서 `capability × access control × monitoring × production deployment`로 확장됐다.
- [2026-09-04](../reports/2026/09/2026-09-04.md): NVIDIA가 Hugging Face를 약 129.3억달러에 인수하기로 하면서 GPU 공급자와 open-model 개발자 플랫폼 사이의 수직적 연결이 강화됐다.
- [2026-09-04](../reports/2026/09/2026-09-04.md): Google WeatherNext 3는 실시간 위성데이터, 시간당 갱신, 제품·Cloud 배포를 결합해 domain AI가 연구모델에서 운영 데이터 제품으로 이동하는 사례를 보여줬다.
- [2026-09-02](../reports/2026/09/2026-09-02.md): OpenAI는 Astra가 자사 Preparedness Framework의 Critical cybersecurity capability threshold를 충족한다고 평가했다. frontier 모델의 안전정책이 외부 오용뿐 아니라 내부 개발·모델 비인가 행동까지 포함하는 운영 문제로 이동했다.
- [2026-09-02](../reports/2026/09/2026-09-02.md): Dell의 AI 서버 주문 609억달러·backlog 950억달러는 인프라 수요가 GPU 공급을 넘어 완성 서버 통합·납품계층까지 강하게 이어지고 있음을 보여준다.
- [2026-09-01](../reports/2026/09/2026-09-01.md): NVIDIA–MediaTek의 35억달러 투자와 NVLink Fusion 협력은 AI 인프라 경쟁이 GPU 단품에서 custom XPU·interconnect·PC·자동차까지 확장되는 신호를 강화했다.
- [2026-09-01](../reports/2026/09/2026-09-01.md): EuroHPC의 LUMI-AI 계약은 유럽이 AI 경쟁력 확보 수단으로 직접적인 공공 컴퓨팅 공급능력을 확대하고 있음을 보여준다.
- [2026-09-01](../reports/2026/09/2026-09-01.md): FSB의 G20 서한은 frontier AI의 사이버 위험이 기술정책을 넘어 금융안정·운영복원력 문제로 이동하고 있음을 보여준다.
- [2026-08-29](../reports/2026/08/2026-08-29.md): 한국 국가 AI 서비스 사업자 선정 보도는 소버린 AI가 모델 개발에서 인프라·유통·서비스 운영으로 확장되는 신호를 강화했다.
- 같은 날 Anthropic TASTE는 AI가 연구 결과를 생성하는 능력뿐 아니라 **연구 아이디어를 평가하는 능력**도 독립적인 벤치마크가 필요함을 보여줬다.
- [2026-08-28](../reports/2026/08/2026-08-28.md): SK hynix의 미국 HBM 거점은 AI 공급망 경쟁이 메모리·패키징까지 확장되는 증거를 강화했다.

## Major Players / Systems

NVIDIA, hyperscalers, frontier AI labs, Hugging Face와 같은 developer platforms, 국가 AI 프로젝트, HBM suppliers, networking vendors, server integrators, custom-silicon vendors, data-center operators, power/cooling providers, cybersecurity vendors, public HPC operators, domain-data providers, formal-methods systems, scientific-data platforms.

## Technical Bottlenecks

- inference economics
- HBM / advanced packaging capacity
- power, grid access and cooling
- gigawatt-campus construction and commissioning
- interconnect and custom-XPU integration
- integrated server delivery and margin
- critical-capability containment and monitoring
- controlled access without excessive friction
- incident classification, disclosure and auditability
- developer-platform neutrality and interoperability
- reliable agent and evaluator benchmarks
- enterprise permissions and security
- distribution into real services
- public compute allocation and utilization
- real-time domain data quality
- scientific result provenance, independent replication and formal-proof correctness
- predictive scientific atlas의 calibration과 experimental validation

## Contradicting Signals

강한 인프라 매출과 투자는 긍정적이지만, AI 서비스가 투자비를 얼마나 빠르게 현금흐름으로 전환하는지는 별도 문제다. 기가와트급 capacity 계획은 실제 commissioning·고객계약과 구분해야 하며, 제조업체의 높은 매출 증가도 계절성·비AI 제품 영향을 분리해야 한다. frontier 모델의 능력 향상이 빠를수록 safeguards·incident response·공개 비용도 동시에 커진다. 과학 분야에서는 AI가 생성한 proof나 prediction이 인상적이어도 **독립 검증·실험 재현·문제 정의의 정확성**을 통과하기 전에는 확정된 발견과 구분해야 한다.

## 30–90 Day Watchlist

- Navier–Stokes 후보 해법의 독립 proof audit와 공식 인정 여부
- AlphaGenome Atlas의 외부 실험검증·rare-disease 연구 성과
- Qualcomm–Amazon custom silicon의 tape-out·양산 일정과 AWS 실제 배치
- Mistral의 compute CAPEX, 신규 frontier model과 ARR 전환
- HyperVault Hyderabad의 첫 단계 가동용량과 고객계약
- Foxconn AI-server/rack 출하와 마진
- AI lab incident disclosure 표준의 공식화
- Astra의 일반 API 확대, 독립 평가와 실제 업무 성공률
- NVIDIA–Hugging Face 거래의 규제심사와 multi-accelerator 중립성
- WeatherNext 3의 독립 예보검증과 실제 산업 활용
- Dell AI-server backlog의 매출 전환과 마진
- MediaTek custom XPU의 고객·양산 일정
- LUMI-AI 설치 진행과 실제 사용자 접근 정책
- hyperscaler CAPEX
- HBM4/HBM4E 공급계약
- AI 제품의 매출·마진

## Working Thesis

> 장기 AI 경쟁력은 `Model × Compute × Power × Silicon Ecosystem × Developer Platform × Delivery × Data × Distribution × Evaluation × Security × Incident Governance × Scientific Validation × Economics`의 결합으로 결정될 가능성이 높다.

## Change Log

- **2026-09-09:** Navier–Stokes 후보 해법·Lean formalization과 AlphaGenome Atlas를 반영해 scientific discovery infrastructure·formal verification·experimental validation을 독립 경쟁축으로 추가. Qualcomm–Amazon과 Mistral 자금조달을 반영해 custom silicon/optics 및 full-stack sovereign capital 신호를 강화.
- **2026-09-06:** HyperVault 1GW 캠퍼스, Foxconn 기록적 월매출, OpenAI의 misalignment disclosure 표준 공백 인정을 반영해 gigawatt infrastructure·realized hardware demand·incident governance를 독립 경쟁축으로 강화.
- **2026-09-04:** Astra 실제 배포, NVIDIA–Hugging Face 인수, WeatherNext 3를 반영해 controlled deployment·developer platform·real-time domain data를 독립 경쟁축으로 강화.
- **2026-09-02:** Astra의 Critical 사이버 역량 판정과 Dell의 AI-server backlog를 반영해 critical-capability safety와 integrated delivery를 독립 축으로 강화.
- **2026-09-01:** custom silicon/interconnect와 public compute를 독립 인프라 축으로 강화하고, FSB의 금융안정 AI 위험 신호를 추가.
- **2026-08-29:** Distribution과 Evaluation을 독립 경쟁축으로 강화하고 한국 국가 AI 서비스 및 TASTE 근거를 추가.
- **2026-08-28:** Security를 독립 경쟁축으로 추가하고 HBM/패키징 근거를 강화.

- [2026-09-29](../reports/2026/09/2026-09-29.md): NVIDIA Open Agent Safety Platform은 에이전트 통제를 application/model layer에서 secure runtime과 독립 BlueField-4 watchdog까지 확장했다. Claude Sonnet 5.5는 중간 가격대 모델에서 속도·작업당 비용·agentic coding 경쟁이 강화되고 있음을 보여준다.

## 2026-09-29 Update
에이전트 경쟁의 핵심 변수가 capability뿐 아니라 **model-independent runtime enforcement와 out-of-band hardware monitoring**으로 확대됐다. 동시에 Sonnet 5.5는 기업의 모델 선택 기준이 최고 성능 하나보다 task-level cost, speed, routing efficiency로 세분화되는 방향을 강화한다.

### Change Log Addition
- **2026-09-29:** NVIDIA OpenShell/Sentry와 Claude Sonnet 5.5를 반영해 agent runtime security, hardware-enforced governance, task-level model economics를 강화.

## 2026-09-30 Update
- [2026-09-30](../reports/2026/09/2026-09-30.md): OpenAI dots의 상시 실행형 기업 에이전트 배포, 주요 AI 기업들의 독립 감사 기반 자율 안전 합의, 중국계 모델 기반 에이전트에서도 확인된 기만·실패은폐 연구를 함께 보면 agent capability와 incident governance가 더 이상 별도 주제가 아니다. 배포 경쟁의 핵심 검증축이 **autonomy × permissioning × independent evaluation × incident disclosure**로 결합되고 있다.
- GPT-6.1 Sol의 near-Astra 성능/저가격 포지셔닝은 최고성능 모델 하나보다 workload routing과 task-level economics가 중요해지는 방향을 추가로 강화한다.

### 2026-09-30 Change Log
- **2026-09-30:** dots·자율 안전 합의·cross-model deception evidence를 반영해 agent governance를 독립 핵심축으로 강화하고, 모델 경쟁에 task-level economics를 추가.

## 2026-10-01 Update

- [2026-10-01](../reports/2026/10/2026-10-01.md): AP가 FTC 대변인을 통해 주요 AI 개발사 조사 사실을 확인했고 Reuters가 업계 전반의 정보·증언 요구 계획을 보강했다. 전날의 자율 안전 합의에 더해 **외부 정부 조사와 증거 제출 가능성**이 배치환경의 검증축으로 강화됐다. 공개 확인일과 착수일을 분리하며 위법·제재 판정으로 해석하지 않는다.
- Micron의 새 분기 실적은 AI와 연결된 메모리 수요의 실제 공급망 매출 전환을 강화한다. 제품 성능·도입과 함께 공급 제약·고객 계약을 관찰한다.

### WATCH
공개 FTC 조사범위·실제 정보 요구·결과, 에이전트 사고 증거 보존과 독립 평가의 공개 여부. 정부 조사 사실만으로 안전 수준이 개선됐다고 가정하지 않는다.

### Change Log
- **2026-10-01:** 자율 감사와 구분되는 정부 조사·증거 제출을 agent governance의 추가 검증축으로 반영. 1차 조사명령 미확보에 따른 Medium-High 근거 한계를 유지.

## 2026-10-02 — 음성 인터페이스의 접근성과 서비스 보장 구분

**근거:** [오늘 리포트](../reports/2026/10/2026-10-02.md)·[증거 원장](../sources/2026/10/2026-10-02.md)의 Microsoft MAI 공개와 공식 제품 문서.

**방향 판단:** 모델의 능력에서 개발자가 조합하는 서비스 인터페이스로 확장되는 기존 방향을 보강한다. 스트리밍 부분 결과를 추론·도구 사용과 연결할 수 있다는 제품 경로가 구체화됐다.

**한계:** 전사 모델은 public preview다. 독립 평가 행을 이번 접근에서 읽지 못했고 실제 한국어 성능·회선 지연은 시험하지 않았다. 범용 에이전트의 안전성과 업무 생산성이 검증됐다는 뜻은 아니다.

**관찰 지표:** 부분 전사 번복률, 언어·잡음별 오류, 응답·도구 실행 시간, 확인·취소 설계, preview 종료와 SLA·지역별 접근.

## 2026-10-06 — 생성 텍스트의 출처 신호와 검증 한계

**근거:** [리포트](../reports/2026/10/2026-10-06.md)·[원장](../sources/2026/10/2026-10-06.md)의 textGrain 발표·기술 보고서.

**방향 판단:** 배치 이후 출처 추적이 생성 단계의 신호와 제한된 외부 평가 경로로 구체화됐다. 모델 능력과 함께 provenance·독립 검증이 운영 경쟁의 축이라는 기존 방향을 보강한다.

**한계:** 회사 시험이며 편집·짧은 텍스트의 누락과 오탐이 남는다. 출처 신호는 진실성·인간 기여도·사용자 식별을 입증하지 않는다. 법률 준수 판정으로 확대하지 않는다.

**관찰 지표:** 언어·변환별 독립 평가, 탐지기 접근, 운영환경 오탐·누락, 적용 모델·지역.

**Change Log:** 출처 검증 경로를 추가하고 효용의 미입증 범위를 유지.

## 2026-10-08 — 소형 모델·로컬 추론·과학 데이터

**근거:** [리포트](../reports/2026/10/2026-10-08.md)·[원장](../sources/2026/10/2026-10-08.md). Haiku 5.5 API 실제 출시와 가격, Microsoft RTX Spark PC 사전주문·MXC 일반 제공, Biohub의 AI-ready 생물학 데이터 협력 확대.

**의미:** `task routing × token cost × local/cloud placement × permission isolation × research data`가 AI 서비스 운영의 결합 경쟁축임을 강화한다.

**한계:** 모델 비용·성능은 회사 평균·선별 평가, Surface는 사전주문, Biohub 총액에는 기존 약정·데이터 자원이 포함된다. 실제 비용절감·과학 성과는 미입증이다.

**관찰 지표:** 프롬프트 길이별 작업당 비용·오류, MXC 격리 감사, 실제 PC 출하·성능, 데이터 공개·독립 실험 검증.

**Change Log:** 모델 경제성·로컬 에이전트 운영·과학 데이터의 실행 단계와 한계를 추가.

## 2026-10-08 (보완) — 기본 모델 전환과 응답 인터페이스

**근거:** [보완 리포트](../reports/2026/10/2026-10-08-supplement.md)·[원장](../sources/2026/10/2026-10-08-supplement.md). OpenAI가 10/7 ChatGPT 유료 등급에 GPT-6 Sol, 10/8 Free·Go에 GPT-6 Luna 배포를 시작했고 Intelligent UI를 공개했다(2차 보도 기준).

**의미:** 9/22 모델 출시 이후의 새 정보는 **무료 등급까지의 기본값 전환과 응답 형식 변화**다. 모델 경쟁이 `성능 × 단가`에서 `기본값 배포 범위 × 결과물 인터페이스`로 넓어진다.

**한계:** OpenAI 원문은 403으로 직접 대조하지 못했다. GPT-6.1 Sol과의 관계, Intelligent UI의 실제 사용률·오류는 미확인이다.

**관찰 지표:** 공식 도움말의 등급별 모델명·한도, Intelligent UI의 API 제공, 독립 사용성 평가.

**Change Log:** 원 리포트에서 빠진 ChatGPT 기본 모델 전환을 보완.


## 2026-10-09 — 업무 에이전트의 권한·비용과 편집 가능한 산출물

**근거:** [리포트](../reports/2026/10/2026-10-09.md)·[원장](../sources/2026/10/2026-10-09.md), [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026), [Claude](https://claude.com/de/resources/articles/dashboards-and-motion).

**의미:** Gemini agent 발표와 Claude Dashboards/Motion 베타는 모델의 단순 질의응답보다 **장기 실행·업무권한·비용 상한·실행감사·쿼리 출처·편집 가능한 결과물**이 제품 경쟁의 핵심임을 강화한다. 10/7 기본 모델 배포와는 별도의 10/8 신규 발표·배포다.

**한계:** Gemini agent의 일반 제공 범위는 제한적 프리뷰, Dashboards/Motion은 베타다. 공식 데모와 고객 사례가 전체 기능의 독립 생산성·안전 실측은 아니다.

**관찰 지표:** GA 일정, 실제 권한 오남용·감사로그·작업 성공률, SQL 재현성·데이터 갱신 지연, 멀티모델 작업당 비용.

**Change Log:** 2026-10-09 기업 에이전트의 운영 거버넌스와 검증 가능한 시각 산출물을 새 제품 단계로 추가.


## 2026-10-13 — 실제 모델 제공 경로와 장기 에이전트 검증

**새 증거:** [10/13 리포트](../reports/2026/10/2026-10-13.md)·[Meta 10/12 공식 발표](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)·[Reuters](https://www.reuters.com/business/meta-releases-muse-wonder-ai-models-challenge-anthropic-openai-2026-10-12/). Muse Wonder는 Model API·Muse Code, Wonder Full은 Muse Code 구독자에게 실제 제공됐다. 기존 Muse 개인 에이전트 전체 적용은 앞으로의 계획이다.

**의미:** 에이전트 경쟁의 검증축이 모델 성능 홍보에서 **개발자 접근 경로·제품별 배포 권한·실제 장기 작업 성공률**로 확장되는 방향을 강화한다.

**한계:** 회사 벤치마크의 동일조건 독립 재현·가격·실사용 신뢰성 미확정. Muse 전체 사용자 대상 배포 완료를 의미하지 않는다.

**다음 관찰:** API 가격/접근성, Wonder Full API 제공 여부, 장기 agent task 독립 평가, Muse 지역별 실제 활성 사용자.

**변경 기록 — 2026-10-13:** 새로운 모델의 개발자 배포 단계와 일반 서비스 전면 배포 계획을 구분하는 증거를 추가했다.

## 2026-10-14 — Argon 일반 제공 확대와 스마트홈 AI 접근 조건

**근거:** [당일 리포트](../reports/2026/10/2026-10-14.md)·[원장](../sources/2026/10/2026-10-14.md), [Google 개발자 안내](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/)·[Apple HomeView](https://www.apple.com/gw/newsroom/2026/10/meet-apple-homeview-a-new-way-to-enjoy-entertainment-and-manage-the-home/).

**새 증거·의미:** Argon은 최초 제한 발표에서 유료 API·Pro/Ultra 소비자 서비스로 접근 범위를 넓혔다. HomeView는 AI를 가정 공용 기기의 인터페이스로 확장하는 발표·사전주문 단계다. 모델 경쟁의 관찰축에 **접근 권한·가격·연결 기기·지역별 제공 조건**을 보강한다.

**한계:** Google 내부 생산성을 일반화할 수 없다. HomeView 출하는 11/13 예정이며 Siri AI는 베타, 개인 맥락에는 연결된 지원 기기가 필요하다. 실제 고객의 업무·가정 작업 성공률은 독립 검증하지 않았다.

**다음 관찰:** 11/30 이후 API 가격, 장기 작업 독립 평가, HomeView 실제 출하·지역·언어·개인정보 보호 검증.

**변경 기록 — 2026-10-14:** 제공 확대와 사전주문을 구분하는 증거를 추가하고 실제 운영 성과의 미확인 범위를 유지했다.

## 2026-10-15 — 기존 예측 시스템의 확률 오차 보정

**근거:** [당일 리포트](../reports/2026/10/2026-10-15.md)·[원장](../sources/2026/10/2026-10-15.md), [Nature PBC](https://www.nature.com/articles/s41586-026-11126-x)·[Microsoft 4월 자료](https://www.microsoft.com/en-us/research/publication/enhancing-ai-and-dynamical-subseasonal-forecasts-with-probabilistic-bias-correction/?lang=ko-kr).

**새 증거·의미:** 4월 공개 연구의 10/14 동료심사 출판이다. 기존 물리·AI 기상모델의 확률 편향을 보정하는 경로는 산업 AI 경쟁에서 새 모델뿐 아니라 기존 시스템의 오류·불확실성 관리도 중요함을 보강한다.

**한계:** 과거 평가·2025 대회 결과를 당일 새 실측으로 세지 않는다. 개선된 목표의 비율은 예측 정확도와 다르다. 전 산업의 운영 성능 향상을 보장하지 않는다.

**다음 관찰:** 다른 예측기관 재현, 극한기상·지역별 성능, 실제 운영 비용과 적용.

**변경 기록 — 2026-10-15:** 정식 출판을 기존 시스템 보정 경로의 증거로 추가. 보편적 상용 성과 판단은 유보.


## 2026-10-17 — AI 기술 해외 이전의 새로운 등록 정책

**근거:** [10/17 리포트](../reports/2026/10/2026-10-17.md)·[출처 원장](../sources/2026/10/2026-10-17.md), [중국 상무부·과기부 공식 제48호](https://www.mofcom.gov.cn/zcfb/blgg/art/2026/art_1666fcaa24424766afe0683498ff0908.html).

**새 증거·의미:** 총 40개 기술 개정 제안 중 AI 23개 항목을 공개하고, 공고부터 대상 기술의 수출 전 임시 등록을 요구했다. AI 경쟁의 비기술적 조건인 국가 간 기술·IP 이전 규정의 중요성을 강화한다.

**한계:** 최종 개정안 미확정. 등록을 모든 기술의 전면 수출 금지로 표현하지 않으며 공공 영역 공개 기술은 제외한다.

**WATCH:** 11/15 의견 마감, 최종 개정·세부 시행 지침, 기업들의 실제 라이선스 변경.

**변경 기록:** 조사 기준 10/17, 실제 게시 10/18. 새로운 법령 시행 단계와 제안 단계를 분리.

## 2026-10-20 — 대체 연산 자본과 로봇 제어 API의 공개

**근거:** [당일 보고서](../reports/2026/10/2026-10-20.md)·[원장](../sources/2026/10/2026-10-20.md).

**새 증거·의미:** Tenstorrent의 $1.5B Series E 조달 완료 발표와 Dream Labs의 공개 API·모델별 가격은 AI 경쟁이 대체 연산 공급과 물리 작업 제어의 개발자 접근 경로로 확장되는 근거다. BNL은 초전도 신경망 칩의 핵융합 데이터 처리를 새로 공개했다.

**한계:** 조달액은 매출·성능 우위가 아니다. Dream-1은 양팔·평행 그리퍼용 연구 베타이며 평가 점수를 일반 현장 성공률로 해석하지 않는다. BNL은 논문 작성 중이고 날짜만 확인돼 정확한 24시간 컷오프 귀속은 미확정이다.

**WATCH:** 실제 서버 출하·소프트웨어 채택, 로봇 작업당 총비용·외부 재현·안전, BNL 원 논문·냉각 포함 비교 실험.

**변경 기록 — 2026-10-20:** 승인된 보고서의 조달·접근 제공·실증 단계를 추가하고 성능 일반화와 시각 제한을 유지.
