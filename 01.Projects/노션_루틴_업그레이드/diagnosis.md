# 노션 루틴 3종 현황 진단 및 업그레이드 계획

**진단일: 2026-08-02** · 요구사항은 같은 폴더 `requirements.md` 참조.

## 구조 현황

- 스킬 실체: `~/.claude/skills/notion-*` → `~/.agents/skills/` 심볼릭 링크. 정본은 `vibe-ai-config/skills/personal/{calendar,budget,diet}/` — 설치본과 diff 0 (동기화 정상).
- notion-suite 플러그인(1.1.5)은 `/notion` 커맨드·훅·공통 레퍼런스(`notion-common.md`)만 배포. 스킬 본체는 별도 채널(`~/.agents/skills`) — **배포 경로 이원화**.
- 일지 슬롯에 write하는 주체가 3개: `notion-weekly-schedule` / `notion-weekly-routine` / `gws-cal-to-notion`. 각자 슬롯 매핑 사본 보유.

## 핵심 리스크 (H = 데이터 손실 가능)

1. **[H] 슬롯 write 3주체 분산** — 슬롯 매핑이 4곳(스킬 ref 2 + gws + SOP README)에 중복 기술, 이미 모순 발생: 스킬 reference에 주말 시각표 없음 / 종일 이벤트 배치 규칙이 SOP와 정면 충돌(gws "LIFE1 우선" vs SOP "LIFE1 임의 배치 금지").
2. **[H] gws-cal-to-notion 기본 모드 `replace`** — 캘린더 동기화가 수동 입력 슬롯을 덮어씀. 롤백은 스스로 best-effort라 자인.
3. **[H] 슬롯 부분 replace 시 다른 슬롯 삭제** — 경고만 3중 반복, 강제 수단(슬롯 개수 카운트 검증 등) 없음.
4. **[H] 롤백 사실상 불가** — "원본 복원 시도" 규칙은 있으나 fetch 스냅샷 보관 지시가 어디에도 없음.
5. **[M] 깨진 공통 레퍼런스 경로** — `notion-budget`·`notion-diary`의 `../../references/notion-common.md`가 실체·정본 양쪽에서 부재. 실제 파일은 `claude/plugins/notion-suite/references/notion-common.md`. 예산 스킬이 공통 규약(fetch-first·에러 처리·조회/변경 구분)을 런타임에 미로드.
6. **[M] 공통 레퍼런스 참조 비대칭** — `diet`·`weekly-schedule`은 notion-common을 아예 참조 안 함.
7. **[M] 예산 카테고리 자기모순** — SKILL.md 본문 6종 vs rules·reference 7종(의류·생활 유무).
8. **[M] diet → budget 역방향 분기 부재** — "식재료+가격" 이중 분기가 예산 쪽에만 있어 식단 스킬이 먼저 잡히면 지출 기록 누락.
9. **[M] Diet 주간 페이지는 n8n 생성 의존** — 실패 시 폴백 없이 데드엔드 (예산·다이어리는 자동 생성 폴백 있음).
10. **[L] DB ID 4개가 11개 지점에 하드코딩** / 예산 합계 LLM 수동 재계산(검산 없음) / `weekly-schedule` 트리거 빈약 / 일정 도메인만 툴 무관 SOP(`04.일정.md`) 부재 / orphan 플러그인 캐시(notion-suite 1.1.0·1.1.4) 잔존.

## 업그레이드 계획 (3단계)

### Phase 1 — 안정성 (데이터 손실 차단) ✅ 2026-08-02 완료 (vibe-ai-config `8fe8509`, `23b5d0d`)
- [x] 슬롯 편집 절차를 단일 reference로 통합 — `notion-weekly-schedule/references/slot-edit-protocol.md` 신설, 3주체는 인용만
- [x] gws-cal-to-notion 기본 모드 replace → append 전환 (replace는 명시 요청 + 경고 후에만)
- [x] 슬롯 편집 전 슬롯 라인 개수(6줄) 자가검증 — 불일치 시 update 중단
- [x] 편집 전 fetch 스냅샷 보관 → 검증 실패 시 결정적 복원 (프로토콜 + notion-common 양쪽)
- [x] notion-common.md 깨진 경로 수정(budget·diary) + diet/weekly-schedule 참조 신설
- 부수: notion-suite 플러그인 1.1.5→1.1.6 bump. 스킬 6개 재배포, 배포본↔정본 diff 0 검증.
- 후속 메모: pre-commit 자동 bump 훅 미발동 원인 미조사 → 별도 점검 필요.
- 주말 슬롯 시각표는 slot-edit-protocol.md에 포함됨 → Phase 2의 "주말 시각표 반영" 항목 해소.

### Phase 2 — 정합성
- [ ] 예산 카테고리 6/7종 모순 해소
- [x] 주말 슬롯 시각표를 weekly-schedule reference에 반영 (Phase 1 slot-edit-protocol.md로 해소)
- [ ] diet → budget 역방향 분기 추가
- [ ] DB ID를 단일 파일로 추출, 11개 지점 참조 일원화

### Phase 3 — 기능·가용성 (+요구사항 반영)

> **설계 원칙(requirements §0)**: 도메인 규칙과 노션 접근(어댑터)을 분리해, 향후 노션 없이도 동작 가능한 구조로 설계한다. 필요 시 스킬 명명·구조 재편도 이 단계에서 결정.

- [ ] gws CLI → Google Calendar MCP 전환 (requirements R1)
- [ ] 예정/완료 상태 구분 표기 규칙 신설 (requirements R5)
- [ ] 일요일 KPT 회고 자동 실행 루틴 (requirements R6)
- [ ] Wish list 등록 구조 설계·구현 (requirements B1)
- [ ] 뱅크샐러드 내보내기 파일 → 지출 일괄 기록 파이프라인 + 중복 방지 (requirements B2)
- [ ] 지출 ↔ wish list 매핑/대체 규칙 (requirements B3)
- [ ] 월말 지출 정리·요약 루틴 (requirements B4)
- [ ] 보유 식재료 이월·재고 관리 규칙 명확화 (requirements D1)
- [ ] 요일×끼니(점심/저녁) 실적·예정 기록 구조 (requirements D2)
- [ ] Diet 페이지 부재 시 폴백 생성 절차
- [ ] `02.Areas/07.개인관리/04.일정.md` SOP 신설
- [ ] weekly-schedule 트리거 보강 · 예산 합계 검산 규칙
- [ ] orphan 플러그인 캐시(1.1.0/1.1.4) 정리

작업 대상: vibe-ai-config 정본 + 이 볼트 SOP 문서. 스킬 수정 → skills.sh 배포 → SOP 동기화가 한 사이클.
