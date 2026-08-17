# ParaType 속성 제거 기록 (2026-08-17)

노션 `Projects` DB 에서 `ParaType` select 속성을 삭제했다. 이 문서는 삭제 근거와 **`Status` 로부터 복원되지 않는 값**의 스냅샷이다.

## 삭제 근거

1. **옵션 4개 중 2개가 사용 불가.** `ParaType` 옵션은 `Project`·`Area`·`Resource`·`Archive` 였으나, 이 DB 는 Projects DB 라 모든 행이 정의상 프로젝트다. Areas 는 별도 DB(`collection://27dbfe89-6a73-47bf-8b07-865f8b48b7fb`)에 있고 이 DB 에는 이미 그쪽을 가리키는 **`Area` relation** 이 있다. 실제로 `Area`·`Resource` 값을 쓴 행은 **0건**이었다.
2. **남은 2개는 `Status` 와 중복.** `ParaType=Archive` 93건 중 92건이 `Status ∈ (Done, Canceled)` 였다. 노션 `Status` 는 이미 `complete` 그룹(Done·Canceled)을 구분하므로 같은 정보를 두 번 적는 구조였다.
3. **참조하는 코드·스킬이 없었다.** 볼트 ↔ 노션 대응은 폴더명·페이지명·`Notion ID` 로 이뤄진다. `ParaType` 을 "PARA 동기화 키" 로 기술한 것은 2026-08-17 작성 당시의 추측이었고 실제 소비처가 없어 함께 정정했다.

## 대체 규칙

**아카이브 판정 = `Status ∈ (Done, Canceled)`** 로 일원화한다.

## 스냅샷 — Status 로 복원되지 않던 값 10건

삭제 시점에 `ParaType` 과 `Status` 가 어긋나 있던 행이다. 나머지 약 108건은 `Archive ↔ (Done|Canceled)` · `Project ↔ 진행 상태` 로 규칙적이라 복원 가능하다.

| 프로젝트 | Status | 삭제 전 ParaType |
|---|---|---|
| 자바스크립트 라이브러리 제작 | Paused | Archive |
| php 소스 분석 프로젝트 | Canceled | _(없음)_ |
| Claude Code 하네스 환경 정비 — Subagent-First 글로벌화 & SoC 정리 | Done | Project |
| MCP 활용 통합 워크플로우 구축 | Done | Project |
| Outline to Markdown | Canceled | Project |
| 로또 번호 추천기 | Done | Project |
| 이메일 분류 자동화처리 | Done | Project |
| 코코아 클론 챌린지 | Canceled | Project |
| 파일 관리 및 문서화 자동화 | Done | Project |
| 하네스 엔지니어링 리서치 + 설정 업데이트 | Done | Project |

> 이 10건이 곧 "두 속성을 손으로 맞추다 어긋난" 사례다 — 중복 필드를 없앤 이유이기도 하다.

## 동반 수정

- `02.Areas/07.개인관리/05.프로젝트.md` — 필드 규칙에서 `ParaType` 행 제거, 아카이브 판정을 `Status` 기준으로 재정의
- `vibe-ai-config` `notion-project-manager` — `SKILL.md` rules·`references/db-schema.md` 에서 `ParaType` 기술 제거
