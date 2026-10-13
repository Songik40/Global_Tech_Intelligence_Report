# Daily cloud publication

매일 **08:45 Asia/Seoul(UTC 전날 23:45)**, 주말 포함, GitHub-hosted Ubuntu runner에서 실행하도록 구성했다. Mac 전원·앱·로그인 세션이 필요하지 않다. GitHub 일정 실행은 대기열 때문에 늦어질 수 있으므로 실제 조사 시작 시각을 컷오프로 쓴다.

## 전환 상태와 활성화

**초기 상태는 예약 발행 비활성이다.** `DAILY_PUBLISH_ENABLED`가 문자열 `true`일 때만 예약 실행이 동작한다. 기존 ChatGPT 클라우드 예약은 실제 새 발행 경로의 검증까지 유지한다. 이 문서나 코드 설치만으로 전환 성공을 주장하지 않는다.

1. [Actions secrets](https://github.com/Songik40/Global_Tech_Intelligence_Report/settings/secrets/actions)에 `OPENAI_API_KEY`와 `REPORT_INSTRUCTIONS`를 등록한다. `REPORT_INSTRUCTIONS`에는 기존 예약에 등록된 전체 프롬프트를 생략·요약하지 않고 그대로 넣는다. 개인 프롬프트·예약 식별자·API 키는 공개 저장소나 채팅에 게시하지 않는다. OpenAI API 결제·사용량 한도를 별도로 설정한다. ChatGPT 구독과 API 결제는 별개다.
2. [Daily global tech report](https://github.com/Songik40/Global_Tech_Intelligence_Report/actions/workflows/daily-report.yml)에서 `Run workflow` → `verify`로 기존 보고서 검증을 실행한다. `recover`는 이미 발행된 당일 보고서의 누락 검증 기록만 보완한다.
3. 새로운 날짜에 `publish`를 수동 실행해 조사·편집 검토·게시·원격 검증을 실제로 확인한다. 이미 당일 보고서가 있으면 재작성 없이 검증만 한다. 조사 결과가 거절되면 초안 artifact와 이유가 남고 발행하지 않는다.
4. 성공한 run의 `result.json`, 원격 main, 출처 원장에 완료형 기록이 있는지 확인한 뒤 기존 ChatGPT 예약을 중지하고 [Actions variables](https://github.com/Songik40/Global_Tech_Intelligence_Report/settings/variables/actions)에 `DAILY_PUBLISH_ENABLED=true`를 등록한다. 새 API 발행 테스트가 실패하면 기존 예약을 유지한다.

## 권한과 데이터 흐름

- `research`: GitHub `contents:read`, checkout 자격 증명 저장 금지. GPT-6.1 Sol **high** + web search로 조사·작성 후 별도 편집 검토. GitHub 쓰기 도구·토큰을 모델에 전달하지 않는다. 이 모델의 계정/API 접근은 실제 호출로만 확인하며 미지원이면 오류를 보고한다.
- `publish`: 모델 호출·OpenAI API 키 없음. GitHub의 해당 저장소 `GITHUB_TOKEN(contents:write)`만 사용한다. 출력 JSON을 데이터로 읽고 실행하지 않는다. 허용 경로는 당일 report/source/assets, 두 색인, 기존 trends/signals뿐이다. `.github`, scripts, methodology, 기존 과거 리포트는 모델 출력으로 변경할 수 없다.
- 트렌드·시그널의 과거 내용은 보존하고 근거를 덧붙인다. 원격 HEAD가 달라지면 강제 푸시·덮어쓰기 없이 중지한다. 동시 실행은 직렬화한다. 별도 ChatGPT 예약과의 경쟁도 당일 존재 검사와 fast-forward 조건으로 방어하지만, 새 경로 검증 후 기존 예약을 중지하는 것이 정상 운영 조건이다.
- 원격 내용을 다시 읽어 SHA-256·상대경로·SVG XML·표시 폭·외부 HTTP 상태를 기록하고 원장에 검증 로그를 커밋한다. 그 로그 커밋까지 다시 읽어야 `글로벌 리포트 푸시 완료`를 출력한다. 401/403은 접근 제한으로 공개하며 원문 열람 성공을 주장하지 않는다. 잘못된 리다이렉트·404·접속 실패는 발행 완료로 처리하지 않는다.
- 전 단계의 초안과 검증 결과는 Actions artifact로 남는다. 이미 게시됐으나 원장 기록이 누락된 경우 `recover`로 재개한다. 게시 전 편집 검토가 거절된 초안은 자동으로 승인하거나 재시도하지 않는다.

## 실패 처리

429·일부 일시적인 5xx만 제한적으로 재시도한다. 모델 거절·401/403·안전/권한 오류는 구체적인 실패를 보고하고 중지한다. 보안 정책 우회를 위한 토큰 교체·내용 난독화·다른 도구 사용은 하지 않는다. 분리된 발행 단계는 일반 에이전트의 매번 도구 쓰기 승인을 줄이는 설계이며, 모든 정책·GitHub 권한·외부 사이트 접근·서비스 장애를 해결한다는 보장은 아니다.

GitHub 기본 실패 알림을 활성화하면 실패한 run을 확인할 수 있다. 별도 메신저나 이메일 전송은 구성하지 않았다. 공개 저장소 예약은 장기간 저장소 활동이 없으면 GitHub가 비활성화할 수 있다.

## 보존한 원문과 검증 범위

전체 개인 프롬프트는 비공개 `REPORT_INSTRUCTIONS` Secret으로 보존한다. API에 전달할 때에는 모델의 역할을 조사·작성으로 한정하는 adapter를 앞에 추가하며, 원문의 GitHub 발행·위임·원격 재검증 지시는 deterministic publisher가 담당한다. API 응답이 원문 지시를 되돌려줄 수 있으므로 artifact에는 응답 전체를 저장하지 않고 ID·모델·상태·사용량만 남긴다.

정적 검사는 사실의 진위를 완전히 판정하지 않는다. 별도 모델 편집 검토도 오류를 놓칠 수 있다. 주요 사실·출처·시간·제한을 원장과 artifact에 남겨 사후 검토할 수 있도록 한다. 현재 methodology가 바뀌면 매번 최신 main을 읽어 조사·편집 검토에 전달한다.

공식 참고: [Responses web search](https://developers.openai.com/api/docs/guides/tools-web-search), [structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs), [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [GitHub scheduled workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows), [GITHUB_TOKEN permissions](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token).
