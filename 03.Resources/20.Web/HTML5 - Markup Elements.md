---
type: HTML/CSS
archive: false
---
### 포맷팅 요소

---

포맷팅 요소에는 화면에는 동일하게 출려되지만 각 요소가 가진 의미가 다른 것이 있다.

예를 들면, <b>와 <strong>은 모두 텍스트를 굵게 표현하지만, <strong>요소는 텍스트를 강조.

tag명

<abbr>

<address>

<blockquote>

<q>

<cite>

<pre>

<code>

<mark>

<hr>

<b>, <strong>

<i>, <em>

<big>, <small>

<sup>, <sub>

<s>, <u>

설명

생략된 약어 표시, Title 속성을 함께 사용

연락처 정보 표시

긴 인용문구 표시, 좌우로 들여쓰기가 됨.

짧은 이용문구 표시, 좌우로 따옴표가 붙음.

웹 문서나 포스트에서 참고 내용 표시

공백, 줄바꿈등 입력된 그래도 화면에 표시

컴퓨터 인식을 위한 소스 코드

특정 문자열을 강조, 화면에는 하이라이팅 됨.

구분선.

굵은 글씨로 표시, 특정 문자열을 강조(<strong>).

이탤릭(기울게) 표시, 특정 문자열을 강조(<em>)

큰 글자, 작은 글자로 표시

위 첨자, 아래 첨자로 표시.

취소선, 밑줄

  

### 목록형 요소

---

목록 tag는 하나 이상의 하위 tag를 포함

목록 tag는 각 항목을 들여쓰기로 표현.

번호 또는 심볼을 이용해서 목록을 표현.

tag명

<ul>  
  

<ol>  
  

<li>  
  

<dl>  
  

<dt>

<dd>

설명

번호 없는 목록을 표시. 항목 앞에 심볼을 표시.

번호 있는 목록을 표시. 숫자, 알파벳, 로마숫자 등으로 표시.

목록 항목 <ul>이나 <ol>tag 하위에서 사용.

용어 정의와 설명에 대한 내용을 목록화해서 표시.

용어 목록의 정의 부분을 나타냄.

용어 목록의 설명 부분을 나타냄.

속성

  
  
type  
  
  

start

reversed

속성값

1  
a  
A  
i  
l  

숫자

  

설명

숫자(기본값)  
영문 소문자  
영문 대문자  
로마숫자 소문자  
로마숫자 대문자  

시작 번호

역순으로 표시

  

### table

---

HTML table 모델

HTML table 모델은 데이터를 행(Row)과 열(Column)의 셀(Cell)에 표시.

행 그룹요소인 <thead>, <tbody>, <tfoot> 요소를 사용하여 행들을 그룹화.

<colgroup>과 <col> 요소는 열 그룹을 위한 추가적인 구조정보를 제공.

table의 셀(Cell)은 머리글(<th>)이나 데이터(<td>)를 가질 수 있음.

  

table 스타일

<table>, <tr>, <td> tag에는 table에 스타일을 적용하는 다양한 속성들이 있다.

frame 속성은 table의 특정 선을 보여줄지를 결정하며, rules 속성은 셀과 셀사이의 줄이 나타날 것인가를 지정.

table 정렬을 위한 align 속성, background, bgcolor, border 속성 등이 있음.

HTML5부터는 이러한 속성들을 더 이상 지원하지 않는다. 스타일은 CSS를 사용하여 적용.

  

table 제목

<caption> tag는 table 제목을 정의하기 위해 사용하며 <table> start tag 바로 뒤에 위치.

<caption> tag는 table 당 하나만 사용.

table 제목은 기본적으로 가운데 정렬, 정렬 방식 변경은 CSS를 사용.

  

행(Row) 그룹 요소

table 행 그룹 요소는 table의 행들을 머리글, 바닥글, 하나 이상의 본체 항목으로 그룹핑.

행 그룹 요소에는 머리글 (<thead>), 본체항목(<tbody>), 바닥글(<tfoot>) 요소가 있다.

각 행 그룹은 최소 하나 이상의 <tr>을 가져야 함.

  

열(Column) 그룹 요소

table열 그룹 요소는 table 내에서 구조적인 분를 가능케함.

<colgroup> 요소는 명시적인 열 그룹을 만들며, <col> 요소는 열(column)을 묶어 그룹핑 함.

<colgroup> 요소의 span 속성은 열 그룹에서 열의 개수를 정의.

<col> 요소의 span 속성은 <col>에 의해 묶여진 열의 개수를 말함.

  

테두리(border)

cellspacing은 table Cell과 Cell 사이의 공간을 의미.

cellpadding은 Cell 외곽과 Cell 컨텐츠 사이 공간을 의미.

HTML5 부터는 테두리 스타일 관련 속성을 지원하지 않고, CSS를 사용.

  

셀 병합

HTML table의 <td> 요소에는 셀(Cell)을 병합하기 위한 두 개의 속성이 있음.

colspan속성은 두 개 이상의 열(Column)을 하나로 합치기 위해 사용.

rowspan 속성은 두 개 이상의 행(Row)을 하나로 합치기 위해 사용.

  

### 이미지 요소

---

<img> tag를 사용하며 이미지를 삽입하기 위해 사용.

src 속성은 이미지 경로를 지정하기 위해 사용 (상대경로, URL 모두 가능).

height, width 속성은 이미지 사이즈를 지정하기 위해 사용.

alt 속성은 이미지를 표시할 수 없을 때 화면에 대신하여 보여질 텍스트를 지정.

  

<figure>는 설명 글을 붙여야 할 대상을 지정.

<figcpation> : 설명글이 필요한 대상은 <figure> 태그로 묶고 설명 글은 <figcpation> 태그로 묶는다.

설명 글을 붙일 수 있는 대상은 이미지나 오디오, 비디오 같은 미디어파일이나 텍스트 단락이나 표.

```HTML
<img src="이미지 파일의 URL"
			alt="문자열"
			width="이미지 폭"
			height="이미지 높이">
```

### 링크 요소

---

Anchor

<a> tag를 사용하며, 하나의 문서에서 다른 문서로 연결하기 위해 (하이퍼링크) 사용.

tag를 서로 중첩해서 사용할 수 없다.

href 속성은 하이퍼링크를 클릭했을 때 이동할 문서의 URL이나 문서의 책갈피를 지정.

  

target

속성 값

_blank

_self

_parent

_top

설명

링크 내용이 새 창이나 새탭에서 열린다.

target 속성의 기본 값으로 링크가 있는 화면에서 열린다.

프레임을 사용했을 때 링크 내용을 부모 프레임에 표시.

프레임을 사용했을 때 프레임에서 벗어나 링크 내용을 전체 화면에 표시.

  

\#anchor

같은 페이지 안에서 특정 요소를 클릭 시 그 위치로 한 번에 이동시킨다.

<tag id="anchor name"> text or image </tag>

<a href="\#anchor name">text or image</a>

  

map

하나의 이미지에 여러 개의 link(Click 위치에 따라 서로 다른 link).

<map name="map name"><area></area>...</map>

이미지에 영역을 표시 할 때 <area> 사용.

area의 속성은 href(링크 경로), target(링크 표시 대상), shape(링크로 사용할 영역의 형태) 등.

shape의 값으로는 default, rect, circle, poly가 있다.

  

link

link tag를 사용하며 문서와 외부 자원을 연결하기 위해 사용.

<head> 위치에 정의하며 여러 자원을 연결할 수 있다.

rel 속성은 현재 문서와 연결된 문서 사이의 연관관계를 지정하기 위해 사용.

href 속성은 연결된 문서의 위치를 지정하기 위해 사용.

  

```HTML
<a href="URL"|"URL#앵커이름"|"#앵커이름"
		target="윈도우이름"
		download>
텍스트 혹은 이미지
</a>
```

```HTML
<a href="picturepage.html">...</a>
<a href="https://www.naver.com">...</a>
```

```HTML
<p id="chap1">...</p>
<a href="\#chap1">...</a>

<a href="student.html\#chap1">...</a>
```

```HTML
<a href="Elvis.png" download>...</a>
```

### 프레임 요소 - iframe

---

화면의 일부분에 다른 문서를 포함.

src 속성은 포함시킬 외부 문서의 경로를 지정(상대경로, URL 모두 가능)

height, width 속성은 프레임 사이즈를 지정.

name 속성은 프레임의 이름을 지정.

  

### <audio>, <video>

---

플러그인 없이 오디오나 비디오를 재생할 수 있도록 표준화

물론 플래시 애니메이션과 같이 표준화되지 않은 미디어를 재생하기 위해서는 플러그인의 설치가 필요하며, 이런 경우 다음 두 태그를 사용한다.

> <embed>, <object>

- src - 음악 파일의 경로 지정, preload - 음악을 재생하기 전에 모두 불러올지 지정
- autoplay - 음악을 자동 재생할지 지정, loop - 음악을 반복할지 지정, controls - 음악 재생 도구를 출력할지 지정

### <video>

---

```HTML
<video src="URL"
			width=""
			height=""
			controls
			autoplay
			muted
			loop>
```

  

### <audio>

---

```HTML
<audio src="URL"
			controls
			autoplay
			loop>
```