# 🔑 노션 DB / Collection ID 정본 (ids.md)

> **이 파일이 노션 저장소 식별자(ID)의 단일 정본(SSoT)이다.**
> 도메인 허브([허브 README](../../README.md) · [[01.다이어리]] · [[02.식단]] · [[03.예산]] · [[04.일정]])와 스킬(vibe-ai-config `notion-*`)은 ID를 하드코딩하지 말고 이 파일을 인용한다.
> 노션(저장소) 교체·재구축 시 **이 파일만** 갱신하면 된다.

## ID 표

| 대상 | ID | 용도 | 출처 |
|---|---|---|---|
| 일지 및 회고 (Diary/Schedule) | data_source `d4c94e28-6040-45f4-a4ae-69b74a6b26b4` | 주간 일지·회고 페이지의 부모 DB — 주간 페이지 생성·검색 기준 | 스킬 `notion-weekly-schedule`·`notion-weekly-retrospective` references/page-structure.md, `notion-weekly-routine` references/slot-mapping.md |
| Diet | `collection://ed46300e-3f34-4ad5-8319-100810b659b9` | 주간 식단 페이지 DB | 스킬 `notion-diet-manager` references/db-schema.md |
| Ingredients | `collection://3f8112d6-3518-4d77-b86c-8e481c687d2f` | 식재료 마스터 DB — 재고 SoT는 `보유 중` checkbox (2026-08-06 신설) | 스킬 `notion-diet-manager` references/db-schema.md |
| Foods | `collection://8b14c31d-85b4-411d-a1ed-538222261d09` | 음식 마스터 DB | 스킬 `notion-diet-manager` references/db-schema.md |
| 🏦 Household Ledger | `collection://17f03db9-14ee-4379-bd14-f47194444f87` | 월간 예산 페이지 DB — 제목 `YYYY년 MM월 지출`, 예산·입금·저축 속성 + `거래내역` relation·`가계부금액` rollup(2026-08-06 신설). 구 Ledger relation·rollup은 2026-08-06 절단(수식 재정의 잔여) | 2026-08-06 실스키마 조사 (`01.Projects/노션_루틴_업그레이드/db-requirements.md`) |
| 🧺 Ledger | `collection://7391b842-ef1c-42c5-a7ca-d82068dbaccd` | 지출 트랜잭션 + **위시리스트** DB — 실행 status(아직여유/실행고민/실행예정→실행완료/지출완료/실행취소)가 wish 후보→구매 라이프사이클 담당. `매핑 거래` relation(2026-08-06 신설)으로 거래내역과 연결 | 2026-08-06 실스키마 조사 (`db-requirements.md` §2-b) |
| 💳 거래내역 | `collection://f6f2513b-0caa-4fb2-b831-ccc5ea8a04d5` | 뱅크샐러드 가계부 원본 DB (2026-08-06 신설) — 거래일·금액·타입·대분류·소분류·결제수단·`월 예산` relation·`위시리스트` relation(←Ledger). 중복 키 = 거래일+금액+Name | `db-requirements.md` §2-b |

## ID 없음 (동적 검색 도메인)

| 대상 | 식별 방법 |
|---|---|
| 다이어리 (일간 페이지) | **고정 ID 없음** — 동적 검색: `{YYYY-MM-DD}` → `일기 {YYYY-MM-DD}` → `Diary {YYYY-MM-DD}` → `Daily {YYYY-MM-DD}`. 상세는 [[01.다이어리]] |

> ⚠️ **예산은 동적 검색 도메인이 아니다** (2026-08-06 정정): 월간 페이지는 Household Ledger DB 소속이며 제목 규칙은 `YYYY년 MM월 지출`. 구 검색 키워드(`{YYYY-MM} 예산`·`Budget {YYYY-MM}`·`가계부`)는 실체와 불일치해 폐기. [[03.예산]] 재작성 전까지 본 표가 우선.

## 페이지 명명 규칙 (검색 키워드)

- 주차 계산: ISO 8601 (월요일 시작). 표준 검색 형식 `week {WW} {YYYY}`
- 일지/회고: 검색 `week {WW} {YYYY}` → 제목 `[week XX] @YYYY/MM/DD → YYYY/MM/DD 일지` ("식단" 페이지 제외)
- 식단: 검색 `week {WW} {YYYY} 식단` → 제목 `[week XX] @YYYY/MM/DD → YYYY/MM/DD 식단`
