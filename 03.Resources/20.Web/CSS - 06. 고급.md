---
type: HTML/CSS
archive: false
---
## 내비게이션 바

### 내비게이션 바(navigation bar)

---

사용자가 웹 사이트에서 가장 많이 클릭하는 영역 중 하나가 바로 내비게이션 바입니다.

내비게이션 바(navigation bar)는 우리가 흔히 사용하는 웹 사이트의 메뉴를 의미합니다.

HTML 요소만으로 만든 단순한 메뉴에 CSS를 이용하면, 보기에도 이쁘고 쓰기도 편리한 메뉴로 손쉽게 바꿀 수 있습니다.

### 링크를 사용한 리스트 메뉴

---

내비게이션 바 중에서도 가장 기본적인 것이 바로 링크(link)를 사용한 리스트 메뉴입니다.

HTML에서 링크는 <a>태그로 표현합니다.

다음 예제는 링크를 사용하여 구현한 간단한 메뉴 예제입니다.

```HTML
<ul>
	<li><a href="/index.php">Home</a></li>
	<li><a href="/html/intro">HTML</a></li>
	<li><a href="/css/intro">CSS</a></li>
	<li><a href="/javascript/intro">자바스크립트</a></li>
</ul>
```

### 수직 내비게이션 바

---

링크를 사용한 리스트 메뉴에 display 속성값을 block으로 설정하면, 간단히 수직 내비게이션 바를 만들 수 있습니다.

```HTML
<style> 
ul { 
	background-color: \#FFDAB9; 
	width: 150px; 
	list-style-type: none; 
	margin: 0; 
	padding: 0; 
} 
li a { 
	display: block; 
	color: \#000000; 
	padding: 8px; 
	text-decoration: none; 
	font-weight: bold; 
} 
li a:hover { background-color: \#CD853F; color: white; } 
</style>
```

위의 예제에서 인라인 요소인 <a>요소의 display 속성값을 블록(block)으로 변경하면, 메뉴의 어느 곳을 클릭하더라도 바로 연결된 페이지로 넘어가게 설정됩니다.

  

클래스(class)를 이용하면 내비게이션 바에서 현재 메뉴의 위치도 표현할 수 있습니다.

```HTML
<style>
li a.current { background-color: \#FF6347; color: white; }
li a:hover:not(.current) { background-color: \#CD853F; color: white; }
</style>
```

위의 예제에서는 :not 선택자를 이용하여 현재 메뉴를 나타내는 current 클래스와 그 외의 메뉴의 배경색을 구분하고 있습니다.

  

border 속성을 이용하면 내비게이션 바에 경계선을 표현할 수 있습니다.

```HTML
<style>
li { border-bottom: solid 1px black; }
li:last-child { border-bottom: none; }
</style>
```

### 수평 내비게이션 바

---

수평 내비게이션 바는 다음과 같은 속성을 이용해 만들 수 있습니다.

1. display 속성의 inline 속성값을 이용한 방법

2. floating 속성을 이용한 방법

### display 속성의 inline 속성값을 이용한 방법

---

링크를 사용한 리스트 메뉴에서 <li>요소의 display 속성값을 inline으로 설정합니다.

그러면 블록 요소였던 <li>요소가 인라인 요소의 성질을 갖도록 변경됩니다.

인라인 요소로 변경된 <li>요소는 너비가 자신의 내용만큼만을 차지하도록 변경됩니다.

따라서 모든 <li>요소가 수평으로 늘어서게 되며, 이것을 이용하여 수평 내비게이션 바를 만들게 됩니다.

```HTML
<style>
li { display: inline; }
</style>
```

### floating 속성을 이용한 방법

---

링크를 사용한 리스트 메뉴의 <li>요소에 float 속성을 설정합니다.

이때 float 속성값을 left로 설정하면, 모든 메뉴가 왼쪽으로 정렬됩니다.

또한, float 속성값을 right로 설정하면, 모든 메뉴가 오른쪽으로 정렬됩니다.

```HTML
<style>
li { float: left; }
li a { display: block; background-color: **\#FFDAB9**; padding: **8px**; }
</style>
```

  

CSS를 이용하면 수평 내비게이션 바에 여러 가지 스타일을 설정할 수 있습니다.

```HTML
<style> 
ul { 
	background-color: \#FFDAB9; 
	list-style-type: none; 
	margin: 0; 
	padding: 0; 
	overflow: hidden; 
} 
li { float: left; } 
li a { 
	display: block; 
	background-color: \#FFDAB9; 
	color: \#000000; 
	padding: 8px; 
	text-decoration: none; 
	text-align: center; 
	font-weight: bold; 
} 
li a:hover { background-color: \#CD853F; color: white; } 
</style>
```

  

클래스(class)를 이용하면 내비게이션 바에서 현재 메뉴의 위치도 표현할 수 있습니다.

```HTML
<style>
li a.current { background-color: \#FF6347; color: white; }
li a:hover:not(.current) { background-color: \#CD853F; color: white; }
</style>
```

위의 예제에서는 :not 선택자를 이용하여 현재 메뉴를 나타내는 current 클래스와 그 외의 메뉴의 배경색을 구분하고 있습니다.

  

<ul>요소나 <ol>요소의 float 속성값을 조절하면, 왼쪽 메뉴뿐만 아니라 오른쪽 메뉴도 같이 설정할 수 있습니다.

```HTML
<ul>
	<li><a href="/index.php">Home</a></li>
	<li><a href="/html/intro">HTML</a></li>
	<li><a class="current" href="/css/intro">CSS</a></li>
<ul style="float:right; list-style-type:none;">
	<li><a href="/bbs/login.php">로그인</a></li>
	<li><a href="/bbs/register_form.php">회원가입</a></li>
</ul>
```

위의 예제에서 Home, HTML, CSS 메뉴는 왼쪽으로 정렬되며, 로그인, 회원가입 메뉴는 오른쪽으로 정렬됩니다.

  

border 속성을 이용하면 내비게이션 바에 경계선을 표현할 수 있습니다.

```HTML
<style>
li { float: left; border-right: solid 1p* white; }
li:last-child { border-right: none; }
<style>
```

  

## 드롭다운

### 드롭다운(dropdown) 효과

---

해당 요소에 마우스를 올려서 다른 요소나 텍스트가 나타나게 하는 효과를 드롭다운(dropdown) 효과라고 합니다.

CSS를 이용하면 이러한 드롭다운 효과를 간단히 설정할 수 있습니다.

다음 예제는 display 속성을 이용하여 드롭다운 효과를 구현하는 예제입니다.

```HTML
<style>
	.dropdown { position: relative; display: inline-block; }
	.dropdown-content {
		display: none;
		position: absolute;
		background-color: \#F9F9F9;
		min-width: 160px;
		padding: 8px;
		box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
	}
	.dropdown:hover .dropdown-content { display: block; }
</style>
```

위의 예제에서 사용자가 마우스를 올리면 나타날 <div>요소의 display 속성값을 none으로 설정합니다.

이렇게 설정하면 처음에는 눈에 보이지 않게 됩니다.

하지만 특정 요소에 마우스를 올리면 해당 <div>요소의 display 속성값이 블록(block)으로 변경됩니다.

따라서 이때에는 이 <div>요소가 눈에 보이게 됩니다.

위의 예제에서 사용된 inline-block 속성값에 대한 더 자세한 사항은 CSS 디스플레이 수업에서 확인할 수 있습니다.

[CSS 디스플레이 수업 확인 =>](http://www.tcpschool.com/css/css_position_display)

### 드롭다운(Dropdown) 메뉴

---

메뉴에 마우스를 올리면 하위 메뉴가 나타나게 하는 메뉴를 드롭다운(dropdown) 메뉴라고 합니다.

드롭다운 효과를 이용하면 이러한 드롭다운 메뉴도 간단히 구현할 수 있습니다.

```HTML
<style> 
.dropdown-button { background-color: \#FFDAB9; padding: 8px; font-size: 15px; border: none; } 
.dropdown { position: relative; display: inline-block; } 
.dropdown-content { display: none; position: absolute; background-color: \#FFDAB9; min-width: 70px; padding: 8px; box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2); } 
.dropdown-content a { color: black; padding: 8px; text-decoration: none; display: block; } 
.dropdown-content a:hover { background-color: \#CD853F; } 
.dropdown:hover .dropdown-content { display: block; } 
.dropdown:hover .dropdown-button { background-color: \#CD853F; } 
</style>
```

  

## 툴팁

### 툴팁(tooltip) 효과

---

해당 요소에 마우스를 올리면 추가적인 정보가 나타나게 하는 효과를 툴팁(tooltip) 효과라고 합니다.

CSS를 이용하면 이러한 툴팁 효과를 간단히 설정할 수 있습니다.

다음 예제는 visiblility 속성을 이용하여 툴팁 효과를 구현하는 예제입니다.

```HTML
<style> 
.tooltip { position: relative; display: inline-block; } 
.tooltip .tooltip-content { 
	visibility: hidden; 
	width: 300px; 
	background-color: orange; 
	padding: 0; 
	margin-top: 10px; 
	color: white; 
	text-align: center; 
	position: absolute; 
	z-index: 1; 
} 
.tooltip:hover .tooltip-content { visibility: visible; } 
</style>
```

CSS를 이용하면 툴팁(tooltip)이 나타나는 위치도 간단히 설정할 수 있습니다.

CSS의 상대적 위치를 나타내는 top, right, bottom, left 속성을 이용하여 툴팁의 상대 위치를 설정할 수 있습니다.

  

다음 예제는 툴팁이 해당 요소의 아래 쪽이 아닌 왼쪽에 나타나도록 구현한 예제입니다.

```HTML
<style>
.tooltip { margin: auto; }
.tooltip .tooltip-content { top: -15px; right: 105%; }
</style>
```

  

다음 예제는 해당 요소에 마우스를 올리면 툴팁이 위쪽에 나타나도록 구현한 예제입니다.

```HTML
<style>
.tooltip { margin: auto; }
.tooltip .tooltip-content { bottom: 100%; left: 50%; margin-left: -150px; }
</style>
```

  

또한, 다음 예제처럼 툴팁(tooltip)의 모양을 말풍선 모양처럼 설정할 수도 있습니다.

```HTML
<style>
.tooltip .tooltip-content::after {
	content: " ";
	position: absolute;
	top: 100%;
	left: 50%;
	margin-left: -10px;
	border-width: 10px;
	border-style: solid;
	border-color: orange transparent transparent transparent;
}
</style>
```

위의 예제에서 툴팁의 말풍선 모양은 border-color 속성값을 transparent로 설정하여 구현할 수 있습니다.

transparent 속성값은 투명함을 의미합니다.

  

## Form 요소

### form 요소

---

CSS를 이용하면 사용자의 입력을 받는 input 요소에도 다양한 스타일을 설정할 수 있습니다.

### input 요소의 크기 설정

---

width 속성을 이용하여 input 요소의 크기를 설정할 수 있습니다.

```HTML
<style> 
input { width: 100%; padding: 10px 20px; margin: 5px 0; box-sizing: border-box; } 
</style>
```

위의 예제에서 사용된 box-sizing 속성에 대한 더 자세한 사항은 CSS 사용자 인터페이스 수업에서 확인할 수 있습니다.

[CSS 사용자 인터페이스 수업 확인 =>](http://www.tcpschool.com/css/css3_expand_ui)

### input 요소의 테두리 설정

---

border 속성을 이용하여 input 요소의 테두리(border) 색상과 두께를 바꿀 수 있습니다.

또한, border-radius 속성을 이용하여 input 요소의 모서리를 둥글게 만들 수도 있습니다.

```HTML
<style> 
input[type="text"] { 
	border: solid 2px \#D2691E; border-radius: 8px; 
} 
input[type="password"] { border: none; border-bottom: solid 2px \#D2691E; } 
</style>
```

### input 요소에 배경색 적용

---

background-color 속성을 이용하여 input 요소의 배경색을 설정할 수 있습니다.

또한, color 속성을 이용하여 input 요소의 텍스트 색상를 변경할 수도 있습니다.

```HTML
<style>
input { background-color: \#FFF8DC; color: olive; }
</style>
```

### 포커스를 가지고 있는 input 요소의 스타일 적용

---

:focus 선택자를 이용하여 해당 input 요소가 포커스(focus)를 가지고 있을 때의 스타일을 별도로 설정할 수 있습니다.

```HTML
<style> 
input[type="text"] { 
	border: solid 2px \#FFE4B5; 
	-webkit-transition: 0.5s; 
	transition: 0.5s; 
} 
input[type="text"]:focus { 
	border: solid 2px \#D2691E; 
} 
input[type="password"] { border: solid 1px black; } 
input[type="password"]:focus { background-color: \#E0FFFF; } 
</style>
```

### input 요소에 아이콘(icon)이나 이미지 삽입

---

background-image 속성을 이용하여 input 요소에 아이콘(icon)이나 이미지를 삽입할 수 있습니다.

또한, background-position 속성을 이용하여 삽입한 아이콘이나 이미지가 나타날 위치를 설정할 수도 있습니다.

```HTML
<style>
input {
	background-image: url("/examples/images/img_search_icon.png");
	background-position: 5px 4px;
	background-repeat: no-repeat;
}
</style>
```

### textarea 요소의 크기 조절

---

resize 속성을 이용하여 textarea 요소의 크기를 조절할 수 있습니다.

resize 속성을 설정하면 해당 textarea 요소의 오른쪽 아래 부분에 마우스로 잡을 수 있는 핸들이 생깁니다.

사용자가 그 핸들을 마우스로 클릭하여 조절하면 textarea 요소의 크기를 마음대로 조절할 수 있게 됩니다.

CSS에서 사용할 수 있는 resize 속성값은 다음과 같습니다.

|속성|설명|
|---|---|
|none|해당 요소의 크기를 조절할 수 없음. (기본 설정)|
|both|사용자가 해당 요소의 높이와 너비를 모두 조절할 수 있음.|
|horizontal|사용자가 해당 요소의 너비만을 조절할 수 있음.|
|vertical|사용자가 해당 요소의 높이만을 조절할 수 있음.|

```HTML
<style>
textarea { width: 100%; height: 200px; box-sizing: border-box; resize: both; }
</style>
```

resize 속성은 익스플로러에서 지원하지 않습니다.

### select 요소에 스타일 적용

---

CSS를 이용하면 select 요소에도 여러 가지 스타일을 적용할 수 있습니다.

```HTML
<style> 
select { 
	width: 100%; 
	padding: 10px; 
	border: solid 1px black; 
	border-radius: 5px; 
	background-color: \#FFFFE0; 
} 
</style>
```

  

## @규칙

### @규칙(at-rule)

---

CSS에서는 W3C에서 규정하고 있는 몇몇 규칙들을 사용할 수 있습니다.

그 중에서도 많이 사용되는 대표적인 규칙은 다음과 같습니다.

1. @import

2. @font-face

3. @media

### @import 규칙

---

@import 규칙은 다른 스타일 시트에서 스타일 규칙을 가져올 수 있는 규칙입니다.

이 규칙은 스타일 시트에 사용되는 문자 인코딩을 지정하는 @charset 규칙을 제외하고 모든 다른 규칙보다 앞서 명시되어야 합니다.

보통 HTML 문서에는 다음과 같이 여러 개의 <link>태그를 사용하여 스타일 시트를 추가합니다.

```HTML
### HTML 문서
<head>
	<title>@import 규칙</title>
	<link rel="stylesheet" href="firstStyleSheet.css">
	<link rel="stylesheet" href="secondStyleSheet.css">
	...
	<link rel="stylesheet" href="hundredStyleSheet.css">
</head>
```

  

하지만 이렇게 추가하는 CSS 파일의 개수가 늘어날수록 웹 서버의 부하도 같이 커지게 됩니다.

따라서 HTML 문서에는 일정 개수의 CSS 파일만을 추가하고, 추가된 CSS 파일에서 @import 규칙을 이용해 또 다른 CSS 파일을 추가하는 방법을 사용합니다.

```HTML
### HTML 문서
<head>
	<title>@import 규칙</title>
	<link rel="stylesheet" href="firstStyleSheet.css">
	<link rel="stylesheet" href="secondStyleSheet.css">
</head>
```

```HTML
### firstStyleSheet.css
@import url("thirdStyleSheet.css");
@import "fourthStyleSheet.css";
...
```

  

@import 규칙을 사용해도 추가하는 CSS 파일의 개수가 늘어나면 여전히 웹 서버의 부하는 커질 수밖에 없습니다.

따라서 웹 서버의 부하를 줄이기 위해 작성한 CSS 파일들을 적절히 분산해서 추가하는 방법이 필요해집니다.

@import 규칙을 이용하면 미디어 쿼리(media query)의 조건에 따라 필요한 CSS 파일만을 선별적으로 불러올 수 있습니다.

다음 예제는 프린트할 때에는 firstStyleSheet.css 파일을 불러오고, 스크린이 가로 방향으로 설정되어 있을 때는 secondStyleSheet.css 파일을 불러오는 예제입니다.

```HTML
<head>
	<title>@import 규칙</title>
	@import url("firstStyleSheet.css") print;
	@import "secondStyleSheet.css" screen and (orientation:landscape);
</head>
```

  

### @font-face 규칙

---

@font-face 규칙은 웹 폰트(web font)를 정의할 때 사용하는 규칙입니다.

웹 폰트(web font)는 사용자의 컴퓨터에 설치되어 있지 않은 글꼴(font)을 웹 브라우저가 사용할 수 있게 해줍니다.

우선 웹 폰트를 서버에 올려놓고, CSS 파일에 @font-face 규칙을 사용하여 웹 폰트를 정의하고 추가합니다.

그러면 해당 웹 페이지에 접속하는 모든 웹 브라우저는 자동으로 서버에서 웹 폰트를 내려받아 해당 글꼴을 표시하게 됩니다.

```HTML
<style>
	@font-face {
		font-family: "myWebFont";
		src: local("NanumGothic"), url("NanumGothic.eot"), url("NanumGothic.ttf"), url("NanumGothic.woff");
	}
	* { font-family: "myWebFont"; }
</style>
```

  

@font-face 규칙에 대한 더 자세한 사항은 CSS3 웹 글꼴 수업에서 확인할 수 있습니다.

[CSS3 웹 글꼴 수업 확인 =>](http://www.tcpschool.com/css/css3_module_webfonts)

### @media 규칙

---

CSS2에서는 @media 규칙을 통해 서로 다른 미디어 타입(media type)을 위한 맞춤식 스타일 시트를 지원합니다.

다음 예제는 HTML 문서가 스크린에 표현될 때와 프린트할 때 서로 다른 스타일을 적용해 주는 예제입니다.

```HTML
<style>
	body { background-color: darkorange; }
	@media screen {
		body { background-color: black; color: white; }
	}
	@media print {
		body { background-color: white; color: black; }
	}
</style>
```

  

미디어 쿼리(media query)에 대한 더 자세한 사항은 CSS 미디어 쿼리 수업에서 확인할 수 있습니다.

[CSS 미디어 쿼리 수업 확인 =>](http://www.tcpschool.com/css/css3_expand_mq)