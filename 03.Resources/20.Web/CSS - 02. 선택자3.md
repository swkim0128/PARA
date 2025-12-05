---
type: HTML/CSS
archive: false
---
## 의사 요소

### 의사 요소(pseudo-element)

---

의사 요소(pseudo-element)는 해당 HTML 요소의 특정 부분만을 선택할 때 사용합니다.

### 의사 요소의 문법

---

의사 요소(pseudo-element)를 사용하기 위한 문법은 다음과 같습니다.

> [!important]  
> 문법선택자::의사요소이름 {속성: 속성값;}  
  
> [!important]  
> CSS1과 CSS2에서는 의사 클래스와 의사 요소를 나타낼 때 하나의 콜론(:)으로 함께 표기하였습니다.하지만 CSS3에서는 의사 클래스의 표현과 의사 요소의 표현을 구분하기로 합니다.따라서 CSS3에서는 의사 클래스는 하나의 콜론(:)을, 의사 요소에는 두 개의 콜론(::)을 사용하고 있습니다.  

  

### 대표적인 CSS 의사 요소

---

CSS에서 자주 사용하는 대표적인 의사 요소는 다음과 같습니다.

- ::first-letter::first-line::before::after::selection

### ::first-letter

---

이 의사 요소(pseudo-element)는 텍스트의 첫 글자만을 선택합니다.

단, 블록(block) 타입의 요소에만 사용할 수 있습니다.

이 의사 요소를 통해 사용할 수 있는 속성은 다음과 같습니다.

- font 속성color 속성 background 속성margin 속성padding 속성border 속성text-decoration 속성text-transform 속성line-height 속성float 속성clear 속성vertical-align 속성 (단, float 속성값이 none일 경우에만)

```HTML
<style>
p::first-letter { color: \#FF4500; font-size: 2em; }
</style>
```

### ::first-line

---

이 의사 요소는 텍스트의 첫 라인만을 선택합니다.

단, 블록(block) 타입의 요소에만 사용할 수 있습니다.

이 의사 요소를 통해 사용할 수 있는 속성은 다음과 같습니다.

- font 속성color 속성 background 속성
- word-spacing 속성letter-spacing 속성text-decoration 속성text-transform 속성line-height 속성clear 속성vertical-align 속성

```HTML
<style>
p::first-line { color: \#FF4500; font-size: 2em; }
</style>
```

### ::before

---

이 의사 요소는 특정 요소의 내용(content) 부분 바로 앞에 다른 요소를 삽입할 때 사용합니다.

```HTML
<style>
p::before { content: url("/examples/images/img_penguin.png"); }
</style>
```

### ::after

---

이 의사 요소는 특정 요소의 내용(content) 부분 바로 뒤에 다른 요소를 삽입할 때 사용합니다.

```HTML
<style>
p::after { content: url("/examples/images/img_penguin.png"); }
</style>
```

### ::selection

---

이 의사 요소는 해당 요소에서 사용자가 선택한 부분만을 선택할 때 사용합니다.

```HTML
<style>
p::selection { color: \#FF4500; }
</style>
```

### 의사 요소의 동시 적용

---

하나의 HTML 요소에 여러 개의 의사 요소를 동시에 적용할 수 있습니다.

```HTML
<style>
p::first-letter { color: \#FFD700; font-size: 2em; font-weight: bold; }
p::first-line { color: \#FF4500; }
</style>
```

### CSS 의사 요소(pseudo-elements)

---

|속성|설명|
|---|---|
|::first-letter|텍스트의 첫 글자만을 선택함.|
|::first-line|텍스트의 첫 라인만을 선택함.|
|::before|특정 요소의 내용(content) 부분 바로 앞에 다른 요소를 삽입할 때 사용함.|
|::after|특정 요소의 내용(content) 부분 바로 뒤에 다른 요소를 삽입할 때 사용함.|
|::selection|해당 요소에서 사용자가 선택한 부분만 선택함.|

  

## 속성 선택자

### 속성 선택자(attribute selectors)

---

속성 선택자를 사용하면 특정 속성이나 특정 속성값을 가지고 있는 HTML 요소를 선택할 수 있습니다.

### 기본 속성 선택자

---

CSS에서 사용할 수 있는 기본 속성 선택자는 다음과 같습니다.

- [속성이름] 선택자
- [속성이름="속성값"] 선택자

### [속성이름] 선택자

---

> [!important]  
> 문법[속성이름]  

[속성이름] 선택자는 특정 속성을 가지고 있는 요소를 모두 선택합니다.

```HTML
<style>
[title] { background: black; color: yellow; }
</style>
```

### [속성이름="속성값"] 선택자

---

> [!important]  
> 문법[속성이름="속성값"]  

[속성이름="속성값"] 선택자는 특정 속성을 가지고 있으며, 해당 속성의 속성값까지 일치하는 요소를 모두 선택합니다.

```HTML
<style>
[title="first h2"] { background: black; color: yellow; }
</style>
```

### 문자열 속성 선택자

---

CSS에서는 기본 속성 선택자 이외에도 문자열 속성 선택자를 제공합니다.

문자열 속성 선택자는 HTML 요소가 가지고 있는 특정 속성의 속성값 내에 특정 문자열을 확인하여 선택해 줍니다.

CSS에서 사용할 수 있는 문자열 속성 선택자는 다음과 같습니다.

- [속성이름~="속성값"] 선택자
- [속성이름|="속성값"] 선택자
- [속성이름^="속성값"] 선택자
- [속성이름$="속성값"] 선택자
- [속성이름*="속성값"] 선택자

> [!important]  
> 익스플로러 8과 그 이전 버전에서는 HTML 문서에 <!DOCTYPE html>태그가 삽입되어 있어야만 문자열 속성 선택자를 제대로 인식합니다.  

### [속성이름~="속성값"] 선택자

---

> [!important]  
> 문법[속성이름~="속성값"]  

[속성이름~="속성값"] 선택자는 특정 속성의 속성값에 특정 문자열로 이루어진 하나의 단어를 포함하는 요소를 모두 선택합니다.

```HTML
<style>
[title~="first"] { background: black; color: yellow; }
</style>
```

위의 예제에서는 title 속성값이 "first h2"인 요소와 "first p"인 요소만 선택됩니다.

title 속성값이 "first-p"인 요소는 선택되지 않습니다.

이처럼 [속성이름~="속성값"] 선택자는 title 속성값이 정확히 "first"인 요소나 띄어쓰기(whitespace)를 기준으로 인식되는 단어에 "first"를 포함한 요소만을 선택합니다.

[속성이름~="속성값"] 선택자는 띄어쓰기(whitespace)를 기준으로 단어를 인식합니다.따라서 예제처럼 하이픈(-)으로 연결된 단어는 전부 하나의 단어로 인식하며, 각각 별도의 단어로 인식하지 않습니다.

### [속성이름|="속성값"] 선택자

---

> [!important]  
> 문법[속성이름|="속성값"]  

[속성이름|="속성값"] 선택자는 특정 속성의 속성값이 특정 문자열로 이루어진 하나의 단어로 시작하는 요소를 모두 선택합니다.

```HTML
<style>
[title|="first"] { background: black; color: yellow; }
</style>
```

위의 예제에서는 title 속성값이 "first-p"인 요소만 선택됩니다.

title 속성값이 "first h2"나 "first p"인 요소들은 선택되지 않습니다.

이처럼 [속성이름|="속성값"] 선택자는 title 속성값이 정확히 "first"인 요소나 "first" 바로 다음에 하이픈(-)으로 시작하는 요소만을 선택합니다.

### [속성이름^="속성값"] 선택자

---

> [!important]  
> 문법[속성이름^="속성값"]  

[속성이름^="속성값"] 선택자는 특정 속성의 속성값이 특정 문자열로 시작하는 요소를 모두 선택합니다.

```HTML
<style>
[title^="first"] { background: black; color: yellow; }
</style>
```

이 선택자는 [속성이름|="속성값"] 선택자와는 달리 속성값이 특정 문자열로 시작하면 모두 선택해 줍니다.

따라서 위의 예제에서는 title 속성값이 "first"로 시작되는 요소가 모두 선택됩니다.

### [속성이름$="속성값"] 선택자

---

> [!important]  
> 문법[속성이름$="속성값"]  

[속성이름$="속성값"] 선택자는 특정 속성의 속성값이 특정 문자열로 끝나는 요소를 모두 선택합니다.

```HTML
<style>
[title$="first"] { background: black; color: yellow; }
</style>
```

이 선택자는 특정 속성의 속성값이 특정 문자열로 끝나기만 하면 모두 선택해 줍니다.

따라서 위의 예제에서는 title 속성값이 "first"로 끝나는 요소가 모두 선택됩니다.

### [속성이름*="속성값"] 선택자

---

> [!important]  
> 문법[속성이름*="속성값"]  

[속성이름*="속성값"] 선택자는 특정 속성의 속성값에 특정 문자열를 포함하는 요소를 모두 선택합니다.

```HTML
<style>
[title*="first"] { background: black; color: yellow; }
</style>
```

이 선택자는 특정 속성의 속성값이 특정 문자열를 포함하기만 하면 모두 선택해 줍니다.

따라서 위의 예제에서는 title 속성값에 "first"를 포함하는 요소가 모두 선택됩니다.

### 속성 선택자의 활용

---

위에서 설명한 속성 선택자들을 활용하면 클래스나 아이디의 지정 없이도 스타일을 적용할 HTML 요소를 손쉽게 선택할 수  있습니다.

```HTML
<style> 
input[type="text"] { width: 150px; display: block; background-color: \#FFEFD5; margin-bottom: 10px; } 
input[type="password"] { width: 130px; display: block; background-color: \#90EE90; border: solid 2px red; } 
input[type="password"]:focus { background-color: \#FFC0CB; } 
</style>
```

  

## 기타 의사 클래스

### :not

---

:not 선택자는 모든 선택자와 함께 사용할 수 있으며, 해당 선택자를 반대로 적용하여 선택합니다.

```HTML
<style>
input { color: \#FFEFD5; }
input:not([type="password"]) { background-color: \#CD853F; }
</style>
```

### :lang

---

:lang 선택자는 특정 HTML 요소를 사용자 컴퓨터의 언어 설정에 따라 다르게 표현할 때 사용합니다.

예를 들면, 영어에서는 인용의 표현으로 따옴표("")를 사용하나, 프랑스어에서는 부등호(<>)를 사용합니다.

이렇게 언어에 따라 달라지는 태그의 모양을 사용자 컴퓨터의 언어 설정에 따라 다르게 표현할 수 있게 해줍니다.

```HTML
<style>
:lang(en) { quotes: '"' '"'  "'"  "'"; }
:lang(fr) { quotes: "<<" ">>" "<" ">"; }
</style>
```