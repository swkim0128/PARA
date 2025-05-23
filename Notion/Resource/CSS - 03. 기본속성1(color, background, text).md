---
type: HTML/CSS
archive: false
---
## CSS 색

> [!important]  
> CSS에서 색을 표현하는 방법에는 다음과 같이 세 가지 방법이 있습니다.1. 색상 이름으로 표현2. RGB 색상값으로 표현3. 16진수 색상값으로 표현  

  

### 색상 이름으로 표현

---

HTML에서 색상 이름은 대소문자를 구분하지 않습니다.

```HTML
<style>
.blue { color: blue; }
.green { color: green; }
.silver { color: silver; }
</style>
```

현재는 대부분의 브라우저가 140개의 색상 이름을 지원하고 있습니다.

### RGB 색상값으로 표현

---

모니터나 스크린은 빨간색(Red), 녹색(Green), 파란색(Blue)을 혼합하여 색을 표현합니다.

따라서 HTML에서도 이 세 가지 색을 가지고 색을 표현하는 RGB 색상을 사용합니다.

RGB 색상의 기본색(Red, Green, Blue)은 각각 0부터 255까지의 범위를 가집니다.

```HTML
<style>
.blue { color: rgb(**0,0,255**); }
.green { color: rgb(**0,128,0**); }
.silver { color: rgb(**192,192,192**); }
</style>
```

### 16진수 색상값으로 표현

---

16진수 색상값은 RGB 색상값을 각각 16진수로 변환한 것입니다.

따라서 RGB 색상의 기본색(Red, Green, Blue)은 각각 00부터 FF까지의 범위를 가집니다.

예를 들면, 녹색을 나타내는 RGB 색상값 rgb(0,255,0)은 16진수 색상값으로는 \#00FF00이 됩니다.

```HTML
<style>
.blue { color: **\#0000FF**; }
.green { color: **\#008000**; }
.silver { color: **\#C0C0C0**; }
</style>
```

  

## **CSS 배경**

CSS에서 사용할 수 있는 background 속성은 다음과 같습니다.

1. background-color

2. background-image

3. background-repeat

4. background-position

5. background-attachment

### background-color 속성

---

background-color 속성은 해당 HTML 요소의 배경색(background color)을 설정합니다.

```HTML
<style>
body { background-color: lightblue; }
h1 { background-color: rgb(**255,128,0**); }
p { background-color: **\#FFFFCC**; }
</style>
```

### background-image 속성

---

background-image 속성은 해당 HTML 요소의 배경으로 나타날 배경 이미지(image)를 설정합니다.

설정된 배경 이미지는 기본 설정으로 HTML 요소 전체에 걸쳐 반복되어 나타납니다.

```HTML
<style>
body { background-image: url("/examples/images/img_background_good.png"); }
</style>
```

배경 이미지를 사용할 때에는 이미지가 본문의 텍스트를 방해하지 않도록 주의를 기울여야 합니다.

```HTML
<style>
body { background-image: url("/examples/images/img_background_bad.png"); }
</style>
```

### background-repeat 속성

---

배경 이미지는 기본 설정으로 수평과 수직 방향으로 모두 반복되어 나타납니다.

background-repeat 속성을 이용하면 이러한 배경 이미지를 수평이나 수직 방향으로만 반복되도록 설정할 수 있습니다.

다음 예제는 배경 이미지의 수평 반복을 보여줍니다.

```HTML
<style>
body { background-image: url("/examples/images/img_man.png"); background-repeat: repeat-x; }
</style>
```

  

다음 예제는 배경 이미지의 수직 반복을 보여줍니다.

```HTML
<style>
body { background-image: url("/examples/images/img_man.png"); background-repeat: repeat-y; }
</style>
```

  

배경 이미지가 반복되지 않고 한 번만 나타나게 할 수도 있습니다.

```HTML
<style>
body { background-image: url("/examples/images/img_man.png"); background-repeat: no-repeat; }
</style>
```

### background-position 속성

---

background-position 속성은 반복되지 않는 배경 이미지의 상대 위치(relative position)를 설정합니다.

```HTML
<style>
body {
background-image: url("/examples/images/img_man.png");
background-repeat: no-repeat;
background-position: top right;
}
</style>
```

이 속성에서 사용할 수 있는 키워드의 조합은 다음과 같습니다.

1. left top

2. left center

3. left bottom

4. right top

5. right center

6. right bottom

7. center top

8. center center

9. center bottom

또한, 퍼센트(%)나 픽셀(px)을 사용하여 상대 위치를 직접 명시할 수도 있습니다.

이때 상대 위치를 결정하는 기준은 해당 요소의 왼쪽 상단(left top)이 됩니다.

다음 예제는 배경 이미지의 상대 위치를 픽셀 단위로 직접 명시한 예제입니다.

```HTML
<style>
body {
background-image: url("/examples/images/img_man.png");
background-repeat: no-repeat;
background-position: **100px** **200px**;
}
</style>
```

### background-attachment 속성

---

background-attachment 속성을 사용하여 위치가 설정된 배경 이미지를 해당 위치에 고정시킬 수도 있습니다.

이렇게 고정된 배경 이미지는 스크롤과는 무관하게 화면의 위치에서 이동하지 않습니다.

```HTML
<style>
body {
background-image: url("/examples/images/img_man.png");
background-repeat: no-repeat;
background-position: left bottom;
background-attachment: fixed;
}
</style>
```

### background 속성 한 번에 적용하기

---

위에서 언급한 모든 background 속성을 이용한 스타일을 한 줄에 설정할 수 있습니다.

```HTML
<style>
body { background: **\#FFCCCC** url("/examples/images/img_man.png") no-repeat left bottom fixed; }
</style>
```

### CSS background 속성

---

|속성|설명|
|---|---|
|background|모든 background 속성을 이용한 스타일을 한 줄에 설정할 수 있음.|
|background-color|HTML 요소의 배경색을 설정함.|
|background-image|HTML 요소의 배경 이미지를 설정함.|
|background-repeat|설정된 배경 이미지의 반복 유무를 설정함.|
|background-position|반복되지 않는 배경 이미지의 상대 위치를 설정함.|
|background-attachment|배경 이미지를 스크롤과는 무관하게 해당 위치에 고정시킴.|

  

## CSS 텍스트

CSS는 여러 기능을 가진 다양한 Text 속성을 제공합니다.

CSS에서 사용할 수 있는 대표적인 text 속성은 다음과 같습니다.

1. color

2. direction

3. letter-spacing

4. word-spacing

5. text-indent

6. text-align

7. text-decoration

8. text-transform

9. line-height

10. text-shadow

### color 속성

---

color 속성은 텍스트의 색상을 설정합니다.

웹 페이지에서 텍스트의 기본 색상은 검정색입니다.

<body>태그에 명시된 color 속성값은 웹 페이지 내의 모든 텍스트 요소에 적용됩니다.

하지만 각 요소별로 따로 명시된 color 속성값이 있다면, 해당 속성값이 <body>태그에 명시된 속성값보다 우선 적용됩니다.

```HTML
<style>
body { color: red; }
p { color: maroon; }
</style>
```

### direction 속성

---

direction 속성은 텍스트가 써지는 방향을 설정합니다.

웹 페이지에서 텍스트는 기본적으로 왼쪽에서 오른쪽 방향으로 써집니다.

direction 속성이 left-to-right(ltr)일 때는 기본 설정처럼 텍스트가 왼쪽에서 오른쪽 방향으로 써집니다.

하지만, direction 속성이 right-to-left(rtl)일 때는 텍스트가 반대 방향인 오른쪽에서 왼쪽 방향으로 써집니다.

다음 예제는 "객체 지향 프로그래밍"이라는 문자열을 한글과 아랍어로 각각 나타낸 예제입니다.

```HTML
<style>
.rightToLeft { direction: rtl; }
</style>
```

아랍어는 한글이나 영어와는 달리 오른쪽에서 왼쪽 방향으로 텍스트를 읽고 쓰는 언어입니다.

따라서 아랍어와 같이 텍스트를 반대 방향으로 쓰는 언어를 나타낼 때는 텍스트가 써지는 방향을 direction 속성을 사용하여 변경해 줘야 합니다.

### letter-spacing 속성

---

letter-spacing 속성은 텍스트 내에서 글자 사이의 간격을 설정합니다.

```HTML
<style>
.decLetterSpacing { letter-spacing: **-3px**; }
.incLetterSpacing { letter-spacing: **10px**; }
</style>
```

### word-spacing 속성

---

word-spacing 속성은 텍스트 내에서 단어 사이의 간격을 설정합니다.

letter-spacing 속성과는 달리 문자 간의 간격이 아닌 단어 간의 간격을 기준으로 설정합니다.

```HTML
<style>
.decWordSpacing { word-spacing: **-3px**; }
.incWordSpacing { word-spacing: **10px**; }
</style>
```

### text-indent 속성

---

text-indent 속성은 단락의 첫 줄에 들여쓰기할지 안 할지를 설정합니다.

웹 페이지에서 단락은 기본적으로 들여쓰기가 설정되어 있지 않습니다.

```HTML
<style>
.paraIndent { text-indent: **30px**; }
</style>
```

### text-align 속성

---

text-align 속성은 텍스트의 수평 방향 정렬을 설정합니다.

text-align 속성으로 설정된 정렬 방향은 text-direction 속성과는 상관없이 우선적으로 적용됩니다.

```HTML
<style>
h2 { text-align: left; }
h3 { text-align: right; }
h4 { text-align: center; }
</style>
```

### text-decoration 속성

---

text-decoration 속성은 텍스트에 여러 가지 효과를 설정하거나 제거하는데 사용합니다.

```HTML
<style>
h2 { text-decoration: overline; }
h3 { text-decoration: line-through; }
h4 { text-decoration: underline; }
a { text-decoration: none; }
</style>
```

text-decoration 속성값을 none으로 설정하여 링크(link)가 설정된 텍스트의 밑줄을 제거하는데 자주 사용합니다.

### text-transform 속성

---

text-transform 속성은 텍스트에 포함된 영문자에 대한 대소문자를 설정합니다.

이 속성은 텍스트에 포함된 모든 영문자를 대문자나 소문자로 변경시켜 줍니다.

또한, 단어의 첫 문자만을 대문자로 변경시킬 수도 있습니다.

```HTML
<style>
h2 { text-transform: uppercase; }
h3 { text-transform: lowercase; }
h4 { text-transform: capitalize; }
</style>
```

text-transform 속성은 한글에는 영향을 주지 않으며, 오직 영문자에만 적용됩니다.

### line-height 속성

---

line-height 속성은 텍스트의 줄 간격을 설정합니다.

```HTML
<style>
.narrowLineHeight { line-height: **0.8**; }
.wideLineHeight { line-height: **1.8**; }
</style>
```

### text-shadow 속성

---

text-shadow 속성은 텍스트에 간단한 그림자 효과를 설정합니다.

```HTML
<style>
h2 { text-shadow: **2px** **1px** **\#3399CC**; }
</style>
```

### CSS text 속성

---

|속성|설명|
|---|---|
|color|텍스트의 색상을 설정함.|
|direction|텍스트가 쓰이는 방향을 설정함.|
|letter-spacing|텍스트 내에서 문자 사이의 간격을 설정함.|
|word-spacing|텍스트 내에서 단어 사이의 간격을 설정함.|
|text-indent|단락의 첫 줄을 들여쓰기할지 안 할지를 설정함.|
|text-align|텍스트의 수평 방향 정렬을 설정함.|
|text-decoration|텍스트에 여러 가지 효과를 설정하거나 제거함.|
|text-transform|텍스트에 포함된 영문자에 대한 대소문자를 설정함.|
|line-height|텍스트의 줄 간격을 설정함.|
|text-shadow|텍스트에 그림자 효과를 설정함.|
|unicode-bidi|direction 속성과 같이 사용하여 텍스트의 기본 출력 방향을 설정함.|
|vertical-align|HTML 요소 내의 수직 방향 정렬을 설정함.|
|white-space|HTML 요소 내의 여백을 설정함.|

  

## CSS 글꼴

_CSS_를 사용하면 웹 페이지에 나타나는 글꼴(Font)을 다양하게 설정할 수 있습니다.

CSS에서 사용할 수 있는 font 속성은 다음과 같습니다.

1.font-family

2.font-style

3.font-variant

4.font-weight

5.font-size

### CSS 글꼴 집합(font-family)

---

CSS에는 두 가지의 글꼴 집합(font family)이 존재합니다.

- generic family : 비슷한 모양을 가지는 글꼴 집합 ("Serif", "Monospace" 등)
- font family : 특정 글꼴 집합 ("Times", "Courier" 등)

### font-family 속성

---

font-family 속성은 하나의 글꼴만을 설정할 수도 있고, 여러 개의 글꼴을 같이 설정할 수도 있습니다.

font-family 속성값이 여러 개의 글꼴로 설정되어 있으면, 웹 브라우저는 위에서부터 순서대로 글꼴을 읽어 들입니다.

만약 사용자의 컴퓨터에 첫 번째로 읽어 들인 글꼴이 없으면 다음 글꼴을 확인하게 됩니다.

이런 방식으로 계속해서 읽어 들인 글꼴이 존재하는지를 확인하여, 읽어 들인 글꼴이 사용자의 컴퓨터에 존재하면 해당 글꼴로 표시하게 됩니다.

글꼴의 이름이 한 단어 이상으로 이루어지면 반드시 따옴표를 사용하여 둘러 쌓아야 합니다.

또한, 여러 개의 글꼴을 나열할 때에는 쉼표(,)로 구분 짓습니다.

```HTML
<style>
.serif { font-family: "Times New Roman", Times, serif; }
.sansserif { font-family: Arial, Helvetica, sans-serif; }
</style>
```

### font-style 속성

---

font-style 속성은 주로 이탤릭체를 사용하기 위해 사용하며, 다음과 같이 3가지의 속성값을 가집니다.

- normal : 텍스트에 어떠한 스타일도 적용하지 않습니다.
- italic : 텍스트를 이탤릭체로 나타냅니다.
- oblique : 텍스트를 기울입니다. 이 속성값은 italic과 매우 유사하지만 지원하는 웹 브라우저가 거의 없습니다.

```HTML
<style>
.normal { font-style: normal; }
.italic { font-style: italic; }
.oblique { font-style: oblique; }
</style>
```

### font-variant 속성

---

font-variant 속성은 속성값이 small-caps로 설정되면, 텍스트에 포함된 영문자 중 모든 소문자를 작은 대문자(small-caps) 글꼴로 변경시킵니다.

이때 영문자 중 대문자는 기존 크기 그대로 출력합니다.

작은 대문자(small-caps) 글꼴이란 텍스트의 기존 대문자보다는 약간 작은 크기의 대문자를 의미합니다.

```HTML
<style>
.normal { font-variant: normal; }
.smallCaps { font-variant: small-caps; }
</style>
```

font-variant 속성은 한글에는 적용되지 않으며, 영문자에만 적용됩니다.

### font-weight 속성

---

font-weight 속성은 텍스트를 얼마나 두껍게 표현할지를 설정합니다.

사용할 수 있는 속성값에는 lighter, normal, bold, bolder 등이 있습니다.

또한, 100, 200, 300, ... , 900 등과 같이 숫자로 텍스트의 두께를 설정할 수도 있습니다.

```HTML
<style>
.normal { font-weight: normal; }
.bold { font-weight: **600**; }
.bolder { font-weight: bolder; }
</style>
```

### font-size 속성

---

font-size 속성은 텍스트의 크기를 설정합니다.

웹 디자인에서 텍스트의 크기는 매우 중요한 표현 요소입니다.

하지만 제목을 표현하기 위해서 텍스트의 크기만을 크게 해서는 안 됩니다.

이때에는 제목을 위한 HTML 요소인 <h1>태그부터 <h6>태그를 사용해야 합니다.

### font-size 속성값

---

font-size 속성값은 다음과 같이 두 가지 방식으로 표현할 수 있습니다.

1. 절대적 크기

2. 상대적 크기

절대적 크기는 텍스트의 크기를 명시된 크기 그대로 설정하고자 할 때 사용합니다.

절대적 크기로 설정된 텍스트는 모든 웹 브라우저에서 같은 크기로 표현됩니다.

상대적 크기는 텍스트를 둘러싸고 있는 HTML 요소들의 크기에 따라 텍스트의 크기도 같이 변하는 방식입니다.

또한, 사용자가 웹 브라우저를 통해 텍스트의 크기를 직접 변경할 수도 있습니다.

### font-size의 크기 단위

---

font-size 속성값에 자주 사용되는 대표적인 크기 단위는 다음과 같습니다.

백분율 단위(%)는 기본 크기를 100%로 놓고, 그에 대한 상대적인 크기를 설정합니다.

배수 단위(em)는 해당 글꼴(font)의 기본 크기를 1em으로 놓고, 그에 대한 상대적인 크기를 설정합니다.

픽셀 단위(px)는 스크린의 픽셀(pixel)을 기준으로 하는 절대적인 크기를 설정합니다.

```HTML
<style>
body { font-size: **100%**; }
\#large { font-size: **2.5em**; }
\#small { font-size: **0.7em**; }
\#fixed { font-size: **20px**; }
</style>
```

배수 단위(em)로 설정된 텍스트는 사용자가 웹 브라우저를 통해 크기를 재조정할 수 있습니다.

### CSS font 속성

---

|속성|설명|
|---|---|
|font|모든 font 속성을 이용한 스타일을 한 줄에 설정할 수 있음.|
|font-family|텍스트의 글꼴 집합(font family)을 설정함.|
|font-style|주로 이탤릭체를 사용하기 위해 사용함.|
|font-variant|텍스트에 포함된 영문자 중 소문자만을 작은 대문자(small-caps) 글꼴로 변경시킴.|
|font-weight|텍스트를 얼마나 두껍게 표현할지를 설정함.|
|font-size|텍스트의 크기를 설정함.|