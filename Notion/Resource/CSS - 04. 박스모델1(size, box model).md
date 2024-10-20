---
type: HTML/CSS
archive: false
---
## 크기 단위

### 크기 단위

---

CSS에서 사용하는 크기의 단위에는 %, em, px, cm, mm, inch 등이 있습니다.

그 중에서도 가장 많이 쓰이는 크기 단위는 다음과 같습니다.

1. 백분율 단위(%)

2. 배수 단위(em)

3. 픽셀 단위(px)

백분율 단위(%)는 기본 크기를 100%로 놓고, 그에 대한 상대적인 크기를 설정합니다.

배수 단위(em)는 해당 글꼴(font)의 기본 크기를 1em으로 놓고, 그에 대한 상대적인 크기를 설정합니다.

픽셀 단위(px)는 스크린의 픽셀(pixel)을 기준으로 하는 절대적인 크기를 설정합니다.

```HTML
<style>
\#large { font-size: 200%; }
\#small { font-size: 0.7em; }
\#fixed { font-size: 20px; }
</style>
```

> [!important]  
> 1배 = 1em = 100%를 의미합니다.  

  

## 크기

### 크기(Dimension)

---

CSS를 이용하면 HTML 요소의 크기를 마음대로 설정할 수 있습니다.

CSS에서 크기 조절을 위해 사용할 수 있는 속성은 다음과 같습니다.

1. height

2. width

3. max-width

4. min-width

5. max-height

6. min-height

### height와 width 속성

---

height와 width 속성은 HTML 요소의 높이와 너비를 각각 설정합니다.

이 속성의 기본 설정값은 auto이며, 웹 브라우저가 각 HTML 요소에 맞게 자동으로 높이와 너비를 설정해 줍니다.

```HTML
<style>
div { height: 200px; width: 500px; }
</style>
```

### max-width 속성

---

max-width 속성은 해당 HTML 요소가 가질 수 있는 최대 너비(width)를 설정합니다.

이 속성의 기본 설정값은 none이며, 해당 HTML 요소의 너비에 제한을 두지 않겠다는 의미입니다.

width 속성으로 너비를 설정하면, 설정된 너비 이하로 브라우저의 크기가 줄어들 때 해당 요소에 스크롤 바를 생성하게 됩니다.

하지만 max-width 속성으로 너비를 설정하면 다음과 같이 좀 더 유연한 결과를 얻을 수 있습니다.

max-width 속성으로 너비를 설정하면 줄어드는 웹 브라우저의 크기에 맞춰 해당 HTML 요소의 너비도 자동으로 줄어듭니다.

```HTML
<style>
div.maxWidth { max-width: 500px; }
</style>
```

### min-width 속성

---

min-width 속성은 해당 HTML 요소가 가질 수 있는 최소 너비(width)를 설정합니다.

이 속성의 기본 설정값은 0이며, 해당 HTML 요소의 너비에 제한을 두지 않겠다는 의미입니다.

min-width 속성이 설정된 요소에 width 속성값을 따로 설정하지 않으면 초기 너비(width)는 100%를 가지게 됩니다.

이때 웹 브라우저의 크기가 줄어들면 거기에 맞춰 HTML 요소의 너비도 자동으로 줄어듭니다.

하지만 웹 브라우저가 min-width 속성으로 설정된 너비 이하로 줄어들면, HTML 요소의 너비는 더는 줄어들지 않고 수평 스크롤 바를 생성하게 됩니다.

```HTML
<style>
div.minWidth { min-width: 500px; }
</style>
```

### max-height 속성

---

max-height 속성은 해당 HTML 요소가 가질 수 있는 최대 높이(height)를 설정합니다.

이 속성의 기본 설정값은 none이며, 해당 HTML 요소의 크기에 따라 높이가 자동으로 설정됩니다.

max-height 속성으로 최대 높이를 설정하면, 해당 HTML 요소의 높이를 설정된 높이 이하로 제한합니다.

만약 해당 요소의 높이가 설정된 최대 높이보다 클 경우에는 수직 스크롤 바를 생성하게 됩니다.

```HTML
<style>
p { max-height: 50px; overflow: auto; }
</style>
```

### min-height 속성

---

min-height 속성은 지정된 HTML 요소가 가질 수 있는 최소 높이(height)를 설정합니다.

이 속성의 기본 설정값은 0이며, 해당 HTML 요소의 높이에 제한을 두지 않겠다는 의미입니다.

min-height 속성을 설정하면 해당 HTML 요소의 높이를 설정된 높이 이하로 제한합니다.

즉 height 속성값이 min-height 속성값 이하로 낮아지지 않도록 합니다.

이러한 min-height 속성값은 max-height 속성값과 height 속성값보다 먼저 적용됩니다.

```HTML
<style>
p { min-height: 100px; }
</style>
```

### CSS 크기(dimension) 속성

---

|속성|설명|
|---|---|
|height|해당 HTML 요소의 높이를 설정함.|
|width|해당 HTML 요소의 너비를 설정함.|
|max-width|해당 HTML 요소가 가질 수 있는 최대 너비(width)를 설정함.|
|min-width|해당 HTML 요소가 가질 수 있는 최소 너비(width)를 설정함.|
|max-height|해당 HTML 요소가 가질 수 있는 최대 높이(height)를 설정함.|
|min-height|해당 HTML 요소가 가질 수 있는 최소 높이(height)를 설정함.|

  

## 박스 모델

### 박스 모델(box model)

---

모든 HTML 요소는 박스(box) 모양으로 구성되며, 이것을 박스 모델(box model)이라고 부릅니다.

박스 모델은 HTML 요소를 패딩(padding), 테두리(border), 마진(margin), 그리고 내용(content)으로 구분합니다.

[![](http://www.tcpschool.com/lectures/img_css_boxmodel.png)](http://www.tcpschool.com/lectures/img_css_boxmodel.png)

1. 내용(content) : 텍스트나 이미지가 들어있는 박스의 실질적인 내용 부분입니다.

2. 패딩(padding) : 내용과 테두리 사이의 간격입니다. 패딩은 눈에 보이지 않습니다.

3. 테두리(border) : 내용와 패딩 주변을 감싸는 테두리입니다.

4. 마진(margin) : 테두리와 이웃하는 요소 사이의 간격입니다. 마진은 눈에 보이지 않습니다.

```HTML
<style> 
div { 
background-color: red; 
padding: 50px; 
border: 20px solid maroon; 
margin: 50px; } 
</style>
```

### height와 width 속성의 이해

---

모든 웹 브라우저에서 정확하게 HTML 요소들을 표현하려면 이러한 박스 모델이 어떻게 동작하는지 정확히 알아야만 합니다.

CSS에서 height와 width 속성을 설정할 때 그 크기가 가르키는 부분은 내용(content) 부분만을 대상으로 합니다.

HTML 요소의 height와 width 속성으로 설정된 높이와 너비에 패딩(padding), 테두리(border), 마진(margin)의 크기는 포함되지 않습니다.

```HTML
<style> 
div { 
width: 320px; 
padding: 10px; 
border: 5px solid maroon; 
margin: 0; } 
</style>
```

### HTML 요소의 높이와 너비 구하기

---

[![](http://www.tcpschool.com/lectures/img_css_boxsize.png)](http://www.tcpschool.com/lectures/img_css_boxsize.png)

위의 그림에서 전체 너비(width)를 계산해 보면,

width(70px) + left margin(10px) + left padding(5px) + right padding(5px) + right margin(10px) = 100px 이 됩니다.

즉, HTML 요소의 전체 너비(width)를 계산하는 공식은

width + left padding + right padding + left border + right border + left margin + right margin 입니다.

또한, HTML 요소의 전체 높이(height)를 계산하는 공식은

height + top padding + bottom padding + top border + bottom border + top margin + bottom margin 입니다.

이때 마진(margin) 영역의 크기는 눈으로 바로 확인할 수는 없을 것입니다.

왜냐하면 마진이란 테두리(border)와 이웃하는 요소 사이의 간격이면서, 배경색의 영향을 받지 않기 때문입니다.

하지만 HTML 요소가 차지하는 크기에는 포함됩니다.

> [!important]  
> 익스플로러 8과 그 이전 버전에서는 width나 height 속성으로 설정한 너비나 높이에 패딩과 테두리의 크기까지 포함됩니다.이러한 차이점을 없애기 위해서는 반드시 HTML 문서에 <!DOCTYPE html>태그를 삽입해야만 합니다.