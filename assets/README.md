# Report Assets

이미지·도표 자산의 **출처, 라이선스, 실제 표시 규격**을 날짜별로 관리합니다.

```text
assets/
└── YYYY-MM-DD/
    ├── README.md       # 해당 날짜 asset manifest
    ├── *.svg           # repository-created graphics
    └── remote images   # 실제 파일 대신 URL·라이선스·크레딧을 README에 기록
```

## Common rendering rules

- 가로형 사진: **720–760 px** 권장
- 넓은 SVG/인포그래픽: **760–820 px** 권장
- 세로형 사진: **320–360 px** 권장
- `height`를 강제로 지정하지 않고 `width`만 사용해 원본 종횡비 유지
- 대용량 원본 대신 신뢰 가능한 적정 해상도 derivative/thumbnail을 우선 사용
- redirect 기반 URL보다 가능한 경우 직접 파일 URL을 사용
- 외부 이미지는 원본 페이지를 클릭할 수 있도록 연결

## Rights & evidence rules

- 저작권 조건이 불명확한 기사 사진을 임의로 복제하지 않습니다.
- 외부 바이너리 복사가 제한될 때는 검증된 재사용 가능 원본 이미지를 Markdown에서 원격 임베드합니다.
- 원격 임베드도 반드시 저작자·라이선스·원본 페이지를 기록합니다.
- 대표 이미지는 사건의 증거로 취급하지 않고 `Representative image`임을 명시합니다.
- 자체 제작 SVG의 숫자·주장은 해당 일자 source ledger와 연결합니다.

자세한 내용: [Image Policy](../methodology/image-policy.md)
