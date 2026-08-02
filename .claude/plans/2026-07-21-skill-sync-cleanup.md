# 스킬 동기화 체계 정리 계획 (Claude Code ⇄ agy 합의안)

> 작성: 2026-07-21, Claude Code (para 허브 세션)
> 합의: agy 협의 완료 — 안A 채택 ([AGY-REPLY-DONE] 응답 기준)
> 실행 분담: 단계 ①·② = agy / 단계 ③·④ = Claude Code

## 배경

- 2026-07-21 21:27~21:31 `sync-skills-to-agents` 실행으로 `~/.claude/skills`에 심링크 약 100개가 일괄 생성됨 (`~/.agents/skills/*` 대상).
- 문제 1 — **이중 등록**: swkim0128 마켓플레이스 플러그인(task-mgmt·git-suite·notion-suite·tmux-suite·harness·analyze·vibe-admin·test 등)에 이미 존재하는 스킬들이 `~/.claude/skills` 심링크로도 로드되어 Claude Code에서 트리거 중복·비결정적 라우팅 발생.
- 문제 2 — **유령 스킬 부활**: Claude Code가 오늘 플러그인에서 폐기한 스킬 8종(cancel·hud·debug·trace·plan·ralplan·skill-router·vibe-session)이 구버전 캐시 기준 사본으로 `~/.agents/skills`에 남아 재노출됨.
- 폐기 반영 완료된 최신 플러그인 버전: harness 3.2.8 / analyze 2.2.20 / test 1.1.1 / tmux-suite 1.0.38 / task-mgmt 1.3.11 / vibe-admin 2.1.4 (GitHub push + 로컬 업데이트 완료).

## 합의 원칙 (안A)

1. **정본(SoT) = vibe-ai-config 마켓플레이스 플러그인 소스.**
2. `~/.agents/skills` = agy/Codex/Gemini/Cursor용 **단방향 사본** (skills.sh 규격).
3. `~/.claude/skills` 에는 **플러그인과 중복되는 스킬의 심링크를 생성하지 않는다** (Claude Code는 플러그인에서 직접 로드).

## 실행 단계

### ① [agy] `sync-skills-to-agents.sh` 수정 — `~/Project/vibe-dotfiles/vibe-tools/sync-skills-to-agents.sh`

- **(a) Claude 중복 제외**: `~/.claude/skills` 심링크 생성 시, swkim0128 마켓플레이스 플러그인에 존재하는 스킬명은 제외한다. 제외 목록은 하드코딩하지 말고 실행 시 동적으로 수집:
  `~/.claude/plugins/marketplaces/swkim0128/claude-config/plugins/*/skills/*/` 디렉터리명 집합.
- **(b) 동기화 원본 최신화**: `~/.claude/plugins/cache/swkim0128/<plugin>/<구버전>/` 이 아니라 버전 무관 경로 `~/.claude/plugins/marketplaces/swkim0128/claude-config/plugins/<plugin>/skills/` 를 소스로 사용 (marketplace update 시 항상 최신 유지, 버전 디렉터리 스테일 문제 원천 차단).
- **(c) 고아 정리(prune)**: 정본에서 삭제된 스킬이 `~/.agents/skills` 와 `~/.claude/skills` 에 남지 않도록, 동기화 시 소스에 없는 항목 제거 로직 추가. 단 플러그인 유래가 아닌 고유 스킬(learned, local, para-work, daily-briefing, mail-compose, meeting-setup, nworks-setup, skill-creator, skill-backup, vercel-*, web-design-guidelines, writing-guidelines, find-skills, deploy-to-vercel, notion-project-creator, tmux-session-manager, update-vibe-commands, worktree-agent, legacy-php-euckr-edit, para-task-review 등)은 prune 대상에서 보호한다 — 보호 방식은 매니페스트(동기화 시 기록한 파일 목록) 기반 권장.
- 검증: `bash -n` + `shellcheck` 통과 후 vibe-dotfiles에 커밋.

### ② [agy] 재동기화 실행 + 확인

- 수정된 스크립트로 `sync-skills-to-agents` 1회 실행.
- 확인 항목:
  - `~/.agents/skills` 에서 폐기 스킬 8종(cancel·hud·debug·trace·plan·ralplan·skill-router·vibe-session) 사본이 제거됐는가.
  - `~/.agents/skills/document-latest`, `post-merge`, `php-code-review` 등이 오늘 수정된 최신 내용(Outline 툴명 `mcp__plugin_vibe-admin_outline__*`, plane CLI 방식)으로 갱신됐는가.
  - `~/.claude/skills` 에 플러그인 중복 심링크가 재생성되지 않는가.

### ③ [Claude Code] `~/.claude/skills` 중복 심링크 제거

- ①·② 완료 확인 후 실행. 플러그인에 존재하는 스킬명과 일치하는 심링크 전량 제거 (①(a)와 동일한 동적 목록 기준) + para-task-review 심링크 제거(플러그인 task-review와 트리거 중복, `~/.agents/skills` 원본은 유지).
- 비플러그인 고유 스킬 심링크·일반 파일(README.md, backup-guide.md)은 유지.

### ④ [Claude Code] 검증

- Claude Code 세션 재시작 → 스킬 목록에서 접두사 없는 중복(cancel·debug·hud·plan 등) 소멸 확인.
- `plugin:skill` 접두사 스킬 정상 로드 확인.

## 사고 기록 (2026-07-22 단계 ② 부작용)

- 21:27에 `~/.claude/skills` → `~/.agents/skills` 로 이동됐던 **개인 스킬 9종이 prune 로직에 의해 삭제**됨 (마켓플레이스 소스에 없고 보호 목록에도 없었기 때문).
- Claude 복구 조치: para 백업(`02.Areas/Claude-Skills/`)에서 3종 복원(`skill-backup`, `update-vibe-commands`, `notion-project-creator` → `~/.claude/skills` 실디렉터리), `skill-creator`는 공식 플러그인으로 대체(복원 생략), 깨진 심링크 9개 제거.
- **영구 손실 5종**: `learned`(OMC 학습 스킬 저장소 — 내용물 유무 불명), `legacy-php-euckr-edit`, `para-task-review`, `tmux-session-manager`, `worktree-agent` — 뒤 4종은 플러그인 스킬(analyze:file-encoding-converter+인코딩 훅, task-mgmt:task-review, tmux-suite:tmux-session-start/done, worktree 계열)이 기능 커버.
- **재발 방지 요구(→ agy)**: sync 스크립트 prune 은 "스크립트 자신이 동기화한 항목"만 대상으로 하도록 매니페스트 기반으로 제한할 것. 이동(move)한 개인 스킬은 매니페스트에 보호 항목으로 기록.

## ⑤ [agy] skills.sh 공용 배포 채널 구성 (2026-07-22 사용자 확정 방향)

목적: 개인 컴·업무 컴 어디서든 `skills` CLI(Vercel skills.sh)로 스킬을 설치할 수 있게 vibe-ai-config 를 공용 스킬 저장소로 노출.

- **(a) 집계 디렉터리**: skills CLI 는 표준 위치(레포 루트 `skills/`, 컨테이너 최대 2단계 깊이)만 스캔하므로, `claude-config/plugins/*/skills/*` 를 레포 최상위 `skills/<skill-name>/` 로 평탄화 복사하는 집계 스크립트를 작성·실행하고 결과물을 커밋. (기존 빈 `shared/skills/` 대신 skills CLI 표준인 최상위 `skills/` 권장. 이름 충돌 시 플러그인 접두사로 해소.)
- **(b) 플러그인 업데이트 루틴에 연결**: 플러그인 스킬 수정 → 집계 스크립트 재실행 → 커밋/푸시가 한 흐름이 되도록 (auto-version-bump 훅 또는 별도 훅에 연결 검토).
- **(c) 설치 표준 명령 문서화**:
  - 타 CLI(agy/Codex/Gemini/Cursor)용: `npx skills add swkim0128/vibe-ai-config -g -a <agent>...`
  - **Claude Code 는 대상에서 제외** (`-a claude-code` 금지) — Claude 는 마켓플레이스 플러그인으로 직접 로드하므로 중복 방지.
  - 업무 컴도 동일 명령으로 설치 (마켓플레이스 + skills CLI 병행, Claude 제외 규칙 동일).
- **(d) 기존 `sync-skills-to-agents.sh` 위상**: skills CLI 정착 후 로컬 즉시 반영용 보조 도구로 유지하거나 `npx skills update` 로 대체 — agy 판단.

## 이후 운영 루틴 (skills.sh 채널 반영)

플러그인 스킬 수정 → 집계 스크립트 → vibe-ai-config 커밋/푸시 → Claude: `claude plugin marketplace update` + `claude plugin update` / 타 CLI: `npx skills update` (또는 sync-skills-to-agents).

## 완료 기준

- [x] ① 스크립트 수정 + 정적 검증 + 커밋 (agy, vibe-dotfiles 5ad3740)
- [x] ② 재동기화 + 3개 확인 항목 통과 (agy) — 단 prune 사고 발생, 위 사고 기록 참조
- [x] ③ 중복 심링크 제거 + 백업 복원 (Claude, 2026-07-22)
- [x] ④ Claude 세션 재시작 검증 (Claude, 2026-07-22 — 설치본 harness 3.2.8에 폐기 스킬 8종 부재·Outline 툴명 정합·~/.claude/skills 중복 0건 확인)
- [x] ⑤ skills.sh 공용 배포 채널 구성 (agy, vibe-ai-config c54f8a8 — skills/ 71종 집계 + scripts/aggregate-skills.sh, Claude가 검증 후 push 완료 2026-07-22)
- [x] ⑥ prune 매니페스트 보호 패치 (agy, vibe-dotfiles 3108e91 — ~/.agents/skills/.marketplace-manifest.txt 기반 안전 prune, Claude 검증 완료)
