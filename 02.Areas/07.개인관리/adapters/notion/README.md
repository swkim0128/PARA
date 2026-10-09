# 🔌 어댑터: 노션 — MCP 전제 조건 & 공통 절차

> 개인관리 도메인([허브 README](../../README.md))의 **현재 선택된 저장소 어댑터**. 도메인 규칙은 도메인 문서(`0X.*.md`)가 정본이고, 이 문서는 노션(저장소) 전용 전제 조건·조작 절차만 담는다. 저장소 교체 시 이 폴더(`adapters/notion/`)만 교체한다.

## 전제 조건 (툴별)

| 툴 | Notion 접근 방법 |
|---|---|
| Claude Code | claude.ai Notion 커넥터(MCP) 기본 연결됨. `notion-suite` 스킬 사용 가능 |
| agy (Antigravity) | Notion MCP 서버 연결 필요 (공식: `https://mcp.notion.com/mcp` 또는 API 토큰 기반 서버) |
| Codex | 동일 — `~/.codex/config.toml` 에 Notion MCP 등록 필요 |

도구 이름은 호스트마다 접두어가 다르지만 **기능은 동일 5종**이면 충분하다:
`notion-search`(검색) / `notion-fetch`(페이지·블록 조회) / `notion-create-pages`(생성) / `notion-update-page`(본문 수정) / `notion-update-data-source`(DB 속성 수정)

## DB ID · 페이지 명명 규칙

**→ [ids.md](ids.md) 단일 정본 참조.** 도메인 문서·스킬 어디에도 ID를 하드코딩하지 않는다.

## 공통 절차 사이클

1. `notion-search` 로 대상 페이지 검색 ([ids.md](ids.md) 명명 규칙의 키워드 순차 시도)
2. `notion-fetch` 로 구조 확인 (**fetch-first — 구조 확인 없이 수정 금지**)
3. `notion-update-page` / `notion-create-pages` / `notion-update-data-source` 로 변경
4. 필요 시 `notion-fetch` 재확인

## 노션 전용 주의

- **컬럼 레이아웃**: 노션 페이지가 `<columns>` 구조인 경우, 요일 슬롯 등 부분 수정 시 **해당 컬럼 전체 내용을 replace** (부분 replace는 다른 슬롯 삭제 위험).
- **🏦 Household Ledger 는 새 페이지의 `Name`·`Date` 를 생성 시점 기준으로 덮어쓴다** (2026-10-09 실측). MCP 로 `2026년 11월 지출`·`Date 2026-11-01` 을 넣어 만들었는데, 직후 `2026년 10월 지출`·`2026-10-09`(생성일)로 바뀌어 10월 페이지가 2개가 됐다 — 생성 응답은 입력값을 그대로 돌려주므로 **응답만 보면 못 잡는다.** 원인은 DB 기본 템플릿·자동화로 추정, 미확인. **사용자 규칙(2026-10-09): 미래 월 예산은 Household Ledger 에 미리 만들지 않는다** — 예산 관리 페이지(Budge) 아래 하위 메모 페이지로 계획을 적고, 그 달 1일에 월 페이지를 만들어 옮긴다. 월 페이지를 만들면 **생성 후 `Name`·`Date` 를 다시 조회**해 다르면 `update_properties` 로 되돌린다(되돌린 뒤 재편집에서는 유지됨 확인). DB 행을 빼낼 때는 MCP 에 삭제 도구가 없으므로 `notion-move-pages` 로 일반 페이지 아래로 옮긴다(DB 에서 빠지고 내용은 보존).
