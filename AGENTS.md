# AGENTS.md — PARA 개인 볼트 에이전트 가이드 (공통 정본)

> **이 파일이 모든 AI 도구의 공통 정본(Single Source of Truth)입니다.**
> `CLAUDE.md` / `GEMINI.md` 는 이 파일을 `@AGENTS.md` 로 임포트하고 각 도구 전용 항목만 덧붙입니다.
> 공통 규칙을 바꿀 때는 **이 파일만** 수정하세요.

## 📌 프로젝트 개요

PARA 방법론(Projects·Areas·Resources·Archives)으로 정리하는 **개인 Obsidian 볼트**입니다.

- **용도**: 개인 일정·사이드 프로젝트·공부 기록. **업무 저장소와 완전히 분리** — 회사 코드·업무 문서는 이 볼트에 들어오지 않는다.
- **성격**: 코드 저장소가 아니라 **마크다운 문서 저장소**. 빌드·테스트·배포 파이프라인이 없다 (대체 검증법은 아래 명령어 절).
- **동기화**: obsidian-git 이 자동 커밋·푸시하고, 여러 기기에서 같은 볼트를 연다 (주기·주의점은 아래 「함정」·「버전 관리」).
- **0순위 작업**: 개인관리 루틴(다이어리·식단·예산·일정). 노션을 저장소 어댑터로 사용한다.

## ⌨️ 명령어

**볼트 작업 — `para-work` (단축어 `pwork`)**

| 명령 | 동작 |
|---|---|
| `para-work backup` | 볼트 수동 커밋·푸시 (`DOC: backup YYYY-MM-DD HH:mm:ss`) |
| `para-work briefing` | `NEXT-SESSION.md` 브리핑 열람·오늘 날짜로 갱신 |
| `para-work notion` | 개인관리 루틴(일기·식단·예산) SOP 문서 열람 |
| `para-work menu` | 대화형 fzf 작업 메뉴 |

**세션·위임 — `vibe`** (tmux 세션 안에서만 동작)

| 명령 | 동작 |
|---|---|
| `vibe main` | para 허브 세션 오픈. 도구는 `VIBE_HUB_TOOL`(기본 `claude`) |
| `vibe delegate <프로젝트\|경로> [--tool claude\|codex\|gemini] ["메시지"]` | 현재 창을 pane 분할해 대상 cwd 로 위임 |
| `vibe peek <프로젝트> diff` | 신규 윈도우로 대상 프로젝트 변경사항 열람 |
| `vibe cast` · `vibe reap` · `vibe done` | 세션 상태 확인 · 유휴 정리 · 종료 |

**수동 커밋** (`para-work backup` 과 동일한 동작)

```bash
git add .
git commit -m "DOC: backup $(date '+%Y-%m-%d %H:%M:%S')"
git push
```

**검증(VERIFY)** — 빌드·테스트가 없으므로 다음으로 대체한다.

- 변경 범위 확인 `git -C ~/Project/para diff --stat` → 내용 확인 `git diff`
- 셸 스크립트를 건드렸으면 `shellcheck` 또는 `bash -n` · JSON 이면 `jq .`
- ❌ 사람 눈 검증 금지 — 위 정적 도구의 단일 명령으로 입증한다.

## 📁 디렉터리 구성

```
para/
├── 01.Projects/            목표·종료 시점이 있는 진행 중 프로젝트
├── 02.Areas/               지속 관리가 필요한 장기 영역 (07.개인관리 = 0순위)
├── 03.Resources/           참고·학습 노트. `NN.주제` 형식 24개 + 99.Unsorted
├── 04.Archives/            완료·비활성 문서
├── 05.Excalidraw/          다이어그램 (.excalidraw.md)
├── 06.Temp_Images/         노트 첨부 이미지
├── Template/               회고·노트 템플릿 (templater-obsidian 용)
├── Readwise/ · Notion/     외부 서비스에서 유입되는 동기화 노트
├── memory/                 장기 컨텍스트 (context·people·projects·glossary.md)
├── scripts/                볼트 유틸 스크립트
├── .claude/                Claude 설정 + work-log/YYYY-MM-DD.md (작업 로그)
├── .obsidian/              ⚠️ iCloud 심링크 — 「함정」 절 참조
├── AGENTS.md               ← 이 파일 (공통 정본)
├── CLAUDE.md · GEMINI.md   도구별 어댑터 (@AGENTS.md 임포트 + 전용 꼬리)
└── NEXT-SESSION.md         세션 간 인수인계 SoT
```

**새 파일을 어디에 둘지 판정** — 끝나는 시점이 정해져 있으면 `01.Projects/`, 계속 관리할 주제면 `02.Areas/`, 나중에 찾아볼 자료면 `03.Resources/`. 애매하면 `03.Resources/99.Unsorted/`.

**파일 규칙**

- 모든 문서는 **한국어 마크다운**으로 작성.
- 내부 링크는 Obsidian의 `[[위키-링크]]` 구문 사용.
- 각 리소스 주제는 메인 개요 파일을 가짐 (예: `알고리즘 정리.md`, `Javascript 정리.md`).
- Excalidraw 다이어그램은 `.excalidraw.md` 확장자 사용.

<!-- 유지보수 메모(컨텍스트에 주입되지 않음): 루트에 용도 없는 git 추적 잔여물 — `--help/`, `test-diff.md`, `test-file.md`, `download.html`(0바이트). 정리 대상이나 방치해도 무해. -->

## 🔔 세션 시작 규칙 (개인 컴 필수)

**모든 에이전트(Claude Code, Codex, Gemini CLI, agy/Antigravity)는 이 볼트에서 세션을 시작하면 가장 먼저 다음을 수행한다:**

1. 루트 **`NEXT-SESSION.md`** 의 최상단 「🔜 다음 세션 착수 지점」 절을 읽는다 — 개인 컴 작업 브리핑(SoT). 파일이 크므로 전체 Read 금지(「함정」 절 참조).
2. `git pull` 로 최신 상태를 동기화한다 (obsidian-git이 자동 백업하지만 세션 시작 시 수동 확인).
3. 브리핑의 **최상위 우선순위 작업과 그 "다음 행동"** 을 한 줄로 제안하고, 승인 시 바로 이어서 진행한다.
4. 작업 단위 완료 또는 세션 종료 시 `NEXT-SESSION.md` 의 상태·다음 행동·최종 갱신일을 갱신한다 — 다음 세션이 이어받도록.

## 🤖 도구 분업 & 위임

- **분업**: Claude Code = 허브(작업 관리·위임 지휘)·메인 구현·코드리뷰 / Codex = 조사·2nd opinion·보조 구현 / Gemini CLI = 대량 컨텍스트(1M) 분석·웹 검색 / agy(Antigravity) = 보류(2026-08-14 이탈).
- **Codex 에 허브를 맡기지 않는 이유**: Codex CLI 는 PreToolUse/PostToolUse 훅이 없어 `bash-chain-guard` 류 결정론적 강제가 걸리지 않는다 — 규칙 준수가 지시문에만 의존하게 된다. (전환 이력·사유 전문은 `01.Projects/개인컴_AI_작업환경_업그레이드/design.md`)
- **허브 도구 설정**: `vibe main` 은 `VIBE_HUB_TOOL` 환경변수(기본 `claude`)로 메인 도구를 결정한다. 어댑터 교체 시나리오는 위 `design.md` §3.3 참조.
- **위임 기본값**: 메인 구현/작업은 `claude`(기본), 조사·2nd opinion 은 `--tool codex`, 대량 컨텍스트 분석은 `--tool gemini`. `vibe delegate` 는 도구명을 그대로 실행하는 도구 무관 구조라 PATH 에 있으면 동작한다.
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

## 🗂️ 작업 허브

- `NEXT-SESSION.md` — **실사용 SoT.** 세션 간 인수인계 브리핑. 여기부터 읽는다.
- `01.Projects/` — 진행 중 프로젝트 노트 (프로젝트별 상세 체크리스트·진행내역)
- `.claude/work-log/YYYY-MM-DD.md` — 작업 로그. 작업 완료 직후 당일 파일에 append.
- `TASKS.md` · `dashboard.html` — ⚠️ **2026-05 이후 갱신 정지.** 현행 작업 상태를 여기서 읽지 말 것 (`NEXT-SESSION.md` + `01.Projects/` 가 실제 상태). 되살리기 전까지는 참고용 이력.

## ⚠️ 이 볼트의 함정 (모르면 틀리는 것들)

- **`.obsidian/` 은 iCloud 심링크다** (`~/Library/Mobile Documents/.../config/obsidian/.obsidian`). 볼트 git 이력에 실체가 안 잡히고, 고치면 **모든 기기의 Obsidian 설정이 동시에 바뀐다.** 플러그인·핫키·테마 변경은 이 사실을 인지하고 할 것.
- **스킬 정본은 볼트 밖이다.** universal 정본 = `~/.agents/skills` (Claude 는 `~/.claude/skills/*` 심링크로 참조). 볼트의 `02.Areas/Claude-Skills/` 는 **백업본**이므로 여기를 고쳐도 동작이 안 바뀐다. 스킬을 고칠 땐 정본을 고치고 백업을 갱신하는 순서.
- **식단 도메인만 스킬이 규칙 정본이다.** 업무컴에는 개인 볼트를 두지 않으므로 `notion-diet-manager` 스킬이 정본이고 `02.식단.md` 는 포인터다. 나머지 개인관리 도메인은 반대(볼트 문서가 정본). 정본 위치는 항상 `02.Areas/07.개인관리/README.md` 레지스트리의 「도메인 정본」 열이 알려준다.
- **`NEXT-SESSION.md` 는 약 49KB다.** 통째로 Read 하면 컨텍스트를 크게 먹는다 — 최상단 「다음 세션 착수 지점」 절만 읽고, 필요할 때 해당 절을 찾아 읽을 것. (Claude Code 에서는 SessionStart 훅이 이미 주입해 준다.)
- **커밋 충돌 주의**: obsidian-git 이 파일 변경 후 30분마다 자동 커밋한다. 편집 중 자동 커밋이 끼어들 수 있으므로, 작업 단위가 끝나면 미루지 말고 `para-work backup` 으로 확정할 것.

## 🔄 버전 관리

- 커밋 메시지 형식: `DOC: backup {{date}}` / obsidian-git 자동 커밋: `vault backup: {{date}}`
- 날짜 형식 `YYYY-MM-DD HH:mm:ss` · 파일 변경 후 30분마다 자동 저장 · push 전 pull 활성화

## 🧩 Obsidian 플러그인

동작에 관여하는 것은 **obsidian-git**(자동 백업)·**dataview**(노트 쿼리)·**templater-obsidian**(템플릿)·**obsidian-linter**(마크다운 린팅). 전체 목록은 `ls ~/Project/para/.obsidian/plugins/` 로 확인한다 (설치 위치는 iCloud 심링크 너머 — 「함정」 절 참조).

## 📦 보관 프로젝트 참고

- **OutlineObsidianSync** — `04.Archives/03.OutlineObsidianSync` (보관됨). Outline ↔ Obsidian 양방향 동기화 플러그인(TypeScript, Obsidian Plugin API). 재개 시 빌드 `tsc`, 설치는 `dist/` 내용을 `.obsidian/plugins/outline-sync/` 로 복사.
