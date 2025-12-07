#!/bin/bash
# migrate-to-projects.sh
# 02.Areas의 파일들을 ~/Projects/claude-config-sync로 이동

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "=========================================="
echo "Claude Config 파일 마이그레이션"
echo "=========================================="
echo ""

# 경로 정의
SOURCE_DIR="/Users/eunsol/Project/para/02.Areas/04.Claude-Config"
TARGET_DIR="$HOME/Projects/claude-config-sync"

# 1. 대상 디렉토리 구조 생성
echo "[1/3] 프로젝트 디렉토리 구조 생성 중..."
mkdir -p "$TARGET_DIR"/{skills/notion-weekly-schedule,mcp-configs,scripts,backups,docs}
echo -e "${GREEN}✅ 디렉토리 생성 완료${NC}"
echo ""

# 2. 파일 복사
echo "[2/3] 파일 복사 중..."

# 스크립트
if [ -f "$SOURCE_DIR/sync-claude-config.sh" ]; then
    cp "$SOURCE_DIR/sync-claude-config.sh" "$TARGET_DIR/scripts/"
    chmod +x "$TARGET_DIR/scripts/sync-claude-config.sh"
    echo "  ✓ sync-claude-config.sh → scripts/"
fi

# MCP 설정
if [ -f "$SOURCE_DIR/claude_config_template.json" ]; then
    cp "$SOURCE_DIR/claude_config_template.json" "$TARGET_DIR/mcp-configs/"
    echo "  ✓ claude_config_template.json → mcp-configs/"
fi

# 스킬
if [ -f "$SOURCE_DIR/notion-weekly-schedule-skill.md" ]; then
    cp "$SOURCE_DIR/notion-weekly-schedule-skill.md" "$TARGET_DIR/skills/notion-weekly-schedule/SKILL.md"
    echo "  ✓ notion-weekly-schedule-skill.md → skills/notion-weekly-schedule/SKILL.md"
fi

# 문서
if [ -f "$SOURCE_DIR/Claude-Desktop-Configuration.md" ]; then
    cp "$SOURCE_DIR/Claude-Desktop-Configuration.md" "$TARGET_DIR/docs/"
    echo "  ✓ Claude-Desktop-Configuration.md → docs/"
fi

echo -e "${GREEN}✅ 파일 복사 완료${NC}"
echo ""

# 3. 프로젝트 README 생성
echo "[3/3] 프로젝트 README 생성 중..."
cat > "$TARGET_DIR/README.md" << 'READMEEOF'
# Claude Config Sync

Claude Desktop과 Claude Code 간 설정 및 스킬 동기화 프로젝트

## 📁 프로젝트 구조

```
claude-config-sync/
├── README.md                    # 이 파일
├── docs/                        # 상세 문서
│   └── Claude-Desktop-Configuration.md
├── skills/                      # 클로드 스킬 파일들
│   └── notion-weekly-schedule/
│       └── SKILL.md
├── mcp-configs/                 # MCP 서버 설정 파일들
│   └── claude_config_template.json
├── scripts/                     # 동기화 스크립트
│   └── sync-claude-config.sh
└── backups/                     # 설정 백업 파일들
```

## 🚀 빠른 시작

### 1. 스크립트 실행
```bash
cd ~/Projects/claude-config-sync/scripts
./sync-claude-config.sh
```

### 2. 환경 변수 설정
```bash
# ~/.zshrc 또는 ~/.bashrc에 추가
export NOTION_API_KEY="your-notion-api-key"

# 적용
source ~/.zshrc
```

### 3. Claude Code 재시작

## 📝 동기화 대상

### MCP 서버
- filesystem
- notion
- google-calendar
- google-drive
- gmail

### 스킬
- notion-weekly-schedule: 노션 주간 일정 관리

## 📚 문서

- [상세 설정 가이드](docs/Claude-Desktop-Configuration.md)
- [사용 가이드](../para/02.Areas/04.Claude-Config/README.md)

## 🔄 동기화 흐름

1. Claude Desktop 설정 백업
2. Claude Code로 복사
3. 스킬 동기화
4. 환경 변수 확인

## 💾 백업

동기화 시 자동으로 `backups/` 디렉토리에 백업이 생성됩니다.

## 📌 참고

원본 가이드: `/Users/eunsol/Project/para/02.Areas/04.Claude-Config/`
READMEEOF

echo -e "${GREEN}✅ README 생성 완료${NC}"
echo ""

# 완료
echo "=========================================="
echo -e "${GREEN}마이그레이션 완료!${NC}"
echo "=========================================="
echo ""
echo "프로젝트 위치: $TARGET_DIR"
echo ""
echo "다음 단계:"
echo "1. cd ~/Projects/claude-config-sync"
echo "2. ls -la  # 구조 확인"
echo "3. cd scripts && ./sync-claude-config.sh  # 동기화 실행"
echo ""
