# 개인 컴 멀티 AI CLI 작업 환경 설계 (A안 — 확정)

- 작성일: 2026-07-17
- 상태: 구현 완료 (2026-07-17) — 잔여: GitHub PAT 재발급(사용자, 2026-08-06 진행 안 하기로 결정), **Codex 편입(2026-08-14 착수 확정)**
- 관련 레포: para(본 볼트), vibe-ai-config, vibe-dotfiles, ~/.gemini
- **이력**: 2026-07-21 본 설계를 뒤집고 agy(Antigravity) 허브로 전환 → **2026-08-14 철회, 본 설계(Claude Code 허브)로 복귀**. 사유는 agy 실사용 품질 미달(Flash 모델·토큰 만료). 동시에 §6 비범위였던 Codex 어댑터 채우기가 구독 확정(ChatGPT Plus)으로 착수 항목이 됨.

## 1. 배경과 목표

업무용 컴의 AI 작업 환경(cmux + tmux + vibe 런처 + Claude 하네스)이 개인 컴에 이식 완료된 상태에서, 개인 컴 고유 조건에 맞춰 업그레이드한다.

- 개인 컴은 Claude Code 단독이 아니라 **Gemini CLI를 병행**하고, Codex CLI는 추후 편입한다.
- para 허브에서 작업을 관리하다가 프로젝트 작업이 필요하면 **해당 프로젝트의 AI 도구를 pane 또는 워크스페이스로 열어** 작업한다 (업무 컴과 동일한 허브-위임 모델).

## 2. 확정 결정사항

| 항목 | 결정 |
| --- | --- |
| 구독 플랜 | Claude Pro/Max(회사 팀 플랜 경유) + ~~Gemini AI Pro/Ultra~~ → **ChatGPT Plus**(2026-08-14 전환: Google AI Pro 축소) |
| Codex | ~~보류~~ → **편입 확정(2026-08-14)** — `--tool codex` 는 `vibe delegate` 가 도구 무관 구조라 이미 동작. 남은 일은 `vibe-ai-config/codex/` 어댑터(MCP) 채우기 |
| 허브 도구 | **Claude Code** (vibe/cmux 위임 인프라·notion-suite·훅이 전부 Claude 기반). 단, Claude 접근이 회사 팀 플랜 의존이라 **허브 역할은 교체 가능하게 설계** (§3.3) |
| Gemini 역할 | **작업 성격별 분업** — 조사·대량 컨텍스트(1M) 분석·문서화·웹 검색 |
| agy(Antigravity) | 보조로 전환 — 브라우저 실검증·IDE형 대량 분석 시 사용 |
| 모니터 | 상황마다 다름(노트북 단독 ⇄ 외장 모니터) — 두 시나리오 모두 대응 |

## 3. 아키텍처 — 허브-위임 모델 + 도구 선택 확장

### 3.1 도구 라우팅 테이블

| 작업 성격 | 도구 | 실행 경로 |
| --- | --- | --- |
| 작업 관리·노션 루틴·위임 지휘 | Claude Code | `vibe main` → para 허브 pane |
| 구현·커밋·코드리뷰·오케스트레이션 | Claude Code | `vibe delegate <프로젝트>` |
| 대량 컨텍스트(1M) 분석·웹 검색 | Gemini CLI | `vibe delegate <프로젝트> --tool gemini` |
| 조사·2nd opinion·보조 구현 | Codex CLI | `vibe delegate <프로젝트> --tool codex` (2026-08-14 편입). 훅·서브에이전트 지원 확인(2026-08-17) — 허브 후보이기도 함 |
| ~~브라우저 실검증·IDE 작업~~ | ~~agy (Antigravity)~~ | 보류(2026-08-14) |

> ✅ **Codex 훅 미지원 판단은 오판 — 2026-08-17 실측으로 철회.** `codex-cli 0.147.0` 은 훅 11종(`PreToolUse`·`PermissionRequest`·`PostToolUse`·`SessionStart`·`SessionEnd`·`UserPromptSubmit`·`SubagentStart/Stop`·`Stop`·`Pre/PostCompact`)을 지원하며 차단 규약(exit 2 + stderr, `permissionDecision:deny`)·출력 필드명이 Claude Code 와 거의 동일하다. 설정은 `~/.codex/hooks.json`이고 훅마다 `trusted_hash` 신뢰 계층이 추가로 있다(Claude 에는 없는 계층). 서브에이전트(`spawnAgent`·`default_subagent_model`)·스킬·플러그인·마켓플레이스도 지원하고, `.claude/` 설정 임포트 모듈(`external-agent-migration`)이 내장돼 있다.
>
> 따라서 **Codex 를 위임 전용으로 묶는 구조적 근거는 없다.** 현재 Claude 허브 유지는 스킬 57개·플러그인 15개·`vibe` 인프라의 전환 비용 판단일 뿐이며, 필요해지면 재검토 가능한 사안이다. (실사용 검증은 `codex login` 이후 — 현재 미인증)

**Single-Writer 원칙 유지**: 하나의 레포에는 동시에 한 도구만 Write. Gemini pane과 Claude pane이 같은 레포를 잡지 않도록 위임 시 허브가 점유 상태(`git status` dirty 여부)를 확인한다.

### 3.2 화면 구성

- **기본 (노트북 단독)**: tmux main-vertical — 좌 50% para 허브(Claude), 우측 스택에 위임 pane(Claude/Gemini 혼재 가능). pane 2개 초과 시 가독성이 떨어지므로 3번째부터는 cmux 탭 또는 워크스페이스로 승격.
- **외장 모니터**: 허브 워크스페이스는 노트북 화면, 장기 작업 프로젝트는 `cmux-proj`로 별도 cmux 워크스페이스를 외장 모니터에 배치.
- **열람**: 변경 확인은 `vibe peek <프로젝트> diff` (cmux diff surface 자동 승격) — 기존 규칙 그대로.
- **에스컬레이션 기준(기존 규칙 준용)**: 장기 체류·강격리 → `cmux-proj` / 멀티 레포 이슈 → `cmux-issue`.

### 3.3 허브 도구 교체 가능성 (De-risking)

Claude Code 접근은 회사 팀 플랜에 의존하므로, 팀 플랜 이탈 시 agy 또는 Codex가 메인이 될 수 있다. 이에 대비해 **허브를 특정 도구에 하드코딩하지 않는다**:

1. **허브 도구 파라미터화**: `vibe main`도 delegate와 동일하게 도구 선택을 지원 (`VIBE_HUB_TOOL` 환경변수, 기본 `claude`). 허브 교체 = 환경변수 1줄 변경.
2. **SoT는 도구 무관 파일로 유지**: 작업 인수인계(NEXT-SESSION.md·TASKS.md), 규칙 정본(vibe-ai-config/shared/ — coding-partner.md·SOP 5종), 개인관리 SOP(02.Areas/07.개인관리/)는 전부 마크다운이라 어떤 도구든 읽고 이어받을 수 있음. Claude 전용 스킬(notion-suite 등)이 없어도 SOP 폴백 경로가 이미 정의돼 있음.
3. **어댑터 구조 활용**: vibe-ai-config의 shared → 어댑터(claude-config / antigravity / codex) 빌드 구조가 이미 존재. 허브 교체 시 해당 어댑터를 채우는 것이 유일한 추가 작업 (Codex 어댑터 채우기가 그 시나리오의 첫 단계).

## 4. 구현 항목 (4건)

### 4.1 vibe.sh `--tool` 옵션 추가 — `vibe-ai-config` 레포

- `vibe delegate <프로젝트> [--tool claude|gemini|codex] ["메시지"]` — 기본값 `claude`(기존 동작 100% 보존).
- `--tool gemini`이면 pane에서 `gemini` CLI를 대상 프로젝트 cwd로 실행. 초기 메시지 전달은 gemini CLI 인자 규격에 맞춰 처리(미지원 시 pane에 프롬프트만 준비).
- `--tool codex`는 미설치 시 "codex 미설치 — 보류 상태" 안내 후 종료(자리 예약).
- `VIBE_DELEGATED=1` 마커·pane 타이틀 규칙은 도구 무관 동일 적용. pane 타이틀에 도구명 표기(예: `gemini:legigraph`).
- `vibe main`은 `VIBE_HUB_TOOL` 환경변수(기본 `claude`)로 허브 도구를 결정 — §3.3 허브 교체 대비.
- 검증: `bash -n` + `shellcheck` 통과, `vibe delegate <proj>`(무옵션) 기존 동작 회귀 확인.

### 4.2 cmux-projects.txt 개인화 — `vibe-dotfiles` 레포

- 제거: 업무 전용 3종 (bshop, BillingMPAdmin, PHPLib — 개인 컴에 레포 없음).
- 유지: para(pin), vibe-dotfiles(pin), vibe-ai-config.
- 추가: legigraph, grafana-test (현재 NEXT-SESSION.md 활성 프로젝트 기준). 이후 필요 시 추가 등록.

### 4.3 GitHub PAT 보안 이전 — `~/.gemini/settings.json`

- settings.json의 평문 PAT를 제거하고 환경변수 참조(`$GITHUB_PERSONAL_ACCESS_TOKEN` 등 gemini CLI 지원 문법)로 교체.
- 실제 토큰 값은 `~/.zshrc.local`(git 미추적)에 export. **노출된 기존 토큰은 사용자가 GitHub에서 재발급/폐기** (사용자 액션 필요).

### 4.4 para CLAUDE.md 세션 규칙 갱신 — 본 볼트

- "agy(Antigravity)가 메인 툴" 문구를 본 설계로 교체: **Claude Code = 허브·구현 / Gemini = 조사·대량분석·문서화 / agy = 브라우저 검증 보조 / Codex = 보류(예약)**.
- 도구 라우팅 테이블(§3.1)과 화면 구성 규칙(§3.2) 요약을 반영.
- `NEXT-SESSION.md`에 본 프로젝트 항목 추가.

## 5. 구현 순서·범위·롤백

- 순서: 4.4(볼트, cwd 내부) → 4.2 → 4.1 → 4.3. 4.1이 유일한 코드 변경이며 나머지는 설정·문서.
- 4.1/4.2는 각 레포 규율에 따라 격리 브랜치(worktree)에서 외과수술식으로 수행.
- 롤백: 전부 git 추적 파일(4.3의 토큰 값 제외)이라 revert로 즉시 복구 가능.

## 6. 비범위 (YAGNI)

- ~~Codex 어댑터(`vibe-ai-config/codex/`) 채우기 — 구독 확정 후 별도 작업.~~ → **2026-08-14 범위로 승격**(ChatGPT Plus 구독 확정). 현재 `codex/` 는 AGENTS.md 심링크 + MCP 1종(`sequential-thinking`)뿐 — agy 가 쓰던 7종 수준으로 `~/.codex/config.toml` 을 채우는 것이 다음 작업.
- Gemini용 위임 자동화 훅·서브에이전트 매핑 — pane 수동 위임으로 시작, 필요해지면 추가.
- launchd 자동화 신규 추가 없음 (기존 3종 유지).
