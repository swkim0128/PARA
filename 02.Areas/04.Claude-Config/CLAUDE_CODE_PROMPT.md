# Claude Code 작업 프롬프트

## 📋 작업 목표
`~/Projects/claude-config-sync` 프로젝트를 생성하고, `/Users/eunsol/Project/para/02.Areas/04.Claude-Config`에 있는 백업 관련 파일들을 적절히 이동/정리합니다.

---

## 🎯 작업 요구사항

### 1. 프로젝트 디렉토리 구조 생성
```
~/Projects/claude-config-sync/
├── README.md
├── skills/
│   └── notion-weekly-schedule/
│       └── SKILL.md
├── mcp-configs/
│   ├── claude_desktop_config.json
│   └── claude_code_config.json
├── scripts/
│   └── sync-claude-config.sh
└── backups/
    └── .gitkeep
```

### 2. 파일 이동 및 정리

#### 원본 경로 (이동할 파일들)
`/Users/eunsol/Project/para/02.Areas/04.Claude-Config/`에서:
- `claude_config_template.json` → `~/Projects/claude-config-sync/mcp-configs/claude_desktop_config.json`
- `sync-claude-config.sh` → `~/Projects/claude-config-sync/scripts/sync-claude-config.sh`
- `notion-weekly-schedule-skill.md` → 전체 스킬 파일로 확장하여 `~/Projects/claude-config-sync/skills/notion-weekly-schedule/SKILL.md`

#### 유지할 파일 (Areas에 남김)
`/Users/eunsol/Project/para/02.Areas/04.Claude-Config/`에:
- `README.md` (사용 가이드)
- `Claude-Desktop-Configuration.md` (상세 문서)

### 3. 스크립트 수정

`sync-claude-config.sh` 스크립트의 경로를 업데이트:
```bash
# 변경 전
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 변경 후 - 프로젝트 루트 기준으로 경로 설정
PROJECT_ROOT="$HOME/Projects/claude-config-sync"
BACKUP_DIR="$PROJECT_ROOT/backups"
```

### 4. README.md 작성

프로젝트 루트에 다음 내용을 포함하는 README.md 작성:
- 프로젝트 개요
- 디렉토리 구조
- 설치 및 사용 방법
- 동기화 프로세스
- 환경 변수 설정
- 문서 참조 링크

### 5. SKILL.md 작성

`/mnt/skills/user/notion-weekly-schedule/SKILL.md`의 전체 내용을 복사하여 
`~/Projects/claude-config-sync/skills/notion-weekly-schedule/SKILL.md`로 생성

---

## 🔧 구체적인 작업 단계

### Step 1: 프로젝트 디렉토리 생성
```bash
mkdir -p ~/Projects/claude-config-sync/{skills/notion-weekly-schedule,mcp-configs,scripts,backups}
```

### Step 2: 파일 복사
```bash
# MCP 설정 파일
cp /Users/eunsol/Project/para/02.Areas/04.Claude-Config/claude_config_template.json \
   ~/Projects/claude-config-sync/mcp-configs/claude_desktop_config.json

# 동기화 스크립트
cp /Users/eunsol/Project/para/02.Areas/04.Claude-Config/sync-claude-config.sh \
   ~/Projects/claude-config-sync/scripts/sync-claude-config.sh

# 스킬 파일 (전체 내용)
cp /mnt/skills/user/notion-weekly-schedule/SKILL.md \
   ~/Projects/claude-config-sync/skills/notion-weekly-schedule/SKILL.md
```

### Step 3: 스크립트 수정
`~/Projects/claude-config-sync/scripts/sync-claude-config.sh` 파일에서:
- `SCRIPT_DIR` → `PROJECT_ROOT` 경로 변경
- `BACKUP_DIR` 경로를 `$PROJECT_ROOT/backups`로 수정
- 스킬 소스 경로 업데이트

### Step 4: 권한 설정
```bash
chmod +x ~/Projects/claude-config-sync/scripts/sync-claude-config.sh
```

### Step 5: README.md 생성
프로젝트 루트에 상세한 README.md 작성

### Step 6: .gitignore 생성
```bash
cat > ~/Projects/claude-config-sync/.gitignore << 'EOF'
# 백업 파일
backups/*.json

# 환경 변수
.env

# macOS
.DS_Store

# 민감한 정보
*_secret*
*_private*
EOF
```

### Step 7: Areas 경로 정리
`/Users/eunsol/Project/para/02.Areas/04.Claude-Config/README.md`를 업데이트하여:
- 실제 프로젝트 위치 안내: `~/Projects/claude-config-sync`
- 사용 가이드 유지
- 프로젝트 링크 추가

---

## 📝 필요한 파일 내용

### 1. ~/Projects/claude-config-sync/README.md

```markdown
# Claude Config Sync

Claude Desktop과 Claude Code 간 MCP 서버 설정 및 스킬 동기화 프로젝트

## 📁 프로젝트 구조

\`\`\`
claude-config-sync/
├── README.md                    # 프로젝트 개요
├── skills/                      # Claude 스킬 파일들
│   └── notion-weekly-schedule/
│       └── SKILL.md
├── mcp-configs/                 # MCP 서버 설정
│   ├── claude_desktop_config.json
│   └── claude_code_config.json
├── scripts/                     # 자동화 스크립트
│   └── sync-claude-config.sh
└── backups/                     # 설정 백업
\`\`\`

## 🚀 빠른 시작

1. 환경 변수 설정
2. 스크립트 실행
3. Claude Code 재시작

자세한 내용은 `/Users/eunsol/Project/para/02.Areas/04.Claude-Config/` 문서 참조
```

### 2. MCP 설정 파일 템플릿

`mcp-configs/claude_desktop_config.json`에 현재 사용 중인 MCP 서버 설정 포함

---

## ✅ 완료 체크리스트

- [ ] `~/Projects/claude-config-sync` 디렉토리 구조 생성
- [ ] 파일 복사 완료
- [ ] 스크립트 경로 수정
- [ ] 실행 권한 부여
- [ ] README.md 작성
- [ ] .gitignore 작성
- [ ] Areas 경로 README 업데이트
- [ ] 스킬 파일 전체 내용 복사
- [ ] 백업 디렉토리 설정

---

## 🔗 참고 문서

- 사용 가이드: `/Users/eunsol/Project/para/02.Areas/04.Claude-Config/README.md`
- 상세 설정: `/Users/eunsol/Project/para/02.Areas/04.Claude-Config/Claude-Desktop-Configuration.md`
- 원본 스킬: `/mnt/skills/user/notion-weekly-schedule/SKILL.md`
