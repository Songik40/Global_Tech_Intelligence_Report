---
title: "Source Ledger — 보완 리포트 2026-10-08"
date: 2026-10-08
type: supplement
window_utc: "2026-10-06T00:02:20Z ~ 2026-10-07T23:49:07Z"
status: verified
post_publication: true
---
# Source Ledger — 보완 리포트 2026-10-08

[보완 리포트](../../../reports/2026/10/2026-10-08-supplement.md) · [원 리포트](../../../reports/2026/10/2026-10-08.md) · [원 원장](2026-10-08.md)

## 범위와 원칙

- **원 리포트 구간:** 2026-10-06 23:49:07–10-07 23:49:07 UTC = 10-07 08:49:07–10-08 08:49:07 KST.
- **공백 구간:** 직전 발행 리포트(2026-10-06) 컷오프 2026-10-06 00:02:20 UTC부터 원 리포트 구간 시작 전까지. 10-07 리포트 미발행으로 어느 리포트에도 속하지 않았다.
- **점검 시점:** 2026-10-08 게시 후. 등급은 [source ranking](../../../methodology/source-ranking.md) 기준이다.
- **접근 메모:** openai.com, reuters.com, nobelprize.org는 점검 시 직접 열람이 막혔다(403/401). 해당 항목은 그 사실을 적고, FACT는 본문을 실제로 확인한 출처로만 썼다.

## 1. 누리호 5차 발사 — 원 리포트 구간

| ID | 원본 URL·출처 | 등급 | 날짜·시각·시간대 | 직접 확인·교차검증·한계 |
|---|---|---|---|---|
| P1 | [Korea Times](https://www.koreatimes.co.kr/business/tech-science/20261007/nuri-rocket-deploys-14-satellites-1-cubesat-fails-to-release) | B2 | 게시 **10/7 12:27 KST**, 22:18 KST 갱신 | 발사 12:25 KST, 15기 중 14기 분리, PERSAT02(쿼터니언) 미분리, 청장 14시경 성공 발표, 6호 13:08경 세종기지 첫 교신·17:52까지 5기 교신, 성공률 75%→80% |
| P2 | [파이낸셜뉴스](https://www.fnnews.com/news/202610071826359850) | B2 | 입력 **10/7 18:27 KST**, 21:24 갱신 | 15기 구성, 성공 기준 570km±15km 충족, PERSAT02는 분리 신호 수신 후 덮개 미개방, 한화에어로스페이스 발사 준비·운용 확대 |
| P3 | [비즈니스코리아](https://www.businesskorea.co.kr/news/articleView.html?idxno=278387) | C | 게시 **10/7 14:58 KST** | 약 575km 분리 개시, 주탑재 35~40초 간격. **"15기 모두 분리"는 이후 보도로 정정된 초기 정보**라 근거에서 제외 |
| P4 | [우주항공청 포토뉴스(발사일 확정)](https://www.kasa.go.kr/prog/bbsArticle/BBSMSTR_000000000012/view.do?nttId=B000000003419Ui3cJ8&mno=sub01_01_03) | A1, 배경 | 8/27 발사관리위원회 결정 | 발사 예정일 10/7 확정. **사전 공지된 예정 이벤트였다는 근거** |

**A1 원문:** 우주항공청 성공 발표 보도자료 URL은 점검 시 찾지 못했다. 성공 발표는 공식 브리핑을 인용한 서로 독립된 보도(P1·P2)로 확인했다.  
**판정:** 발사·주탑재 분리·초기 교신 Medium-High(A1 원문 확보 시 High), 큐브위성 분리 수 Medium-High(초기 보도 불일치 후 14기로 수렴).

## 2. OpenAI GPT-6 ChatGPT 전체 배포 — 원 리포트 구간

| ID | 원본 URL·출처 | 등급 | 날짜·시각·시간대 | 직접 확인·교차검증·한계 |
|---|---|---|---|---|
| P5 | [OpenAI 공식](https://openai.com/index/gpt-6-for-everyone/) | A1 | 10/7, 시각 미확정 | **HTTP 403, 본문 미대조** |
| P6 | [Unite.AI](https://www.unite.ai/openai-brings-gpt-6-with-intelligent-ui-to-all-chatgpt-tiers/) | C | 10/7 | Plus·Pro·Business·Enterprise는 10/7부터 Sol, Free·Go는 10/8부터 Luna, Intelligent UI 설명, 주간 12억 명 이상(회사 수치) |

**판정:** 배포 사실 Medium(C등급 단독 본문 확인, B등급 보도 미확보). 9/22 모델 출시는 [9/29 보완 리포트](../09/2026-09-29-supplement.md)에서 다뤘고, 이번 신규 정보는 기본 모델 전환과 Intelligent UI로 한정했다.

## 3. LG전자 3분기 잠정실적 — 원 리포트 구간

| ID | 원본 URL·출처 | 등급 | 날짜·시각·시간대 | 직접 확인·교차검증·한계 |
|---|---|---|---|---|
| P7 | [SBS Biz](https://news.sbs.co.kr/english/article.do?news_id=N1008786974) | B2 | **10/7 13:43 KST** | 매출 23.827조(+8.9%), 영업이익 7,818억(+13.5%), 누적 71.38조·4.03조, 컨센서스 9,417억(연합인포맥스) 대비 17% 하회 |
| P8 | [서울경제](https://en.sedaily.com/finance/2026/10/07/lg-electronics-q3-profit-rises-135-percent-misses-estimates) | B2 | **10/7 11:03 KST**, 11:24 갱신 | 매출·영업이익 일치, 이달 말 순이익·사업부 공개 예정 |
| P9 | [KED Global](https://www.kedglobal.com/earnings/newsView/ked202610070009) | B2 | **10/7 14:14 KST** | 기대 하회, 주가 10% 가까이 하락, LG이노텍 부진, 데이터센터 냉각 수주 |
| P10 | LG전자 2분기 실적 발표(LG 글로벌 사이트) | A1, 배경 | 7월 | 2분기 매출 23.83조·영업이익 1.58조. **검색 결과 요약 수준으로만 확인** — 전 분기 비교는 저장소 계산 |

**DART 원문:** 직접 열지 않았다. 서로 독립된 매체 세 곳의 수치가 일치했다.  
**판정:** 잠정 수치 High, LG이노텍 원인 귀속 Medium(애널리스트 해석). 컨센서스는 집계 기관마다 달라(9,417억~9,758억) 범위로 썼다.

## 4. 2026 노벨 화학상 — 원 리포트 구간

| ID | 원본 URL·출처 | 등급 | 날짜·시각·시간대 | 직접 확인·교차검증·한계 |
|---|---|---|---|---|
| P11 | [스웨덴 왕립과학원](https://www.kva.se/en/news/the-nobel-prize-in-chemistry-2026/) | A1 | **10/7**, 시각 미확정 | Kagan(Université Paris-Sud)·Soai(도쿄이과대) 공동 수상, 수상 사유 원문 확인 |
| P12 | [Nobel Prize 보도자료](https://www.nobelprize.org/prizes/chemistry/2026/press-release/) | A1 | 10/7 | 동일 발표의 공식 보도자료. 동일 기관 계열로 독립 출처로 세지 않음 |

**판정:** High.

## 5. 2026 노벨 물리학상 — 공백 구간

| ID | 원본 URL·출처 | 등급 | 날짜·시각·시간대 | 직접 확인·교차검증·한계 |
|---|---|---|---|---|
| P13 | [스웨덴 왕립과학원](https://www.kva.se/en/news/the-nobel-prize-in-physics-2026/) | A1 | **10/6**, 시각 미확정 | Halzen(위스콘신대 매디슨), IceCube 기여·고에너지 천체 중성미자 발견. nobelprize.org는 접근 차단 |

**판정:** High. **공백 구간 항목**으로 표시했다.

## 후보 점검 기록 (선정하지 않음, 독립 재확인 전)

| 구간 | 후보 | 참고 URL | 메모 |
|---|---|---|---|
| 원 리포트 | NASA Crew-12 ISS 분리 | [NASA blog](https://www.nasa.gov/blogs/spacestation/2026/10/07/nasas-spacex-crew-12-undocks-in-dragon-for-ride-home/) | 10/7. 귀환은 구간 밖 |
| 원 리포트 | 9월 FOMC 의사록 | — | 10/7 14:00 ET. Fed 원문 미확인 |
| 원 리포트 | 롯데하이마트·롯데글로벌로지스 휴머노이드 물류 실증 과제 선정 | [파이낸셜뉴스](https://www.fnnews.com/news/202610070924553608) | 10/7. 로봇 분야 **부분 점검** |
| 원 리포트 | 한국기계연구원 휴머노이드 KAIROS V0.7 시연 | [헤럴드경제](https://biz.heraldcorp.com/article/10865339) | 10/7 |
| 원 리포트 | 서울 AI 로봇쇼(10/6~8, COEX) | [서울시](https://news.seoul.go.kr/economy/archives/574797) | 행사 진행 중 |
| 공백 | Mistral Large 4 공개 프리뷰 | [Mistral](https://mistral.ai/news/mistral-large-4/) | 10/6 |
| 공백 | Waymo 첫 사모 차입 50억달러로 확대 | [Yahoo Finance(Bloomberg)](https://finance.yahoo.com/technology/articles/waymo-upsizes-debut-private-loan-202409769.html) | 익명 소식통, 미종결 |
| 공백 | Waymo 디트로이트 완전 무인 운행(직원 한정) | [ClickOnDetroit](https://www.clickondetroit.com/news/local/2026/10/06/waymo-begins-fully-autonomous-driving-in-detroit-what-to-know/) | Waymo 원문 미확인 |
| 공백 | SpaceX, 엔비디아 칩 구매용 400억달러 차입 협상 | [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-06/spacex-seeking-to-raise-40-billion-to-buy-nvidia-chips-ft-says) | FT 첫 보도, 초기 협상 |
| 공백 | Google–Constellation 3.59GW 전력 계약 | [Reuters](https://www.reuters.com/business/energy/google-enters-massive-36-gw-power-deal-with-constellation-energy-2026-10-06/) | reuters.com 접근 차단 |

## 누락 원인 판단

- **누리호:** 원 원장의 선정·제외 목록에 없다. 저장소 전체에서 누리호·우주항공청 언급이 0건이며, 8/27 발사일 확정(P4) 이후 어떤 WATCH에도 오르지 않았다. 한국 1차 출처와 예정 이벤트 대조가 수집 단계에 없었던 것이 원인으로 판단된다.
- **노벨 물리학상:** 10-07 미발행으로 생긴 공백 구간에 있었다. 기존 관행("미발행 구간 소급 없음")이 원인이다.
- **GPT-6 배포:** 같은 모델명의 9/22 출시를 이미 다뤄 반복으로 오인됐을 가능성이 있다. 반복 규칙은 "새로운 사실이 생긴 경우"를 허용한다.
- 위 원인에 대응해 [editorial policy](../../../methodology/editorial-policy.md)와 [source ranking](../../../methodology/source-ranking.md)에 규칙을 추가했다.

## 게시 후 검증

- 게시 전 이 원장과 보완 리포트의 저장소 내부 상대 링크를 모두 확인했다.
- 외부 URL은 위 표의 "직접 확인" 열 기준으로 점검 시 실제로 열어 대조했다. 접근 차단 URL은 각 행에 적었다.
