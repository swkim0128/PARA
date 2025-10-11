# MCP(Model Context Protocol) 활용 종합 가이드

## 1. MCP 개념

### MCP란 무엇인가?

MCP(Model Context Protocol)는 AI 애플리케이션이 외부 데이터 소스 및 도구와 안전하게 연결될 수 있도록 Anthropic이 개발한 개방형 프로토콜입니다.

**핵심 특징:**
- **표준화된 연결**: AI 모델과 다양한 데이터 소스를 일관된 방식으로 연결
- **보안성**: 안전한 데이터 접근 및 권한 관리
- **확장성**: 필요에 따라 새로운 서버를 추가하여 기능 확장
- **양방향 통신**: AI가 데이터를 읽고 작업을 수행할 수 있음

### 일상생활에서 활용할 수 있는 예제

#### 1. **개인 지식 관리**
- Notion, Obsidian 등의 노트와 연동하여 개인 지식베이스 검색
- 과거 작성한 문서를 바탕으로 새로운 콘텐츠 생성
- 회의록, 일기, 프로젝트 노트 자동 정리

#### 2. **업무 자동화**
- Google Drive 문서 자동 분석 및 요약
- Slack 메시지 검색 및 중요 내용 정리
- GitHub 코드 리뷰 및 이슈 관리

#### 3. **데이터 분석**
- SQLite 데이터베이스 쿼리 및 분석
- CSV/Excel 파일 데이터 시각화
- 웹사이트 데이터 스크래핑 및 분석

#### 4. **파일 시스템 관리**
- 로컬 파일 검색 및 내용 분석
- 대용량 문서 요약
- 코드베이스 탐색 및 리팩토링 제안

---

## 2. 주요 MCP 서버 소개

### MCP 클라이언트 비교

MCP는 다양한 AI 클라이언트에서 사용할 수 있습니다. 각 클라이언트의 특징을 비교해보겠습니다.

| 클라이언트 | 용도 | 장점 | 설정 위치 |
|-----------|------|------|----------|
| **Claude Desktop** | GUI 기반 대화형 인터페이스 | - 직관적인 UI<br>- 파일 업로드 지원<br>- 아티팩트 생성 | `~/Library/Application Support/Claude/`<br>(Mac) |
| **Claude Code** | 터미널 기반 코딩 도구 | - 개발 워크플로우 최적화<br>- Git 통합<br>- 빠른 코드 생성 | `~/.claude/` |
| **Gemini CLI** | Google AI 터미널 도구 | - Google 서비스 통합<br>- 다양한 모델 지원<br>- 스크립트 자동화 | `~/.gemini/` |

### MCP 클라이언트 설치

#### Claude Desktop
```bash
# Mac
brew install --cask claude

# Windows
# https://claude.ai/download 에서 다운로드

# Linux
# AppImage 또는 .deb 패키지 사용
```

#### Claude Code
```bash
# npm을 통한 설치
npm install -g @anthropic-ai/claude-code

# 설치 확인
claude-code --version

# 초기 설정
claude-code init
```

#### Gemini CLI
```bash
# pip를 통한 설치
pip install google-gemini-cli

# 또는 pipx 사용 (권장)
pipx install google-gemini-cli

# 설치 확인
gemini --version

# API 키 설정
gemini auth login
```

---

### 2.1 Filesystem MCP Server

**용도**: 로컬 파일 시스템 접근 및 관리

**설치 방법:**
```bash
# npm 설치
npm install -g @modelcontextprotocol/server-filesystem
```

**설정 방법:**

#### Claude Desktop 설정

**설정 파일 위치:**
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

**설정 파일 예시:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/Documents",
        "/Users/username/Projects"
      ]
    }
  }
}
```

#### Claude Code 설정

Claude Code는 터미널에서 직접 MCP 서버를 사용합니다.

**설정 파일 위치:**
- `~/.claude/claude_code_config.json`

**설정 파일 예시:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/username/projects"
      ]
    }
  }
}
```

**Claude Code 사용법:**
```bash
# Claude Code 설치
npm install -g @anthropic-ai/claude-code

# MCP 서버와 함께 Claude Code 실행
claude-code

# 특정 디렉토리에서 실행
claude-code --directory /path/to/project
```

#### Gemini CLI 설정

Google Gemini CLI에서도 MCP 프로토콜을 지원합니다.

**설정 파일 위치:**
- `~/.gemini/mcp_config.json`

**설정 파일 예시:**
```json
{
  "mcp": {
    "servers": {
      "filesystem": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-filesystem",
          "/home/username/documents"
        ],
        "env": {}
      }
    }
  }
}
```

**Gemini CLI 설치 및 사용:**
```bash
# Gemini CLI 설치
pip install google-gemini-cli

# 설정 파일 확인
gemini config show

# MCP 서버와 함께 실행
gemini chat --use-mcp

# 특정 MCP 서버만 활성화
gemini chat --mcp-server filesystem
```

**활용 예제:**
- 프로젝트 파일 구조 분석
- 코드 파일 읽기 및 수정 제안
- 문서 검색 및 내용 요약
- 로그 파일 분석

**작업 흐름:**
1. 특정 디렉토리 경로 설정
2. AI에게 파일 검색/분석 요청
3. 파일 내용 읽기 및 처리
4. 필요시 파일 생성/수정 제안

---

### 2.2 GitHub MCP Server

**용도**: GitHub 저장소와 이슈, PR 관리

**설치 방법:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**설정 방법:**

#### Claude Desktop 설정

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

#### Claude Code 설정

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

**환경 변수로 토큰 관리 (권장):**
```bash
# ~/.bashrc 또는 ~/.zshrc에 추가
export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_your_token_here"

# Claude Code 실행
claude-code
```

#### Gemini CLI 설정

```json
{
  "mcp": {
    "servers": {
      "github": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-github"
        ],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

**Gemini CLI 환경 변수 설정:**
```bash
# 환경 변수 설정
export GITHUB_TOKEN="ghp_your_token_here"

# Gemini CLI 실행
gemini chat --use-mcp --mcp-server github
```

**활용 예제:**
- 코드 리뷰 자동화
- 이슈 생성 및 관리
- PR 요약 및 변경사항 분석
- 커밋 히스토리 분석

**작업 흐름:**
1. GitHub Token 생성 및 설정
2. 저장소 지정
3. 이슈/PR 검색 및 분석
4. 코드 변경사항 리뷰
5. 자동 응답 또는 코멘트 생성

---

### 2.3 Google Drive MCP Server

**용도**: Google Drive 문서 접근 및 관리

**설치 방법:**
```bash
npm install -g @modelcontextprotocol/server-gdrive
```

**설정 방법:**

#### Claude Desktop 설정

```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-gdrive"
      ]
    }
  }
}
```

#### Claude Code 설정

```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-gdrive"
      ],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/path/to/credentials.json"
      }
    }
  }
}
```

#### Gemini CLI 설정

Gemini CLI는 Google 서비스와 네이티브 통합되므로 별도 MCP 서버 없이 Drive 접근이 가능합니다.

```json
{
  "mcp": {
    "servers": {
      "gdrive": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-gdrive"
        ]
      }
    }
  }
}
```

**Google OAuth 인증:**
```bash
# Claude Desktop/Code: 첫 실행 시 브라우저에서 인증
# Gemini CLI: 자동으로 Google 계정 사용
gemini auth login --enable-drive
```

**활용 예제:**
- 문서 검색 및 요약
- 스프레드시트 데이터 분석
- 프레젠테이션 내용 정리
- 팀 문서 통합 관리

**작업 흐름:**
1. Google OAuth 인증
2. 드라이브 문서 검색
3. 문서 내용 읽기
4. 데이터 분석 또는 요약
5. 결과 리포트 생성

---

### 2.4 Slack MCP Server

**용도**: Slack 메시지 검색 및 분석

**설치 방법:**
```bash
npm install -g @modelcontextprotocol/server-slack
```

**설정 방법:**

#### Claude Desktop 설정

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-slack"
      ],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token",
        "SLACK_TEAM_ID": "your-team-id"
      }
    }
  }
}
```

#### Claude Code 설정

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-slack"
      ],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
        "SLACK_TEAM_ID": "${SLACK_TEAM_ID}"
      }
    }
  }
}
```

**환경 변수 설정:**
```bash
# ~/.bashrc 또는 ~/.zshrc
export SLACK_BOT_TOKEN="xoxb-your-token"
export SLACK_TEAM_ID="your-team-id"
```

#### Gemini CLI 설정

```json
{
  "mcp": {
    "servers": {
      "slack": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-slack"
        ],
        "env": {
          "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
          "SLACK_TEAM_ID": "${SLACK_TEAM_ID}"
        }
      }
    }
  }
}
```

**Slack Bot Token 생성:**
1. https://api.slack.com/apps 접속
2. "Create New App" 클릭
3. Bot Token Scopes 설정:
   - `channels:history`
   - `channels:read`
   - `users:read`
   - `search:read`
4. Install to Workspace
5. Bot User OAuth Token 복사

**활용 예제:**
- 채널별 주요 논의사항 요약
- 특정 키워드 검색
- 미팅 노트 자동 생성
- 팀 커뮤니케이션 패턴 분석

**작업 흐름:**
1. Slack App 생성 및 Token 발급
2. 채널 또는 기간 지정
3. 메시지 검색 및 수집
4. 내용 분석 및 정리
5. 요약 리포트 생성

---

### 2.5 SQLite MCP Server

**용도**: SQLite 데이터베이스 쿼리 및 분석

**설치 방법:**
```bash
npm install -g @modelcontextprotocol/server-sqlite
```

**설정 방법:**

#### Claude Desktop 설정

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "/path/to/database.db"
      ]
    }
  }
}
```

**여러 데이터베이스 설정:**
```json
{
  "mcpServers": {
    "sqlite-main": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "/path/to/main.db"
      ]
    },
    "sqlite-analytics": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "/path/to/analytics.db"
      ]
    }
  }
}
```

#### Claude Code 설정

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "./data/app.db"
      ]
    }
  }
}
```

**프로젝트별 데이터베이스 설정:**
```bash
# 프로젝트 디렉토리의 .claude/config.json
{
  "mcpServers": {
    "project-db": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "./database.sqlite"
      ]
    }
  }
}
```

#### Gemini CLI 설정

```json
{
  "mcp": {
    "servers": {
      "sqlite": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-sqlite",
          "/home/username/data/database.db"
        ]
      }
    }
  }
}
```

**Gemini CLI 사용 예:**
```bash
# 특정 데이터베이스로 대화 시작
gemini chat --use-mcp --mcp-server sqlite

# 쿼리 실행 예시
gemini query --mcp sqlite "Show me all tables in the database"
```

**활용 예제:**
- 데이터베이스 스키마 분석
- 자연어로 SQL 쿼리 생성
- 데이터 트렌드 분석
- 데이터 품질 검사

**작업 흐름:**
1. 데이터베이스 파일 지정
2. 자연어로 데이터 질문
3. AI가 SQL 쿼리 생성
4. 쿼리 실행 및 결과 분석
5. 시각화 또는 인사이트 제공

---

**작성일**: 2025년 10월
**버전**: 1.0
**작성자**: MCP 프로젝트 팀
