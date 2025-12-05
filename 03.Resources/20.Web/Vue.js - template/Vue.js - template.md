---
type: Vue.js
archive: false
---
### 보간법(Interpolation)

---

- 문자열
    
    데이터 바인딩의 가장 기본 형태는 "Mustache" 구문(이중 중괄호)을 사용한 텍스트 보간
    
    {{ 속성명 }}
    
    v-once 디렉티브를 사용하여데이터 변경 시 업데이트 되지 않는 일회성 보간을 수행
    
    v-once
    
    ![[Untitled 51.png|Untitled 51.png]]
    
    ![[Untitled 1 29.png|Untitled 1 29.png]]
    

  

- 원시 HTML
    
    이중 중괄호(mustaches)는 HTML이 아닌 일반 텍스트로 데이터를 해석
    
    실제 HTML을 출력하려면 v-html 디렉티브를 사용
    
    ![[Untitled 2 28.png|Untitled 2 28.png]]
    
    ![[Untitled 3 27.png|Untitled 3 27.png]]
    
      
    
- JavaScript 표현식 사용
    
    Vue.js는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
    
    ![[Untitled 4 23.png|Untitled 4 23.png]]
    
    한가지 제한사항은 각 바인딩에 하나의 단일 표현식만 포함될 수 있으므로 아래처럼 작성하면 안된다.
    
    ![[Untitled 5 21.png|Untitled 5 21.png]]
    
    ![[Untitled 6 18.png|Untitled 6 18.png]]
    
      
    

### 디렉티브(Directives)

---

디렉티브는 v-접두사가 있는 특수 속성

디렉티브 속성 값은 단일 JavaScript 표현식이 된다. (v-for는 예외)

디렉티브의 역할은 표현식의 값이 변경될 때 사이드 이펙트를 반응적으로 DOM에 적용.

![[Untitled 7 15.png|Untitled 7 15.png]]

  

==v-model==

양방향 바인딩 처리를 위해서 사용 (form의 input, textarea).

![[Untitled 8 13.png|Untitled 8 13.png]]

  

==v-bind==

엘리먼트의 속성과 바인딩 처리를 위해서 사용

v-bind는 약어로 ":" 로 사용 가능

![[Untitled 9 13.png|Untitled 9 13.png]]

  

==v-show==

조건에 따라 엘리먼트를 화면에 렌더링

style의 display를 변경

![[Untitled 10 11.png|Untitled 10 11.png]]

  

==v-if, v-else-if, v-else==

조건에 따라 엘리먼트를 화면에 렌더링

![[Untitled 11 9.png|Untitled 11 9.png]]

  

- v-show VS v-if의 차이점
    
    ![[Untitled 12 9.png|Untitled 12 9.png]]
    
      
    

==v-for==

배열이나 객체의 반복에 사용

v-for="요소변수이름 in 배열" v-for="(요소변수이름, 인덱스) in 배열"

![[Untitled 13 9.png|Untitled 13 9.png]]

  

==template==

여러 개의 태그들을 묶어서 처리해야 할 경우 template를 사용

v-if, v-for, component 등과 함께 많이 사용

![[Untitled 14 9.png|Untitled 14 9.png]]

  

==v-cloak==

Vue Instance가 준비될 때까지 mustache 바인딩을 숨기는데 사용

[v-cloak] { display: none }과 같은 CSS 규칙과 함께 사용

Vue Instance가 준비되면 v-cloak는 제거됨

![[Untitled 15 8.png|Untitled 15 8.png]]

  

### Vue method

---

Vue Instance는 생성과 관련된 data 및 method의 정의 가능

method안에서 data를 "this.데이터이름" 으로 접근 가능

![[Untitled 16 7.png|Untitled 16 7.png]]

![[Untitled 17 5.png|Untitled 17 5.png]]