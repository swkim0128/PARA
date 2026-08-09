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
