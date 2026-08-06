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
