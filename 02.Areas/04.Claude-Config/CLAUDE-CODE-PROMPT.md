# Claude Code 프롬프트 - Claude Config Sync 프로젝트 생성

다음 프롬프트를 Claude Code에 복사하여 붙여넣으세요.

---

## 📋 Claude Code 프롬프트

```
~/Projects/claude-config-sync 프로젝트를 생성해주세요.

### 프로젝트 구조

```
claude-config-sync/
├── README.md
├── docs/
│   └── Claude-Desktop-Configuration.md
├── skills/
│   └── notion-weekly-schedule/
│       └── SKILL.md
├── mcp-configs/
│   └── claude_config_template.json
├── scripts/
│   └── sync-claude-config.sh
└── backups/
    └── .gitkeep
```

### 1. README.md

프로젝트 소개 및 빠른 시작 가이드 작성:
- 프로젝트 개요: Claude Desktop과 Claude Code 간 MCP 설정 및 스킬 동기화
- 프로젝트 구조 설명
- 빠른 시작 가이드 (스크립트 실행 방법)
- 환경 변수 설정 방법
- 동기화 대상 (MCP 서버, 스킬 목록)

### 2. mcp-configs/claude_config_template.json

다음 MCP 서버 설정:
- filesystem: /Users/eunsol/Project 경로 접근
- notion: NOTION_API_KEY 환경 변수 사용
- google-calendar
- google-drive  
- gmail

JSON 형식으로 작성, @modelcontextprotocol/server-* 패키지 사용

### 3. scripts/sync-claude-config.sh

동기화 스크립트 작성 (Bash):
- Claude Desktop 설정 백업 (타임스탬프 포함)
- Claude Desktop → Claude Code 설정 복사
- /mnt/skills/user/ → ~/.claude/skills/ 스킬 동기화
- 환경 변수 확인 (NOTION_API_KEY)
- 진행 상황 출력 (색상 포함)
- 백업 파일은 backups/ 디렉토리에 저장

### 4. skills/notion-weekly-schedule/SKILL.md

노션 주간 일정 관리 스킬 문서:
- 데이터베이스: '일지 및 회고' (Data Source ID: d4c94e28-6040-45f4-a4ae-69b74a6b26b4)
- 기능: 이번 주 일정 페이지 검색, 자연어로 일정 추가, WORK/LIFE 자동 분류
- 주간 페이지 형식: [week XX] MM.DD ~ MM.DD 일지
- 사용 예시 포함

### 5. docs/Claude-Desktop-Configuration.md

상세 설정 가이드:
- MCP 서버별 설정 방법
- 환경 변수 설정 가이드
- 수동 동기화 방법
- 문제 해결 가이드
- 백업 및 복원 방법

### 6. backups/.gitkeep

빈 파일로 디렉토리 유지

---

모든 파일을 생성하고, sync-claude-config.sh에는 실행 권한을 부여해주세요.
```

---

## 사용 방법

1. Claude Code 실행
2. 위 프롬프트 전체를 복사
3. Claude Code에 붙여넣기
4. 엔터 키

Claude Code가 자동으로 프로젝트 구조를 생성하고 모든 파일을 작성합니다.
