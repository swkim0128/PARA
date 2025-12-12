# 현재 설치된 MCP 서버 및 Claude Code 설치 가이드

## 📋 현재 Claude Desktop에 설치된 MCP 서버

### 1. sequential-thinking
- **패키지**: `@modelcontextprotocol/server-sequential-thinking`
- **용도**: 단계별 사고 과정을 통한 문제 해결

### 2. google-calendar
- **패키지**: `@cocal/google-calendar-mcp`
- **용도**: Google Calendar 통합
- **환경 변수**: `GOOGLE_OAUTH_CREDENTIALS`
- **설정 파일**: `/Users/eunsol/.env/gcp-oauth.keys.json`

---

## 🚀 Claude Code 빠른 설치

### 한 줄 명령어로 설치

```bash
mkdir -p ~/.claude && cp ~/Library/Application\ Support/Claude/claude_desktop_config.json ~/.claude/claude_code_config.json && echo "✅ 설치 완료! Claude Code를 재시작하세요."
```

### 단계별 설치

```bash
# 1. 디렉토리 생성
mkdir -p ~/.claude

# 2. 설정 파일 복사
cp ~/Library/Application\ Support/Claude/claude_desktop_config.json \
   ~/.claude/claude_code_config.json

# 3. 확인
cat ~/.claude/claude_code_config.json
```

---

## 📦 설정 파일 내용

`~/.claude/claude_code_config.json`:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    },
    "google-calendar": {
      "command": "npx",
      "args": ["@cocal/google-calendar-mcp"],
      "env": {
        "GOOGLE_OAUTH_CREDENTIALS": "/Users/eunsol/.env/gcp-oauth.keys.json"
      }
    }
  }
}
```

---

## ✅ 설치 확인

```bash
# 설정 파일 확인
cat ~/.claude/claude_code_config.json | jq .

# MCP 서버 목록
cat ~/.claude/claude_code_config.json | jq '.mcpServers | keys'
```

**예상 출력:**
```json
[
  "google-calendar",
  "sequential-thinking"
]
```

---

## 🔑 Google OAuth 파일 확인

```bash
ls -la /Users/eunsol/.env/gcp-oauth.keys.json
```

이 파일이 있어야 Google Calendar가 작동합니다.

---

## 🔄 Claude Code 재시작

설정 후 반드시 Claude Code를 재시작하세요!

---

## 🛠️ 문제 해결

### 설정 파일이 읽히지 않을 때
```bash
# JSON 문법 확인
cat ~/.claude/claude_code_config.json | python3 -m json.tool
```

### MCP 서버 연결 실패
```bash
# npx 캐시 삭제
rm -rf ~/.npm/_npx

# 패키지 직접 설치
npm install -g @modelcontextprotocol/server-sequential-thinking
npm install -g @cocal/google-calendar-mcp
```
