# Claude Desktop 설정 및 Claude Code 동기화 상세 가이드

> 작성일: 2024-12-05
> 목적: Claude Desktop → Claude Code 완벽 마이그레이션

---

## 🎯 목표

Claude Desktop에서 사용 중인 MCP 서버와 스킬을 Claude Code에도 동일하게 적용하여, 두 환경에서 일관된 작업 경험을 제공합니다.

---

## 📂 파일 위치

### Claude Desktop 설정
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

### Claude Code 설정
```
~/.claude/claude_code_config.json
```

### 스킬 위치
- **Claude Desktop**: `/mnt/skills/user/`
- **Claude Code**: `~/.claude/skills/`

---

## 🔧 MCP 서버 설정

### 현재 사용 중인 MCP 서버

#### 1. Filesystem
파일 시스템 접근을 제공합니다.

```json
"filesystem": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/eunsol/Project"
  ]
}
```

#### 2. Notion
Notion 통합을 제공합니다.

```json
"notion": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-notion"
  ],
  "env": {
    "NOTION_API_KEY": "${NOTION_API_KEY}"
  }
}
```

#### 3. Google Calendar
Google Calendar 통합을 제공합니다.

```json
"google-calendar": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-google-calendar"
  ]
}
```

#### 4. Google Drive
Google Drive 통합을 제공합니다.

```json
"google-drive": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-google-drive"
  ]
}
```

#### 5. Gmail
Gmail 통합을 제공합니다.

```json
"gmail": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-gmail"
  ]
}
```

---

## 🔑 환경 변수 설정

### ~/.zshrc 또는 ~/.bashrc에 추가

```bash
# Notion API Key
export NOTION_API_KEY="your_notion_integration_token"

# 기타 API 키들...
```

### 적용
```bash
source ~/.zshrc  # 또는 source ~/.bashrc
```

### 확인
```bash
echo $NOTION_API_KEY
```

---

## 🚀 동기화 실행

### 1. 스크립트 실행 권한 부여
```bash
chmod +x /Users/eunsol/Project/para/02.Areas/04.Claude-Config/sync-claude-config.sh
```

### 2. 스크립트 실행
```bash
cd /Users/eunsol/Project/para/02.Areas/04.Claude-Config
./sync-claude-config.sh
```

### 3. 실행 결과 확인
스크립트는 다음 작업을 수행합니다:
- 기존 설정 백업
- MCP 설정 파일 복사
- 스킬 디렉토리 동기화
- 환경 변수 확인

---

## 📋 수동 동기화

스크립트를 사용하지 않고 수동으로 동기화하려면:

### 1. 설정 파일 복사
```bash
mkdir -p ~/.claude
cp ~/Library/Application\ Support/Claude/claude_desktop_config.json \
   ~/.claude/claude_code_config.json
```

### 2. 스킬 복사
```bash
mkdir -p ~/.claude/skills
cp -r /mnt/skills/user/* ~/.claude/skills/
```

---

## ✅ 검증

### MCP 서버 연결 확인
```bash
# 설정 파일 확인
cat ~/.claude/claude_code_config.json | jq .

# MCP 서버 목록
cat ~/.claude/claude_code_config.json | jq '.mcpServers | keys'
```

### 스킬 확인
```bash
# 스킬 목록
ls -la ~/.claude/skills/

# 스킬 문서 확인
find ~/.claude/skills/ -name "SKILL.md"
```

---

## 🔄 정기 동기화

### Cron 설정 (선택사항)
```bash
# crontab 편집
crontab -e

# 매일 오전 9시 동기화
0 9 * * * /Users/eunsol/Project/para/02.Areas/04.Claude-Config/sync-claude-config.sh
```

---

## 🛠️ 문제 해결

### MCP 서버가 연결되지 않을 때
1. MCP 패키지 설치 확인
2. 환경 변수 설정 확인
3. JSON 문법 검사
4. Claude Code 재시작

### 스킬이 인식되지 않을 때
1. 스킬 디렉토리 경로 확인
2. SKILL.md 파일 존재 확인
3. Claude Code 재시작

---

## 📚 참고 자료

- [Claude Documentation](https://docs.claude.com)
- [MCP Protocol](https://modelcontextprotocol.io)
- [Notion API](https://developers.notion.com)
