# Claude Code 및 Copilot CLI 기반 개발 자동화 가이드라인

## 1\. 도입 개요 및 기대 효과

본 가이드라인은 팀 내 개발자들이 대규모 컨텍스트 기반 추론에 강한 **Claude Code**와 빠른 터미널 실행 및 테스트에 강한 **GitHub Copilot CLI**를 교차 활용하여 소프트웨어 개발 생명주기(SDLC)를 자동화할 수 있도록 돕기 위해 작성되었습니다.

* **Claude Code의 강점:** 최대 100만 토큰의 컨텍스트 창을 지원하여 리포지토리 전체의 아키텍처를 이해하고, 다수 파일에 걸친 복잡한 로직 설계 및 리팩토링을 주도하는 '추론 우선형(Reasoning-first)' 에이전트입니다1-3.  
* **Copilot CLI의 강점:** 터미널 네이티브 환경에서 짧은 지연 시간(Low-latency)으로 명령을 실행하고, 유닛 테스트 반복 및 에러 로그 분석을 통한 즉각적인 디버깅을 수행하는 '실행 우선형(Execution-first)' 에이전트입니다3-5.

**기대 효과:**

* **생산성 극대화:** 인간 개발자는 기획 및 리뷰에 집중하고, 단순 반복적인 코드 작성, 테스트 생성, PR 초안 작성 등은 AI가 전담합니다2, 6\.  
* **문맥 전환(Context Switching) 최소화:** IDE, 터미널, 브라우저(Jira/GitHub)를 오가는 시간을 줄이고 터미널 내에서 모든 작업을 완수합니다7.  
* **고품질 코드 유지:** Claude의 다중 파일 분석과 Copilot의 즉각적인 런타임 테스트가 상호 보완되어 결함 발생률을 낮춥니다6.

## 2\. 사전 준비 (설치 및 인증)

두 에이전트를 원활하게 구동하기 위해 적절한 런타임 환경과 터미널 설정이 필요합니다.  
**1\) 시스템 요구사항**

* **Node.js:** Claude Code는 **v18.0.0 이상**, GitHub Copilot CLI는 **v22.0.0 이상**이 필수입니다8. (두 도구를 함께 쓰려면 v22 이상 설치를 권장합니다).  
* **Windows 사용자 필수:** Claude Code는 내부적으로 Unix 계열의 명령어를 사용하므로 **Git for Windows(Git Bash)** 설치가 반드시 필요합니다9, 10\.

**2\) Claude Code 설치 및 인증**  
\# 글로벌 설치 (네이티브 스크립트 권장)  
curl \-fsSL https://claude.ai/install.sh | bash

\# 또는 npm 사용 시  
npm install \-g @anthropic-ai/claude-code

\# 인증 (실행 시 자동으로 브라우저가 열리며 인증 진행)  
claude

* 설치 및 인증 완료 후 claude doctor 명령어를 통해 정상 작동 여부를 점검할 수 있습니다11, 12\.

**3\) GitHub Copilot CLI 설치 및 인증**  
\# npm을 통한 설치  
npm install \-g @github/copilot

\# 인증 (GitHub 자격 증명 사용)  
copilot auth login

## 3\. 공통 환경 설정 (MCP 및 설정 파일 템플릿)

AI 에이전트가 우리 팀의 프로젝트 컨텍스트와 외부 시스템(GitHub, Jira 등)을 이해할 수 있도록 환경을 세팅합니다.  
**1\) CLAUDE.md 작성 (프로젝트 컨텍스트 공유)**프로젝트 루트 디렉토리에 CLAUDE.md 파일을 생성하면, Claude Code가 매 세션마다 이 파일을 읽어 팀의 코딩 컨벤션과 명령어 규칙을 학습합니다13, 14\.  
\# 프로젝트 개요  
이 프로젝트는 React와 Node.js로 구성된 e-commerce 앱입니다.

\# 코딩 규칙  
\- 모든 비동기 작업은 Promise 대신 async/await을 사용하세요.  
\- 컴포넌트는 Functional Component로 작성하세요.

\# 자주 사용하는 명령어  
\- 개발 서버 실행: \`npm run dev\`  
\- 테스트 실행: \`npm run test\`  
**2\) .env 및 .mcp.json 설정 템플릿**팀원 간 MCP 구성을 공유하기 위해 프로젝트 루트에 .mcp.json을 추가하고 버전 관리에 포함시킵니다15, 16\. 민감한 API 키는 .env 파일에 분리하여 보안을 유지합니다17.  
**.env (반드시 .gitignore에 추가):**  
GITHUB\_TOKEN=your\_github\_personal\_access\_token  
JIRA\_API\_TOKEN=your\_jira\_token  
**.mcp.json (버전 관리 포함):**  
{  
  "mcpServers": {  
    "github": {  
      "command": "npx",  
      "args": \["-y", "@modelcontextprotocol/server-github"\],  
      "env": {  
        "GITHUB\_PERSONAL\_ACCESS\_TOKEN": "${GITHUB\_TOKEN}"  
      }  
    },  
    "jira": {  
      "command": "npx",  
      "args": \["-y", "@modelcontextprotocol/server-jira"\],  
      "env": {  
        "JIRA\_API\_TOKEN": "${JIRA\_API\_TOKEN}"  
      }  
    }  
  }  
}

## 4\. 단계별 실행 가이드 (이슈 생성부터 배포, 문서 동기화까지)

### Step 1: 지능형 이슈 생성 (Claude Code)

기획 단계의 문서나 회의록을 바탕으로 Claude Code와 연결된 Jira/GitHub MCP를 사용하여 작업을 정형화합니다18.  
claude "업로드된 기획 문서(feature\_spec.pdf)를 분석해서 현재 코드베이스에 맞게 GitHub에 OAuth2 모듈 구현을 위한 이슈를 생성해 줘."

* **작동 방식:** Claude가 MCP를 통해 create\_issue 도구를 호출하여, 라벨과 마일스톤이 포함된 상세한 이슈를 자동 생성합니다18, 19\.

### Step 2: 소스 분석 및 자율적 기능 구현 (Claude Code)

광범위한 파일 검색과 논리적 설계가 필요한 실제 기능 구현은 100만 토큰의 컨텍스트를 가진 Claude Code가 주도합니다3.  
claude "이슈 \#45를 해결하기 위해 OAuth2 모듈을 구현해. 먼저 계획(Plan)을 제시하고 내가 승인하면 코드를 수정해 줘."

* **작동 방식:** Claude가 Glob, Read 도구로 코드를 분석한 뒤 Plan 모드로 진입하여 변경 계획을 제안합니다20, 21\. 검토 후 승인하면 Edit 도구를 통해 코드를 작성합니다21.

### Step 3: 고정밀 테스트 및 검증 (GitHub Copilot CLI)

기능 구현 후, 터미널 로그 분석과 빠른 에러 수정(Self-correction)에 강한 Copilot CLI를 호출합니다6.  
copilot  
\# 대화형 프롬프트 진입 후  
/tests "방금 구현된 OAuth2 모듈에 대한 유닛 테스트를 생성하고 실행해 줘."

\# 에러 발생 시  
/fixTestFailure "테스트 실패 에러 로그를 분석하고 즉석에서 코드를 수정해 줘."

* **작동 방식:** Copilot CLI의 Task 에이전트가 테스트를 실행하며, 실패 로그를 실시간으로 분석해 코드를 즉각적으로 수정합니다5, 22\.

### Step 4: 전략적 Git 반영 및 풀 리퀘스트(PR) 생성

테스트를 통과하면 변경 사항을 요약하여 PR을 생성합니다. Claude Code가 Diff를 읽어 고품질의 설명을 작성합니다23.  
claude /commit  
claude /pr

* **작동 방식:** 변경된 코드를 분석해 Conventional Commits에 맞는 메시지를 작성하고, 템플릿에 맞춘 초안 PR(Draft PR)을 생성합니다19, 23\. 이후 설정된 CI/CD에 따라 배포 파이프라인이 구동됩니다.

### Step 5: 문서 동기화 및 지식 베이스 업데이트 (Claude Code)

작업이 끝난 후, 다음 세션이나 다른 팀원이 참고할 수 있도록 프로젝트 문서를 최신 상태로 유지합니다24.  
claude "새로 추가된 환경 변수와 OAuth2 인증 플로우의 변경 사항을 README.md와 CLAUDE.md에 업데이트해 줘."

* 필요 시 /compact 명령어를 사용해 이번 세션에서 중요했던 공학적 결정만 기억하도록 메모리를 압축합니다24.

## 5\. 자주 묻는 질문(FAQ) 또는 트러블슈팅 가이드

**Q1. Windows에서 claude 실행 시 "Claude Code on Windows requires git-bash" 에러가 발생합니다.**

* **A:** 시스템 환경 변수(PATH)에 Git Bash 경로가 올바르게 지정되지 않아서 발생합니다. PowerShell이나 터미널 환경 변수에 CLAUDE\_CODE\_GIT\_BASH\_PATH=C:\\Program Files\\Git\\bin\\bash.exe를 직접 등록한 후 터미널을 재시작하세요25, 26\.

**Q2. npm 전역 설치 시 EACCES(권한 거부) 에러가 발생하여 설치가 안 됩니다.**

* **A:** 시스템의 글로벌 모듈 디렉토리에 쓰기 권한이 부족하여 발생합니다. sudo를 사용하지 마시고, mkdir \~/.npm-global로 사용자 디렉토리를 만든 뒤, npm config set prefix '\~/.npm-global'을 적용하세요. 이후 \~/.bashrc 또는 \~/.zshrc에 export PATH=\~/.npm-global/bin:$PATH를 추가합니다27, 28\.

**Q3. Claude가 민감한 .env 파일을 자꾸 수정하거나 로그에 노출하려고 합니다.**

* **A:** 보안 설정을 통해 접근을 원천 차단해야 합니다. 프로젝트 폴더의 .claude/settings.json 파일 내 permissions.deny 배열에 ".env" 및 ".git/" 경로를 추가하면 파일 시스템 접근을 거부할 수 있습니다29, 30\.

**Q4. 대규모 작업을 하다 보니 "Context too large" 에러가 자주 나타납니다.**

* **A:** 세션이 길어져 컨텍스트 창이 가득 찬 경우입니다. /compact 명령어를 사용해 이전 대화를 요약 압축하여 공간을 확보하거나, 전혀 다른 태스크로 전환할 때는 /clear 명령어를 통해 깨끗한 세션에서 다시 시작하는 것이 좋습니다31-33.

**Q5. Claude Code와 Copilot CLI를 어떻게 구분해서 써야 할지 헷갈립니다.**

* **A:** 도구의 목적이 다릅니다. **다수의 파일이 얽힌 아키텍처 변경, 새로운 프레임워크 도입, 전체 시스템 파악** 등 넓은 범위의 '설계 및 구현'은 Claude Code에 맡기세요2, 34, 35\. 반면, **현재 열려 있는 파일의 빠른 로직 수정, 유닛 테스트 작성, 빌드 에러 및 터미널 에러 로그의 실시간 디버깅** 등 짧고 반복적인 '실행' 단계에서는 Copilot CLI를 사용하는 것이 효율적입니다4, 35\.

