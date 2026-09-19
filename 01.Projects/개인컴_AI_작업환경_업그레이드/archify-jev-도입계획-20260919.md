# Archify · Jev 도입 계획 — 2026-09-19

> **이 문서는 계획이다. 아직 아무것도 설치하지 않았다.** 각 단계는 `[작업] → verify: [정적 도구 단일 명령]` 으로 닫는다.
> 조사 근거는 전부 이번 세션 실측 또는 1차 출처(저장소 파일·공식 문서). 2차 블로그 주장은 별도 표기했다.
> 선행: [[shared-배치-개선계획-20260913]](배포 파이프라인) · 오늘 [[.claude/work-log/2026-09-19]](Instapaper MCP — Keychain+install.sh 규약을 여기서 재사용한다)

## 0. 두 기술의 성격 — 서로 무관하다

| | Archify | Jev |
|---|---|---|
| 하는 일 | 구조화된 JSON → **검증된 다이어그램 HTML** | 텍스트 → **타입 있는 판단값**(선택·점수·불리언) |
| 분류 | 로컬 Node 스킬 (렌더러+검증기) | 외부 API (모델) |
| 우리 쪽 위치 | 에이전트의 **출력 형식** | 에이전트의 **판단 일부 외주** |
| 비용 | 0 | 입력 $0.042/M · 출력 0 |
| 업무컴 제약 | 없음 (완전 로컬) | **회사 데이터 외부 전송 — 정책 게이트 필요** |

같이 도입하지만 **의존관계가 없으므로 병렬 진행**한다. Archify 가 먼저 끝난다.

---

## 1. Archify — 조사 결과

### 1-A. 실체

- 저장소 `github.com/tt-a1i/archify` · **MIT** · ★66.8k · 최종 푸시 2026-09-18
- 스킬 실체는 레포 루트가 아니라 **`archify/` 하위**: `SKILL.md`(16KB) · `bin/` · `schemas/` · `renderers/` · `examples/` · `references/` · `recipes/`
- **런타임 의존성 0** — `package.json` 의 `ajv`·`parse5`·`saxes`·`simple-icons` 는 전부 `devDependencies`(생성·테스트용). 실행은 **순정 Node ≥18** 로 충분 (이 맥 v26.8.1 ✅)
- 기본 브랜치 `main` = **`2.17.0-dev.1` 개발판** / 최신 안정 태그 = **`v2.16.0` (2026-08-30)**

### 1-B. 에이전트 사용 흐름 (SKILL.md 원문 기준)

1. 타입 선택 — `architecture` · `workflow` · `sequence` · `dataflow` · `lifecycle`
   모호하면 `node bin/archify.mjs guide "<시나리오>" --json`
2. `schemas/` 와 `examples/` 에서 **해당 타입 1개씩만** 읽는다 (렌더러 소스·테스트는 읽지 말 것 — SKILL.md 명시)
3. 후보 JSON 작성 — 주 경로 1개, 노드 12개 이하, `meta.quality_profile: "showcase"`
4. **검증**
   ```bash
   node bin/archify.mjs validate <type> <candidate.json> --quality showcase --json
   ```
   ⚠️ 영수증에 **artifact 체크 9개 전부 + composition error 0 + warning 0** 이어야 showcase 합격. 4개만 나오면 basic 검증이라 합격이 아니다.
5. **납품** (최종 수락 명령, 1회만)
   ```bash
   node bin/archify.mjs deliver <type> <candidate.json> <output.html> --quality showcase --json
   ```
   사양 바이트를 동결·스냅샷 후 원자적 커밋, 사양·산출물 각각 SHA-256 + 바이트수 영수증. **비정상 종료를 성공이라 쓸 수 없다.**
6. **브라우저 증거** (선택)
   ```bash
   node bin/archify.mjs visual-check <output.html> --json
   ```
7. 미리보기(선택) `node bin/archify.mjs preview <type> <in>.json <out>.html --quality showcase [--open]`

### 1-C. 네트워크·외부 의존 — 실측

| 항목 | 사실 | 근거 |
|---|---|---|
| 업데이트 확인 | `scripts/check-update.mjs` 가 `https://tt-a1i.github.io/archify/skill-updates/archify/stable.json` 조회 | `skill-release.json` |
| 차단 | **`ARCHIFY_UPDATE_CHECK_DISABLED=1` → 즉시 silent** | `check-update.mjs:1637` 원문 확인 |
| 브라우저 | `visual-check` 가 **로컬 설치 Chrome/Chromium 을 CDP(파이프)로 직접 구동**. 번들·다운로드 없음. 경로 지정 `ARCHIFY_CHROME` | `bin/visual-check.mjs:107-130` |
| 코드 업로드 | **없음** — 분석은 에이전트가 로컬에서 한다 | SKILL.md |

### 1-D. 한계 — 사용 규약에 반드시 반영할 것

**Archify 의 검증은 "그림이 제대로 그려졌나"이지 "내용이 사실인가"가 아니다.**
9개 체크는 스키마·레이아웃·경로 겹침·라벨 가림 같은 렌더링 정합성이다. **코드에 없는 의존성을 그려도 통과한다.** 소개 글들이 "없는 의존성을 그리지 않도록 검증한다"고 쓴 것은 과장이다.
→ 그래서 §3 Phase A-3 **엣지 대조 게이트**를 넣는다. 이 게이트를 통과하지 못하면 도입하지 않는다.

---

## 2. Jev — 조사 결과

### 2-A. 실체 (전부 1차 출처 확인)

- TypeSafe AI · 2026-09-15 공개 · $40M(DCVC 리드) · 창업자 Diogo Almeida(전 OpenAI, RLHF·InstructGPT 연구)
- **SDK 실재 확인**
  - PyPI `typesafe-sdk` **0.7.0** (2026-09-18, Python ≥3.10)
  - npm `@typesafe-ai/sdk` **0.6.0** (Node 20+)
- 모델 id: `jev-latest` → **`jev-1.13.0`** (`jev-preview` 도 현재 동일)
- 키 발급: **https://console.typesafe.ai/settings/keys** — 공식 문서에는 waitlist 언급이 없다(런칭 글은 early access). **실제 자력 발급 가능 여부는 로그인해봐야 확정된다.**
- 환경변수: `TYPESAFE_API_KEY`

### 2-B. 한도 (공식 문서)

| 항목 | 값 |
|---|---|
| 컨텍스트 | **요청당 64k 토큰 · `state` 단독 32k** |
| Choice | 최대 **255** 선택지 |
| Score | **2~10** 단계 |
| 입력 형식 | 텍스트 전용 (문자열·JSON 객체·배열). 이미지·음성 ❌ |
| Rate limit | 250,000 tok/s · 1,200 req/min (문서가 "동적 조정 중" 경고) |
| 가격 | 입력 $0.042/M · 출력 $0 |

### 2-C. 호출 형태

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()                      # TYPESAFE_API_KEY 를 env 에서 읽음
response = client.system_one(
    state=ticket,                              # str | dict | list
    questions={
        "department": Choice(
            instructions="Which team should handle this",
            criteria={"billing": "결제·구독", "technical": "버그·연동", "sales": "가격·계정"},
        ),
        "urgency": Score(instructions="긴급도", criteria=["low", "medium", "high"]),
        "needs_human": Noul(instructions="사람 검토가 필요한가"),
    },
)
response.answers["department"].choice          # "billing"
response.answers["department"].probabilities   # {"billing":0.84, "technical":0.159, ...}
response.answers["department"].confidence      # 0.596
```

TypeScript 는 `import { choice, noul, TypeSafeClient } from "@typesafe-ai/sdk"` + `client.systemOne({state, questions})`.

### 2-D. 유보 기록 (2026-09-19, 사용자 판단으로 진행 확정)

도입 전 제기했던 우려 3건을 기록으로 남긴다. 계획은 이 우려를 **검증 게이트로 전환**해 반영했다.

1. **볼륨** — 444배 저렴이 의미를 가지려면 하루 수만 건 규모여야 하는데 현재 판단 호출은 하루 수십 건. → C-4 골든셋 평가에서 **정확도**로 판정한다(비용이 아니라).
2. **업무컴 외부 전송** — 슬랙 멘션 본문·이슈 내용을 외부 API로 보내야 분류가 된다. → **C-6 를 회사 정책 게이트로 분리**. 개인컴 먼저, 업무컴은 승인 후.
3. **감사 추적** — 선택지와 확률만 남고 근거가 없다. → C-5 에서 **confidence 임계 미달 시 사람/LLM 검토로 분기**하는 설계를 필수 조건으로 둔다.

---

## 3. Phase A — Archify 격리 테스트 (개인컴, 정본 미변경)

> 목표: **정본·`~/.agents/skills` 를 건드리지 않고** 품질과 정확도를 판정한다.

### A-1. 안정 태그 격리 클론
- 작업: `v2.16.0` 태그를 스크래치패드에 클론 (개발판 `main` 아님)
- verify: `git -C <dir> describe --tags` == `v2.16.0` · `node <dir>/archify/bin/archify.mjs --help` exit 0 · `du -sh <dir>/archify` 로 **벤더링 시 증가할 용량 측정**

### A-2. 첫 다이어그램 — 작은 대상
- 대상: `~/Library/Application Support/vibe-ai-config/instapaper-mcp` (TypeScript, 오늘 받은 것 · 소스 2파일이라 대조가 쉽다)
- 타입: `architecture` (MCP 서버 ↔ Instapaper API ↔ Keychain 래퍼)
- verify: `validate architecture <cand>.json --quality showcase --json` → **artifact 체크 9/9 · error 0 · warning 0**

### A-3. 🔴 엣지 대조 게이트 (핵심 — 통과 못 하면 도입 중단)
- 작업: 생성된 JSON 의 **모든 relationship 을 표로 뽑고**, 각 엣지마다 실제 소스의 근거 위치(`파일:줄`)를 찾는다
- verify: **근거 없는 엣지 0건.** 1건이라도 나오면 "환각 발생" 으로 기록하고, 도입하더라도 §4 사용 규약에 "엣지 대조 필수" 를 명문화한 뒤에만 진행

### A-4. 납품 + 브라우저 증거
- verify: `deliver` exit 0 + SHA-256 영수증 · `visual-check <out>.html --json` exit 0 · containment pass
- 이 맥의 Chrome 경로가 자동 탐지되는지 동시 확인 (`/Applications/Google Chrome.app/...`)

### A-5. 두 번째 대상 — 실전 규모
- 대상: `04.Archives/03.OutlineObsidianSync` (TypeScript 플러그인) 또는 `vibe-ai-config/install.sh` 배포 흐름(`workflow` 타입)
- verify: A-2~A-4 동일 게이트. **12노드 제한 안에서 의미가 유지되는지**가 실전 판정 기준

---

## 4. Phase B — Archify 정본 편입 · 배포

### B-1. 벤더링 위치
- 제안: **`skills/review/archify/`** (코드 이해·리뷰 계열. `code-review`·`explain-change` 와 같은 묶음)
- 소스는 `v2.16.0` 태그의 **`archify/` 서브트리만** 복사 (`.github`·`benchmarks`·`experiments`·`docs`·`archify.zip` 제외)
- verify: `ls skills/review/archify/SKILL.md` · `du -sh skills/review/archify`

### B-2. 배포 파이프라인 통과 확인
- 작업: `npx --yes skills@latest add "$REPO_ROOT" --full-depth --skill archify -g -y` (install.sh 의 시험 설치 경로 그대로)
- verify: `~/.agents/skills/archify/SKILL.md` 존재 · `~/.claude/skills/archify` 가 심링크 · `node ~/.agents/skills/archify/bin/archify.mjs --help` exit 0
- ⚠️ `npx skills` 는 **심링크가 아니라 복사**다(install.sh 주석). 업스트림 갱신 = 벤더 소스 교체 후 재설치.

### B-3. 업데이트 체크 차단 배선
- 작업: `ARCHIFY_UPDATE_CHECK_DISABLED=1` 을 상시 env 로. 위치 후보 — `.claude/settings.json` 의 `env` / `~/.zshrc.local` / `codex/config-root.toml`
- 근거: 업무컴에서 외부 GET 이 나가는 걸 기본값으로 두지 않는다. SKILL.md 가 매 생성마다 체커를 1회 돌리게 돼 있다.
- verify: `ARCHIFY_UPDATE_CHECK_DISABLED=1 node ~/.agents/skills/archify/scripts/check-update.mjs` → silent

### B-4. 버전 고정 기록
- 작업: `skills/review/archify/VENDORED.md` — 업스트림 URL · 태그 `v2.16.0` · 커밋 SHA · 벤더 일자 · 제외한 디렉터리 목록
- 근거: 개발판이 하루 단위로 움직이는 저장소다. 기록 없으면 개인컴·업무컴 산출물이 갈린다.

### B-5. 트리거 등록
- 작업: `shared/commands.md` 「스킬」 절에 1줄 — "아키텍처 그려줘 / 구조 그림 / 시퀀스 다이어그램 / 이 코드 흐름 시각화" → `archify`
- verify: `grep -n archify shared/commands.md`

### B-6. 업무컴 반영
- 작업: 업무컴에서 `install.sh work`
- 🔴 **선결 확인**: 업무컴에 Chrome/Chromium 이 있는지 (`visual-check` 전제). 없으면 `visual-check` 는 건너뛰고 `deliver` 영수증까지만 사용
- verify: `node ~/.agents/skills/archify/bin/archify.mjs --help` exit 0 · 업무 레포 1건으로 A-2~A-3 재현

---

## 5. Phase C — Jev 도입

### C-1. 키 발급 (사용자 단계)
- https://console.typesafe.ai/settings/keys 에서 발급. 대기자 명단이면 등록만 하고 C-2 는 보류
- **Keychain 저장** — Instapaper 와 같은 규약 재사용:
  ```bash
  security add-generic-password -U -a "$USER" -s 'vibe-ai-config.typesafe.api-key' -w
  ```
- verify: `security find-generic-password -a "$USER" -s 'vibe-ai-config.typesafe.api-key'` exit 0 (값 출력 없이 존재만)

### C-2. 격리 PoC
- 작업: 스크래치패드에 `uv venv` → `uv pip install typesafe-sdk` → 호출 1건 (§2-C 예제)
- verify: 응답에 `choice`·`probabilities`·`confidence` 3개 필드 존재 · exit 0

### C-3. 한국 지연시간 실측
- 작업: 동일 요청 10회, 왕복 시간 측정
- 근거: 공식 70~500ms 는 **TypeSafe 자체 발표 + 미 서부 노트북 측정**이다. 한국 기준 수치가 아니다.
- verify: 측정표(최소·중앙·최대). 중앙값이 1초를 넘으면 "실시간 판단" 용도는 탈락으로 기록

### C-4. 골든셋 정확도 평가 — 대상 1개로 좁힌다
- 대상: **`slack-mention-triage` 의 4분류** (신규 작업요청 / 기존 이슈 / 질문 / 정보공유)
- 작업: ① 과거 멘션 30건 수집 → ② 사람이 정답 라벨링 → ③ Jev `Choice` 분류 → ④ 현행(Opus) 분류와 대조
- verify: 정확도·혼동표. **Jev 가 현행보다 낮으면 편입하지 않는다.**
- ⚠️ 이 단계에서 슬랙 멘션 본문이 외부로 나간다. **개인 계정·비업무 데이터로만** 수행하거나, 익명화 후 수행.

### C-5. 편입 설계 (C-4 통과 시)
- 필수 조건: **confidence 임계 미달 → 사람/LLM 검토로 분기.** 임계값은 C-4 데이터로 정한다
- 감사 추적: 선택·확률·confidence 를 작업 로그에 남긴다 (근거가 없는 대신 수치를 남긴다)
- 비밀: Keychain 래퍼 방식 재사용. `TYPESAFE_API_KEY` 를 파일·env 파일에 평문 저장 ❌

### C-6. 🔴 업무컴 적용 — 정책 게이트 (에이전트 판단 범위 밖)
- 업무컴 데이터(슬랙 멘션·이슈·코드)를 TypeSafe API 로 보내는 것은 **회사 정책 확인이 선행**되어야 한다
- 확인 전에는 **개인컴 개인 데이터에만** 적용한다

---

## 6. 결정 필요 사항

| # | 항목 | 제안 | 근거 |
|---|---|---|---|
| 1 | Archify 를 벤더링할까, `npx skills add tt-a1i/archify -g` 직접 설치할까 | **벤더링** | 직접 설치는 `~/.agents/skills` 에 실체를 깔아 레포 정본 밖에 자산이 생긴다 → 업무컴 재현 불가·드리프트. 볼트 함정 「정본 이원화」와 같은 패턴 |
| 2 | 태그 `v2.16.0` vs 기본 브랜치(`2.17.0-dev.1`) | **v2.16.0** | 개발판은 어제도 푸시됐다. 두 머신 산출물 동일성이 깨진다 |
| 3 | 벤더링 위치 | `skills/review/` | 코드 이해 계열. A-1 에서 잰 용량이 과도하면 재검토 |
| 4 | `ARCHIFY_UPDATE_CHECK_DISABLED` 배선 위치 | `.claude/settings.json` env | 도구 무관하게 깔리려면 shell 이 아니라 하네스 설정이 낫다 — B-3 에서 실측 후 확정 |
| 5 | Jev 업무컴 적용 | **보류** (C-6 정책 게이트) | 회사 데이터 외부 전송 |

## 7. 리스크

- **Archify 환각 엣지** — 검증기가 못 잡는다. A-3 게이트가 유일한 방어선이고, 업무컴 레거시 PHP 에서 가장 위험하다
- **업스트림 churn** — ★66.8k·open issue 82·개발판 일일 푸시. 태그 고정 + `VENDORED.md` 로만 방어된다
- **Chrome 의존** — `visual-check` 전용. 없어도 `deliver` 까지는 동작하므로 치명적이지 않다
- **Jev rate limit 변동** — 공식 문서가 "동적 조정 중, 예고 없이 변경" 이라고 명시. 운영 편입 시 실패 처리 경로 필수
- **Jev early access 불확실** — 키가 안 나오면 Phase C 전체가 대기. Phase A·B 와 독립이라 Archify 진행은 막히지 않는다

## 8. 순서

```
A-1 → A-2 → A-3(게이트) → A-4 → A-5 → B-1 → B-2 → B-3 → B-4 → B-5 → B-6(업무컴)
C-1(사용자) → C-2 → C-3 → C-4(게이트) → C-5 → C-6(정책 게이트)
```

A·B 와 C 는 병렬. C-1 은 지금 바로 사용자가 할 수 있다.
