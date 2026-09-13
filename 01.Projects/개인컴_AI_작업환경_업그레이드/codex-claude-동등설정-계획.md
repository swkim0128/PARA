---
title: Codex · Claude Code 동등 설정 계획
status: todo
created: 2026-09-09
project: 개인컴_AI_작업환경_업그레이드
---

# Codex · Claude Code 동등 설정 계획

> **목표**: 정본 하나 → 두 도구에 같은 설정이 배포된다. 메인/서브 전환은 `VIBE_HUB_TOOL` 한 줄이면 끝나야 한다.
> **당장의 운영**: 모델 사용량 때문에 **Claude Code 메인 유지**. Codex는 서브로 동등하게 준비만 해둔다.
> **근거**: 2026-09-03~08 실측 (`vibe-ai-config/docs/settings-inventory.md` · `.claude/work-log/2026-09-04.md`·`2026-09-08.md`).

## 0. 원칙 (이미 정본에 있는 것 — 재확인)

1. **정본은 하나, 도구는 어댑터.** `shared/` 가 도구 무관 정본, `claude/`·`codex/` 는 경로·메커니즘 번역만. 규칙 본문 복제 금지.
2. **도구가 합성(import)을 못 하면 생성(generate)한다.** Claude `settings.json` 을 base+overlay 로 생성하는 선례. 생성물은 정본이 아니며 `install.sh` 만 쓴다.
3. **배포 명령은 `./install.sh [personal|work]` 하나.** 도구별 배포 스크립트를 따로 만들지 않는다.
4. **강제는 지시문이 아니라 훅·권한으로.** 단, Codex 훅은 **미신뢰 시 fail-open** 이므로 신뢰 절차가 없는 네이티브 수단(`rules/`)을 우선한다.
5. **검증은 파서로.** TOML 은 `tomllib`, JSON 은 `jq`, 셸은 `shellcheck`. 눈으로 보지 않는다.

## 1. 현재 상태 — 계층별 동등성 표

| 계층 | 정본 | Claude 소비 | Codex 소비 | 동등성 |
|---|---|---|---|---|
| 공통 규칙 | `shared/rules/AGENTS.md` | `~/.claude/AGENTS.md` 심링크 + `CLAUDE.md` 가 `@import` | `~/.codex/AGENTS.md` 심링크 | ✅ |
| 도구 어댑터(명령 레지스트리·위임 관용구) | `claude/CLAUDE.md`·`CLAUDE-commands.md` | `@import` 상시 로드 | **없음** — 전역 파일 1개만 읽음 | ❌ |
| 프로젝트 규칙 | 각 레포 `AGENTS.md` | `CLAUDE.md` = `@AGENTS.md` + 꼬리 | `AGENTS.md` 네이티브 + `project_doc_fallback_filenames=["CLAUDE.md"]` | ⚠️ vibe-ai-config ✅ · vibe-dotfiles fallback 의존 |
| 스킬 | `skills/` → `~/.agents/skills` | 심링크 | 심링크(62개 인식) | ✅ |
| MCP | `claude/mcp.base.json` **와** `codex/mcp.toml` | jq 병합 → `~/.claude.json` | `codex mcp add` | ❌ **정본 2개** |
| 권한 allow(100) | `settings.base.json` | 네이티브 | **없음** → 매 명령 승인 | ❌ |
| 권한 deny/ask(39) | `settings.base.json` | 네이티브 | `permission-guard.sh` 훅(정본을 읽음, fail-open) | ⚠️ |
| 훅 | `claude/hooks/`(전용) + `shared/hooks/`(도구무관, **어느 쪽도 미배선**) | `settings.json` 직접 배선 | `codex/hooks.json` → 일부 shim | ⚠️ 이중 구조 |
| 상태줄 / HUD | claude-dashboard ↔ `codex/tui.toml` + codex-hud | | | ➖ 성격상 별개, 동등 대상 아님 |
| 배포기 | `install.sh` | ✅ | `install_codex_*` — **config.toml 쓰기 결함**(§2 P0) | ⚠️ |
| 전환 스위치 | `VIBE_HUB_TOOL` (`zshrc.local.template`) | | | ✅ 존재 — 현재 미커밋 `codex` 로 변경돼 있음 |

## 2. 단계 계획

각 단계는 `[작업] → verify: [정적 검사]` 형식. 앞 단계가 끝나야 다음으로.

### P0 — 즉시 (Claude 메인 유지 상태에서 안전 확보)

| # | 작업 | verify |
|---|---|---|
| 0-1 | **`VIBE_HUB_TOOL` 을 `claude` 로 되돌린다.** `vibe-dotfiles/zsh/zshrc.local.template` 미커밋 변경(`codex`) 폐기 + `~/.zshrc.local` 원복. Codex 메인은 P1~P3 완료 후. | `zsh -c 'source ~/.zshrc.local; echo $VIBE_HUB_TOOL'` = `claude` |
| 0-2 | **`install_codex_tui` 결함 수정** — ① 루트 키 구획(`codex/config-root.toml`)을 `config.toml` **맨 앞**(첫 `[` 헤더 앞)에 ② `[tui]` 구획은 끝에 ③ 마커 사이에 소스에 없는 실질 줄이 있으면 **삭제 대신 중단** ④ BEGIN만 있고 END 없으면 중단 ⑤ 쓰기 전 `.bak.<ts>` 백업 | `python3 -c 'import tomllib…'` 로 `d["project_doc_fallback_filenames"]==["CLAUDE.md"]`, 전후 파싱 비교에서 관리 키 제외 전부 동일, 3회 연속 실행 출력 동일 |
| 0-3 | 훅 신뢰 재확인 — **사용자만** `/hooks` → `t`. 추정 복원·자동 승인 금지. | `/hooks` 의 `Active` 열 = `Installed` 열 |
| 0-4 | 미푸시 5건 · para 미커밋 5건 정리, `stash@{0}` 드롭 판단 | `git status -sb` 클린 |

### P1 — 정본 단일화 (같은 파일이 두 도구를 먹인다)

| # | 작업 | verify |
|---|---|---|
| 1-1 | **MCP 정본 통합** — `claude/mcp.base.json` 만 남기고 `codex/mcp.toml` 폐기. `install.sh` 가 같은 JSON에서 Claude 병합 + `codex mcp add` 를 생성. | `codex mcp list` 서버 집합 == `jq '.mcpServers\|keys' mcp.base.json` |
| 1-2 | **권한 allow 이식** — `settings.base.json` `permissions.allow` 100건 → `install.sh` 가 `~/.codex/rules/vibe.rules` 로 **생성**(`prefix_rule(pattern=[argv…], decision="allow")`). Claude 패턴 `Bash(git add:*)` → argv 접두 `["git","add"]` 변환기 작성. | Codex 매뉴얼(28963~29098행, Codex 보고)의 `execpolicy check` 로 규칙 파일 검증 · 대표 명령 3종 무프롬프트 실행 |
| 1-3 | **권한 deny/ask 를 rules 로 이관** — 매뉴얼상 decision `allow/prompt/forbidden` 지원(Codex 보고, **본인 미검증 → 먼저 확인**). 지원되면 `permission-guard.sh` 훅 폐기 → **fail-open 문제 소멸**. 미지원분만 훅에 남긴다. | `chmod -R 777 <scratch>` → forbidden, `git push` → prompt, `git status` → allow. **훅 없이** 재현 |
| 1-4 | **훅 이중 구조 해소** — `shared/hooks/` 를 두 도구 공통 배선으로 승격. Claude: `settings.base.json` hooks 를 `shims/claude.sh <hook>` 호출로 전환(현재 미배선). Codex: `hooks.json` 전부 `shims/codex.sh`. `codex/hooks/*.sh` 전용 스크립트는 `core/` 로 이관 또는 rules 이식 후 삭제. | `shared/hooks/test.sh` 확장 — 훅 × {claude,codex} 계약 검증 통과 |

### P2 — 어댑터 층 동등화

| # | 작업 | verify |
|---|---|---|
| 2-1 | **명령 레지스트리 도구 무관화** — `CLAUDE-commands.md` 의 도구 무관 부분(`vibe delegate`·`vibe peek`·`para-work`·세션·워크스페이스)을 `shared/commands.md` 로 이동. Claude 는 `@import`, Codex 는 2-2 의 꼬리에 concat. Claude 전용(슬래시 명령·플러그인)만 `CLAUDE-commands.md` 에 잔류. | `grep -c` 로 두 파일 간 중복 항목 0 |
| 2-2 | **Codex 전역 어댑터 생성** — `install.sh` 가 `~/.codex/AGENTS.md` = `shared/rules/AGENTS.md` + `shared/commands.md` + `codex/AGENTS.tail.md` 를 **생성**(심링크 대체). tail = Codex 전용 위임 관용구·경로만. 32 KiB 상한 확인. | `codex --ask-for-approval never "Summarize the current instructions."` 가 레지스트리 항목을 인용 · `wc -c` < 32768 |
| 2-3 | `harness-reminder` 를 Codex 표현(서브에이전트 관용구)으로 재작성해 `prompt-gates` 에 통합 | 구현 의도 프롬프트 → `additionalContext` 주입 확인 |
| 2-4 | `config-drift-check.sh` 에 생성물 해시(AGENTS.md 생성본·rules·hooks.json) 추가 → 정본과 어긋나면 SessionStart 경고 | 정본 수정 후 재기동 시 경고 1회, install 후 무출력 |

### P3 — 프로젝트 규칙 동등화

| # | 작업 | verify |
|---|---|---|
| 3-1 | `vibe-dotfiles/AGENTS.md` 신설(para·vibe-ai-config 패턴: `AGENTS.md` 정본 + `CLAUDE.md` = `@AGENTS.md` + 꼬리). fallback 은 안전망으로 유지. | Codex 를 dotfiles 에서 실행 → 규칙 인용 |
| 3-2 | `para/AGENTS.md` 크기 점검(전역+프로젝트 합 32 KiB 상한) | `wc -c` 합산 |

### P4 — 전환 리허설

| # | 작업 | verify |
|---|---|---|
| 4-1 | `VIBE_HUB_TOOL=codex` 로 **임시** 토글 → `vibe main` 이 Codex 허브를 띄우고 위임·peek·개인관리(Notion MCP) 가 동작하는지 체크리스트 | 체크리스트 전항 ✅ 후 `claude` 원복 |
| 4-2 | `status/<env>.md` 스냅샷에 Codex 섹션(rules 수·hooks Active·AGENTS 생성본 해시) 추가 | 두 머신 스냅샷 `diff` 로 판별 가능 |

#### 4-1 리허설 체크리스트 (2026-09-13 작성 — 전항 ✅ 전에는 토글 확정 금지)

전제(9/13 실측 완료): `install.sh personal` head `0720742` 드리프트 0 · `hooks.json` `_note→description`(`c9f9227`) · `/hooks` 6건 신뢰(`[hooks.state]` 6 해시) · notion OAuth 로그인 완료.

| # | 항목 | 방법 | 결과 |
|---|---|---|---|
| R1 | `vibe` 가 Codex 비대화형 셸에서 실행됨 | Codex 에서 `vibe cast` | ✅ 9/13 `f311099` — `~/.local/bin/vibe → vibe.sh` 심링크(tmux-suite install 5단계) + vibe.sh 심링크 실경로 해석. Codex 셸 `vibe cast` 정상 |
| R2 | 위임 pane 생성 | Codex 에서 `vibe delegate <경로> --tool claude "…"` → pane 생성·메시지 주입 | ✅ 9/13 새 Codex 세션(0.154.0)에서 `vibe cast` 정상 응답 |
| R3 | `TMUX` 환경 전달 | Codex Bash 에서 `tmux display-message -p '#{pane_id}'` | ✅ `TMUX=/private/tmp/tmux-501/default,…` · pane `%4` 전달 확인 |
| R4 | SessionStart `briefing-inject` | Codex 새 세션 첫 응답이 NEXT-SESSION 착수 지점을 인용 | ✅ 새 세션에 `# NEXT-SESSION — 개인 컴 작업 브리핑` 주입 확인 |
| R5 | SessionStart `config-drift-check` | 정본 1줄 교란 → 새 세션에 경보 → 원복 | ✅ 9/9 교란→경보→원복 실측 + 9/13 재배포 후 무출력 |
| R6 | PreToolUse `bash-chain-guard` | Codex 에 `echo a && echo b` 실행 요청 → 차단 문구 | ✅ `echo a && echo b` → “셸 체이닝 '&&' 감지” 차단 |
| R7 | PreToolUse `curl-terminal-guard` | curl 터미널 출력 요청 → 차단 | ✅ `curl -sI` → “curl 을 에이전트 셸로 직접 실행할 수 없습니다” 차단 |
| R8 | UserPromptSubmit `prompt-gates` | 구현 요청 프롬프트에 게이트 문구 주입 | ✅ 프롬프트에 `🧭 하네스 3단계 — 구현 의도 감지` 주입 |
| R9 | PostToolUse `activity-log` | `~/.local/share/vibe-hooks/` 에 Codex 행 기록 | ✅ `~/.local/share/vibe-hooks/activity/2026-09-13.jsonl` 에 `harness:codex` 행 기록 |
| R10 | rules | `sudo ls` → forbidden · `git push` → prompt · `git status` → allow (런타임) | ✅ sudo ls=forbidden · git push=prompt · git status=allow |
| R11 | 개인관리 루틴 | Codex 에서 notion MCP 로 이번 주 일지 페이지 조회 1회 | ✅ Diary DB 에서 `[week 37] 09.09 ~ 09.18 일지` 조회 |
| R12 | `VIBE_HUB_TOOL=codex vibe main` | Codex 허브 기동 + 상태줄 five-hour/weekly 표시 | ⏳ 사용자 육안 — 토글 확정 시 수행 |
| R13 | `install.sh` 재실행 안전 | Codex 가 `[hooks.state]` 를 관리 구획 안에 쓴 상태에서 install 통과 + 해시 보존 | ✅ 9/13 `226d109` — 구획 안 외부 테이블을 END 뒤로 보존 이동, hooks.state 6건 유지, doctor 0 warn |

토글 확정 시 함께: `AGENTS.md`(para) 「도구 분업·위임 기본값」 절 · `vibe-dotfiles/zsh/zshrc.local.template` · 4-2 스냅샷.

## 3. 동등화 불가 — 문서로만 남기는 것

| 항목 | 사유 |
|---|---|
| `WorktreeCreate` 훅 | Codex 훅 이벤트에 없음 |
| `Write`/`Edit`/`Task` 의미 훅(`settings-guard`·`subagent-first-*`·`install-sync-check`) | Codex 는 `apply_patch`·서브에이전트 모델이 다름 |
| HUD 시각 동등 | Codex `status_line` 은 고정 항목 열거형, 커스텀 렌더 불가. 성격상 별개로 두고 tmux 2행 바가 교차 잔량을 맡는다 |
| Claude `Agent(subagent_type…)` 지시문 | Codex 표현으로 재작성(2-3), 원문 이식 불가 |

## 4. 결정이 필요한 것

1. **0-1 원복 승인** — dotfiles `VIBE_HUB_TOOL=codex` 미커밋 변경을 버리고 `claude` 로. (Claude 메인 유지와 정합)
2. **1-3 rules 의 deny/ask** — 매뉴얼 지원 확인 결과에 따라 `permission-guard.sh` 훅을 **폐기**할지. 폐기가 맞다(fail-open 제거)고 보지만 확인 후 결정.
3. **`stash@{0}` 드롭**.

## 5. 이 계획이 지키는 것 / 깨지 않는 것

- 정본 수는 **줄어든다** (MCP 2→1, 훅 구조 2→1, 명령 레지스트리 도구 종속 → 무관).
- `install.sh` 는 여전히 하나. 생성물은 Claude `settings.json` · Codex `AGENTS.md`·`rules/`·`hooks.json`·`config.toml` 구획 — 전부 `install.sh` 만 쓴다.
- 업무 프로필(`work`)은 건드리지 않는다.
- 훅 신뢰·원격 push·삭제는 사용자 단계.
