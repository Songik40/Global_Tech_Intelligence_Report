# Image Policy

이 저장소의 시각자료는 **정보 전달, 안정적인 GitHub 렌더링, 저작권 준수**를 동시에 만족해야 합니다.

## 1. Preferred Asset Order

1. 저장소에서 직접 만든 SVG·도표
2. 재사용 조건이 명확한 공식 기관 자료
3. Wikimedia Commons 등 라이선스가 명확한 외부 자료
4. 원문 기사 링크만 제공 — 이미지 권리가 불명확한 경우

Reuters/AP 등 기사 페이지의 사진을 임의로 복사해 저장소에 업로드하지 않습니다.

## 2. GitHub Rendering Standard

Markdown 기본 이미지 문법은 원본 크기와 비율에 따라 지나치게 크게 보일 수 있으므로, 리포트 본문에서는 가능한 한 HTML `<img>` 태그의 `width` 속성을 사용합니다.

### Recommended display widths

| Asset type | Recommended width |
|---|---:|
| Landscape photo | 720–760 px |
| Wide infographic / SVG | 760–820 px |
| Portrait photo | 320–360 px |
| Small logo / icon | 120–240 px |

### Rules

- **높이(`height`)를 강제로 지정하지 않습니다.** `width`만 사용해 원본 종횡비를 유지합니다.
- 4K/8K급 원본을 그대로 표시하기보다, 신뢰할 수 있는 720–1024 px derivative/thumbnail이 있으면 우선 사용합니다.
- 세로형 사진은 최대폭으로 렌더링하지 않습니다. 긴 세로 사진은 읽기 흐름을 크게 깨뜨리므로 320–360 px 정도로 제한합니다.
- 외부 이미지의 redirect URL은 GitHub 이미지 프록시에서 실패할 수 있으므로 가능한 경우 **직접 파일 URL**을 사용합니다.
- 외부 이미지는 원본 Commons/기관 페이지를 `<a>`로 연결해 클릭 시 출처를 확인할 수 있게 합니다.
- 캡션에는 최소한 **대표 이미지 여부, 저작자/기관, 라이선스**를 표시합니다.

## 3. Aspect Ratio

이미지를 리포트 레이아웃에 맞추기 위해 임의로 찌그러뜨리지 않습니다.

- 원본 비율 유지
- 필요하면 표시 폭만 줄임
- 강제 crop은 원본 라이선스가 허용되고 정보 손실이 없을 때만 사용
- 대표 이미지가 사건 그 자체의 증거가 아니라면 캡션에 `Representative image`라고 명시

## 4. Reliability

외부 이미지를 사용하기 전에 다음을 확인합니다.

- 원본 페이지가 존재하는가
- 라이선스가 명확한가
- 이미지 직접 URL이 실제 파일을 가리키는가
- 지나치게 큰 원본 대신 안정적인 derivative가 있는가

외부 이미지가 불안정하면 사진을 억지로 넣지 않고 저장소의 자체 SVG로 대체하거나 원본 페이지 링크만 제공합니다.

## 5. Asset Manifest

각 날짜의 `assets/YYYY-MM-DD/README.md`에는 다음을 기록합니다.

- 파일 또는 표시 URL
- 원본 페이지
- 저작자/기관
- 라이선스
- 대표 이미지 여부
- 수정 여부
- 리포트 내 권장 표시 폭

## 6. Repository-created Graphics

직접 만든 도표는 SVG를 기본 형식으로 사용합니다.

장점:

- 텍스트와 선이 확대해도 선명함
- GitHub에서 가볍게 렌더링됨
- 파일 크기가 작음
- 출처 데이터와 해석을 분리해 표현하기 쉬움

SVG 자체는 원본 데이터를 과장하거나 기사 사진을 복제하지 않고, 리포트의 구조·관계·수치 요약을 설명하기 위한 용도로 사용합니다.
