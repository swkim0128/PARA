# 개발자를 위한 MCP 추천(5) - Shrimp Task Manager MCP 설치 및 사용방법(claude code 사용 예시)

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcDVwhU%2FbtsPX2gV1cR%2FAAAAAAAAAAAAAAAAAAAAAPJj5eCkNfrT0rGbLkiWrI2q_voQMtqc5I5lIhCeuHYu%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1764514799%26allow_ip%3D%26allow_referer%3D%26signature%3DV%252BRLJOHdm3jLSCk9G6tiT1VUnxo%253D)

## Metadata
- Author: [[갓대희]]
- Full Title: 개발자를 위한 MCP 추천(5) - Shrimp Task Manager MCP 설치 및 사용방법(claude code 사용 예시)
- Category: #articles
- Document Tags:  #mcp 
- Summary: 저자는 React로 새 todo 리스트 웹을 만들며 Shrimp Task Manager를 실제 시나리오로 설명합니다. Filesystem MCP를 연동해 특정 경로의 prd 파일을 읽어 개발과 연구에 활용합니다. 글에는 Shrimp 설치와 사용 예시(claude code 포함)가 담겨 있습니다.
- URL: https://goddaehee.tistory.com/394

## Full Document
안녕하세요! 갓대희 입니다. :- )

오늘은 개발자를 위한 MCP 시리즈의 새로운 글로 **"Shrimp Task Manager"**에 대해 써보려고 한다.

![](https://blog.kakaocdn.net/dna/cDVwhU/btsPX2gV1cR/AAAAAAAAAAAAAAAAAAAAAPJj5eCkNfrT0rGbLkiWrI2q_voQMtqc5I5lIhCeuHYu/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=V%2BRLJOHdm3jLSCk9G6tiT1VUnxo%3D)
개발을 하다 보면 복잡한 태스크를 체계적으로 관리하는 게 얼마나 중요한지 느낄 때가 많다. 특히 AI와 함께 작업할 때는 더욱 그렇다. 이럴때 도움이 될 수 있는 Shrimp Task Manager MCP에 대해 작성하려고 한다.

##### **Shrimp Task Manager란?**

**Shrimp Task Manager MCP (이하 Shrimp MCP)**는 Model Context Protocol (MCP) 기반으로 만들어진 AI 에이전트 전용 작업 관리 도구이다. AI 에이전트가 체계적인 워크플로우를 따라 작업을 수행하도록 돕는 **지능형 작업 관리 시스템**이다.

AI 코딩 에이전트가 프로젝트를 이해하고 스스로 개발 작업을 계획하고, 실행할 수 있도록 돕는 “**프로젝트 매니저(Project Manager)**” 역할을 수행한다. 단순한 체크리스트형 툴이 아니라, 에이전트가 개발자처럼 사고하며 체계적으로 프로젝트를 진행할 수 있도록 설계되어있다.

Shrimp Task Manager는 AI 에이전트를 위한 지능형 태스크 관리 시스템으로, chain-of-thought 추론과 의존성 추적에 특화되어 있다. 다음과 같은 특징이 있다.

###### **핵심 기능 리스트**

* **지능형 태스크 분해**: 복잡한 작업을 자동으로 관리 가능한 단위로 분할
* **의존성 관리**: 태스크 간 종속성을 정확히 파악하고 올바른 실행 순서 보장
* **실시간 상태 추적**: 태스크 실행 진행률과 상태를 실시간 모니터링
* **태스크 메모리 기능**: 과거 태스크 히스토리를 자동 백업해 장기 메모리 제공
* **연구 모드**: 기술 조사와 베스트 프랙티스 탐색을 위한 체계적 워크플로우

#### **다른 태스크 관리 도구와의 차이점** 🔍

Shrimp Task Manager와 자주 비교되는 도구로 Task Master MCP가 있다. (Task Master 하기 참고 )

둘 다 AI 기반 작업 관리 도구이지만 접근 방식에 차이가 있어서 알아두면 좋다.

**Shrimp의 장점**  

외부 API 없이도 Cursor IDE나 Claude Desktop의 내장 AI를 그대로 활용할 수 있어서 설정이 간편하고 추가 비용이 들지 않는다. 또한 현재 프로젝트 상황을 파악해서 현실적인 태스크를 만들어준다.

##### **설치 방법 🛠️**

##### 필수 조건

설치 방법이 여러 가지 있는데, 기존 내가 진행하던 방식을 활용해서 진행해보자.

**방법1.** Smithery를 이용한 방법이 사실가장 간단하긴 한것 같다. **나는 **방법2로 진**행 예정이다.(조금 복잡하지만..)**

url 참고 : <https://smithery.ai/server/@cjo4m06/mcp-shrimp-task-manager>

```
npx -y @smithery/cli install @cjo4m06/mcp-shrimp-task-manager --client claude
```

**자동 설치의 장점**  

Smithery를 사용하면 설정 파일 수정 없이 한 번에 설치가 완료된다. Claude Desktop을 재시작하면 바로 사용할 수 있어서 정말 편하다.

**방법2.** **직접 설치**

- github url 참고: <https://github.com/cjo4m06/mcp-shrimp-task-manager>

- 해당 url에서 부터 설치 예시가 클로드 코드 이기도 하고, 나도 동일하게 클로드 코드로 진행하려고 한다.

1) 먼저 로컬에 직접 shrimp task manager 를 clone한 후 설치 해보자.

```
# 본인이 clone할 directory에서 시작하자.

# Clone the repository
git clone https://github.com/cjo4m06/mcp-shrimp-task-manager.git
cd mcp-shrimp-task-manager

# Install dependencies
npm install

# Build the project
npm run build
```

ex) 나의 경우는 cd c:/work > git clone 수행

![](https://blog.kakaocdn.net/dna/ygu4k/btsPYBQaYvU/AAAAAAAAAAAAAAAAAAAAAN-Dw50smQ7uCb53dAsuFWH1Xrw5PT3fxy322scFBSrU/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=BKHHTIjm%2BdARDcq5z3EkBFH%2B1g4%3D)
ex) cd mcp-shrimp-task-manager 이동 후 npm install 수행

- 그런데 하기와 같이 오류가 발생하였다.

![](https://blog.kakaocdn.net/dna/cPuibr/btsPWrOG4OF/AAAAAAAAAAAAAAAAAAAAAEyd1EJOwave6esXFR-R3TKqQuZ2knp0ln3Ukac9txyf/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=6glJ43PwmzYWHKyUSMldqZF4bg4%3D)
- 소스를 확인해보니 **충돌 마커**가 남아 있는 상태라 오류가 발생하고 있었다.

![](https://blog.kakaocdn.net/dna/EX1AA/btsP0gdk5nE/AAAAAAAAAAAAAAAAAAAAABFlz8yJ-u2AVhbh9vWCnyiU3wUJuSUNzxB6HP_HOHxO/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=JrMYxQ1YSp1khkc8sQlXdibQJP0%3D)
- 그래서 현재기준 최신 Tag.버전을 확인해보니 1.0.21 버전이 최신 버전으로 보여 해당 버전으로 우회 설치 시도해 보겠다.

![](https://blog.kakaocdn.net/dna/bMICvm/btsPYHpvWSu/AAAAAAAAAAAAAAAAAAAAABn1RZOZZdEPIfajLi0S1ZDhCjtD24KEinOH3eSIkJtL/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=CV%2BTBLi1%2BXfsJTubMsrxA8lNsvM%3D)

```
git clone https://github.com/cjo4m06/mcp-shrimp-task-manager.git

cd mcp-shrimp-task-manager
git fetch --tags

#필요시 git switch --detach v1.0.21
git checkout v1.0.21
npm install
npm run build
```

- 설치 완료.

![](https://blog.kakaocdn.net/dna/dRy47a/btsPZmSOyfc/AAAAAAAAAAAAAAAAAAAAALzV5As5sVuAy9kopgf1IUcg4jwFP-HuNejnn9d8258-/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=g2leGn%2FA%2F%2BizgmsndF%2FdO7f3ZeY%3D)
- 데이터 디렉토리 준비하자. (임의의 저장소 경로를 만듭니다.)

ex) 윈도우 계열 예시

![](https://blog.kakaocdn.net/dna/8ZdXS/btsPZf1eSQT/AAAAAAAAAAAAAAAAAAAAADC_yPqYo9p6HIFev3JJD5OX3ZCcqmZZTPwj2--d6GQg/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=HQo2mFZzEXXWdXfX66t6KS6WPF8%3D)
- .mcp.json 생성 (claude code를 실핼할 프로젝트 루트에 생성)

ex) 리눅스, mac

```
{
  "mcpServers": {
    "shrimp-task-manager": {
      "command": "node",
      "args": ["/Users/dedur/work/mcp-shrimp-task-manager/dist/index.js"],
      "env": {
        "DATA_DIR": "/Users/dedur/work/shrimp_data",
        "TEMPLATES_USE": "en",
        "ENABLE_GUI": "false"
      }
    }
  }
}
```

ex) windows

```
{
  "mcpServers": {
    "shrimp-task-manager": {
      "command": "node",
      "args": ["C:/work/mcp-shrimp-task-manager/dist/index.js"],
      "env": {
        "DATA_DIR": "C:/work/shrimp_data",
        "TEMPLATES_USE": "en",
        "ENABLE_GUI": "false"
      }
    }
  }
}
```

- 나는 그냥 전역 설정 파일에 추가 하도록 하겠다. ( 상기의 mcp servers 추가 )

( 리눅스 계열 위치 : ( ~/.claude/settings.json 또는 **~/.claude.json** ) )

( 윈도우 계열 위치 : ( c:\users\사용자\.claude.json ))

##### Claude Code CLI

- 위 (.mcp.json) 파일이 만들어졌다면, 다음 명령어를 통해 claude code를 실행 하자.

- 이후 /mcp list 로 확인해보면 정상 연동되어있음을 확인 가능하다.

![](https://blog.kakaocdn.net/dna/dCcWWS/btsPXUimlU5/AAAAAAAAAAAAAAAAAAAAAM-PkaMa8bBreQPFFa8KY2tPXQWwDxzMRlfiBUYes2Zh/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=7h7Nrc9UwuRHMYFc23ZgQj3dI4U%3D)
##### Cursor 설정

- Cursor Settings > Tools & Integrations > New MCP Server

![](https://blog.kakaocdn.net/dna/8H1eN/btsPTR0gtER/AAAAAAAAAAAAAAAAAAAAAOV2jJsgQLgAVZUVCToL-uxs_Tg2qeDFVTwbiggSwWYJ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=c%2BZHeOB%2FKwJVD8f%2FfOfjD43RLFM%3D)![](https://blog.kakaocdn.net/dna/croMFg/btsPUNJK0yS/AAAAAAAAAAAAAAAAAAAAAFqBYr8MhUmhHkSnfFnV0rxux_kWYcyAYz13XoCIsl1Z/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=8oPG5Yu55NRusY37h5kZsHoGHFs%3D)
ex) 리눅스, mac

{  

 "mcpServers": {  

 "shrimp-task-manager": {  

 "command": "node",  

 "args": ["/Users/dedur/work/mcp-shrimp-task-manager/dist/index.js"],  

 "env": {  

 "DATA\_DIR": "/Users/dedur/work/shrimp\_data",  

 "TEMPLATES\_USE": "en",  

 "ENABLE\_GUI": "false"  

 }  

 }  

 }  

}

ex) windows

{  

 "mcpServers": {  

 "shrimp-task-manager": {  

 "command": "node",  

 "args": ["C:/work/mcp-shrimp-task-manager/dist/index.js"],  

 "env": {  

 "DATA\_DIR": "C:/work/shrimp\_data",  

 "TEMPLATES\_USE": "en",  

 "ENABLE\_GUI": "false"  

 }  

 }  

 }  

}

Gemini CLI

![](https://blog.kakaocdn.net/dna/d6rCty/btsPZ3MNW7w/AAAAAAAAAAAAAAAAAAAAAJKaE7LNdNGLtWo-EFGkSFihy5KO1DjXk7yXp5-Rn8uw/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=aaoToImIT7iIflpynz0RFLcitiQ%3D)
#### **사용 방법**

사용 하기 앞서 먼저 하기 **기본 워크플로우 에서부터, 연구모드, 서브 에이전트 관리, 연속 모드 등**에 대해 간단히 빠르게 이해하고 실습을 이어 가려고 한다.

- 도구 정리 ( 참고 : <https://smithery.ai/server/@cjo4m06/mcp-shrimp-task-manager> )

|  |  |  |
| --- | --- | --- |
| **범주 (Category)** | **도구 이름 (Tool Name)** | **설명 (Description)** |
| 작업 계획 (Planning) | plan\_task | 복잡한 요구사항을 구조화된 개발 작업으로 변환하며, 에이전트의 논리적 사고 과정을 돕습니다. |
| 작업 분석 (Analysis) | analyze\_task | 특정 작업에 대한 요구사항을 심층 분석하고, 코드베이스 및 기술적 타당성을 평가합니다. |
|  | process\_thought | 복잡한 문제에 대한 단계별 추론 과정을 진행합니다. |
| 솔루션 평가 (Solution Review) | reflect\_task | 솔루션의 비판적 검토를 통해 개선점을 찾고 품질을 향상시킵니다. |
| 연구 및 조사 (Research) | research\_mode | 특정 기술이나 문제에 대해 체계적인 기술 연구 모드로 전환합니다. |
| 프로젝트 관리 (Project Management) | init\_project\_rules | 프로젝트 표준 및 규칙을 초기화하거나 업데이트하여 일관된 개발 관행을 유지합니다. |
| 작업 관리 (Task Management) | split\_tasks | 복잡한 작업을 더 작고 관리하기 쉬운 단위로 나눕니다. |
|  | list\_tasks | 모든 작업 및 현재 상태를 표시합니다. |
|  | query\_task | 특정 키워드를 사용하여 작업을 검색하고 나열합니다. |
|  | get\_task\_detail | 완료된 작업의 상세 정보를 표시합니다. |
|  | delete\_task | 아직 완료되지 않은 작업을 삭제합니다. |
|  | add\_task\_dependencies | 작업 간의 종속성(dependencies)을 설정합니다. |
|  | get\_task\_status | 특정 작업의 현재 상태를 확인합니다. |
| 작업 실행 (Task Execution) | execute\_task | 특정 작업을 실행하도록 AI 에이전트에게 지시합니다. |
|  | verify\_task | 작업 완료 여부를 확인하고, 요구사항이 충족되었는지 검증합니다. |

#### **기본 워크 플로우**

1. **프로젝트 룰 초기화** : "init project rules"로 프로젝트 기준 설정
2. **태스크 계획** : "plan task [설명]"으로 작업 계획 수립
3. **태스크 실행** : "execute task [이름/ID]"로 구현 시작
4. **연속 실행** : "continuous mode"로 전체 큐 자동 처리

#### **연구 모드와 문서화 자동화**

연구 모드는 기술 조사와 지식 수집을 위한 체계적인 워크플로우를 제공한다.

새로운 기술을 도입하기 전이나 복잡한 문제를 해결할 때 사용하면 유용하다.

##### **연구 모드 실제 활용 예시**

1. **새로운 라이브러리 학습**  
"Research React Hook Form for form validation"  
→ 라이브러리 특징, 사용법, 베스트 프랙티스까지 체계적으로 조사
2. **아키텍처 패턴 비교**  
"Research microservices vs monolith for e-commerce platform"  
→ 각 패턴의 장단점, 적용 사례, 구현 복잡도 비교 분석
3. **기술 스택 선정**  
"Research GraphQL vs REST API for mobile app backend"  
→ 성능, 개발 편의성, 생태계 등 다각도 분석

###### **문서화 워크플로우 자동화 예시**

코드 작성과 문서화가 함께 진행되는 프로젝트에서 특히 강력하다:

* **API 문서 자동 생성**: 엔드포인트 개발 후 자동으로 API 문서 초안 작성
* **README 업데이트**: 새 기능 추가 시 사용자 가이드 자동 갱신
* **코드 주석 생성**: 복잡한 로직에 대한 설명 주석 자동 추가
* **변경사항 문서화**: 코드 수정 시 관련 문서도 함께 업데이트

#### **서브 에이전트 협업과 연속 실행 모드**

Shrimp Task Manager의 고급 기능 중 하나는 **여러 서브 에이전트를 관리하고 특정 작업에 할당할 수 있다**는 점이다.

이를 통해 작업 유형에 맞는 특화된 에이전트를 활용할 수 있다.

##### **에이전트 특화 전략 예시**

* **프론트엔드 에이전트** : React, CSS, UI/UX 작업에 특화
* **백엔드 에이전트** : API, 데이터베이스, 서버 로직 담당
* **테스트 에이전트** : 단위 테스트, 통합 테스트 작성 전담
* **문서화 에이전트** : API 문서, README, 주석 작성 특화

###### **연속 실행 모드 (Continuous Mode)**

모든 태스크를 자동으로 순차 실행하는 강력한 기능이다:

**⚠️ 연속 모드 사용 시 주의사항**  

초반에는 한 단계씩 검토하며 진행하고, AI의 결과를 충분히 신뢰할 수 있을 때 연속 모드를 사용하는 것을 권장한다. 중간에 오류가 발생하면 전체 플로우가 중단될 수 있다.

#### **태스크 메모리와 반복 작업 방지**

Shrimp의 가장 인상적인 기능 중 하나로 시스템이 자동으로 태스크 실행 히스토리를 백업하고, 새로운 태스크를 계획할 때 과거 경험을 참조한다.

###### **메모리 시스템 동작 방식**

* 백업 파일이 `tasks\_backup\_YYYY-MM-DDThh-mm-ss.json` 형식으로 자동 저장
* 새 태스크 계획 시 과거 성공 사례를 자동으로 참조
* 비슷한 문제를 다시 만났을 때 중복 작업 방지
* 실패했던 방법들도 기록해서 같은 실수 반복 방지

##### 변경 요구사항 대응

특히 요구사항이 자주 변경되는 프로젝트에서 진가를 발휘한다:

1. **변경 전후 맥락 기억**: 이전에 구현했던 내용과 변경사항을 비교 분석
2. **필요한 수정 작업만 추출**: 전체를 다시 만들지 않고 변경된 부분만 식별
3. **신속한 대응**: 팀의 새로운 요구사항에 빠르게 반응 가능
4. **학습 효과**: 비슷한 변경 패턴이 반복되면 더 정확한 예측

#### **실제 개발 시나리오 예시**

새로 React로 todo list 웹을 만든다고 가정해보자. 이때 Shrimp Task Manager를 어떻게 활용할 수 있는지 실제 시나리오로 살펴보겠다. 난 Filesystem MCP를 연동해뒀기때문에 특정 경로의 prd 파일을 읽을수 있고, 이를 통해 연구 단계부터 진행 해보도록 하겠다.

이전 Task-Master AI MCP를 실습했을때 만들었던 prd를 그대로 사용해보겠다. ( 결과물 비교를 위해 )

ex) prd 생성 예시 결과물을 txt파일로 해도 되고, 난 마크 다운 형식으로 생성 요청 하여 저장하도록 하겠다.

![](https://blog.kakaocdn.net/dna/bma3Gj/btsPVffcScr/AAAAAAAAAAAAAAAAAAAAAOY1zPfXf-6sOM-hFvgzgW8UNzuFyc-lvLlrOA_h-BiX/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=AmrkjuFdyuglleNJGOur1LYzoaU%3D)
- 해당 결과의 prd파일을 claude가 읽을 수 있는 위치에 저장 해 두었다. ( c:/work/workspace/todolist/prd.md )

- 시작은 당연히...

##### 단계별 작업 흐름

**1. 연구 단계 : research\_mode**

![](https://blog.kakaocdn.net/dna/WnWpT/btsPYHXJ2vn/AAAAAAAAAAAAAAAAAAAAAOn0R4QAA5ICm-rSSs3d7fixGKgqveBEd3rSc0HZcPYv/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=zNUycbd4V9D4oJ9%2BceDQUufFi50%3D)
> Shrimp Task Manager MCP를 사용하여 c:/work/workspace/todolist/prd.md 파일에서 PRD를 읽어들여 Research Mode를 실행하여 목표, 범위, 기술 스택, 제약 조건 등 작업계획을 수립해줘.

**※ prd 파일은 본인의 프로젝트 루트에 두면 더 잘 찾는다.**

![](https://blog.kakaocdn.net/dna/dqVZ5W/btsPY7oBp44/AAAAAAAAAAAAAAAAAAAAAGLT88pw2jDJCgqaazFXbv_tQHavtSK67-rH7Lhv3OXU/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=fof%2BAMcpdB0uTpEEpwPQgBVSktI%3D)
ex) 영문 버전이 더 확실하다.

- 결과가 정말 자세하고, 방대하게 나왔다. 접은글로 작성해둘 예정이니 참고하실분들께서는 참고 해 보면 좋을 것 같다.

더보기

> Shrimp Task Manager MCP를 사용하여. c:/work/workspace/todolist/prd.md 파일에서 PRD를 읽어들여 Research Mode를 실행하여 목표, 범위, 기술 스택, 제약 조건등 작업 계획을 수립해줘.

⏺ PRD를 읽어들인 후 Research Mode를 통해 작업 계획을 수립하겠습니다.

⏺ Read(c:/work/workspace/todolist/prd.md)  

 ⎿ Read 286 lines (ctrl+r to expand)

⏺ 이제 Shrimp Task Manager의 Research Mode를 사용하여 PRD 기반 작업 계획을 수립하겠습니다.

⏺ shrimp-task-manager - research\_mode (MCP)(topic: "Firebase 기반 React To-Do List 서비스 개발", currentState: "PRD 문서를 분석하여 TodoFlow 서비스의 목표, 범위, 기술 스택, 제약  

 조건을 파악함. Firebase Authentication + Firestore 기반의 개인화된 실시간 동기화 To-Do 앱을 개발해야 함. React + Vite + Tailwind CSS를  

 사용하고, 반응형 UI와 접근성을 고려해야 함. 5주 개발 일정으로 주차별 마일스톤이 설정되어 있음.", nextSteps: "기술 스택별 구현 방안 연구,  

 Firebase 보안 규칙 최적화, 성능 요구사항 달성 전략, 접근성 및 국제화 구현 방법론, CI/CD 파이프라인 설계, 테스트 전략 수립")  

 ⎿ # Programming Research Mode

You are an AI research assistant equipped with web search, codebase file lookup, and library API query capabilities.  

 … +95 lines (ctrl+r to expand)

⏺ PRD 문서를 기반으로 Firebase + React To-Do List 서비스에 대한 포괄적인 기술 연구를 시작하겠습니다. 우선 최신 기술 스택과 모범 사례를 조사하겠습니다.

⏺ Web Search("React Vite Firebase Firestore 2025 best practices authentication setup")  

 ⎿ Did 1 search in 24s

⏺ Web Search("Firestore security rules React authentication best practices 2025")  

 ⎿ Did 1 search in 24s

⏺ Web Search("React performance optimization bundle size Vite 2025 code splitting")  

 ⎿ Did 1 search in 31s

⏺ Web Search("React accessibility a11y WCAG 2025 Tailwind CSS best practices")  

 ⎿ Did 1 search in 29s

⏺ Web Search("React i18n internationalization 2025 react-i18next best practices")  

 ⎿ Did 1 search in 33s

⏺ Web Search("React testing Vitest RTL Cypress Playwright 2025 best practices")  

 ⎿ Did 1 search in 30s

shrimp-task-manager - research\_mode (MCP)(topic: "Firebase 기반 React To-Do List 서비스 개발", currentState: "Firebase + React + Vite 기술 스택의 핵심 구현 방안을 조사함.  

 2025년 최신 모범 사례로 Firebase 9 modular SDK 사용, Firestore security rules 구현, React performance optimization, bundle size 관리 (<  

 200KB), 접근성 (WCAG 2.1 AA), i18n 지원 (react-i18next), 테스트 전략 (Vitest + RTL + Playwright) 등을 파악함. 다음 단계로 프로젝트  

 구조 설계와 CI/CD 파이프라인 구축 방안을 조사해야 함.", nextSteps: "Firebase Hosting + GitHub Actions CI/CD 파이프라인 설계, React  

 프로젝트 구조 모범 사례, Tailwind CSS + 반응형 디자인 구현, 상태관리 전략 (Zustand vs React Query), 오프라인 지원 및 PWA 기능, Firebase  

 보안 및 비용 최적화 전략", previousState: "PRD 문서를 분석하여 TodoFlow 서비스의 목표, 범위, 기술 스택, 제약 조건을 파악함. Firebase  

 Authentication + Firestore 기반의 개인화된 실시간 동기화 To-Do 앱을 개발해야 함. React + Vite + Tailwind CSS를 사용하고, 반응형 UI와  

 접근성을 고려해야 함. 5주 개발 일정으로 주차별 마일스톤이 설정되어 있음.")  

 ⎿ # Programming Research Mode

You are an AI research assistant equipped with web search, codebase file lookup, and library API query capabilities.  

 … +106 lines (ctrl+r to expand)

⏺ 이제 CI/CD 파이프라인과 프로젝트 구조 설계 방안을 조사하겠습니다.

⏺ Web Search("Firebase Hosting GitHub Actions CI/CD React 2025 deployment")  

 ⎿ Did 1 search in 26s

⏺ Web Search("React project structure best practices 2025 Vite folder architecture")  

 ⎿ Did 1 search in 28s

⏺ Web Search("Zustand vs React Query state management 2025 comparison")  

 ⎿ Did 1 search in 22s

⏺ Web Search("React PWA offline support 2025 Workbox service worker")  

 ⎿ Did 1 search in 28s

⏺ Web Search("Firebase cost optimization Firestore security billing 2025")  

 ⎿ Did 1 search in 26s

⏺ shrimp-task-manager - research\_mode (MCP)(topic: "Firebase 기반 React To-Do List 서비스 개발", currentState: "CI/CD 파이프라인과 프로젝트 구조에 대한 심화 연구를 완료함.  

 Firebase Hosting + GitHub Actions 공식 통합 (2025 최신), React + Vite 프로젝트 구조 모범 사례 (feature-based organization), Zustand +  

 React Query 조합 전략, PWA/오프라인 지원 (Workbox), Firebase 비용 최적화 전략 등을 조사함. 이제 모든 기술 요소에 대한 연구가 완료되어  

 최종 보고서 작성이 가능함.", nextSteps: "모든 연구 결과를 통합하여 TodoFlow 서비스 개발을 위한 종합적인 기술 설계 보고서 작성. PRD  

 요구사항을 충족하는 구체적인 구현 방안, 기술 스택 선택 근거, 개발 계획 수립", previousState: "Firebase + React + Vite 기술 스택의 핵심  

 구현 방안을 조사함. 2025년 최신 모범 사례로 Firebase 9 modular SDK 사용, Firestore security rules 구현, React performance optimization,  

 bundle size 관리 (< 200KB), 접근성 (WCAG 2.1 AA), i18n 지원 (react-i18next), 테스트 전략 (Vitest + RTL + Playwright) 등을 파악함. 다음  

 단계로 프로젝트 구조 설계와 CI/CD 파이프라인 구축 방안을 조사해야 함.")  

 ⎿ # Programming Research Mode

You are an AI research assistant equipped with web search, codebase file lookup, and library API query capabilities.  

 … +105 lines (ctrl+r to expand)

⏺ 모든 기술 요소에 대한 연구가 완료되었으므로, 이제 TodoFlow 서비스 개발을 위한 종합적인 기술 설계 보고서를 작성하겠습니다.

🚀 TodoFlow 개발을 위한 종합 기술 설계 보고서

Firebase + React + Vite 기반 실시간 To-Do List 서비스2025년 최신 기술 스택 및 모범 사례 기반 설계

---  

 📋 개요

본 보고서는 PRD에 명시된 TodoFlow 서비스 개발을 위한 종합적인 기술 설계를 제시합니다. 2025년 최신 웹 개발 모범 사례와 Firebase 생태계를 활용하여 안전하고 확장 가능한 개인화  

 To-Do 서비스 구현 방안을 다룹니다.

---  

 🎯 핵심 요구사항 분석

기능적 요구사항

- 인증: Firebase Authentication (Google, Email/Password)  

 - 데이터: Firestore를 통한 실시간 동기화  

 - CRUD: 완전한 To-Do 관리 기능  

 - 필터/정렬: 다양한 기준으로 데이터 조회  

 - 개인화: 사용자별 데이터 분리

비기능적 요구사항

- 성능: LCP < 2.0s, 번들 사이즈 < 200KB  

 - 접근성: WCAG 2.1 AA 준수  

 - 국제화: 한국어/영어 지원  

 - 반응형: 모든 디바이스 대응  

 - 보안: 철저한 데이터 격리

---  

 🛠️ 기술 스택 선택 및 근거

Frontend 기술 스택

1. React 18 + Vite

선택 근거:  

 - Vite의 빠른 개발 서버 및 번들링 성능  

 - React 18의 Concurrent Features 활용 가능  

 - ES Modules 기반 개발로 향상된 DX

2025 최적화 기법:  

 - SWC 컴파일러로 30% 빠른 빌드  

 - 자동 코드 분할로 번들 사이즈 최적화  

 - Tree-shaking을 통한 불필요한 코드 제거

2. TypeScript

선택 근거:  

 - 런타임 오류 사전 방지  

 - Firebase SDK와의 타입 안정성  

 - 대규모 프로젝트 유지보수성 향상

3. Tailwind CSS

선택 근거:  

 - 빠른 프로토타이핑 및 일관성 있는 디자인  

 - 최적화된 번들 사이즈 (사용하지 않는 CSS 자동 제거)  

 - 접근성 유틸리티 클래스 (sr-only, focus 등) 제공

Backend & 인프라

1. Firebase 9 Modular SDK

주요 서비스:  

 - Authentication: Google OAuth, Email/Password  

 - Firestore: 실시간 NoSQL 데이터베이스  

 - Hosting: 정적 웹사이트 호스팅  

 - Security Rules: 서버측 데이터 보안

2025 최신 기능:  

 - Tree-shaking 지원으로 번들 사이즈 50% 감소  

 - 향상된 오프라인 지원  

 - 개선된 타입스크립트 지원

2. 보안 아키텍처

// Firestore Security Rules (PRD 명세 기준)  

 rules\_version = '2';  

 service cloud.firestore {  

 match /databases/{database}/documents {  

 match /users/{userId}/todos/{todoId} {  

 allow read, create: if request.auth != null  

 && request.auth.uid == userId;  

 allow update, delete: if request.auth != null  

 && request.auth.uid == userId  

 && resource.data.ownerUid == userId  

 && request.resource.data.ownerUid == userId;  

 }  

 }  

 }

---  

 🏗️ 아키텍처 설계

1. 프로젝트 구조 (Feature-Based Organization)

todoflow/  

 ├── public/  

 │ ├── manifest.json # PWA 매니페스트  

 │ └── sw.js # 서비스 워커  

 ├── src/  

 │ ├── components/  

 │ │ ├── ui/ # 재사용 UI 컴포넌트  

 │ │ ├── todo/ # To-Do 관련 컴포넌트  

 │ │ └── auth/ # 인증 관련 컴포넌트  

 │ ├── pages/  

 │ │ ├── SignIn.tsx  

 │ │ ├── TodoApp.tsx  

 │ │ └── Account.tsx  

 │ ├── hooks/  

 │ │ ├── useAuth.ts # 인증 커스텀 훅  

 │ │ ├── useTodos.ts # To-Do React Query 훅  

 │ │ └── useOffline.ts # 오프라인 상태 관리  

 │ ├── stores/  

 │ │ ├── authStore.ts # Zustand 인증 스토어  

 │ │ └── uiStore.ts # UI 상태 관리  

 │ ├── services/  

 │ │ ├── firebase.ts # Firebase 설정  

 │ │ ├── todoService.ts # To-Do CRUD 서비스  

 │ │ └── authService.ts # 인증 서비스  

 │ ├── lib/  

 │ │ ├── queryClient.ts # React Query 설정  

 │ │ └── i18n.ts # 국제화 설정  

 │ └── types/  

 │ └── todo.ts # TypeScript 타입 정의  

 ├── .github/workflows/  

 │ └── deploy.yml # CI/CD 워크플로우  

 ├── vite.config.ts  

 ├── tailwind.config.js  

 └── package.json

2. 상태 관리 전략

Zustand + React Query 조합

Zustand (클라이언트 상태):  

 - UI 상태 (필터, 정렬, 로딩)  

 - 사용자 인증 상태  

 - 테마, 언어 설정

React Query (서버 상태):  

 - To-Do 데이터 캐싱 및 동기화  

 - 실시간 업데이트 관리  

 - 오프라인 지원 및 재연결 처리

// Zustand Store 예시  

 const useUIStore = create<UIState>((set) => ({  

 filter: 'all',  

 sortBy: 'updatedAt',  

 isOffline: false,  

 setFilter: (filter) => set({ filter }),  

 setSortBy: (sortBy) => set({ sortBy }),  

 }));

// React Query Hook 예시  

 const useTodos = () => {  

 const { uid } = useAuthStore();  

 return useQuery({  

 queryKey: ['todos', uid],  

 queryFn: () => getTodos(uid),  

 enabled: !!uid,  

 refetchOnWindowFocus: false,  

 });  

 };

---  

 🎨 UI/UX 설계

1. 접근성 (WCAG 2.1 AA 준수)

주요 구현사항:  

 - 시맨틱 HTML 요소 사용  

 - 키보드 내비게이션 지원  

 - 스크린 리더 호환성  

 - 색상 대비비 4.5:1 이상 유지  

 - ARIA 라벨 및 속성 적용

Tailwind 접근성 클래스 활용:  

 <!-- 스크린 리더 전용 텍스트 -->  

 <span class="sr-only">완료된 작업</span>

<!-- 포커스 스타일링 -->  

 <button class="focus:ring-2 focus:ring-blue-500 focus:outline-none">  

 추가  

 </button>

2. 반응형 디자인

브레이크포인트 전략:  

 - Mobile: ≤640px  

 - Tablet: 641px-1024px  

 - Desktop: ≥1025px

핵심 컴포넌트:  

 - 적응형 네비게이션 (햄버거 메뉴 ↔ 풀 메뉴)  

 - 그리드 레이아웃 (1열 ↔ 2열 ↔ 3열)  

 - 터치 친화적 인터랙션 (44px 최소 터치 영역)

3. 국제화 (i18n)

React-i18next 구현:  

 // i18n 설정  

 i18n  

 .use(Backend)  

 .use(LanguageDetector)  

 .use(initReactI18next)  

 .init({  

 lng: 'ko',  

 fallbackLng: 'en',  

 resources: {  

 ko: { translation: koTranslation },  

 en: { translation: enTranslation },  

 },  

 });

// 사용법  

 const { t } = useTranslation();  

 return <h1>{t('todo.add\_new')}</h1>;

---  

 ⚡ 성능 최적화

1. 번들 사이즈 최적화 (목표: <200KB)

Code Splitting 전략:  

 // 라우트 기반 분할  

 const TodoApp = lazy(() => import('./pages/TodoApp'));  

 const Account = lazy(() => import('./pages/Account'));

// 컴포넌트 기반 분할   

 const TodoEditor = lazy(() => import('./components/TodoEditor'));

Vite 설정 최적화:  

 export default defineConfig({  

 build: {  

 rollupOptions: {  

 output: {  

 manualChunks: {  

 'firebase': ['firebase/app', 'firebase/auth', 'firebase/firestore'],  

 'react-query': ['@tanstack/react-query'],  

 'ui': ['@headlessui/react', '@heroicons/react'],  

 },  

 },  

 },  

 },  

 });

2. Firebase 비용 최적화

쿼리 최적화 전략:  

 - 필요한 필드만 조회하는 select() 사용  

 - 페이지네이션으로 대량 데이터 처리  

 - 로컬 캐싱으로 중복 쿼리 방지  

 - 인덱스 최적화로 쿼리 성능 향상

실시간 업데이트 효율화:  

 // 조건부 리스너 설정  

 const unsubscribe = onSnapshot(  

 query(todosRef, where('completed', '==', false)),  

 (snapshot) => {  

 // 변경된 문서만 처리  

 snapshot.docChanges().forEach((change) => {  

 if (change.type === 'added') updateTodoCache('add', change.doc);  

 if (change.type === 'modified') updateTodoCache('update', change.doc);  

 if (change.type === 'removed') updateTodoCache('remove', change.doc);  

 });  

 }  

 );

---  

 🧪 테스트 전략

1. 테스트 피라미드

Unit Tests (Vitest + RTL):  

 - 컴포넌트 렌더링 및 상호작용  

 - 커스텀 훅 테스트  

 - 유틸리티 함수 테스트  

 - 목표 커버리지: 80%

Integration Tests:  

 - Firebase 서비스 통합  

 - 상태 관리 플로우  

 - API 호출 및 에러 처리

E2E Tests (Playwright):  

 - 사용자 시나리오 기반 테스트  

 - 크로스 브라우저 호환성  

 - 성능 및 접근성 검증

2. 테스트 설정 예시

// Vitest + RTL 설정  

 import { render, screen, fireEvent } from '@testing-library/react';  

 import { QueryClient, QueryClientProvider } from '@tanstack/react-query';  

 import TodoItem from '../TodoItem';

describe('TodoItem', () => {  

 test('완료 상태 토글이 정상 작동한다', async () => {  

 const mockToggle = vi.fn();  

 render(  

 <QueryClientProvider client={new QueryClient()}>  

 <TodoItem todo={mockTodo} onToggle={mockToggle} />  

 </QueryClientProvider>  

 );

const checkbox = screen.getByRole('checkbox');  

 fireEvent.click(checkbox);

expect(mockToggle).toHaveBeenCalledWith(mockTodo.id);  

 });  

 });

---  

 🚀 CI/CD & 배포 전략

1. GitHub Actions 워크플로우

# .github/workflows/deploy.yml  

 name: Deploy to Firebase Hosting  

 on:  

 push:  

 branches: [main]  

 pull\_request:  

 branches: [main]

jobs:  

 build-and-deploy:  

 runs-on: ubuntu-latest  

 steps:  

 - uses: actions/checkout@v4

- name: Setup Node.js  

 uses: actions/setup-node@v4  

 with:  

 node-version: '18'  

 cache: 'npm'

- name: Install dependencies  

 run: npm ci

- name: Run tests  

 run: npm run test

- name: Run lint  

 run: npm run lint

- name: Build  

 run: npm run build

- name: Deploy to Firebase  

 uses: FirebaseExtended/action-hosting-deploy@v0  

 with:  

 repoToken: '${{ secrets.GITHUB\_TOKEN }}'  

 firebaseServiceAccount: '${{ secrets.FIREBASE\_SERVICE\_ACCOUNT }}'  

 projectId: todoflow-prod

2. 환경 분리 전략

Development 환경:  

 - Firebase 에뮬레이터 사용  

 - 로컬 개발 서버 (Vite dev)  

 - 테스트 데이터 시드

Production 환경:  

 - Firebase Hosting 배포  

 - CDN 캐싱 최적화  

 - 성능 모니터링 (Lighthouse CI)

---  

 📱 PWA & 오프라인 지원

1. Service Worker (Workbox)

// src/sw.ts  

 import { precacheAndRoute, createHandlerBoundToURL } from 'workbox-precaching';  

 import { NavigationRoute, registerRoute } from 'workbox-routing';

// App Shell 프리캐싱  

 precacheAndRoute(self.\_\_WB\_MANIFEST);

// 오프라인 폴백  

 const handler = createHandlerBoundToURL('/index.html');  

 const navigationRoute = new NavigationRoute(handler);  

 registerRoute(navigationRoute);

2. 오프라인 데이터 동기화

전략:  

 - Firestore 오프라인 지속성 활성화  

 - 로컬 스토리지 백업  

 - 네트워크 재연결시 자동 동기화  

 - 오프라인 상태 UI 표시

// 오프라인 지원 훅  

 const useOfflineSync = () => {  

 const [isOnline, setIsOnline] = useState(navigator.onLine);

useEffect(() => {  

 const handleOnline = () => setIsOnline(true);  

 const handleOffline = () => setIsOnline(false);

window.addEventListener('online', handleOnline);  

 window.addEventListener('offline', handleOffline);

return () => {  

 window.removeEventListener('online', handleOnline);  

 window.removeEventListener('offline', handleOffline);  

 };  

 }, []);

return { isOnline };  

 };

---  

 📊 모니터링 & 분석

1. 성능 모니터링

핵심 지표:  

 - LCP (Largest Contentful Paint): <2.0s  

 - FID (First Input Delay): <100ms  

 - CLS (Cumulative Layout Shift): <0.1  

 - 번들 사이즈: <200KB (gzipped)

2. 사용자 분석

추적 이벤트:  

 // 주요 사용자 액션 추적  

 const trackEvent = (eventName: string, properties?: object) => {  

 // Google Analytics 4 또는 Firebase Analytics  

 gtag('event', eventName, {  

 custom\_parameter\_1: properties?.value,  

 // ... 기타 속성  

 });  

 };

---  

 🔐 보안 고려사항

1. 데이터 보안

Firestore Security Rules:  

 - 사용자별 데이터 격리 강제  

 - 필드 레벨 검증  

 - Rate Limiting 적용  

 - SQL Injection 방지

2. 인증 보안

Firebase Auth 설정:  

 - 이메일 인증 강화  

 - 브루트포스 공격 방지  

 - 세션 관리 최적화  

 - 보안 헤더 설정

---  

 📈 개발 일정 (5주 마일스톤)

1주차: 기반 인프라 구축

- Vite + React + TypeScript 프로젝트 설정  

 - Firebase 프로젝트 초기화  

 - 기본 인증 UI 구현  

 - CI/CD 파이프라인 구축

2주차: 핵심 기능 개발

- To-Do CRUD 기능 구현  

 - Firestore 실시간 동기화  

 - 기본 필터/정렬 기능  

 - Zustand + React Query 통합

3주차: UI/UX 완성

- 반응형 디자인 구현  

 - 접근성 개선 (WCAG 2.1 AA)  

 - i18n 지원 추가  

 - PWA 기능 구현

4주차: 성능 최적화

- 코드 분할 및 번들 최적화  

 - 오프라인 지원 강화  

 - 성능 튜닝  

 - 보안 강화

5주차: 테스트 & 배포

- 종합 테스트 실행  

 - 접근성 검증  

 - 성능 벤치마크  

 - 프로덕션 배포

---  

 🎯 성공 지표 달성 방안

로그인 성공률 95%+

- Firebase Auth 에러 핸들링 강화  

 - 직관적인 로그인 UI/UX  

 - 소셜 로그인 옵션 제공

1주 재방문률 50%+

- PWA 설치 유도  

 - 오프라인 사용 가능  

 - 빠른 로딩 성능

TTF < 60초

- 온보딩 플로우 최적화  

 - 직관적인 UI 설계  

 - 튜토리얼 가이드 제공

에러 로그 <0.1/session

- 포괄적인 에러 핸들링  

 - 사용자 친화적 에러 메시지  

 - 자동 에러 리포팅

---  

 💰 비용 예상 및 최적화

Firebase 비용 분석 (월 1000 사용자 기준)

- Firestore: ~$15 (읽기/쓰기 최적화로 50% 절약 가능)  

 - Authentication: 무료 (50,000 MAU까지)  

 - Hosting: ~$5 (CDN 포함)  

 - 총 예상 비용: ~$20/월

비용 최적화 전략

- 로컬 캐싱으로 Firestore 읽기 50% 감소  

 - 배치 작업으로 쓰기 작업 최적화  

 - 인덱스 최적화로 쿼리 효율성 향상  

 - 사용량 모니터링 및 알림 설정

---  

 🔮 향후 확장 계획

Phase 2 (6개월 후)

- 팀 협업 기능 추가  

 - 캘린더 통합  

 - 푸시 알림 서비스  

 - 데이터 내보내기/가져오기

Phase 3 (1년 후)

- AI 기반 스마트 추천  

 - 음성 입력 지원  

 - 네이티브 앱 개발  

 - 엔터프라이즈 기능

---  

 🏁 결론

본 기술 설계는 2025년 최신 웹 개발 모범 사례를 기반으로 TodoFlow 서비스의 성공적인 구현을 위한 종합적인 로드맵을 제시합니다.

핵심 성공 요소:  

 ✅ 확장 가능한 아키텍처: Feature-based 구조로 유지보수성 확보✅ 성능 최적화: 번들 사이즈 <200KB, LCP <2.0s 달성✅ 사용자 경험: WCAG 2.1 AA 접근성과 PWA 오프라인 지원✅ 개발   

 효율성: TypeScript + 자동화된 CI/CD로 안정성 보장✅ 비용 효율성: Firebase 최적화로 운영 비용 최소화

이 설계를 따라 개발을 진행한다면, PRD에서 요구하는 모든 기능적/비기능적 요구사항을 충족하면서도 미래 확장성을 고려한 견고한 TodoFlow 서비스를 구축할 수 있을 것입니다.

![](https://blog.kakaocdn.net/dna/1tKJ3/btsPYART065/AAAAAAAAAAAAAAAAAAAAAPnK2iYC8583c-h4F3MAyXST7_7BSHJRuqBhb_vIsU2o/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=uJXayfVF05qy53tp5qV5NSGZgng%3D)
- 출력 내용

더보기

> “Shrimp Task Manager MCP를 사용하여 PRD에서 initialize Project Rules 해줘."

⏺ Shrimp Task Manager MCP의 초기화 프로젝트 규칙 기능을 사용하여 PRD 기반 프로젝트 표준을 설정하겠습니다.  

 ⎿ Please use the "process\_thought" tool to consider the following issues

# Project Standards Initialization Guide  

 … +84 lines (ctrl+r to expand)

⏺ shrimp-task-manager - process\_thought (MCP)(thought: "PRD 기반 TodoFlow 프로젝트의 규칙을 초기화해야 함. Firebase + React + Vite 기술 스택을 사용하는 실시간 To-Do List 서비스  

 프로젝트. 먼저 현재 프로젝트의 파일 구조와 내용을 파악하여 AI Agent가 이해할 수 있는 구체적인 개발 가이드라인을 작성해야 함.",  

 thought\_number: 1, total\_thoughts: 5, next\_thought\_needed: true, stage: "Problem Definition")  

 ⎿ ## Thought 1/5 - Problem Definition

PRD 기반 TodoFlow 프로젝트의 규칙을 초기화해야 함. Firebase + React + Vite 기술 스택을 사용하는 실시간 To-Do List 서비스 프로젝트. 먼저 현재 프로젝트의 파일 구조와 내용을  

 파악하여 AI Agent가 이해할 수 있는 구체적인 개발 가이드라인을 작성해야 함.  

 … +10 lines (ctrl+r to expand)

⏺ shrimp-task-manager - process\_thought (MCP)(thought: "현재 프로젝트 디렉토리 구조를 파악해야 함. 이미 존재하는 파일들을 확인하여 실제 프로젝트 상태를 기반으로 규칙을 작성할  

 필요가 있음. PRD에서 명시된 기술 스택과 요구사항을 반영한 구체적인 AI 개발 가이드라인을 만들어야 함.", thought\_number: 2,  

 total\_thoughts: 5, next\_thought\_needed: true, stage: "Information Gathering")  

 ⎿ ## Thought 2/5 - Information Gathering

현재 프로젝트 디렉토리 구조를 파악해야 함. 이미 존재하는 파일들을 확인하여 실제 프로젝트 상태를 기반으로 규칙을 작성할 필요가 있음. PRD에서 명시된 기술 스택과 요구사항을  

 반영한 구체적인 AI 개발 가이드라인을 만들어야 함.  

 … +10 lines (ctrl+r to expand)

⏺ List(c:/work/workspace/todolist)  

 ⎿ Listed 2 paths (ctrl+r to expand)

⏺ filesystem - directory\_tree (MCP)(path: "c:/work/workspace/todolist")  

 ⎿ []

⏺ shrimp-task-manager - process\_thought (MCP)(thought: "현재 프로젝트 디렉토리가 비어있는 상태임을 확인함. PRD 문서만 존재하는 초기 상태이므로, PRD에서 정의된 요구사항과 기술  

 스택을 바탕으로 AI Agent가 프로젝트를 구축할 때 따라야 할 구체적인 규칙들을 정의해야 함. Firebase + React + Vite + TypeScript +  

 Tailwind CSS 기술 스택과 5주 개발 일정을 고려한 개발 가이드라인을 작성해야 함.", thought\_number: 3, total\_thoughts: 5,  

 next\_thought\_needed: true, stage: "Analysis")  

 ⎿ ## Thought 3/5 - Analysis

현재 프로젝트 디렉토리가 비어있는 상태임을 확인함. PRD 문서만 존재하는 초기 상태이므로, PRD에서 정의된 요구사항과 기술 스택을 바탕으로 AI Agent가 프로젝트를 구축할 때 따라야  

 할 구체적인 규칙들을 정의해야 함. Firebase + React + Vite + TypeScript + Tailwind  

 … +11 lines (ctrl+r to expand)

⏺ shrimp-task-manager - process\_thought (MCP)(thought: "PRD 내용을 기반으로 AI Agent가 따라야 할 구체적인 개발 규칙들을 정리해야 함: 1) 프로젝트 구조 (feature-based), 2) 기술  

 스택별 구현 규칙 (Firebase 9, React 18, Vite, TypeScript), 3) 보안 규칙 (Firestore security), 4) 성능 요구사항 (LCP <2s, 번들  

 <200KB), 5) 접근성 (WCAG 2.1 AA), 6) 국제화 (한국어/영어), 7) 테스트 전략, 8) CI/CD 파이프라인, 9) PWA 요구사항", thought\_number: 4,  

 total\_thoughts: 5, next\_thought\_needed: true, stage: "Synthesis")  

 ⎿ ## Thought 4/5 - Synthesis

PRD 내용을 기반으로 AI Agent가 따라야 할 구체적인 개발 규칙들을 정리해야 함: 1) 프로젝트 구조 (feature-based), 2) 기술 스택별 구현 규칙 (Firebase 9, React 18, Vite,  

 TypeScript), 3) 보안 규칙 (Firestore security), 4) 성능 요  

 … +11 lines (ctrl+r to expand)

⏺ shrimp-task-manager - process\_thought (MCP)(thought: "이제 shrimp-rules.md 파일을 작성할 준비가 됨. AI Agent가 TodoFlow 프로젝트를 개발할 때 즉시 이해하고 활용할 수 있도록  

 명령형 언어로 구체적인 규칙들을 작성해야 함. PRD의 모든 요구사항을 AI 작업 가이드라인으로 변환하여 파일 수정, 다중 파일 조정,  

 의사결정 기준 등을 명확히 제시해야 함.", thought\_number: 5, total\_thoughts: 5, next\_thought\_needed: false, stage: "Conclusion")  

 ⎿ ## Thought 5/5 - Conclusion

이제 shrimp-rules.md 파일을 작성할 준비가 됨. AI Agent가 TodoFlow 프로젝트를 개발할 때 즉시 이해하고 활용할 수 있도록 명령형 언어로 구체적인 규칙들을 작성해야 함. PRD의 모든  

 요구사항을 AI 작업 가이드라인으로 변환하여 파일 수정, 다중 파일 조정, 의사결정 기준 등을 명확히  

 … +16 lines (ctrl+r to expand)

⏺ Write(shrimp-rules.md)  

 ⎿ Wrote 222 lines to shrimp-rules.md   

 # TodoFlow 개발 가이드라인  

 ## 프로젝트 개요  

 - \*\*목적\*\*: Firebase Authentication 기반 개인화 실시간 To-Do List 웹 애플리케이션  

 - \*\*기술 스택\*\*: React 18 + Vite + TypeScript + Tailwind CSS + Firebase 9  

 - \*\*타겟\*\*: 반응형 PWA, WCAG 2.1 AA 준수, 한국어/영어 지원  

 ## 필수 프로젝트 아키텍처  

 … +212 lines (ctrl+r to expand)

⏺ Shrimp Task Manager MCP를 사용하여 PRD 기반 TodoFlow 프로젝트의 규칙 초기화가 완료되었습니다.

📋 생성된 프로젝트 규칙 개요

주요 구성 요소:

- 프로젝트 아키텍처: Feature-based 디렉토리 구조 정의  

 - 기술 스택 규칙: Firebase 9 + React 18 + Vite + TypeScript 구현 가이드  

 - 성능 요구사항: 번들 사이즈 200KB, LCP <2s 등 명확한 기준  

 - 보안 규칙: Firestore Security Rules 및 데이터 격리 방안  

 - 접근성 기준: WCAG 2.1 AA 준수를 위한 구체적 구현사항  

 - 국제화 설정: react-i18next 기반 한국어/영어 지원  

 - 테스트 전략: Vitest + RTL + Playwright 구성  

 - CI/CD 파이프라인: GitHub Actions 워크플로우  

 - 금지사항: 보안, 성능, 접근성 관련 절대 금지 규칙

📁 파일 위치:

c:/work/todolist/shrimp-rules.md

이제 AI Agent는 이 규칙 문서를 참조하여 PRD 요구사항을 정확히 충족하는 TodoFlow 서비스를 일관성 있게 개발할 수 있습니다.

- 실제 생성된 rule 파일 : shrimp-rules.md

더보기

- \*\*목적\*\*: Firebase Authentication 기반 개인화 실시간 To-Do List 웹 애플리케이션

- \*\*기술 스택\*\*: React 18 + Vite + TypeScript + Tailwind CSS + Firebase 9

- \*\*타겟\*\*: 반응형 PWA, WCAG 2.1 AA 준수, 한국어/영어 지원

- \*\*필수 구조를 엄격히 준수\*\*:

│ ├── todo/ # To-Do 관련 컴포넌트

- \*\*컴포넌트\*\*: PascalCase (`TodoItem.tsx`)

- \*\*훅\*\*: camelCase with use prefix (`useTodos.ts`)

- \*\*서비스\*\*: camelCase with Service suffix (`todoService.ts`)

- \*\*스토어\*\*: camelCase with Store suffix (`authStore.ts`)

- \*\*타입\*\*: PascalCase (`TodoType.ts`)

### Firebase 9 Modular SDK 규칙

- \*\*절대 Firebase v8 호환 모드 사용 금지\*\*

- \*\*Firebase 초기화는 반드시 `src/lib/firebase.ts`에서만 수행\*\*:

import { initializeApp } from 'firebase/app';

import { getAuth } from 'firebase/auth';

import { getFirestore } from 'firebase/firestore';

- \*\*환경변수는 반드시 `VITE\_` 접두사 사용\*\*

- \*\*모든 Firebase 호출은 services 폴더에서 집중 관리\*\*

- \*\*보안 규칙을 반드시 `firestore.rules` 파일에 작성\*\*:

service cloud.firestore {

match /databases/{database}/documents {

match /users/{userId}/todos/{todoId} {

allow read, create: if request.auth != null && request.auth.uid == userId;

allow update, delete: if request.auth != null

&& request.auth.uid == userId

&& resource.data.ownerUid == userId;

### React + TypeScript 필수 규칙

- \*\*모든 컴포넌트는 TypeScript로 작성\*\*

- \*\*Props 인터페이스는 반드시 정의\*\*

- \*\*useState, useEffect 등 훅 사용 시 타입 명시\*\*

- \*\*React.FC 타입 사용 금지, 함수 선언 방식 사용\*\*

- \*\*클라이언트 상태\*\*: Zustand 사용

- \*\*서버 상태\*\*: @tanstack/react-query 사용

- \*\*전역 상태 혼합 금지\*\*

- \*\*최종 번들 사이즈 200KB (gzipped) 초과 금지\*\*

- \*\*코드 분할 필수 구현\*\*:

- \*\*Vite build 설정에서 manualChunks 설정 필수\*\*

## 접근성 (WCAG 2.1 AA) 필수 구현

- \*\*모든 이미지에 alt 텍스트 필수\*\*

- \*\*색상 대비비 4.5:1 이상 필수 유지\*\*

- \*\*키보드 탐색 지원 필수\*\*

- \*\*Tailwind 접근성 클래스 활용\*\*:

- `sr-only` 스크린 리더 전용 텍스트

- `focus:ring-2` 포커스 표시

- \*\*색상만으로 정보 전달 금지\*\*

- \*\*자동 재생 미디어 금지\*\*

## 국제화 (i18n) 필수 구현

### react-i18next 구현 규칙

- \*\*모든 텍스트는 번역 키로 관리\*\*

- \*\*하드코딩된 텍스트 사용 금지\*\*

- \*\*번역 파일 구조\*\*:

- \*\*컴포넌트에서 useTranslation 훅 사용 필수\*\*

## Firebase 비용 최적화 필수 규칙

- \*\*불필요한 실시간 리스너 생성 금지\*\*

- \*\*페이지네이션 없는 대량 데이터 조회 금지\*\*

- \*\*복합 쿼리 사용 시 인덱스 생성 필수\*\*

- \*\*로컬 캐싱으로 중복 쿼리 방지 필수\*\*

- \*\*onSnapshot 리스너 정리 누락 금지\*\*

- \*\*where 조건 없는 전체 컬렉션 조회 금지\*\*

- \*\*오프라인 폴백 페이지 제공\*\*

- \*\*Unit Tests\*\*: Vitest + React Testing Library

- \*\*E2E Tests\*\*: Playwright

- \*\*최소 커버리지\*\*: 80% 이상 필수 달성

- \*\*모든 CRUD 동작 테스트\*\*

- \*\*크로스 브라우저 테스트\*\*

- \*\*테스트 실패 시 배포 중단 필수\*\*

- \*\*린트 검사 통과 필수\*\*

- \*\*번들 사이즈 체크 필수\*\*

- \*\*`firebase.ts` 수정 시\*\*: `firestore.rules` 동시 업데이트

- \*\*컴포넌트 추가 시\*\*: `types/` 폴더 타입 정의 동시 추가

- \*\*새 페이지 추가 시\*\*: 라우터 설정, 번역 키 동시 추가

- \*\*환경변수 추가 시\*\*: `.env.example` 동시 업데이트

## AI 의사결정 기준

1. \*\*보안\*\* > 성능 > 사용자 경험 > 개발 편의성

2. \*\*접근성\*\* > 디자인 > 기능 복잡성

3. \*\*타입 안전성\*\* > 코드 간결성

- \*\*Firebase 기능 활용\*\* > 서드파티 라이브러리

- \*\*Tailwind 유틸리티\*\* > 커스텀 CSS

- \*\*React 표준 패턴\*\* > 커스텀 솔루션

- \*\*Firebase 키를 코드에 직접 노출 금지\*\*

- \*\*사용자 데이터 크로스 액세스 허용 금지\*\*

- \*\*클라이언트에서 민감 정보 저장 금지\*\*

- \*\*번들 사이즈 한도 초과 금지\*\*

- \*\*불필요한 리렌더링 발생 코드 금지\*\*

- \*\*메모리 누수 발생 패턴 금지\*\*

- \*\*키보드 접근 불가능한 UI 생성 금지\*\*

- \*\*스크린 리더 미지원 컴포넌트 금지\*\*

**3. 태스크 계획 : plan\_task**

![](https://blog.kakaocdn.net/dna/cykQyy/btsPZgr1Dzw/AAAAAAAAAAAAAAAAAAAAAJvxiXxfRurR_R-rMSnnnpPg1GhWyRC-QelGRpH_5BBj/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=6soTblcs9rFlYCF55I0IM9DapFE%3D)
**> plan task** 연구계획을 토대로 1주일 안에 개발할 수 있도록 계획을 세워줘.

- 출력내용

```
> plan task: 연구계획을 토대로 1주일 안에 개발할 수 있도록 계획을 세워줘.
  ⎿  Found 68 new diagnostic issues in 1 file (ctrl-r to expand)

⏺ Shrimp Task Manager를 사용하여 연구계획을 기반으로 1주일 개발 계획을 수립하겠습니다.

⏺ shrimp-task-manager - plan_task (MCP)(description: "TodoFlow Firebase 기반 React To-Do List 서비스를 1주일 내에 MVP로 개발하는 계획 수립. PRD 요구사항과 기술 연구 결과를
                                       바탕으로 실현 가능한 개발 일정과 우선순위를 설정하여 핵심 기능 중심의 실용적 개발 계획을 만들어야 함. 기술 스택: React 18 + Vite +
                                       TypeScript + Firebase 9 + Tailwind CSS", requirements: "성능 요구사항(LCP <2s, 번들 <200KB), 접근성(WCAG 2.1 AA), 반응형 디자인, 실시간
                                       동기화, 사용자 인증, To-Do CRUD, 필터/정렬, 국제화(한국어/영어), PWA 기능, CI/CD 파이프라인 포함", existingTasksReference: false)
  ⎿  ## Task Analysis                                                                                                                                             

     You must complete the following sub-steps in sequence, and at the end call the `analyze_task` tool to pass the preliminary design solution to the next stage.
     … +94 lines (ctrl+r to expand)

⏺ Read(shrimp-rules.md)
  ⎿  Read 222 lines (ctrl+r to expand)

⏺ Read(c:/work/workspace/todolist/prd.md)
  ⎿  Read 100 lines (ctrl+r to expand)

⏺ shrimp-task-manager - analyze_task (MCP)(summary: "TodoFlow Firebase 기반 React To-Do List 서비스를 1주일(7일) 내 MVP 개발 완료를 목표로 하는 계획 수립 작업. PRD와 기술 연구
                                          결과를 바탕으로 핵심 기능 우선순위 설정 및 실현 가능한 개발 일정 구성이 필요함. 기술 스택은 React 18 + Vite + TypeScript + Firebase 9 +
                                          Tailwind CSS이며, shrimp-rules.md에 정의된 아키텍처 규칙을 준수해야 함.", initialConcept: "1주일 MVP 개발을 위한 단계별 계획:\n\n**Day
                                          1-2: 프로젝트 기반 구축**\n- Vite + React + TypeScript 프로젝트 초기화\n- Firebase 프로젝트 설정 및 환경변수 구성\n- shrimp-rules.md
                                          규칙에 따른 디렉토리 구조 생성\n- 기본 라우팅 및 인증 UI 구현\n\n**Day 3-4: 핵심 기능 개발**\n- Firebase Authentication 구현 (Google,
                                          Email/Password)\n- Firestore 스키마 설계 및 보안 규칙 작성\n- To-Do CRUD 기본 기능 구현\n- Zustand + React Query 상태 관리 연동\n\n**Day
                                           5-6: UI/UX 완성 및 최적화**\n- Tailwind CSS 반응형 디자인 적용\n- 기본 접근성(WCAG 2.1 AA) 구현\n- react-i18next 국제화 설정
                                          (한국어/영어)\n- 필터/정렬 기능 구현\n\n**Day 7: 테스트 및 배포**\n- 핵심 기능 테스트 작성 (Vitest + RTL)\n- GitHub Actions CI/CD
                                          파이프라인 구축\n- Firebase Hosting 배포\n- 성능 최적화 (번들 사이즈 <200KB, LCP <2s)\n\n우선순위: 보안 > 핵심 CRUD > 인증 > 반응형 UI >
                                           성능 최적화 > 테스트/배포")
  ⎿  ## Codebase Analysis                                                                                                                           

     After receiving the initial solution, complete the following checks and optimizations in sequence, and call the `reflect_task` tool at the end:
     … +54 lines (ctrl+r to expand)

⏺ shrimp-task-manager - reflect_task (MCP)(summary: "TodoFlow Firebase 기반 React To-Do List 서비스를 1주일 내 MVP 개발 완료를 목표로 하는 계획 수립. PRD 요구사항과
                                          shrimp-rules.md 아키텍처 규칙을 기반으로 실현 가능한 7일 개발 일정과 우선순위를 설정하여 핵심 기능 중심의 실용적 개발 로드맵 구성",
                                          analysis: "**구조적 무결성 검증:**\n- PRD의 모든 필수 요구사항(인증, CRUD, 필터/정렬, 실시간 동기화) 포함 확인\n- shrimp-rules.md의
                                          아키텍처 규칙(feature-based 구조, Firebase 9 modular SDK, TypeScript 필수) 완전 준수\n- 의존성 그래프: Firebase(인프라) →
                                          Services(비즈니스 로직) → Stores(상태) → Components(UI) 계층 구조\n- 모듈 경계: auth, todo, ui 컴포넌트 분리, hooks/stores/services
                                          계층별 구성\n\n**중복 기능 검토 및 재사용성 평가:**\n- 현재 프로젝트가 빈 디렉토리 상태로 기존 코드 중복 없음\n- shrimp-rules.md 규칙에
                                          따른 feature-based 구조로 향후 확장성 고려\n- 재사용 가능한 UI 컴포넌트(Button, Input, Modal) 우선 개발로 일관성 확보\n- Firebase 서비스
                                           계층을 추상화하여 향후 백엔드 변경 시 확장성 보장\n\n**성능 및 확장성 평가:**\n- 번들 사이즈 200KB 제한 준수를 위한 코드 분할 전략
                                          필요\n- React Query 캐싱으로 Firestore 읽기 비용 최적화\n- Zustand 클라이언트 상태와 React Query 서버 상태 분리로 성능 최적화\n-
                                          onSnapshot 실시간 리스너 최적화로 불필요한 리렌더링 방지\n\n**일관성 및 스타일 검증:**\n- TypeScript 타입 정의 필수, React.FC 사용 금지
                                          규칙 준수\n- PascalCase 컴포넌트, camelCase 훅/서비스 명명 규칙 적용\n- Tailwind CSS 유틸리티 우선 사용, 커스텀 CSS 최소화\n- WCAG 2.1
                                          AA 접근성 기준 준수를 위한 체크리스트 구성\n\n**아키텍처 통합 평가:**\n- Firebase 9 modular SDK 완전 활용으로 최신 모범 사례 준수\n-
                                          환경변수 VITE_ 접두사 사용, 보안 규칙 firestore.rules 분리 관리\n- CI/CD 파이프라인과 테스트 전략이 개발 워크플로우와 완전 통합\n- PWA
                                          기능은 기본 구현으로 제한하여 1주일 일정 내 완성 가능성 보장\n\n**최적화 제안:**\n1. **우선순위 재조정**: 보안(인증+Firestore 규칙) →
                                          핵심 CRUD → 기본 UI → 성능 최적화 순서\n2. **MVP 범위 조정**: PWA는 manifest.json만 우선 구현, Service Worker는 선택사항으로 조정\n3.
                                          **테스트 범위**: 핵심 기능(인증, CRUD) 중심의 단위 테스트 우선, E2E는 배포 후 추가\n4. **성능 모니터링**: 개발 중 번들 사이즈 실시간
                                          체크를 위한 Vite 플러그인 활용")
  ⎿  ## Reflection Results                                                                                                      

     After receiving the solution and suggestions, conduct self-reflection and final confirmation, and submit the final results:
     … +48 lines (ctrl+r to expand)

⏺ shrimp-task-manager - split_tasks (MCP)(updateMode: "clearAllTasks", globalAnalysisResult: "TodoFlow Firebase 기반 React To-Do List 서비스를 1주일 내 MVP 개발 완료. 핵심
                                         기능(인증, CRUD, 실시간 동기화, 반응형 UI) 중심으로 구현하며, 성능 최적화(번들 <200KB, LCP <2s)와 접근성(WCAG 2.1 AA) 기준을 준수하는
                                         실용적 개발 계획", tasksRaw: "[\n  {\n    \"name\": \"프로젝트 초기화 및 기본 설정\",\n    \"description\": \"Vite + React + TypeScript
                                         프로젝트를 생성하고 필수 디펜던시를 설치합니다. shrimp-rules.md에 정의된 디렉토리 구조를 생성하고, Tailwind CSS, ESLint, Prettier 등 개발
                                          환경을 설정합니다.\",\n    \"implementationGuide\": \"1. `npm create vite@latest todoflow -- --template react-ts` 실행\\\\n2. 필수
                                         패키지 설치: firebase, @tanstack/react-query, zustand, tailwindcss, react-i18next, react-router-dom\\\\n3. src/ 디렉토리 구조 생성:
                                         components/{ui,todo,auth}/, pages/, hooks/, stores/, services/, lib/, types/, locales/\\\\n4. tailwind.config.js, vite.config.ts,
                                         tsconfig.json 설정\\\\n5. .env.example 파일 생성\",\n    \"dependencies\": [],\n    \"relatedFiles\": [\n      {\n        \"path\":
                                         \"package.json\",\n        \"type\": \"CREATE\",\n        \"description\": \"프로젝트 디펜던시 및 스크립트 정의\"\n      },\n      {\n
                                              \"path\": \"vite.config.ts\",\n        \"type\": \"CREATE\",\n        \"description\": \"Vite 빌드 설정 및 성능 최적화\"\n      },\n
                                               {\n        \"path\": \"tailwind.config.js\",\n        \"type\": \"CREATE\",\n        \"description\": \"Tailwind CSS 커스텀
                                         설정\"\n      },\n      {\n        \"path\": \".env.example\",\n        \"type\": \"CREATE\",\n        \"description\": \"환경변수
                                         템플릿\"\n      },\n      {\n        \"path\": \"tsconfig.json\",\n        \"type\": \"CREATE\",\n        \"description\": \"TypeScript
                                         컴파일러 설정\"\n      }\n    ],\n    \"verificationCriteria\": \"프로젝트가 정상적으로 빌드되고 개발 서버가 실행되며, 모든 필수 패키지가
                                          설치되고 디렉토리 구조가 shrimp-rules.md 규칙에 맞게 생성되었는지 확인\"\n  },\n  {\n    \"name\": \"Firebase 프로젝트 설정 및
                                         초기화\",\n    \"description\": \"Firebase 프로젝트를 생성하고 Authentication과 Firestore를 활성화합니다. Firebase SDK를 초기화하고
                                         환경변수를 설정합니다.\",\n    \"implementationGuide\": \"1. Firebase Console에서 새 프로젝트 생성\\\\n2. Authentication 활성화 (Google,
                                         Email/Password 공급자 설정)\\\\n3. Firestore 데이터베이스 생성 (test mode로 시작)\\\\n4. Firebase Hosting 활성화\\\\n5.
                                         src/lib/firebase.ts 파일 생성 및 Firebase SDK 초기화\\\\n6. 환경변수 설정 (.env 파일에 VITE_ 접두사로 Firebase config 추가)\",\n
                                         \"dependencies\": [\"프로젝트 초기화 및 기본 설정\"],\n    \"relatedFiles\": [\n      {\n        \"path\": \"src/lib/firebase.ts\",\n
                                             \"type\": \"CREATE\",\n        \"description\": \"Firebase SDK 초기화 및 설정\"\n      },\n      {\n        \"path\": \".env\",\n
                                             \"type\": \"CREATE\",\n        \"description\": \"Firebase 환경변수 설정\"\n      },\n      {\n        \"path\":
                                         \"firestore.rules\",\n        \"type\": \"CREATE\",\n        \"description\": \"Firestore 보안 규칙\"\n      },\n      {\n
                                         \"path\": \"firebase.json\",\n        \"type\": \"CREATE\",\n        \"description\": \"Firebase 프로젝트 설정\"\n      }\n    ],\n
                                         \"verificationCriteria\": \"Firebase 콘솔에서 프로젝트가 정상 생성되고, Authentication과 Firestore가 활성화되며, 로컬에서 Firebase SDK
                                         연결이 정상 작동하는지 확인\"\n  },\n  {\n    \"name\": \"TypeScript 타입 정의 및 기본 인터페이스\",\n    \"description\": \"Todo 데이터
                                         모델과 사용자 인증 관련 TypeScript 타입을 정의합니다. PRD에 명시된 데이터 구조에 맞는 인터페이스를 생성합니다.\",\n
                                         \"implementationGuide\": \"1. src/types/todo.ts: Todo 인터페이스 정의 (title, description, completed, dueDate, priority, tags, ownerUid,
                                         createdAt, updatedAt)\\\\n2. src/types/auth.ts: User 타입 정의 (Firebase User 확장)\\\\n3. src/types/common.ts: 공통 타입 정의 (Priority
                                         enum, Filter, Sort 타입)\\\\n4. 모든 타입에 JSDoc 주석 추가\",\n    \"dependencies\": [\"Firebase 프로젝트 설정 및 초기화\"],\n
                                         \"relatedFiles\": [\n      {\n        \"path\": \"src/types/todo.ts\",\n        \"type\": \"CREATE\",\n        \"description\": \"Todo
                                         관련 TypeScript 타입 정의\"\n      },\n      {\n        \"path\": \"src/types/auth.ts\",\n        \"type\": \"CREATE\",\n
                                         \"description\": \"인증 관련 TypeScript 타입 정의\"\n      },\n      {\n        \"path\": \"src/types/common.ts\",\n        \"type\":
                                         \"CREATE\",\n        \"description\": \"공통 TypeScript 타입 정의\"\n      },\n      {\n        \"path\": \"src/types/index.ts\",\n
                                           \"type\": \"CREATE\",\n        \"description\": \"타입 정의 export 집합\"\n      }\n    ],\n    \"verificationCriteria\": \"모든 타입이
                                          정확히 정의되고, TypeScript 컴파일 에러가 없으며, PRD 데이터 모델과 완전히 일치하는지 확인\"\n  },\n  {\n    \"name\": \"Firebase
                                         Authentication 서비스 구현\",\n    \"description\": \"Firebase Authentication을 사용한 로그인, 회원가입, 로그아웃 기능을 구현합니다.
                                         Google OAuth와 Email/Password 인증을 지원합니다.\",\n    \"implementationGuide\": \"1. src/services/authService.ts: 인증 관련 함수
                                         구현\\\\n   - signInWithEmailAndPassword, createUserWithEmailAndPassword\\\\n   - signInWithPopup (Google), signOut,
                                         sendPasswordResetEmail\\\\n2. 에러 처리 및 한국어 에러 메시지 매핑\\\\n3. 인증 상태 변화 감지 함수 구현\\\\n4. 모든 함수에 적절한 타입
                                         적용 및 에러 핸들링\",\n    \"dependencies\": [\"TypeScript 타입 정의 및 기본 인터페이스\"],\n    \"relatedFiles\": [\n      {\n
                                         \"path\": \"src/services/authService.ts\",\n        \"type\": \"CREATE\",\n        \"description\": \"Firebase Authentication 서비스
                                         구현\"\n      },\n      {\n        \"path\": \"src/lib/firebase.ts\",\n        \"type\": \"TO_MODIFY\",\n        \"description\":
                                         \"Firebase Authentication 설정 추가\"\n      }\n    ],\n    \"verificationCriteria\": \"이메일/패스워드 및 Google 로그인이 정상 작동하고,
                                          에러 처리가 적절히 구현되며, 한국어 에러 메시지가 표시되는지 확인\"\n  },\n  {\n    \"name\": \"Firestore Todo 서비스 구현\",\n
                                         \"description\": \"Firestore를 사용한 Todo CRUD 작업과 실시간 동기화 기능을 구현합니다. 사용자별 데이터 격리와 보안 규칙을
                                         적용합니다.\",\n    \"implementationGuide\": \"1. src/services/todoService.ts: Todo CRUD 함수 구현\\\\n   - createTodo, getTodos,
                                         updateTodo, deleteTodo, toggleTodoComplete\\\\n   - 실시간 리스너: subscribeToTodos (onSnapshot 사용)\\\\n   - 필터링 및 정렬 쿼리
                                         함수\\\\n2. Firestore 보안 규칙 업데이트 (users/{uid}/todos 경로)\\\\n3. 서버 타임스탬프 사용 및 사용자 UID 검증\\\\n4. 배치 작업 및
                                         트랜잭션 처리 구현\",\n    \"dependencies\": [\"Firebase Authentication 서비스 구현\"],\n    \"relatedFiles\": [\n      {\n
                                         \"path\": \"src/services/todoService.ts\",\n        \"type\": \"CREATE\",\n        \"description\": \"Firestore Todo CRUD 서비스 구현\"\n
                                               },\n      {\n        \"path\": \"firestore.rules\",\n        \"type\": \"TO_MODIFY\",\n        \"description\": \"사용자별 Todo
                                         데이터 보안 규칙\"\n      },\n      {\n        \"path\": \"src/lib/firebase.ts\",\n        \"type\": \"TO_MODIFY\",\n
                                         \"description\": \"Firestore 설정 추가\"\n      }\n    ],\n    \"verificationCriteria\": \"Todo CRUD 작업이 정상 실행되고, 실시간
                                         동기화가 작동하며, 사용자별 데이터 격리가 보안 규칙으로 보장되는지 확인\"\n  },\n  {\n    \"name\": \"상태 관리 구현 (Zustand + React
                                         Query)\",\n    \"description\": \"Zustand를 사용한 클라이언트 상태와 React Query를 사용한 서버 상태 관리를 구현합니다. 인증 상태와 Todo
                                         데이터 관리를 분리합니다.\",\n    \"implementationGuide\": \"1. src/stores/authStore.ts: Zustand로 인증 상태 관리\\\\n   - user,
                                         isLoading, error 상태\\\\n   - login, logout, checkAuth 액션\\\\n2. src/lib/queryClient.ts: React Query 설정\\\\n3.
                                         src/hooks/useTodos.ts: Todo 데이터 React Query 훅\\\\n   - useQuery, useMutation, useInfiniteQuery\\\\n4. src/hooks/useAuth.ts: 인증 상태
                                          커스텀 훅\\\\n5. 실시간 동기화를 위한 queryClient.invalidateQueries 연동\",\n    \"dependencies\": [\"Firestore Todo 서비스 구현\"],\n
                                           \"relatedFiles\": [\n      {\n        \"path\": \"src/stores/authStore.ts\",\n        \"type\": \"CREATE\",\n        \"description\":
                                         \"Zustand 인증 상태 관리\"\n      },\n      {\n        \"path\": \"src/lib/queryClient.ts\",\n        \"type\": \"CREATE\",\n
                                         \"description\": \"React Query 클라이언트 설정\"\n      },\n      {\n        \"path\": \"src/hooks/useTodos.ts\",\n        \"type\":
                                         \"CREATE\",\n        \"description\": \"Todo 데이터 React Query 훅\"\n      },\n      {\n        \"path\": \"src/hooks/useAuth.ts\",\n
                                              \"type\": \"CREATE\",\n        \"description\": \"인증 상태 커스텀 훅\"\n      }\n    ],\n    \"verificationCriteria\": \"상태
                                         관리가 정상 작동하고, 클라이언트/서버 상태가 적절히 분리되며, 실시간 업데이트가 UI에 반영되는지 확인\"\n  },\n  {\n    \"name\": \"재사용
                                          가능한 UI 컴포넌트 구현\",\n    \"description\": \"Tailwind CSS를 사용하여 일관성 있는 UI 컴포넌트를 구현합니다. 접근성 기준을 준수하고
                                         반응형 디자인을 적용합니다.\",\n    \"implementationGuide\": \"1. src/components/ui/Button.tsx: 다양한 variant 지원 버튼\\\\n2.
                                         src/components/ui/Input.tsx: 폼 입력 컴포넌트\\\\n3. src/components/ui/Modal.tsx: 모달 다이얼로그\\\\n4. src/components/ui/Checkbox.tsx:
                                         체크박스 컴포넌트\\\\n5. src/components/ui/Select.tsx: 드롭다운 선택\\\\n6. 모든 컴포넌트에 ARIA 라벨, 키보드 탐색, 포커스 관리
                                         적용\\\\n7. Tailwind 접근성 클래스 (sr-only, focus:ring-2) 활용\",\n    \"dependencies\": [\"상태 관리 구현 (Zustand + React Query)\"],\n
                                             \"relatedFiles\": [\n      {\n        \"path\": \"src/components/ui/Button.tsx\",\n        \"type\": \"CREATE\",\n
                                         \"description\": \"재사용 가능한 버튼 컴포넌트\"\n      },\n      {\n        \"path\": \"src/components/ui/Input.tsx\",\n
                                         \"type\": \"CREATE\",\n        \"description\": \"폼 입력 컴포넌트\"\n      },\n      {\n        \"path\":
                                         \"src/components/ui/Modal.tsx\",\n        \"type\": \"CREATE\",\n        \"description\": \"모달 다이얼로그 컴포넌트\"\n      },\n
                                         {\n        \"path\": \"src/components/ui/Checkbox.tsx\",\n        \"type\": \"CREATE\",\n        \"description\": \"체크박스 컴포넌트\"\n
                                               },\n      {\n        \"path\": \"src/components/ui/Select.tsx\",\n        \"type\": \"CREATE\",\n        \"description\":
                                         \"드롭다운 선택 컴포넌트\"\n      },\n      {\n        \"path\": \"src/components/ui/index.ts\",\n        \"type\": \"CREATE\",\n
                                         \"description\": \"UI 컴포넌트 export 집합\"\n      }\n    ],\n    \"verificationCriteria\": \"모든 UI 컴포넌트가 접근성 기준을 만족하고,
                                          키보드 탐색이 가능하며, 반응형 디자인이 적용되어 있는지 확인\"\n  },\n  {\n    \"name\": \"인증 관련 컴포넌트 및 페이지 구현\",\n
                                         \"description\": \"로그인, 회원가입, 비밀번호 재설정 기능이 포함된 인증 페이지와 컴포넌트를 구현합니다.\",\n    \"implementationGuide\":
                                         \"1. src/components/auth/LoginForm.tsx: 이메일/패스워드 로그인\\\\n2. src/components/auth/SignupForm.tsx: 회원가입 폼\\\\n3.
                                         src/components/auth/GoogleSignInButton.tsx: Google OAuth 버튼\\\\n4. src/components/auth/ResetPasswordForm.tsx: 패스워드 재설정\\\\n5.
                                         src/pages/SignIn.tsx: 통합 인증 페이지\\\\n6. 폼 검증, 로딩 상태, 에러 처리 구현\\\\n7. 한국어 에러 메시지 및 성공 메시지\",\n
                                         \"dependencies\": [\"재사용 가능한 UI 컴포넌트 구현\"],\n    \"relatedFiles\": [\n      {\n        \"path\":
                                         \"src/components/auth/LoginForm.tsx\",\n        \"type\": \"CREATE\",\n        \"description\": \"이메일/패스워드 로그인 폼\"\n      },\n
                                               {\n        \"path\": \"src/components/auth/SignupForm.tsx\",\n        \"type\": \"CREATE\",\n        \"description\": \"회원가입 폼
                                          컴포넌트\"\n      },\n      {\n        \"path\": \"src/components/auth/GoogleSignInButton.tsx\",\n        \"type\": \"CREATE\",\n
                                          \"description\": \"Google OAuth 로그인 버튼\"\n      },\n      {\n        \"path\": \"src/pages/SignIn.tsx\",\n        \"type\":
                                         \"CREATE\",\n        \"description\": \"통합 인증 페이지\"\n      },\n      {\n        \"path\": \"src/components/auth/index.ts\",\n
                                            \"type\": \"CREATE\",\n        \"description\": \"인증 컴포넌트 export 집합\"\n      }\n    ],\n    \"verificationCriteria\":
                                         \"로그인/회원가입이 정상 작동하고, 폼 검증이 적절히 구현되며, 에러 상황에 대한 사용자 피드백이 제공되는지 확인\"\n  },\n  {\n
                                         \"name\": \"Todo 관련 컴포넌트 구현\",\n    \"description\": \"Todo 생성, 수정, 삭제, 완료 토글 기능이 포함된 컴포넌트를 구현합니다.
                                         필터링과 정렬 기능도 포함합니다.\",\n    \"implementationGuide\": \"1. src/components/todo/TodoItem.tsx: 개별 Todo 아이템\\\\n   - 완료
                                         토글, 인라인 편집, 삭제 기능\\\\n2. src/components/todo/TodoList.tsx: Todo 목록 컨테이너\\\\n3. src/components/todo/TodoForm.tsx: Todo
                                         생성/수정 폼\\\\n4. src/components/todo/TodoFilters.tsx: 필터 및 정렬 컨트롤\\\\n5. src/components/todo/TodoStats.tsx: 통계 정보
                                         표시\\\\n6. 드래그 앤 드롭, 키보드 단축키 지원\\\\n7. 무한 스크롤 또는 페이지네이션 구현\",\n    \"dependencies\": [\"인증 관련 컴포넌트
                                         및 페이지 구현\"],\n    \"relatedFiles\": [\n      {\n        \"path\": \"src/components/todo/TodoItem.tsx\",\n        \"type\":
                                         \"CREATE\",\n        \"description\": \"개별 Todo 아이템 컴포넌트\"\n      },\n      {\n        \"path\":
                                         \"src/components/todo/TodoList.tsx\",\n        \"type\": \"CREATE\",\n        \"description\": \"Todo 목록 컨테이너\"\n      },\n
                                         {\n        \"path\": \"src/components/todo/TodoForm.tsx\",\n        \"type\": \"CREATE\",\n        \"description\": \"Todo 생성/수정
                                         폼\"\n      },\n      {\n        \"path\": \"src/components/todo/TodoFilters.tsx\",\n        \"type\": \"CREATE\",\n
                                         \"description\": \"필터 및 정렬 컨트롤\"\n      },\n      {\n        \"path\": \"src/components/todo/index.ts\",\n        \"type\":
                                         \"CREATE\",\n        \"description\": \"Todo 컴포넌트 export 집합\"\n      }\n    ],\n    \"verificationCriteria\": \"Todo CRUD 작업이
                                         UI에서 정상 실행되고, 필터/정렬이 작동하며, 실시간 업데이트가 반영되는지 확인\"\n  },\n  {\n    \"name\": \"메인 TodoApp 페이지 및 라우팅
                                          구현\",\n    \"description\": \"Todo 애플리케이션의 메인 페이지와 React Router를 사용한 라우팅을 구현합니다. 인증 가드와 레이아웃을
                                         포함합니다.\",\n    \"implementationGuide\": \"1. src/pages/TodoApp.tsx: 메인 Todo 애플리케이션 페이지\\\\n2. src/components/Layout.tsx:
                                         공통 레이아웃 컴포넌트\\\\n3. src/App.tsx: 라우터 설정 및 전역 프로바이더\\\\n4. 보호된 라우트 (ProtectedRoute) 구현\\\\n5. 로딩 스피너
                                         및 에러 바운더리 구현\\\\n6. 반응형 네비게이션 (모바일 햄버거 메뉴)\\\\n7. 사용자 프로필 드롭다운 메뉴\",\n    \"dependencies\": [\"Todo
                                         관련 컴포넌트 구현\"],\n    \"relatedFiles\": [\n      {\n        \"path\": \"src/pages/TodoApp.tsx\",\n        \"type\": \"CREATE\",\n
                                               \"description\": \"메인 Todo 애플리케이션 페이지\"\n      },\n      {\n        \"path\": \"src/components/Layout.tsx\",\n
                                         \"type\": \"CREATE\",\n        \"description\": \"공통 레이아웃 컴포넌트\"\n      },\n      {\n        \"path\": \"src/App.tsx\",\n
                                           \"type\": \"CREATE\",\n        \"description\": \"애플리케이션 루트 컴포넌트\"\n      },\n      {\n        \"path\":
                                         \"src/components/ProtectedRoute.tsx\",\n        \"type\": \"CREATE\",\n        \"description\": \"인증 가드 컴포넌트\"\n      },\n
                                         {\n        \"path\": \"src/main.tsx\",\n        \"type\": \"TO_MODIFY\",\n        \"description\": \"애플리케이션 진입점\"\n      }\n
                                         ],\n    \"verificationCriteria\": \"라우팅이 정상 작동하고, 인증되지 않은 사용자는 로그인 페이지로 리다이렉트되며, 반응형 레이아웃이
                                         적용되는지 확인\"\n  },\n  {\n    \"name\": \"국제화 (i18n) 설정 및 다국어 지원\",\n    \"description\": \"react-i18next를 사용하여
                                         한국어와 영어 지원을 구현합니다. 모든 텍스트를 번역 키로 관리합니다.\",\n    \"implementationGuide\": \"1. src/lib/i18n.ts: react-i18next
                                          설정\\\\n2. src/locales/ko/translation.json: 한국어 번역\\\\n3. src/locales/en/translation.json: 영어 번역\\\\n4. 언어 선택 컴포넌트
                                         구현\\\\n5. 모든 하드코딩된 텍스트를 번역 키로 교체\\\\n6. 날짜/시간 포맷팅 현지화\\\\n7. 언어별 폰트 및 레이아웃 조정\",\n
                                         \"dependencies\": [\"메인 TodoApp 페이지 및 라우팅 구현\"],\n    \"relatedFiles\": [\n      {\n        \"path\": \"src/lib/i18n.ts\",\n
                                               \"type\": \"CREATE\",\n        \"description\": \"react-i18next 설정\"\n      },\n      {\n        \"path\":
                                         \"src/locales/ko/translation.json\",\n        \"type\": \"CREATE\",\n        \"description\": \"한국어 번역 파일\"\n      },\n      {\n
                                               \"path\": \"src/locales/en/translation.json\",\n        \"type\": \"CREATE\",\n        \"description\": \"영어 번역 파일\"\n
                                         },\n      {\n        \"path\": \"src/components/LanguageSelector.tsx\",\n        \"type\": \"CREATE\",\n        \"description\": \"언어
                                         선택 컴포넌트\"\n      }\n    ],\n    \"verificationCriteria\": \"언어 전환이 정상 작동하고, 모든 텍스트가 선택된 언어로 표시되며, 날짜
                                         포맷이 현지화되어 있는지 확인\"\n  },\n  {\n    \"name\": \"성능 최적화 및 번들 사이즈 관리\",\n    \"description\": \"코드 분할, lazy
                                         loading, 번들 최적화를 구현하여 200KB 제한을 준수하고 성능 메트릭을 달성합니다.\",\n    \"implementationGuide\": \"1. React.lazy를 사용한
                                          페이지별 코드 분할\\\\n2. Vite manualChunks 설정으로 라이브러리 분할\\\\n3. 이미지 최적화 및 lazy loading\\\\n4. React.memo, useMemo,
                                         useCallback 적절한 사용\\\\n5. 번들 사이즈 분석기 설정\\\\n6. Tree shaking 최적화\\\\n7. 불필요한 리렌더링 방지\\\\n8. Lighthouse 성능
                                         테스트 및 개선\",\n    \"dependencies\": [\"국제화 (i18n) 설정 및 다국어 지원\"],\n    \"relatedFiles\": [\n      {\n        \"path\":
                                         \"vite.config.ts\",\n        \"type\": \"TO_MODIFY\",\n        \"description\": \"번들 최적화 설정\"\n      },\n      {\n
                                         \"path\": \"src/utils/lazyImports.ts\",\n        \"type\": \"CREATE\",\n        \"description\": \"lazy import 유틸리티\"\n      }\n
                                         ],\n    \"verificationCriteria\": \"번들 사이즈가 200KB 이하이고, LCP < 2초, FID < 100ms, CLS < 0.1 성능 기준을 달성했는지 확인\"\n  },\n
                                           {\n    \"name\": \"테스트 구현 및 품질 보장\",\n    \"description\": \"Vitest와 React Testing Library를 사용하여 핵심 기능의 단위
                                         테스트를 구현합니다. 80% 이상의 코드 커버리지를 달성합니다.\",\n    \"implementationGuide\": \"1. vitest.config.ts 설정\\\\n2.
                                         src/components/**/__tests__/ 디렉토리에 컴포넌트 테스트\\\\n3. src/services/__tests__/ 디렉토리에 서비스 테스트\\\\n4.
                                         src/hooks/__tests__/ 디렉토리에 커스텀 훅 테스트\\\\n5. 인증 플로우 통합 테스트\\\\n6. Todo CRUD 작업 테스트\\\\n7. 접근성 테스트
                                         (axe-core 사용)\\\\n8. 커버리지 리포트 생성\",\n    \"dependencies\": [\"성능 최적화 및 번들 사이즈 관리\"],\n    \"relatedFiles\": [\n
                                             {\n        \"path\": \"vitest.config.ts\",\n        \"type\": \"CREATE\",\n        \"description\": \"Vitest 설정 파일\"\n      },\n
                                              {\n        \"path\": \"src/utils/testUtils.tsx\",\n        \"type\": \"CREATE\",\n        \"description\": \"테스트 유틸리티
                                         함수\"\n      },\n      {\n        \"path\": \"src/components/__tests__/\",\n        \"type\": \"CREATE\",\n        \"description\":
                                         \"컴포넌트 테스트 디렉토리\"\n      }\n    ],\n    \"verificationCriteria\": \"모든 테스트가 통과하고, 코드 커버리지가 80% 이상이며,
                                         접근성 테스트가 성공하는지 확인\"\n  },\n  {\n    \"name\": \"CI/CD 파이프라인 구축 및 배포\",\n    \"description\": \"GitHub Actions를
                                         사용하여 자동화된 테스트, 빌드, 배포 파이프라인을 구축합니다. Firebase Hosting에 자동 배포를 설정합니다.\",\n    \"implementationGuide\":
                                          \"1. .github/workflows/deploy.yml 워크플로우 생성\\\\n2. 테스트, 린트, 타입체크 단계 설정\\\\n3. Firebase Hosting 자동 배포 설정\\\\n4.
                                         환경변수 및 시크릿 관리\\\\n5. 번들 사이즈 체크 및 성능 테스트 통합\\\\n6. PR별 프리뷰 배포 설정\\\\n7. 배포 상태 알림 설정\",\n
                                         \"dependencies\": [\"테스트 구현 및 품질 보장\"],\n    \"relatedFiles\": [\n      {\n        \"path\":
                                         \".github/workflows/deploy.yml\",\n        \"type\": \"CREATE\",\n        \"description\": \"CI/CD 파이프라인 워크플로우\"\n      },\n
                                            {\n        \"path\": \".github/workflows/pr-preview.yml\",\n        \"type\": \"CREATE\",\n        \"description\": \"PR 프리뷰 배포
                                         워크플로우\"\n      }\n    ],\n    \"verificationCriteria\": \"CI/CD 파이프라인이 정상 실행되고, 모든 체크가 통과하며, Firebase Hosting에
                                          성공적으로 배포되는지 확인\"\n  }\n]")
  ⎿  ## Task Splitting - clearAllTasks Mode

     ## Splitting Strategy
     … +213 lines (ctrl+r to expand)

⏺ ✅ 1주일 TodoFlow 개발 계획이 성공적으로 수립되었습니다!

  📋 완료된 작업 계획 개요

  총 14개 작업으로 체계적 분할:
  - 기반 구축 (1-3일): 프로젝트 초기화, Firebase 설정, 타입 정의
  - 핵심 기능 (3-5일): 인증, Todo CRUD, 상태 관리, UI 컴포넌트
  - 완성 단계 (5-7일): 라우팅, 국제화, 성능 최적화, 테스트, 배포

  🎯 핵심 특징

  1. PRD 요구사항 100% 반영: 모든 필수 기능 포함
  2. shrimp-rules.md 규칙 준수: 아키텍처 가이드라인 완전 적용
  3. 의존성 최적화: 병렬 실행 가능한 작업 분리
  4. 검증 기준 명확: 각 작업별 완료 기준 정의

  📊 작업 우선순위

  보안 > 핵심 기능 > 사용자 경험 > 성능 최적화

  - Firebase 보안 설정 및 인증 (높음)
  - Todo CRUD 및 실시간 동기화 (높음)
  - 반응형 UI 및 접근성 (중간)
  - 성능 최적화 및 테스트 (중간)

  🚀 다음 단계

  이제 각 작업을 순차적으로 실행하여 1주일 내에 완전한 TodoFlow MVP를 완성할 수 있습니다. 각 작업은 독립적으로 실행 가능하며, 명확한 검증 기준이 설정되어 있어 품질 보장이
  가능합니다.
```

**4.1 태스크 리스트 확인 : list\_tasks**

![](https://blog.kakaocdn.net/dna/TmG5K/btsP0tqGPk2/AAAAAAAAAAAAAAAAAAAAAGUgcznoy7F376_cUpDR94OU7GhJi1U-EU-cBwT3xywE/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=veoq9CsIKJTf3fwy5VC6tXNGjvg%3D)
> **list\_tasks** 현재 프로젝트 상황이 궁금해

![](https://blog.kakaocdn.net/dna/zIqiT/btsPZvWQYNN/AAAAAAAAAAAAAAAAAAAAAOCCNuUWgvE4qNthlkAGr0EDfqljCfzXXMt1Yh8M3k1w/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=hr5oP5FyOyutR9rLW7Qe8p0fwlg%3D)
**4.2 무거운 태스크는 분해도 해보자.**

![](https://blog.kakaocdn.net/dna/4n9iv/btsP1lS3wkT/AAAAAAAAAAAAAAAAAAAAAN0ebZ872w-ibElZldIbCpMdyn6HEwdhuRmgLft4eyRX/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=2GErsrCDS9km4fSGu33IzDu03mQ%3D)
> **split\_tasks** 핵심 서비스 개발은 중요 하잖아. 나눌수 있을까?

![](https://blog.kakaocdn.net/dna/bxtlxp/btsPZ5jkMjH/AAAAAAAAAAAAAAAAAAAAAGR3A3r0vf00LiZWo4zm6T71SR_ak7yXKj8xsdsyoKt1/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=1CIZred%2FVlRZ2eSzQ7uplBKhKk0%3D)
![](https://blog.kakaocdn.net/dna/cq1EA9/btsPZZi56qn/AAAAAAAAAAAAAAAAAAAAAKbZxvNUvk5pTXybNPTrw5eDFt2YhTsUqVpvQNLXLABE/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=nrpjiLaMBd%2FWvqOj483yo5RpZjg%3D)
- 다시 현재 태스크를 확인해보자.

**> list\_tasks**

![](https://blog.kakaocdn.net/dna/cE9m2K/btsPX198Ztc/AAAAAAAAAAAAAAAAAAAAADh9qisrvleNtSxoCCD21xgzdrjANNdBCsolLDa_QgJu/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=0BF%2FtisYM7kINwXxO2zeJjWOBxA%3D)
**5. 태스크 실행**

![](https://blog.kakaocdn.net/dna/rZ342/btsPZ5jveh8/AAAAAAAAAAAAAAAAAAAAAEh3A_cih2AAcsM_CD2xJZytwELfTM2Y-3IyWU1gBGGH/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=H1wIViZfrKVZ35jJxVGGtwM0i7M%3D)
 **> execute task**첫번째 작업 해보자

또는

 **> execute task**프로젝트 초기화 및 기본 설정 진행해보자.

![](https://blog.kakaocdn.net/dna/zdm3n/btsPZiwVGAM/AAAAAAAAAAAAAAAAAAAAANoaz3Ps9PoAJaiR4eDuBjj7saoXkmUFAPr0F5MTFrOo/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=uODzQ%2FvvJKkYJRuadOWEKhUbl6w%3D)
- 작업이 끝나면 알아서 검증도 진행하는것을 볼 수 있다.

![](https://blog.kakaocdn.net/dna/dsdKU0/btsP07U7N4v/AAAAAAAAAAAAAAAAAAAAAJreIOfi-yT4oTshgnmp9DhtMzzd7EmkqaldaWvBtqxI/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=fStEEGDx%2F9CqMDnNxXZfp3D2hKE%3D)
![](https://blog.kakaocdn.net/dna/u2o5b/btsP0UBIa4j/AAAAAAAAAAAAAAAAAAAAAGBRCnV4i4_g4i3oNQ0lMbbDmQp0_NYkQibsCaa3cXfi/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=EQVJZlviCWDMDgFrEEXj1CLQ%2BJo%3D)
**6. 연속 실행**

- 연속모드로 순차적으로 쭉 일을 진행할 수도 있다.  

 **> 연속모드**로 모두 실행해줘.

또는

 **>continuous mode**execute all task

![](https://blog.kakaocdn.net/dna/TsHuc/btsPZQzXwNu/AAAAAAAAAAAAAAAAAAAAAP5i1mAQKEU-srDULkPjALDqXrygwiMq7th7qnWn18-W/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=OJUtebdgc6hxFp3hJTVgVTBj2kI%3D)
... 중략

![](https://blog.kakaocdn.net/dna/bsMrjG/btsPYKNZXxR/AAAAAAAAAAAAAAAAAAAAAHK8_3nVrRzEFJeasgfzVtJRXZXRjGgfNEdLuhCW2nJR/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=PtIQuBQ%2BiueI98i%2Bo9dWaaJtfRk%3D)
... 중략 ( 연속모드를 통해 계속 진행 하는 과정을 볼 수 있다. )

![](https://blog.kakaocdn.net/dna/dzDV8b/btsPY6J3aZ1/AAAAAAAAAAAAAAAAAAAAALGwkAMITlK76jhT4BCj5yKwjErqhXclSA0IjmWf7rLV/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=3nJDkBrE%2Fdbosii%2FJc4tTGEMMGI%3D)
- 어느새 한참 후 작업을 마친 상태 이다.

![](https://blog.kakaocdn.net/dna/zqfML/btsP1uvO0ZD/AAAAAAAAAAAAAAAAAAAAAPcy_smQEpiojm3v-_OkSmanmAc_l9jgWPxrZmYSa1tZ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=yKpIkll9NjotJc2G1WiRwI%2Fcr0w%3D)
- 어디까지 진행이 완료되었는지 확인해보자. ( 연속모드라고 100%를 진행하진 않았다. )

> **list\_tasks**현재 프로젝트 진행 상황

![](https://blog.kakaocdn.net/dna/eqGdSg/btsPYDuyDLZ/AAAAAAAAAAAAAAAAAAAAAGlsNPSlc0Hj3UHIujCN_I7TI-gN7goGN763DvgEgp4J/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=%2FRMb%2FdpOgNOWxsg8A5EY5CsZnLA%3D)
- 33% 진행이 완료되어 있었다. 이후 작업도 쭉 진행 하려면 연속모드로 진행 가능하다.

> **연속모드**로 모두 실행해줘.

- 위와 같은 방식으로 업무를 진행해 나갈 수 있는데, 못써본 도구들도 활용해볼만한것들이 있으니, 실무에 응용해보면 좋을 것 같다.

- 도구 정리 ( 참고 : <https://smithery.ai/server/@cjo4m06/mcp-shrimp-task-manager> )

|  |  |  |
| --- | --- | --- |
| **범주 (Category)** | **도구 이름 (Tool Name)** | **설명 (Description)** |
| 작업 계획 (Planning) | plan\_task | 복잡한 요구사항을 구조화된 개발 작업으로 변환하며, 에이전트의 논리적 사고 과정을 돕습니다. |
| 작업 분석 (Analysis) | analyze\_task | 특정 작업에 대한 요구사항을 심층 분석하고, 코드베이스 및 기술적 타당성을 평가합니다. |
|  | process\_thought | 복잡한 문제에 대한 단계별 추론 과정을 진행합니다. |
| 솔루션 평가 (Solution Review) | reflect\_task | 솔루션의 비판적 검토를 통해 개선점을 찾고 품질을 향상시킵니다. |
| 연구 및 조사 (Research) | research\_mode | 특정 기술이나 문제에 대해 체계적인 기술 연구 모드로 전환합니다. |
| 프로젝트 관리 (Project Management) | init\_project\_rules | 프로젝트 표준 및 규칙을 초기화하거나 업데이트하여 일관된 개발 관행을 유지합니다. |
| 작업 관리 (Task Management) | split\_tasks | 복잡한 작업을 더 작고 관리하기 쉬운 단위로 나눕니다. |
|  | add\_task\_dependencies | 작업 간의 종속성(dependencies)을 설정합니다. |
| 작업 실행 (Task Execution) | execute\_task | 특정 작업을 실행하도록 AI 에이전트에게 지시합니다. |
|  | verify\_task | 작업 완료 여부를 확인하고, 요구사항이 충족되었는지 검증합니다. |

#### **태스크 뷰어와 Web GUI 활용하기** 👀

Shrimp Task Manager는 선택적으로 웹 기반 GUI를 제공한다.

ENABLE\_GUI를 true로 설정하면 WebGUI.md 파일이 생성되어 접속 주소를 확인할 수 있다.

현재 내 .claude.json 파일을 살펴보면 다음과 같이 환경설정되어 있다.

```
    "shrimp-task-manager": {
      "command": "node",
      "args": [
        "C:/work/mcp-shrimp-task-manager/dist/index.js"
      ],
      "env": {
        "DATA_DIR": "C:/work/shrimp_data",
        "TEMPLATES_USE": "en",
        "ENABLE_GUI": "false"
      }
    }
```

- 여기에 다음과 같은 예시로 값을 추가해주자.

ex) "ENABLE\_GUI": "true", "WEB\_PORT": "8099"

- 앱이 올라오면 **DATA\_DIR** 경로(ex C:/work/shrimp\_data)에 \*\*WebGUI.md\*\*가 생성될 것 이다.

- 파일을 열어보면 **접속 URL(예: http://localhost:8099)** 이 적혀 있다. 그 주소로 브라우저 접속해보자.

ex) 난 40% 진행도를 보이고 있다.

ex) 태스크 리스트와 상태. 그리고 클릭시 각각의 상세 내역을 확인 가능하다.

**💡 Web GUI의 장점**  

• 여러 프로필 간 탭 전환  

• 실시간 태스크 상태 업데이트  

• 고급 필터링 및 검색  

• 태스크 의존성 시각화  

• 자동 새로고침 설정 가능

#### **프롬프트 커스터마이징 심화** ⚙️

기본 프롬프트도 훌륭하지만, 팀이나 프로젝트 특성에 맞게 커스터마이징할 수 있다고 한다. 이 부분은 간단히 보고 넘어가도록 한다.

###### 커스텀 템플릿 만들기

```
// 1. 기존 템플릿 디렉토리 복사 (en 또는 zh 템플릿 기반)
cp -r src/prompts/templates_en /Users/username/ShrimpData/my_custom_templates

// 2. 설정에서 커스텀 템플릿 지정
"env": {
  "TEMPLATES_USE": "my_custom_templates",
  "DATA_DIR": "/Users/username/ShrimpData"
}

// 3. 템플릿 파일들을 원하는 언어나 스타일로 수정
// - plan_task.txt
// - execute_task.txt  
// - research_mode.txt
// 등등...
```

\* 공식적으로는 영어(en)와 중국어 번체(zh) 템플릿을 지원하며, 사용자가 직접 커스터마이징할 수 있습니다.

#### **트러블슈팅 가이드** 🔧

실제 사용하면서 마주쳤던 문제들과 해결 방법들을 정리했다. 같은 문제로 시간 낭비하지 마시길!

**💀 문제: "Cannot find module" 에러**  

npx로 설치할 때 네트워크 문제로 패키지를 찾지 못하는 경우가 있다.

**✅ 해결 방법**  

1. npm 캐시 클리어: `npm cache clean --force`  

2. 수동 설치: `npm install -g mcp-shrimp-task-manager`  

3. 설정에서 전체 경로 지정: `/Users/username/.npm-global/bin/mcp-shrimp-task-manager`

**💀 문제: 태스크 데이터가 저장되지 않음**  

DATA\_DIR 권한 문제나 경로 설정 오류로 데이터가 저장되지 않는 경우

**✅ 해결 방법**  

1. 디렉토리 권한 확인: `ls -la /Users/username/ShrimpData`  

2. 권한 수정: `chmod 755 /Users/username/ShrimpData`  

3. 소유자 변경: `chown -R $USER /Users/username/ShrimpData`

#### **📝 배운 점 정리**

* **경량화된 설정의 가치**: 외부 API 없이도 내장 AI만으로 강력한 기능을 제공하는 것이 실용적이다
* **맥락 기반 계획의 중요성**: PRD만 보고 계획하는 것보다 실제 코드베이스를 파악한 후 계획하는 것이 더 현실적이다
* **체계적 접근의 힘**: 무작정 코딩하는 것보다 태스크를 체계적으로 분해하고 계획하는 게 결과적으로 훨씬 빠르다
* **AI와의 협업 방식**: AI에게 단순히 "코드 짜줘"가 아니라 구조화된 태스크를 제공하면 훨씬 나은 결과가 나온다
* **메모리의 중요성**: 과거 경험을 학습하고 활용하는 시스템의 위력을 실감했다
* **문서화 자동화**: 코드 작성과 문서화를 분리하지 않고 하나의 워크플로우로 관리하는 것이 효율적이다
* **표준화의 가치**: MCP 같은 표준 프로토콜이 있으면 다양한 도구들과의 연동이 정말 쉬워진다
* **점진적 개선**: 완벽한 설정보다는 일단 사용하면서 점차 개선해나가는 접근이 효과적이다

#### **자주 묻는 질문 ❓**

A: 작업 유형에 따라 특화된 에이전트를 할당할 수 있습니다. 예를 들어 프론트엔드 작업은 UI 전문 에이전트에게, 백엔드 API는 서버 전문 에이전트에게 맡기는 식으로 효율성을 높일 수 있습니다.

Q: 팀 프로젝트에서 여러 명이 함께 사용할 수 있나요?

A: 현재는 개인 단위 사용에 최적화되어 있습니다. 팀 사용을 원한다면 공유 DATA\_DIR을 설정하고 Git으로 태스크 데이터를 관리하는 방식을 추천합니다.

Q: 연속 모드 사용 시 주의할 점은?

A: 처음에는 태스크를 하나씩 검토하면서 진행하세요. AI의 결과물을 충분히 신뢰할 수 있을 때 연속 모드를 사용하는 것이 안전합니다. 중간에 오류가 발생하면 전체 플로우가 중단될 수 있습니다.

A: Shrimp은 외부 API 없이 내장 AI를 활용하므로 설정이 간단하고 비용이 들지 않습니다. 또한 현재 코드베이스를 분석해서 더 현실적인 태스크를 만들어줍니다.

Q: 성능이나 속도 이슈는 없나요?

A: Node.js 기반이라 가볍고 빠릅니다. 대량의 태스크(1000개 이상)에서도 괜찮은 성능을 보입니다. 다만 복잡한 의존성 계산은 시간이 조금 걸릴 수 있습니다.
