---
type: HTML/CSS
archive: false
---
## 패딩

### 패딩(padding)

---

padding 속성은 내용(content)과 테두리(border) 사이의 간격인 패딩 영역의 크기를 설정합니다.

이러한 패딩 영역은 background-color 속성으로 설정하는 배경색의 영향을 함께 받습니다.

CSS를 사용하면 패딩 영역의 크기를 방향별로 따로 설정할 수 있습니다.

[![](http://www.tcpschool.com/lectures/img_css_boxmodel_padding.png)](http://www.tcpschool.com/lectures/img_css_boxmodel_padding.png)

### 패딩(padding) 속성

---

CSS에서는 HTML 요소의 패딩 영역을 설정하기 위해 다음과 같은 속성을 제공합니다.

1. padding-top

2. padding-right

3. padding-bottom

4. padding-left

```HTML
<style> 
div.pad { 
padding-top: 50px; 
padding-right: 10px; 
padding-bottom: 30px; 
padding-left: 100px; 
} 
</style>
```

### 패딩 축약 표현(padding shorthand)

---

모든 padding 속성을 이용한 스타일을 한 줄에 설정할 수 있습니다.

```HTML
<style> 
div.four { padding: 20px 50px 30px 50px; } 
div.three { padding: 20px 50px 30px; } 
</style>
```

4개의 padding 속성값을 가질 때는 top, right, bottom, left 순으로 설정합니다.

ex) padding: 10px 20px 30px 40px;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

padding-top: 10px;

padding-right: 20px;

padding-bottom: 30px;

padding-left: 40px;

  

3개의 padding 속성값을 가질 때는 top, right와 left, bottom 순으로 설정합니다.

ex) padding: 10px 20px 30px;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

padding-top: 10px;

padding-right: 20px;

padding-bottom: 30px;

padding-left: 20px;

  

2개의 padding 속성값을 가질 때는 top과 bottom, right와 left 순으로 설정합니다.

ex) padding: 10px 20px;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

padding-top: 10px;

padding-right: 20px;

padding-bottom: 10px;

padding-left: 20px;

  

1개의 padding 속성값을 가질 때는 모든 패딩값을 같게 설정합니다.

ex) padding: 10px;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

padding-top: 10px;

padding-right: 10px;

padding-bottom: 10px;

padding-left: 10px;

### CSS padding 속성

---

|속성|설명|
|---|---|
|padding|모든 padding 속성을 이용한 스타일을 한 줄에 설정할 수 있음.|
|padding-top|윗쪽의 패딩(padding) 값을 설정함.|
|padding-right|오른쪽의 패딩(padding) 값을 설정함.|
|padding-bottom|아래쪽의 패딩(padding) 값을 설정함.|
|padding-left|왼쪽의 패딩(padding) 값을 설정함.|

  

## 테두리

### 테두리(border)

---

border 속성은 내용(content)과 패딩(padding) 영역을 둘러싸는 테두리의 스타일을 설정합니다.

[![](http://www.tcpschool.com/lectures/img_css_boxmodel_border.png)](http://www.tcpschool.com/lectures/img_css_boxmodel_border.png)

### border-style 속성

---

border-style 속성을 이용하면 테두리(border)를 다양한 모양으로 설정할 수 있습니다.

- dotted : 테두리를 점선으로 설정함.
- dashed : 테두리를 약간 긴 점선으로 설정함.
- solid : 테두리를 실선으로 설정함.
- double : 테두리를 이중 실선으로 설정함.
- groove : 테두리를 3차원인 입체적인 선으로 설정하며, border-color 속성값에 영향을 받음.
- ridge : 테두리를 3차원인 능선효과가 있는 선으로 설정하며, border-color 속성값에 영향을 받음.
- inset : 테두리를 3차원인 내지로 끼운 선으로 설정하며, border-color 속성값에 영향을 받음.
- outset : 테두리를 3차원인 외지로 끼운 선으로 설정하며, border-color 속성값에 영향을 받음.
- none : 테두리를 없앰.
- hidden : 테두리가 존재하기는 하지만 표현되지는 않음.

```HTML
<style>
.dotted {border-style: dotted;}
.dashed {border-style: dashed;}
.solid {border-style: solid;}
.double {border-style: double;}
.groove {border-style: groove;}
.ridge {border-style: ridge;}
.inset {border-style: inset;}
.outset {border-style: outset;}
.none {border-style: none;}
.hidden {border-style: hidden;}
.mix {border-style: solid dashed dotted double;}
</style>
```

### border-width 속성

---

border-width 속성은 테두리(border)의 두께를 설정합니다.

px, em, cm 등과 같은 CSS 크기 단위를 이용하여 두께를 직접 설정할 수 있습니다.

또한, 미리 설정해 놓은 예약어인 thin, medium, thick을 사용하여 설정할 수도 있습니다.

```HTML
<style> 
.dottedA { border-style: dotted; border-width: 2px; } 
.dottedB { border-style: dotted; border-width: 5px; } 
.dashedA { border-style: dashed; border-width: thin; } 
.dashedB { border-style: dashed; border-width: thick; } 
.doubleA { border-style: double; border-width: 5px; } 
.doubleB { border-style: double; border-width: thick; } 
.mix { border-style: solid; border-width: 1px 2px 10px thick; } 
</style>
```

### border-color 속성

---

border-color 속성은 테두리(border)의 색상을 설정합니다.

기본적인 color 속성값들뿐만 아니라 투명한 선을 나타내는 transparent 속성값을 사용할 수도 있습니다.

border-color 속성값이 설정되지 않으면 해당 요소의 color 속성값을 그대로 물려받습니다.

```HTML
<style>
.red { border-color: red; }
.green { border-color: rgb(0,255,0); }
.blue { border-color: \#0000FF; }
.mix { border-color: red green blue maroon; }
.color { color: teal; }
</style>
```

### 테두리(border)의 개별 설정

---

CSS를 사용하면 테두리의 위쪽, 오른쪽, 아래쪽, 왼쪽 부분에 대하여 개별적으로 스타일을 적용할 수 있습니다.

```HTML
<style>
.mixA {
border-top-style: dotted;
border-right-style: double;
border-bottom-style: dotted;
border-left-style: double;
}
.mixB { border-style: dotted double; }
</style>
```

4개의 border-style 속성값을 가질 때는 top, right, bottom, left 순으로 설정합니다.

ex) border-style: dotted dashed solid double;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

border-style-top: dotted;

border-style-right: dashed;

border-style-bottom: solid;

border-style-left: double;

  

3개의 border-style 속성값을 가질 때는 top, right와 left, bottom 순으로 설정합니다.

ex) border-style: dotted dashed solid;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

border-style-top: dotted;

border-style-right: dashed;

border-style-bottom: solid;

border-style-left: dashed;

  

2개의 border-style 속성값을 가질 때는 top과 bottom, right와 left 순으로 설정합니다.

ex) border-style: dotted dashed;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

border-style-top: dotted;

border-style-right: dashed;

border-style-bottom: dotted;

border-style-left: dashed;

  

1개의 border-style 속성값을 가질 때는 모든 테두리의 스타일을 같게 설정합니다.

ex) border-style: dotted;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

border-style-top: dotted;

border-style-right: dotted;

border-style-bottom: dotted;

border-style-left: dotted;

### 테두리 축약 표현(border shorthand)

---

모든 border 속성을 이용한 스타일을 한 줄에 설정할 수 있습니다.

```HTML
<style>
.good { border: 3px solid teal; }
.wrong { border: 5px teal; }
</style>
```

border 속성을 설정하기 위해서는 반드시 border-style 속성이 먼저 설정되어 있어야 합니다.

### CSS border 속성

---

|속성|설명|
|---|---|
|border|모든 border 속성을 이용한 스타일을 한 줄에 설정할 수 있음.|
|border-style|테두리(border)를 다양한 모양으로 설정함.|
|border-width|테두리(border)의 너비를 설정함.|
|border-color|테두리(border)의 색상을 설정함.|
|border-top|테두리(border)의 top 부분 속성을 한 번에 설정함.|
|border-top-style|테두리(border)의 top 부분의 스타일을 설정함.|
|border-top-width|테두리(border)의 top 부분의 너비를 설정함.|
|border-top-color|테두리(border)의 top 부분의 색상을 설정함.|
|border-right|테두리(border)의 right 부분 속성을 한 번에 설정함.|
|border-right-style|테두리(border)의 right 부분의 스타일을 설정함.|
|border-right-width|테두리(border)의 right 부분의 너비를 설정함.|
|border-right-color|테두리(border)의 right 부분의 색상을 설정함.|
|border-bottom|테두리(border)의 bottom 부분 속성을 한 번에 설정함.|
|border-bottom-style|테두리(border)의 bottom 부분의 스타일을 설정함.|
|border-bottom-width|테두리(border)의 bottom 부분의 너비를 설정함.|
|border-bottom-color|테두리(border)의 bottom 부분의 색상을 설정함.|
|border-left|테두리(border)의 left 부분 속성을 한 번에 설정함.|
|border-left-style|테두리(border)의 left 부분의 스타일을 설정함.|
|border-left-width|테두리(border)의 left 부분의 너비를 설정함.|
|border-left-color|테두리(border)의 left 부분의 색상을 설정함.|

  

## 마진

### 마진(Margin)

---

margin 속성은 테두리(border)와 이웃하는 요소 사이의 간격인 마진 영역의 크기를 설정합니다.

이러한 마진 영역은 패딩 영역과는 달리 background-color 속성으로 설정하는 배경색의 영향을 받지 않습니다.

CSS를 사용하면 마진 영역의 크기를 방향별로 따로 설정할 수 있습니다.

[![](http://www.tcpschool.com/lectures/img_css_boxmodel_margin.png)](http://www.tcpschool.com/lectures/img_css_boxmodel_margin.png)

### 마진(margin) 속성

---

CSS에서는 HTML 요소의 마진 영역을 설정하기 위해 다음과 같은 속성을 제공합니다.

1. margin-top

2. margin-right

3. margin-bottom

4. margin-left

margin 속성값을 음수로 설정하여 해당 요소를 다른 요소의 위에 겹치게 할 수도 있습니다.

```HTML
<style> 
div.mar { 
margin-top: -25px; 
margin-right: 10px; 
margin-bottom: 30px; 
margin-left: 100px; 
} 
</style>
```

margin 속성값을 inherit로 설정하면, 부모(parent) 요소의 margin 속성값을 그대로 물려받습니다.

```HTML
<style>
div.parent { height: 100px; margin-left: 100px; }
div.child { background-color: \#FFF8DC; margin-left: inherit; }
</style>
```

### 마진 축약 표현(margin shorthand)

---

모든 margin 속성을 이용한 스타일을 한 줄에 설정할 수 있습니다.

```HTML
<style>
div.four { margin: 20px 50px 30px 50px; }
div.three { margin: 20px 50px 30px; }
</style>
```

4개의 margin 속성값을 가질 때는 top, right, bottom, left 순으로 설정합니다.

ex) margin: 10px 20px 30px 40px;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

margin-top: 10px;

margin-right: 20px;

margin-bottom: 30px;

margin-left: 40px;

  

3개의 margin 속성값을 가질 때는 top, right와 left, bottom 순으로 설정합니다.

ex) margin: 10px 20px 30px;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

margin-top: 10px;

margin-right: 20px;

margin-bottom: 30px;

margin-left: 20px;

  

2개의 margin 속성값을 가질 때는 top과 bottom, right와 left 순으로 설정합니다.

ex) margin: 10px 20px;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

margin-top: 10px;

margin-right: 20px;

margin-bottom: 10px;

margin-left: 20px;

  

1개의 margin 속성값을 가질 때는 모든 마진값을 같게 설정합니다.

ex) margin: 10px;

(위의 예제는 아래 4줄의 코드와 같은 의미를 가지고 있습니다.)

margin-top: 10px;

margin-right: 10px;

margin-bottom: 10px;

margin-left: 10px;

### margin 속성값에 auto를 사용하는 이유

---

margin 속성값을 auto로 설정하면, 웹 브라우저가 수평 방향 마진(margin) 값을 자동으로 설정합니다.

즉, 해당 HTML 요소의 왼쪽과 오른쪽 마진을 자동으로 설정하게 됩니다.

그 결과 해당 요소는 그 요소를 포함하고 있는 부모(parent) 요소의 정중앙에 위치하게 됩니다.

```HTML
<style>
div {
border: 2px solid teal;
width: 300px;
margin: auto;
}
</style>
```

### CSS margin 속성

---

|속성|설명|
|---|---|
|margin|모든 margin 속성을 이용한 스타일을 한 줄에 설정할 수 있음.|
|margin-top|윗쪽의 마진(margin) 값을 설정함.|
|margin-right|오른쪽의 마진(margin) 값을 설정함.|
|margin-bottom|아래쪽의 마진(margin) 값을 설정함.|
|margin-left|왼쪽의 마진(margin) 값을 설정함.|

  

## 아웃라인

### 아웃라인(Outline)

---

outline 속성은 HTML 요소의 가장 바깥 부분을 둘러싸고 있는 아웃라인 부분의 스타일을 설정합니다.

이 속성은 border 속성과 마찬가지로 style, width, color 속성을 가집니다.

하지만 outline 속성은 border 속성과는 달리 HTML 요소의 전체 크기에는 포함되지 않습니다.

HTML 요소의 높이나 너비는 outline의 두께에 전혀 영향을 받지 않습니다.

### outline-style 속성

---

outline-style 속성을 이용하면 아웃라인(outline)을 다양한 모양으로 설정할 수 있습니다.

1. dotted : 아웃라인을 점선으로 설정함.

2. dashed : 아웃라인을 약간 긴 점선으로 설정함.

3. solid : 아웃라인을 실선으로 설정함.

4. double : 아웃라인을 이중 실선으로 설정함.

5. groove : 아웃라인을 3차원인 입체적인 선으로 설정하며, outline-color 속성값에 영향을 받음.

6. ridge : 아웃라인을 3차원인 능선효과가 있는 선으로 설정하며, outline-color 속성값에 영향을 받음.

7. inset : 3차원인 내지로 끼운 선으로 설정하며, outline-color 속성값에 영향을 받음.

8. outset : 3차원인 외지로 끼운 선으로 설정하며, outline-color 속성값에 영향을 받음.

9. none : 아웃라인(outline)을 없앰.

10. hidden : 아웃라인(outline)이 존재하기는 하지만 표현되지는 않음.

```HTML
<style>
p.dotted {outline-style: dotted;}
p.dashed {outline-style: dashed;}
p.solid {outline-style: solid;}
p.double {outline-style: double;}
p.groove {outline-style: groove;}
p.ridge {outline-style: ridge;}
p.inset {outline-style: inset;}
p.outset {outline-style: outset;}
p.none {outline-style: none;}
p.hidden {outline-style: hidden;}
</style>
```

> [!important]  
> 익스플로러 8과 그 이전 버전에서는 HTML 문서에 <!DOCTYPE html>태그가 삽입되어 있어야 outline 속성이 제대로 표현됩니다.  

### outline-width 속성

---

outline-width 속성은 아웃라인(outline)의 두께를 설정합니다.

px, em, cm 등과 같은 CSS 크기 단위를 이용하여 두께를 직접 설정할 수 있습니다.

또한, 미리 설정해 놓은 예약어인 thin, medium, thick을 사용하여 설정할 수도 있습니다.

```HTML
<style>
p.solidA { outline-style: solid; outline-color: violet; outline-width: 2px; }
p.solidB { outline-style: solid; outline-color: coral; outline-width: 7px; }
p.dashedA { outline-style: dashed; outline-color: violet; outline-width: thin; }
p.dashedB { outline-style: dashed; outline-color: coral; outline-width: thick; }
</style>
```

### outline-color 속성

---

outline-color 속성은 아웃라인(outline)의 색상을 설정합니다.

기본적인 color 속성값들뿐만 아니라 색반전을 나타내는 invert 속성값을 사용할 수 있습니다.

또한, invert 속성값은 배경색과 상관없이 아웃라인을 보여주기 위한 색반전을 설정합니다.

```HTML
<style> 
p { border: 1px solid black; outline-style: dashed; } 
p.red { outline-color: red; } 
p.green { outline-color: rgb(0,255,0); } 
p.blue { outline-color: \#0000FF; } 
p.invert { outline-color: invert; } 
</style>
```

### 아웃라인 축약 표현(outline shorthand)

---

모든 outline 속성을 이용한 스타일을 한 줄에 설정할 수 있습니다.

```HTML
<style> 
p { border: 1px solid black; } 
p.none { border-style: none; } 
p.good { outline: 3px solid teal; } 
p.wrong { outline: 5px teal; } 
</style>
```

outline 속성을 설정하기 위해서는 반드시 outline-style 속성이 먼저 설정되어 있어야 합니다.

### CSS outline 속성

---

|속성|설명|
|---|---|
|outline|모든 outline 속성을 이용한 스타일을 한 줄에 설정할 수 있음.|
|outline-style|아웃라인(outline)를 다양한 모양으로 설정함.|
|outline-width|아웃라인(outline)의 너비를 설정함.|
|outline-color|아웃라인(outline)의 색상을 설정함.|
|outline-offset|테두리(border)와 아웃라인(outline) 사이의 여백을 설정함.|