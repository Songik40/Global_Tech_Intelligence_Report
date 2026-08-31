# Artificial Intelligence — Trend Tracker

_Last updated: 2026-09-01_

## Current Direction

AI 경쟁은 **model quality → agent capability → infrastructure → service distribution → evaluation / security**로 범위가 넓어지고 있으며, 최근에는 **custom silicon·interconnect·공공 컴퓨팅 공급**이 독립 경쟁축으로 더 선명해지고 있다.

## Key Drivers

- frontier model 성능과 추론비용
- GPU·HBM·네트워크·전력 확보
- custom silicon과 rack-scale interconnect 생태계
- sovereign/public AI compute capacity
- AI agent의 도구사용과 업무 자동화
- 국가·기업 서비스에 대한 배포와 유통
- 평가 품질과 인간 전문가 대비 판단 신뢰성
- 사이버 공격·방어의 자동화

## Recent Evidence

- [2026-09-01](../reports/2026/09/2026-09-01.md): NVIDIA–MediaTek의 35억달러 투자와 NVLink Fusion 협력은 AI 인프라 경쟁이 GPU 단품에서 custom XPU·interconnect·PC·자동차까지 확장되는 신호를 강화했다.
- [2026-09-01](../reports/2026/09/2026-09-01.md): EuroHPC의 LUMI-AI 계약은 유럽이 AI 경쟁력 확보 수단으로 직접적인 공공 컴퓨팅 공급능력을 확대하고 있음을 보여준다.
- [2026-09-01](../reports/2026/09/2026-09-01.md): FSB의 G20 서한은 frontier AI의 사이버 위험이 기술정책을 넘어 금융안정·운영복원력 문제로 이동하고 있음을 보여준다.
- [2026-08-29](../reports/2026/08/2026-08-29.md): 한국 국가 AI 서비스 사업자 선정 보도는 소버린 AI가 모델 개발에서 인프라·유통·서비스 운영으로 확장되는 신호를 강화했다.
- 같은 날 Anthropic TASTE는 AI가 연구 결과를 생성하는 능력뿐 아니라 **연구 아이디어를 평가하는 능력**도 독립적인 벤치마크가 필요함을 보여줬다.
- [2026-08-28](../reports/2026/08/2026-08-28.md): SK hynix의 미국 HBM 거점은 AI 공급망 경쟁이 메모리·패키징까지 확장되는 증거를 강화했다.

## Major Players / Systems

NVIDIA, hyperscalers, frontier AI labs, 국가 AI 프로젝트, HBM suppliers, networking vendors, custom-silicon vendors, data-center operators, cybersecurity vendors, public HPC operators.

## Technical Bottlenecks

- inference economics
- HBM / advanced packaging capacity
- power and cooling
- interconnect and custom-XPU integration
- reliable agent and evaluator benchmarks
- enterprise permissions and security
- distribution into real services
- public compute allocation and utilization

## Contradicting Signals

강한 인프라 매출과 투자는 긍정적이지만, AI 서비스가 투자비를 얼마나 빠르게 현금흐름으로 전환하는지는 별도 문제다. 공급자 또는 플랫폼 기업의 직접 금융이 늘어날수록 최종수요와 생태계 금융을 구분해야 한다. 평가에서도 모델이 생성 능력과 동일한 수준으로 전문가 판단을 재현한다고 가정할 수 없다.

## 30–90 Day Watchlist

- MediaTek custom XPU의 고객·양산 일정
- LUMI-AI 설치 진행과 실제 사용자 접근 정책
- FSB/G20의 AI 운영복원력 후속 기준
- hyperscaler CAPEX
- HBM4/HBM4E 공급계약
- AI agent 실제 업무 성공률
- AI 제품의 매출·마진

## Working Thesis

> 장기 AI 경쟁력은 `Model × Compute × Silicon Ecosystem × Data × Distribution × Evaluation × Security × Economics`의 결합으로 결정될 가능성이 높다.

## Change Log

- **2026-09-01:** custom silicon/interconnect와 public compute를 독립 인프라 축으로 강화하고, FSB의 금융안정 AI 위험 신호를 추가.
- **2026-08-29:** Distribution과 Evaluation을 독립 경쟁축으로 강화하고 한국 국가 AI 서비스 및 TASTE 근거를 추가.
- **2026-08-28:** Security를 독립 경쟁축으로 추가하고 HBM/패키징 근거를 강화.
