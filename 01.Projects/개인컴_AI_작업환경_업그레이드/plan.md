# 개인컴 AI 작업환경 업그레이드 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 개인 컴 허브-위임 환경을 멀티 AI CLI(Claude 허브 + Gemini 분업, Codex 예약)로 확장하고, 허브 도구를 교체 가능하게 만든다.

**Architecture:** 기존 vibe.sh(tmux pane 위임 런처)에 `--tool` 옵션과 `VIBE_HUB_TOOL` 환경변수를 추가해 pane/허브에 띄우는 CLI를 선택 가능하게 한다. 설정(cmux-projects.txt)·규칙(para CLAUDE.md)·보안(gemini PAT)은 각 정본 파일을 외과수술식으로 수정한다.

**Tech Stack:** bash (vibe.sh), tmux, 마크다운, JSON. 검증 도구: `bash -n` + `shellcheck` (셸), `grep` (설정·문서).

**Spec:** `01.Projects/개인컴_AI_작업환경_업그레이드/design.md` (같은 폴더)

## Global Constraints

- 외과수술식 변경 — 각 파일에서 명시된 라인만 수정, 무관 코드·주석·포맷 개선 금지.
- Bash 명령 체이닝(`&&`, `;`, `|`) 금지 — 단일 명령 여러 번 호출.
- `vibe delegate <대상> ["메시지"]` (옵션 없음) 기존 동작 100% 보존 — 회귀 금지.
- 도구 기본값은 항상 `claude` (`--tool` 생략 시, `VIBE_HUB_TOOL` 미설정 시).
- 토큰 값(`github_pat_...`)을 git 추적 파일·계획 문서에 절대 기록하지 않는다.
- para 볼트 커밋 메시지: `DOC: backup YYYY-MM-DD HH:MM:SS`. 다른 레포는 최근 `git log --oneline -5` 컨벤션을 따른다 (없으면 conventional commits).
- 원격 push 금지 (para 볼트는 obsidian-git 자동 백업이 담당).

---

### Task 1: para CLAUDE.md 세션 규칙 갱신

**Files:**
- Modify: `/Users/eunsol/Project/para/CLAUDE.md` (🔔 세션 시작 규칙 섹션, 파일 상단)

**Interfaces:**
- Consumes: 없음 (첫 태스크)
- Produces: 이후 모든 세션이 로드하는 도구 분업 규칙. Task 3의 `vibe delegate --tool`·`VIBE_HUB_TOOL` 명칭을 여기서 미리 문서화하므로 Task 3 구현은 이 명칭과 정확히 일치해야 한다.

- [x] **Step 1: 세션 시작 규칙 교체**

`/Users/eunsol/Project/para/CLAUDE.md`에서 아래 기존 블록을:

```markdown
## 🔔 세션 시작 규칙 (개인 컴)

- 개인 컴에서는 **agy(Antigravity)가 메인 툴**이다. Claude Code는 보조로 사용한다.
```

다음으로 교체한다 (이후의 NEXT-SESSION.md 관련 불릿들은 그대로 유지):

```markdown
## 🔔 세션 시작 규칙 (개인 컴)

- 개인 컴 도구 분업: **Claude Code = 허브(작업 관리·위임 지휘)·구현·커밋·오케스트레이션 / Gemini CLI = 조사·대량 컨텍스트(1M) 분석·문서화·웹 검색 / agy(Antigravity) = 브라우저 실검증·IDE형 보조 / Codex = 보류(자리 예약)**.
- 허브 도구는 교체 가능: `vibe main` 은 `VIBE_HUB_TOOL` 환경변수(기본 `claude`)로 허브 도구를 결정한다. Claude 팀 플랜 이탈 시 어댑터 교체 시나리오는 `01.Projects/개인컴_AI_작업환경_업그레이드/design.md` §3.3 참조.
- 프로젝트 작업 위임: `vibe delegate <프로젝트|경로> [--tool claude|gemini|codex] ["메시지"]` — 구현은 claude(기본), 조사·문서화는 `--tool gemini`. **Single-Writer 원칙**: 하나의 레포에 동시에 한 도구만 Write (위임 전 대상 레포 dirty 여부 확인).
- 화면 구성: 노트북 단독 = main-vertical(허브 좌 50% + 위임 pane 우측 스택, 3개째부터 cmux 승격) / 외장 모니터 = 장기 프로젝트를 `cmux-proj` 워크스페이스로 분리 배치.
```

- [x] **Step 2: 변경 검증**

Run: `grep -n "VIBE_HUB_TOOL" /Users/eunsol/Project/para/CLAUDE.md`
Expected: 1건 매치 (새 규칙 라인)

Run: `grep -n "agy(Antigravity)가 메인 툴" /Users/eunsol/Project/para/CLAUDE.md`
Expected: 매치 없음 (exit 1)

- [x] **Step 3: 커밋**

```bash
git -C /Users/eunsol/Project/para add CLAUDE.md
git -C /Users/eunsol/Project/para commit -m "DOC: backup $(date '+%Y-%m-%d %H:%M:%S')"
```

---

### Task 2: cmux-projects.txt 개인화

**Files:**
- Modify: `/Users/eunsol/Project/vibe-dotfiles/vibe-tools/cmux-projects.txt` (`~/.config/vibe-tools/`는 이 디렉토리 심링크 — 반드시 레포 쪽 경로를 수정)

**Interfaces:**
- Consumes: 없음
- Produces: cmux-proj 런처가 읽는 프로젝트 목록. 형식: `name|path|hexcolor|description|pin(선택)`

- [x] **Step 1: 업무 프로젝트 3줄 제거, 개인 프로젝트 2줄 추가**

기존 파일에서 아래 3줄을 삭제:

```
bshop|$HOME/Project/danawa/eshop/bshop|#B7410E|독립몰 (PHP/EUC-KR)
BillingMPAdmin|$HOME/Project/danawa/billing/BillingMPAdmin|#1A5276|빌링 마켓플레이스 어드민
PHPLib|$HOME/Project/danawa/global_library/PHPLib|#8E44AD|다나와 글로벌 공통 라이브러리 (PHP/EUC-KR)
```

같은 자리에 아래 2줄을 추가 (기존 vibe-dotfiles·vibe-ai-config·para 3줄은 그대로 유지):

```
legigraph|$HOME/Project/legigraph|#2E4053|입법 그래프 사이드 프로젝트 (설계 완료·구현 재개 대기)
grafana-test|$HOME/Project/grafana-test|#E67E22|Grafana 모니터링 실습 환경
```

- [x] **Step 2: 형식 검증**

Run: `grep -c '^[a-zA-Z]' /Users/eunsol/Project/vibe-dotfiles/vibe-tools/cmux-projects.txt`
Expected: 5 (주석(#) 제외 데이터 5줄 — para, vibe-dotfiles, vibe-ai-config, legigraph, grafana-test)

Run: `grep -n "danawa" /Users/eunsol/Project/vibe-dotfiles/vibe-tools/cmux-projects.txt`
Expected: 매치 없음 (exit 1)

경로 실존 확인:

Run: `ls -d /Users/eunsol/Project/legigraph`
Expected: 디렉토리 출력

Run: `ls -d /Users/eunsol/Project/grafana-test`
Expected: 디렉토리 출력

- [x] **Step 3: 커밋 (vibe-dotfiles 레포)**

먼저 컨벤션 확인: `git -C /Users/eunsol/Project/vibe-dotfiles log --oneline -5`

```bash
git -C /Users/eunsol/Project/vibe-dotfiles add vibe-tools/cmux-projects.txt
git -C /Users/eunsol/Project/vibe-dotfiles commit -m "chore(cmux): 개인 컴 프로젝트 목록으로 교체 (업무 3종 제거, legigraph·grafana-test 추가)"
```

(레포 로그가 다른 prefix 컨벤션이면 그에 맞춘다. 데이터 파일 3줄 교체이므로 worktree 격리 없이 main 직접 커밋 허용 — 소스코드 아님.)

---

### Task 3: vibe.sh `--tool` 옵션 + `VIBE_HUB_TOOL`

**Files:**
- Modify: `/Users/eunsol/Project/vibe-ai-config/claude-config/plugins/tmux-suite/scripts/vibe.sh`
  - `main)` 케이스: L146-166
  - `delegate)` 케이스: L315-390
  - help 텍스트: L504-534
- 격리: vibe-ai-config는 소스코드 변경이므로 **git worktree에서 작업 후 main 병합** (sop_git_branch 준수, 브랜치 1개)

**Interfaces:**
- Consumes: Task 1이 문서화한 명칭 — `--tool claude|gemini|codex`, `VIBE_HUB_TOOL`(기본 `claude`)
- Produces: `vibe delegate <대상> [--tool <t>] ["메시지"]`, `VIBE_HUB_TOOL=<t> vibe main`. pane 타이틀 `<tool>:<프로젝트명>`

- [x] **Step 1: worktree 생성**

```bash
git -C /Users/eunsol/Project/vibe-ai-config worktree add /Users/eunsol/Project/vibe-ai-config/.worktrees/feat-vibe-delegate-tool -b feat/vibe-delegate-tool
```

이후 편집은 전부 `.worktrees/feat-vibe-delegate-tool/claude-config/plugins/tmux-suite/scripts/vibe.sh` 대상.

- [x] **Step 2: `main)` 케이스에 허브 도구 파라미터화**

L153-155의 기존 코드:

```bash
    # 백그라운드 세션 생성 — win1(claude): 메인 에이전트
    tmux new-session -d -s "$PARA_SESSION" -n "claude"
    tmux send-keys -t "${PARA_SESSION}:claude" "claude" Enter
```

를 다음으로 교체 (창 이름 `claude`는 resume·cast가 참조하므로 변경 금지):

```bash
    # 백그라운드 세션 생성 — win1(claude): 메인 에이전트 (VIBE_HUB_TOOL 로 교체 가능, 기본 claude)
    HUB_TOOL="${VIBE_HUB_TOOL:-claude}"
    tmux new-session -d -s "$PARA_SESSION" -n "claude"
    tmux send-keys -t "${PARA_SESSION}:claude" "$HUB_TOOL" Enter
```

- [x] **Step 3: `delegate)` 케이스 인자 파싱을 `--tool` 지원으로 교체**

L316-317의 기존 코드:

```bash
    TARGET_ARG="${2:-}"
    MESSAGE="${3:-}"
```

를 다음으로 교체:

```bash
    shift
    TARGET_ARG=""
    MESSAGE=""
    TOOL="claude"
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --tool)
                TOOL="${2:-}"
                if [[ -z "$TOOL" ]]; then
                    echo "오류: --tool 값이 필요합니다 (claude|gemini|codex)" >&2; exit 1
                fi
                shift 2
                ;;
            *)
                if [[ -z "$TARGET_ARG" ]]; then
                    TARGET_ARG="$1"
                elif [[ -z "$MESSAGE" ]]; then
                    MESSAGE="$1"
                fi
                shift
                ;;
        esac
    done

    # 도구 검증: claude 는 통과, gemini/codex 는 설치 확인, 그 외 거부
    case "$TOOL" in
        claude) ;;
        codex)
            if ! command -v codex >/dev/null 2>&1; then
                echo "오류: codex 미설치 — 보류 상태(자리 예약). 설치 후 다시 시도하세요." >&2; exit 1
            fi
            ;;
        gemini)
            if ! command -v gemini >/dev/null 2>&1; then
                echo "오류: gemini CLI 가 설치되어 있지 않습니다." >&2; exit 1
            fi
            ;;
        *)
            echo "오류: 지원하지 않는 도구: $TOOL (claude|gemini|codex)" >&2; exit 1
            ;;
    esac
```

- [x] **Step 4: pane 실행·타이틀·준비 폴링을 도구 일반화**

L356-358의 기존 코드:

```bash
    # 새 pane 에서 claude 실행 (--continue 없이 대상 cwd 의 새 컨텍스트로 시작)
    # VIBE_DELEGATED=1 표식 주입 → 하위 claude 가 delegate 현장임을 인지해 별도 세션 생성 억제
    tmux send-keys -t "$NEW_PANE" "VIBE_DELEGATED=1 claude" Enter
```

를 다음으로 교체:

```bash
    # 새 pane 에서 선택 도구 실행 (--continue 없이 대상 cwd 의 새 컨텍스트로 시작)
    # VIBE_DELEGATED=1 표식 주입 → 하위 에이전트가 delegate 현장임을 인지해 별도 세션 생성 억제
    tmux send-keys -t "$NEW_PANE" "VIBE_DELEGATED=1 $TOOL" Enter
    tmux select-pane -t "$NEW_PANE" -T "${TOOL}:$(basename "$TARGET_DIR")"
```

L362-370의 준비 폴링 중 grep 패턴 라인:

```bash
            if [[ -n "$NEW_TTY" ]] && ps -t "$NEW_TTY" 2>/dev/null | grep -q "[c]laude"; then
```

를 도구 일반화 패턴으로 교체 (루프 시작 전에 `TOOL_PAT` 정의 추가):

```bash
        TOOL_PAT="[${TOOL:0:1}]${TOOL:1}"
```
(위 라인은 `NEW_TTY=...` 라인 바로 다음에 추가)

```bash
            if [[ -n "$NEW_TTY" ]] && ps -t "$NEW_TTY" 2>/dev/null | grep -q "$TOOL_PAT"; then
```

같은 블록의 안내 문구 `⚠️  claude 준비 확인 실패` 는 `⚠️  $TOOL 준비 확인 실패` 로 교체.

L388의 완료 echo:

```bash
    echo "🤝 위임 pane 생성 → $NEW_PANE  cwd=$TARGET_DIR  (현재 창 좌측 50% 고정, 신규 pane 은 우측 스택 맨 아래 append, 관찰 가능)"
```

를 다음으로 교체:

```bash
    echo "🤝 위임 pane 생성 → $NEW_PANE  tool=$TOOL  cwd=$TARGET_DIR  (현재 창 좌측 50% 고정, 신규 pane 은 우측 스택 맨 아래 append, 관찰 가능)"
```

- [x] **Step 5: help 텍스트 갱신**

L513 delegate 설명 라인을:

```
  vibe delegate <프로젝트|경로> [--tool claude|gemini|codex] ["메시지"] 현재 창에 split pane 생성 후 대상 cwd 로 선택 도구 위임(기본 claude, 경량·관찰 가능)
```

로 교체하고, L509 main 라인 아래 주석 성격으로 예시 섹션(L524-532)에 다음 2줄 추가:

```
  vibe delegate legigraph --tool gemini "레포 구조 조사해서 요약해줘"
  VIBE_HUB_TOOL=gemini vibe main       # 허브 도구 교체 (기본 claude)
```

- [x] **Step 6: 정적 검증 (VERIFY)**

Run: `bash -n /Users/eunsol/Project/vibe-ai-config/.worktrees/feat-vibe-delegate-tool/claude-config/plugins/tmux-suite/scripts/vibe.sh`
Expected: 출력 없음 (exit 0)

Run: `shellcheck /Users/eunsol/Project/vibe-ai-config/.worktrees/feat-vibe-delegate-tool/claude-config/plugins/tmux-suite/scripts/vibe.sh`
Expected: 변경 전 대비 **신규 경고 0건** (기존 경고는 비교 기준: 변경 전 원본에 shellcheck 실행해 두 결과를 비교)

기본 경로 회귀 확인 (문자열 수준):

Run: `grep -n 'TOOL="claude"' /Users/eunsol/Project/vibe-ai-config/.worktrees/feat-vibe-delegate-tool/claude-config/plugins/tmux-suite/scripts/vibe.sh`
Expected: 1건 (기본값 claude 보존)

- [x] **Step 7: 커밋 + main 병합 + worktree 정리**

먼저 컨벤션 확인: `git -C /Users/eunsol/Project/vibe-ai-config log --oneline -5`

```bash
git -C /Users/eunsol/Project/vibe-ai-config/.worktrees/feat-vibe-delegate-tool add claude-config/plugins/tmux-suite/scripts/vibe.sh
git -C /Users/eunsol/Project/vibe-ai-config/.worktrees/feat-vibe-delegate-tool commit -m "feat(tmux-suite): vibe delegate --tool 옵션·VIBE_HUB_TOOL 허브 파라미터화 (gemini/codex 멀티 CLI)"
git -C /Users/eunsol/Project/vibe-ai-config merge feat/vibe-delegate-tool
git -C /Users/eunsol/Project/vibe-ai-config worktree remove /Users/eunsol/Project/vibe-ai-config/.worktrees/feat-vibe-delegate-tool
git -C /Users/eunsol/Project/vibe-ai-config branch -d feat/vibe-delegate-tool
```

(push 는 하지 않는다 — 사용자 확인 후 별도.)

- [ ] **Step 8: 스모크 테스트 (선택 — tmux 세션 안에서만 가능, 사용자 수동)**

사용자 또는 tmux 내부 세션에서 수동 확인:
- `vibe delegate para` → 기존과 동일하게 claude pane 생성 (회귀 확인)
- `vibe delegate para --tool gemini` → gemini pane 생성, 타이틀 `gemini:para`
- `vibe delegate para --tool codex` → "codex 미설치 — 보류 상태" 오류 후 종료

---

### Task 4: Gemini settings.json PAT 환경변수 이전

**Files:**
- Modify: `/Users/eunsol/.gemini/settings.json` (L41 — github MCP env 블록)
- Modify(append): `/Users/eunsol/.zshrc.local` (git 미추적 — 없으면 생성)

**Interfaces:**
- Consumes: 없음
- Produces: `GITHUB_PERSONAL_ACCESS_TOKEN` 환경변수 (gemini CLI 가 settings.json 의 `$VAR` 문법으로 해석)

**주의: 토큰 실값을 계획·로그·git 추적 파일에 절대 기록하지 않는다.**

- [x] **Step 1: 토큰을 ~/.zshrc.local 로 이전**

`/Users/eunsol/.gemini/settings.json` L41에 있는 현재 토큰 값(`github_pat_...`)을 복사해 `/Users/eunsol/.zshrc.local`에 append (파일이 없으면 생성):

```bash
# Gemini CLI github MCP 용 (settings.json 에서 $GITHUB_PERSONAL_ACCESS_TOKEN 참조)
export GITHUB_PERSONAL_ACCESS_TOKEN="<settings.json L41 의 기존 값>"
```

- [x] **Step 2: settings.json 에서 평문 제거**

L41을:

```json
        "GITHUB_PERSONAL_ACCESS_TOKEN": "$GITHUB_PERSONAL_ACCESS_TOKEN"
```

으로 교체 (gemini CLI 는 settings.json 값의 `$VAR`/`${VAR}` 환경변수 해석을 지원).

- [x] **Step 3: 검증**

Run: `grep -c "github_pat_" /Users/eunsol/.gemini/settings.json`
Expected: 0 (grep exit 1)

Run: `grep -c "github_pat_" /Users/eunsol/.zshrc.local`
Expected: 1

JSON 유효성:

Run: `python3 -m json.tool /Users/eunsol/.gemini/settings.json`
Expected: 정상 파싱 출력 (단, 이 명령은 stdout 에 토큰이 포함될 수 있으므로 출력은 확인 후 버린다 — 이미 평문 제거됐으므로 안전)

새 셸에서 gemini github MCP 동작 확인 (수동): `gemini mcp list` 또는 gemini 세션에서 github 도구 호출.

- [x] **Step 4: 사용자 액션 안내 (구현 밖)**

기존 토큰은 이미 평문 노출 이력이 있으므로 **GitHub → Settings → Developer settings 에서 재발급(rotate)** 을 권장. 재발급 시 `~/.zshrc.local` 값만 갱신하면 된다. (에이전트가 대신 할 수 없음 — 보고에 명시.)

---

### Task 5: 마무리 — NEXT-SESSION.md·design.md 상태 갱신

**Files:**
- Modify: `/Users/eunsol/Project/para/NEXT-SESSION.md`
- Modify: `/Users/eunsol/Project/para/01.Projects/개인컴_AI_작업환경_업그레이드/design.md` (상태 라인)

**Interfaces:**
- Consumes: Task 1-4 완료 상태
- Produces: 차기 세션 인수인계 정보

- [x] **Step 1: design.md 상태 갱신**

`- 상태: 설계 승인 대기 (A안 구두 승인 완료, 문서 검토 대기)` 라인을 `- 상태: 구현 완료 (YYYY-MM-DD) — 잔여: GitHub PAT 재발급(사용자), Codex 편입(보류)` 으로 교체 (실제 날짜 기입).

- [x] **Step 2: NEXT-SESSION.md 에 완료 기록 추가**

`## 🧹 정리 작업` 섹션 위에 다음 블록 추가:

```markdown
## ✅ 완료 — 개인컴 AI 작업환경 업그레이드 (YYYY-MM-DD)

- Claude 허브 + Gemini 분업 체제 구성 완료. `vibe delegate <프로젝트> --tool gemini` 로 조사·문서화 위임, `VIBE_HUB_TOOL` 로 허브 교체 가능.
- 설계·계획: `01.Projects/개인컴_AI_작업환경_업그레이드/`
- 잔여 사용자 액션: GitHub PAT 재발급 (기존 토큰 평문 노출 이력) → `~/.zshrc.local` 값 갱신
```

최종 갱신 날짜 라인(`**최종 갱신: ...**`)을 오늘 날짜로 갱신.

- [x] **Step 3: 검증 + 커밋**

Run: `grep -n "개인컴 AI 작업환경" /Users/eunsol/Project/para/NEXT-SESSION.md`
Expected: 1건 이상 매치

```bash
git -C /Users/eunsol/Project/para add NEXT-SESSION.md "01.Projects/개인컴_AI_작업환경_업그레이드/design.md"
git -C /Users/eunsol/Project/para commit -m "DOC: backup $(date '+%Y-%m-%d %H:%M:%S')"
```

---

## 실행 전략 메모

- Task 1·5 = para(cwd 내부). Task 2·3·4 = cwd 외부 파일 — 백그라운드 서브에이전트는 cwd 외부 Edit/Write 권한이 거부되므로, **메인 세션이 직접 수행**하거나 tmux 환경에서는 `vibe delegate vibe-ai-config` / `vibe delegate vibe-dotfiles` pane 위임으로 수행한다.
- Task 4의 토큰 값은 화면·로그에 에코하지 않는다 (Read 로 확인 후 Edit 로만 이동).
