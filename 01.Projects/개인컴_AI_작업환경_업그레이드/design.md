# 개인 컴 멀티 AI CLI 작업 환경 설계 (A안 — 확정)

- 작성일: 2026-07-17
- 상태: 설계 승인 대기 (A안 구두 승인 완료, 문서 검토 대기)
- 관련 레포: para(본 볼트), vibe-ai-config, vibe-dotfiles, ~/.gemini

## 1. 배경과 목표

업무용 컴의 AI 작업 환경(cmux + tmux + vibe 런처 + Claude 하네스)이 개인 컴에 이식 완료된 상태에서, 개인 컴 고유 조건에 맞춰 업그레이드한다.

- 개인 컴은 Claude Code 단독이 아니라 **Gemini CLI를 병행**하고, Codex CLI는 추후 편입한다.
- para 허브에서 작업을 관리하다가 프로젝트 작업이 필요하면 **해당 프로젝트의 AI 도구를 pane 또는 워크스페이스로 열어** 작업한다 (업무 컴과 동일한 허브-위임 모델).

## 2. 확정 결정사항

| 항목 | 결정 |
| --- | --- |
| 구독 플랜 | Claude Pro/Max + Gemini AI Pro/Ultra |
| Codex | **보류** — 자리만 예약, 나중에 `--tool codex`로 편입 |
| 허브 도구 | **Claude Code** (vibe/cmux 위임 인프라·notion-suite·훅이 전부 Claude 기반) |
| Gemini 역할 | **작업 성격별 분업** — 조사·대량 컨텍스트(1M) 분석·문서화·웹 검색 |
| agy(Antigravity) | 보조로 전환 — 브라우저 실검증·IDE형 대량 분석 시 사용 |
| 모니터 | 상황마다 다름(노트북 단독 ⇄ 외장 모니터) — 두 시나리오 모두 대응 |

## 3. 아키텍처 — 허브-위임 모델 + 도구 선택 확장

### 3.1 도구 라우팅 테이블

| 작업 성격 | 도구 | 실행 경로 |
| --- | --- | --- |
| 작업 관리·노션 루틴·위임 지휘 | Claude Code | `vibe main` → para 허브 pane |
| 구현·커밋·코드리뷰·오케스트레이션 | Claude Code | `vibe delegate <프로젝트>` |
| 조사·대량 분석·문서화·웹 검색 | Gemini CLI | `vibe delegate <프로젝트> --tool gemini` (신규) |
| 브라우저 실검증·IDE 작업 | agy (Antigravity) | GUI 직접 실행 (tmux 밖) |
| (예약) 알고리즘·리뷰 세컨드 오피니언 | Codex CLI | `--tool codex` (추후) |

**Single-Writer 원칙 유지**: 하나의 레포에는 동시에 한 도구만 Write. Gemini pane과 Claude pane이 같은 레포를 잡지 않도록 위임 시 허브가 점유 상태(`git status` dirty 여부)를 확인한다.

### 3.2 화면 구성

- **기본 (노트북 단독)**: tmux main-vertical — 좌 50% para 허브(Claude), 우측 스택에 위임 pane(Claude/Gemini 혼재 가능). pane 2개 초과 시 가독성이 떨어지므로 3번째부터는 cmux 탭 또는 워크스페이스로 승격.
- **외장 모니터**: 허브 워크스페이스는 노트북 화면, 장기 작업 프로젝트는 `cmux-proj`로 별도 cmux 워크스페이스를 외장 모니터에 배치.
- **열람**: 변경 확인은 `vibe peek <프로젝트> diff` (cmux diff surface 자동 승격) — 기존 규칙 그대로.
- **에스컬레이션 기준(기존 규칙 준용)**: 장기 체류·강격리 → `cmux-proj` / 멀티 레포 이슈 → `cmux-issue`.

## 4. 구현 항목 (4건)

### 4.1 vibe.sh `--tool` 옵션 추가 — `vibe-ai-config` 레포

- `vibe delegate <프로젝트> [--tool claude|gemini|codex] ["메시지"]` — 기본값 `claude`(기존 동작 100% 보존).
- `--tool gemini`이면 pane에서 `gemini` CLI를 대상 프로젝트 cwd로 실행. 초기 메시지 전달은 gemini CLI 인자 규격에 맞춰 처리(미지원 시 pane에 프롬프트만 준비).
- `--tool codex`는 미설치 시 "codex 미설치 — 보류 상태" 안내 후 종료(자리 예약).
- `VIBE_DELEGATED=1` 마커·pane 타이틀 규칙은 도구 무관 동일 적용. pane 타이틀에 도구명 표기(예: `gemini:legigraph`).
- 검증: `bash -n` + `shellcheck` 통과, `vibe delegate <proj>`(무옵션) 기존 동작 회귀 확인.

### 4.2 cmux-projects.txt 개인화 — `vibe-dotfiles` 레포

- 제거: 업무 전용 3종 (bshop, BillingMPAdmin, PHPLib — 개인 컴에 레포 없음).
- 유지: para(pin), vibe-dotfiles(pin), vibe-ai-config.
- 추가: legigraph, grafana-test (현재 NEXT-SESSION.md 활성 프로젝트 기준). 이후 필요 시 추가 등록.

### 4.3 GitHub PAT 보안 이전 — `~/.gemini/settings.json`

- settings.json의 평문 PAT를 제거하고 환경변수 참조(`$GITHUB_PERSONAL_ACCESS_TOKEN` 등 gemini CLI 지원 문법)로 교체.
- 실제 토큰 값은 `~/.zshrc.local`(git 미추적)에 export. **노출된 기존 토큰은 사용자가 GitHub에서 재발급/폐기** (사용자 액션 필요).

### 4.4 para CLAUDE.md 세션 규칙 갱신 — 본 볼트

- "agy(Antigravity)가 메인 툴" 문구를 본 설계로 교체: **Claude Code = 허브·구현 / Gemini = 조사·대량분석·문서화 / agy = 브라우저 검증 보조 / Codex = 보류(예약)**.
- 도구 라우팅 테이블(§3.1)과 화면 구성 규칙(§3.2) 요약을 반영.
- `NEXT-SESSION.md`에 본 프로젝트 항목 추가.

## 5. 구현 순서·범위·롤백

- 순서: 4.4(볼트, cwd 내부) → 4.2 → 4.1 → 4.3. 4.1이 유일한 코드 변경이며 나머지는 설정·문서.
- 4.1/4.2는 각 레포 규율에 따라 격리 브랜치(worktree)에서 외과수술식으로 수행.
- 롤백: 전부 git 추적 파일(4.3의 토큰 값 제외)이라 revert로 즉시 복구 가능.

## 6. 비범위 (YAGNI)

- Codex 어댑터(`vibe-ai-config/codex/`) 채우기 — 구독 확정 후 별도 작업.
- Gemini용 위임 자동화 훅·서브에이전트 매핑 — pane 수동 위임으로 시작, 필요해지면 추가.
- launchd 자동화 신규 추가 없음 (기존 3종 유지).
