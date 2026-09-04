# Robotics & Autonomy — Trend Tracker

_Last updated: 2026-09-05_

## Current Direction

로봇·자율주행은 **기술 데모 → 실제 배치 → 인증·신뢰성·경제성 검증 → 지역 생산·상업 운행 → 인프라 규모 통합** 단계로 이동하고 있다. 목적형 robotaxi가 실제 서비스에 투입되면서 **차량 구조 자체의 규제 적합성**도 소프트웨어 안전성과 동등한 상용화 변수로 부상했다.

## Key Drivers

- 멀티모달 모델과 로봇 제어
- 실제 환경 행동 데이터
- 액추에이터·배터리·센서 비용
- fleet learning
- 안전성과 운영 신뢰성
- 규제 인증과 서비스 허가
- 차량 안전기준과 purpose-built autonomy 설계의 정합성
- 지역 산업구조와 실제 수요에 맞는 배치
- 대량생산·현지조달·서비스 네트워크
- 저가 개발 플랫폼과 개발자 생태계
- 물류·항만·광업 등 기존 산업 인프라와의 통합

## Recent Evidence

- [2026-09-05](../reports/2026/09/2026-09-05.md): Tesla가 Austin Robotaxi 서비스에 Cybercab을 실제 투입한 직후 NHTSA가 FMVSS 자기인증에 대한 Audit Query를 열었다. driverless capability가 실제 목적형 차량으로 이동하면서 certification strategy와 차량 안전기준이 독립 상용화 병목이 됐다.
- [2026-09-04](../reports/2026/09/2026-09-04.md): Wayve·Uber가 런던에서 일반 이용자 대상 supervised autonomous rides를 실제로 시작했다. 전략·허가 단계에서 실제 consumer operations로 이동한 신호다.
- [2026-09-01](../reports/2026/09/2026-09-01.md): HUMAIN과 Applied Intuition이 사우디 주요 물류축에 2030년까지 수천 대의 자율주행 트럭을 배치한다는 계획을 발표했다. 자율주행 경쟁이 도시 단위 서비스에서 국가 물류 인프라 계획으로 확대되는 신호다.
- [2026-08-31](../reports/2026/08/2026-08-31.md): Pony.ai·FutureLink가 한국에서 10대 인증 차량을 시작으로 총 200대의 7세대 로보택시 도입을 추진한다고 공개했다. 자율주행 경쟁이 시험주행에서 인증·차량도입·상업운행 준비로 이동하는 신호다.
- [2026-08-31](../reports/2026/08/2026-08-31.md): Pollen Robotics의 399달러 Microduck이 출시 직후 강한 초기 주문 신호를 보였다. Physical AI 실험의 진입비용을 낮추는 개발자 플랫폼이 별도 시장을 형성할 가능성을 보여준다.
- [2026-08-30](../reports/2026/08/2026-08-30.md): Minth와 AGIBOT가 세르비아 Šabac에서 휴머노이드 로봇 양산을 시작했다. Physical AI 경쟁이 중국 내 생산에서 유럽 인접 지역 생산거점과 서비스망 구축으로 확장되는 신호다.
- [2026-08-29](../reports/2026/08/2026-08-29.md): 중국 NDRC가 로봇 산업의 지역 적합성, 질서 있는 발전, 실제 환경 데이터와 신뢰성 검증을 강조하면서 '무조건적 확장'보다 실배치 중심의 정책 신호가 강화됐다.

## Major Players / Systems

중국 휴머노이드 업체, 글로벌 산업용 로봇 기업, 자율주행 서비스 사업자, 자동차 제조사, foundation robotics 연구그룹, 지역 제조 파트너, 저가 로봇 개발 플랫폼, 물류·광업·항만 운영자, 자동차 안전 규제기관.

## Technical Bottlenecks

- 장시간 무개입 작동
- 정밀 manipulation
- 새로운 작업에 대한 일반화
- 실패 복구
- 안전 검증
- 인증·규제 승인
- purpose-built autonomous vehicle의 기존 안전기준 적합성
- 작업당 총비용
- 실제 환경 데이터의 품질과 규모
- 계획 생산능력을 실제 유료 수요로 전환하는 속도
- 대형 fleet의 원격지원·정비·보험 체계

## Contradicting Signals

생산능력과 투자·기업 수는 빠르게 증가하지만, 반복 가능하고 수익성 있는 실제 작업 데이터는 상대적으로 부족하다. 공장 오픈·사전주문·`planned capacity`·목표 차량 수는 상용화 성과와 다르며 실제 인도량, 유료 이용량, 가동률을 별도로 봐야 한다. 목적형 robotaxi는 기존 수동제어 장치를 제거할수록 소프트웨어 성능과 별개로 인증·법규 적합성 리스크가 커질 수 있다.

## Commercialization Metrics

- 작업 성공률
- intervention rate
- mean time between failures
- 시간당 비용
- 새로운 작업 학습 시간
- 실제 유료 고객 배치 수
- 실기기 데이터 수집량과 품질
- 월별 생산량·가동률·현지조달률
- 자율주행 인증 차량 수·paid rides / paid freight·fleet utilization
- 규제 audit·면제·인증 진행 상태
- tonne-km당 비용과 사고율
- 개발자 플랫폼의 활성 사용자·소프트웨어 기여도

## 30–90 Day Watchlist

- NHTSA Cybercab Audit Query와 FMVSS 적합성·면제 경로
- Austin Cybercab 실제 유료 운행량·fleet utilization·안전데이터
- 런던 supervised rides의 driverless 전환 진행
- 사우디 자율주행 트럭 첫 실제 배치·유료 화물운송
- 한국 내 Pony.ai 인증 차량 실제 반입 및 규제 진행
- Microduck 실제 출하·SDK/시뮬레이터 개발자 활동
- 세르비아 생산거점의 실제 월별 생산·인도량
- 실제 운영시간·intervention rate·사고율 공개

## Working Thesis

> Physical AI와 자율주행의 승자는 가장 인상적인 데모보다 **신뢰 가능한 실제 데이터, 규제 통과, 차량·시스템 안전기준 적합성, 지역별 적용 적합성, 대량생산·서비스 능력, 인프라 통합, 경제성**을 먼저 연결하는 쪽일 가능성이 높다.

## Change Log

- **2026-09-05:** Tesla Cybercab 배포와 NHTSA Audit Query를 반영해 purpose-built AV의 차량 안전기준 적합성과 regulatory audit를 독립 상용화 변수로 추가.
- **2026-09-01:** 사우디 국가 규모 자율주행 트럭 계획을 반영해 물류 인프라 통합·paid freight·tonne-km 비용을 상용화 변수로 추가.
- **2026-08-31:** Pony.ai 한국 200대 로보택시 계획을 반영해 인증·paid rides·fleet utilization을 핵심 상용화 변수로 강화. Microduck 초기 수요를 반영해 저가 개발자 플랫폼을 새로운 데이터·생태계 변수로 추가.
- **2026-08-30:** Minth·AGIBOT 세르비아 양산을 반영해 지역 생산·현지조달·실생산량을 핵심 상용화 변수로 추가.
- **2026-08-29:** 중국 NDRC 정책 신호를 반영해 '정책적 선별'과 지역 적합성을 핵심 변수로 추가.
