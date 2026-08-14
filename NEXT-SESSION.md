# 🖥️ NEXT-SESSION — 개인 컴 작업 브리핑

> **이 파일은 세션 간 인수인계 SoT다.** 개인 컴에서 에이전트(agy 메인 허브·구현, Claude Code/Gemini 보조·조사) 세션을 열면
> 가장 먼저 이 파일을 읽고 최상위 작업의 "다음 행동"부터 이어서 진행한다.
> 작업 단위가 끝나면 해당 항목의 상태·다음 행동을 갱신하고 저장한다 (obsidian-git이 자동 백업).

**최종 갱신: 2026-08-06** (OMC 제거 후속 4건 전부 마감 — 설정 정비 완결)

## 🔧 2026-08-02 설정 정비 상태 (Claude Code 재시작 직전 저장)

- **OMC(oh-my-claudecode) 완전 제거 완료 + 재시작 검증 통과(2026-08-02)**: 재시작 후 세션에 omc 스킬/에이전트 0개, npm 전역 empty, installed_plugins/marketplaces 등록 없음, statusLine(claude-dashboard 1.26.2) 정상 확인. 잔여 데이터(`~/.claude/plugins/cache/omc/` 307MB, `~/.omc` 16K)도 사용자 승인 하에 삭제 완료 — 개인컴 OMC 흔적 0.
- **claude-dashboard 복구**: 삭제된 것 아니었음 — statusLine이 캐시에 없는 1.27.0을 가리켜 깨져 보임. 정본에서 1.26.2로 정합(vibe-ai-config 커밋 `a69b632`), settings.json 재생성됨.
- **7/31 개인컴 적용 런북**(스킬 npx 복사 전환·48개·8그룹) 적용 완료 상태 검증됨 — dangling 0, 48/48.
- 후속 — **전부 마감(2026-08-06)**: ① ~~업무컴에 OMC 제거 반영~~ (8/6 완료) ② ~~vibe-ai-config omc 잔여 참조 정리~~ (`pipeline` 스킬은 이미 제거돼 있었고, `multi-dispatch/SKILL.md` 상태 경로 `.omc/state` → `.claude/state` 대체, 커밋 `8954354`) ③ ~~`~/.omc` + 고아 캐시 삭제~~ (8/2 완료) ④ ~~para 볼트 `.omc/` 잔여물 삭제~~ (8/6 완료 — 디렉토리 제거 + `.gitignore`에 `.omc/` 추가).
- GitHub PAT 재발급(개인컴 AI 작업환경 잔여 액션)은 **진행하지 않기로 결정(2026-08-06)**.
- **8/6 설정 구성 감사 + 정리 완료**: ① `~/.claude/.omc*` 잔재 3건 삭제(8/2 정리 때 누락분 — 이제 OMC 흔적 진짜 0) ② 레거시 `~/.claude/config.json`(구식 MCP 설정) 삭제 ③ 고아 마켓플레이스 디렉토리(`affaan-m-everything-claude-code `) 삭제 ④ `plane-mcp@cc-claude`를 settings.base → work overlay로 이동(개인컴에서 조용한 로드 실패 해소) ⑤ allow 중복 패턴 18건 정리(88→70) ⑥ git 로컬 파괴성 명령(restore·checkout --·stash drop/clear·reset --hard) ask 승격(git * allow·push 무확인은 유지) — vibe-ai-config `d8c85a6`·`57471f5`, `./install.sh personal` 재생성 완료. **업무컴 후속: 다음 `git pull` + `./install.sh work` 시 자동 반영(plane-mcp는 work overlay 경유 유지).**

## 🔀 agy 메인 전환 준비 — 설정 점검 결과 (2026-08-09, 전환은 보류)

> 방침: 개인컴 메인 도구를 Claude Code → **agy(Antigravity)** 로 전환한다. **지금 전환하지 않고**, agy 설정이 갖춰진 뒤 실행한다.

**이미 갖춰진 것**: `VIBE_HUB_TOOL=agy`(~/.zshrc.local) · 규칙 주입 경로 작동(`~/.gemini/GEMINI.md` 관리 블록 = 정본 AGENTS.md + agy-tail, `~/.agents/AGENTS.md` 심링크) · 프로젝트 규칙(`para/GEMINI.md` → `@AGENTS.md`) · 스킬 53개(`~/.agents/skills`) · MCP 7종(notionMCP·google-calendar·context7·github·playwright·browsermcp·sequential-thinking) · SOP 워크플로우 4종 · 권한 시드.

**보완 필요 (전환 전)**
1. **훅 미배치 — 최대 갭이나 agy 지원은 확인됨(2026-08-09 실측).** agy 1.1.10 바이너리에 훅 엔진 구현 확인 — 이벤트 5종(PreToolUse·PostToolUse·PreInvocation·PostInvocation·Stop), `~/.agents/hooks.json`(전역)·`<ws>/.agents/hooks.json`. **즉 지원 여부가 아니라 "우리 훅 9종의 이식"이 남은 일.** 제약 2건: ⓐ **SessionStart 이벤트 없음** → 브리핑 주입은 `PreInvocation` + `invocationNum==1` 에뮬레이션 ⓑ Claude의 `type:"agent"` 훅(commit PHP LSP 게이트)은 agy 미지원(command 전용)이라 셸 재작성. 입출력 스키마도 달라(camelCase, `decision`/`injectSteps`) 어댑터 계층 필요. 상세 = vibe-ai-config `antigravity/README.md` 검증 이력(`5a7302a`).
2. ~~서브에이전트 미구현~~ → **정정(2026-08-09)**: `run_subagent`·`SubagentSpec`·`KillSubagent` 및 멀티에이전트 오케스트레이터(owl) 구현 확인. README의 "v2 후보" 기술이 agy 1.1.0 기준으로 낡았던 것. 남은 일은 위임 규율(CLAUDE-delegation.md)의 agy 이식뿐.
3. **스킬 3개 누락**: `notion-project-creator`(개인관리 도메인 — 확인 필요) · `skill-backup` · `update-vibe-commands`(Claude 전용 성격, 무시 가능).
4. **install.sh 문구 불일치**: 실행 로그의 "antigravity 어댑터 미구현 — skip(P3/P4)"과 실제 배포 상태(스킬 53개 존재)가 어긋남 → 배포 경로 확정 후 문구 정리(재설치 시 누락 위험).
5. **MCP 실호출 미검증**: notionMCP는 `mcp-remote` OAuth → 토큰 만료 시 재인증 필요. 전환 전 agy에서 Notion·GCal 1회 실호출 검증.
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
- **검증**: shellcheck 무경고 + `test.sh` 13/13(양 하네스 계약 전수). **agy 배선 완료**(`~/.agents/hooks.json`, install.sh 가 자동 생성). **Claude 배선은 보류** — briefing·activity 는 기존 훅과 중복이라, 신규 가치가 있는 `bash-chain-guard` 만 `settings.base.json` 에 추가하면 됨(절차는 `shared/hooks/README.md`, `ask` 모드로 시작 권장).
- MCP 실측 제약: agy 에 SessionStart 없음(PreInvocation+invocationNum==1 로 에뮬), `type:"agent"` 훅 미지원.

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

## 🟡 3순위 — Spring 프레임워크 개념·원리 조사 (`Planning`)

- 위치: `01.Projects/Spring_프레임워크_개념_원리_조사/`
- 현황: 학습 범위 5개 영역(Core IoC/DI/AOP, MVC, Boot, Security, Data) 정의만 됨. 폴더 안 자료는 CQRS/Outbox 뿐(saga-pattern과 중복) — 정작 Spring 자료 0개.
- **다음 행동: Spring Core(IoC/DI) 정리 노트 1편 작성 착수** → status를 In progress로.

## ✅ 완료 — 개인컴 AI 작업환경 업그레이드 (2026-07-17, 메인 도구: agy)

- agy(Antigravity) 메인 허브 + Claude/Gemini 보조 분업 체제 구성 완료 (`VIBE_HUB_TOOL=agy`). `vibe delegate <프로젝트> --tool <tool>` 로 적절한 도구에 위임 가능.
- 설계·계획: `01.Projects/개인컴_AI_작업환경_업그레이드/`
- 잔여 사용자 액션: ~~GitHub PAT 재발급~~ — 진행하지 않기로 결정(2026-08-06)

## 🧹 정리 작업 (짧게 끝남)

- [ ] **saga-pattern 마감 처리**: 자료 13/13 완비, 남은 액션 없음 → Notion PRO-117 상태 Done 검토 + `TASKS.md` Done 섹션 이동
- [ ] **Diary 공백 메우기**: `02.Areas/01.Diary/` 주간 일지가 week 24(~6/14)에서 중단 — week 25~28 요약이라도 채우기

## ⏸ 보류 (재개 조건 명시)

- **legigraph** (`Paused`): 설계·와이어프레임 완료, 구현 미착수. 재개 시 첫 작업 = Atomic Design 컴포넌트 스캐폴딩 + GraphCanvas. 위 1~3순위가 정리되기 전엔 착수하지 않음.

## 📥 백로그 (Someday)

- 컴퓨터 구조 개념 정독 / 친절한 SQL 튜닝 정독 (`TASKS.md` 참조)

---

### 세션 종료 체크리스트 (에이전트용)

1. 진행한 항목의 현황·다음 행동을 위에서 갱신했는가?
2. `study_guide.md` 등 프로젝트 내 체크박스를 실제로 갱신했는가?
3. 최종 갱신 날짜를 오늘로 바꿨는가?
