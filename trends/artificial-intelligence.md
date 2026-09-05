# Artificial Intelligence — Trend Tracker

_Last updated: 2026-09-06_

## Current Direction

AI 경쟁은 **model quality → agent capability → infrastructure → developer platform → service distribution → evaluation / security → incident governance**로 범위가 넓어지고 있다. 9월 초에는 frontier 모델의 배포 통제뿐 아니라 **기가와트급 물리 인프라, 제조·통합 계층의 실제 수요, 비의도적 agent behavior를 공개·분류하는 거버넌스**까지 전략적 경쟁축으로 부상했다.

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

## Recent Evidence

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

NVIDIA, hyperscalers, frontier AI labs, Hugging Face와 같은 developer platforms, 국가 AI 프로젝트, HBM suppliers, networking vendors, server integrators, custom-silicon vendors, data-center operators, power/cooling providers, cybersecurity vendors, public HPC operators, domain-data providers.

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

## Contradicting Signals

강한 인프라 매출과 투자는 긍정적이지만, AI 서비스가 투자비를 얼마나 빠르게 현금흐름으로 전환하는지는 별도 문제다. 기가와트급 capacity 계획은 실제 commissioning·고객계약과 구분해야 하며, 제조업체의 높은 매출 증가도 계절성·비AI 제품 영향을 분리해야 한다. frontier 모델의 능력 향상이 빠를수록 safeguards·incident response·공개 비용도 동시에 커진다.

## 30–90 Day Watchlist

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
- AI agent 실제 업무 성공률
- AI 제품의 매출·마진

## Working Thesis

> 장기 AI 경쟁력은 `Model × Compute × Power × Silicon Ecosystem × Developer Platform × Delivery × Data × Distribution × Evaluation × Security × Incident Governance × Economics`의 결합으로 결정될 가능성이 높다.

## Change Log

- **2026-09-06:** HyperVault 1GW 캠퍼스, Foxconn 기록적 월매출, OpenAI의 misalignment disclosure 표준 공백 인정을 반영해 gigawatt infrastructure·realized hardware demand·incident governance를 독립 경쟁축으로 강화.
- **2026-09-04:** Astra 실제 배포, NVIDIA–Hugging Face 인수, WeatherNext 3를 반영해 controlled deployment·developer platform·real-time domain data를 독립 경쟁축으로 강화.
- **2026-09-02:** Astra의 Critical 사이버 역량 판정과 Dell의 AI-server backlog를 반영해 critical-capability safety와 integrated delivery를 독립 축으로 강화.
- **2026-09-01:** custom silicon/interconnect와 public compute를 독립 인프라 축으로 강화하고, FSB의 금융안정 AI 위험 신호를 추가.
- **2026-08-29:** Distribution과 Evaluation을 독립 경쟁축으로 강화하고 한국 국가 AI 서비스 및 TASTE 근거를 추가.
- **2026-08-28:** Security를 독립 경쟁축으로 추가하고 HBM/패키징 근거를 강화.
