# AGENTS.md — PARA 개인 볼트 에이전트 가이드 (공통 정본)

이 저장소는 PARA 방법론 기반 개인 Obsidian 볼트입니다 (개인 일정·사이드 프로젝트·공부 전용).

> **이 파일이 모든 AI 도구의 공통 정본(Single Source of Truth)입니다.**
> `CLAUDE.md` / `GEMINI.md` 는 이 파일을 `@AGENTS.md` 로 임포트하고 각 도구 전용 항목만 덧붙입니다.
> 공통 규칙을 바꿀 때는 **이 파일만** 수정하세요.

## 🔔 세션 시작 규칙 (개인 컴 필수)

**모든 에이전트(agy/Antigravity, Claude Code, Gemini CLI, Codex)는 이 볼트에서 세션을 시작하면 가장 먼저 다음을 수행한다:**

1. 루트의 **`NEXT-SESSION.md`** 를 읽는다 — 개인 컴 작업 브리핑(SoT).
2. `git pull` 로 최신 상태를 동기화한다 (obsidian-git이 자동 백업하지만 세션 시작 시 수동 확인).
3. 브리핑의 **최상위 우선순위 작업과 그 "다음 행동"** 을 한 줄로 제안하고, 승인 시 바로 이어서 진행한다.
4. 작업 단위 완료 또는 세션 종료 시 `NEXT-SESSION.md` 의 상태·다음 행동·최종 갱신일을 갱신한다 — 다음 세션이 이어받도록.

## 🤖 도구 분업 & 위임

- **분업**: agy(Antigravity) = 허브(작업 관리·위임 지휘)·메인 구현·오케스트레이션 / Claude Code = 보조·구현·코드리뷰 / Gemini CLI = 조사·대량 컨텍스트(1M) 분석·문서화·웹 검색 / Codex = 보류(자리 예약).
- **허브 도구 설정**: `vibe main` 은 `VIBE_HUB_TOOL` 환경변수(현재 `agy`)로 메인 도구를 결정한다. Claude 팀 플랜 이탈 또는 메인 도구 전환 시 어댑터 교체 시나리오는 `01.Projects/개인컴_AI_작업환경_업그레이드/design.md` §3.3 참조.
- **프로젝트 작업 위임**: `vibe delegate <프로젝트|경로> [--tool agy|claude|gemini|codex] ["메시지"]` — 메인 구현/작업은 agy(기본), 조사·문서화는 `--tool gemini`, 필요 시 `--tool claude`.
- **Single-Writer 원칙**: 하나의 레포에 동시에 한 도구만 Write. 위임 전 대상 레포의 dirty 여부를 확인한다.
- **화면 구성**: 노트북 단독 = main-vertical(허브 좌 50% + 위임 pane 우측 스택, 3개째부터 cmux 승격) / 외장 모니터 = 장기 프로젝트를 `cmux-proj` 워크스페이스로 분리 배치.

## 🍱 개인관리 기능 라우팅 (다이어리·식단·예산·일정 — 0순위 작업)

개인관리가 도메인이고 노션은 현재 선택된 저장소 어댑터다. 사용자가 아래 의도를 표현하면 **어느 툴이든** 해당 도메인 문서를 Read 한 뒤 수행한다 (현재 어댑터: Notion MCP):

| 사용자 표현 | 도메인 문서 |
|---|---|
| 일기·기분·오늘 하루 | `02.Areas/07.개인관리/01.다이어리.md` |
| 먹었어·식재료·장 봤어 | `02.Areas/07.개인관리/02.식단.md` |
| ~원·지출·구매·잔액·wish list | `02.Areas/07.개인관리/03.예산.md` |
| 일정·이번 주 계획·시간 블럭·주간 회고 | `02.Areas/07.개인관리/04.일정.md` |

기능→환경별 수단 매핑의 정본 레지스트리는 `02.Areas/07.개인관리/README.md` (도구 무관 진입점). 노션 전용 규약(DB ID·명명 규칙·MCP 전제 조건)은 `02.Areas/07.개인관리/adapters/notion/README.md` 참조.

## 🛠️ 개인 작업 통합 CLI (para-work)

모든 에이전트는 터미널 명령으로 아래 작업을 즉시 실행할 수 있습니다 (단축어: `pwork`):

- `para-work backup` — Obsidian 볼트 수동 커밋 및 푸시 (`DOC: backup YYYY-MM-DD HH:mm:ss`)
- `para-work briefing` — `NEXT-SESSION.md` 브리핑 열람 및 오늘 날짜로 갱신
- `para-work notion` — Notion 루틴 (일기·식단·예산) SOP 문서 열람
- `para-work menu` — 대화형 fzf 작업 메뉴 실행

## 🗂️ 작업 허브

- `NEXT-SESSION.md` — 세션 간 인수인계 브리핑 (최우선 참조)
- `TASKS.md` — GTD 스타일 태스크 목록 (**Active** 진행 중 / **Waiting On** 대기 / **Someday** 언젠가 / **Done** 완료 이력)
- `dashboard.html` — `TASKS.md` 기반 생산성 대시보드 UI
- `01.Projects/` — 진행 중 프로젝트 노트 (프로젝트별 상세 체크리스트)

## 📁 저장소 구조 & 파일 규칙

PARA 4분류에 번호 접두사를 사용합니다:

- **`01.Projects/`** — 명확한 목표가 있는 진행 중인 프로젝트
- **`02.Areas/`** — 지속적인 문서화가 필요한 장기적인 영역
- **`03.Resources/`** — 참고 자료 및 학습 노트 (주제별: Algorithm, JavaScript, React, TypeScript, Kotlin 등)
- **`04.Archives/`** — 완료되었거나 비활성화된 문서

- 새 파일 생성 시 위 구조를 준수할 것.
- 각 리소스 주제는 메인 개요 파일을 가짐 (예: `알고리즘 정리.md`, `Javascript 정리.md`).
- 모든 문서는 **한국어 마크다운** 형식으로 작성.
- 내부 링크는 Obsidian의 `[[위키-링크]]` 구문 사용.
- Excalidraw 다이어그램은 `.excalidraw.md` 확장자 사용.

## 🔄 버전 관리

이 볼트는 자동 백업을 위해 obsidian-git 플러그인을 사용합니다:

- 커밋 메시지 형식: `DOC: backup {{date}}` / 자동 커밋: `vault backup: {{date}}`
- 날짜 형식: `YYYY-MM-DD HH:mm:ss` · 파일 변경 후 30분마다 자동 저장 · push 전 pull 활성화

**수동으로 커밋할 때**는 기존 규칙을 따르세요 (또는 `para-work backup`):

```bash
git add .
git commit -m "DOC: backup $(date '+%Y-%m-%d %H:%M:%S')"
git push
```

## 🧩 Obsidian 플러그인

**obsidian-git**(Git 자동 백업) · **dataview**(노트 데이터 쿼리) · **calendar**(일일 노트 달력) · **templater-obsidian**(템플릿) · **excalidraw**(다이어그램) · **obsidian-linter**(마크다운 린팅) · **readwise-official**(Readwise 연동)

## 📦 보관 프로젝트 참고

- **OutlineObsidianSync** — `04.Archives/03.OutlineObsidianSync` (보관됨). Outline ↔ Obsidian 양방향 동기화 플러그인(TypeScript, Obsidian Plugin API). 재개 시 빌드 `tsc`, 설치는 `dist/` 내용을 `.obsidian/plugins/outline-sync/` 로 복사.
