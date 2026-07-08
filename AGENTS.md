# AGENTS.md — PARA 개인 볼트 에이전트 가이드

이 저장소는 PARA 방법론 기반 개인 Obsidian 볼트입니다 (개인 일정·사이드 프로젝트·공부 전용).
상세 가이드는 [GEMINI.md](GEMINI.md) 와 [CLAUDE.md](CLAUDE.md) 를 참고하세요.

## 🔔 세션 시작 규칙 (개인 컴 필수)

**모든 에이전트(Antigravity/agy, Gemini, Claude, Codex)는 이 볼트에서 세션을 시작하면 가장 먼저 다음을 수행한다:**

1. 루트의 **`NEXT-SESSION.md`** 를 읽는다 — 개인 컴에서 진행할 작업 브리핑(SoT)이다.
2. `git pull` 로 최신 상태를 동기화한다 (obsidian-git이 자동 백업하지만, 세션 시작 시 수동 확인).
3. 브리핑의 **최상위 우선순위 작업과 그 "다음 행동"** 을 사용자에게 한 줄로 제안하고, 승인 시 바로 이어서 진행한다.
4. 세션 종료(또는 작업 단위 완료) 시 `NEXT-SESSION.md` 의 해당 작업 상태와 "다음 행동"을 갱신해 둔다 — 다음 세션이 이어받을 수 있도록.

## 🍱 노션 루틴 관리 라우팅 (다이어리·식단·예산)

사용자가 아래 의도를 표현하면 **어느 툴이든** 해당 SOP를 Read 한 뒤 Notion MCP로 수행한다:

| 사용자 표현 | SOP 문서 |
|---|---|
| 일기·기분·오늘 하루 | `02.Areas/07.Notion-Ops/01.다이어리.md` |
| 먹었어·식재료·장 봤어 | `02.Areas/07.Notion-Ops/02.식단.md` |
| ~원·지출·구매·잔액 | `02.Areas/07.Notion-Ops/03.예산.md` |

공통 규약(DB ID·명명 규칙·메타 룰)과 툴별 Notion MCP 전제 조건은 `02.Areas/07.Notion-Ops/README.md` 참조.
Claude Code에서는 네이티브 `notion-suite` 스킬이 우선하며, 이 SOP는 agy(Antigravity)/Codex/Gemini용 SoT다.

## 작업 허브

- `NEXT-SESSION.md` — 세션 간 인수인계 브리핑 (최우선 참조)
- `TASKS.md` — GTD 스타일 프로젝트/태스크 목록 (Active/Waiting/Someday/Done)
- `01.Projects/` — 진행 중 프로젝트 노트 (프로젝트별 상세 체크리스트)

## 커밋 규칙

수동 커밋 시: `DOC: backup YYYY-MM-DD HH:mm:ss` 형식 (자세한 내용은 GEMINI.md 참조)
