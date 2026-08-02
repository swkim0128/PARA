# 계획: agy(Antigravity) ↔ Claude Code 설정 패리티

> 작성 2026-07-29 · 상태: **계획(승인 대기)** · 요청: "개인환경 메인=agy 확정, agy 설정을 Claude Code와 동일하게"

## 0. 목표 (2026-07-29 재정의)

**최근 변경한 Claude Code 설정을 "전역 AI 도구 설정"의 정본(SoT)으로 삼아 모든 AI 도구(agy·gemini·codex 등)에 반영한다.** 개인 메인=agy 확정은 유지하되, 방향은 "agy를 Claude에 맞춘다"가 아니라 **"최근 Claude 설정 = 새 글로벌 정본 → 전 도구 전파"**.

- 핵심 delta: Claude 스킬의 **`npx skills` 전환**(업무컴 선반영). 이 방식(단일 SoT `skills/` → npx skills로 전 도구 심링크 배포)을 전역 표준으로 승격.
- **2026-07-22 install.sh TOOLS-루프 설계는 stale** — 업무컴 Claude 변경 이전 의도. 현행 목적에 맞게 재정렬 대상.
- 두 하네스 메커니즘 차이로 "파일 복사"가 아닌 "계약 이식"은 여전히 유효(§1-C 표준 지형 참조).

### 0-A. 당면 스코프 (우선 착수) + 전역 공유 요건
- **당면 목적**: 최근 변경한 전역 Claude MD 규칙(허브 `CLAUDE.md` + `CLAUDE-commands.md` + `CLAUDE-delegation.md`) 내용을 **agy에도 반영**.
- **전역 공유 요건(2026-07-29 추가)**: agy 반영 후, 이 설정이 **전역 공유**되어야 함 = vibe-ai-config SSoT에 커밋·push → 전 머신(개인·업무)·전 도구가 동일 수령. 로컬 배포본만 고치는 것 금지(config-change 규율).
- **구조 함의 (중요)**: "전역 공유"가 성립하려면 정본 규칙이 **Claude 전용 `claude-config/CLAUDE.md`가 아니라 공유 `shared/` 정본**에 있어야 함. 현재 최근 변경은 claude-config에만 있고 agy 소스(`coding-partner.md`)엔 없음 → **정본을 shared/로 승격·일원화**가 선행되어야 양쪽이 한 소스에서 파생 가능.
  - 최근 델타(git): `d371746`(CLAUDE-commands.md 신규+허브 라우팅), `f30121e`(§5 @import 로드), `8ccd2a6`(CLAUDE-user.md 포인터 제거), `68b19f3`(superpowers 제거).
  - 난점: 최근 변경이 Claude `@import`(`@~/.claude/CLAUDE-commands.md`)에 의존 → agy가 @import 미지원 시 **평탄화(flatten) 인라인** 필요. (조사 에이전트 `research-rules-sync.md`가 확정 중.)

---

## 1. 조사 결론 (계획을 바꾸는 핵심 사실)

### 1-A. 기존 agy 어댑터 경로가 최신 공식과 불일치 (중요)
`antigravity/install.sh`(2026-07-08 실측 기반)가 쓰는 경로 중 상당수가 현행 Antigravity CLI 공식 문서와 어긋난다:

| 항목 | 기존 어댑터(2026-07-08) | 공식 현행(2026-07 확인) | 판정 |
|---|---|---|---|
| 글로벌 규칙 | `~/.agents/AGENTS.md` 심링크 + `~/.gemini/GEMINI.md` 블록 | **`~/.gemini/GEMINI.md`(auto-load)** + 워크스페이스 `AGENTS.md`/`GEMINI.md` | GEMINI.md 블록 ✅ / `~/.agents/AGENTS.md` ❌ 근거 없음 |
| 워크플로우 | `~/.agents/workflows/*.md` | 홈 레벨 workflows 없음 — 절차는 **스킬**로 표현 | ❌ 경로 무효 |
| 스킬(글로벌) | (미배포) | **`~/.gemini/antigravity-cli/skills/`** (npx skills CLI 문자열은 `~/.gemini/antigravity/skills/` 로 보임 — 실측 검증 필요) | 경로 확정 필요 |
| 훅 | 미구현("v2 후보") | **5종**(PreToolUse·PostToolUse·PreInvocation·PostInvocation·Stop), `.agents/hooks.json` 또는 `~/.gemini/config/hooks.json` | 신규 구현 대상 |
| MCP | `~/.gemini/config/mcp_config.json` (`url`/`serverUrl` 투영) | `~/.gemini/config/mcp_config.json` ✅ — 단 원격은 **`serverUrl` 필수**(구 `url`/`httpUrl` 무음 실패) | 키 교정 필요 |
| 권한 | `~/.gemini/antigravity-cli/settings.json` union | 동일 ✅ | OK |

→ **기존 어댑터는 "MCP·권한·GEMINI.md 블록"은 맞지만, `~/.agents/` 홈경로(규칙·워크플로우·스킬)는 무효**. 스킬 미배포·훅 미구현.

### 1-B. `npx skills`가 antigravity 타겟을 지원
- 70+ 에이전트 지원(`claude-code`·`cursor`·`codex`·`antigravity`·`gemini-cli`·`opencode`…). 심링크 기본, 단일 SoT.
- 한 SKILL.md 세트를 Claude+Antigravity 동시 배포 가능: `npx skills add <repo> -a claude-code -a antigravity --all`
- ⚠ Antigravity 글로벌 스킬 타겟 경로 문서(`antigravity-cli/skills`) vs CLI 문자열(`antigravity/skills`) 불일치 → **실측 검증 필수**.

### 1-C. 표준화 지형 (AAIF/Linux Foundation, 2025-12~)
- **표준화됨**: 규칙=**AGENTS.md**, 프로토콜=**MCP**. (Claude는 AGENTS.md 네이티브 미독 → `@import`/심링크 브릿지 필요.)
- **미표준(도구별 브릿지 필수)**: 스킬(SKILL.md는 de-facto), 권한(전부 독자 포맷), 훅/커맨드/서브에이전트.

### 1-D. 성숙한 통합 도구 존재 (전략 분기의 핵심)
- **agentsync** — SoT `~/.agentsync/`, `agentsync apply`가 도구별 네이티브로 변환. MCP·메모리·스킬·플러그인·슬래시커맨드·서브에이전트·훅·LSP 통합, 암호화 시크릿, lossy-projection 리포트. **Antigravity 명시 지원**(31 에이전트).
- **rulesync** — `npx rulesync`, 규칙+MCP+권한을 20~30개 도구로 생성. 기존 CLAUDE.md/.cursorrules import 가능.
- **dot-agents** — `~/.agents/` 심링크 모델(규칙·스킬·훅·설정, 권한 제외).
- 다중 머신 전송은 **chezmoi** 권장.

---

## 1-E. 규칙 반영 메커니즘 (조사 확정 — 3차 조사 `research-rules-sync.md`)

- **Antigravity도 `@import` 지원**(Gemini 메모리 프로세서, 5단계 중첩·순환감지) — 단 Antigravity 자체 문서는 저신뢰, 경로 방언 상이(Claude `@~/…` vs Gemini `@./`·`@/abs/`).
- **`~/.gemini/GEMINI.md`는 Gemini CLI와 경로 충돌**(bug #16058). 사용자는 Gemini CLI도 병용 → **agy 규칙 타겟을 `~/.gemini/AGENTS.md`로 전환 권장**(Antigravity는 읽고 Gemini CLI는 기본 미독).
- **채택 방식 = flatten(평탄화) 하이브리드**: Claude 허브를 정본 유지 + agy용은 허브의 `@import`를 **인라인 결합(flatten)**해 단일 규칙 블록 생성 → 경로 방언·@import 저신뢰 문제 원천 회피. (심링크는 대안이나 로드 테스트 필수. 동기화 툴 rulesync/ai-rules-sync는 `@import`를 번역 못하고 경고만 → 부적합.)

**확정 사실**: Claude 상시 로드 규칙 = `CLAUDE.md`(허브) + `@CLAUDE-commands.md` 뿐. `CLAUDE-delegation.md`=온디맨드, `coding-partner.md`=허브 미로드.

**반영 설계(당면)**:
1. SoT: `claude-config/CLAUDE.md` + `CLAUDE-commands.md` 정본 유지(이미 shared repo → git으로 전역 공유).
2. **flatten 제너레이터 신규**: 허브의 `@import` 해석해 (허브+commands) 단일 md 생성.
3. **agy 주입**: `antigravity/install.sh`가 flatten 결과를 관리 블록으로 주입, 타겟 **`~/.gemini/AGENTS.md`**(GEMINI.md에서 전환).
4. **전역 공유**: 제너레이터+어댑터 변경 vibe-ai-config 커밋·push.

**설계 결정 필요**:
- D1: agy 타겟 `~/.gemini/AGENTS.md` 전환(권장·충돌회피) vs 현행 `GEMINI.md` 유지(2026-07-08 자동로드 실증).
- D2: agy 규칙 내용 = Claude 상시셋(허브+commands)만 **정확히 일치**(coding-partner 페르소나 드롭) vs 허브+commands+coding-partner 페르소나 **병기**(agy에 톤·자가검증 유지).

## 2. 전략 분기 (사용자 결정 필요)

우리의 현재 스택(hand-rolled `install.sh`+`deploy-links.sh`+`antigravity/install.sh`)이 이미 이 문제를 수동으로 풀고 있다. 두 갈래:

- **전략 A — 기존 hand-rolled 어댑터 교정·확장** (제어권 유지, 학습비용 0, 유지보수 자가부담)
  - `antigravity/install.sh`의 무효 경로(`~/.agents/*`) 제거·교정, 스킬 배포 추가, 훅 5종 구현, MCP `serverUrl` 교정.
- **전략 B — agentsync 도입** (Antigravity 공식 지원·훅/스킬/권한 일괄·유지보수 위임, 신규 도구 의존·마이그레이션 비용)
  - 정본을 `~/.agentsync/`로 이관, `agentsync apply`로 Claude+agy 동시 생성. 기존 스크립트는 폐기 또는 축소.

> **권고**: 우선 **전략 A로 최소 교정**(경로·MCP·스킬·규칙 격차)해 즉시 패리티를 확보하고, 병행으로 **agentsync를 PoC**(비파괴, 별도 브랜치)로 평가 후 전환 여부 결정. 이유: 기존 스택이 이미 80% 동작(MCP·권한·GEMINI.md)하므로 전면 이관보다 격차 교정이 저비용·저위험.

---

## 3. 패리티 격차별 작업 항목 (전략 A 기준)

### G1. 규칙 내용 격차 (위임 코어 누락)
- 문제: `shared/rules/coding-partner.md`(agy·Claude 공통 SoT)에 Claude 허브 §5(**Subagent-first·vibe delegate·모델 라우팅·Explore/Plan 매핑**)와 위임 상세가 없음 → agy가 위임 규율 미수령.
- 작업: 위임 코어를 도구무관 형태로 `coding-partner.md`에 추가(경로 의존 표현은 라우터 꼬리에 분리) → `build-*-user.sh` 재실행으로 양쪽 파생.
- verify: 생성물 diff, agy `/context`로 주입 확인.

### G2. 스킬 배포 (npx skills 전환) — **[확정] Claude+agy 공통**
- 결정(2026-07-29): 업무용 컴이 이미 Claude 스킬을 `npx skills`로 전환 → **개인 컴도 동일 방향**. 선택 아님, 필수.
- 문제: (Claude) `install.sh`가 `install_skills` 손수 심링크로 `~/.claude/skills` 생성 = CLI 미사용. (agy) 스킬 미배포 + `~/.agents/skills` 무효 경로.
- 작업:
  - **Claude**: `install.sh`의 `claude)` 케이스 `install_skills "$CLAUDE_DIR/skills"` → `npx skills add <repo> -a claude-code --skill '*' -g -y`(심링크 모드)로 교체. 정본=레포 top-level `skills/`. 플러그인은 스킬 미보유(orphaned)라 이중로드 없음.
  - **agy**: `antigravity/install.sh`에 `npx skills add <repo> -a antigravity --skill '*' -g -y` 추가.
  - 한 명령 통합 가능: `npx skills add <repo> -a claude-code -a antigravity --all -g -y`.
  - **선행 실측 게이트**: (a) 로컬 레포를 소스로 쓰는 방법(`npx skills add <local-path>` 지원 여부), (b) agy 글로벌 스킬 경로(`antigravity-cli/skills` vs `antigravity/skills`), (c) **업무용 컴이 쓴 정확한 invocation/flags 확인해 일치**(불일치 시 SSoT로 통일).
- verify: Claude `/skills`·agy `/skills`로 72종 로드 확인, 이중로드 없음 확인.

### G3. 훅 5종 신규 구현
- 문제: agy 훅 미구현. Claude의 가드(bash 체이닝 금지·경계 검증·activity-logger)가 agy엔 없음.
- 작업: `antigravity/hooks.json` 작성(PreToolUse matcher `run_command` → bash 체이닝 검사 등), `install.sh`가 `~/.gemini/config/hooks.json`로 배치. camelCase 필드(`toolCall`…) 준수.
- 범위 주의: Claude 13종 훅 중 agy 5종에만 매핑 가능 — 나머지는 이식 불가(문서화).
- verify: agy `/hooks` 목록 확인.

### G4. MCP serverUrl 교정
- 작업: `antigravity/install.sh`의 MCP 변환 jq에서 원격 서버 `url`/`httpUrl` → `serverUrl` 매핑 추가.
- verify: `jq empty mcp_config.json`, agy `/mcp` 로드 확인.

### G5. 권한 패리티 점검
- 작업: `agy-permissions.json`의 allow/ask가 Claude deny(원격 MR self-approve 등 최신 4종 포함) 정신과 정합한지 점검. 포맷 상이(패턴 vs exact-path)로 lossy — 핵심 파괴적 명령만 보장.

### G6. (연관) Claude 설정 스킴 일원화 — 선행
- 문제: 라이브 `~/.claude/settings.json` = `settings.personal.json` 심링크(구 스킴) vs 최신 커밋은 `settings.base.json`+overlay(신 스킴) → 최근 deny 4종 미적용.
- 작업: `install.sh personal` 재실행으로 base+overlay 생성형 전환, deploy-links.sh 심링크 스킴 폐기 정리.
- verify: `jq empty ~/.claude/settings.json`, deny 4종 존재 확인.

---

## 4. 실행 순서 (승인 후)

1. **G6 선행**: Claude 설정 스킴 일원화(저위험, 즉시 효과).
2. **G1 규칙**: coding-partner.md 위임 코어 추가 → 양쪽 재생성.
3. **G4 MCP serverUrl 교정** + **G2 스킬 npx 전환**(경로 실측 먼저).
4. **G3 훅 5종** 구현.
5. **G5 권한 점검**.
6. 통합: `antigravity/install.sh` 재실행 → agy 재시작 → `/context`·`/skills`·`/mcp`·`/hooks` 검증.
7. (병행/후속) **agentsync PoC** 평가 → 전략 B 전환 여부 재결정.

## 5. 리스크
- Antigravity 스킬 경로 문서/CLI 불일치 → 실측 없이는 스킬 배포 실패 가능. **G2 착수 전 실측 게이트**.
- agy 훅 스키마(camelCase·5종)는 실기 검증 필요 — 문서만으로 오작동 가능.
- 편집 대상 대부분 vibe-ai-config(cwd 외부) → config-change 규율상 패널 위임 또는 설정레포 master 직접 편집.

## 6. 미결 결정
- [ ] 전략 A(교정) vs B(agentsync) — 권고: A 우선 + B PoC 병행.
- [x] **Claude 스킬 npx skills 전환 → 확정(2026-07-29, 업무용과 동일). G2에 반영.**
- [ ] 훅 이식 범위(가드 전부 vs 핵심만).
- [ ] G6(설정 스킴 일원화) 선착수 여부.
