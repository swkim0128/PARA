#!/bin/bash
# sync-claude-config.sh
# Claude Desktop 설정을 Claude Code에 동기화하는 스크립트

set -e

# 색상 정의
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 경로 정의
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DESKTOP_CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
CODE_CONFIG="$HOME/.claude/claude_code_config.json"
SKILLS_SRC="/mnt/skills/user"
SKILLS_DEST="$HOME/.claude/skills"
BACKUP_DIR="$SCRIPT_DIR/backups"

echo "=========================================="
echo "Claude Desktop → Claude Code 동기화"
echo "=========================================="
echo ""

# 백업 디렉토리 생성
mkdir -p "$BACKUP_DIR"

# 1. 기존 설정 백업
echo "[1/4] 기존 설정 백업 중..."
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

if [ -f "$DESKTOP_CONFIG" ]; then
    cp "$DESKTOP_CONFIG" "$BACKUP_DIR/claude_desktop_config_$TIMESTAMP.json"
    echo -e "${GREEN}✅ Claude Desktop 설정 백업 완료${NC}"
    echo "   → $BACKUP_DIR/claude_desktop_config_$TIMESTAMP.json"
fi

if [ -f "$CODE_CONFIG" ]; then
    cp "$CODE_CONFIG" "$BACKUP_DIR/claude_code_config_$TIMESTAMP.json"
    echo -e "${GREEN}✅ Claude Code 설정 백업 완료${NC}"
    echo "   → $BACKUP_DIR/claude_code_config_$TIMESTAMP.json"
fi
echo ""

# 2. MCP 설정 파일 동기화
echo "[2/4] MCP 설정 파일 동기화 중..."
if [ -f "$DESKTOP_CONFIG" ]; then
    mkdir -p "$HOME/.claude"
    cp "$DESKTOP_CONFIG" "$CODE_CONFIG"
    echo -e "${GREEN}✅ MCP 설정 파일 동기화 완료${NC}"
    echo "   - 소스: $DESKTOP_CONFIG"
    echo "   - 대상: $CODE_CONFIG"
else
    echo -e "${RED}❌ Claude Desktop 설정 파일을 찾을 수 없습니다.${NC}"
    echo "   경로: $DESKTOP_CONFIG"
    echo ""
    echo "   설정 파일을 수동으로 생성하려면:"
    echo "   cp $SCRIPT_DIR/claude_config_template.json $CODE_CONFIG"
fi
echo ""

# 3. 스킬 동기화
echo "[3/4] 스킬 동기화 중..."
if [ -d "$SKILLS_SRC" ]; then
    mkdir -p "$SKILLS_DEST"
    cp -r "$SKILLS_SRC"/* "$SKILLS_DEST/" 2>/dev/null || true
    echo -e "${GREEN}✅ 스킬 동기화 완료${NC}"
    echo "   - 소스: $SKILLS_SRC"
    echo "   - 대상: $SKILLS_DEST"
    
    if [ -d "$SKILLS_DEST" ]; then
        echo ""
        echo "   동기화된 스킬:"
        for skill in "$SKILLS_DEST"/*; do
            if [ -d "$skill" ]; then
                echo "   - $(basename "$skill")"
            fi
        done
    fi
else
    echo -e "${YELLOW}⚠️  스킬 디렉토리를 찾을 수 없습니다.${NC}"
    echo "   경로: $SKILLS_SRC"
fi
echo ""

# 4. 환경 변수 확인
echo "[4/4] 환경 변수 확인 중..."
REQUIRED_VARS=("NOTION_API_KEY")
MISSING_VARS=()

for var in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!var}" ]; then
        MISSING_VARS+=("$var")
    fi
done

if [ ${#MISSING_VARS[@]} -eq 0 ]; then
    echo -e "${GREEN}✅ 필요한 환경 변수가 모두 설정되어 있습니다.${NC}"
else
    echo -e "${YELLOW}⚠️  다음 환경 변수가 설정되지 않았습니다:${NC}"
    for var in "${MISSING_VARS[@]}"; do
        echo "   - $var"
    done
    echo ""
    echo "   환경 변수 설정 방법:"
    echo "   ~/.zshrc 또는 ~/.bashrc에 다음 내용을 추가하세요:"
    echo ""
    for var in "${MISSING_VARS[@]}"; do
        echo "   export $var=\"your-$var-here\""
    done
    echo ""
    echo "   설정 후: source ~/.zshrc"
fi
echo ""

# 완료 메시지
echo "=========================================="
echo -e "${GREEN}동기화 완료!${NC}"
echo "=========================================="
echo ""
echo "다음 단계:"
echo "1. Claude Code를 재시작하세요"
echo "2. MCP 서버 연결 상태를 확인하세요"
echo "3. 스킬이 정상적으로 동작하는지 테스트하세요"
echo ""
echo "백업 위치: $BACKUP_DIR"
echo ""
