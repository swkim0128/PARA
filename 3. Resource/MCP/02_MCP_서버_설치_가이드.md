# MCP 서버 설치 가이드

## 📋 목차

1. [공식 MCP 서버 소개](#공식-mcp-서버-소개)
2. [필수 사전 준비](#필수-사전-준비)
3. [주요 MCP 서버 설치](#주요-mcp-서버-설치)
4. [서버별 상세 가이드](#서버별-상세-가이드)
5. [추가 MCP 서버](#추가-mcp-서버)
6. [Microsoft MCP 서버](#microsoft-mcp-서버)

---

## 공식 MCP 서버 소개

### 📦 공식 레포지토리

**GitHub**: https://github.com/modelcontextprotocol/servers

공식 MCP 서버들은 MCP 기능과 공식 SDK를 시연하기 위해 제공됩니다.

---

## 필수 사전 준비

### 시스템 요구사항

```bash
# Node.js 설치 확인 (v18 이상 필요)
node --version

# npm 설치 확인
npm --version
```

### Node.js 설치

```bash
# Mac (Homebrew)
brew install node

# Windows (Chocolatey)
choco install nodejs

# Linux (Ubuntu/Debian)
sudo apt install nodejs npm
```

---

## 주요 MCP 서버 설치

### 1. Everything Server 🌟

**설명**: 프롬프트, 리소스, 도구를 포함한 참조/테스트 서버

**GitHub**: https://github.com/modelcontextprotocol/servers/tree/main/src/everything

**설치**:
```bash
npm install -g @modelcontextprotocol/server-everything
```

**설정** (Claude Desktop):
```json
{
  "mcpServers": {
    "everything": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-everything"]
    }
  }
}
```

**주요 기능**:
- 모든 MCP 기능 시연 (Resources, Tools, Prompts)
- 테스트 및 개발용
- 프로토콜 이해를 위한 참조 구현

---

### 2. Filesystem Server 📁

**설명**: 안전한 파일 작업 및 접근 제어

**GitHub**: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem

**설치**:
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**설정** (Claude Desktop):
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/directory1",
        "/path/to/allowed/directory2"
      ]
    }
  }
}
```

**주요 기능**:
- 파일 읽기 및 쓰기
- 디렉토리 탐색
- 파일 검색
- 접근 제어 (허용된 디렉토리만)

**사용 예시**:
```
"내 프로젝트 폴더의 모든 Python 파일을 찾아줘"
"README.md 파일의 내용을 읽어줘"
"새로운 설정 파일을 생성해줘"
```

---

### 3. GitHub Server 🐙

**설명**: GitHub API 통합으로 저장소 관리 및 파일 작업

**GitHub**: https://github.com/github/github-mcp-server  
(이전: https://github.com/modelcontextprotocol/servers/tree/main/src/github)

**설치**:
```bash
npm install -g @modelcontextprotocol/server-github
```

**GitHub Personal Access Token 생성**:
1. GitHub 설정 → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token" 클릭
3. 필요한 권한 선택:
   - `repo` (전체 저장소 접근)
   - `read:user` (사용자 정보 읽기)
4. 토큰 복사 (한 번만 표시됨!)

**설정** (Claude Desktop):
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

**주요 기능**:
- 파일 읽기/쓰기/업데이트
- 브랜치 관리 (자동 브랜치 생성)
- Pull Request 생성 및 관리
- 이슈 검색 및 생성
- 코드 검색
- 저장소 관리

**사용 예시**:
```
"내 저장소의 최근 이슈 10개를 보여줘"
"main.py 파일을 읽어줘"
"새로운 기능 브랜치를 만들고 파일을 업데이트해줘"
"PR을 생성해줘"
```

---

### 4. Memory Server 🧠

**설명**: 지식 그래프 기반 영구 메모리 시스템

**GitHub**: https://github.com/modelcontextprotocol/servers/tree/main/src/memory

**설치**:
```bash
npm install -g @modelcontextprotocol/server-memory
```

**설정** (Claude Desktop):
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

**주요 기능**:
- 지식 그래프 저장
- 엔티티 관계 관리
- 영구 메모리 유지
- 대화 컨텍스트 저장

**사용 예시**:
```
"내가 좋아하는 프로그래밍 언어로 Python을 기억해줘"
"지난주에 논의했던 프로젝트에 대해 알려줘"
"John이 선호하는 작업 방식을 저장해줘"
```

---

### 5. Fetch Server 🌐

**설명**: 웹 콘텐츠 가져오기 및 LLM용 변환

**GitHub**: https://github.com/modelcontextprotocol/servers/tree/main/src/fetch

**설치**:
```bash
npm install -g @modelcontextprotocol/server-fetch
```

**설정** (Claude Desktop):
```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    }
  }
}
```

**주요 기능**:
- 웹 페이지 가져오기
- HTML을 마크다운으로 변환
- PDF 내용 추출
- 효율적인 LLM 컨텍스트 생성

**사용 예시**:
```
"https://example.com의 내용을 가져와서 요약해줘"
"이 문서 URL의 주요 포인트를 추출해줘"
```

---

### 6. Git Server 🔧

**설명**: Git 저장소 읽기, 검색, 조작 도구

**GitHub**: https://github.com/modelcontextprotocol/servers/tree/main/src/git

**설치**:
```bash
npm install -g @modelcontextprotocol/server-git
```

**설정** (Claude Desktop):
```json
{
  "mcpServers": {
    "git": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-git"]
    }
  }
}
```

**주요 기능**:
- Git 히스토리 조회
- 브랜치 관리
- 커밋 정보 검색
- Diff 분석

---

### 7. Sequential Thinking Server 🤔

**설명**: 사고 순서를 통한 동적이고 반성적인 문제 해결

**GitHub**: https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking

**설치**:
```bash
npm install -g @modelcontextprotocol/server-sequentialthinking
```

**설정** (Claude Desktop):
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequentialthinking"]
    }
  }
}
```

**주요 기능**:
- 단계별 사고 과정 추적
- 문제 해결 단계 기록
- 사고 흐름 분석

---

### 8. Time Server ⏰

**설명**: 시간 및 시간대 변환 기능

**GitHub**: https://github.com/modelcontextprotocol/servers/tree/main/src/time

**설치**:
```bash
npm install -g @modelcontextprotocol/server-time
```

**설정** (Claude Desktop):
```json
{
  "mcpServers": {
    "time": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-time"]
    }
  }
}
```

**주요 기능**:
- 현재 시간 조회
- 시간대 변환
- 시간 계산

---

## 추가 MCP 서버

### 공식 통합 서버

#### Slack Server 💬
**GitHub**: https://github.com/modelcontextprotocol/servers

```bash
npm install -g @modelcontextprotocol/server-slack
```

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token",
        "SLACK_TEAM_ID": "your-team-id"
      }
    }
  }
}
```

**주요 기능**:
- 채널 관리
- 메시지 전송 및 검색
- 사용자 정보 조회

---

#### Google Maps Server 🗺️
```bash
npm install -g @modelcontextprotocol/server-googlemaps
```

```json
{
  "mcpServers": {
    "googlemaps": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-googlemaps"],
      "env": {
        "GOOGLE_MAPS_API_KEY": "your_api_key"
      }
    }
  }
}
```

**주요 기능**:
- 위치 서비스
- 경로 찾기
- 장소 세부 정보

---

#### Puppeteer Server 🤖
**GitHub**: https://github.com/modelcontextprotocol/servers

```bash
npm install -g @modelcontextprotocol/server-puppeteer
```

**주요 기능**:
- 브라우저 자동화
- 웹 스크래핑
- 스크린샷 캡처
- 폼 자동 입력

---

### 커뮤니티 서버

공식 커뮤니티 레지스트리에서 더 많은 서버를 찾을 수 있습니다:

**MCP Registry**: https://github.com/modelcontextprotocol/registry

주요 서버:
- **Atlassian**: Jira 및 Confluence 통합
- **Box**: Intelligent Content Management
- **BrowserStack**: 테스트 플랫폼 접근
- **Buildkite**: CI/CD 파이프라인 관리
- **Auth0**: 인증 및 권한 관리

---

## Microsoft MCP 서버

Microsoft는 Azure 및 Microsoft 365 서비스를 위한 공식 MCP 서버를 제공합니다.

**GitHub**: https://github.com/microsoft/mcp

### 주요 Microsoft MCP 서버

#### 1. Azure MCP Server ☁️
**설명**: Azure 서비스와의 통합

**주요 기능**:
- Azure AI Foundry
- Azure DevOps
- Fabric RTI 서비스
- Azure 리소스 관리

#### 2. Microsoft 365 MCP Server 📊
**설명**: Microsoft 365 및 Copilot 통합

**주요 기능**:
- Microsoft 365 앱 및 에이전트 구축
- Microsoft 365 Copilot 통합
- SharePoint, Teams 등 접근

#### 3. SQL Server MCP Server 🗄️
**설명**: SQL 데이터베이스와의 자연어 대화

**주요 기능**:
- 자연어 쿼리
- 테이블 스키마 관리
- CRUD 작업

#### 4. NuGet MCP Server 📦
**설명**: NuGet 패키지 관리

**주요 기능**:
- 패키지 검색
- 버전 관리
- 의존성 분석

#### 5. Markdown MCP Server 📝
**설명**: Markdown 처리 및 조작

**주요 기능**:
- Markdown 파싱
- 포맷 변환
- 콘텐츠 변환

---

## 설치 확인 방법

### MCP Inspector 사용

```bash
# MCP Inspector 설치
npm install -g @modelcontextprotocol/inspector

# 서버 테스트
npx @modelcontextprotocol/inspector
```

### Claude Desktop에서 확인

1. Claude Desktop 재시작
2. 새 대화 시작
3. MCP 도구가 활성화되었는지 확인
4. 테스트 명령 실행:
   ```
   "사용 가능한 도구 목록을 보여줘"
   ```

---

## 문제 해결

### 일반적인 문제

#### 1. 서버가 시작되지 않음
```bash
# Node.js 버전 확인
node --version  # v18 이상이어야 함

# 캐시 정리
npm cache clean --force

# 재설치
npm install -g @modelcontextprotocol/server-[name]
```

#### 2. 인증 오류

**GitHub Token**:
- 토큰이 만료되지 않았는지 확인
- 필요한 권한(`repo`, `read:user`)이 있는지 확인
- 환경 변수가 올바르게 설정되었는지 확인

**Slack Token**:
- Bot Token Scopes 확인:
  - `channels:history`
  - `channels:read`
  - `users:read`
  - `search:read`

#### 3. 경로 문제 (Filesystem Server)

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/absolute/path/to/directory"  // 절대 경로 사용
      ]
    }
  }
}
```

---

## 다음 단계

1. ✅ 필요한 MCP 서버 설치
2. ⬜ 설정 파일 구성
3. ⬜ 인증 정보 설정
4. ⬜ Claude Desktop 재시작
5. ⬜ 서버 연결 테스트
6. ⬜ 실제 워크플로우에 적용

---

## 참고 자료

### 공식 문서
- **MCP 서버 레포지토리**: https://github.com/modelcontextprotocol/servers
- **MCP 레지스트리**: https://github.com/modelcontextprotocol/registry
- **Microsoft MCP**: https://github.com/microsoft/mcp
- **MCP 공식 사이트**: https://modelcontextprotocol.io

### 커뮤니티
- **GitHub Discussions**: https://github.com/modelcontextprotocol/specification/discussions
- **Discord**: modelcontextprotocol.io/community

### SDK
- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk
- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk
- **C# SDK**: https://github.com/modelcontextprotocol/csharp-sdk

---

**작성일**: 2025년 10월 11일  
**버전**: 1.0  
**최종 업데이트**: GitHub 서버 이전 반영 (github/github-mcp-server)
