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

## 🆕 신규 프로젝트 — 노션 루틴 3종 업그레이드 (2026-08-02 착수)

- 위치: `01.Projects/노션_루틴_업그레이드/` — `requirements.md`(§0 아키텍처 + 일정 R1-6·예산 B1-4·식단 D1-2, 설계 4결정 확정) + `diagnosis.md`(진단 + 진행 추적) + `design.md`(3계층 아키텍처 + 기능 설계).
- 진행: **Phase 1 안정성 완료**(vibe-ai-config `8fe8509`·`23b5d0d`, push 완료) → **도메인 정본 정비 완료**(02.Areas/07.개인관리(구 Notion-Ops → 도메인 상위로 개칭): ids.md(현 adapters/notion/ids.md)·04.일정.md 신설, 02/03/README 재편, "도메인 정본 + 스킬 어댑터" 원칙으로 CLAUDE.md/AGENTS.md 갱신) → **Phase 2+3 스킬 구현 위임 중**(pane %14, vibe-ai-config: ID 인용 전환·뱅크샐러드 import·wish list·월말 정리·요일×끼니·재고 SoT·GCal MCP 전환 등 11개 항목).
- 뱅크샐러드 드롭 폴더 생성됨: `~/Documents/banksalad/` (볼트 밖 — 금융 데이터 git 제외).
- **8/6 노션 DB 구성 업데이트 완료** (`db-requirements.md` 신설 — 업무컴 작성분 미접근으로 개인컴 재작성): ① 예산 실체 발견 — 이미 2-DB 체계(🏦 Household Ledger 월 페이지 + 🧺 Ledger 지출 트랜잭션, 카테고리 12종·실행 status) 운영 중, 도메인 문서(03.예산.md)의 "동적 검색+마크다운 표+7종"은 실체와 전면 불일치 ② 스키마 적용: Ingredients `보유 중`(재고 SoT)·Ledger `가맹점`+`출처`(뱅크샐러드 import 키) 추가 ③ ids.md에 예산 2-DB 등록 + 동적 검색 기술 폐기 ④ 재고 백필은 대상 0건(주간 relation이 placeholder `_` 뿐).
- **다음 행동: ① 03.예산.md 전면 재작성(2-DB·12종·실행 status 기준) + 02.식단.md '보유 중' 반영 ② notion-budget·notion-diet-manager 스킬을 실스키마 기준으로 갱신(pane %14 위임분 검증과 병합) ③ 실데이터 리허설(뱅크샐러드 샘플 dry-run) ④ 실보유 식재료 사용자 입력 받아 보유 중 체크.**

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
