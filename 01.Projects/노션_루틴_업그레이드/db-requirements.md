# 노션 DB 구성 업데이트 — 요구사항 (Diet · Ingredients · 예산)

**작성일: 2026-08-06** · 작성 경위: 업무컴에서 작성한 요구사항이 접근 가능한 경로(볼트 git·vibe-ai-config·노션·Plane)에 없어 **개인컴에서 재작성**. 근거: `design.md`(D1·D2·B1~B4) + 노션 실스키마 조사(아래 §1).

## 1. 현재 실태 조사 결과 (2026-08-06 기준)

### 예산 — 도메인 문서와 실체 전면 불일치 (핵심 발견)

실제 노션 예산은 이미 2-DB 체계로 운영 중이다. `03.예산.md`의 "동적 검색 + 페이지 마크다운 표 + 카테고리 7종"은 실체와 다르다.

| DB | ID | 실체 |
|---|---|---|
| 🏦 Household Ledger (월 페이지) | `collection://17f03db9-14ee-4379-bd14-f47194444f87` | 제목 `YYYY년 MM월 지출`(예: HL-36 = 2026년 05월). 속성: Date·Year·BasicLedgerPrice(기본예산)·ExtraLedgerPrice(예산외)·DepositPrice/ExtraDepositPrice(입금)·SavingAmount(저축)·FixedExpenses/VariableExpenses/OutOfBudgetExpenses(→Ledger relation)·합계 rollup·수식(AllLedgerPrice/AllExpenditurePrice/AllLeftAmount/LeftExpenditure)·auto ID(HL-) |
| 🧺 Ledger (지출 트랜잭션) | `collection://7391b842-ef1c-42c5-a7ca-d82068dbaccd` | 속성: Name(품목)·가격(won)·지출일(date)·카테고리(select **12종**)·세부 카테고리(multi_select 48종)·정기 지출일(select)·실행(status 6단계: 아직여유→실행고민→실행예정→실행완료→지출완료/실행취소)·Place·URL·할당 버튼 2종(변동/예산외). 카테고리별 페이지 템플릿 11종 |

- **카테고리 실체 12종**: 식비·교통·문화여가·의료건강·주거통신·의복미용·생활용품·교육학습·여행숙박·금융·경조선물·기타비용 — 도메인 문서의 "7종 확정"과 충돌. **실체(12종)를 정본으로 채택**하고 문서를 후속 갱신한다.
- Wish list 역할은 별도 표가 아니라 **Ledger의 실행 status 라이프사이클**(아직여유/실행고민/실행예정 = 후보, 지출완료 = 확정) + 월 페이지 "지출 후보 / 다음 달 지출 후보" 섹션이 수행 중.

### Ingredients / Diet

- Ingredients: Name·Tag(multi_select 11종)·Price(won)·URL·생성일시·Diet relation·Latest Date rollup. **재고 상태 속성 없음** → D1(재고 SoT = 마스터 '보유 중')을 담을 스키마 부재.
- Diet: Ingredients relation 설명이 "현재 가지고 있는 식재료" — 구 규칙(주간 페이지 = 재고) 기준. SoT 이전 후에는 파생 뷰.

## 2. 스키마 변경 요구사항

| # | DB | 변경 | 근거 |
|---|---|---|---|
| S1 | Ingredients | `보유 중` CHECKBOX 추가 — 재고 SoT. 구매→체크, 소진→해제 | design D1 |
| S2 | Ingredients | S1 직후 **백필**: 이번 주 Diet 페이지의 Ingredients relation 항목을 `보유 중`=true 로 이관 | D1 이월 규칙 |
| S3 | Ledger | `가맹점` RICH_TEXT 추가 — 뱅크샐러드 중복 방지 키(지출일+가격+가맹점)의 가맹점 축. Name(품목)과 분리 | design B2 |
| S4 | Ledger | `출처` SELECT(대화·뱅크샐러드·정기·기타) 추가 — import 식별·재업로드 안전 | design B2 |
| S5 | ids.md | Household Ledger·Ledger ID 등록, "예산 고정 ID 없음(동적 검색)" 기술 정정 | §1 발견 |

- Diet relation 설명 갱신("파생 뷰(참조용)")은 MCP DDL로 안전 변경이 어려워 **보류** — 노션 UI 수작업 항목으로 기록.
- Household Ledger 자체는 변경 없음 (수식·rollup 체계 완성도 높음 — 외과수술 원칙).

## 2-b. 예산 3-DB 체계 (2026-08-06 사용자 요구 확정 — 업무컴 작성분 구두 재전달)

> 요구: ① 메인 예산 DB ② 뱅크샐러드 가계부를 그대로 기록하는 DB ③ 원하는 품목(위시리스트) DB.
> 매핑: 메인 예산 ← 각 월 거래내역 합산(가계부 금액 계산) / 거래내역 물품 ↔ 위시리스트(해당 상품 = 이 거래 매핑).

| 역할 | DB | ID | 구성 |
|---|---|---|---|
| 메인 예산 | 🏦 Household Ledger (기존) | `collection://17f03db9-...` | `거래내역` relation(신설) + `가계부금액` rollup(sum, 신설)로 월별 가계부 금액 자동 계산 |
| 가계부 원본 | 💳 거래내역 (**신설**) | `collection://f6f2513b-0caa-4fb2-b831-ccc5ea8a04d5` | Name(내용/가맹점)·거래일·금액(won)·타입(지출/수입/이체)·대분류·소분류·결제수단·메모·`월 예산` relation(dual)·`위시리스트` relation(dual←Ledger). 중복 방지 키 = 거래일+금액+Name |
| 위시리스트 | 🧺 Ledger (**기존** — 2026-08-06 사용자 정정) | `collection://7391b842-...` | 실행 status 라이프사이클(아직여유/실행고민/실행예정→실행완료/지출완료/실행취소)이 wish 후보→구매 확정을 담당. `매핑 거래` relation(dual→거래내역, 신설)으로 "해당 상품 = 이 거래" 연결 |

- 채택 가정: ① B1의 "월 페이지 내 섹션" 결정은 본 요구(DB 기반)로 **대체** ② 거래내역 DB는 뱅크샐러드 원본 전용, 수동 기록·정기 지출은 기존 Ledger 플로우 지속.
- **이체 기록 방침(2026-08-07 확정)**: 뱅샐 원본의 **이체 거래도 그대로 기록**한다(원본 충실성 우선). 타입 `이체`는 지출·수입·고정·예산외 어느 행 수식에도 잡히지 않아 월 예산 집계에는 영향이 없다.
- **정정 이력(2026-08-06)**: 최초에 별도 🛒 Wish List DB(`collection://55704520-...`)를 신설했으나 사용자 정정("위시리스트 디비 = Ledger DB")에 따라 **휴지통 이동**, 매핑은 Ledger `매핑 거래`로 재구성. 같은 이유로 Ledger에 추가했던 `가맹점`·`출처`도 제거(원본 정보는 거래내역 DB 소관).

## 3. 후속 (본 문서 범위 밖, 다음 단계)

1. `03.예산.md` 전면 재작성 — 2-DB 체계·카테고리 12종·실행 status 라이프사이클 기준으로 (7종 표기·마크다운 표 절차 폐기).
2. `02.식단.md` — '보유 중' 속성명 확정 반영 (규칙은 이미 SoT 기준으로 작성돼 있음).
3. vibe-ai-config `notion-budget`·`notion-diet-manager` 스킬을 실스키마 기준으로 갱신 (pane %14 위임분 검증과 병합).

## 적용 이력

- [x] S1 보유 중 추가 (2026-08-06 적용, checkbox 확인)
- [x] S2 백필 — **대상 0건으로 종료**: 이번 주(week 32) relation 유일 항목이 n8n 템플릿 placeholder `_`(38개 주간 페이지에 연결된 더미)로 확인됨. 직전 주(week 31) 식단 페이지는 미생성. 실재고는 사용자 입력 시 체크.
- [x] ~~S3 가맹점 추가~~ → **롤백**(가계부 원본은 거래내역 DB 소관으로 정리)
- [x] ~~S4 출처 추가~~ → **롤백**(동상)
- [x] S5 ids.md 갱신 (Household Ledger·Ledger 등록, 예산 동적 검색 기술 폐기 정정)
- [x] S6 💳 거래내역 DB 신설 + 월 예산 relation (2026-08-06)
- [x] ~~S7 🛒 Wish List DB 신설~~ → **폐기(휴지통)** — 위시리스트 = 기존 Ledger로 정정
- [x] S8 Household Ledger `가계부금액` rollup 신설 (2026-08-06)
- [x] S9 Ledger `매핑 거래` relation 신설 (dual → 거래내역 `위시리스트`) (2026-08-06)
- [x] S10 Household Ledger ↔ Ledger 관계 절단 (2026-08-06 사용자 지시) — relation 3종(FixedExpenses/VariableExpenses/OutOfBudgetExpenses) + 종속 rollup 3종(FixedExpenditure/VariableExpenditure/ExcludingExpenditure) 제거. 기존 월 페이지(2024~2026)의 지출 매핑 링크는 소실(노션 UI의 삭제 속성 복구로 되돌리기 가능).
- [x] S11 거래내역 `예산외` CHECKBOX + 행 수식 3종(`지출액`=지출∧¬예산외, `예산외지출액`=지출∧예산외, `수입액`=수입) 신설 (2026-08-06)
- [x] S12 Household Ledger 금액 rollup 3종 신설: `지출금액`·`예산외지출금액`·`수입금액` = 거래내역 행 수식 sum. 임시 `가계부금액` rollup은 대체 후 제거 (2026-08-06)
  - 구현 노트: MCP 수식 파서가 relation 순회(`prop("거래내역").filter(...)`)를 지원하지 않아 **행 수식 + rollup(sum)** 2단 구성으로 우회.
- [x] S13 거래내역 relation 정리 — 폐기된 Wish List DB를 가리키던 죽은 `위시리스트` relation 삭제, Ledger 쪽 relation을 `위시리스트`로 개명 (2026-08-06)
- [x] ~~잔여: HL 구 수식 깨짐~~ → S15에서 해소.
- [x] S14 **7월 거래 import** (2026-08-06): 뱅크샐러드 xlsx(Gmail 첨부, 드롭 폴더 경유) → 거래내역 DB 122건(지출 117 −1,972,073 / 수입 5 +2,848,107), 이체 제외, 월 예산(2026년 7월 지출) relation 매핑. 원본 합계와 일치 검증.
- [x] S16 **전월 일괄 import — 업무컴 수행분** (2026-08-07 금, 개인컴에서 2026-08-09 확인): 거래내역 DB 총 **1,911건**. **이체 포함 방침으로 확정**(사용자 판단 — 개인컴 7월 import 때의 "이체 제외"를 대체). 6월분 이미 완료(지출 102 −2,137,542 / 수입 7 +2,853,048 / 이체 69)라 개인컴 6월 import는 **실행 전 취소**(중복 방지). 7월 지출 117건 −1,972,073은 S14 결과 그대로 유지되고 이체 60건만 추가됨 — 중복 없음(전수 중복 검사: 동일 날짜·금액·내용 3건뿐, 원본 실거래로 판단).
  - **미해소 차이 1건**: 6월 지출이 개인컴 8/2 export 기준 103건 −2,150,702 vs 노션 102건 −2,137,542 → **1건 13,160원 누락 가능**. 업무컴이 더 최신 export를 썼다면 정상. 필요 시 해당 건 특정 후 보완.
- [x] S15 **이전 표시 값 복원** (2026-08-06): 거래내역에 `고정` checkbox + 행 수식 4분류(변동지출액·고정지출액·예산외지출액·수입액, 뱅샐 부호 규약: 지출액=−금액, 환불 자동 차감) → HL rollup 4종(**수입금·변동지출·고정지출·예산외지출**) + `총지출` 수식. 깨졌던 구 수식 3종 재정의: AllExpenditurePrice=변동+고정+예산외, AllLeftAmount=Basic+Extra−총지출, LeftExpenditure=Basic−변동−고정(의미 재구성 — 원 수식 코드는 미확인, 채택 가정). 7월 고정지출 12건 백필(소분류 월세·통신비·관리비·보험·서비스구독 + 정기 기부 2건) — 변동 105건 128.0만 / 고정 12건 69.2만.
