# Global Tech Intelligence Report

전 세계의 **AI·테크, 로봇·자율주행, 우주·과학, 경제·투자**를 매일 추적하는 공개 인텔리전스 리포트 저장소입니다.

이 저장소의 목표는 뉴스 링크를 쌓는 것이 아니라, **확인 가능한 사실 → 분석 → 누적 트렌드 → 장기 신호**로 연결하는 것입니다.

## Latest Report

- **[2026-09-03 Daily Intelligence Report](reports/2026/09/2026-09-03.md)** — 검증 완료
- 조사 컷오프: **2026-09-03 08:09 KST / 2026-09-02 23:09 UTC**
- 조사 범위: 최근 24시간의 새로운 발표·실제 상태 변화를 우선

## Current Major Signals

| Signal | Direction | Current evidence |
|---|---|---|
| AI policy / data access | ↑ Institutionalizing | G20, AI·IP·표준을 공통 혁신정책 축으로 합의 |
| AI infrastructure | ↑ Power bottleneck | Vertiv, UIG 인수로 grid-to-chip 전력 포트폴리오 확장 |
| Autonomous driving | ↑ Operations competition | Uber, AV 투자를 유지하며 demand/fleet 운영 플랫폼 전략 강화 |
| Space mission execution | ↑ Integration | Dragonfly 비행용 전기 하네스 설치 완료 |
| Domain AI | ↑ Data-centric deployment | Owkin K Pro + 멀티모달 환자 데이터, Boehringer 도입 |

## Repository Structure

```text
.
├── README.md
├── reports/
│   ├── README.md
│   └── YYYY/MM/YYYY-MM-DD.md
├── sources/
│   └── YYYY/MM/YYYY-MM-DD.md
├── trends/
│   ├── artificial-intelligence.md
│   ├── robotics-autonomy.md
│   ├── space-science.md
│   └── economy-investment.md
├── signals/
│   ├── physical-ai.md
│   ├── ai-infrastructure.md
│   ├── humanoid-commercialization.md
│   ├── autonomous-driving.md
│   └── space-commercialization.md
├── assets/
│   ├── README.md
│   └── YYYY-MM-DD/
└── methodology/
    ├── editorial-policy.md
    ├── source-ranking.md
    └── image-policy.md
```

## What Each Folder Does

| Path | 역할 | 업데이트 방식 |
|---|---|---|
| `reports/` | **매일 읽는 완성 리포트**. Top developments, FACT/ANALYSIS/UNCERTAINTY/WATCH, 분야 간 연결 분석을 포함 | 매일 새 파일 추가 |
| `sources/` | **증거 원장(Source Ledger)**. 일일 리포트에 사용한 1차·2차 출처, 날짜, 검증 메모, 이미지 출처를 기록 | 각 report와 1:1 대응 |
| `trends/` | **분야별 누적 동향**. AI, 로봇, 우주, 시장 등 큰 분야의 방향성이 어떻게 바뀌는지 장기간 추적 | 새 증거가 기존 판단을 강화/약화할 때 갱신 |
| `signals/` | **카테고리를 가로지르는 핵심 테마**. Physical AI, AI infrastructure처럼 여러 산업을 연결하는 구조적 변화를 추적 | 의미 있는 신호가 생길 때 갱신 |
| `assets/` | **리포트 시각자료와 라이선스 기록**. 직접 만든 SVG와 외부 이미지의 출처·저작자·라이선스·표시 규격을 관리 | 날짜별 폴더 생성 |
| `methodology/` | **리포트 작성 규칙**. 무엇을 중요한 뉴스로 고르는지, 출처 신뢰도를 어떻게 평가하는지, 이미지 사용 기준이 무엇인지 공개 | 정책 변경 시 갱신 |

## How the Pieces Connect

```text
Fresh news / official announcement
             ↓
         sources/
             ↓
          reports/
        ↙          ↘
   trends/        signals/
      ↓              ↓
분야의 장기 방향   분야를 넘는 구조적 변화
```

`reports/`가 하루의 스냅샷이라면, `trends/`와 `signals/`는 시간이 쌓일수록 가치가 커지는 누적 분석 계층입니다.

## Evidence Labels

- **FACT** — 출처에서 직접 확인되는 사실
- **ANALYSIS** — 사실을 바탕으로 한 해석
- **UNCERTAINTY** — 아직 확정되지 않았거나 출처 간 표현 차이가 있는 부분
- **WATCH** — 다음 업데이트에서 확인해야 할 지표

## Source Standard

가능하면 공식 기업·기관 발표, 규제기관·정부·논문 등 **1차 출처**를 먼저 확인합니다. Reuters·AP 등 고신뢰 매체는 독립 교차검증과 맥락 보강에 사용합니다. 자세한 기준은 [Source Ranking](methodology/source-ranking.md)을 참고하세요.

## Visual Standard

GitHub에서 이미지가 지나치게 커지거나 깨지는 문제를 피하기 위해 다음 규칙을 적용합니다.

- 가로형 사진·도표: **760–820 px 이하**
- 세로형 사진: **320–360 px 정도**
- `width`만 지정해 **원본 종횡비를 유지**하고 높이를 강제로 지정하지 않음
- 대용량 원본보다 Wikimedia 등에서 제공하는 적절한 해상도의 derivative/thumbnail을 우선 사용
- redirect 기반 이미지 URL보다 안정적인 직접 파일 URL을 우선 사용
- 외부 이미지는 원본 페이지로 클릭 연결하고, 캡션에 저작자·라이선스를 표시
- 직접 만든 도표는 `assets/` 안의 SVG로 저장

자세한 기준은 [Image Policy](methodology/image-policy.md)에 기록합니다.

## Methodology

- [Editorial Policy](methodology/editorial-policy.md)
- [Source Ranking](methodology/source-ranking.md)
- [Image Policy](methodology/image-policy.md)

## Trend Trackers

- [Artificial Intelligence](trends/artificial-intelligence.md)
- [Robotics & Autonomy](trends/robotics-autonomy.md)
- [Space & Science](trends/space-science.md)
- [Economy & Investment](trends/economy-investment.md)

## Persistent Signals

- [Physical AI](signals/physical-ai.md)
- [AI Infrastructure](signals/ai-infrastructure.md)
- [Humanoid Commercialization](signals/humanoid-commercialization.md)
- [Autonomous Driving](signals/autonomous-driving.md)
- [Space Commercialization & Data Infrastructure](signals/space-commercialization.md)

---

> Research and information tracking only. Analysis is interpretation based on cited evidence and is not financial advice.