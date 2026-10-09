# 웹 리서치 자동화 엔진

- **노션**: [PRO-132](https://app.notion.com/p/3e0a25196d348147bac3fb522e522232)
- **상태**: Done (2026-10-09 완료 처리 — 사용자 지시)
- **기간**: 2026-09-19 ~ 2026-10-09
- **우선순위**: 중간
- **코드 레포**: `~/Project/web-research-engine` (브랜치 `PRO-132`, 커밋 `196d79c`, **리모트 없음**)

## 완료 정리 (2026-10-09)

**결론**: 동작 방향이 정해졌으므로 프로젝트를 닫는다. 처음 계획한 「raw CDP 캡처 → HTTP 승격 → 스케줄 반복」(B축)이 아니라, **로그인된 Aside 브라우저로 사용자 요청 시 1회 실행**(A축)하는 방향으로 정리됐다. 유스케이스 3개 중 2개가 반복 실행 대상이 아니었기 때문이다.

### 만든 것

| 산출물 | 위치 | 상태 |
|---|---|---|
| action recipe 포맷 v0.3 | `web-research-engine/docs/recipe-format.md` | 확정 — 모든 필드가 실측된 실패 하나에 대응 |
| 3사이트 recipe (스마트스토어·오늘의집·쿠팡) | `web-research-engine/recipes/` | 확정, 3사이트 모두 찜 → 목록 검증 → 원복 완주 이력 |
| A축 실행기 (계획 / `--execute` / `--revert-after-verify`) + YAML→JSON 빌드 | `web-research-engine/src/run-recipe.mjs` · `scripts/build-recipes.rb` | 테스트 8/8 통과 (2026-10-09 재실행) |
| **쿠팡 주문내역 → 구입 품목 추출 (읽기)** | `vibe-ai-config/shared/scripts/aside-suite/shop-orders.sh` | 2026-10-09 완료·push(`14f3e6a`), 시나리오 7종 검증 — [[쿠팡-식재료-수집-20261009]] |

### 정해진 방향 (재개 시 출발점)

- **로그인이 필요한 사이트 작업은 Aside 브라우저로 한다.** raw CDP 직접 구현은 불필요 — 무인 스케줄 실행(B축)에서만 의미가 있다.
- **한 작업은 `aside repl` 한 번의 호출 안에서 끝낸다**(호출마다 새 세션, 연 탭도 닫힘).
- **읽기 도구는 `vibe-ai-config` aside-suite 스크립트**로 만든다(양 머신 배포). 쓰기(찜·장바구니)는 `web-research-engine` recipe 실행기.
- **안전 규칙 5개는 그대로 유지**: 상태 모르는 토글 실행 금지 · revert 없는 액션 제외 · 로그인 추측 금지 · 정상 이용 범위만 · 성공 판정은 상태 재조회.

### 하지 않은 것 (필요해지면 새 프로젝트로)

- **B축 전체 미착수** — raw CDP 캡처·리플레이, HTTP 승격, launchd 스케줄, Research Archive(SQLite FTS). 반복 조사 수요가 생기면 노션 PRO-132 본문 「MVP 범위 (B축)」 Phase 1~5 가 계획이다.
- 스마트스토어·오늘의집 **통합 실행기 재검증** — 네이버는 Aside 위치 지정자와 접근성 스냅샷의 이름 불일치로 클릭 전 차단, 오늘의집은 당시 로그아웃 상태로 차단(recipe 계약 테스트는 통과).
- `notion-budget` 위시 등록과의 연결 지점.
- `shop-orders.sh` 스마트스토어 추가 · 비로그인 시 종료코드 2 실측.

### 남은 정리 (사용자 판단)

- `~/Project/web-research-engine` — 리모트 미설정. 보존하려면 원격 저장소 생성·push 가 필요하다.
- `~/.cache/web-research-engine` (약 149MB) — 초기에 만든 Chrome 디버그 프로필. Aside 채택으로 불필요. 삭제는 사용자 확인 후.
