---
type: JavaScript
archive: false
---
### DOM 개요

---

DOM(Document Object Model)은 HTML과 XML문서의 구조를 정의하는 API를 제공.

DOM은 문서 요소 집합을 트리 형태의 계층 구조로 HTML을 표현.

HTML 계층 구조의 제일 위에는 document 노드가 있다.

그 아래로 HTML 태그나 요소(element)들을 표현하는 노드와 문자열을 표현하는 노드가 있다.

  

**문서 계층 구조**

Document는 HTML 또는 XML 문서를 표현

HTMLDocument는 HTML 문서와 요소만을 표현.

HTMLElement의 하위 타입은 HTML 단일 요소나 요소 집합의 속성에 해당하는 JavaScript 프로퍼티를 정의.

Comment 노드는 HTML이나 XML의 주석을 표현

![[Untitled 38.png|Untitled 38.png]]

### 문서 객체 만들기

---

문서 객체는 text node를 갖는 객체와 갖지 않는 객체로 나뉨.

함수명

createElement(tagName)

createTextNode(text)

appendChild(node)

설명

element node를 생성.

text node를 생성.

객체에 node를 child로 추가.

![[Untitled 1 16.png|Untitled 1 16.png]]

  

객체의 속성 설정.

함수명

setAttribute(name, value)

getAttribute(name)

설명

객체의 속성을 지정.

객체의 속성값을 가져옴.

![[Untitled 2 15.png|Untitled 2 15.png]]

  

innerHTML & innerText.

속성

innerHTML

innerText

설명

문자열을 HTML태그로 삽입.

문자열을 text node로 삽입.

  

### 문서 객체 가져오기

---

객체 가져오기.

함수명

getElementById(id)

getElementsByClassName(classname)  
  

getElementsByTagName(tagname)

getElementsByName(name)  
  

querySelector(selector)

querySelectorAll(selector)

설명

태그의 id 속성이 id와 일치하는 element 객체 얻기.

태그의 class 속성이 classname과 일치하는 element 배열 얻기

태그 이름이 tagname과 일치하는 element 배열 얻기

태그의 name 속성이 anem과 일치하는 element 배열 얻기

selector에 일치하는 첫번째 element 객체 얻기.

selector에 일치하는 모든 element 배열 얻기.

  

```HTML
	<script type="text/javascript">
		window.onload = function () {
			var msg = document.getElementById('header');
			msg.innerHTML = '안녕 싸피!!!</h2>';

			var ssafy = document.getElementsByClassName('ssafy');
			var ssafy = document.getElementsByTagName('h2');

			var msg = document.querySelector('\#header');
			var ssafy = document.querySelectorAll('.ssafy');
		};
	</script>
</head>
<body>
	<h2 id='header'>Hello SSAFY!!</h2>
</body>
```

  

### 문서 객체 제거

---

객체 제거

속성

removeChild(childnode)

설명

객체의 자식 노드를 제거.

```HTML
	<script type="text/javascript">
		window.onload = function () {
			var ssafy6 = document.querySelector('\#ssafy6');

			document.body.removeChild(ssafy6);
		};
	</script>
</head>
<body>
	<h2 id='ssafy3'>Hello SSAFY!!</h2>
	<h2 id='ssafy4'>Hello SSAFY!!</h2>
	<h2 id='ssafy5'>Hello SSAFY!!</h2>
	<h2 id='ssafy6'>Hello SSAFY!!</h2>
</body>
```

  

### 요약

---

DOM은 HTML 문서의 내용을 조작할 수 있는 API로 HTML을 계층구조 형식의 객체로 표현.

DOM으로 HTML 문서의 검색과 조작(추가, 수정, 삭제)을 할 수 있다.

![[Untitled 3 14.png|Untitled 3 14.png]]