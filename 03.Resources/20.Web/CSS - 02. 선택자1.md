---
type: HTML/CSS
archive: false
---
## 선택자

### 선택자(selector)

---

CSS에서는 스타일을 적용할 대상을 선택하기 위해서 선택자(selector)를 사용합니다.

지금까지 살펴본 대표적인 선택자는 다음과 같습니다.

- 전체 선택자
- HTML 요소 선택자
- 아이디(id) 선택자
- 클래스(class) 선택자
- 그룹(group) 선택자

### 전체 선택자

---

CSS를 적용할 대상으로 HTML 문서 내부의 모든 요소를 선택합니다.

```HTML
<style>
{ color: red; }
</style>
```

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
\#heading { color: sandybrown; text-decoration: line-through; }
</style>
...
<h2 id="heading">이 부분에 스타일을 적용합니다.</h2>
```

HTML과 CSS에서는 하나의 웹 페이지에 속하는 여러 요소에 같은 아이디 이름을 사용해도 별 문제없이 동작합니다.

하지만 이렇게 중복된 아이디를 가지고 자바스크립트 작업을 하게 되면 오류가 발생합니다.

따라서 되도록이면 하나의 웹 페이지에 속하는 요소에는 다른 아이디 이름을 사용하거나 클래스를 사용하는 것이 좋습니다.

### 클래스(class) 선택자

---

클래스 선택자는 특정 집단의 여러 요소를 한 번에 선택할 때 사용합니다.

이러한 특정 집단을 클래스(class)라고 하며, 같은 클래스 이름을 가지는 요소들을 모두 선택해 줍니다.

```HTML
<style>
.headings { color: deepskyblue; text-decoration: overline; }
</style>
...
<h2 class="headings">이 부분에 스타일을 적용합니다.</h2>
<p>클래스 선택자를 이용하여 스타일을 적용할 HTML 요소들을 한 번에 선택할 수 있습니다.</p>
<h3 class="headings">이 부분에도 같은 스타일을 적용합니다.</h3>
```

### 그룹 선택자

---

그룹 선택자는 위에서 언급한 여러 선택자를 같이 사용하고자 할 때 사용합니다.

그룹 선택자는 여러 선택자를 쉼표(,)로 구분하여 연결합니다.

이러한 그룹 선택자는 코드를 중복해서 작성하지 않도록 하여 코드를 간결하게 만들어 줍니다.

```HTML
<style>
h2 { color: navy; }
h2, h3 { text-align: center; }
h2, h3, p { background-color: lightgray; }
</style>
```

  

## 결합 선택자

### 결합 선택자

---

CSS 선택자는 하나 이상의 선택자를 포함할 수 있습니다.

결합 선택자는 연관된 선택자들 간의 관계를 설정해 줍니다.

### 자손 선택자(descendant selector)

---

자손 선택자는 해당 요소의 하위 요소 중에서 특정 타입의 요소를 모두 선택합니다.

다음 예제는 모든 <div>태그의 하위 요소 중에서 <p>태그를 모두 선택하는 예제입니다.

```CSS
div p {스타일;}
```

위의 예제처럼 자손 선택자는 div와 p 사이에 한 칸의 띄어쓰기를 반드시 명시해야 합니다.

```HTML
<style>
div p { background-color: \#FFEFD5; }
</style>
```

### 자식 선택자(child selector)

---

자식 선택자는 해당 요소의 바로 밑에 존재하는 하위 요소 중에서 특정 타입의 요소를 모두 선택합니다.

다음 예제는 모든 <div>태그의 바로 밑에 존재하는 하위 요소 중에서 <p>태그를 모두 선택하는 예제입니다.

```CSS
div > p {스타일;}
```

```HTML
<style>
div > p { background-color: **\#FFEFD5**; }
</style>
```

  

## 동위 선택자

### 동위 선택자(s[ibling s](https://www.w3.org/TR/css3-selectors/#sibling-combinators)elector)

---

동위 선택자는 동위 관계에 있는 요소 중에서 해당 요소보다 뒤에 존재하는 특정 타입의 요소를 모두 선택합니다.

동위 관계란 HTML 요소의 계층 구조에서 같은 부모(parent) 요소를 가지고 있는 요소들을 의미합니다.

이러한 동위 관계에 있는 요소들을 형제(sibling) 요소라고 합니다.

[![](http://www.tcpschool.com/lectures/img_css_sibling.png)](http://www.tcpschool.com/lectures/img_css_sibling.png)

위의 그림에서 초록색으로 표시된 세 요소는 모두 <body>요소를 부모 요소로 가집니다.

따라서 이 세 요소는 동위 관계에 있는 형제 요소라고 할 수 있습니다.

### 일반 동위 선택자(general sibling [s](https://www.w3.org/TR/css3-selectors/#sibling-combinators)elector)

---

일반 동위 선택자는 해당 요소와 동위 관계에 있으며, 해당 요소보다 뒤에 존재하는 특정 타입의 요소를 모두 선택합니다.

다음 예제는 모든 <div>태그와 동위 관계에 있는 요소 중에서 <div>태그보다 뒤에 존재하는 <p>태그를 모두 선택하는 예제입니다.

```CSS
div ~ p {스타일;}
```

  

```HTML
<style>
div ~ p { background-color: \#FFE4E1; }
</style>
```

### 인접 동위 선택자(adjacent sibling [s](https://www.w3.org/TR/css3-selectors/#sibling-combinators)elector)

---

영어로 adjacent는 인접한, 가까운 이라는 의미가 있습니다.

인접 동위 선택자는 해당 요소와 동위 관계에 있으며, 해당 요소의 바로 뒤에 존재하는 특정 타입의 요소를 모두 선택합니다..

다음 예제는 모든 <div>태그와 동위 관계에 있는 요소 중에서 <div>태그의 바로 뒤에 존재하는 <p>태그를 모두 선택하는 예제입니다.

```CSS
div + p {스타일;}
```

  

```HTML
<style>
div + p { background-color: \#FFE4E1; }
</style>
```

  

## 의사 클래스

### 의사 클래스(pseudo-class)

---

CSS에서 의사 클래스(pseudo-class)는 선택하고자 하는 HTML 요소의 특별한 '상태(state)'를 명시할 때 사용합니다.

### 의사 클래스의 문법

---

의사 클래스(pseudo-class)를 사용하기 위한 문법은 다음과 같습니다.

> [!important]  
> 문법선택자:의사클래스이름 {속성: 속성값;}  

클래스(class)나 아이디(id)에도 의사 클래스(pseudo-class)를 사용할 수 있습니다.

> [!important]  
> 문법선택자.클래스이름:의사클래스이름 {속성: 속성값;}선택자#아이디이름:의사클래스이름 {속성: 속성값;}  

의사 클래스(pseudo-class)의 이름은 대소문자를 구분하지 않습니다.

### 대표적인 CSS 의사 클래스

---

CSS에서 자주 사용하는 대표적인 의사 클래스는 다음과 같습니다.

1. 동적 의사 클래스(dynamic pseudo-classes)

- :link
- :visited
- :hover
- :active
- :focus

[동적 의사 클래스 수업 확인 =>](http://www.tcpschool.com/css/css_selector_dynamic)

  

2. 상태 의사 클래스(UI element states pseudo-classes)

- :checked
- :enabled
- :disabled

[상태 의사 클래스 수업 확인 =>](http://www.tcpschool.com/css/css_selector_state)

  

3. 구조 의사 클래스(structural pseudo-classes)

- :first-child
- :nth-child
- :first-of-type
- :nth-of-type

[구조 의사 클래스 수업 확인 =>](http://www.tcpschool.com/css/css_selector_structure)

  

4. 기타 의사 클래스

- :not
- :lang

[기타 의사 클래스 수업 확인 =>](http://www.tcpschool.com/css/css_selector_etc)

### CSS 의사 클래스(pseudo classes)

---

|속성|설명|
|---|---|
|:link|사용자가 아직 한 번도 해당 링크를 통해서 연결된 페이지를 방문하지 않은 상태를 모두 선택함. (기본 상태)|
|:visited|사용자가 한 번이라도 해당 링크를 통해서 연결된 페이지를 방문한 상태를 모두 선택함.|
|:hover|사용자의 마우스 커서가 링크 위에 올라가 있는 상태를 모두 선택함.|
|:active|사용자가 마우스로 링크를 클릭하고 있는 상태를 모두 선택함.|
|:focus|초점이 맞춰진 input 요소를 모두 선택함.|
|:checked|체크된(checked) 상태의 input 요소를 모두 선택함.|
|:enabled|사용할 수 있는 input 요소를 모두 선택함.|
|:disabled|사용할 수 없는 input 요소를 모두 선택함.|
|:target|현재 활성화된 target 요소를 모두 선택함.|
|:in-range|특정 범위 내의 값을 가지는 input 요소를 모두 선택함.|
|:out-of-range|특정 범위를 벗어나는 값을 가지는 input 요소를 모두 선택함.|
|:read-only|readonly 속성을 가지는 input 요소를 모두 선택함.|
|:read-write|readonly 속성을 가지지 않는 input 요소를 모두 선택함.|
|:required|required 속성을 가지는 input 요소를 모두 선택함.|
|:optional|required 속성을 가지지 않는 input 요소를 모두 선택함.|
|:valid|유효한 값을 가지는 input 요소를 모두 선택함.|
|:invalid|유효하지 않은 값을 가지는 input 요소를 모두 선택함.|
|:first-child|모든 자식(child) 요소 중에서 첫 번째에 위치하는 자식(child) 요소를 모두 선택함.|
|:last-child|모든 자식(child) 요소 중에서 마지막에 위치하는 자식(child) 요소를 모두 선택함.|
|:nth-child|모든 자식(child) 요소 중에서 앞에서부터 n번째에 위치하는 자식(child) 요소를 모두 선택함.|
|:nth-last-child|모든 자식(child) 요소 중에서 뒤에서부터 n번째에 위치하는 자식(child) 요소를 모두 선택함.|
|:first-of-type|모든 자식(child) 요소 중에서 첫 번째로 등장하는 특정 요소를 모두 선택함.|
|:last-of-type|모든 자식(child) 요소 중에서 마지막으로 등장하는 특정 요소를 모두 선택함.|
|:nth-of-type|모든 자식(child) 요소 중에서 n번째로 등장하는 특정 요소를 모두 선택함.|
|:nth-last-of-type|모든 자식(child) 요소 중에서 뒤에서부터 n번째로 등장하는 특정 요소를 모두 선택함.|
|:only-child|자식(child) 요소를 단 하나만 가지는 모든 요소의 자식(child) 요소를 선택함.|
|:only-of-type|자식(child)  요소를 특정 요소 단 하나만 가지는 모든 요소의 자식(child) 요소를 선택함.|
|:empty|아무런 자식(child) 요소도 가지지 않는 요소를 모두 선택함.|
|:root|문서의 root 요소를 선택함.|
|:not(선택자)|모든 선택자와 함께 사용할 수 있으며, 해당 선택자를 반대로 적용함.|
|:lang(언어)|특정 요소를 언어 설정에 따라 다르게 표현할 때에 사용함.|