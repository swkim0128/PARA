# 🧭 Notion-Ops — 노션 루틴 관리 공통 규약 (툴 무관 SOP)

> **목적**: 노션 다이어리·식단·예산 관리를 **어떤 AI 툴(Claude Code, agy/Antigravity, Codex, Gemini)에서든** 동일하게 수행하기 위한 이식 가능한 절차서.
> 원본: Claude 플러그인 `notion-suite` 스킬 (2026-07-08 이식). Claude Code에서는 네이티브 스킬(`/notion` 계열)이 우선이며, 이 문서는 타 툴용 SoT이자 폴백이다.

## 전제 조건 (툴별)

| 툴 | Notion 접근 방법 |
|---|---|
| Claude Code | claude.ai Notion 커넥터(MCP) 기본 연결됨. `notion-suite` 스킬 사용 가능 |
| agy (Antigravity) | Notion MCP 서버 연결 필요 (공식: `https://mcp.notion.com/mcp` 또는 API 토큰 기반 서버) |
| Codex | 동일 — `~/.codex/config.toml` 에 Notion MCP 등록 필요 |

도구 이름은 호스트마다 접두어가 다르지만 **기능은 동일 5종**이면 충분하다:
`notion-search`(검색) / `notion-fetch`(페이지·블록 조회) / `notion-create-pages`(생성) / `notion-update-page`(본문 수정) / `notion-update-data-source`(DB 속성 수정)

## 핵심 DB ID (하드코딩 — 이 볼트의 유일한 구체 소스)

| DB | ID | 용도 |
|---|---|---|
| Diet | `collection://ed46300e-3f34-4ad5-8319-100810b659b9` | 주간 식단 페이지 |
| Ingredients | `collection://3f8112d6-3518-4d77-b86c-8e481c687d2f` | 식재료 마스터 |
| Foods | `collection://8b14c31d-85b4-411d-a1ed-538222261d09` | 음식 마스터 |
| 일지 및 회고 (Diary/Schedule) | data_source `d4c94e28-6040-45f4-a4ae-69b74a6b26b4` | 주간 일지·회고 |

다이어리(일간)·예산 DB는 ID 미고정 — 아래 검색 규칙으로 동적 발견한다.

## 공통 절차 사이클

1. `notion-search` 로 대상 페이지 검색 (아래 명명 규칙의 키워드 순차 시도)
2. `notion-fetch` 로 구조 확인 (**fetch-first — 구조 확인 없이 수정 금지**)
3. `notion-update-page` / `notion-create-pages` / `notion-update-data-source` 로 변경
4. 필요 시 `notion-fetch` 재확인

## 페이지 명명 규칙 (검색 키워드)

- 주차 계산: ISO 8601 (월요일 시작). 표준 검색 형식 `week {WW} {YYYY}`
- 일정/회고: `week {WW} {YYYY}` → 페이지 제목 `[week XX] @YYYY/MM/DD → YYYY/MM/DD 일지`
- 식단: `week {WW} {YYYY} 식단` → `[week XX] @YYYY/MM/DD → YYYY/MM/DD 식단`
- 다이어리: `{YYYY-MM-DD}` → `일기 {YYYY-MM-DD}` → `Diary {YYYY-MM-DD}` → `Daily {YYYY-MM-DD}`
- 예산: `{YYYY-MM} 예산` → `Budget {YYYY-MM}` → `예산 {YYYY}년 {M}월` → `가계부 {YYYY-MM}`

## 메타 룰 (전 도메인 공통)

1. **append-only**: 기존 본문·관계 배열을 덮어쓰지 않는다. 관계 업데이트는 기존 배열 유지 후 추가.
2. **idempotent**: 중복 기록 방지 (도메인별 중복 판정 기준은 각 SOP 참조).
3. **읽기/변경 의도 구분**: "보여줘/확인/얼마" → search·fetch만, update 금지.
4. **컬럼 레이아웃 주의**: 노션 페이지가 `<columns>` 구조인 경우, 요일 슬롯 등 부분 수정 시 **해당 컬럼 전체 내용을 replace** (부분 replace는 다른 슬롯 삭제 위험).
5. 슬롯 시각 매핑(주간 일지): 평일 LIFE1(06-09)·WORK1(09-12)·WORK2(12-15)·WORK3(15-18)·LIFE2(18-21)·LIFE3(21-24) / 주말 LIFE1~6 (3시간 단위). 시각 미상 항목을 LIFE1에 임의 배치 금지 — 저녁(LIFE2·3)에 보수 배치하거나 사용자에게 확인.

## 결과 보고 템플릿

```
✅ 작업 완료
📄 페이지: [<페이지명>](<URL>)
🔄 변경: <한 줄 요약>
📌 다음 단계: <옵션>
```

## 도메인 라우팅

| 사용자 표현 | SOP |
|---|---|
| 기분·하루·오늘 어땠는지·일기 | [01.다이어리](01.다이어리.md) |
| 먹었어·식재료·장 봤어 | [02.식단](02.식단.md) |
| ~원·지출·구매·카드·잔액 | [03.예산](03.예산.md) |
| 회고·KPT·주간 일정 | (Claude: `notion-suite` weekly 스킬 / 타 툴: 위 DB ID + 슬롯 매핑 참조) |
