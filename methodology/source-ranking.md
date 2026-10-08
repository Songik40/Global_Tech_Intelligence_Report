# Source Ranking

## Tier A — Primary / authoritative

### A1: Official primary source
- 정부·우주기관·규제기관
- 기업 공식 newsroom
- 연구기관·대학 공식 발표
- 원 논문 또는 학회 자료

### A2: Filing / investor / machine-readable data
- 기업 IR·실적자료
- 규제 공시
- 공식 통계·시장 데이터

### Korean primary sources

국내 사건은 국문 1차 출처를 먼저 찾고, 영문 보도(Reuters, Yonhap, Korea Times 등)는 교차검증에 쓴다.

- **A1:** 우주항공청(KASA), 한국항공우주연구원(KARI), 과학기술정보통신부, 산업통상자원부, 대한민국 정책브리핑(korea.kr), 기업 국문 뉴스룸
- **A2:** DART·KIND 공시(잠정실적 등), 한국은행, 통계청

## Tier B — High-quality independent reporting

### B1
Reuters, AP와 같이 편집·사실검증 체계를 갖춘 국제 뉴스 통신·매체. 1차 출처에서 얻기 어려운 독립 확인, 현장 취재, 관계자 정보에 사용한다.

### B2
전문성이 높은 주요 경제·과학 매체. 보조 맥락으로 사용하되 핵심 숫자는 가능한 한 원출처를 다시 확인한다.

## Tier C — Specialist / trade press

산업 전문매체, 기업 블로그, 분석기관. 기술적 맥락에 유용하지만 이해관계와 방법론을 확인한다.

## Tier D — Unverified / social

소셜미디어, 익명 게시물, 출처가 불분명한 재가공 기사. **단독으로 FACT의 근거로 사용하지 않는다.**

## Confidence mapping

- **High:** 강한 1차 출처 + 독립 교차검증, 또는 단독으로도 충분한 권위 있는 공식 데이터
- **Medium-High:** 신뢰도 높은 독립 취재이나 전체 1차 근거가 공개되지 않음
- **Medium:** 제한된 출처 또는 초기 발표
- **Low:** 검증 불충분 — 일반적으로 TOP 5에서 제외

## Claim hierarchy

`Observed fact > official target > independent estimate > analyst interpretation > rumor`

보고서에서 이 계층을 섞어 쓰지 않는다. 회사 목표는 사실이 아니라 **회사가 제시한 목표가 존재한다는 사실**로 표현한다.

## Syndication and labeling

- 통신사 기사를 다른 사이트의 전재본으로 인용하면 **"Reuters (Investing.com 전재)"**처럼 원 매체와 게재처를 함께 표기한다.
- 바이라인 또는 "(Reuters)" 표기를 확인한 경우에만 원 매체 등급(B1)을 준다. 원 매체를 확인할 수 없으면 C로 낮춘다.
- 링크가 다른 기사로 리다이렉트되면 최종 URL·제목·시각을 원장에 남긴다. 원래 설명과 다른 기사라면 그 출처를 근거에서 뺀다.

## Timestamps

- 게시 시각은 **본문 표기 → 페이지 메타데이터(`article:published_time` 등)** 순서로 확인한다. 둘 다 없을 때만 "미확정"으로 쓴다.
- 페이지에 시간대가 없으면 "시간대 미표시"라고 쓰고, 추정한 시간대에는 "(추정)"을 붙인다.
- 검색 엔진 색인 시각을 발표 시각으로 쓰지 않는다.

## Access failures

- 원문이 403/401 등으로 열리지 않으면 원장에 그 사실을 적고, FACT는 본문을 실제로 확인한 출처로만 쓴다.
- 1차 출처를 열지 못하고 2차 출처만으로 쓴 항목은 Confidence를 한 단계 낮춘다.
