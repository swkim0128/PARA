# 🖥️ NEXT-SESSION — 개인 컴 작업 브리핑

> **이 파일은 세션 간 인수인계 SoT다.** 개인 컴에서 에이전트(Claude Code 허브·구현, Codex/Gemini 보조·조사) 세션을 열면
> 가장 먼저 이 파일을 읽고 최상위 작업의 "다음 행동"부터 이어서 진행한다.
> 작업 단위가 끝나면 해당 항목의 상태·다음 행동을 갱신하고 저장한다 (obsidian-git이 자동 백업).

**최종 갱신: 2026-09-23**

## 🔜 다음 세션 착수 지점 — 작업별 모델 선택·Jev 연동 (2026-09-23)

- 상세: [[작업별-모델-라우팅-20260923]]. `vibe-ai-config` 정본에 작업별 모델 실행기와 Jev 선택 연결 구현. `vibe run`으로 새 작업 시작 시 적용하며 전역 기본 모델은 유지한다.
- 분류: routine=Luna/low, implement=Terra/medium, review=Sol/medium, deep=Astra/high. 사전 작업 매핑 우선, 미등록 요청은 명시한 비민감 요약으로 선택적 Jev 분류.
- 검증: SDK 모의 HTTP 포함 테스트 통과, 실제 launcher dry-run·정적 검증 통과. 실서비스 Jev 및 Codex 모델 응답은 미검증.
- 🚫 **Jev 는 무기한 대기 (2026-09-23 확정)**: typesafe.ai 가입·로그인이 막혀 키 발급 자체가 불가하다. 재개 시점은 외부에 달려 있다. 코드는 키 부재 시 로컬 기본값으로 안전 강등되므로 **제거하지 않고 휴면 상태로 존치**한다. 실호출 검증 하네스는 준비돼 있고 키만 들어오면 4케이스를 한 번에 돌린다.
- 그 결과 **로컬 규칙 분류가 주 경로로 승격**됐다. Jev 는 선택적 보강으로 내린다.
- 남은 범위: 기존 TUI의 매 입력 자동 전환은 미구현(설계·실현가능성은 확인됨 — 노트 참조). 생성 AGENTS 배포·커밋·푸시는 하지 않음.
- 다음 행동: 로컬 분류기의 과매칭 수정 마무리 → 커밋·배포 판단. 매 입력 자동 라우팅은 `codex --remote` + `turn/start` 가로채는 프록시로 **TUI 재작성 없이** 가능하다(노트에 실측 근거·정정 3건).
- 아래 개인관리·웹 리서치 프로젝트 상태와 기존 미커밋 파일은 보존했다.

## 🔜 다음 세션 착수 지점 — 노션 프로젝트 확인 후 웹 리서치 엔진 테스트 대기 (2026-09-23, 최신)

### 노션 Projects DB 확인 결과

개인 태그 프로젝트를 조회하고 사용자가 알려준 진행 상황을 관련 태스크에 반영했다.

| 우선 검토 | 프로젝트 | 노션 상태 | 우선순위 | 종료일 | 판단 |
|---|---|---|---|---|---|
| 1 | [[집 정리]] | In progress | 높음 | 2026-10-31 | 바닥 정리 완료. 책상·부엌 짐 정리 진행 중 |
| 2 | [[벌크업]] | In progress | 높음 | 2026-11-23 | 식단 기록 재가동·7일 기준선·장보기/보충제 태스크가 기한 경과 |
| 3 | [[2026 하반기 지출 예산 및 가용 금액 계획]] | In progress | 높음 | 2026-12-01 | 하반기 예정 지출·가용 금액 산정. 블랙프라이데이는 하위 구매 시점 |
| 4 | [[대구 본가 4박 5일 (9/22~9/26)]] | Planning | 중간 | 2026-09-26 | 현재 진행 중인 일정으로 종료일 임박 |
| 5 | [[웹 리서치 자동화 엔진]] | Planning | 중간 | 미지정 | 테스트는 이 프로젝트 확인 후 진행. 열린 태스크 행은 조회되지 않음 |
| 6 | [[overnight_worker launchd 설정]] | In progress | 낮음 | 미지정 | 우선순위 낮은 진행 항목 |

### 웹 리서치 자동화 엔진(PRO-132) 다음 행동

- 쿠팡 쓰기 테스트 및 실행기 TODO는 **노션 프로젝트 확인 이후로 보류**한다.
- 노션 프로젝트 상태는 `Planning` 그대로 둔다. 구현 산출물의 존재만으로 상태를 추정해 변경하지 않는다.
- 테스트 재개 시 순서: 쿠팡 쓰기 테스트 결과 확인 → `recipes/coupang.yaml`의 검증·원복 필드 확정 → 실행기 TODO 2개(YAML→JSON 빌드, `buildReplScript`) 처리.
- 기존 안전 규칙(상태 사전 확인 없는 토글 금지, 원복·외부 상태 검증 필수)은 유지한다.

### 현재 개인 프로젝트 작업

- `집 정리`: 노션 태스크 `1회차 — 바닥 정리`를 `Done`으로 변경했다. 기존 통합 태스크는 `책상·부엌 짐 정리 실행`으로 바꾸고 `In progress`로 전환했다.
- `2026 하반기 지출 예산 및 가용 금액 계획`: 프로젝트 제목을 하반기 범위로 정정했다. 블랙프라이데이는 하위 구매 시점으로 유지하고, 태스크는 `2026 예정 지출 품목·가용 금액 정리`로 정정했다.
- 11월까지 관리 기준: 9~11월 수입금, 예정 지출 품목·금액·결제월, 고정생활비를 확정한 뒤 가용 금액을 계산한다. 목적저축 100만원은 우선 확보하고 비상금 344만원은 분리 보존한다.
- 수입금은 월 2,845,000원으로 동일하며 9~11월 총수입 기준은 8,535,000원이다. 다음 작업은 리프트업 수납침대·인덕션·에어프라이어·수면안대·의류의 예상 금액과 결제월을 확정하는 것이다.
- 이번 달 확정 실지출은 PT 330,000원 + 레이저 제모 358,000원 + 치아교정 검증 100,000원 = 788,000원이다. 치아교정 총 예상비용 5,300,000원에 검증 비용이 포함되므로 향후 잔여 치료비는 약 5,200,000원이다.
- 최신 운영 기준: 월 수입 2,845,000원 중 1,630,000원은 고정·변동 운영 예산, 300,000원·150,000원·100,000원은 일반 저축, 블랙프라이데이 목적자금 1,000,000원은 11월 16일까지 별도 확보한다. 예정 품목은 예산 외 지출로 구매 가능 여부를 판정한다.
- 11월까지 예정 지출: 월 운영예산 9~11월 합계 4,890,000원, 예산 외 확정·계획 항목 약 6,900,000원(축의금 700,000원 + 교정 잔여 5,200,000원 + 블랙프라이데이 1,000,000원). 구매 후보 7종은 금액 미정으로 별도 판정한다.
- 10월 1일 교정치과 방문 예정. 당일 교정비 일부 결제 가능성이 있으므로 결제액·분할납부·다음 결제일을 확인한 뒤 11월 현금흐름을 갱신한다.

### PARA 동기화 범위

- 이 브리핑과 오늘 작업 로그에 노션 조회 결과, 집 정리 진행 상태, 블랙프라이데이 품목 정리 태스크를 반영했다.
- 로컬 미커밋 파일(`Jev` 자료·집 정리 이미지·`nvim.log`·기존 작업 로그)은 이번 동기화에서 건드리지 않는다.

## 🔜 다음 세션 착수 지점 — 웹 자동화 엔진 A축 (2026-09-20 새벽, **최신**)

**이 절이 아래 모든 과거 브리핑보다 우선한다.** 상세는 [[.claude/work-log/2026-09-19]] (자정 넘겼지만 연속 세션이라 같은 파일).

> 🤝 **도구 전환**: 2026-09-20 새벽 Claude Code → **Codex 로 인계**. 아래 「Codex 인계 메모」를 먼저 읽을 것.

### A. 웹 리서치 자동화 엔진 (PRO-132) — A축 recipe 3종 + 실행기 스켈레톤 🔴 진행 중

**신규 레포 `~/Project/web-research-engine`** (2026-09-20 생성, 커밋 `bad6b31`, **리모트 없음·미푸시**).
노션 정본 [PRO-132](https://app.notion.com/p/3e0a25196d348147bac3fb522e522232) — 유스케이스·A/B 축 분리·실측 결과가 전부 기재돼 있다.

**핵심 판단(이미 내려짐 — 되돌리려면 근거부터 볼 것)**
- 유스케이스 3건 중 2건(찜·장바구니, 위시 등록)은 **스케줄 반복 대상이 아니다** → 엔진을 **A축(온디맨드 액션) / B축(무인 반복 조사)** 으로 분리. 노션 문서의 기존 Phase 1~5 는 **B축 계획**이다.
- **유스케이스 3(상품정보 → 노션 위시)은 이미 구현돼 있다** — `notion-budget` 스킬의 「상품 페이지 → 위시 등록」 절. **재개발 금지**, 연결만 하면 된다.
- **A축에 raw CDP 직접 구현은 불필요.** Aside 브라우저가 그 역할을 한다. raw CDP 는 B축(launchd 무인 실행)에서만 값을 한다.
- `chrome-devtools-mcp` 는 이 세션에서 **연결 실패**했다(메인 Chrome 이 9222 를 열고 `DevToolsActivePort` 도 있는데 못 찾는다고 함 — **원인 미규명**). 그래서 Aside 로 전환했다.

**완료**
- recipe 포맷 **v0.3** 확정 (`docs/recipe-format.md`). **모든 필드가 실측된 실패 양상 하나에 대응한다** — 근거는 `docs/findings-2026-09-20.md`. 3사이트가 모든 축에서 달라서 검증에 최소 3개가 필요했다.
- **스마트스토어**(`aria-pressed`) · **오늘의집**(접근성 이름 토글) 쓰기 테스트 **완주·원복 확인**. 186→187→186 / 102→101.
- 실행기 스켈레톤 `src/run-recipe.mjs` — recipe 로드 + **안전 게이트** + 실행 계획 출력. `node --check` 통과.

**🔴 다음 한 걸음**
1. **쿠팡 쓰기 테스트 결과 확인** — 인계 시점에 Aside 에서 **실행 중이었다**(상품 페이지 여는 중, **찜 클릭 전**). 결과를 확인해 `recipes/coupang.yaml` 의 `revert.same_element: UNKNOWN` 과 `verify` 를 확정할 것. 진행 로그: `/private/tmp/claude-501/-Users-eunsol-Project-para/26be54c3-*/tasks/b232ra64g.output`
2. **실행기 TODO 2개** — ①YAML→JSON 빌드 단계(런타임 의존성 0 원칙 때문에 파서 미도입) ②`buildReplScript()` 미구현. ⚠️ **`aside repl "..."` 은 호출마다 새 세션이라 `page`·`const` 가 유지되지 않는다** — 한 액션의 전 과정을 **단일 REPL 호출용 JS** 로 생성해야 한다. 여기가 다음 구현 지점이다.
3. `notion-budget` 위시 등록과의 연결 지점 정의 (유스케이스 3)

**🚫 타협 금지 안전 규칙** (`README.md`·실행기 게이트에 집행됨)
- **상태를 모르는 토글은 실행하지 않는다.** 찜은 토글이라 이미 찜된 대상을 다시 누르면 **해제된다** — "찜해줘" 가 "찜 해제" 로 조용히 뒤집힌다. 쿠팡이 실제로 이 케이스다(`state.by: external_list`, `fragility: HIGH`).
- `revert` 없는 액션은 자동화 대상에서 제외 · 로그인은 추측 금지(미로그인이면 사용자에게 요청) · 성공 판정은 "눌렀다" 가 아니라 "상태 재조회에서 보인다".
- **`login_gate` 에 사용자명 문자열을 기대값으로 하드코딩하지 않는다** — 사이트마다 표시 체계가 다르다(쿠팡=실명 / 오늘의집=닉네임, **같은 계정**). 지표는 개인 영역의 존재 여부로 잡는다.

### 🤝 Codex 인계 메모

- **Single-Writer**: 이 세션(Claude Code)은 종료한다. `web-research-engine` 과 `para` 양쪽 다 Codex 가 단독 Write 로 이어받는다.
- **레포 상태** — `web-research-engine`: 커밋 `bad6b31` 1개, 워킹트리 clean, **리모트 미설정**(푸시하려면 원격 생성 필요). `para`: 미커밋 다수(`para-work backup` 은 사용자 판단). `vibe-ai-config`: 커밋 `0101c3a` **미푸시** + Instapaper 9건 미커밋.
- **열린 pane**: `%7`(이 세션 claude, 종료 예정) · `%3`(zsh) · `%12`(claude, vibe-ai-config — Phase 5·6·4 완료 후 유휴).
- **Aside 세션이 쿠팡 쓰기 테스트를 돌고 있다.** 완료되면 스스로 찜을 해제하도록 지시돼 있다. 중간에 죽었으면 `wish-web.coupang.com/wishInitView.pang` 에서 `국내산 애플민트, 10g, 1개` 가 남아 있는지 확인하고 있으면 해제할 것.

### B. 이월 — 어제 완료분

- **vibe-ai-config 배치 개선 Phase 1~6 전부 완료** (`0101c3a` 미푸시). 사용자 판단 대기 6건은 아래 A절 참조.
- **Jev 개인 전용 분리 완료** (`feat/jev-personal` 브랜치, 커밋 `8988aff` 미푸시).
- **Archify 개념 설명 완료** — 코드 로직 표현 가능 여부 조사까지 끝. 결론: 부분적으로 가능하며 코드 `파일:줄` 근거(`sources`) 기재는 `architecture` 타입 전용.
- 🔴 **정리 대기(사용자가 내일 진행하기로 함)**: `rm -rf ~/.cache/web-research-engine` (149M, Claude 가 만든 Chrome 디버그 프로필 — Aside 채택으로 불필요해짐).

---

## 🔜 이전 착수 지점 — Archify·Jev 도입 (2026-09-19, 위 절로 대체됨)

상세는 [[.claude/work-log/2026-09-19]].

### A. Archify · Jev 도입 — **Archify 개인 배포됨(미커밋) · Jev 개인 전용 분리 커밋 완료** 🔴 진행 중

계획 정본 [[01.Projects/개인컴_AI_작업환경_업그레이드/archify-jev-도입계획-20260919]] (조사 완료 · Phase A~C · verify 게이트 2개 · 결정 5건 §6).

- **사용자 결정(9/19)**: Archify는 개인·업무 공통 로컬 도구로 배포. **Jev는 개인 데이터 전용이며, 업무 설정·업무 데이터에는 연결하지 않는다.**
- **완료(A-1~A-4)** — `/private/tmp/archify-v2.16.0`에 안정 태그를 격리 clone(`git describe`=`v2.16.0`)했고 CLI help exit 0·벤더 후보 7.3MB를 확인했다. Instapaper MCP 첫 다이어그램은 showcase 9/9·error/warning 0, A-3 엣지 5건 전부 `파일:줄` 근거 있음, `deliver` SHA-256 영수증 및 local Chrome visual-check까지 통과했다.
- **Archify 배포 상태** — `/Users/eunsol/Project/vibe-ai-config/.git/worktree/chore-archify`의 미커밋 변경으로 `skills/review/archify`를 벤더링하고 개인 설치를 실행했다. 현재 `~/.agents/skills/archify` 및 Claude 스킬 심링크는 이 worktree를 가리킨다. 배포 검증은 `doctor`·`demo`·showcase 9/9·visual-check 통과. 커밋 전에는 worktree를 삭제하거나 다른 설치를 실행하지 않는다.
- **Jev 개인 전용 분리 — 완료·커밋됨 (2026-09-19 밤, Claude Code 이어받음)** — Codex pane `%11`이 5시간 한도 소진으로 작업 로그 기록 직전 `Failed to apply patch`로 중단됐고(코드 변경 자체는 온전), Claude Code가 재검증 후 완주했다.
  - 브랜치 `feat/jev-personal` (워크트리 `.git/worktree/jev-personal`, 이전 detached HEAD 에서 분기), 커밋 **`8988aff`** — 4파일 +80. **미푸시** (푸시는 사용자 판단).
  - 구성: `profiles/personal.conf` 에 기본 비활성 `JEV_ENABLED=0` + Keychain 서비스명만(키 값 없음) · `install.sh` 는 `MODE=personal && JEV_ENABLED=1` 일 때만 `~/.local/bin/vibe-jev` 배포 · 래퍼 `shared/scripts/jev-personal.sh` 는 Keychain 키를 자식 프로세스에만 `TYPESAFE_API_KEY` 로 전달 · 정책 문서 `docs/jev-personal-policy.md`.
  - 검증: `bash -n install.sh` 통과 · `shellcheck shared/scripts/jev-personal.sh` 경고 0 · 배선 순서(프로필 source L74 → `INSTALL_LINKS` L127 → Jev 분기 L163) · `~/.local/bin/vibe-jev` 미존재로 기본 비활성 실증 · `profiles/work.conf` 무변경.
  - 워크트리 작업 로그는 `.gitignore` 의 `.claude/*` 로 커밋 대상이 아니다(로컬 기록).
- **다음 한 걸음** — Archify 개념 설명을 사용자에게 제공한다. 이후 `chore/archify` 워크트리의 미커밋 4건(`skills/review/archify/` 벤더링 포함) 커밋 여부를 판단한다.
- 🔴 **중단 게이트 2개** — A-3(생성된 모든 엣지를 소스 `파일:줄` 과 대조, 근거 없는 엣지 0건) · C-4(슬랙 멘션 골든셋 30건에서 Jev 가 현행 Opus 보다 정확도 낮으면 편입 안 함).
- **C-1 은 개인 전용 사용자 단계** — console.typesafe.ai/settings/keys 에서 키 발급 시도(대기자 명단이면 등록만). 발급되면 개인 Keychain `vibe-ai-config.typesafe.api-key` 로 저장하며, 업무 계정·업무 데이터에는 사용하지 않는다.
- 조사 요약: Archify = 렌더러+검증기(분석은 에이전트가 함) · 런타임 의존성 0 · 외부 통신은 업데이트 확인 1건뿐(`ARCHIFY_UPDATE_CHECK_DISABLED=1` 로 차단) · `visual-check` 는 로컬 Chrome 을 CDP 로 구동. Jev = SDK 실재(PyPI 0.7.0 / npm 0.6.0) · `jev-latest`→`jev-1.13.0` · 64k/요청, state 32k · Choice 255개.


### B. Instapaper MCP — 배포까지 완료, **사용자 단계만 남음**

Codex 가 오전에 하다 사용량 한도로 멈춘 것을 Claude Code 로 완주했다. Codex 전용 MCP 이며 **기본 비활성으로 배포**된 상태다.

- 실측 완료: 래퍼 심링크 · `~/.codex/config.toml` 관리 구획(`enabled` = 불리언 `false`) · `codex mcp list` exit 0 · `install.sh personal` 멱등 · 더미 자격증명 stdio 핸드셰이크(도구 **26개**) · Keychain 가드 exit 1.
- 수정 1건: 래퍼 SC2155 — Keychain 항목이 없어도 빈 값으로 기동되던 것을 사유+등록 명령 출력 후 `exit 1` 로.
- **발견**: MCP 본체는 인증 실패해도 죽지 않고 계속 서비스한다 → 승인 전에 켜면 "붙어는 있는데 전 호출 실패" 상태. 그래서 활성화 전 인증 확인 절차를 `docs/instapaper-mcp.md` 에 추가했다.

**🔴 다음 한 걸음 (사용자 단계)**
1. Instapaper 개발자 API 승인 신청·수령 (https://www.instapaper.com/api) — consumer key·secret
2. Keychain 4개 항목 등록 (`docs/instapaper-mcp.md` 의 `security add-generic-password` 4줄) — **현재 전부 미등록**
3. 인증 확인 `~/.codex/instapaper-mcp.sh < /dev/null` → `Failed to authenticate` 없으면 통과
4. `INSTAPAPER_MCP_ENABLED=true ./install.sh personal` → Codex 재시작

**미결**: Phase 1·2·3 은 **커밋·푸시 완료**(`master` = `3229576`, `origin/master` 와 동기 — 9/19 Codex 세션). master 워킹트리에 남은 미커밋은 **Instapaper 관련 9건뿐**(`codex/instapaper-mcp.sh`·`codex/instapaper-mcp.toml`·`docs/instapaper-mcp.md`·`install.sh`·`shared/mcp.base.json`·`codex/README.md`·`codex/config-root.toml`·`status/personal.md`·`.codex/`) — 커밋·푸시는 사용자 판단. Instapaper 위임 pane `%10`은 9/19 Codex 세션에서 종료했다.

---

## 🔜 카페 작업 종료·집에서 재개 (2026-09-13 저녁, 위 절로 대체됨)

9/13 카페에서 Claude Code(Opus/Fable)로 작업. 아래 두 갈래가 열려 있다. 이 절이 아래 모든 과거 브리핑보다 우선한다.

### A. vibe-ai-config 배치 개선 — **Phase 1~6 전부 완료·커밋됨 (미푸시)** ✅

계획 정본 [[01.Projects/개인컴_AI_작업환경_업그레이드/shared-배치-개선계획-20260913]] (근거 감사 4건 · Phase 별 verify 게이트 · 결정 §9).

- ~~**HEAD = `c99a80d` 그대로. 미커밋 47개 파일**~~ → **2026-09-19 커밋·푸시 완료** (`3229576` "refactor(shared): 공용 자산을 shared/ 로 재배치 + Codex 호환·가드 정비"). 위 최신 절의 「미결」 참조.
- 완료: **Phase 1**(mcp.base.json·delegate-pane-guard → shared, 사문 훅 격리, gitignore 키 보호, preamble 로더 디커플링, references → shared) · **Phase 3**(git-guard 출력형식, pane 도구판정, auto-version-bump 안전가드, readonly-allow 모순제거) · **Phase 2**(sops Codex 배포, install-sync-check 코어승격, drift/smoke/test Codex 커버리지, 문서 허위 정정) · **3-C**(analyze 훅 19개→단일 static-checks.js, **처음으로 발화 시작**).
- 검증 최종: `test.sh` PASS=22 FAIL=0 · `smoke-hooks.sh` 26건 실패 0(rc=127 소멸) · `install.sh personal` ❌0·멱등 · `drift-report` 드리프트 없음 · `codex --profile routine mcp list` exit 0.
- ~~**남은 것: Phase 5 → 6 → 4**~~ → **2026-09-20 00:04 완료** (pane `%12` 위임, 커밋 **`0101c3a`** "fix(hooks): Codex 미발화 훅 복구 + _unused 회수원 정리 + zshrc 빈 줄 누적 수정" — **미푸시**).
  - **전제 정정**: Phase 4·5·6 의 **본체는 이미 `3229576` 에 들어 있었다**(스크립트 이동 14종·규약/매핑표·회수 가드 2종 전부 실재, 계획서 헤더의 "완료(미커밋)" 표기가 낡았던 것). 실제 잔여는 §6-Z·§7-B 의 🔴 항목이었고 그것을 수행했다.
  - **Phase 5** — `analyze` PreToolUse matcher 가 `Read|Edit|Write` 라 `php-encoding-check.sh` 가 **Codex 에서 영구 미발화**였다(5-B 규약의 유일한 위반). matcher 에 `apply_patch` 추가 + 스크립트에 `file_path` 폴백(Codex `apply_patch` 필드명 미확정 → `tool_input` 문자열 리프에서 경로 추출)을 **한 쌍으로** 수정하고, 재발 방지를 위해 `test.sh` 에 matcher 린트를 넣어 결정론적으로 승격했다.
  - **Phase 6** — `_unused/` 회수원 3개 + 빈 매니페스트 1개 삭제, `hooks.json` 사문 참조 4종 제거(대체재 실재를 정적 대조로 확정한 뒤).
  - **Phase 4** — `~/.zshrc` 빈 줄 누적 버그를 awk 빈 줄 버퍼링 방식으로 교체(무관한 빈 줄은 원문 보존).
  - **VERIFY**: `test.sh` **PASS=41 FAIL=0**(38→41) · 새 린트 음성 실측(위반 픽스처에서 FAIL=1) · `apply_patch` 페이로드 직접 실측(EUC-KR→deny / UTF-8→통과) · zshrc 멱등성(격리 HOME 3회 후 1회차와 diff 무출력, 구 로직은 5→6→7 누적으로 버그 실재 입증) · `smoke-hooks.sh --run` 30건 실패 0 · `bash -n`·`shellcheck`·`jq` 전부 무출력.
  - Instapaper 9건은 **손대지 않은 채 그대로**(실측 확인). 작업 로그는 `vibe-ai-config/.claude/work-log/2026-09-19.md` 에 12건 append.
- 🔴 **사용자 판단 대기 6건** (에이전트 수행 불가)
  1. **공용경로 심링크가 `chore-archify` 워크트리를 가리킨다** — `readlink -f ~/.local/bin/vibe` = `.git/worktree/chore-archify/shared/scripts/tmux-suite/vibe.sh` (**직접 실측 확인**). 내용은 master 와 동일해 지금은 정상이나, **그 워크트리를 지우면 `vibe`·`pane-*`·`claude-delegate` 가 한꺼번에 dangling** 된다. 복구: master 워킹트리에서 `bash claude/plugins/tmux-suite/install.sh --links-only`. (⚠️ `~/.agents/skills/archify` 는 실물 디렉터리라 이 위험의 대상이 아니다 — 워크트리를 지워도 스킬은 살아 있다)
  2. 유령 플러그인 3종 제거 — `claude plugin uninstall harness@swkim0128` · `test@swkim0128` · `vibe-admin@swkim0128` (1개씩 실행)
  3. `_unused/` 잔존 9파일 — 현행 대체재가 없어 거버넌스 후단("대체재도 없고 깨지지도 않았으면 남기고 사용자 판단")에 걸림. `review-mr.md`·`e2e.md`·worktree 훅 2종·`session-end-summary`·`pre-compact-checkpoint`.
  4. 선행 드리프트 1건 — `~/.claude/settings.json` 에만 있는 `env.ARCHIFY_UPDATE_CHECK_DISABLED`. `./install.sh personal` 로 해소하면 그 키가 사라지고 **승인 대기 Instapaper 변경이 라이브 배포**되므로 실행 보류.
  5. 푸시·커밋 승인 — `0101c3a` push · vibe-dotfiles 미커밋 13건 · Instapaper MCP 9건.
  6. Codex TUI `/hooks` 에서 `analyze` 항목 `Active` 재확인 (`hooks.json` 변경됨, 계획서 §8-1).

**🔴 재개 시 먼저 볼 것 2가지**
1. ~~**Stop 훅이 꺼져 있다.**~~ → **2026-09-19 실측: Stop 훅은 이미 복원돼 활성이다** (`.claude/settings.json`·`.codex/hooks.json` 양쪽 `Stop` 블록 존재, `auto-version-bump.sh` 호출. 백업 `.phase1-bak` 2개는 9/13자로 남아 있음). 9/13 사고(인덱스 전체 동반 커밋) 는 Phase 3 안전가드로 해소됐음을 코드로 확인 — ①자기 pathspec(`claude/plugins/*/.claude-plugin/plugin.json`·`.claude-plugin/marketplace.json`) 밖 staged 변경이 있으면 commit·push 를 **스킵** ②커밋은 `commit --only <자기 pathspec>`. 다만 **자기 버전 bump 는 여전히 자동 push** 하므로, 이 레포에 pane 을 띄울 땐 인덱스를 더럽힌 채 세션을 끝내지 말 것. 계획서 §7-A.
2. **Codex `/hooks` 재신뢰 미완**(사용량 부족으로 보류). 바뀐 것: `~/.codex/hooks.json`(delegate-pane-guard·install-sync-check 신규 → 인덱스 밀림) · 플러그인 `task-mgmt/hooks.json`. TUI `/hooks` `Active` 열 확인 후 `t`. **추정 복원·자동 승인 금지.**

**주의**: 이 레포에 에이전트 pane 을 띄우면 Stop 훅이 돈다(현재는 꺼둠). 확인은 para cwd 에서 `git -C` 로. 메모리 [[vibe-ai-config-stop-hook-trap]].
**미완 부수**: `~/.agents/hooks.json` 이 3건만 반영(agy 미설치라 install 이 생성 스킵) — 필요 시 `bash shared/hooks/generate-agy-hooks.sh`. analyze 플러그인 캐시는 손으로 동기화해둔 상태라 **재설치하면 되돌아간다**(푸시 전까지).

### B. 🏠 집 정리 (PRO-129) — **집에서 사진 촬영부터**

노션 페이지는 9/12 생성 완료(완료기준 7·Phase 1~4·물품목록 19행·위시리스트 대조 8건·구매예정 4+1·후보링크 11). **체크박스 전부 미완** — 구조만 짜인 상태.

- **다음 한 걸음**: 구역별 사진 5장 촬영·업로드 → 입구 전경 / 책상·서랍 / 침대·침대아래 / 옷장·행거 / 바닥·임시적치물. 각 구역 전경 1장 + 근접 1~3장, 서랍·수납함은 **열린 상태**, 치수 필요한 곳은 줄자·기준물체 함께.
- **사진 분석 가능**: Claude Code 는 `Read` 도구로 이미지 직독 · Codex 는 `codex -i <파일>`(초기 프롬프트 첨부). 사진은 `06.Temp_Images/집정리/` 에 두고 경로를 주면 물품 추출 → 노션 「사진 기반 물품 인벤토리」 표에 기재.
- **한계 준수**: 가려진 것·서랍 안쪽·겹친 것은 놓친다. 추출 결과는 `확인 필요` 로 두고 **사진만으로 처분·구매 확정 금지**. 치수는 반드시 줄자 실측(수납함 구매가 걸림).
- 미해결: 후보/구매예정 링크 **15개가 전부 `품목 확인 필요`**(단축 링크만) — 10월 프라이데이 전 해소 필요. 10월 프라이데이 정확한 날짜 미확인.

### C. 기타 이월

- 볼트 ↔ 노션 동기화 누락: `집 정리`(PRO-129)·`벌크업`(PRO-128) 둘 다 `01.Projects/` 폴더 없음. 규칙(05.프로젝트.md)대로 폴더를 만들지, "노션 단독 관리" 예외를 명문화할지 판단 필요.
- para 볼트 미커밋: `NEXT-SESSION.md`·`work-log/2026-09-13.md`·계획서·감사노트. `para-work backup` 은 사용자 판단.
- 열린 pane (2026-09-19 밤 실측): `%7`(para 허브 claude)·`%3`(zsh, vibe-ai-config)·**`%12`(claude, vibe-ai-config — 배치 개선 Phase 5→6→4 위임 중)**. Codex pane `%11` 은 한도 소진으로 종료·`%12` 로 교체했다. 지시서 `…/scratchpad/delegate-brief-vibe-ai-config.md`.

---

## 🔜 다음 세션 착수 지점 — Claude Code로 설정 수정 인계 (2026-09-13, 위 절로 대체됨)

사용자 요청으로 Codex 분석을 종료하고 **Claude Code를 다시 실행해 설정을 업데이트**한다. 아래 과거 브리핑보다 이 절과 [[01.Projects/개인컴_AI_작업환경_업그레이드/codex-이식기능-감사-20260913]]을 우선한다.

1. ~~**프로필 오류부터 수정**~~ ✅ 9/13 17:1x Claude 완료 — 정본 `codex/model-profiles/<name>.config.toml` 분리 · `install.sh` purge+별도 배포 · `--profile routine|review|deep mcp list` 3개 exit 0 실측 · 사용자 설정 tomllib 무손실 · 미커밋. **신규**: shared/claude/codex 배치 감사 → 개선 계획 [[01.Projects/개인컴_AI_작업환경_업그레이드/shared-배치-개선계획-20260913]] (P0 4건 즉시 가능 · 결정 필요 5건 §7). (원문) `codex --profile routine mcp list`는 exit 1. 설치기가 넣은 구형 `[profiles.*]`가 현재 CLI의 별도 `*.config.toml` 형식과 충돌한다. routine/review/deep 모두 실패. 이전 “배포·검증 완료” 판정을 철회한다. `vibe-ai-config` 정본·설치기 수정 후 실제 프로필 로드 3개와 사용자 설정 보존을 검증할 것.
2. **위임 기본값 정합화:** 허브는 환경변수로 Codex지만 `vibe delegate` 스크립트 기본값은 Claude. 문서의 Codex 기본 위임 설명과 다르다.
3. **에이전트·훅 실동작 검증:** 이식 에이전트 4개는 정의 존재만 확인. 공통 훅 6개는 배선·신뢰 항목만 확인. 기존 계약 16/16은 Claude/agy 중심이며 Codex 전체 검증이 아니다. 스모크 15건은 `timeout` 부재로 미실행.
4. 현재 기본 모델은 **astra/low**. 사용량 한도 소진 시 Claude로 이어가는 운영 결정은 유효하지만 자동 전환 장치는 없다. DB/네트워크 경고는 접근 제한 여부부터 확인하며 손상·서비스 불통으로 단정하지 않는다.

저장소 인계: `vibe-ai-config`는 감사 시점 `13d561f`·`c99a80d` 미푸시, `status/personal.md` 수정, 기존 `.codex/` 비추적. 기존 변경 보존·격리 작업. 집 정리(PRO-129)는 사진 인벤토리 준비 완료·사진 업로드 대기. 이번 세션에서 커밋·푸시하지 않는다.

## 🔜 다음 세션 착수 지점 (2026-09-13 **Codex 메인 전환 확정·진행 중** — 다음 세션은 Codex 허브로 연다)

> **⚡ 인계(9/13 12:2x, 사용자 요청으로 Claude 종료)**: 토글 확정됨. 완료 = `~/.zshrc.local`·tmux 전역 `VIBE_HUB_TOOL=codex` · para `AGENTS.md` 분업·위임 기본값 절 갱신. **Codex pane 에서 진행 중이던 위임 2건** — 결과는 각 레포 `git log` 로 확인:
> - `%4` (vibe-ai-config): [A] `status/<env>.md` 스냅샷에 Codex 섹션(4-2) · [B] Codex 기동 시 업데이트 프롬프트 억제(config 키 실측 → 없으면 vibe.sh settle 보정) · `install.sh personal` · 커밋 2건(push 안 함 → **다음 세션이 push**).
> - `%4` 는 종료 시점에 **`config-snapshot.sh` 편집 승인 프롬프트(y)에서 대기 중** — cwd(para) 밖 파일 편집이라 Codex 가 승인을 요구. 사용자가 `y` 를 누르거나, 다음 세션에서 vibe-ai-config cwd 의 Codex 로 다시 위임.
> - `%21` (vibe-dotfiles): **실패 — Codex 가 기동되지 않고 주입 메시지가 zsh 에 떨어짐**(`command not found` 잡음만, 레포 무손상). 원인 미확인(신규 디렉터리 신뢰 프롬프트 추정). `zsh/zshrc.local.template` `VIBE_HUB_TOOL` 기본값 `codex` 변경은 **미완** → 다음 세션에서 재위임(1줄 변경). vibe-dotfiles 에 untracked `vibe-tools/pane-list.sh`·`pane-peek.sh`·`pane-wait.sh` 3개는 이전부터 있던 것(이번 작업과 무관).
> - 잔여: R12 `vibe main` 육안(새 tmux 세션에서 Codex 허브 기동 확인) · 업무 컴 `install.sh work` 재실행 · 리허설 pane %20 정리(`vibe reap`).

> 운영 결정(9/9): 모델 사용량 때문에 Claude Code 메인 유지 → **9/13 재점검: 설정·훅·rules·MCP·위임 전부 Codex 에서 동작 실측(R1~R11·R13 ✅)**. 남은 것은 토글 확정 결정과 R12 육안뿐. Codex 사용량 여유 `5h 80% · weekly 97%`(9/13 12:09).
> 계획 정본: [[01.Projects/개인컴_AI_작업환경_업그레이드/codex-claude-동등설정-계획]] §4-1 체크리스트 · 상세 [[.claude/work-log/2026-09-13]].

**9/13 요약** — 블로커 3건(드리프트·훅 미신뢰·notion OAuth) 해소 + 발견 수정 3건: `hooks.json` `_note` 키 0.153.4 거부(`c9f9227`) · Codex 가 관리 구획 안에 `[hooks.state]` 를 써서 install 이 막히던 구조(`226d109`, **9/8 소실 사고 원인**) · `vibe` 가 Codex 셸에 없던 것(`f311099`, `~/.local/bin/vibe`). Codex `0.154.0` 으로 올라감(위임 pane 이 업데이트 프롬프트를 눌러버림 — 재발 주의).

**토글 확정 시 할 일(한 세션)**: ① `~/.zshrc.local` + `vibe-dotfiles/zsh/zshrc.local.template` `VIBE_HUB_TOOL=codex`(dotfiles 는 위임) ② para `AGENTS.md` 「도구 분업·위임 기본값」 절 갱신 ③ `status/<env>.md` 에 Codex 섹션(4-2) ④ R12 `vibe main` 육안 ⑤ 업무 컴 `install.sh work` 재실행(`f311099` 심링크·`226d109` 반영).

**P0 완료**
- 0-1 `VIBE_HUB_TOOL` → `claude` 원복 — template(git 클린)·`~/.zshrc.local`·tmux 전역 셋 다 확인.
- 0-2 `install_codex_config` 재작성 후 라이브 배포(`3630ec6`). tomllib 검증: 루트 fallback `["CLAUDE.md"]`, `projects` 클린, model·MCP 보존, `strict-config 0 fail`. 백업 `~/.codex/config.toml.bak.20260909-001111`.

**P0 사용자 단계 (에이전트 수행 불가)**
- 0-3 훅 신뢰 — `[hooks.state]` 는 소실 상태 그대로. Codex TUI `/hooks` 에서 `Active` 열 확인 후 필요 시 `t`. **추정 복원·자동 승인 금지.**
- 0-4 `vibe-ai-config` 미푸시 **6건**(`ffb1cb2`·`e3c6d20`·`0384432`·`3630ec6` + 2) 푸시 판단 · `stash@{0}` 드롭 판단 · para 미커밋 커밋.

**P1 진행 (9/9, `d558fdc`)**
- 1-1 ✅ MCP 정본 통합 — `codex/mcp.toml` 폐기, `claude/mcp.base.json` 하나(+`.codexOnly.notion`). `codex mcp list` == 정본 집합 확인.
- 1-2 ✅ allow 100건 → `~/.codex/rules/vibe.rules` 생성(`gen-rules.py`, 105건). `execpolicy check` 16케이스 통과.
- 1-3 ✅ **rules 가 `prompt/forbidden` 지원 + 샌드박스 내부 실행도 차단(실측)** → `permission-guard.sh` 훅 폐기. fail-open 소멸.
- 1-4 ✅ **전부 배선(사용자 결정 1번, `50d8632`)** — 코어 5종(briefing-inject·activity-log·bash-chain-guard·curl-terminal-guard·prompt-gates) × Claude·Codex. Claude `settings.json` 재생성·즉시 반영. **`bash-chain-guard` 활성 → 체이닝 Bash deny**(배선 직후 Claude 자신의 멀티라인 호출부터 차단됨 — 정상). para 프로젝트 훅(`cat NEXT-SESSION.md` 전체 49KB)은 공통 `briefing-inject`(상단 80줄)로 대체·제거.
- 사용자 단계: **notion OAuth 미완료**(9/9 `invalid_token` 실측) → `codex mcp login notion` · 훅 신뢰(`/hooks` `t`) · 미푸시 8건 · `stash@{0}`.

**P2 완료 (9/9, `4bfd042`·`3212054`·`efacc0c` — 전부 푸시)**
- 2-1 ✅ `claude/CLAUDE-commands.md` → `shared/commands.md`(도구 무관 정본). Claude 는 `@~/.claude/shared-commands.md`, Codex 는 생성물에 concat.
- 2-2 ✅ `install_codex_agents` — `~/.codex/AGENTS.md` = 공통 규칙 + 레지스트리 + `codex/AGENTS.tail.md` **생성**(심링크 대체, 15,023B/32KiB). 레포 `codex/AGENTS.md` 심링크 제거.
- 2-3 ✅ harness-reminder → `prompt-gates` 3번째 게이트(`VIBE_HOOK_HARNESS` 로 Claude/Codex 문구 분기). Claude `hooks/harness-reminder.sh` 폐기, `settings.json` 재생성.
- 2-4 ✅ `codex/hooks/config-drift-check.sh` — 생성물 3종(AGENTS.md·vibe.rules·hooks.json)을 정본에서 재생성해 sha 비교(`3212054`). **재생성 로직은 install.sh 복제본** — install.sh 생성 규칙을 바꾸면 훅도 같이.
- 부수 수정 ✅ `shims/claude.sh` deny 가 `continue:false`(턴 중단)였던 것을 `permissionDecision:"deny"`(도구 차단)로(`efacc0c`). 위임 pane 이 가드에 걸릴 때마다 턴이 죽어 3회 재주입한 원인. Claude 즉시 라이브. 상세 [[.claude/work-log/2026-09-09]].

**다음 세션 착수 (업무 컴 또는 개인 컴)**
1. **업무 컴**: `vibe-ai-config` `git pull` → `./install.sh work` → `diff status/personal.md status/work.md`. 개인 컴은 9/9 01:24 `install.sh personal` 완료(`head=efacc0c`, Codex 드리프트 훅 무출력 확인, `status/personal.md` `2a29cdf` 푸시).
2. **P3** `vibe-dotfiles/AGENTS.md` 신설 → **P4** 리허설(계획서 참조).
3. 이월: `.claude/settings.json` 327행 `statusLine` 파이프 정리 검토 · 8/29 이월 위험 2건(Stop 훅 auto-push · activity-logger 마스킹).

**사용자 단계 (누적, 에이전트 불가)**
- ~~Codex 훅 재신뢰~~ ✅ 9/13 (`[hooks.state]` 6건) · ~~`codex mcp login notion`~~ ✅ 9/13
- **토글 확정 여부 결정** (위 「토글 확정 시 할 일」)
- `vibe-ai-config` `stash@{0}` 드롭(스냅샷 잔여, 재생성으로 대체됨)
- 리허설 pane %20(Codex) 정리 — `vibe reap`

**Q&A 9/9**: 훅 설정의 `|` — `matcher`(213·235·255행)는 정규식 OR 로 **필수**. 327행 `statusLine` 의 파이프는 claude-dashboard 플러그인 원본 명령(기존, 가드 대상 아님) — 정리 원하면 다음 세션 검토.

<details><summary>2026-09-08 중단 인계 (완료 처리됨)</summary>


- 사용자 요청으로 구현·검증 중단. Claude 1번 패널(%1)도 중단 확인. 자동 재개하지 않는다.
- 완료: 개인 `vibe-dotfiles/zsh/zshrc.local.template` 및 `~/.zshrc.local`의 `VIBE_HUB_TOOL=codex`. 새 zsh에서 personal/codex, tmux 전역 codex 확인. 문법·diff 검사 통과. dotfiles 변경은 미커밋.
- **미완**: `vibe-ai-config/install.sh`의 `install_codex_tui` 배포 결함. fallback 키가 프로젝트 테이블 하위에 들어가 root에서 None. 배포 후 hooks.state 소실도 관측했으며 원인 확정·보존 검증 필요.
- Claude가 `codex/config-root.toml`을 만들고 `codex/tui.toml`을 수정하다 중단. 구현·배포 완료 아님. 다음 행동은 현 diff 확인 후 root 키 배치와 사용자 설정 보존·멱등성 검증. 훅 신뢰를 임의 복원/승인하지 않는다.
- 상세: [[.claude/work-log/2026-09-08]]. 기존 아래 브리핑은 과거 기록이다.

</details>

## 🔜 다음 세션 착수 지점 (2026-08-29 인계)

> 2026-08-29 세션은 **Claude Code 업데이트 재시작**으로 종료. 아래가 이어받을 지점이다.

1. 🔴 **업무 컴에서 `./install.sh work` 1회 실행** ← 이게 마지막 조각
   - 그래야 `vibe-ai-config/status/work.md` 가 생기고, 그때부터 **두 머신 비교가 해시 두 줄**로 끝난다(`diff status/personal.md status/work.md`).
   - 지금은 업무 컴 배포 시점을 알 방법이 없다 — 8/19~8/28 개인 컴이 일주일 뒤처졌던 것과 같은 상태일 수 있다.

2. 🟡 **vibe-ai-config 커밋 3건 미푸시** — `4977e76` · `e743c28` · `95c05be` (master ↑3)
   - 푸시해야 업무 컴이 이 인프라를 받는다. 1번의 선행 조건이다.

3. 🟡 **오늘 구축한 설정 인프라 — 요약**
   - `docs/settings-inventory.md` = 정본 문서 / `status/<env>.md` = 머신별 배포 스냅샷(자동) / `config-drift-check.sh` = SessionStart 드리프트 경보(91ms, 정상 시 무출력)
   - **배포 명령은 `./install.sh [personal|work]` 하나뿐.** `deploy-links.sh` 는 흡수·폐기(`_unused/`) — 다른 배포 스크립트를 찾지 말 것.
   - agy 는 `TOOLS` 에서 제거(코드는 보존 — 복귀 시 다시 추가하면 살아남).
   - 볼트 절차서: `02.Areas/04.Claude-Config/설정-점검-가이드.md`

4. 🟢 **이월 — 구조적 위험 2건**
   - Stop 훅 `auto-version-bump.sh` 가 턴 종료 시 커밋을 자동 push 할 수 있다. `git push` 를 `permissions.ask` 로 승격한 규율을 훅이 무력화하는 구조.
   - `activity-logger` 가 Bash 명령 문자열을 **공개 저장소**(para)에 그대로 기록한다. 8/22 에 회사 식별자가 유입될 뻔해 스크럽했다. 마스킹 또는 work-log gitignore 검토 필요.

### 💡 2026-08-29 에 배운 것 (재발 방지)

- **심링크 자산은 커밋 즉시 반영, 생성·복사 자산은 `install.sh` 필요.** 이 비대칭이 개인 컴을 일주일간 옛 설정으로 돌게 했다.
- **훅 스크립트는 심링크라 항상 최신인데 배선은 `settings.json` 안에 있다** → "파일은 있는데 동작 안 함". `readonly-bash-allow.sh` 가 정확히 이 상태로 9일간 미작동했다.
- 스킬 배포 검증은 **개수가 아니라 집합 차이**로 — 배포본에 외부 스킬 12개가 섞여 개수 비교는 오탐이 난다.

## 🔜 이전 착수 지점 (2026-08-22 인계)

1. 🔴 **사용자 직접 조치 2건** — 에이전트가 수행 불가
   - [ ] **`DIARY-346` 노션 UI 에서 삭제** — Notion MCP 에 삭제/휴지통 도구가 없다(create·update·move·duplicate 뿐). week 34 일지 중복분이며 **화·수·목 WORK 항목은 DIARY-347 로 병합 완료**, 제목을 `삭제예정 — 병합완료 → DIARY-347` 로 바꿔 `week {WW} {YYYY}` 검색 충돌은 이미 제거했다.
   - [ ] **Home 의 `## 🍽 식단` 섹션을 Pulse 탭 안으로 드래그** — `<tabs>` 는 노션 마크다운 스펙에 없는 블록이라 API 로 탭 내부에 쓸 수 없다. `create_view`·`move_pages` 모두 페이지 최하단에만 붙는다. Pulse 탭엔 이미 `### 작업`·`### 돈` 이 있어 `### 식단` 이 합류할 자리다.

2. 🔴 **Stop 훅 `auto-version-bump.sh` 자동 push 차단** (Tasks 등록됨)
   - 턴 종료 시 커밋을 자동 push 한다. 2026-08-22 에 `git push` 를 `permissions.ask` 로 승격했는데 훅이 그 규율을 무력화하는 구조다.

3. 🟡 **노션 루틴 업그레이드 잔여 — Tasks DB 에 6건 등록 완료**
   - 우선순위 순: `03.예산.md 구버전 절 전면 재작성`(높음) → `Foods 레시피/외식 분리 + 재료 연결` → `위시 ↔ 거래내역 매핑 재설계` → `diagnosis.md 체크리스트 실사` → `Projects DB Area·유형 롤업 매듭` → `Sprint 자동 생성 중지 검토`
   - ⚠️ `diagnosis.md` 미완료 16건은 **현실과 어긋나 있다** — `DB ID 단일 파일 추출`(=ids.md)·`04.일정.md SOP 신설`은 이미 완료, `Diet 폴백 생성 절차`는 아래 n8n 규칙으로 **무효화**. 인용 전에 실사할 것.

### 📌 2026-08-22 확정 규칙 — 다음 세션이 반드시 알아야 할 것

- **주기 페이지 생성 = 매주 일요일 n8n 전담.** 다이어리·식단 페이지를 에이전트가 생성하지 않는다. 대상이 없으면 **생성하지 말고 보고 후 중단.** 정본 = `02.Areas/07.개인관리/README.md` 메타 룰 6 (+ `01.다이어리.md`·`04.일정.md`, 스킬은 커밋 `f0b8ec7`).
  - 근거: 자동 생성분 제목의 `[week 00]` 접두가 명명 규칙을 깨 스킬 검색이 실패 → 스킬이 페이지를 하나 더 만들어 week 34 일지가 2개로 갈라졌다(week 30 도 동일).
- **뱅크샐러드 import = 다음 달 초**(전월 거래 정리 완료 후). **당월 거래내역·HL 행이 비어 있는 것은 정상**이며 결함으로 진단하지 말 것. 정본 = `03.예산.md` 「운영 리듬 (2026-08-22 확정)」.
- **문서↔스키마 드리프트 정정** — `매핑 거래`(Ledger)·`위시리스트`(거래내역) relation 은 **양쪽 스키마 어디에도 없다**(실측). `ids.md` 2곳·`03.예산.md` 1곳 정정 완료.

### 🖥 2026-08-22 노션 화면 변경 — 재작업 방지용

- **Project** — `🔥 진행 중 · 다음 할 일`(board, 개인+미완료 4건) / `🧩 열린 태스크` / `🅿️ 멈춘 프로젝트`·`📚 전체 프로젝트`(토글). 구 3탭 통합 뷰는 **삭제**.
- **Food** — 대시보드를 Home 으로 이관하고 **이전 구성으로 원복**(`## 식재료 현황` · `## 식단·음식` 2섹션).
- **Home** — 최하단에 `## 🍽 식단` 대시보드 5블록(재고 수·재고 카테고리·장볼 것·오래 안 먹은 요리·식단 캘린더). 기존 Dash Board 콜아웃·시계/날씨·`<tabs>` 무손상.
- **Budge** — `📊 이전 예산 통계`(HL table, Date DESC) + `💸 위시 금액 요약`(실행 예정 총액·검토 중 총액). Quick Actions 버튼 3개 무손상.
- ⚠️ **formula/rollup 필터는 API 로 못 만든다** — `만들 수 있음` 필터가 조회 0건을 반환한다(값이 `formulaResult://` 참조로만 옴). 필요하면 노션 UI 에서 직접 걸 것.

4. ✅ **chrome-devtools-mcp — 검증 완료(2026-08-22). 원인은 쿠팡 미로그인이었다.**
   - [x] 크롬 원격 디버깅 활성 — 기본 프로필 `DevToolsActivePort`=9222, 사용자 크롬(pid 687, 14:52 실행, 부모 launchd)에 부착.
   - [x] Claude Code 재시작 후 MCP 로드 — `chrome-devtools-mcp ✔ Connected`,
     `list_pages`·`new_page`·`select_page`·`navigate_page`·`evaluate_script`·`take_screenshot` 모두 정상.
   - [x] **상품 상세 403 해소** — 쿠팡 **미로그인** 상태에서만 `/vp/products/…` 가 본문 249자 403
     (`"요청하신 페이지의 사용권한이 없습니다"`). URL 직접 열기·검색결과 실클릭 모두 403 이었으나
     **사용자 로그인 후 동일 URL 정상 로드**(본문 36KB). 봇 탐지가 아니라 로그인 조건이었다 —
     이전 세션 노트의 "쿠팡 403 = 도메인 차단" 추정은 **미로그인 상태의 관측**이었음.
   - [x] **추출 실측** — `맥심 싱글 오리진 브라질 산토스 원두커피` / `21,900원` /
     `coupang.com/vp/products/1164380709?itemId=2141478022&vendorItemId=70139853779`.
     셀렉터: 상품명 `.prod-buy-header__title` · 판매가 `.price-amount.final-price-amount`.
   - [x] **폴백 경로도 확보** — 검색 페이지(`/np/search`)는 미로그인에도 열리고 카드 innerText 에
     상품명·정가·판매가·링크가 모두 있다. 브라우저 없이 쓸 다나와 쇼핑 MCP(`search_products`)도 실측 성공.
   - **정본 반영 완료**: `notion-budget/SKILL.md` 「상품 페이지 → 위시 등록」에
     ① 쿠팡 상품 상세 = **로그인 필수**(403 시 차단 단정 금지, 로그인 먼저 확인) ② 폴백 순서(검색결과 카드 → 다나와 MCP → 붙여넣기)
     ③ 실측 셀렉터·`evaluate_script` 우선 규칙 추가.
   - **install.sh 커밋 완료** — `648f52a fix(install): MCP 등록 경로를 ~/.claude.json .mcpServers 로 교정` (master, 미푸시).
   - **남은 것**: 🧺 Ledger 실제 행 생성까지의 완주는 미실행(테스트 데이터로 노션 오염 방지). 실제 위시 등록 요청 시 그대로 통과할 상태.

## 🔜 이전 착수 지점 (2026-08-17 인계)

1. 🔴 **Codex 편입 마무리** — 도구 전환에서 유일하게 남은 인프라 작업
   - [ ] **`codex login`** ← **선행 필수.** `codex doctor` 가 `✗ auth no Codex credentials` 를 보고한다. 이게 안 되면 아래 둘 다 막힌다.
   - [ ] **Codex 어댑터 MCP 보강** — `vibe-ai-config/codex/` 는 현재 `AGENTS.md` 심링크 + `~/.codex/config.toml` 의 MCP 1종(`sequential-thinking`)뿐. agy 가 쓰던 7종(notionMCP·google-calendar·context7·github·playwright·browsermcp·sequential-thinking) 수준으로 이식.
   - [ ] **`bash-chain-guard` Codex 이식 검토** — `shared/hooks/` 가 core + shim 구조라 `shims/codex.sh` 하나만 추가하면 된다. Codex 의 이벤트명·출력 필드명이 Claude 와 거의 같아 `shims/claude.sh` 를 거의 복제 가능.
   - **실측 근거(2026-08-17)**: `codex-cli 0.147.0` 은 훅 11종(`PreToolUse`·`PermissionRequest`·`PostToolUse`·`SessionStart`·`SessionEnd`·`UserPromptSubmit`·`SubagentStart/Stop`·`Stop`·`Pre/PostCompact`)·서브에이전트·스킬·플러그인을 지원한다. 차단 규약(exit 2 + stderr, `permissionDecision:deny`)이 Claude Code 와 거의 동일하고 설정은 `~/.codex/hooks.json`, 훅마다 `trusted_hash` 신뢰 계층이 추가로 있다. `.claude/` 설정 임포트 모듈(`external-agent-migration`)도 내장.
   - ⚠️ **"Codex 는 훅이 없다" 던 이전 기록은 오판이었다 — 인용하지 말 것.** Claude 허브 유지는 **전환 비용** 판단(스킬 57개·플러그인 15개·`vibe` 인프라)이지 구조적 제약이 아니다.
2. 🟡 **Google AI Pro 다운그레이드** — 사용자 직접(웹). agy 이탈에 따른 정리.
3. 🟢 **진행 중 프로젝트 2건** — `개인컴 AI 작업환경 업그레이드`(위 1번이 그 잔여 작업) · `노션 루틴 업그레이드`(Phase 2·3 잔여). 나머지 6건은 Paused/Planning/Backlog.
4. 🔧 **tmux-suite 재사용성 리팩토링** — 원칙은 `shared/rules/AGENTS.md` §2 에 반영 완료("재사용성 = 추상화 추가가 아니라 종속 제거"). 대상: ① `vibe.sh:41`(`start`)·`:556`(`resume`) 의 `claude` 하드코딩 → `VIBE_HUB_TOOL`/`--tool` 로 (`main:154` 는 이미 적용됨) ② `vibe reap` → `reap-idle-claude.sh` Claude 전용 ③ `claude-{send,delegate,switch,skills}.sh` 네이밍·도구 종속 ④ 위치 이관 `claude/plugins/tmux-suite/` → `shared/`(`CLAUDE.md:53`·`marketplace.json`·aliases·스킬 참조 동반 수정 필요, 계획 먼저).
5. 미착수: `03.예산.md` 전면 재작성(구버전 절 3개), Pulse 차트 UI 마무리(숫자 정밀도·월 그룹), Project `작업 현황` 기본 뷰 지정, HL `총지출` 수식 값 확인.
6. 🧹 남은 정리 후보: `03.Resources` 번호 결번(12·16·22) · `vibe-ai-config/skills/work/tracking/task-review/SKILL.md:8` 의 `TASKS.md` 언급(아카이브됨).

## ✅ 2026-08-14~17 완료 (커밋 10건)

- **도구 분업 전환** — agy 허브 철회 → Claude Code 허브 복귀, Codex(ChatGPT Plus) 편입. `VIBE_HUB_TOOL` 을 `~/.zshrc.local` + `vibe-dotfiles/zsh/zshrc.local.template` 양쪽에서 `claude` 로 (vibe-dotfiles `a9cc68a`).
- **`AGENTS.md` 작성법 정규화** — Claude Code 공식 기준(200줄 이하·개요/디렉터리/명령어 필수)에 맞춰 재편. 139줄, 함정 절 신설, VERIFY 수단 명시.
- **개인관리에 프로젝트 도메인 등재** — `05.프로젝트.md` 신설(범위 경계·볼트↔노션 1:1·상태 판정 규칙), `ids.md` 에 Projects·Tasks·Sprint 등재로 스킬 ID 하드코딩 규칙 위반 해소(vibe-ai-config `356d726`).
- **노션 Projects DB 최신화 + 트리아지** — 볼트에만 있던 3건 신규 등록, 활성 16건 → 8건으로 정리(아카이브 7·Done 1·Paused 정정 2), 태그 결손 전량 보정.
- **`ParaType` 속성 삭제** — `Status` 와 중복(93건 중 92건 일치)이고 옵션 `Area`·`Resource` 는 Projects DB 에서 사용 0건이었다. **아카이브 판정은 `Status ∈ (Done, Canceled)` 로 일원화.** 근거·스냅샷 → `01.Projects/노션_루틴_업그레이드/paratype-removal-20260817.md`
- **스킬 정리** — `notion-project-creator` 폐기(타깃 DB 404 + 기능 중복 + 고아), `notion-project-manager` 를 `ids.md` 인용으로 전환.
- **볼트 정리** — `TASKS.md`·`dashboard.html` 아카이브(노션 DB 와 이중 관리 해소), Spring 프로젝트 아카이브, 루트 잔여물 6건 제거, 옛 "Notion → PARA 단방향" 헤더 5곳 폐기.

## 🗄️ agy(Antigravity) — 철회(2026-08-14), 기록만 보존

> 아래는 agy 하네스 실측 기록이다. **방침은 폐기됐으니 작업 지시로 읽지 말 것.** 다른 도구 평가 시 참고 가치가 있어 남긴다.

1. `bash-chain-guard` 정상 작동 확인(2026-08-14 18:36) — agy 가 `||` 체이닝을 시도하자 pane 에 `⚠ Tool call denied by pre-tool hook` 출력.
2. notionMCP 검증 완료 — `mcp-remote@0.1.37` JSON-RPC 핸드셰이크 정상, `notion-search` 실검색 성공(Notion MCP 1.2.0, 툴 28개).
3. `vibe delegate <프로젝트> --tool agy` 실기동 확인(pane `%16`, Antigravity CLI 1.1.13). 단 `Quota unavailable: Antigravity token expired`.
4. 미해결로 남긴 것: `generate-agy-hooks.sh` 출력 경로(`~/.agents/hooks.json` vs agy 가 읽는 `~/.gemini/config/hooks.json`) · `antigravity/README.md` customization root 오기.

## 🔧 2026-08-02 설정 정비 상태 (Claude Code 재시작 직전 저장)

- **OMC(oh-my-claudecode) 완전 제거 완료 + 재시작 검증 통과(2026-08-02)**: 재시작 후 세션에 omc 스킬/에이전트 0개, npm 전역 empty, installed_plugins/marketplaces 등록 없음, statusLine(claude-dashboard 1.26.2) 정상 확인. 잔여 데이터(`~/.claude/plugins/cache/omc/` 307MB, `~/.omc` 16K)도 사용자 승인 하에 삭제 완료 — 개인컴 OMC 흔적 0.
- **claude-dashboard 복구**: 삭제된 것 아니었음 — statusLine이 캐시에 없는 1.27.0을 가리켜 깨져 보임. 정본에서 1.26.2로 정합(vibe-ai-config 커밋 `a69b632`), settings.json 재생성됨.
- **7/31 개인컴 적용 런북**(스킬 npx 복사 전환·48개·8그룹) 적용 완료 상태 검증됨 — dangling 0, 48/48.
- 후속 — **전부 마감(2026-08-06)**: ① ~~업무컴에 OMC 제거 반영~~ (8/6 완료) ② ~~vibe-ai-config omc 잔여 참조 정리~~ (`pipeline` 스킬은 이미 제거돼 있었고, `multi-dispatch/SKILL.md` 상태 경로 `.omc/state` → `.claude/state` 대체, 커밋 `8954354`) ③ ~~`~/.omc` + 고아 캐시 삭제~~ (8/2 완료) ④ ~~para 볼트 `.omc/` 잔여물 삭제~~ (8/6 완료 — 디렉토리 제거 + `.gitignore`에 `.omc/` 추가).
- GitHub PAT 재발급(개인컴 AI 작업환경 잔여 액션)은 **진행하지 않기로 결정(2026-08-06)**.
- **8/6 설정 구성 감사 + 정리 완료**: ① `~/.claude/.omc*` 잔재 3건 삭제(8/2 정리 때 누락분 — 이제 OMC 흔적 진짜 0) ② 레거시 `~/.claude/config.json`(구식 MCP 설정) 삭제 ③ 고아 마켓플레이스 디렉토리(`affaan-m-everything-claude-code `) 삭제 ④ `plane-mcp@cc-claude`를 settings.base → work overlay로 이동(개인컴에서 조용한 로드 실패 해소) ⑤ allow 중복 패턴 18건 정리(88→70) ⑥ git 로컬 파괴성 명령(restore·checkout --·stash drop/clear·reset --hard) ask 승격(git * allow·push 무확인은 유지) — vibe-ai-config `d8c85a6`·`57471f5`, `./install.sh personal` 재생성 완료. **업무컴 후속: 다음 `git pull` + `./install.sh work` 시 자동 반영(plane-mcp는 work overlay 경유 유지).**

## 🔀 ~~agy 메인 전환 준비~~ — **철회(2026-08-14)**, 조사 기록으로만 보존

> ⛔ **이 절의 방침은 2026-08-14 폐기됐다** (위 착수 지점 0번 참조). 아래 내용은 agy 하네스 실측 조사 기록으로만 남긴다 — 훅 엔진·서브에이전트·MCP 취약점 분석은 다른 도구 평가 시 재사용 가치가 있다.
>
> ~~방침: 개인컴 메인 도구를 Claude Code → **agy(Antigravity)** 로 전환한다. **지금 전환하지 않고**, agy 설정이 갖춰진 뒤 실행한다.~~

**이미 갖춰진 것**: `VIBE_HUB_TOOL=agy`(~/.zshrc.local) · 규칙 주입 경로 작동(`~/.gemini/GEMINI.md` 관리 블록 = 정본 AGENTS.md + agy-tail, `~/.agents/AGENTS.md` 심링크) · 프로젝트 규칙(`para/GEMINI.md` → `@AGENTS.md`) · 스킬 53개(`~/.agents/skills`) · MCP 7종(notionMCP·google-calendar·context7·github·playwright·browsermcp·sequential-thinking) · SOP 워크플로우 4종 · 권한 시드.

**보완 필요 (전환 전)**
1. **훅 미배치 — 최대 갭이나 agy 지원은 확인됨(2026-08-09 실측).** agy 1.1.10 바이너리에 훅 엔진 구현 확인 — 이벤트 5종(PreToolUse·PostToolUse·PreInvocation·PostInvocation·Stop), `~/.agents/hooks.json`(전역)·`<ws>/.agents/hooks.json`. **즉 지원 여부가 아니라 "우리 훅 9종의 이식"이 남은 일.** 제약 2건: ⓐ **SessionStart 이벤트 없음** → 브리핑 주입은 `PreInvocation` + `invocationNum==1` 에뮬레이션 ⓑ Claude의 `type:"agent"` 훅(commit PHP LSP 게이트)은 agy 미지원(command 전용)이라 셸 재작성. 입출력 스키마도 달라(camelCase, `decision`/`injectSteps`) 어댑터 계층 필요. 상세 = vibe-ai-config `antigravity/README.md` 검증 이력(`5a7302a`).
2. ~~서브에이전트 미구현~~ → **정정(2026-08-09)**: `run_subagent`·`SubagentSpec`·`KillSubagent` 및 멀티에이전트 오케스트레이터(owl) 구현 확인. README의 "v2 후보" 기술이 agy 1.1.0 기준으로 낡았던 것. 남은 일은 위임 규율(CLAUDE-delegation.md)의 agy 이식뿐.
3. ~~**스킬 3개 누락**~~: `notion-project-creator` → **2026-08-17 폐기 완료** (타깃 DB `2a9a2519…` 가 404 부재 + `notion-project-manager` 와 기능 중복 + universal 정본 미배포 고아. 볼트 `02.Areas/Claude-Skills/notion-project-creator/` 에 이력 보존). `skill-backup` · `update-vibe-commands` 는 Claude 전용 성격이라 무시 가능.
4. **install.sh 문구 불일치**: 실행 로그의 "antigravity 어댑터 미구현 — skip(P3/P4)"과 실제 배포 상태(스킬 53개 존재)가 어긋남 → 배포 경로 확정 후 문구 정리(재설치 시 누락 위험).
5. 🚨 **MCP 실호출 시도 → 실패 확인(2026-08-14)**. `agy -p '…'` 로 읽기 전용 테스트를 돌렸으나 **5분 타임아웃, 응답 0바이트**. 로그(`~/.gemini/antigravity-cli/cli.log`) 원인: `MCP: 1 server(s) still connecting after 5m0s: notionMCP` → `Print mode: timed out after 1494 polls (printed=0)`.
   - **구조적 취약점 — MCP 하나가 안 붙으면 print 모드가 통째로 멈춘다.** 다른 MCP 6종과 모델·규칙 로드는 정상이었는데도 아무 작업을 못 했다. **agy 를 메인으로 전환하기 전 반드시 해결해야 하는 급소.**
   - 원인: `notionMCP` = `npx -y mcp-remote https://mcp.notion.com/mcp`(OAuth). 인증 캐시 `~/.mcp-auth/` 최신이 **mcp-remote-0.1.37 / 2026-02-22** 뿐 — `npx -y` 가 매번 최신 버전을 받으므로 버전 상승과 함께 캐시가 무효화됐다.
   - **해결(사용자 작업 필요)**: 터미널에서 `npx -y mcp-remote https://mcp.notion.com/mcp` 1회 실행 → 브라우저 인증 → 토큰 캐시 후 Ctrl+C. 그다음 agy 재테스트.
   - 대안: 인증 전까지 `~/.gemini/config/mcp_config.json` 에서 notionMCP 를 잠시 빼면 agy 자체(규칙·훅·스킬) 검증은 가능.
6. ✅ **agy 자체 검증은 통과(2026-08-14, notionMCP 임시 제거 후)**. `agy -p` 로 읽기 전용 작업 정상 완주 — ① **식단 정본을 스스로 찾아냄**(`~/.agents/skills/notion-diet-manager/references/db-schema.md`) → 오늘 확정한 "스킬이 정본" 구조가 agy 에서 작동 확인 ② 핵심 규칙 3개 정확 요약(요일×끼니 표 정본·`보유 중` 단일 정본·`구분` 필수) ③ **GEMINI.md 관리 블록의 AGENTS.md 규칙 인용**(절대 금지·3대 자가 검증) → 규칙 주입 경로 정상. **즉 막힌 것은 notionMCP 하나뿐이고, 규칙·스킬·작업 수행은 정상이다.**
7. ~~🐛 **`vibe delegate` 가 agy 를 지원하지 않는다**~~ → **해결(2026-08-14)**: `vibe.sh` delegate 의 도구 화이트리스트에 `agy` 추가(설치 확인 + 미설치 시 명확한 오류), 오류·usage·help 문구를 `agy|claude|gemini|codex` 로 정정, 메시지 프롬프트의 하드코딩 "claude" → 선택 도구명으로 치환. `bash -n`·`shellcheck -S warning` 통과. **남은 불일치**: 기본값은 여전히 `claude` 인데 `para/AGENTS.md` 는 "agy(기본)" 로 기술.
6. statusLine/사용량: claude-dashboard는 Claude 전용 — agy-hud 대체 여부 확인.

**권고 순서**: ① hooks.json 최소 3종(브리핑 주입·작업로그·Bash 체이닝 가드) 구현 → ② agy 실기 검증 1회 → ③ install.sh 정합 정리 → ④ 실사용 전환(허브 변수는 이미 agy).

## ⚙️ 설정 확인 — 2026-08-14 (업무컴 설정 반영 후)

- 상태: 모델 `null`(기본 = Opus 5 1M) · 권한 allow 70/ask 10 · 스킬 58개 · 훅 이벤트 5종 / **스크립트 13종** · statusLine claude-dashboard(버전 와일드카드) · vibe-ai-config clean.
- 업무컴에서 들어온 커밋 3개: `88d286c` **curl-terminal-guard**(에이전트 Bash 직접 `curl` 차단) · `3cc4836` **notion-diet-manager 갱신**(노션 식단 DB 구조 변경 반영 + Foods 재료 백필 훅) · `0a1c480` delegation 중복 pane 생성 금지.
- **식단 DB 구조 변경 → `02.식단.md` 정본 갱신 완료(2026-08-14)**. 노션 식단 DB가 8/11·8/14 두 차례 바뀐 것을 반영: ① **Diet ↔ Ingredients relation 삭제**(8/11) → 재고는 `보유 중` 체크박스 단일 정본, Diet 쪽 동기화 지시 전부 제거 ② **Diet ↔ Food 신규 미기입**(8/14 결정) → 주차별 정본은 본문 요일×끼니 표, 기존 링크는 이력 보존. `Needed Ingredient List` 롤업이 신규 주차에 비는 건 **정상** ③ **Ingredients 신설 속성 `구분`(소모품/상비품)·`장보기`(checkbox)** — `구분` 미부여 시 「소모품 (보유 우선)」 뷰에 안 나오므로 **생성 시 필수** ④ **Foods ↔ 식재료 백필은 근거 기반**(본문 식재료 섹션·사용자 언급만, 외식·배달 제외, 일괄 변환 금지).
  - 🚨 **정본 이원화 발생 — 원칙 위반 상태.** 업무컴 커밋(`3cc4836`)이 "para 볼트의 02.식단.md는 실재하지 않아"라고 판단해 도메인 규칙(재고 SoT·표 규격·태그 분류표·폴백·분기)을 **스킬 내부 `references/db-schema.md` 로 흡수**했다. 그러나 **파일은 실재한다**(업무컴에 개인 볼트가 없어 오판한 것으로 보임). 지금은 도메인 정본과 스킬이 같은 규칙을 중복 보유 → **"도메인 문서 = 정본, 스킬 = 어댑터" 원칙에 반한다.**
  - ✅ **해소 — 식단만 "스킬이 정본" 예외로 확정(2026-08-14, 사용자 결정)**. 근거: **업무컴에는 개인 볼트를 두지 않는다.** 볼트 없이도 작업 가능해야 하므로 스킬이 규칙을 자체 보유한다.
    - `02.식단.md` → **포인터 문서로 축약**(정본 경로·갱신 규칙 + 자주 틀리는 지점 최소 요약만). 규칙 본문을 다시 들이지 않는다.
    - `02.Areas/07.개인관리/README.md` — 아키텍처 원칙에 예외 명시 + 레지스트리 「도메인 정본」 열을 `스킬 내부`로 갱신. **정본 위치는 항상 이 표가 알려준다.**
    - `para/CLAUDE.md` — 예외 규정 추가 + `notion-suite` → `personal-suite` 개명 반영(`5da01a4`).
    - 정본 경로: 레포 `vibe-ai-config/skills/personal/diet/notion-diet-manager/references/db-schema.md` → 배포 `~/.agents/skills/…`(universal) → Claude 는 심링크. **한 번 배포하면 Claude·agy 양쪽에서 동일하게 읽힌다.** 스킬 편집 후 `install.sh` 재실행 필요(레포 편집 즉시반영 없음).
    - 다른 도메인도 볼트 미동기 환경에서 쓰게 되면 같은 전환 필요 — 그때 레지스트리 열을 함께 갱신.
  - 미해소: 8/9 조사에서 확인한 `보유 중` 0건(재고 운영 미개시).
- **`bash-chain-guard` Claude 배선은 사용자 판단으로 보류(2026-08-14)** — agy 는 배선됨. Bash 체이닝 금지는 당분간 지시문(AGENTS.md)으로만 강제.

## 🪝 도구 무관 훅 3종 (2026-08-09 완료)

- 정본 `vibe-ai-config/shared/hooks/` — 코어 3종(`briefing-inject`·`activity-log`·`bash-chain-guard`) + shim 2종(claude/agy) + `manifest.json` + `test.sh`. 커밋 `1b2071d`.
- **검증**: shellcheck 무경고 + `test.sh` 13/13(양 하네스 계약 전수). **Claude 배선은 보류** — briefing·activity 는 기존 훅과 중복이라, 신규 가치가 있는 `bash-chain-guard` 만 `settings.base.json` 에 추가하면 됨(절차는 `shared/hooks/README.md`, `ask` 모드로 시작 권장).
- 🚨 **~~agy 배선 완료~~ → 거짓이었음(2026-08-14 실측 정정).** `~/.agents/hooks.json` 은 install.sh 가 정상 생성하지만 **agy 가 그 파일을 읽지 않는다.** agy 로그: `hooks_manager.go:53] loaded 0 named hooks from **0 hooks.json file(s)**` — 파싱 실패가 아니라 **파일 미발견**. 2026-08-06 로그에도 동일 → 처음부터 한 번도 로드된 적 없다.
  - 증거 보강: 실기 테스트에서 체이닝 명령(`echo "test1" && echo "test2"`)이 **exit 0 정상 실행**(차단 없음), `activity-log` 출력 디렉토리 `~/.local/share/vibe-hooks/activity/` **미생성**. 훅 3종 전부 미작동.
  - **`antigravity/README.md` 의 "customization root = 전역 `~/.agents/hooks.json`" 기술도 오류.** 실제 경로 미규명 — agy 가 MCP 를 `~/.gemini/config/mcp_config.json` 에서 읽는 것을 보면 `~/.gemini/config/hooks.json` 이 유력 후보. 워크스페이스 `<ws>/.agents/hooks.json` 도 미검증.
  - ✅ **경로 규명 완료(2026-08-14, agy 바이너리 문자열 분석)**: 전역 customization root = **`~/.gemini/config/`**. 바이너리 내장 문서에 `**Global Configuration**: ~/.gemini/config/mcp_config.json` · `3. **Global Discovery**: ~/.gemini/config/` 로 명시. **`.agents/` 는 `skills/`·`plugins/`·`skills.json` 전용**이며 hooks.json 과 짝지어진 문자열이 없다 → 그래서 **스킬 53개는 정상 작동했고 훅만 죽어 있었다.**
    - **조치**: `~/.gemini/config/hooks.json` 배치 완료(`~/.agents/hooks.json` 은 삭제하지 않고 남김). **검증 미완** — agy 재실행 후 로그에 `loaded 3 named hooks from 1 hooks.json file(s)` 가 찍히는지, 체이닝 명령이 `deny` 되는지 확인 필요.
    - **후속 수정 대상**: ① `shared/hooks/generate-agy-hooks.sh` 출력 경로를 `~/.gemini/config/hooks.json` 으로 ② `antigravity/README.md` 의 "customization root = 전역 `~/.agents/hooks.json`" 오기 정정 ③ 8/9 의 "agy 배선 완료" 기록도 이 정정에 맞춰 이미 수정함.

## 🖥 패널 생성 경로 (2026-08-14 확인)

- **`tmux split-window` 는 권한 `deny`** (`tmux new-session*`·`tmux new -s*` 도 deny). 에이전트가 직접 pane 을 못 만든다.
- **allow**: `cmux:*` · `~/.config/vibe-tools/claude-delegate.sh *` · `claude-send.sh *` · `tmux send-keys:*` · list/capture/display-message 계열.
  - ✅ 2026-08-14: 이 allow 들이 가리키던 `~/.config/vibe-tools/*.sh` 가 실재하지 않아 죽은 룰이었음 → `tmux-suite/install.sh` 에 [4/4] 공용경로 심링크 배포 단계를 추가하고 실행, 9개 링크 생성으로 **살아남**. 비대화형 `zsh -c ~/.config/vibe-tools/vibe.sh ...` 동작 실증 완료(같은 명령을 `vibe` alias 로 부르면 여전히 `command not found` — 의도된 차이).
- ⇒ **agy pane 생성 정식 경로 = `vibe delegate <프로젝트> --tool agy ["메시지"]`** (2026-08-14 지원 추가). `cmux` + `tmux send-keys` 2단계 우회는 폴백으로만. **실제 기동 미검증 — 다음 세션에서 1회 확인할 것.**
- MCP 실측 제약: agy 에 SessionStart 없음(PreInvocation+invocationNum==1 로 에뮬), `type:"agent"` 훅 미지원.
- ✅ **agy 스킬 정본 직결(2026-08-14)** — agy 스킬 탐색이 `~/.agents/skills` **복사본**을 보던 구조를 `~/.gemini/config/skills.json` 선언으로 **vibe-ai-config/skills 직결**로 전환. 탐색이 `<root>/<스킬>/SKILL.md` 1단계 평면이라 중첩 그룹 17개를 entries 로 펼쳐야 하는데, 손 관리 대신 `antigravity/generate-agy-skills-json.sh` 가 스캔·생성하고 루트 `install.sh` [3/5] antigravity 분기에서 자동 실행된다(hooks 생성기와 같은 패턴). 스펙 근거: `agy-customizations/docs/json_configs.md`.
  - 검증: agy 재시작 후 "`ps` 스킬 실제 로드 경로" 질의 → `/Users/eunsol/Project/vibe-ai-config/skills/work/tracking/ps/SKILL.md` 응답(신규 세션·도구 호출 없이 메타데이터에서 즉답 → 선언이 실제 반영됨).
  - ⏭️ **미정리(사용자 판단으로 보류)**: `sync-skills-to-agents.sh` 의 agy 복사 구간과 `~/.agents/skills` 복사본 53개는 그대로 둠. 중복 로드 여부 관찰 후 별건 제거.

## 🏠 노션 홈 대시보드 (2026-08-09 진행 중)

- 대상: `Home` 위키 페이지. **상단(Dash Board 제목·시계·날씨·구분선·빈 aside)은 유지 대상** — 손대지 말 것.
- 현재 남은 것: **🔗 바로가기**(2열 — 왼쪽 `02 Areas`: 일지·Diet·Ingredients·Household Ledger·거래내역·Ledger / 오른쪽 `01 Projects`: Projects·Tasks + 03·04 진입) + **📊 지금 상태**(프로젝트 상태 도넛·Task 상태 도넛·월별 지출 추이 막대).
- 시행착오로 만들었다 **삭제한 것**: 돈 자세히·AI가 만진 것·PARA 구역 3개 섹션(사용자가 UI에서 삭제).
- **개인관리는 PARA 상 02 Areas** — 바로가기 분류의 기준(사용자 지적, 2026-08-09).
- ✅ 월별 지출 추이 X축 해결: DSL 로 날짜 묶음 단위 지정 불가 → `월 예산` **relation 으로 GROUP BY** 하여 월별 막대 완성(1,911건 전부 relation 연결 확인).
- 🚨 **핵심 제약 — `Home` 은 위키 DB 라 페이지 블록을 MCP 로 읽을 수 없다.** `notion-fetch` 가 DB 스키마·뷰만 반환(URL 형식 3종 시도 모두 동일). 쓰기(insert/update_content)는 되지만 읽기가 안 돼서 정확한 수정·삭제가 불가능(차트 블록 삭제 실패 사유).
  - **다음 행동: 대시보드를 일반 페이지(예 `🏠 대시보드`)로 이전** → 그 후엔 전체 블록 읽기·수정 가능. `Home` 위키는 문서 인덱스로 존치.
- **바로가기 최종안(사용자 확인 대기)**: 2열 — 왼쪽 `02 Areas`(Diary·Food·Budge) + `01 Projects`(Project) / 오른쪽 `03 Resources`(Resource·경험 정리·Tags) + `04 Archives`(Archive). DB 직접 링크는 제외(각 페이지 안에서 접근). 페이지 URL 은 Home 위키 DB 조회로 확보 가능.
  - 미확인: Diary·Food·Budge·Project 페이지 **안에 해당 DB 가 실제로 들어 있는지** — 껍데기면 링크드 뷰 추가 필요.
- MCP 제약 정리: `status` 속성 필터 무시됨(select 는 정상) · 수식 속성 GROUP BY 불가 · 차트/뷰는 페이지 **끝에만** 추가(중간 삽입·토글 내부 배치 불가).

### ✅ 새 홈 페이지 확보 — 2026-08-09

- **노션 기본 Home 이 사용자 화면에 보이지 않음** → 사용자가 일반 페이지 `Home` 신설: `https://app.notion.com/p/3b7a25196d34804b9d70e3fb61c9175b` (최상위, 아이콘 home_gray).
- **일반 페이지 = fetch 로 전체 블록 읽기 가능 확인**(현재 내용 비어 있음). 위키 사각지대 해소 — 앞으로 대시보드 편집은 이 페이지에서 한다.
- 구 `Home` 위키(`ab742f27…`)에 남아 있는 것: 상단 헤더(Dash Board aside·시계·날씨 위젯·구분선·빈 aside) + 바로가기 + 차트 3종(프로젝트 상태·Task 상태·월별 지출 추이). **차트/뷰 블록은 API 로 이동 불가 → 새 페이지에서 재생성해야 함**(정의는 아래 및 위 기록 참조). 헤더 위젯은 UI 에서 복사·이동.

### 📦 이관 실행 결과 — 2026-08-09 (사용자 수행 + Claude 정리)

- **사용자가 이관 완료**: 헤더(Dash Board·시계·날씨·구분선·빈 콜아웃) + 진입 페이지 6종(Project·Food·Budge·경험 정리·Resource·Tags·Archive)이 새 `Home` 일반 페이지(`3b7a2519…175b`)로 이동. 구 위키에 남은 것은 16개(진입 페이지 `Diary` 1 + 템플릿 5 + 회고 프롬프트 5 + 연말회고 5).
- **바로가기 재구성 완료(Claude)**: DB 직접 멘션 8개(Diary DB·Diet·Household Ledger·Ingredients·Projects·Tasks·거래내역·DB) → **진입 페이지 경유** 2열로 교체. 왼쪽 `02 Areas`(Diary·Food·Budge) + `01 Projects`(Project) / 오른쪽 `03 Resources`(Resource·경험 정리·Tags) + `04 Archives`(Archive). **DB 바로 링크 금지 = 사용자 방침(2026-08-09).**
- **진입 페이지 실체 확인(위키 밖이라 이제 읽힘)**: Project=Current Projects 링크드뷰+Projects DB · Food=이번 주 현황 DB+식재료 현황 토글 DB · Budge=Quick Actions 버튼+지출 통계/지출 정리/이전 지출 내역 DB · Diary=다이어리 DB+회고 DB+프롬프트·템플릿 토글. **껍데기 아님 — 링크드 뷰 추가 불필요.**
- ~~Budge 페이지가 구 지출 DB 3종을 물고 있음~~ → **오진이었음(2026-08-09 정정)**. 3개 블록 전부 현행 체계였다: `7129a14e`=🏦 HL(`month view`) · `2ad01c66`=🧺 Ledger(`고정 지출`·`지출보드`) · `280a2519`=🧺 Ledger(`기본 보기`, 실행=완료분). **링크드 뷰의 정체는 블록 URL 을 fetch 해 `data-source` 를 확인해야 알 수 있다 — 블록 제목만 보고 판단하지 말 것.**
- 남은 것: ① **차트 3종 재생성**(프로젝트 상태·Task 상태·월별 지출 추이 — API 이동 불가, 페이지 끝에만 추가 가능) ② 하단 콜아웃 5개(이관된 자식 페이지 담긴 껍데기) UI 정리 — API 삭제 시 자식 페이지까지 삭제 위험이라 손대지 않음 ③ `Diary` 진입 페이지 위키 밖으로 이동 ④ 위키 이름 `03 Resources` 로 변경.

### 🗂 탭 블록 도입 + Index 탭 완성 — 2026-08-09

- **노션 신규 `탭(Tabs)` 블록은 MCP 로 읽기·쓰기 모두 된다** — 마크다운 스펙 문서에는 없지만 `<tabs>`/`<tab>` 로 실제 동작(실측). 현재 탭 3개: `Index`(완성) · `Pulse`(빈) · `Week`(빈). 탭 이름 규칙 = 영문 명사 1단어(볼트 페이지명 Diary·Food·Budge·Project 와 동일 톤).
- 🚨 **`update_content` 다중 라인 매칭은 탭이 있는 페이지에서 실패한다.** 컨테이너 태그(`<column>`·`<tab>`) 포함 old_str 은 "No matches found". 단일 라인만 매칭됨. 게다가 탭 경계에서 삽입하면 **뒤따르는 블록이 탭 안으로 빨려 들어가고 헤딩이 소실**된다(실측 2회: `## 🔗 바로가기` 헤딩 소실, 콜아웃 안 `Project` 자식 페이지 블록이 본문에서 빠짐 — 페이지 자체는 무사, 부모가 Home 직속으로 변경).
  - **결론: 탭 있는 페이지의 구조 편집은 `replace_content`(전체 재작성)로만 한다.** 자식 페이지(`<page>`)를 새 콘텐츠에 전부 포함시키면 유실 없음(검증 완료).
  - 사용자가 UI 에서 동시 편집 중이면 매칭이 어긋난다 — 편집 전 재조회 필수.
- **Index 탭 확정(안 1 = PARA 4구역 카드)**: 2열 50:50, 각 열에 콜아웃 카드 2장. **PARA 구역 4색 고정 — Areas `blue_bg` / Projects `green_bg` / Resources `purple_bg` / Archives `gray_bg`** (볼트 전체 재사용 규칙). 카드 안은 자식 페이지 블록(아이콘 유지·화살표 없음). 좌 4항목 / 우 4항목으로 높이 균형. 배치는 번호순이 아니라 사용 빈도순.
- **링크 표현 방침(사용자)**: 멘션·링크의 ↗ 화살표를 싫어함 → **자식 페이지 블록** 사용. DB 직접 링크도 금지(진입 페이지 경유). 아이콘은 이모지가 아니라 **노션 기본 아이콘** 계열로 통일.
- **`Pulse` 탭 완성(2026-08-09)**: 2열에 도넛 2종(프로젝트 상태·Task 상태) + 하단에 월별 지출 추이 막대. `notion-create-view`(parent_page_id)로 만들면 **페이지 끝에 생성**되고, `replace_content` 로 **탭 안으로 이동 가능**(검증 완료).
  - 🚨 **MCP DSL 은 `status` 타입 필터를 조용히 버린다** — `FILTER "Status" = "In progress"` 를 넣어도 `advancedFilter.filters: []` 로 저장됨. **`select` 필터는 정상**(`타입=지출` 반영 확인). UI 에서 직접 걸면 `simpleFilters` 로 정상 저장되므로, status 필터가 필요한 뷰는 **생성만 MCP·필터는 UI** 로 분담한다.
  - **숫자 카드는 폐기**(status 필터 불가로 전체 개수만 표시). 도넛 2종은 사용자가 UI 에서 `To-do + In progress` 그룹 필터를 걸어 활성만 남김.
  - 실데이터(2026-08-09): Projects 108건 중 활성 16(Backlog 6·Paused 5·In progress 3·Planning 2), Tasks 556건 중 활성 3(In progress 2·Not started 1). **누적 Done(86·529)은 지표가 아니라 아카이브 크기** — 필터 없이는 도넛이 Done 덩어리 하나가 되어 무의미.
- **월별 지출 차트 = 🏦 Household Ledger DB + `총지출` 수식 기준이 정답**(2026-08-09 확정). 거래내역 DB 기준으로 만들면 `금액`이 음수 저장이라 막대가 아래로 뻗는데, **차트에는 부호 반전·절대값 옵션이 없다.** HL 은 월 단위 행이라 X축도 자연스럽고 `총지출` 수식이 Y축 집계로 정상 동작한다.
  - 🚨 **Y축 선택 가능 조건은 미규명.** 거래내역에서는 수식(`총지출액`·`abs()` 신설분·상수 `1` 테스트까지)이 전부 Y축 목록에 뜨지 않았으나, HL 에서는 `총지출` 수식이 정상 선택된다. DB 별로 갈리는 원인 불명 — **차트를 만들 때는 추측하지 말고 대상 DB 에서 Y축 목록을 먼저 확인할 것.**
  - 🔧 **차트는 MCP 생성 → UI 마무리** 분담이 고정 패턴. View DSL 이 못 다루는 것 3종은 반드시 UI 에서: ① **숫자 정밀도**(축약 2.3M → 원값) = `chartFormat.numberPrecisionOverride: "precision_uncapped"` ② **날짜 그룹 단위**(DSL 은 항상 `day` — 월별로 보려면 Month 로 변경) ③ **`status` 필터**. DSL `CHART` 가 받는 건 AGGREGATE·COLOR·HEIGHT·SORT·STACK BY·CAPTION 뿐.
  - 시행착오로 만들었다 **되돌린 것**: 거래내역 `지출액` 수식(`abs(prop("금액"))`), `총지출액` 수식(기존 자산이었으나 불필요 판정으로 제거), HL `월지출` number 속성 + 12개월 수동 백필. **파생 데이터를 수동 복제하지 말 것** — 거래내역이 이미 relation 으로 연결돼 있어 중복이고, 새 거래마다 어긋난다(사용자 지적).
  - 부수 수정: `2026년 06월 지출` HL 행의 `Date` 오류 정정(2026-08-06 → 2026-06-01). 다른 행은 전부 해당 월 1일.
- **`예산외` 판정 기준 = 뱅샐 `메모`의 `#예산외지출` 태그**(2026-08-09 규명, 문서 미기재였음). 노션 거래내역의 `예산외` 체크박스는 이 태그가 달린 거래에만 설정된다. **현재 태깅은 2026-06 8건뿐**(원본 엑셀에도 6월만 존재 — import 누락 아님, 태깅을 6월부터 시작). 따라서 HL `예산외지출` rollup 이 6월만 표시되는 건 정상. 과거 달 소급 분류는 데이터상 근거가 없어 수동 판단 필요 — 별도 작업.
  - 🚨 **뱅샐 export 에는 예산외 플래그가 없다**(2026-08-09 실측). `가계부 내역` 시트 10컬럼(날짜·시간·타입·대분류·소분류·내용·금액·화폐·결제수단·메모) 어디에도 없고, `뱅샐현황` 시트(고객정보·현금흐름·재무·보험·투자·대출)에도 없음. **앱에서 예산외로 설정해도 노션으로 넘어오지 않는다 — 반드시 뱅샐 `메모`에 `#예산외지출` 태그를 직접 달 것.**
  - 참고: `고정` 체크박스는 전 기간 채워져 있음(월 12~17건). db-requirements S15 의 "7월 고정 12건 백필"은 이후 전월로 확장 완료된 상태.
  - 💡 **`뱅샐현황` 시트에 대분류별 월별 지출 집계표 있음**(경조선물·교통·금융·기타비용·문화여가·생활용품·식비·의료건강·의복미용·주거통신 × 13개월, 이체 제외·양수). 노션 카테고리별 집계 검증의 기준 데이터로 활용 가능.
- **뱅샐 import 파이프라인 정규화 완료(2026-08-09)** — 정본 = `02.Areas/07.개인관리/03.예산.md` §뱅크샐러드 import 파이프라인. 4단계(Gmail 수신·다운로드 → 파싱 → 검증 → 노션 업로드)이며 **① 첨부 저장만 수동**(Gmail MCP 에 첨부 다운로드 도구 없음). 메일 규격: 발신 `export-noreply@banksalad.com` · 제목 `{이름}님의 뱅크샐러드 엑셀 내보내기 데이터 (YYYY-MM-DD HH:MM:SS)`.
  - 🐛 **파서 실질 버그 발견·수정**(vibe-ai-config `62ed4d3`): `parse_banksalad.py` 가 **첫 시트만 읽어** 현재 형식의 뱅샐 파일에서 **거래 0건**을 반환하고 있었다(xlsx 시트 2개 — `뱅샐현황`·`가계부 내역`). 헤더 탐지되는 시트 중 행 최다를 고르도록 변경 + 시트 정렬을 숫자 기준으로.
  - **판정 규칙을 파서에 내장**(요청): `fixed` = 소분류 ∈ {서비스구독·보험·기부·통신비·월세·관리비·**전기세**}, `out_of_budget` = 메모 `#예산외지출`. **파서와 03.예산.md 는 항상 함께 갱신할 것.**
  - VERIFY: 실파일 1,931건 파싱 → 8월(노션 미import) 제외 시 fixed 187건·oob 8건으로 **노션 실데이터와 전건 일치**(소분류별로도 일치).
- **뱅크샐러드 엑셀 ↔ 노션 교차검증(2026-08-09)**: 엑셀 `2025-08-02~2026-08-02.xlsx` 기준 지출 1,186건 −23,098,770 vs 노션 1,175건 −22,830,555 → **차이는 정확히 2026-08 분 11건 268,215원**(미 import). 나머지 12개월 완전 일치. 기록에 남아 있던 "6월 13,160원 차이"는 이 기준에선 나타나지 않음. 로컬 집계 스크립트: `openpyxl` 로 `가계부 내역` 시트(헤더: 날짜·시간·타입·대분류·소분류·내용·금액·화폐·결제수단·메모) 파싱.
- **거래내역 `대분류`·`소분류` text → select 전환 완료(2026-08-09)**: 대분류 21옵션·소분류 30옵션, **1,911건 값 손실 0**(변환 전후 GROUP BY 분포 전수 대조 검증). `ALTER COLUMN "X" SET SELECT('값':색, ...)` 로 옵션을 미리 정의하면 기존 텍스트 값이 그대로 매핑된다. 색은 계열별 통일 — 식비 orange · 주거/생활 blue · 문화여가 purple · 교통 brown · 의료 red · 경조/미용 pink · **수입 계열(급여·부수입·기타수입·보험금·투자·저축) green** · 미분류/기타 gray.
  - 효과: select 는 필터·GROUP BY 가 모두 정상 동작 → **카테고리별 지출 도넛을 MCP 로 생성 가능**(`GROUP BY "대분류"` + `FILTER "타입"="지출"` + `sum ON "지출액"`). status 와 달리 제약 없음.
- **`Week` 탭 폐기 → 최종 2탭 확정(`Index` / `Pulse`, 2026-08-09).** 넣으려던 내용(이번 주 일지·식단·마감 Task)이 전부 진입 페이지(Diary·Food·Project)에 이미 있어 **두 군데서 관리하게 되는 중복**이었다. **홈은 색인(Index)과 지표(Pulse)만 담당하고 상세는 진입 페이지가 갖는다** — PARA 원칙과도 정합.
- **Pulse 2구획 확정**: `### 작업`(프로젝트·Task 도넛) / `### 돈`(월별 지출). 색은 쓰지 않는다 — **4색은 Index 의 PARA 구역 코드 전용**이라 Pulse 에 색을 넣으면 의미가 충돌한다.
- **추가 지표 검토 결과 — 전부 보류(2026-08-09)**. 데이터를 다 훑었고 결론은 "지금 3개가 상한".
  - ❌ 예산 잔여 추이(HL `AllLeftAmount`) — **월초에 전월 지출을 일괄 업로드**하는 운영이라 월중 잔여가 실시간이 아니다(사용자).
  - ❌ 다이어리 작성 추이 — 데이터는 충분(262건: 2022=29·2023=57·2024=82·2025=60·2026=33)하나 불필요 판단.
  - ❌ 위시리스트 대기 금액(🧺 Ledger) — 대기 8건 41.5만(아직여유 7·실행예정 1). 그때그때 갱신하지 않으면 예산 잔여와 같은 이유로 무의미.
  - ❌ 위시리스트 상태 도넛 — 555건 중 지출완료 447(80%)로 **Projects·Tasks 와 같은 "완료 덩어리" 함정**.
  - ❌ 카테고리별 지출 — 거래내역 `금액`이 음수라 **금액 기준 차트 불가**(건수 기준은 의미 약함). 양수 집계를 든 DB 가 없다.
  - 🚨 **식단 지표는 데이터가 아니라 운영이 빠진 상태** — 🥕 Ingredients 52건 중 **`보유 중` 체크 0건**. 재고 SoT 로 정한 속성이 신설만 되고 운영 미개시. 체크를 쓰기 시작해야 재고 도넛이 의미를 갖는다.
  - 🚨 **다이어리에 감정·기분 속성이 없다** — 속성은 Title·Year·Quarter·Tags(회고/일상/OJT)·AI 요약뿐. 기분은 본문 텍스트에만 존재하므로, 지표화하려면 `기분` select 신설 + 262건 소급 입력이 필요하다.
- 남은 다듬기(선택): Task 도넛은 활성 3건뿐이라 조각 2개 — 숫자 카드/리스트 대체 검토. Pulse 월별 지출 차트는 UI 에서 숫자 정밀도·월 그룹 조정 필요.

### 💰 예산 3-DB 역할 확정 — 2026-08-09 (사용자 정의)

**정본 = `02.Areas/07.개인관리/03.예산.md` §3-DB 역할** (해당 절 신설). 8/6 기술("HL = 메인 예산")을 대체한다.

| DB | 역할 |
|---|---|
| **💳 거래내역** | **실제 거래를 저장하는 원장(SoT)** — 모든 수치의 출발점 |
| **🏦 Household Ledger** | **거래내역의 통계** — 월 단위 집계만, 자체 거래 데이터 없음 |
| **🧺 Ledger** | **위시리스트** — 구매하면 `매핑 거래` relation 으로 거래내역에 연결 |

- HL 수치가 이상하면 **거래내역을 먼저 본다**(HL 은 파생 집계).
- 🧺 Ledger 는 지출을 직접 기록하는 곳이 **아니다** — 구매 전 후보 목록.
- ⚠️ `03.예산.md` 의 **카테고리 7종·절차·본문 템플릿 절은 구버전**(실제는 대분류 21종/소분류 30종 select, 월간 페이지 = HL 행). 문서에 경고 배너를 넣어뒀고 **전면 재작성은 여전히 대기 중**.

### 🧹 진입 페이지 정리 — 2026-08-09 (Project · Food · Diary · Budge)

**공통 규칙**(앞으로 진입 페이지 손볼 때 그대로 적용): ① 헤딩 바로 아래 구분선은 제거 — 헤딩 자체가 시각 구분이라 중복 ② 자주 쓰는 것 위로, 참고 자료는 **토글**로 접기 ③ **제목과 내용이 어긋나면 제목을 내용에 맞춘다**.

- **Project**: 빈 동기화 참조 제거 · `Current Projects` → **`작업 현황`**(그 링크드 DB 안에 Tasks 뷰 2개 + Projects 뷰 1개가 섞여 있어 제목이 사실과 달랐음) · 전체 프로젝트(108건)를 토글로 접음 · 말미 빈 블록 제거.
  - **뷰를 블록으로 나누지 않기로 결정** — Tasks 활성이 3건뿐이라(In progress 2·Not started 1) 나누면 **거의 빈 보드 2개**만 늘어난다. Projects 는 활성 16건이라 볼 만함. **Tasks 를 실제로 굴려 스프린트에 10~20건 쌓이면** 그때 `진행 중 프로젝트` / `이번 스프린트` / `전체`로 분리한다.
  - 남은 UI 작업: `작업 현황` 블록의 **기본 뷰를 `Current Project Board`로** 지정(블록 내 뷰 순서·기본값은 MCP 불가).
- **Food**: 헤딩 아래 중복 구분선 2개 제거. 구조는 원래 양호(이번 주 현황 + 식재료 현황 토글).
- **Budge**: **예산 3-DB 역할 확정에 맞춰 재구성**(아래 참조) — `월별 통계`(HL) → `위시리스트`(Ledger) → `구매 완료` 토글(Ledger 완료분) → `거래내역` 토글(💳 신규 추가). Quick Actions 동기화 블록의 버튼 3개는 `<unknown url=... alt="button"/>` 로 재현해 보존(검증 완료).
  - ⚠️ **HL 스키마가 이 세션 중 사용자에 의해 바뀜**: `BasicLedgerPrice` → **`LedgerPrice`** 로 개칭, `AllExpenditurePrice` 삭제. Home Pulse 월별 지출 차트는 `총지출` 을 쓰므로 영향 없으나, `총지출` 수식이 삭제된 속성을 참조했다면 깨질 수 있어 **화면에서 값 확인 필요**.
- **Diary**: 중복 구분선 제거 + **`연말 회고` 토글 신설**. 기존엔 `템플릿` 토글 안에 템플릿 4개와 연말회고 문서 5개·기록 수집·앨범 정리·작성 절차가 뒤섞여, 템플릿 하나 꺼내려면 1년에 한 번 쓰는 루틴이 같이 쏟아졌다. **내용 변경 없이 위치만 이동** — 자식 페이지 14개(프롬프트 5·템플릿 4·연말회고 5) 전수 보존 검증.

### 🎯 도구 목적별 재배치 — 2026-08-09 확정

> 원칙: **도구를 목적에 맞게 쓴다.** 현재 `Home` 위키에 PARA 진입 페이지가 섞여 있는 것은 위키를 홈 대시보드로 쓰던 시절의 잔재 — 정리 대상(사용자 확인).

| 도구 | 용도 | 대상 |
|---|---|---|
| 일반 페이지 | **진입점·대시보드** (레이아웃 자유 + AI 가 블록 읽기 가능) | `🏠 대시보드` 신설 · PARA 진입 페이지 5종 |
| 위키 DB | **03 Resources = 지식 창고** (하위 페이지 자동 인덱싱 + 태그) | 템플릿 5 · 회고 프롬프트 5 · 경험 정리 · Tags |
| 일반 DB | **데이터** | Projects·Tasks·Diary·Diet·Ingredients·Household Ledger·거래내역·Ledger |

**이관 순서(안전순)**: ① `🏠 대시보드` 일반 페이지 신설(현 Home 내용 이전) → ② 진입 페이지 5종(Project·Diary·Food·Budge·Archive) 위키 밖으로 이동 → ③ 위키 이름 `03 Resources` 로 변경 → ④ 대시보드 바로가기를 새 위치로 연결.
- 부수 효과: 진입 페이지가 위키를 벗어나면 **AI 가 그 페이지들도 읽기·수정 가능**해짐(현재는 Diary·Food·Budge 내부 확인 불가).
- 이동 시 페이지 링크는 유지되나 위키 전용 속성(소유자·인증)은 소실 — 개인 볼트라 실사용 없어 무해.
- 연말회고 5종은 Archive 로 이관 검토(자료가 아니라 산출물).
- 부수 변경: 거래내역에 `총지출액` 수식 추가(`타입=지출`이면 −금액, 이체·수입 제외).

## 🆕 신규 프로젝트 — 노션 루틴 3종 업그레이드 (2026-08-02 착수)

- 위치: `01.Projects/노션_루틴_업그레이드/` — `requirements.md`(§0 아키텍처 + 일정 R1-6·예산 B1-4·식단 D1-2, 설계 4결정 확정) + `diagnosis.md`(진단 + 진행 추적) + `design.md`(3계층 아키텍처 + 기능 설계).
- 진행: **Phase 1 안정성 완료**(vibe-ai-config `8fe8509`·`23b5d0d`, push 완료) → **도메인 정본 정비 완료**(02.Areas/07.개인관리(구 Notion-Ops → 도메인 상위로 개칭): ids.md(현 adapters/notion/ids.md)·04.일정.md 신설, 02/03/README 재편, "도메인 정본 + 스킬 어댑터" 원칙으로 CLAUDE.md/AGENTS.md 갱신) → **Phase 2+3 스킬 구현 위임 중**(pane %14, vibe-ai-config: ID 인용 전환·뱅크샐러드 import·wish list·월말 정리·요일×끼니·재고 SoT·GCal MCP 전환 등 11개 항목).
- 뱅크샐러드 드롭 폴더 생성됨: `~/Documents/banksalad/` (볼트 밖 — 금융 데이터 git 제외).
- **8/6 노션 DB 구성 업데이트 완료** (`db-requirements.md` 신설 — 업무컴 작성분 미접근으로 개인컴 재작성): ① 예산 실체 발견 — 이미 2-DB 체계(🏦 Household Ledger 월 페이지 + 🧺 Ledger 지출 트랜잭션, 카테고리 12종·실행 status) 운영 중, 도메인 문서(03.예산.md)의 "동적 검색+마크다운 표+7종"은 실체와 전면 불일치 ② 스키마 적용: Ingredients `보유 중`(재고 SoT)·Ledger `가맹점`+`출처` 추가 ③ **예산 3-DB 체계 구축(사용자 요구 확정)**: 🏦 Household Ledger(메인 예산, `거래내역` relation+`가계부금액` rollup 신설) + 💳 거래내역(뱅크샐러드 원본, 신설 `collection://f6f2513b-...`) + 🧺 Ledger(**위시리스트 역할 — 사용자 정정**, `매핑 거래` relation 신설; 최초 신설했던 별도 Wish List DB와 Ledger `가맹점`·`출처`는 정정에 따라 폐기/롤백) ④ ids.md에 예산 3-DB 등록 + 동적 검색 기술 폐기 ⑤ 재고 백필은 대상 0건(주간 relation이 placeholder `_` 뿐) ⑥ DB 잠금(UI Lock)은 MCP 스키마 변경을 막지 않음 확인(재조회 검증).
- **8/6 저녁 추가 진행**: ① 예산 3-DB 확정(메인=🏦 HL / 원본=💳 거래내역 / 위시=🧺 Ledger) + HL↔Ledger 관계 절단 ② **7월 뱅크샐러드 import 완료**(122건, 원본 합계 일치 검증) ③ HL 표시 값 복원 — rollup 4종(수입금·변동지출·고정지출·예산외지출)+총지출, 깨진 수식 3종 재정의, 고정 12건 백필. 상세: `db-requirements.md` S6~S15. 뱅샐 파일: `~/Documents/banksalad/2025-08-02~2026-08-02.xlsx`(1년치 — 나머지 11개월 import는 보류).
- **8/7(금) 업무컴에서 전월 일괄 import 완료** — 거래내역 총 1,911건, **이체 포함 방침 확정**. 개인컴 6월 import는 중복 방지로 취소. 미해소: 6월 지출 1건 13,160원 차이(개인컴 8/2 export 대비). 상세 `db-requirements.md` S16.
- **8/9 설정**: personal overlay 의 `model` 고정(`claude-fable-5[1m]`) 제거 — 업무컴과 동일하게 Claude Code 기본 모델(현 Opus 5 1M)을 따른다 (vibe-ai-config `7832457`, install.sh 재생성·검증 완료).
- **다음 행동: ① 03.예산.md 전면 재작성(3-DB·거래내역 파이프라인·이체 포함 방침 기준) + 02.식단.md '보유 중' 반영 ② notion-budget·notion-diet-manager 스킬을 실스키마 기준으로 갱신(pane %14 위임분 검증과 병합) ③ 전월 거래의 `고정` 백필(현재 7월만 완료 — 6월 이전은 미분류) ④ HL 월 페이지별 BasicLedgerPrice 확인(7월 0원) ⑤ 6월 1건 차이 추적 여부 결정.**

---

## ⭐ 0순위 — 개인관리 루틴 (매 세션 우선 수행)

> 어떤 툴(agy/Claude/Codex)에서든 요청 시 `02.Areas/07.개인관리/` 의 도메인 문서를 읽고 수행한다 (현재 저장소 어댑터: Notion MCP).

1. **다이어리** — 오늘 일지(감정/주요 사건/하이라이트) 기록 → SOP: `02.Areas/07.개인관리/01.다이어리.md`
2. **식단** — 오늘 식단 기록/관리 → SOP: `02.Areas/07.개인관리/02.식단.md`
3. **예산** — 지출/예산 기록·점검 → SOP: `02.Areas/07.개인관리/03.예산.md`

## 🔴 1순위 — Grafana 모니터링 실습 (`In progress` / 높음)

- 위치: `01.Projects/Grafana_모니터링_공부/`
- 현황: 이론 자료 17개 정리 완료. 그러나 `study_guide.md` 실습 체크리스트 **0/13** — 손 실습 미착수.
- **다음 행동: 기초 실습 3개 착수**
    1. Grafana 설치 및 실행 (Docker 권장: `docker run -d -p 3000:3000 grafana/grafana`)
    2. 기본 UI 이해 (로그인 → 데이터소스/대시보드 메뉴 탐색)
    3. 첫 번째 대시보드 생성
- 완료 시 `study_guide.md` 체크박스 갱신 → 다음은 중급(Prometheus 연동, PromQL).

## 🟡 2순위 — Election-2026-Local-Archive (외부 API 대기 + 검증)

- 위치: `01.Projects/Election-2026-Local-Archive/`
- 현황: 수집 스크립트 4종 완성. 6/13 시도 시 sgId=20260603이 `INFO-03`(데이터 없음) — 선관위 OpenAPI 반영(선거 후 2~3주) 대기 중. **7월 초면 반영됐을 가능성 높음 → 세션 열 때마다 재시도 가치 있음.**
- **다음 행동: `fetch_winners.py` 재실행으로 20260603 데이터 반영 여부 확인**
    - 성공 시: `docs/election_type_codes.md`의 sgTypecode 미검증 8개(1,2,4,5,6,7,8,9) 검증 → parsed 데이터 생성 → README §7 변경 이력 기록
    - 여전히 INFO-03이면: 상태만 이 파일에 기록하고 다음 순위로.

## 🗄️ ~~3순위 — Spring 프레임워크 개념·원리 조사~~ → **아카이브(2026-08-17)**

- 위치 이동: `01.Projects/` → **`04.Archives/Spring_프레임워크_개념_원리_조사/`** · 노션 `Canceled` + `ParaType=Archive`
- 사유: 2026-02-01 생성 후 6.5개월간 Spring 산출물 0건. 폴더에 있던 CQRS/Outbox 문서 6건은 `saga-pattern/` 과 동일 내용의 오배치여서 삭제(원본은 `saga-pattern/` 03~08 에 보존).
- 재개 시: 새 프로젝트로 시작할 것. 학습 범위 5개 영역(Core IoC/DI/AOP · MVC · Boot · Security · Data) 정의는 아카이브 README 에 남아 있어 출발점으로 재사용 가능.

## ✅ 완료 — 개인컴 AI 작업환경 업그레이드 (2026-07-17, 메인 도구: agy)

- agy(Antigravity) 메인 허브 + Claude/Gemini 보조 분업 체제 구성 완료 (`VIBE_HUB_TOOL=agy`). `vibe delegate <프로젝트> --tool <tool>` 로 적절한 도구에 위임 가능.
- 설계·계획: `01.Projects/개인컴_AI_작업환경_업그레이드/`
- 잔여 사용자 액션: ~~GitHub PAT 재발급~~ — 진행하지 않기로 결정(2026-08-06)

## 🧹 정리 작업 (짧게 끝남)

- [ ] **saga-pattern 마감 처리**: 자료 13/13 완비, 남은 액션 없음 → Notion PRO-117 을 `Done` 으로 올릴지 검토 (2026-08-17 현재 `Paused` — 산출물이 2026-02-26 이후 정지)
- [ ] **Diary 공백 메우기**: `02.Areas/01.Diary/` 주간 일지가 week 24(~6/14)에서 중단 — week 25~28 요약이라도 채우기

## ⏸ 보류 (재개 조건 명시)

- **legigraph** (`Paused`): 설계·와이어프레임 완료, 구현 미착수. 재개 시 첫 작업 = Atomic Design 컴포넌트 스캐폴딩 + GraphCanvas. 위 1~3순위가 정리되기 전엔 착수하지 않음.

## 📥 백로그 (Someday)

- ~~컴퓨터 구조 개념 정독 / 친절한 SQL 튜닝 정독~~ — **2026-08-17 아카이브**(생성 후 산출물 0건). 백로그 관리는 노션 `Projects` DB 로 일원화했다.
- LLM Wiki/KB 영상 시청 + PARA 적용 (노션 `Backlog`)

---

### 세션 종료 체크리스트 (에이전트용)

1. 진행한 항목의 현황·다음 행동을 위에서 갱신했는가?
2. `study_guide.md` 등 프로젝트 내 체크박스를 실제로 갱신했는가?
3. 최종 갱신 날짜를 오늘로 바꿨는가?
