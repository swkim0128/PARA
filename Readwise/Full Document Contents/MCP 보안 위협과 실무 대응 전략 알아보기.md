# MCP 보안 위협과 실무 대응 전략 알아보기

![rw-book-cover](https://cdn.infograb.io/insight_prod/img/blog/2025-10-29-mcp-security.png)

## Metadata
- Author: [[https://gitlab.com/grace8540808]]
- Full Title: MCP 보안 위협과 실무 대응 전략 알아보기
- Category: #articles
- Document Tags:  #mcp 
- Summary: MCP 사용이 늘면서 프롬프트 인젝션, 자격증명 탈취, 공급망 변조 등 다양한 보안 위협이 증가하고 있습니다. 위협을 줄이려면 최소 권한 원칙, 검증된 서버 사용, 중앙 집중식 시크릿 관리, 실행 환경 격리, 상호작용 모니터링 같은 대응책이 필요합니다. 섀도 MCP와 툴 포이즈닝 등 보이지 않는 위험도 함께 점검해야 합니다.
- URL: https://insight.infograb.net/blog/2025/10/29/mcp-security/

## Full Document
최근 MCP 활용도와 확장성이 높아지면서 관련 보안 위협도 함께 증가하고 있습니다. 프롬프트 인젝션, 자격증명 탈취, 공급망 변조 등 다양한 위험이 MCP 환경의 신뢰성과 무결성을 위협하고 있죠. MCP 서버는 민감한 시스템에 직접 접근하기에 취약점 하나가 전체 인프라에 미치는 파장은 클 수 있습니다.

이 글에서는 오늘날 MCP 환경에서 발생하는 6가지 주요 보안 위협과 5가지 대응 방안을 정리했는데요. 보안 위협으로 프롬프트 인젝션과 자격증명 탈취·노출, 공급망 변조, 툴 포이즈닝, 권한 남용, 섀도 MCP를 알아보고요. 대응 방안으로 최소 권한 원칙부터 검증된 MCP 서버 사용, 중앙 집중식 시크릿 관리, 실행 환경 격리, MCP 상호작용 모니터링까지 자세히 살펴보겠습니다.

#### MCP 보안 위협 유형[​](https://insight.infograb.net/blog/2025/10/29/mcp-security/#mcp-보안-위협-유형)

MCP 환경에 존재하는 보안 위협의 특성과 발생 메커니즘, 잠재적 피해 범위를 알아보겠습니다.

#mermaid-svg-4933958{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:16px;fill:#333;}#mermaid-svg-4933958 .error-icon{fill:#552222;}#mermaid-svg-4933958 .error-text{fill:#552222;stroke:#552222;}#mermaid-svg-4933958 .edge-thickness-normal{stroke-width:2px;}#mermaid-svg-4933958 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-svg-4933958 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-svg-4933958 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-svg-4933958 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-svg-4933958 .marker{fill:#333333;stroke:#333333;}#mermaid-svg-4933958 .marker.cross{stroke:#333333;}#mermaid-svg-4933958 svg{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:16px;}#mermaid-svg-4933958 .label{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;color:#333;}#mermaid-svg-4933958 .cluster-label text{fill:#333;}#mermaid-svg-4933958 .cluster-label span,#mermaid-svg-4933958 p{color:#333;}#mermaid-svg-4933958 .label text,#mermaid-svg-4933958 span,#mermaid-svg-4933958 p{fill:#333;color:#333;}#mermaid-svg-4933958 .node rect,#mermaid-svg-4933958 .node circle,#mermaid-svg-4933958 .node ellipse,#mermaid-svg-4933958 .node polygon,#mermaid-svg-4933958 .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#mermaid-svg-4933958 .flowchart-label text{text-anchor:middle;}#mermaid-svg-4933958 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-svg-4933958 .node .label{text-align:center;}#mermaid-svg-4933958 .node.clickable{cursor:pointer;}#mermaid-svg-4933958 .arrowheadPath{fill:#333333;}#mermaid-svg-4933958 .edgePath .path{stroke:#333333;stroke-width:2.0px;}#mermaid-svg-4933958 .flowchart-link{stroke:#333333;fill:none;}#mermaid-svg-4933958 .edgeLabel{background-color:#e8e8e8;text-align:center;}#mermaid-svg-4933958 .edgeLabel rect{opacity:0.5;background-color:#e8e8e8;fill:#e8e8e8;}#mermaid-svg-4933958 .labelBkg{background-color:rgba(232, 232, 232, 0.5);}#mermaid-svg-4933958 .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#mermaid-svg-4933958 .cluster text{fill:#333;}#mermaid-svg-4933958 .cluster span,#mermaid-svg-4933958 p{color:#333;}#mermaid-svg-4933958 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:12px;background:hsl(80, 100%, 96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-svg-4933958 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#333;}#mermaid-svg-4933958 :root{--mermaid-font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;}입력 기반접근 기반공급망MCP 환경 운영보안 위협  
유형은?프롬프트 인젝션  
툴 포이즈닝자격증명 탈취  
권한 남용공급망 변조  
섀도 MCPAI 동작 조작  
은밀한 공격무단 접근  
데이터 유출신뢰 악용  
감사 회피전체 인프라  
보안 위협대응 필요##### 1. 프롬프트 인젝션(Prompt Injection)[​](https://insight.infograb.net/blog/2025/10/29/mcp-security/#1-프롬프트-인젝션prompt-injection)

프롬프트 인젝션은 사용자가 직접 제공하거나, 손상된 외부 데이터 소스를 통해 간접적으로 제공하는 악의적인 입력으로 발생합니다. 이러한 입력은 AI 동작을 조작하도록 설계됐는데요. 무단 거래, 민감한 데이터 유출, 내부 시스템 손상과 같은 의도하지 않은 작업을 수행하도록 AI를 유도하죠. 악의적인 프롬프트는 MCP 시스템의 상호 연결된 특성 때문에 빠르게 전파되고요. 이는 기업의 여러 운영 영역에 영향을 미칠 수 있습니다.

##### 2. 자격증명 탈취·노출[​](https://insight.infograb.net/blog/2025/10/29/mcp-security/#2-자격증명-탈취노출)

공격자가 자격증명을 탈취하면, 해당 자격증명에 허용된 권한 범위 내에서 외부 서비스에 합법적인 사용자처럼 접근할 수 있습니다. MCP 서버는 외부 서비스 인증과 연결을 위해 OAuth 토큰, API 키 등 자격증명을 사용하는데요. 탈취된 토큰이 메일 읽기·삭제 권한을 포함하면, 공격자가 사용자 대신 이메일을 읽고 삭제할 수 있고요. 클라우드에 저장된 파일에 접근하거나, 다른 API를 호출할 수도 있죠. 특히 MCP 서버가 여러 자격증명을 보유하면, 서버 하나가 손상될 때 권한 범위와 토큰 수명에 따라 피해 범위는 광범위해질 수 있습니다.

공급망 변조는 사용자가 신뢰하고 광범위하게 배포·채택한 도구가 이후 은밀히 변조돼 악의적인 동작을 수행하는 공격입니다. 공격자는 배포 파이프라인, 라이브러리 레지스트리, MCP 서버의 코드·업데이트 경로를 손상시키는데요. 이로써 도구가 악의적인 출력을 반환하거나, 비정상적인 행위를 하도록 유도할 수 있죠. 그 결과, 민감한 데이터 유출, 중요한 비즈니스 운영 방해, 금전적 손실 등 피해를 초래할 수 있습니다.

##### 4. 툴 포이즈닝(Tool Poisoning)[​](https://insight.infograb.net/blog/2025/10/29/mcp-security/#4-툴-포이즈닝tool-poisoning)

툴 포이즈닝은 프롬프트 인젝션을 활용해 사용자가 모르는 상태로 클라이언트 동작에 영향을 끼칩니다. 공격자는 AI 에이전트가 설명, 매개변수, 운영 지침 등 MCP 툴 메타데이터에 갖는 ‘내재한 신뢰’를 악용하는데요. 공격자는 이 메타데이터 내에 악의적인 명령, 미세한 조작을 내장해 사용자가 일상적인 점검으로는 이를 탐지하기 어렵죠. 그 결과, 큰 피해가 발생하기 전까지 의도하지 않은 작업과 시스템 취약점의 존재를 인지하지 못할 수 있습니다.

##### 5. 권한 남용[​](https://insight.infograb.net/blog/2025/10/29/mcp-security/#5-권한-남용)

권한 남용은 MCP 도구에 필요 이상으로 많은 접근, 권한을 부여할 때 발생할 수 있습니다. 과도한 권한이 주어지면, MCP 도구가 민감한 데이터와 중요한 시스템 운영에 광범위하게 접근할 수 있는데요. 그 결과, 악의적인 행위자가 이를 악용하거나, 사용자가 실수로 오용해 보안 위협으로 이어질 수 있죠. 예를 들어, HR 업무를 지원하는 AI 에이전트는 직원 기록, 재무 데이터, 전략 정보가 담긴 전체 데이터베이스에 접근할 수도 있는데요. 이 에이전트가 공격 대상이 되면, 정보 유출 사고가 발생할 수 있습니다.

##### 6. 섀도 MCP(Shadow MCP)[​](https://insight.infograb.net/blog/2025/10/29/mcp-security/#6-섀도-mcpshadow-mcp)

섀도 MCP는 조직 내에서 승인되지 않았거나, 모니터링되지 않는 MCP 인스턴스입니다. 공식 인프라 외부에서 동작하지만, 여전히 내부 시스템이나 데이터에 접근하는 비인가 MCP 서버나 클라이언트가 이에 해당하죠. 섀도 MCP는 기존 감사 시스템이나 접근 제어 정책으로 탐지되지 않은 채 작업 실행, 정보 추출 등을 수행할 수 있습니다. 일부 섀도 MCP는 운영 효율을 높이려는 목적으로 도입됐지만, 버전 노후화나 설정 오류로 보안 수준의 불일치, 검증되지 않은 도구 사용 등 문제를 일으킬 수 있습니다.

이러한 보안 위협에 대응하는 방안을 중요도와 우선순위에 따라 살펴보겠습니다.

#mermaid-svg-1647726{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:16px;fill:#333;}#mermaid-svg-1647726 .error-icon{fill:#552222;}#mermaid-svg-1647726 .error-text{fill:#552222;stroke:#552222;}#mermaid-svg-1647726 .edge-thickness-normal{stroke-width:2px;}#mermaid-svg-1647726 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-svg-1647726 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-svg-1647726 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-svg-1647726 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-svg-1647726 .marker{fill:#333333;stroke:#333333;}#mermaid-svg-1647726 .marker.cross{stroke:#333333;}#mermaid-svg-1647726 svg{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:16px;}#mermaid-svg-1647726 .label{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;color:#333;}#mermaid-svg-1647726 .cluster-label text{fill:#333;}#mermaid-svg-1647726 .cluster-label span,#mermaid-svg-1647726 p{color:#333;}#mermaid-svg-1647726 .label text,#mermaid-svg-1647726 span,#mermaid-svg-1647726 p{fill:#333;color:#333;}#mermaid-svg-1647726 .node rect,#mermaid-svg-1647726 .node circle,#mermaid-svg-1647726 .node ellipse,#mermaid-svg-1647726 .node polygon,#mermaid-svg-1647726 .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#mermaid-svg-1647726 .flowchart-label text{text-anchor:middle;}#mermaid-svg-1647726 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-svg-1647726 .node .label{text-align:center;}#mermaid-svg-1647726 .node.clickable{cursor:pointer;}#mermaid-svg-1647726 .arrowheadPath{fill:#333333;}#mermaid-svg-1647726 .edgePath .path{stroke:#333333;stroke-width:2.0px;}#mermaid-svg-1647726 .flowchart-link{stroke:#333333;fill:none;}#mermaid-svg-1647726 .edgeLabel{background-color:#e8e8e8;text-align:center;}#mermaid-svg-1647726 .edgeLabel rect{opacity:0.5;background-color:#e8e8e8;fill:#e8e8e8;}#mermaid-svg-1647726 .labelBkg{background-color:rgba(232, 232, 232, 0.5);}#mermaid-svg-1647726 .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#mermaid-svg-1647726 .cluster text{fill:#333;}#mermaid-svg-1647726 .cluster span,#mermaid-svg-1647726 p{color:#333;}#mermaid-svg-1647726 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:12px;background:hsl(80, 100%, 96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-svg-1647726 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#333;}#mermaid-svg-1647726 :root{--mermaid-font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;}1순위2순위3순위4순위5순위충분부족MCP 보안  
강화 시작대응  
우선순위는?최소 권한  
원칙 준수검증된  
서버 사용시크릿  
관리실행 환경  
격리상호작용  
모니터링RBAC 정책  
권한 검토서명 검증  
무결성 검사중앙 집중식  
암호화 보관컨테이너/VM  
격리입출력  
로그 분석보안  
수준안전한  
MCP 환경추가 조치  
필요##### 1. 최소 권한 원칙 준수[​](https://insight.infograb.net/blog/2025/10/29/mcp-security/#1-최소-권한-원칙-준수)

모든 MCP 구성 요소에는 최소 권한 원칙을 적용합니다. 각 MCP 서버와 클라이언트가 보유한 권한은 해당 도구의 목적을 수행하는 데 필요한 최소한의 수준으로 제한하는 게 바람직하죠. 특히 도구 명령 실행, 데이터 소스 접근에 불필요하게 광범위한 접근을 부여하지 말아야 합니다. 구체적으로는 RBAC 정책을 도입해 MCP 서버별로 명확한 권한 프로필을 정의하는 게 좋고요. 조직의 위험도와 규모에 따라 분기별 또는 월별로, 구성을 변경할 때 권한 검토를 진행해 과도한 권한을 확인하고 제거하는 걸 권장합니다.

##### 2. 검증된 MCP 서버 사용[​](https://insight.infograb.net/blog/2025/10/29/mcp-security/#2-검증된-mcp-서버-사용)

출처를 신뢰할 수 있는, 검증된 MCP 서버만 사용합니다. 공신력 있는 기업이 제공하는 서버나 조직의 보안 정책에 따라 승인된 서버가 이에 해당하죠. 이는 LLM 프로덕션 환경에서 악의적이거나 검증되지 않은 구성 요소가 유입되는 위험을 줄일 수 있습니다. 구체적으로 다음 조치를 적용하는 걸 권장합니다. 첫째, 디지털 서명된 패키지만 설치하도록 허용하고요. 둘째, 배포 전 무결성 검사를 진행합니다. 셋째, 허용 목록에 등록된 서버만 사용하고요. 넷째, 승인된 서버 목록을 주기적으로 업데이트합니다.

시크릿을 중앙 집중식으로 관리하고, 암호화된 시크릿 관리 도구에 보관합니다. 이는 평문 시크릿 노출을 방지할 수 있는데요. 다음 조치도 병행하면 좋습니다. 첫째, 코드 리포지터리의 시크릿 스캔을 자동화하고요. 둘째, Pre-commit hook으로 하드코딩된 자격증명을 차단합니다. 셋째, 시크릿 로테이션 정책을 적용하고요. 넷째, 시크릿 접근 로그를 통합 모니터링합니다. 다섯째, 접근 범위와 만료 기간을 자동으로 제한하도록 설정하고요.

##### 4. 실행 환경 격리[​](https://insight.infograb.net/blog/2025/10/29/mcp-security/#4-실행-환경-격리)

MCP 도구를 컨테이너, 샌드박스, VM 등 격리된 실행 환경에서 운영합니다. 이는 악성 코드나 손상된 도구가 호스트 시스템에 직접 영향을 미치는 걸 방지하죠. 또 보안 사고가 발생해도 침해 영향을 격리 환경 내부로 제한할 수 있습니다. 단, Linux 컨테이너는 호스트 커널을 공유하기에 완전한 격리를 제공하지 않으며, 커널 취약점이 발생하면 탈출 위험이 있는데요. 따라서 민감한 데이터나 위험도가 높은 코드를 처리할 때는 VM 기반 샌드박스나 하드웨어 가상화를 권장하고요. 격리 수준은 위험도와 서비스 중요도에 따라 결정합니다.

##### 5. MCP 상호작용 모니터링[​](https://insight.infograb.net/blog/2025/10/29/mcp-security/#5-mcp-상호작용-모니터링)

LLM의 입출력과 MCP 서버의 상호작용 방식을 모니터링합니다. LLM의 입출력을 모니터링하면 공격자가 프롬프트 컨텍스트를 조작하거나 민감한 데이터를 추출하려는 시도를 포착하는 데 도움이 되죠. MCP 서버를 모니터링할 때는 다음 세 가지를 추적하면 보안 인사이트를 얻을 수 있는데요. 이는 Datadog에서 제시하는 내용입니다. 첫째, 손상된 서버 도구의 무단 API 호출과 같은 예기치 않은 서버 동작을 확인하는 이벤트 로그, 둘째, 서드파티 서버에 임베디드된 악의적인 패키지와 코드, 셋째, MCP 구성 파일에 하드코딩된 시크릿과 자격증명입니다.
