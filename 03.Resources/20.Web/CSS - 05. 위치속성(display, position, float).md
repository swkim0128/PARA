---
type: HTML/CSS
archive: false
---
## 디스플레이

### display 속성

---

display 속성은 웹 페이지의 레이아웃(layout)을 결정하는 CSS의 중요한 속성 중 하나입니다.

이 속성은 해당 HTML 요소가 웹 브라우저에 언제 어떻게 보이는가를 결정합니다.

대부분의 HTML 요소는 display 속성의 기본값으로 다음 두 가지 값 중 하나의 값을 가집니다.

1. 블록(block)

2. 인라인(inline)

### 블록(block)

---

display 속성값이 블록(block)인 요소는 언제나 새로운 라인(line)에서 시작하며, 해당 라인의 모든 너비를 차지합니다.

> [!important]  
> <div>, <h1>, <p>, <ul>, <ol>, <form>요소는 대표적인 블록(block) 요소입니다.  

### 인라인(inline)

---

display 속성값이 인라인(inline)인 요소는 새로운 라인(line)에서 시작하지 않습니다.

또한, 요소의 너비도 해당 라인 전체가 아닌 해당 HTML 요소의 내용(content)만큼만 차지합니다.

> [!important]  
> <span>, <a>, <img>요소는 대표적인 인라인(inline) 요소입니다.  

### display 속성의 기본 설정값의 변경

---

HTML의 모든 요소는 각각의 기본 display 속성값을 가지고 있습니다.

하지만 display 속성값이 블록인 요소의 속성값을 인라인으로 바꿀 수 있습니다.

또한, 반대로 display 속성값이 인라인인 요소의 속성값을 블록으로 바꿀 수도 있습니다.

이렇게 HTML 요소의 display 속성값을 변경함으로써 웹 페이지를 개발자가 원하는 모양으로 변경할 수 있습니다.

```HTML
<style>
li { display: inline; }
</style>
```

위의 예제에서 블록 요소인 <li>요소의 display 속성값을 인라인으로 변경하고 있습니다.

display 속성값이 인라인으로 변경된 <li>요소는 해당 라인의 모든 너비를 차지하는 블록 요소의 특징을 잃어버리게 됩니다.

display 속성값을 변경해도, 실제로 해당 요소가 완전히 다른 타입의 요소로 바뀌는 것은 아닙니다.

즉, display 속성값을 인라인에서 블록으로 변경했더라도, 변경된 요소는 내부에 다른 요소를 포함할 수 없습니다.

왜냐하면, 처음부터 display 속성값이 블록인 요소만이 내부에 다른 요소를 포함할 수 있기 때문입니다.

### 인라인-블록(inline-block)

---

인라인과 블록 이외에도 display 속성에 자주 사용되는 속성값에는 인라인-블록(inline-block)이 있습니다.

display 속성값이 인라인-블록으로 설정된 요소는 해당 요소 자체는 인라인(inline) 요소처럼 동작합니다.

하지만 해당 요소 내부에서는 블록(block) 요소처럼 동작합니다.

이처럼 인라인-블록 요소는 인라인 요소와 비슷하지만, 너비와 높이를 설정할 수 있습니다.

또한, 블록 요소처럼 margin을 이용하여 여백을 지정할 수도 있게 됩니다.

다음 예제는 다양한 display 속성값의 동작을 보여주는 예제입니다.

```HTML
<style>
div { width: 100px; height: 50px; }
.first { background-color: aqua; }
.second { background-color: green; }
.third { background-color: yellow; }
.inline { display: inline; }
.inline-block { display: inline-block; }
</style>
```

  

위의 예제처럼 display 속성값이 인라인-블록으로 설정된 요소들은 인라인 요소처럼 한 줄로 늘어서게 됩니다.

하지만 블록 요소처럼 너비와 높이를 설정할 수 있게 됩니다.

따라서 웹 사이트의 메뉴나 내비게이션 바를 만들 때 자주 사용됩니다.

### visibility 속성

---

visibility 속성은 HTML 요소가 웹 페이지에 표현될지 아닐지만을 결정합니다.

따라서 웹 페이지에는 나타나지 않더라도 레이아웃 내에는 여전히 존재하게 되며, 코드 내에도 당연히 존재하게 됩니다.

visibility 속성을 자바스크립트와 함께 사용하면 매우 복잡한 메뉴나 레이아웃을 손쉽게 만들 수 있습니다.

visibility 속성에 사용할 수 있는 속성값은 다음과 같습니다.

1. visible : 해당 HTML 요소를 웹 페이지에 나타냅니다.

2. hidden : HTML 요소를 웹 페이지에 나타내지 않습니다. 하지만 여전히 웹 페이지의 레이아웃에는 존재합니다.

3. collapse : 이 속성값은 동적인 테이블에서만 사용할 수 있으며, 테이블의 테두리를 한 줄만 보여줍니다.

### HTML 요소 숨기기

---

HTML 요소를 숨기기 위해서는 display 속성값을 none으로 설정하면 됩니다.

이렇게 하면 해당 요소는 웹 페이지에 더 이상 나타나지 않으며, 웹 페이지의 레이아웃에도 영향을 미치지 않습니다.

또한, visibility 속성값을 hidden으로 설정해도 HTML 요소를 숨길 수 있습니다.

하지만 display 속성값을 none으로 설정한 것과는 달리, 눈에 보이지만 않을 뿐 여전히 웹 페이지의 레이아웃에는 존재하게 됩니다.

```HTML
<style>
p.none { display: none; }
p.hidden { visibility: hidden; }
</style>
```

> [!important]  
> 따라서 민감하거나 귀중한 데이터를 visibility 속성을 이용하여 감추는 것은 바람직하지 못합니다.  

### opacity 속성

---

opacity 속성을 이용하면 HTML 요소의 투명도를 간단히 조절할 수 있습니다.

opacity 속성값은 0.0부터 1.0까지 설정할 수 있으며, 속성값이 0에 가까울수록 투명한 상태가 됩니다.

익스플로러 8과 그 이전 버전에서는 투명도를 표현하기 위해 다음과 같은 문법을 사용합니다.

> [!important]  
> 문법filter:alpha(opacity=x)  

여기서 x값은 0부터 100까지 설정할 수 있으며, x값이 0에 가까울수록 투명한 상태가 됩니다.

다음 예제는 대부분의 웹 브라우저뿐만 아니라 익스플로러 8과 그 이전 버전에서도 투명도를 정확하게 표현하는 예제입니다.

```HTML
<style> 
img { opacity: 0.4; filter: alpha(opacity=40); } 
img:hover { opacity: 1.0; filter: alpha(opacity=100); } 
</style>
```

  

## 포지션

### position 속성

---

position 속성은 HTML 요소가 위치를 결정하는 방식을 설정합니다.

CSS에서 요소의 위치를 결정하는 방식에는 다음과 같이 4가지 방식이 있습니다.

1. 정적 위치(static position) 지정 방식

2. 상대 위치(relative position) 지정 방식

3. 고정 위치(fixed position) 지정 방식

4. 절대 위치(absolute position) 지정 방식

### 정적 위치(static position) 지정 방식

---

HTML 요소의 위치를 결정하는 가장 기본적인 방식은 정적 위치(static position) 지정 방식입니다.

position 속성값이 static으로 설정된 요소는 top, right, bottom, left 속성값에 영향을 받지 않습니다.

정적 위치(static position) 지정 방식은 단순히 웹 페이지의 흐름에 따라 차례대로 요소들을 위치시키는 방식입니다.

```HTML
<style>
div { position: static; }
</style>
```

모든 HTML 요소의 position 속성의 기본 설정값은 static입니다.

### 상대 위치(relative position) 지정 방식

---

상대 위치(relative position) 지정 방식은 해당 HTML 요소의 기본 위치를 기준으로 위치를 설정하는 방식입니다.

HTML 요소의 기본 위치란 해당 요소가 정적 위치(static position) 지정 방식일 때 결정되는 위치를 의미합니다.

```HTML
<style>
div.relative { position: relative; left: 30px; }
</style>
```

### 고정 위치(fixed position) 지정 방식

---

고정 위치(fixed position) 지정 방식은 뷰포트(viewport)를 기준으로 위치를 설정하는 방식입니다.

즉, 웹 페이지가 스크롤 되어도 고정 위치로 지정된 요소는 항상 같은 곳에 위치하게 됩니다.

```HTML
<style>
div.fixed { position: fixed; top: 0; right: 0; }
</style>
```

### 절대 위치(absolute position) 지정 방식

---

절대 위치(absolute position) 지정 방식은 고정 위치가 뷰포트를 기준으로 위치를 결정하는 것과 비슷하게 동작합니다.

단지 뷰포트(viewport)를 기준으로 하는 것이 아닌 위치가 설정된 조상(ancestor) 요소를 기준으로 위치를 설정하게 됩니다.

하지만 위치가 설정된 조상(ancestor) 요소를 가지지 않는다면, HTML 문서의 body 요소를 기준으로 위치를 설정하게 됩니다.

```HTML
<style>
div.absolute { position: absolute; top: 50px; right: 0; }
</style>
```

위치가 설정된 요소라는 것은 정적 위치(static position) 지정 방식을 제외한 다른 방식(relative, fixed, absolute)으로 위치가 설정된 요소를 의미합니다.

### 정적 위치(static position) 지정 방식과 다른 방식들과의 차이점

---

정적 위치(static position) 지정 방식을 제외한 나머지 다른 방식(relative, fixed, absolute)들은 전부 어떤 기준에 대해 해당 요소의 상대적인 위치를 설정하는 방식입니다.

- 상대 위치(relative position) : 해당 요소가 정적 위치 지정 방식일 때의 위치에 상대적으로 위치함.
- 고정 위치(fixed position) : 뷰포트(viewport)에 상대적으로 위치함.
- 절대 위치(absolute position) : 위치가 설정된 바로 상위의 조상(ancestor) 요소에 상대적으로 위치함.

```HTML
<style>
.static { position: static; }
.relative { position: relative; }
.fixed { position: fixed; }
.absolute { position: absolute; }
</style>
```

### z-index 속성

---

HTML 요소의 위치를 설정하게 되면 어떤 요소들은 설정된 위치 및 방식에 따라 서로 겹칠 수도 있습니다.

z-index 속성은 이렇게 겹쳐지는 요소들이 쌓이는 스택(stack)의 순서를 설정합니다.

스택(stack)의 순서는 양수나 음수 모두 설정할 수 있으며, 크기가 클수록 앞쪽에 위치하고 작을수록 뒤쪽에 위치하게 됩니다.

```HTML
<style> 
.last { 
position: fixed; 
top: 180px; 
left: 120px; 
z-index: -1; } 
</style>
```

### CSS position 속성

---

|속성|설명|
|---|---|
|position|HTML 요소의 위치를 결정하는 방식을 설정함.|
|top|위치가 설정된 조상 요소의 위로부터의 여백을 설정함.|
|right|위치가 설정된 조상 요소의 오른쪽으로부터의 여백을 설정함.|
|bottom|위치가 설정된 조상 요소의 아래로부터의 여백을 설정함.|
|left|위치가 설정된 조상 요소의 왼쪽으로부터의 여백을 설정함.|
|z-index|겹쳐지는 요소들이 쌓이는 스택(stack)의 순서를 설정함.|
|clip|절대 위치(absolute position) 지정 방식으로 위치한 요소를 자름.|
|cursor|표시되는 마우스 커서의 모양을 설정함.|
|overflow|내용(content)의 크기가 해당 요소의 박스(box)를 넘어갈 때 어떻게 처리할지를 설정함.|
|overflow-x|내용(content)의 크기가 해당 요소의 수평 방향으로 박스(box)를 넘어갈 때 어떻게 처리할지를 설정함.|
|overflow-y|내용(content)의 크기가 해당 요소의 수직 방향으로 박스(box)를 넘어갈 때 어떻게 처리할지를 설정함.|

overflow 속성에 대한 더 자세한 사항은 CSS 플로트 수업에서 확인할 수 있습니다.

[CSS 플로트 수업 확인 =>](http://www.tcpschool.com/css/css_position_float)

  

## Float

### float 속성

---

float 속성은 해당 HTML 요소가 주변의 다른 요소들과 자연스럽게 어울리도록 만들어 줍니다.

이 속성은 본래 위와 같은 목적으로 만들어졌지만, 현재는 웹 페이지의 레이아웃(layout)을 작성할 때 자주 사용됩니다.

다음 예제는 이미지와 글자를 함께 출력하는 예제입니다.

```HTML
<style>
img { float: left; margin-right: 20px; }
</style>
```

### clear 속성

---

clear 속성은 float 속성이 적용된 이후 나타나는 요소들의 동작을 조절해 줍니다.

컨테이너 요소에 float 속성이 적용되면 그 이후에 등장하는 모든 요소들은 정확한 위치를 설정하기가 매우 힘들어집니다.

```HTML
<style> 
.left { background-color: \#FF8C00; width: 150px; height: 50px; float: left; } 
.right { background-color: \#9932CC; width: 150px; height: 50px; float: right; } 
</style>
```

따라서 float 속성을 적용하고자 하는 요소가 모두 등장한 이후에는 clear 속성을 사용하여, 이후에 등장하는 요소들이 더는 flaot 속성에 영향을 받지 않도록 설정해줘야 합니다.

```HTML
<style> 
.left { background-color: \#FF8C00; width: 150px; height: 50px; float: left; } 
.right { background-color: \#9932CC; width: 150px; height: 50px; float: right; } 
p { clear: both; } 
</style>
```

### overflow 속성

---

float 속성이 적용된 HTML 요소가 자신을 감싸고 있는 컨테이너 요소보다 크면, 해당 요소의 일부가 밖으로 흘러넘치게 됩니다.

이때 overflow 속성값을 auto로 설정하면, 컨테이너 요소의 크기가 자동으로 내부의 요소를 감쌀 수 있을 만큼 커지게 됩니다.

```HTML
<style> 
div { border: 3px solid \#73AD21; padding: 5px;} 
img { float: left; } 
.good { overflow: auto; } 
</style>
```

### float 속성을 이용한 레이아웃

---

현재 웹 페이지의 레이아웃은 대부분 float 속성을 이용하여 작성되고 있습니다.

다음 예제는 float 속성을 이용해 작성된 레이아웃을 보여줍니다.

```HTML
<style> 
div.page { border: 3px solid \#CD5C5C; overflow: auto; } 
h2 { text-align: center; } 
header{ border: 3px solid \#FFD700; } 
nav { border: 3px solid \#FF1493; width: 150px; float: left; } 
section { border: 3px solid \#00BFFF; margin-left: 156px; } 
footer{ border: 3px solid \#00FA9A; } 
</style>
```

### CSS float 속성

---

|속성|설명|
|---|---|
|float|HTML 요소가 주변의 다른 요소들과 자연스럽게 어울리도록 설정함.|
|clear|float 속성이 적용된 후 나타나는 요소들이 더 이상 float 속성에 영향을 받지 않도록 설정함.|
|overflow|내용(content)의 크기가 해당 요소를 감싸고 있는 컨테이너 요소보다 클 때 어떻게 처리할지를 설정함.|
|overflow-x|내용(content)의 크기가 해당 요소의 수평 방향 박스(box)를 넘어갈 때 어떻게 처리할지를 설정함.|
|overflow-y|내용(content)의 크기가 해당 요소의 수직 방향 박스(box)를 넘어갈 때 어떻게 처리할지를 설정함.|

  

## 정렬

### 정렬(align)

---

블록(block) 타입의 요소를 정렬하기 위해서는 다음과 같은 방법을 사용할 수 있습니다.

1. margin 속성을 이용한 가운데 정렬

2. position 속성을 이용한 좌우 정렬

3. float 속성을 이용한 좌우 정렬

### margin 속성을 이용한 가운데 정렬

---

margin 속성값을 auto로 설정하면, 해당 요소를 감싸고 있는 컨테이너 요소를 기준으로 수평 방향 가운데 정렬이 됩니다.

이때 해당 요소는 특정한 너비를 가져야 하며, 너비를 제외한 나머지 공간은 좌우로 균등하게 나뉘어 여백으로 만들어집니다.

따라서 이 방법을 사용하기 위해서는 반드시 해당 요소의 width 속성값을 먼저 설정해야만 합니다.

```HTML
<style>
div { width: 300px; margin: auto; }
</style>
```

> [!important]  
> 익스플로러 8과 그 이전 버전에서는 HTML 문서에 <!DOCTYPE html>태그가 삽입되어 있어야 float 속성이 제대로 표현됩니다.  

### position 속성을 이용한 좌우 정렬

---

절대 위치 지정 방식으로 위치한 요소는 정상적인 레이아웃에서 벗어나 다른 요소와 겹칠 수 있게 됩니다.

따라서 이 특성을 이용하면 HTML 요소를 수평 방향으로 좌우 정렬할 수 있습니다.

position 속성을 이용하여 정렬할 경우에는 <body>요소에 margin과 padding 속성값을 설정하는 것이 좋습니다.

이렇게 함으로써 웹 브라우저마다 레이아웃이 다르게 보이는 것을 미리 방지할 수 있습니다.

```HTML
<style> 
div { width: 300px; padding: 10px; margin: 0; position: absolute; right: 0; } 
</style>
```

> [!important]  
> 익스플로러 8과 그 이전 버전에서는 HTML 문서에 <!DOCTYPE html>태그가 삽입되어 있어야 float 속성이 제대로 표현됩니다.  

### float 속성을 이용한 좌우 정렬

---

float 속성을 이용하면 수평 방향으로 좌우 정렬할 수 있습니다.

float 속성을 이용하여 정렬할 경우에는 <body>요소에 margin과 padding 속성값을 설정하는 것이 좋습니다.

이렇게 함으로써 웹 브라우저마다 레이아웃이 다르게 보이는 것을 미리 방지할 수 있습니다.

```HTML
<style> 
div { width: 350px; padding: 10px; margin: 0; } 
div.left { float: left } 
div.right { float: right } 
</style>
```

> [!important]  
> 익스플로러 8과 그 이전 버전에서는 HTML 문서에 <!DOCTYPE html>태그가 삽입되어 있어야 float 속성이 제대로 표현됩니다.