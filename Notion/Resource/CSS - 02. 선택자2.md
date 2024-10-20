---
type: HTML/CSS
archive: false
---
## 동적 의사 클래스

### 동적 의사 클래스(dynamic pseudo-class)

---

CSS에서 사용할 수 있는 동적 의사 클래스는 다음과 같습니다.

- :link
- :visited
- :hover
- :active
- :focus

동적 의사 클래스를 사용하면 링크의 상태에 따라 각각의 스타일을 별도로 설정할 수 있습니다.

```HTML
<style>
a:link {color: orange;}
a:visited {color: gray;}
a:hover {color: blue;}
a:active {color: red;}
div:hover { background-color: blue; color: white; }
</style>
```

### 링크(link)의 상태

---

링크는 총 5가지의 상태를 가지며, 각 상태마다 별도의 스타일을 적용할 수 있습니다.

1. link : 링크의 기본 상태이며, 사용자가 아직 한 번도 이 링크를 통해 연결된 페이지를 방문하지 않은 상태입니다.

2. visited : 사용자가 한 번이라도 이 링크를 통해 연결된 페이지를 방문한 상태입니다.

3. hover : 사용자의 마우스 커서가 링크 위에 올라가 있는 상태입니다.

4. active : 사용자가 마우스로 링크를 클릭하고 있는 상태입니다.

5. focus : 키보드나 마우스의 이벤트(event) 또는 다른 형태로 해당 요소가 포커스(focus)를 가지고 있는 상태입니다.

:hover는 반드시 :link와 :visited가 먼저 정의된 후에 정의되어야 정상적으로 동작합니다.

:active는 반드시 :hover가 먼저 정의된 후에 정의되어야 정상적으로 동작합니다.

```HTML
<style>
input { border: 3px solid \#FFEFD5; transition: 0.5s; }
input:focus { border: 3px solid \#CD853F; }
</style>
```

### CSS 동적 의사 클래스(dynamic pseudo-class)

---

|속성|설명|
|---|---|
|:link|사용자가 아직 한 번도 이 링크를 통해서 연결된 페이지를 방문하지 않은 상태를 선택함. (기본 상태)|
|:visited|사용자가 한 번이라도 이 링크를 통해서 연결된 페이지를 방문한 상태를 선택함.|
|:hover|사용자의 마우스 커서가 링크 위에 올라가 있는 상태를 선택함.|
|:active|사용자가 마우스로 링크를 클릭하고 있는 상태를 선택함.|
|:focus|포커스를 가지고 있는 input 요소를 모두 선택함.|

  

## 상태 의사 클래스

### 상태 의사 클래스(UI element states pseudo-class)

---

상태 의사 클래스를 사용하면 입력 양식의 상태에 따라 각각의 스타일을 별도로 설정할 수 있습니다.

CSS에서 사용할 수 있는 상태 의사 클래스는 다음과 같습니다.

- :checked:enabled:disabled

### :checked

---

:checked는 input 요소 중에서 체크된(checked) 상태의 input 요소를 선택합니다.

```HTML
<style>
input { color: **\#FFEFD5**; }
input:checked + span { color: **\#CD853F**; }
</style>
```

### :enabled와 :disabled

---

:enabled는 input 요소 중에서 사용할 수 있는 input 요소를 선택합니다.

또한, :disabled는 input 요소 중에서 사용할 수 없는 input 요소를 선택합니다.

```HTML
<style>
input { color: \#FFEFD5; }
input:disabled + span { color: \#CD853F; }
</style>
```

### CSS 상태 의사 클래스(UI element states pseudo-class)

---

|속성|설명|
|---|---|
|:checked|체크된(checked) 상태의 input 요소를 모두 선택함.|
|:enabled|사용할 수 있는 input 요소를 모두 선택함.|
|:disabled|사용할 수 없는 input 요소를 모두 선택함.|

  

## 구조 의사 클래스

### 구조 의사 클래스(structural pseudo-class)

---

구조 의사 클래스를 사용하면 HTML 요소의 계층 구조에서 특정 위치에 있는 요소를 선택할 수 있습니다.

CSS에서 사용할 수 있는 구조 의사 클래스는 다음과 같습니다.

- :first-child:last-child:nth-child:nth-last-child
- :first-of-type:last-of-type:nth-of-type:nth-last-of-type

### :first-child

---

:first-child는 모든 자식(child) 요소 중에서 맨 앞에 위치하는 자식(child) 요소를 모두 선택합니다.

```HTML
<style>
p:first-child { color: red; font-weight: bold; }
</style>
```

### :last-child

---

:last-child는 모든 자식(child) 요소 중에서 맨 마지막에 위치하는 자식(child) 요소를 모두 선택합니다.

```HTML
<style>
p:last-child { color: red; font-weight: bold; }
</style>
```

### :nth-child

---

:nth-child는 모든 자식(child) 요소 중에서 앞에서부터 n번째에 위치하는 자식(child) 요소를 모두 선택합니다.

```HTML
<style>
p:nth-child(2n) { color: red; font-weight: bold; }
</style>
```

### :nth-last-child

---

:nth-last-child는 모든 자식(child) 요소 중에서 뒤에서부터 n번째에 위치하는 자식(child) 요소를 모두 선택합니다.

```HTML
<style>
p:nth-last-child(3n) { color: red; font-weight: bold; }
</style>
```

### :first-of-type

---

:first-of-type는 모든 자식(child) 요소 중에서 맨 처음으로 등장하는 특정 타입의 요소를 모두 선택합니다.

```HTML
<style>
p:first-of-type { color: red; font-weight: bold; }
</style>
```

### :last-of-type

---

:last-of-type는 모든 자식(child) 요소 중에서 맨 마지막으로 등장하는 특정 타입의 요소를 모두 선택합니다.

```HTML
<style>
p:last-of-type { color: red; font-weight: bold; }
</style>
```

### :nth-of-type

---

:nth-of-type는 모든 자식(child) 요소 중에서 n번째로 등장하는 특정 타입의 요소를 모두 선택합니다.

```HTML
<style>
p:nth-of-type(2n) { color: red; font-weight: bold; }
</style>
```

### :nth-last-of-type

---

:nth-last-of-type는 모든 자식(child) 요소 중에서 뒤에서부터 n번째로 등장하는 특정 타입의 요소를 모두 선택합니다.

```HTML
<style>
p:nth-last-of-type(2n+1) { color: red; font-weight: bold; }
</style>
```

### :only-child

---

:only-child는 자식(child) 요소를 단 하나만 가지는 요소의 자식(child) 요소를 모두 선택합니다.

```HTML
<style>
p:only-child { color: red; font-weight: bold; }
</style>
```

### :only-of-type

---

:only-of-type는 자식(child)  요소로 특정 타입의 요소 단 하나만을 가지는 요소의 자식(child) 요소를 모두 선택합니다.

```HTML
<style>
p:only-of-type { color: red; font-weight: bold; }
</style>
```

### :empty

---

:empty는 자식(child) 요소를 전혀 가지고 있지 않은 요소를 모두 선택합니다.

```HTML
<style>
p:empty { width: 300px; height: 20px; background: red; }
</style>
```

### :root

---

:root는 해당 문서의 root 요소를 선택합니다.

```HTML
<style>
:root { background: red; }
</style>
```

HTML 문서에서 root 요소는 언제나 html 요소입니다.

### CSS 구조 의사 클래스(structural pseudo-class)

---

|속성|설명|
|---|---|
|:first-child|모든 자식(child) 요소 중에서 맨 앞에 위치하는 자식(child) 요소를 모두 선택함.|
|:last-child|모든 자식(child) 요소 중에서 맨 마지막에 위치하는 자식(child) 요소를 모두 선택함.|
|:nth-child|모든 자식(child) 요소 중에서 앞에서부터 n번째에 위치하는 자식(child) 요소를 모두 선택함.|
|:nth-last-child|모든 자식(child) 요소 중에서 뒤에서부터 n번째에 위치하는 자식(child) 요소를 모두 선택함.|
|:first-of-type|모든 자식(child) 요소 중에서 맨 처음으로 등장하는 특정 타입의 요소를 모두 선택함.|
|:last-of-type|모든 자식(child) 요소 중에서 맨 마지막으로 등장하는 특정 타입의 요소를 모두 선택함.|
|:nth-of-type|모든 자식(child) 요소 중에서 n번째로 등장하는 특정 타입의 요소를 모두 선택함.|
|:nth-last-of-type|모든 자식(child) 요소 중에서 뒤에서부터 n번째로 등장하는 특정 타입의 요소를 모두 선택함.|
|:only-child|자식(child) 요소를 단 하나만 가지는 요소의 자식(child) 요소를 모두 선택함.|
|:only-of-type|자식(child)  요소로 특정 타입의 요소 단 하나만을 가지는 요소의 자식(child) 요소를 모두 선택함.|
|:empty|자식(child) 요소를 전혀 가지고 있지 않은 요소를 모두 선택함.|
|:root|문서의 root 요소를 선택함.|