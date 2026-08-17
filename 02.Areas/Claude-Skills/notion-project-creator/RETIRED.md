# ⛔ 폐기됨 — notion-project-creator (2026-08-17)

이 폴더의 `SKILL.md` 는 **더 이상 사용하지 않는 스킬의 이력 보존본**이다. 설치하지 말 것.

## 폐기 사유 (2026-08-17 실측)

1. **타깃 DB 가 존재하지 않는다.** 스킬이 가리키는 Projects data source `2a9a2519-6d34-810a-8745-000bde866d55` 를 `notion-fetch` 로 조회하면 **404 object_not_found**. 상태값 체계(`Idea`/`0. Not started`/`1. In progress`/`2. On hold`/`3. Done`)와 필드 구성(`Archive` checkbox, `Areas`/`Resources`/`Library`/`Notes` relation)도 현행 DB와 전혀 다르다.
2. **기능이 중복된다.** 프로젝트 생성 + 태스크 동시 추가는 `notion-project-manager` 의 「프로젝트 생성」·「태스크 추가」 흐름이 이미 담당한다.
3. **고아 상태였다.** universal 정본(`~/.agents/skills`)에 배포된 적이 없고 `~/.claude/skills/` 에만 실디렉터리로 존재해 Claude 에서만 보였다 — 스킬 배포 아키텍처 위반.

## 현행 대체

| 대상 | 현행 |
|---|---|
| 스킬 | `notion-project-manager` (정본: `vibe-ai-config/skills/personal/project/`) |
| 도메인 규칙 정본 | `02.Areas/07.개인관리/05.프로젝트.md` |
| DB ID 정본 | `02.Areas/07.개인관리/adapters/notion/ids.md` — Projects `96403fef…` |
