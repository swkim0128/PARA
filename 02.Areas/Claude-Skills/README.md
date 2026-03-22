# Claude Skills 백업 디렉토리

## 개요
이 디렉토리는 Claude Code 및 다른 AI CLI 툴에서 직접 적용 가능한 스킬 파일들을 관리합니다.
각 스킬 디렉토리 내 `SKILL.md`를 Claude skills 경로(`~/.claude/skills/<skill-name>/SKILL.md`)에 복사하면 바로 적용됩니다.

## 디렉토리 구조
```
02.Areas/Claude-Skills/
├── README.md
├── <skill-name>/
│   ├── SKILL.md                    # 최신 버전 (항상 현재 적용 중인 버전)
│   ├── SKILL_YYYYMMDD_HHMMSS.md   # 이전 버전 백업 (히스토리)
│   └── SKILL_YYYYMMDD_HHMMSS.md   # 이전 버전 백업 (히스토리)
└── ...
```

## 백업 규칙 (중요)

스킬 업데이트 시 반드시 아래 순서를 준수합니다:

### 1단계: 구버전 백업
```bash
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
cp 02.Areas/Claude-Skills/<skill>/SKILL.md \
   02.Areas/Claude-Skills/<skill>/SKILL_${TIMESTAMP}.md
```

### 2단계: 최신 버전으로 교체
```bash
cp ~/.claude/skills/<skill>/SKILL.md \
   02.Areas/Claude-Skills/<skill>/SKILL.md
```

> **핵심**: `SKILL_날짜.md`는 항상 **업데이트 이전의 구버전**이어야 합니다.
> 신버전을 타임스탬프 파일로 저장하지 마세요.

## 복원 방법

```bash
# 최신 버전 적용
cp 02.Areas/Claude-Skills/<skill>/SKILL.md \
   ~/.claude/skills/<skill>/SKILL.md

# 특정 이전 버전 복원
cp 02.Areas/Claude-Skills/<skill>/SKILL_20260201_063854.md \
   ~/.claude/skills/<skill>/SKILL.md
```

## 등록된 스킬 목록

| 스킬명 | 설명 | 최신 백업 |
|--------|------|----------|
| notion-weekly-schedule | 주간 일정 관리 (진행 중 프로젝트 태스크 동기화 포함) | 2026-03-22 |
| notion-weekly-retrospective | 주간 회고 작성 | 2026-01-25 |
| notion-project-creator | 프로젝트 생성 | - |
| task-management | 태스크 관리 | - |
| skill-creator | 스킬 생성/개선 | - |
| skill-backup | 스킬 백업 관리 | 2026-03-02 |
| gdrive-sort | 구글 드라이브 정리 | - |
| notion-weekly-routine | 주간 일정정리 루틴 (이번 주 정리 → 회고 → 다음 주 계획) | 2026-03-15 |
| notion-diet-manager | 식단 관리 (식재료 추가/제거, 먹은 음식 기록) | 2026-03-22 |
| notion-project-manager | 프로젝트/태스크/스프린트 관리 | 2026-03-22 |

---
*마지막 업데이트: 2026-03-22*
