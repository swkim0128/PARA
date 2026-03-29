# AI 기반 개발 자동화 파이프라인 공식 매뉴얼

## 1\. 개요 및 파이프라인 아키텍처

본 매뉴얼은 팀 내 개발자들이 기획 단계부터 실제 코드 구현, 테스트, 그리고 배포 및 문서 동기화까지의 전 과정을 인공지능 에이전트를 통해 자동화할 수 있도록 지원하는 공식 가이드입니다. 터미널 환경을 벗어나지 않고도 외부 도구(GitHub, 파일시스템, CI/CD 등)를 제어하여 **문맥 전환(Context Switching)을 최소화**하고 **생산성과 코드 품질을 극대화**하는 것을 목적으로 합니다 1, 2\.  
이 파이프라인은 두 가지 핵심 AI 도구의 강점을 결합한 하이브리드 아키텍처로 구성되어 있습니다:

* **Claude Code CLI:** 최대 100만 토큰의 문맥(Context)을 바탕으로 프로젝트 전체의 아키텍처를 이해하고, 복잡한 논리적 수정이나 다중 파일 리팩토링, 기획 및 설계 등 **'추론 우선형(Reasoning-first)' 작업**을 주도합니다 3, 4\. MCP(Model Context Protocol)를 통해 이슈 트래커와 파일 시스템 등 외부 환경을 직접 제어합니다 5\.  
* **GitHub Copilot CLI:** 터미널 네이티브 환경에서 즉각적인 명령 제안과 테스트 코드 생성, 빌드 에러 및 실패한 테스트의 실시간 로그 분석 등 **'실행 우선형(Execution-first)' 작업**에 특화되어 빠르고 정밀한 검증을 담당합니다 3, 6\.

## 2\. 사전 준비 및 설치 가이드 (Prerequisites & Installation)

도구를 원활하게 실행하기 위해 시스템 환경을 준비하고, 각 CLI를 설치 및 인증해야 합니다.  
**시스템 환경 요구사항**

* **Node.js:** GitHub Copilot CLI의 원활한 실행을 위해 **v22.0.0 이상** (LTS 권장) 설치가 필수적입니다 7\.  
* **운영체제 (Windows):** Windows 환경에서 Claude Code를 구동하려면 내부적으로 Unix 계열 명령어를 처리하기 위해 반드시 **Git for Windows (Git Bash)** 또는 WSL2가 설치되어 있어야 합니다 7, 8\.

**Claude Code CLI 설치 및 인증**  
\# macOS, Linux, WSL 환경의 네이티브 설치 (자동 업데이트 지원)  
curl \-fsSL https://claude.ai/install.sh | bash

\# Windows PowerShell 환경 설치  
irm https://claude.ai/install.ps1 | iex

\# 인증: 명령어 실행 시 브라우저가 열리며 Anthropic 계정 연동  
claude auth login

* 설치 후 claude doctor 명령어를 입력하여 정상 작동 여부와 시스템 환경을 점검할 수 있습니다 9\.

**GitHub Copilot CLI 설치 및 인증**  
\# npm을 통한 글로벌 설치  
npm install \-g @github/copilot

\# 인증: 디바이스 플로우를 통해 GitHub 인증 진행  
copilot auth login

* 터미널에 표시된 8자리 코드를 복사하여 브라우저의 GitHub 디바이스 인증 페이지에 입력합니다 10\.

## 3\. 공통 환경 및 마켓플레이스 설정 (Configuration)

Claude Code가 외부 서비스에 접근할 수 있도록 표준 프로토콜인 MCP(Model Context Protocol) 서버를 구성해야 합니다 5\. 팀원 간 일관된 환경을 유지하기 위해 루트 디렉토리에 .mcp.json과 .env 파일을 템플릿화하여 사용합니다.  
**필수 MCP 서버 설치 명령어**  
\# 1\. Issue Tracker (GitHub) \- 이슈 검색, 생성, PR 자동화 지원  
claude mcp add github \-- npx \-y @modelcontextprotocol/server-github

\# 2\. Filesystem \- 허용된 로컬 디렉토리의 파일 접근 및 제어  
claude mcp add fs \-- npx \-y @modelcontextprotocol/server-filesystem /프로젝트/절대경로

\# 3\. CI/CD (CircleCI 예시) \- 파이프라인 모니터링 및 빌드 에러 로그 접근  
claude mcp add circleci \-- npx \-y @circleci/mcp-server-circleci  
**환경 설정 템플릿 (.env 및 .mcp.json)**  
보안을 위해 민감한 키 값은 .env에 저장하고 (Git 무시 설정 필수), 팀원 간 공유할 서버 설정은 .mcp.json에 정의하여 ${VAR} 형태로 동적 매핑합니다 11\.  
.env (각 개발자 로컬 환경에 생성):  
\# GitHub Personal Access Token (repo, project 권한 포함)  
GITHUB\_PERSONAL\_ACCESS\_TOKEN=ghp\_your\_github\_token\_here

\# CI/CD (CircleCI) API Token  
CIRCLECI\_TOKEN=your\_circleci\_token\_here  
.mcp.json (프로젝트 루트에 생성 후 Git 커밋):  
{  
  "mcpServers": {  
    "github": {  
      "command": "npx",  
      "args": \["-y", "@modelcontextprotocol/server-github"\],  
      "env": {  
        "GITHUB\_PERSONAL\_ACCESS\_TOKEN": "${GITHUB\_PERSONAL\_ACCESS\_TOKEN}"  
      }  
    },  
    "circleci": {  
      "command": "npx",  
      "args": \["-y", "@circleci/mcp-server-circleci"\],  
      "env": {  
        "CIRCLECI\_TOKEN": "${CIRCLECI\_TOKEN}"  
      }  
    }  
  }  
}

## 4\. 단계별 운용 가이드 (Step-by-Step Operation)

### Phase 1 기획 및 이슈 관리

* **작업이슈 생성:** 요구사항을 분석하여 GitHub에 새로운 개발 이슈를 등록합니다.  
* claude "새로운 결제 모듈 기능 추가와 관련된 요구사항을 분석하고, GitHub에 '결제 모듈 연동'이라는 제목의 이슈를 생성해 줘."  
* **작업이슈 문서 작성:** 생성된 이슈를 바탕으로 로컬에 상세 명세서를 작성합니다.  
* claude "방금 생성한 GitHub 이슈의 번호와 내용을 참조하여, docs/payment\_spec.md 파일에 작업 상세 명세서를 작성해 줘."  
* **작업이슈 동기화:** 새 명세서의 컨텍스트를 프로젝트 전역 지침 파일에 동기화합니다.  
* claude "payment\_spec.md의 핵심 변경 예정 사항을 분석하고, 이를 CLAUDE.md 프로젝트 컨텍스트에 업데이트해 줘."  
* **작업 요구사항 분석:** 구현에 앞서 기존 소스 아키텍처와의 의존성을 분석합니다.  
* claude "결제 모듈을 구현하기 위해 수정이 필요한 기존 소스 파일(src/ 하위)과 의존성을 분석하고 구현 계획(Plan)을 브리핑해 줘."

### Phase 2 개발 및 테스트

* **개발 소스 분석:** 수립된 계획에 맞춰 코드를 심층 탐색합니다.  
* claude "제시한 구현 계획에 따라 관련된 기존 서비스 및 컨트롤러 파일을 읽고(Read), 수정할 위치를 정확히 파악해 줘."  
* **소스 작업:** 실제 기능 구현 로직을 자율적으로 작성합니다.  
* claude "분석을 바탕으로 결제 모듈 기능을 구현하는 새로운 코드를 작성하고 파일에 저장해(Edit). 보안 규칙과 기존 스타일 가이드를 반드시 준수해."  
* **기능 테스트 (Copilot CLI 활용):** Copilot CLI로 전환하여 터미널 환경에서 빠르고 정밀하게 유닛 테스트를 생성하고 에러를 수정합니다 6\.  
* copilot  
* \# 인터렉티브 모드 진입 후  
* /tests "방금 구현한 결제 모듈에 대한 유닛 테스트 코드를 생성하고 'npm run test' 명령어로 실행해 줘."  
* \# 테스트가 실패할 경우, 자율 수정 명령 하달  
* /fixTestFailure "테스트 실패 로그를 분석하고 실패한 부분을 수정해 줘."

### Phase 3 버전 관리 및 배포

* **Git 작업 반영:** 다시 Claude Code로 돌아와, 수정된 코드를 스테이징하고 커밋을 생성합니다.  
* claude /commit "기능 구현 및 테스트 통과를 확인했어. 변경된 모든 파일을 분석해서 Conventional Commits 규격에 맞는 커밋 메시지를 작성하고 커밋해 줘."  
* **배포 작업:** 반영된 브랜치를 푸시하고 PR(Pull Request)을 생성합니다.  
* claude /pr "현재 커밋된 내용과 관련된 작업이슈 번호를 포함하여, main 브랜치로 병합하기 위한 풀 리퀘스트(PR) 초안을 작성하고 생성해 줘."  
* **배포 (CI/CD 연동):** 연결된 CI/CD MCP를 통해 빌드 상태를 모니터링하고 배포 파이프라인을 실행합니다.  
* claude "방금 생성한 PR에 대해 CircleCI 빌드가 정상적으로 완료되었는지 확인하고, 성공했다면 파이프라인 실행을 진행해 줘."

### Phase 4 사후 처리

* **작업이슈 문서 수정:** 최종적으로 구현된 내용을 바탕으로 명세 문서를 최신화합니다.  
* claude "실제 코딩 과정에서 PR에 포함된 변경 사항(예: 추가된 환경 변수 등)을 반영하여 docs/payment\_spec.md를 수정해 줘."  
* **작업이슈 문서 동기화:** 프로젝트 전반의 문서 최신화 및 완료된 이슈를 닫습니다.  
* claude "최종적으로 README.md의 실행 가이드를 업데이트하고, GitHub에 열려 있는 작업 이슈를 '완료(Closed)' 처리해 줘."

## 5\. 트러블슈팅 및 팁 (FAQ)

**Q1. command not found: claude 또는 claude를 인식할 수 없다는 에러가 발생합니다.**

* **해결책:** 설치 후 실행 파일의 디렉토리가 시스템의 PATH 환경 변수에 제대로 등록되지 않아 발생합니다. macOS/Linux의 경우 터미널을 재시작하거나 \~/.local/bin (또는 설치 시 안내된 경로)을 .bashrc 또는 .zshrc에 추가하세요 12, 13\.

**Q2. Windows에서 "Claude Code on Windows requires git-bash" 에러가 발생합니다.**

* **해결책:** Claude Code는 내부적으로 쉘 명령을 구동하기 위해 Git Bash가 필요합니다. Windows 시스템 환경 변수에 CLAUDE\_CODE\_GIT\_BASH\_PATH 키를 생성하고, 값으로 Git Bash 실행 파일 경로(예: C:\\Program Files\\Git\\bin\\bash.exe)를 명시적으로 설정한 뒤 터미널을 다시 여세요 14, 15\.

**💡 AI 도구 활용을 위한 개발자 팁 (컨텍스트 관리)**

* **CLAUDE.md의 적극 활용:** 프로젝트 루트에 생성한 CLAUDE.md는 에이전트의 영구적인 기억 장치입니다. 프로젝트의 네이밍 규칙, 주로 사용하는 빌드 및 테스트 명령어 등을 적어두면 매번 지시할 필요가 없습니다 16\.  
* **긴 세션에서의 토큰 절약 (/compact 및 /clear):** 긴 시간 동안 대화를 나누어 에이전트의 컨텍스트 창이 꽉 차면 비용과 속도에 악영향을 미칩니다. 대화 내용이 충분히 전개되었다면 /compact 명령어로 현재까지의 중요 문맥을 압축하거나, 새로운 태스크를 시작할 때는 /clear를 입력해 깔끔한 세션에서 다시 시작하는 것이 좋습니다 17, 18\.

