---
type: Mermaid
archive: false
---
Flowcharts - Basic Syntax

A node (default)

A node with text

Graph

Flowchart Orientation

Node shapes

A node with round edges

A stadium-shaped node

A node in a subroutine shape

A node in a cylindrical shape

A node in the form of a circle

A node in an asymmetric shape

A node (rhombus)

A hexagon node

Parallelogram

Parallelogram alt

Trapezoid

Trapezoid alt

Double circle

Links between nodes

A link with arrow head

An open link

Text on links

A link with arrow head and text

Dotted link

Dotted link with text

Thick link

Thick link with text

An invisible link

Chaining of links

New arrow types

Multi directional arrows

Minimum length of a link

Special characters that break syntax

Entity codes to escape characters

Subgraphs

flowcharts

Direction in subgraphs

Interaction

Comments

Styling and classes

Styling links

Styling line curves

Styling a node

Css classes

Default class

Basic support for fontawesome

Graph declarations with spaces between vertices and link and without semicolon

Configuration

Renderer

Width

# **Flowcharts - Basic Syntax**

모든 플로우차트는 기하학적 모양인 노드와 화살표 또는 선인 엣지로 구성됩니다. Mermaid 코드는 이러한 노드와 엣지가 만들어지고 상호 작용하는 방식을 정의합니다.

또한 다양한 화살표 유형, 다중 방향 화살표 및 서브그래프에서의 링크 연결도 가능합니다.

> 중요 사항: Flowchart 노드로 "end"라는 단어를 입력하지 마십시오. 플로우차트가 망가지지 않도록 모든 문자를 대문자로 입력하십시오. 예를 들어 "End" 또는 "END"입니다. 또는 이 해결 방법을 적용할 수 있습니다.

## **A node (default)**

**Code:**

```Mermaid
---
title: Node
---
flowchart LR
    id
```

## **A node with text**

상자 안에 표시되는 텍스트와 id가 다를 수도 있습니다. 이 경우, 여러 번 설정하면 마지막 선언된 텍스트가 사용됩니다. 또한, 나중에 노드의 엣지를 정의할 때 텍스트를 정의하지 않아도 됩니다. 렌더링할 때 이전에 정의된 텍스트가 사용됩니다.

**Code:**

```Mermaid
---
title: Node with text
---
flowchart LR
    id1[This is the text in the box]
```

## **Graph**

이 문장은 Flowchart의 방향을 선언합니다.

이는 flowchart가 위에서 아래로 (`TD` 또는 `TB`) 방향으로 정렬되어 있다는 것을 선언합니다.

**Code:**

```Mermaid
flowchart TD
    Start --> Stop
```

이것은 플로우차트가 왼쪽에서 오른쪽(`LR`)으로 정렬되어 있다는 것을 선언합니다.

**Code:**

```Mermaid
flowchart LR
    Start --> Stop
```

## **Flowchart Orientation**

Possible FlowChart orientations are:

- TB - top to bottom
- TD - top-down/ same as top to bottom
- BT - bottom to top
- RL - right to left
- LR - left to right

## **Node shapes**

### **A node with round edges**

**Code:**

```Mermaid
flowchart LR
    id1(This is the text in the box)
```

### **A stadium-shaped node**

**Code:**

```Mermaid
flowchart LR
    id1([This is the text in the box])
```

### **A node in a subroutine shape**

**Code:**

```Mermaid
flowchart LR
    id1[[This is the text in the box]]
```

### **A node in a cylindrical shape**

**Code:**

```Mermaid
flowchart LR
    id1[(Database)]
```

### **A node in the form of a circle**

**Code:**

```Mermaid
flowchart LR
    id1((This is the text in the circle))
```

### **A node in an asymmetric shape**

**Code:**

```Mermaid
flowchart LR
    id1>This is the text in the box]
```

Currently only the shape above is possible and not its mirror. _This might change with future releases._

### **A node (rhombus)**

**Code:**

```Mermaid
flowchart LR
id1{This is the text in the box}
```

### **A hexagon node**

**Code:**

```Mermaid
flowchart LR
    id1{{This is the text in the box}}
```

Render:

**Code:**

```Mermaid
flowchart LR
    id1{{This is the text in the box}}
```

### **Parallelogram**

**Code:**

```Mermaid
flowchart TD
    id1[/This is the text in the box/]
```

### **Parallelogram alt**

**Code:**

```Mermaid
flowchart TD
    id1[\This is the text in the box\]
```

### **Trapezoid**

**Code:**

```Mermaid
flowchart TD
    A[/Christmas\]
```

### **Trapezoid alt**

**Code:**

```Mermaid
flowchart TD
    B[\Go shopping/]
```

### **Double circle**

**Code:**

```Mermaid
flowchart TD
    id1(((This is the text in the circle)))
```

## **Links between nodes**

노드는 링크/엣지로 연결될 수 있습니다. 다른 유형의 링크를 가질 수 있거나 링크에 텍스트 문자열을 첨부할 수도 있습니다.

### **A link with arrow head**

**Code:**

```Mermaid
flowchart LR
    A-->B
```

### **An open link**

**Code:**

```Mermaid
flowchart LR
    A --- B
```

### **Text on links**

**Code:**

```Mermaid
flowchart LR
    A-- This is the text! ---B
```

or

**Code:**

```Mermaid
flowchart LR
    A---|This is the text|B
```

### **A link with arrow head and text**

**Code:**

```Mermaid
flowchart LR
    A-->|text|B
```

or

**Code:**

```Mermaid
flowchart LR
    A-- text -->B
```

### **Dotted link**

**Code:**

```Mermaid
flowchart LR
   A-.->B;
```

### **Dotted link with text**

**Code:**

```Mermaid
flowchart LR
   A-. text .-> B
```

### **Thick link**

**Code:**

```Mermaid
flowchart LR
   A ==> B
```

### **Thick link with text**

**Code:**

```Mermaid
flowchart LR
   A == text ==> B
```

### **An invisible link**

이는 노드의 기본 위치를 변경하려는 경우에 유용한 도구일 수 있습니다.

**Code:**

```Mermaid
flowchart LR
    A ~~~ B
```

### **Chaining of links**

아래와 같이 한 줄에 여러 링크를 선언할 수 있습니다:

**Code:**

```Mermaid
flowchart LR
   A -- text --> B -- text2 --> C
```

아래와 같이 같은 줄에 여러 노드 링크를 선언하는 것도 가능합니다:

**Code:**

```Mermaid
flowchart LR
   a --> b & c--> d
```

그런 다음 아래의 한 줄처럼 매우 표현력있게 종속성을 설명할 수 있습니다:

**Code:**

```Mermaid
flowchart TB
    A & B--> C & D
```

만약 기본 구문을 사용하여 동일한 다이어그램을 설명하면 4 줄이 소요됩니다. 주의할 점은 마크다운 형식에서 흐름도를 더 어렵게 만들 수 있습니다. 스웨덴어 단어 'lagom'이 떠오릅니다. 이는 너무 많지도 않고 너무 적지도 않음을 의미합니다. 이것은 표현적인 구문에도 적용됩니다.

**Code:**

```Mermaid
flowchart TB
    A --> C
    A --> D
    B --> C
    B --> D
```

### **New arrow types**

아래와 같이 새로운 종류의 화살표가 지원됩니다:

**Code:**

```Mermaid
flowchart LR
    A --o B
    B --x C
```

### **Multi directional arrows**

다방향 화살표를 사용할 수 있습니다.

**Code:**

```Mermaid
flowchart LR
    A o--o B
    B <--> C
    C x--x D
```

### **Minimum length of a link**

흐름도의 각 노드는 연결된 노드에 기반하여 렌더링된 그래프에서 최종적으로 수직 또는 수평 레벨에 할당됩니다(흐름도 방향에 따라 다릅니다). 기본적으로 링크는 어떤 수의 랭크를 거쳐도 상관없지만, 링크 정의에 추가 대시를 추가하여 다른 링크보다 길게 요청할 수 있습니다.

다음 예제에서 노드 _B_에서 노드 _E_로의 링크에 추가로 두 개의 대시가 추가되어 일반적인 링크보다 두 개의 랭크를 더 갖게 됩니다:

**Code:**

```Mermaid
flowchart TD
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]
```

> 참고: 렌더링 엔진은 다른 요청을 수용하기 위해 요청한 순위 수보다 링크를 더 길게 만들 수 있습니다.

링크 라벨이 링크 중간에 작성될 때, 추가 대시는 링크 오른쪽에 추가되어야 합니다. 다음 예시는 이전 예시와 동일합니다:

**Code:**

```Mermaid
flowchart TD
    A[Start] --> B{Is it?}
    B -- Yes --> C[OK]
    C --> D[Rethink]
    D --> B
    B -- No ----> E[End]
```

점선이나 두꺼운 링크를 위해서는, 추가해야 할 문자는 등호 또는 점으로 요약된 표에 나와 있습니다:

|   |   |   |   |
|---|---|---|---|
|**Length**|**1**|**2**|**3**|
|Normal|`---`|`----`|`-----`|
|Normal with arrow|`-->`|`--->`|`---->`|
|Thick|`===`|`====`|`=====`|
|Thick with arrow|`==>`|`===>`|`====>`|
|Dotted|`-.-`|`-..-`|`-...-`|
|Dotted with arrow|`-.->`|`-..->`|`-...->`|

## **Special characters that break syntax**

문제가 되는 문자를 렌더링하기 위해 따옴표 안에 텍스트를 넣을 수 있습니다. 아래 예시와 같이:

**Code:**

```Mermaid
flowchart LR
    id1["This is the (text) in the box"]
```

### **Entity codes to escape characters**

여기에서 설명된 구문을 사용하여 문자를 이스케이프할 수 있습니다.

**Code:**

```Mermaid
flowchart LR
        A["A double quote:\#quot;"] -->B["A dec char:\#9829;"]
```

주어진 숫자는 10진법이므로 `#`는 `\#35;`으로 인코딩될 수 있습니다. 또한 HTML 문자 이름을 사용하는 것도 지원됩니다.

## **Subgraphs**

```Plain
subgraph title
    graph definition
end
```

An example below:

**Code:**

```Mermaid
flowchart TB
    c1-->a2
    subgraph one
    a1-->a2
    end
    subgraph two
    b1-->b2
    end
    subgraph three
    c1-->c2
    end
```

서브그래프에 명시적인 id를 설정할 수도 있습니다.

**Code:**

```Mermaid
flowchart TB
    c1-->a2
    subgraph ide1 [one]
    a1-->a2
    end
```

## **flowcharts**

그래프 유형 flowchart를 사용하면 아래 flowchart에서와 같이 하위 그래프로부터 에지를 설정할 수도 있습니다.

**Code:**

```Mermaid
flowchart TB
    c1-->a2
    subgraph one
    a1-->a2
    end
    subgraph two
    b1-->b2
    end
    subgraph three
    c1-->c2
    end
    one --> two
    three --> two
    two --> c2
```

## **Direction in subgraphs**

그래프 유형이 flowcharts인 경우에는 direction 문을 사용하여 서브그래프가 렌더링될 방향을 설정할 수 있습니다. 다음 예시와 같습니다.

**Code:**

```Mermaid
flowchart LR
  subgraph TOP
    direction TB
    subgraph B1
        direction RL
        i1 -->f1
    end
    subgraph B2
        direction BT
        i2 -->f2
    end
  end
  A --> TOP --> B
  B1 --> B2
```

## **Interaction**

노드에 클릭 이벤트를 바인딩하여 자바스크립트 콜백 또는 새로운 브라우저 탭에서 열리는 링크로 이어질 수 있습니다. **참고**: `securityLevel='strict'`를 사용할 때는 이 기능이 비활성화되고, `securityLevel='loose'`를 사용할 때는 활성화됩니다.

```Plain
click nodeId callback
click nodeId call callback()
```

- nodeId는 노드의 id입니다.
- callback은 그래프를 표시하는 페이지에서 정의된 JavaScript 함수의 이름입니다. 해당 함수는 nodeId를 매개 변수로 호출됩니다.

Examples of tooltip usage below:

```HTML
<script>
  const callback = function () {
    alert('A callback was triggered');
  };
</script>
```

툴팁 텍스트는 겹따옴표로 둘러싸여 있습니다. 툴팁의 스타일은 `.mermaidTooltip` 클래스로 설정됩니다.

**Code:**

```Mermaid
flowchart LR
    A-->B
    B-->C
    C-->D
    click A callback "Tooltip for a callback"
    click B "https://www.github.com" "This is a tooltip for a link"
    click A call callback() "Tooltip for a callback"
    click B href "https://www.github.com" "This is a tooltip for a link"
```

> 성공 - 버전 0.5.2부터 툴팁 기능과 URL 링크 기능을 사용할 수 있습니다.

?> Docsify가 JavaScript 콜백 함수를 처리하는 방식의 제한으로 인해, 위 코드의 대체 작동 데모는 **[이 jsfiddle](https://jsfiddle.net/s37cjoau/3/)**에서 볼 수 있습니다.

링크는 기본적으로 동일한 브라우저 탭 / 창에서 열립니다. 클릭 정의에 링크 대상을 추가하여 이를 변경할 수 있습니다 (_self, _blank, _parent 및 _top이 지원됨) :

**Code:**

```Mermaid
flowchart LR
    A-->B
    B-->C
    C-->D
    D-->E
    click A "https://www.github.com" _blank
    click B "https://www.github.com" "Open this in a new tab" _blank
    click C href "https://www.github.com" _blank
    click D href "https://www.github.com" "Open this in a new tab" _blank
```

HTML 컨텍스트에서 대화형 링크를 사용하는 전체 예시 - 초보자 팁:

```HTML
<body>
  <pre class="mermaid">
    flowchart LR
        A-->B
        B-->C
        C-->D
        click A callback "Tooltip"
        click B "https://www.github.com" "This is a link"
        click C call callback() "Tooltip"
        click D href "https://www.github.com" "This is a link"
  </pre>

  <script>
    const callback = function () {
      alert('A callback was triggered');
    };
    const config = {
      startOnLoad: true,
      flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'cardinal' },
      securityLevel: 'loose',
    };
    mermaid.initialize(config);
  </script>
</body>
```

### **Comments**

흐름도 내에서 주석을 입력할 수 있습니다. 이 주석은 구문 분석기에서 무시됩니다. 주석은 자체 줄에 있어야하며 `%%` (이중 퍼센트 기호)로 시작해야합니다. 주석 시작부터 다음 개행까지의 모든 텍스트는 주석으로 처리되며, 흐름 구문을 포함하여 모든 텍스트가 주석으로 처리됩니다.

**Code:**

```Mermaid
flowchart LR
%% this is a comment A -- text --> B{node}
   A -- text --> B -- text2 --> C
```

## **Styling and classes**

### **Styling links**

링크를 스타일링 할 수 있습니다. 예를 들어, 흐름을 거꾸로 가는 링크를 스타일링하고 싶을 수 있습니다. 링크는 노드와 마찬가지로 id가 없으므로, 링크에 적용될 스타일을 결정하기 위한 다른 방법이 필요합니다. id 대신 그래프에서 링크가 정의된 순서 번호를 사용하거나, 모든 링크에 적용하려면 기본값을 사용합니다. 아래 예제에서는 linkStyle 문에서 정의된 스타일이 그래프에서 네 번째 링크에 속합니다:

```Plain
linkStyle 3 stroke:\#ff3,stroke-width:4px,color:red;
```

### **Styling line curves**

기본 방법이 요구 사항을 충족하지 못하는 경우 항목 간 라인에 사용되는 곡선 유형을 스타일링하는 것이 가능합니다. 사용 가능한 곡선 스타일은 `basis`, `bumpX`, `bumpY`, `cardinal`, `catmullRom`, `linear`, `monotoneX`, `monotoneY`, `natural`, `step`, `stepAfter` 및 `stepBefore`가 있습니다.

이 예시에서 왼쪽에서 오른쪽으로 그려지는 그래프는 `stepBefore` 곡선 스타일을 사용합니다:

```Plain
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
graph LR
```

사용 가능한 모든 곡선의 전체 목록 및 사용자 지정 곡선에 대한 설명을 포함한 자세한 내용은 [**d3-shape**](https://github.com/d3/d3-shape/) 프로젝트의 [**Shapes**](https://github.com/d3/d3-shape/blob/main/README.md#curves) 문서를 참조하십시오.

### **Styling a node**

노드에 더 두꺼운 테두리나 다른 배경색과 같은 구체적인 스타일을 적용하는 것이 가능합니다.

**Code:**

```Mermaid
flowchart LR
    id1(Start)-->id2(Stop)
    style id1 fill:\#f9f,stroke:\#333,stroke-width:4px
    style id2 fill:\#bbf,stroke:\#f66,stroke-width:2px,color:\#fff,stroke-dasharray: 5 5
```

**Classes**

매번 스타일을 정의하는 것보다는 스타일 클래스를 정의하고 다른 모습이 필요한 노드에 이 클래스를 적용하는 것이 더 편리합니다.

아래 예시와 같이 클래스 정의는 다음과 같습니다:

```Plain
    classDef className fill:\#f9f,stroke:\#333,stroke-width:4px;
```

노드에 클래스를 첨부하는 방법은 다음과 같습니다:

```Plain
    class nodeId1 className;
```

노드 목록에 클래스를 한 번에 추가하는 것도 가능합니다:

```Plain
    class nodeId1,nodeId2 className;
```

클래스를 추가하는 더 짧은 방법은 아래와 같이 `:::` 연산자를 사용하여 노드에 클래스 이름을 붙이는 것입니다:

**Code:**

```Mermaid
flowchart LR
    A:::someclass --> B
    classDef someclass fill:\#f96
```

### **Css classes**

css 스타일에서 미리 정의된 클래스를 그래프 정의에서 아래 예시와 같이 적용할 수도 있습니다:

**Example style**

```HTML
<style>
  .cssClass > rect {
    fill: \#ff0000;
    stroke: \#ffff00;
    stroke-width: 4px;
  }
</style>
```

**Example definition**

**Code:**

```Mermaid
flowchart LR
    A-->B[AAA<span>BBB</span>]
    B-->D
    class A cssClass
```

### **Default class**

만약 클래스의 이름이 "default"이면, 특정 클래스 정의 없이 모든 클래스에 할당됩니다.

```Plain
    classDef default fill:\#f9f,stroke:\#333,stroke-width:4px;
```

## **Basic support for fontawesome**

폰트어썸에서 아이콘을 추가할 수 있습니다.

아이콘은 fa:#아이콘 클래스명# 구문을 통해 액세스됩니다.

**Code:**

```Mermaid
flowchart TD
    B["fab:fa-twitter for peace"]
    B-->C[fa:fa-ban forbidden]
    B-->D(fa:fa-spinner)
    B-->E(A fa:fa-camera-retro perhaps?)
```

Mermaid는 Font Awesome 버전 4와 5와만 호환됩니다. 올바른 버전의 Font Awesome를 사용 중인지 확인하세요.

## **Graph declarations with spaces between vertices and link and without semicolon**

- 그래프 선언에서 문장이 세미콜론 없이 끝날 수도 있습니다. 0.2.16 버전 이후에는 그래프 문장을 세미콜론으로 끝내는 것이 선택사항입니다. 따라서 아래 그래프 선언은 예전의 그래프 선언과 함께 유효하며, 이전 구문도 계속 사용 가능합니다.
- 노드와 연결 사이에는 공백을 하나만 허용합니다. 그러나 노드와 텍스트, 연결과 텍스트 사이에는 공백이 없어야 합니다. 이전의 그래프 선언 구문도 계속 작동하므로, 이 새로운 기능은 선택사항이며 가독성을 향상시키기 위해 도입되었습니다.

아래는 그래프 엣지의 새로운 선언 방식으로, 이전 그래프 엣지의 선언 방식과 함께 유효합니다.

**Code:**

```Mermaid
flowchart LR
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

## **Configuration**

### **Renderer**

다이어그램 레이아웃은 렌더러로 처리됩니다. 기본 렌더러는 dagre입니다.

Mermaid 버전 9.4부터는 elk라는 대체 렌더러를 사용할 수 있습니다. elk 렌더러는 더 크고/또는 복잡한 다이어그램에 적합합니다.

_elk_ 렌더러는 실험적인 기능입니다. elk 렌더러로 변경하려면 다음 지시문을 추가하면 됩니다:

```Plain
%%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%
```

이 사이트에서는 이 기능을 사용하려면 mermaid 버전 9.4+를 사용하고 lazy-loading 구성에서 이 기능을 활성화해야합니다.

### **Width**

렌더링된 플로우 차트의 너비를 조정하는 것이 가능합니다.

이는 **mermaid.flowchartConfig**를 정의하거나, CLI를 사용하여 JSON 파일로 구성을 설정함으로써 수행할 수 있습니다. CLI의 사용 방법은 mermaidCLI 페이지에서 설명되어 있습니다. mermaid.flowchartConfig는 구성 매개 변수를 포함하는 JSON 문자열 또는 해당 객체로 설정할 수 있습니다.

```JavaScript
mermaid.flowchartConfig = {
    width: 100%
}
```