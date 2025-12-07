# Claude Desktop & Claude Code 동기화 가이드

> 작업 파일 위치: `~/Projects/claude-config-sync/`

## 🎯 개요

Claude Desktop에서 사용 중인 MCP 서버와 스킬을 Claude Code에도 동일하게 적용하는 방법을 안내합니다.

## 📂 프로젝트 위치

**작업 파일**: `~/Projects/claude-config-sync/`

모든 실제 설정 파일, 스크립트, 스킬 파일은 위 경로에 있습니다.

## 🚀 빠른 시작

### 1. 프로젝트로 이동
```bash
cd ~/Projects/claude-config-sync
```

### 2. 동기화 실행
```bash
cd scripts
chmod +x sync-claude-config.sh
./sync-claude-config.sh
```

### 3. 환경 변수 설정
```bash
# ~/.zshrc 또는 ~/.bashrc에 추가
export NOTION_API_KEY="your-notion-api-key"

# 적용
source ~/.zshrc
```

### 4. Claude Code 재시작

## 📋 설정 대상

### MCP 서버
- **filesystem**: 파일 시스템 접근
- **notion**: Notion 통합
- **google-calendar**: Google Calendar 통합
- **google-drive**: Google Drive 통합
- **gmail**: Gmail 통합

### 스킬
- **notion-weekly-schedule**: 노션 '일지 및 회고' 데이터베이스 관리

## 📝 주요 파일

| 파일 | 위치 | 설명 |
|------|------|------|
| sync-claude-config.sh | `~/Projects/claude-config-sync/scripts/` | 자동 동기화 스크립트 |
| claude_config_template.json | `~/Projects/claude-config-sync/mcp-configs/` | MCP 설정 템플릿 |
| SKILL.md | `~/Projects/claude-config-sync/skills/notion-weekly-schedule/` | 노션 스킬 문서 |

## 🔧 설정 파일 경로

### Claude Desktop
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

### Claude Code
```
~/.claude/claude_code_config.json
```

## 💾 백업

동기화 스크립트는 자동으로 백업을 생성합니다:
- 위치: `~/Projects/claude-config-sync/backups/`
- 형식: `claude_desktop_config_YYYYMMDD_HHMMSS.json`

## 🔄 마이그레이션

이 디렉토리의 파일을 프로젝트로 이동하려면:

```bash
cd /Users/eunsol/Project/para/02.Areas/04.Claude-Config
chmod +x migrate-to-projects.sh
./migrate-to-projects.sh
```

## 📚 상세 문서

자세한 설정 방법은 다음 문서를 참조하세요:
- `~/Projects/claude-config-sync/README.md`
- `~/Projects/claude-config-sync/docs/Claude-Desktop-Configuration.md`

## ❓ 문제 해결

### MCP 서버가 연결되지 않을 때
1. 환경 변수 확인: `echo $NOTION_API_KEY`
2. 설정 파일 확인: `cat ~/.claude/claude_code_config.json | jq .`
3. Claude Code 재시작

### 스킬이 인식되지 않을 때
1. 스킬 디렉토리 확인: `ls -la ~/.claude/skills/`
2. SKILL.md 파일 확인: `find ~/.claude/skills/ -name "SKILL.md"`
3. Claude Code 재시작

## 💡 참고

- [Claude 공식 문서](https://docs.claude.com)
- [MCP 프로토콜](https://modelcontextprotocol.io)
