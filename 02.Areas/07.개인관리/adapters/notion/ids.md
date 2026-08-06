# 🔑 노션 DB / Collection ID 정본 (ids.md)

> **이 파일이 노션 저장소 식별자(ID)의 단일 정본(SSoT)이다.**
> 도메인 허브([허브 README](../../README.md) · [[01.다이어리]] · [[02.식단]] · [[03.예산]] · [[04.일정]])와 스킬(vibe-ai-config `notion-*`)은 ID를 하드코딩하지 말고 이 파일을 인용한다.
> 노션(저장소) 교체·재구축 시 **이 파일만** 갱신하면 된다.

## ID 표

| 대상 | ID | 용도 | 출처 |
|---|---|---|---|
| 일지 및 회고 (Diary/Schedule) | data_source `d4c94e28-6040-45f4-a4ae-69b74a6b26b4` | 주간 일지·회고 페이지의 부모 DB — 주간 페이지 생성·검색 기준 | 스킬 `notion-weekly-schedule`·`notion-weekly-retrospective` references/page-structure.md, `notion-weekly-routine` references/slot-mapping.md |
| Diet | `collection://ed46300e-3f34-4ad5-8319-100810b659b9` | 주간 식단 페이지 DB | 스킬 `notion-diet-manager` references/db-schema.md |
| Ingredients | `collection://3f8112d6-3518-4d77-b86c-8e481c687d2f` | 식재료 마스터 DB — 재고('보유 중') SoT | 스킬 `notion-diet-manager` references/db-schema.md |
| Foods | `collection://8b14c31d-85b4-411d-a1ed-538222261d09` | 음식 마스터 DB | 스킬 `notion-diet-manager` references/db-schema.md |

## ID 없음 (동적 검색 도메인)

| 대상 | 식별 방법 |
|---|---|
| 예산 (월간 Budget 페이지) | **고정 ID 없음** — 명명 규칙으로 동적 검색: `{YYYY-MM} 예산` → `Budget {YYYY-MM}` → `예산 {YYYY}년 {M}월` → `가계부 {YYYY-MM}` (우선순위 순). 상세는 [[03.예산]] |
| 다이어리 (일간 페이지) | **고정 ID 없음** — 동적 검색: `{YYYY-MM-DD}` → `일기 {YYYY-MM-DD}` → `Diary {YYYY-MM-DD}` → `Daily {YYYY-MM-DD}`. 상세는 [[01.다이어리]] |

## 페이지 명명 규칙 (검색 키워드)

- 주차 계산: ISO 8601 (월요일 시작). 표준 검색 형식 `week {WW} {YYYY}`
- 일지/회고: 검색 `week {WW} {YYYY}` → 제목 `[week XX] @YYYY/MM/DD → YYYY/MM/DD 일지` ("식단" 페이지 제외)
- 식단: 검색 `week {WW} {YYYY} 식단` → 제목 `[week XX] @YYYY/MM/DD → YYYY/MM/DD 식단`
