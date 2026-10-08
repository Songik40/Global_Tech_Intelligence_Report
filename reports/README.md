# Daily Report Archive

일일 리포트는 `YYYY/MM/YYYY-MM-DD.md` 형식으로 저장합니다.

## Event Briefings

학회·전시회 등 행사 단위 브리핑은 `YYYY/MM/YYYY-MM-DD-<event-slug>.md`(작성 기준일) 형식으로 저장하고, frontmatter에 `type: event-briefing`을 둡니다. 증거 원장은 `sources/`에 같은 경로·파일명으로 1:1 대응합니다.

| 작성일 | 행사 | 기간·장소 | 상태 |
|---|---|---|---|
| [2026-10-01](2026/10/2026-10-01-iros-2026.md) | IEEE/RSJ IROS 2026 | 09-27~10-01 · Pittsburgh | 검증 완료 · 수상 결과는 2026-10-06 브리핑 |
| [2026-10-06](2026/10/2026-10-06-iros-2026-results.md) | IEEE/RSJ IROS 2026 — 결과 | 09-27~10-01 · Pittsburgh | 검증 완료 · 공식 수상 페이지 갱신 대기 |

## Supplements

게시 후 점검에서 조사 구간 안의 누락 사건이나 미발행일 공백 구간을 보완한 리포트입니다. `YYYY/MM/YYYY-MM-DD-supplement.md`, frontmatter `type: supplement`, 원장은 같은 경로로 1:1 대응합니다. 원 리포트 본문은 고치지 않고 끝에 `Post-publication addendum`을 남깁니다.

| 작성일 | 대상 | 내용 |
|---|---|---|
| [2026-10-08](2026/10/2026-10-08-supplement.md) | 2026-10-08 리포트 + 10-07 공백 구간 | 누리호 5차 발사, GPT-6 ChatGPT 전체 배포, LG전자 잠정실적, 노벨 화학·물리학상 · 원 리포트 정정 |
| [2026-09-29](2026/09/2026-09-29-supplement.md) | 2026-09-23~29 리포트 | 에이전트 사고·자율규제·미중 AI 대화 등 6건 |

## 2026

### October

- [2026-10-08](2026/10/2026-10-08.md) — 삼성 잠정 실적, Haiku 5.5, Surface RTX Spark, Biohub, 핵시계 논문 · [보완](2026/10/2026-10-08-supplement.md)
- [2026-10-06](2026/10/2026-10-06.md) — 산업 데이터 M&A, 새 제조 매출, 텍스트 출처 신호, 광유전학 수상, 로봇 안전 평가 투자
- [2026-10-02](2026/10/2026-10-02.md) — 궤도 AI 시험, 실시간 음성 모델, 제조업 가격 압력, 휴머노이드 안전 연동, Crew-13 도킹
- [2026-10-01](2026/10/2026-10-01.md) — 메모리 실적, FTC 조사 확인, PCE 개정, 로봇 손 사양, 핵융합·양자 연구 정책

### August

- [2026-08-28](2026/08/2026-08-28.md) — AI infrastructure, cyber defense, humanoids, MTG-I2, AI market reaction

## Report lifecycle

1. 조사 구간 확정 — 직전 발행 리포트 이후 미발행일이 있으면 그 컷오프부터 (`공백 구간` 표시)
2. 후보 수집 — 분야별 탐색, 한국 1차 출처, 예정 이벤트 대조, 영향 범위 점검 ([필수 점검](../methodology/editorial-policy.md#candidate-sweep-checklist))
3. 1차 출처 우선 확인
4. 독립 보도와 교차검증
5. FACT / ANALYSIS / UNCERTAINTY 분리
6. 이미지 라이선스 확인
7. 일일 리포트 작성 ([필수 섹션](../methodology/editorial-policy.md#required-sections))
8. `trends/`와 `signals/`에 누적 반영
9. GitHub 반영 후 링크·내용 재검증, 결과를 원장에 완료형으로 기록
10. 누락·오류 발견 시 보완 리포트와 `Post-publication` 기록
