**Claude Code 마켓플레이스 및 MCP 서버 설치/설정 방법**  
Claude Code는 플러그인 마켓플레이스를 통해 MCP 서버와 도구를 동적으로 확장할 수 있습니다1. 공식 마켓플레이스는 시작 시 자동으로 등록되며, 외부 마켓플레이스나 특정 플러그인을 설치할 때는 다음 명령어를 사용합니다.

* **마켓플레이스 추가:** /plugin marketplace add \<소유자/리포지토리\> 또는 Git URL을 입력하여 카탈로그를 등록합니다2, 3\.  
* **플러그인 설치:** /plugin install \<플러그인 이름\>@\<마켓플레이스\> 명령어를 사용하거나, 대화형 프롬프트에서 /plugin을 입력해 **Discover** 탭에서 선택하여 설치합니다1, 4, 5\.  
* **직접 서버 추가:** claude mcp add 명령어를 사용하면 대화형 마법사를 통해 전송 방식(HTTP, stdio 등)과 인증을 설정하며 서버를 추가할 수 있습니다6-8.

**주요 목적별 MCP 구성 방법**  
**1\. 이슈 트래커 (GitHub / Jira)**

* **GitHub:** 원격 HTTP 서버를 통해 연결하며, PR 관리 및 이슈 검색 도구를 제공합니다9, 10\.  
* claude mcp add \--transport http github https://api.githubcopilot.com/mcp/  
* **Jira (Atlassian):** Atlassian 공식 HTTP 전송 방식을 사용하거나, Docker 컨테이너를 통해 독립된 서버로 띄울 수 있습니다11, 12\. API 토큰과 이메일을 환경 변수로 설정해야 합니다13.  
* \# Docker 기반 Jira 서버 구성 예시  
* claude mcp add mcp-atlassian \--scope user \-- docker run \--rm \-i \--env-file $(realpath \~/.config/mcp-atlassian.env) ghcr.io/sooperset/mcp-atlassian:latest

**2\. Filesystem (로컬 파일 시스템 제어)**AI 에이전트가 로컬 파일에 접근하고 제어할 수 있도록 stdio 전송 방식을 사용합니다14, 15\. 보안을 위해 허용할 디렉토리 경로를 명시해야 접근이 제한됩니다16, 17\.  
claude mcp add \--transport stdio filesystem \-- npx \-y @modelcontextprotocol/server-filesystem /접근/허용할/디렉토리/경로  
**3\. CI/CD (CircleCI / GitLab)**

* **CircleCI:** 빌드 실패 로그 조회, 파이프라인 실행(run\_pipeline) 등의 도구를 활용할 수 있습니다18, 19\. CIRCLECI\_TOKEN 환경 변수가 필요합니다20.  
* **GitLab Pipelines:** MR 파이프라인 검토 및 재실행 도구를 지원하며, GITLAB\_PERSONAL\_ACCESS\_TOKEN과 GITLAB\_API\_URL 설정이 요구됩니다21, 22\.

**.mcp.json 및 .env를 활용한 설정값 템플릿화**  
팀원 간에 동일한 MCP 구성을 공유하기 위해 프로젝트 루트에 **.mcp.json** 파일을 생성하여 소스 제어(Git)에 포함시키는 것이 표준입니다23, 24\. 보안을 위해 API 키 같은 민감한 정보는 직접 하드코딩하지 않고, .env 파일에 정의된 변수를 ${VAR} 구문을 사용해 동적으로 매핑합니다25-27.  
**.env 파일 작성 (Git 무시 설정 필수):**  
\# .env  
GITHUB\_TOKEN=ghp\_your\_secret\_github\_token\_here  
CIRCLECI\_API\_KEY=your\_circleci\_secret\_key  
JIRA\_API\_TOKEN=your\_jira\_token  
**.mcp.json 템플릿 예시:**  
{  
  "mcpServers": {  
    "github": {  
      "command": "npx",  
      "args": \["-y", "@modelcontextprotocol/server-github"\],  
      "env": {  
        "GITHUB\_PERSONAL\_ACCESS\_TOKEN": "${GITHUB\_TOKEN}"  
      }  
    },  
    "circleci": {  
      "command": "npx",  
      "args": \["-y", "@circleci/mcp-server-circleci"\],  
      "env": {  
        "CIRCLECI\_TOKEN": "${CIRCLECI\_API\_KEY:-default\_value}"  
      }  
    }  
  }  
}  
이러한 템플릿을 구성하면 Claude Code가 런타임에 .env 파일을 읽어 ${VAR} 값을 실제 자격 증명으로 치환하여 실행하므로, 설정의 이식성과 보안성을 동시에 확보할 수 있습니다25, 26, 28\.  
