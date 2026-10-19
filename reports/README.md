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

- [2026-10-19](2026/10/2026-10-19.md) — Anthropic 조건부 공익기금, Microsoft–Nscale 철수 취재(이유 미확정), MMX 운영계획 · 3건 · 원 컷오프 08:51:36 KST · **수정본 재승인 후 10/19 발행**

- [2026-10-18](2026/10/2026-10-18.md) — IMF IMFC의 AI·금융 위험 공식 결론, 일본은행 정책 관련 IMF 고위 관계자 인터뷰 · 확인된 새 증거 2건 · 11:38:24 KST 컷오프

- [2026-10-17](2026/10/2026-10-17.md) — 중국 AI 수출관리, 미국 AI 자본위험, Toyota Arene 목표, 코스피 반등, NASA ISS 실험 · 원 컷오프 13:39:45 KST · **10/18 실제 게시**

- [2026-10-16](2026/10/2026-10-16.md) — TSMC Q3·4Q 전망, 코스피 급락·금융위, 미국 PPI, 군집위성 첫 영상, Artemis II 열차폐 · 원 컷오프 09:03:07 KST · 24시간 + 17분 40초 공백 점검

- [2026-10-15](2026/10/2026-10-15.md) — 미국 CPI·AI 주식 조정, ASML Q3, Hesai Kosmo, PBC·메타물질 Nature · 원 컷오프 08:45:27 KST · 24시간 조사

- [2026-10-14](2026/10/2026-10-14.md) — Gemini 4 Argon 제공 확대, IMF 금융안정 위험, 한국 반도체주, Apple HomeView, 누리호 교신 · 원 컷오프 08:49:15 KST · 24시간 6분 조사

- [2026-10-13](2026/10/2026-10-13.md) — Meta Muse Wonder, XPENG G9L·NGP 유럽, 2026 경제학상, Fed Hammack, 기후 fingerprint 리뷰

- [2026-10-12](2026/10/2026-10-12.md) — Yandex 추가 중단, Encaleret, Tegoprazan 3상, Acoramidis EHR, AFFIRM 결과 요약

- [2026-10-09](2026/10/2026-10-09.md) — Google 업무 에이전트, NASA–DOE MOU, Upscale Token Fabric, Claude 베타, 미국 모기지 7.40%

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

