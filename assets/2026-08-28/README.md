# Asset Manifest — 2026-08-28

이 문서는 2026-08-28 리포트에 사용한 시각자료의 출처·라이선스·표시 규격을 기록합니다.

## Rendering rules for this report

- Wide SVG / infographic: **820 px**
- Landscape photo: **760 px**
- Portrait photo: **330 px**
- `height`는 지정하지 않고 원본 종횡비를 유지
- Wikimedia redirect URL 대신 가능한 경우 직접 파일 URL 사용

## Repository-created graphics

| File | Purpose | Display width | License |
|---|---|---:|---|
| [hbm-supply-chain.svg](hbm-supply-chain.svg) | HBM/패키징이 AI 인프라 공급망에서 차지하는 위치 설명 | 820 px | Repository original |
| [ai-cyber-defense.svg](ai-cyber-defense.svg) | AI가 공격·방어 양쪽을 가속하는 구조 설명 | 820 px | Repository original |
| [market-snapshot.svg](market-snapshot.svg) | 2026-08-27 미국 시장 반응 요약 | 820 px | Repository original; data from report sources |

## Licensed remote images

### Unitree G1

- Display URL: `https://upload.wikimedia.org/wikipedia/commons/8/8a/Unitree_G1.jpg`
- Source page: https://commons.wikimedia.org/wiki/File:Unitree_G1.jpg
- Author: Sayanesy
- License: CC0 1.0
- Use: Representative Chinese humanoid image only
- Modified: No
- Display width in report: **330 px**
- Layout note: portrait image; intentionally kept narrow to avoid dominating the page

### Meteosat Third Generation Imager

- Display URL: `https://upload.wikimedia.org/wikipedia/commons/d/d8/Meteosat_Third_Generation_ESA418057_%28MTG-I_cropped%29.jpg`
- Source page: https://commons.wikimedia.org/wiki/File:Meteosat_Third_Generation_ESA418057_(MTG-I_cropped).jpg
- Author/Credit: European Space Agency (ESA)
- License: CC BY-SA 3.0 IGO
- Use: Representative MTG-I family render
- Modified: No
- Display width in report: **760 px**
- Reliability note: replaced the previous `Special:Redirect/file/...` embed with a direct Wikimedia file URL

### NVIDIA Headquarters

- Display URL: `https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/NVIDIA_Headquarters.jpg/960px-NVIDIA_Headquarters.jpg`
- Source page: https://commons.wikimedia.org/wiki/File:NVIDIA_Headquarters.jpg
- Author: Coolcaesar
- License: CC BY-SA 4.0
- Use: Representative company image
- Modified: No
- Display width in report: **760 px**
- Performance note: uses Wikimedia's 960 px derivative instead of the multi-megabyte original

## Why some images remain remote

현재 GitHub 연결에서는 외부 웹 이미지의 바이너리 파일을 직접 저장소로 복사하는 경로가 제한됩니다. 따라서 재사용 조건이 검증된 원본만 원격 임베드하고, 라이선스와 실제 표시 URL을 저장소 안에 기록합니다.

직접 만든 설명용 그래픽은 실제 SVG 파일로 `assets/`에 저장합니다.
