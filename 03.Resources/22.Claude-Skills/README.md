# Claude Skills 백업 디렉토리

## 개요
이 디렉토리는 사용자가 작성한 클로드 스킬들의 백업을 저장합니다.

## 디렉토리 구조
```
22.Claude-Skills/
├── README.md              # 이 파일
├── backup-guide.md        # 백업 가이드
└── backups/               # 백업 파일들
    └── [skill-name]_[timestamp]/
        └── SKILL.md
```

## 백업 명명 규칙
- 형식: `[스킬명]_[YYYYMMDD_HHMMSS]`
- 예시: `notion-weekly-schedule_20251219_145005`

## 백업 방법
1. "클로드 스킬 백업해줘" 라고 요청
2. 자동으로 타임스탬프가 포함된 디렉토리에 백업됩니다

## 백업된 스킬 목록
- notion-weekly-schedule (2024-12-19 14:50:05)

## 복원 방법
백업된 스킬을 복원하려면:
1. backups 디렉토리에서 원하는 백업 선택
2. SKILL.md 내용 확인
3. 필요시 /mnt/skills/user/[skill-name]/SKILL.md로 복사

## 참고
- 정기적으로 백업하는 것을 권장합니다
- 오래된 백업은 주기적으로 정리하세요
- 중요한 변경 전에는 항상 백업하세요