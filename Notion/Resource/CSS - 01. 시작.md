---
type: HTML/CSS
archive: false
---
## **CSS 기초**

### CSS란?

---

CSS는 Cascading Style Sheets의 약자입니다.

CSS는 HTML 요소들이 각종 미디어에서 어떻게 보이는가를 정의하는 데 사용되는 스타일 시트 언어입니다.

HTML4 부터는 이러한 모든 서식 설정을 HTML 문서로부터 따로 분리하는 것이 가능해졌습니다.

오늘날 대부분의 웹 브라우저들은 모두 CSS를 지원하고 있습니다.

  

### CSS 버전

---

인터넷의 발전에 따라 CSS는 현재까지 새로운 버전이 계속해서 발표되고 있습니다.

1996년에 최초의 CSS1이 W3C 표준 권고안으로 제정됩니다.

그 이후 1998년에 CSS2가 발표되었으며, 2005년부터는 현재 사용 중인 CSS3가 개발되고 있습니다.

CSS는 현재 모듈(module)별로 개발되고 있으며, 브라우저 공급자가 지원할 모듈을 자유롭게 선택할 수 있도록 하고 있습니다.

따라서 현재 최신 버전의 CSS 표준 권고안은 CSS Level 2 Revision 1 (CSS 2.1)입니다.

최신 버전의 CSS 표준 권고안에 대한 더 자세한 정보를 원한다면, W3C 공식 사이트를 방문하여 확인할 수 있습니다.

[W3C CSS Snapshot 2017 : W3C Working Group Note, 31 January 2017 =>](https://www.w3.org/TR/CSS/)

CSS 표준 권고안의 모듈별 현재 상태에 대해 자세히 알고 싶다면, 다음 링크를 방문하여 확인할 수 있습니다.

[W3C CSS current work & how to participate =>](https://www.w3.org/Style/CSS/current-work)

  

## CSS 문법

### CSS 문법

---

[![](http://www.tcpschool.com/lectures/img_css_syntax.png)](http://www.tcpschool.com/lectures/img_css_syntax.png)

CSS의 문법은 선택자(selector)와 선언부(declaratives)로 구성됩니다.

선택자는 CSS를 적용하고자 하는 HTML 요소(element)를 가리킵니다.

선언부는 하나 이상의 선언들을 세미콜론(;)으로 구분하여 포함할 수 있으며, 중괄호({ })를 사용하여 전체를 둘러쌉니다.

각 선언은 CSS 속성명(property)과 속성값(value)을 가지며, 그 둘은 콜론(:)으로 연결됩니다.

이러한 CSS 선언(declaration)은 언제나 마지막에 세미콜론(;)으로 끝마칩니다.

  

### CSS 선택자

---

스타일을 적용할 HTML 요소를 가리키는 데 사용하는 선택자는 다음과 같습니다.

- HTML 요소 선택자
- 아이디(id) 선택자
- 클래스(class) 선택자
- 그룹(group) 선택자

  

### HTML 요소 선택자

---

CSS를 적용할 대상으로 HTML 요소의 이름을 직접 사용하여 선택할 수 있습니다.

```HTML
<style>

h2 { color: teal; text-decoration: underline; }

</style>

...

<h2>이 부분에 스타일을 적용합니다.</h2>
```

  

### 아이디(id) 선택자

---

아이디 선택자는 CSS를 적용할 대상으로 특정 요소를 선택할 때 사용합니다.

이 선택자는 웹 페이지에 포함된 여러 요소 중에서 특정 아이디 이름을 가지는 요소만을 선택해 줍니다.

```HTML
<style>

\#heading { color: teal; text-decoration: line-through; }

</style>

...

<h2 id="heading">이 부분에 스타일을 적용합니다.</h2>
```

HTML과 CSS에서는 하나의 웹 페이지에 속하는 여러 요소에 같은 아이디 이름을 사용해도 별 문제없이 동작합니다.

하지만 이렇게 중복된 아이디를 가지고 자바스크립트 작업을 하게 되면 오류가 발생합니다.

따라서 되도록이면 하나의 웹 페이지에 속하는 요소에는 다른 아이디 이름을 사용하거나 클래스를 사용하는 것이 좋습니다.

  

### 클래스(class) 선택자

---

클래스 선택자는 특정 집단의 여러 요소를 한 번에 선택할 때 사용합니다.

이러한 특정 집단을 클래스(class)라고 하며, 같은 클래스 이름을 가지는 요소들을 모두 선택해 줍니다.

```HTML
<style>

.headings { color: lime; text-decoration: overline; }

</style>

...

<h2 class="headings">이 부분에 스타일을 적용합니다.</h2>

<p>class 선택자를 이용하여 스타일을 적용할 HTML 요소들을 한 번에 선택할 수 있습니다.</p>

<h3 class="headings">이 부분에도 같은 스타일을 적용합니다.</h3>
```

  

### 그룹(group) 선택자

---

그룹 선택자는 위에서 언급한 여러 선택자를 같이 사용하고자 할 때 사용합니다.

그룹 선택자는 여러 선택자를 쉼표(,)로 구분하여 연결합니다.

이러한 그룹 선택자는 코드를 중복해서 작성하지 않도록 하여 코드를 간결하게 만들어 줍니다.

```HTML
<style>
h1 { color: navy; }
h1, h2 { text-align: center; }
h1, h2, p { background-color: lightgray; }
</style>
```

  

### CSS 주석(comments)

---

주석(comment)이란 개발자가 작성한 해당 코드에 대한 이해를 돕는 설명이나 디버깅을 위해 작성한 구문을 의미합니다.

이러한 주석은 다른 CSS 코드와는 달리 웹 브라우저에 의해 해석되지 않습니다.

CSS에서 주석을 표현하는 방법은 다음과 같습니다.

> [!important]  
> 문법/* 주석내용 */  

```HTML
<style>
p { color: teal; */*이것은 한 줄짜리 주석입니다.*/* font-size: **30px**; }
/*
이것은 두 줄짜리 주석입니다.
몇 줄이라도 가능합니다.
*/
</style>
```

  

> [!important]  
> CSS에서 주석을 작성할 때는 절대로 주석 내부에 또 다른 주석을 넣어서는 안 됩니다.  

다음 예제는 첫 번째 주석 안에 한 줄짜리 두 번째 주석을 삽입한 예제입니다.

이때 첫 번째 주석의 두 번째 라인은 두 번째 주석의 */ 기호로 인해 정상적인 주석으로 인식되지 못합니다.

```CSS
/*
첫 번째 주석의 첫 번째 라인입니다. /* 두 번째 주석입니다. */
첫 번째 주석의 두 번째 라인입니다.
*/
```

  

## CSS 적용

### CSS를 적용하는 방법

---

HTML 문서에 CSS 스타일을 적용할 때에는 다음과 같이 세 가지 방법을 사용할 수 있습니다.

1. 인라인 스타일(Inline style)

2. 내부 스타일 시트(Internal style sheet)

3. 외부 스타일 시트(External style sheet)

### 인라인 스타일(Inline style)

---

인라인 스타일이란 HTML 요소 내부에 style 속성을 사용하여 CSS 스타일을 적용하는 방법입니다.

이러한 인라인 스타일은 해당 요소에만 스타일을 적용할 수 있습니다.

```HTML
<body>
<h2 style="color:green; text-decoration:underline">
인라인 스타일을 이용하여 스타일을 적용하였습니다.
</h2>
</body>
```

> [!important]  
> 이 방식은 한 번 설정된 스타일을 변경하기가 매우 어려우며, 스타일 시트를 사용하는 많은 이점을 잃게 됩니다.따라서 이 방식은 될 수 있으면 꼭 필요한 경우에만 사용해야 합니다.  

  

### 내부 스타일 시트(Internal style sheet)

---

내부 스타일 시트를 이용하는 방법은 HTML 문서 내의 <head>태그에 <style>태그를 사용하여 CSS 스타일을 적용합니다.

이러한 내부 스타일 시트는 해당 HTML 문서에만 스타일을 적용할 수 있습니다.

```HTML
<head>
<style>
body { background-color: lightyellow; }
h2 { color: red; text-decoration: underline; }
</style>
</head>
```

  

### 외부 스타일 시트(External style sheet)

---

외부 스타일 시트를 이용하는 방법은 웹 사이트 전체의 스타일을 하나의 파일에서 변경할 수 있도록 해줍니다.

외부에 작성된 이러한 스타일 시트 파일은 .css 확장자를 사용하여 저장됩니다.

스타일을 적용할 웹 페이지의 <head>태그에 <link>태그를 사용하여 외부 스타일 시트를 포함해야만 스타일이 적용됩니다.

```HTML
<head>
<link rel="stylesheet" href="/examples/media/expand_style.css">
</head>
```

  

위의 예제에서 사용된 CSS 파일의 내용은 다음과 같습니다.

```CSS
/* expand_style.css /*
body { background-color: lightyellow; }
p { color: red; text-decoration: underline; }
```

  

### 스타일 적용의 우선순위

---

위에서 설명한 스타일 적용 방법들이 혼합되어 사용될 경우, 최종적으로 적용되는 스타일은 다음 순서에 따라 결정됩니다.

1. 인라인 스타일 (HTML 요소 내부에 위치함)

2. 내부 / 외부 스타일 시트 (HTML 문서의 head 요소 내부에 위치함)

3. 웹 브라우저 기본 스타일

예를 들어 인라인 스타일이 적용된 태그는 내부나 외부 스타일 시트와는 상관없이 무조건 인라인 스타일이 적용됩니다.

또한, 내부 스타일 시트와 외부 스타일 시트는 가장 마지막에 적용된 스타일 시트가 적용됩니다.

```HTML
<link rel="stylesheet" href="/examples/media/expand_style.css">
...
<h2>이 부분은 외부 스타일 시트만이 적용됩니다.</h2>
<h2 style="color:maroon; text-decoration:line-through"> 이 부분은 인라인 스타일과 외부 스타일 시트가 둘 다 적용됩니다. </h2>
```

  

따라서 웹 사이트의 스타일 적용은 외부 스타일 시트를 사용하는 것이 유지 보수도 편하며, 가장 안정적입니다.

하지만 우리 수업에서는 CSS 파일을 매번 보여줄 수 없으므로, 대부분의 예제에서 내부 스타일 시트를 사용할 것입니다.