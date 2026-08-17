# 🗄️ TASKS.md + dashboard.html — 아카이브 (2026-08-17)

GTD 스타일 태스크 목록(`TASKS.md`)과 그것을 읽어 렌더링하던 생산성 대시보드(`dashboard.html`)다. **더 이상 사용하지 않는다.**

## 아카이브 사유

- **`TASKS.md` 는 2026-05-19 이후 갱신 정지.** 이후 신설된 프로젝트(개인컴 AI 작업환경 업그레이드·노션 루틴 업그레이드·Election-2026-Local-Archive)가 한 건도 반영되지 않았고, 반대로 2026-08-17 아카이브한 항목들이 `Active`·`Someday` 로 남아 있었다.
- **`dashboard.html` 은 2026-02-13 이후 미변경**이며 `TASKS.md` 에 종속돼 있어 함께 정지 상태였다.
- 실사용 SoT 가 `NEXT-SESSION.md` + `01.Projects/` + 노션 Projects DB 로 옮겨가면서 **3중 관리**가 됐고, 갱신되지 않는 쪽이 오히려 잘못된 현황을 보여주는 상태였다.

## 현행 대체

| 용도 | 현행 |
|---|---|
| 세션 간 인수인계·우선순위 | `NEXT-SESSION.md` (실사용 SoT) |
| 프로젝트별 상세·진행내역 | `01.Projects/<프로젝트명>/` |
| 프로젝트 상태 인덱스 | 노션 `Projects` DB — 규칙 정본 `02.Areas/07.개인관리/05.프로젝트.md` |
| 작업 로그 | `.claude/work-log/YYYY-MM-DD.md` |

## 되살리려면

`dashboard.html` 은 브라우저에서 열어 `TASKS.md` 를 직접 선택하는 방식(File System Access API)이라 이 폴더 안에서도 그대로 동작한다. 다만 되살릴 경우 **노션 Projects DB 와 이중 관리가 되는 문제부터 해결할 것** — 그게 이번에 정지한 근본 원인이다.

관련 스킬 `task-management`(`02.Areas/Claude-Skills/task-management/`)도 이 워크플로를 전제로 하며 현재 배포되어 있지 않다.
