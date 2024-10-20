---
type: Vue.js
archive: false
---
### 컴포넌트 (Component)

---

Vue의 가장 강력한 기능 중 하나

HTML Element를 확장하여 재사용 가능한 코드를 캡슐화

Vue Component는 Vue Instance이기도 하기 때문에 모든 옵션 객체를 사용

Life Cycle Hook 사용 가능.

전역 콤포넌트와 지역 컴포넌트

![[Untitled 10.png|Untitled 10.png]]

  

### 전역 컴포넌트 등록

---

전역 컴포넌트를 등록하려면, Vue.component(tagName, options)를 사용

권장하는 컴포넌트 이름 : 케밥 표기법( 전부 소문자, -) 이름 표기법 참조, Style Guide(명명규칙)

![[Untitled 1 3.png|Untitled 1 3.png]]

  

### 지역 컴포넌트 등록

---

컴포넌트를 components 인스턴스 옵션으로 등록함으로써 다른 인스턴스/컴포넌트의 범위에서만 사용할 수 있는 컴포넌트를 만들 수 있다.

![[Untitled 2 3.png|Untitled 2 3.png]]

  

![[Untitled 3 3.png|Untitled 3 3.png]]

  

### Component Template

---

![[Untitled 4 2.png|Untitled 4 2.png]]

  

### Component data 공유

---

문제

![[Untitled 5 2.png|Untitled 5 2.png]]

  

해결

![[Untitled 6 2.png|Untitled 6 2.png]]

  

### 컴포넌트간 통신

---

상위(부모) - 하위(자식) 컴포넌트 간의 data 전달 방법

부모에서 자식 : props라는 특별한 속성을 전달

자식에서 부모 : event로만 전달 가능

![[Untitled 7 2.png|Untitled 7 2.png]]

  

### 상위에서 하위 컴포넌트로 data 전달

---

하위 컴포넌트는 상위 컴포넌트의 값을 직접 참조 불가능.

data와 마찬가지로 props 속성의 값을 template에서 사용이 가능

  

### props

---

![[Untitled 8 2.png|Untitled 8 2.png]]

  

### literal props

---

![[Untitled 9 2.png|Untitled 9 2.png]]

  

### 렌더링 과정

---

1. new Vue()로 상위 컴포넌트인 인스턴스를 하나 생성
2. Vue.component()를 이용하여 하위 컴포넌트인 child-component를 생성
3. <div id="app"> 내부에 <child-component>가 있기 때문에 하위 컴포넌트가 된다. 처음 생성한 인스턴스 객체가 \#app의 요소를 가지기 때문에 부모와 자식 관계가 성립한다.
4. 하위 컴포넌트에 props 속성을 정의한다. ['propsdata']
5. html에 컴포넌트 태그(child-component)를 추가한다.
6. 하위 컴포넌트에 v-bind 속성을 사용하면 상위 컴포넌트의 data의 key에 접근이 가능하다. (message)
7. 상위 컴포넌트의 message 속성 값인 String 값이 하위 컴포넌트의 propsdata로 전달된다.
8. 하위 컴포넌트의 template 속성에 정의된 '<span>{{ propsdata}}</span>'에게 전달된다.

  

### 동적 props

---

v-bind를 사용하여 부모의 데이터에 props를 동적으로 바인딩 할 수 있다.

데이터가 상위에서 업데이트 될 때마다 하위 데이터로도 전달된다.

![[Untitled 10 2.png|Untitled 10 2.png]]

  

v-bind에 대한 단축 구문을 사용하는 것이 더 간단하다.

![[Untitled 11.png]]

  

![[Untitled 12.png]]

![[Untitled 13.png]]

  

### 객체의 속성(properties) 전달 props

---

오브젝트의 모든 속성을 전달할 경우, v-bind:prop-name 대신 v-bind만 작성함으로써 모든 속성을 prop으로 전달할 수 있다.

![[Untitled 14.png]]

  

위 코드는 아래와 같이 동작

![[Untitled 15.png]]

  

![[Untitled 16.png]]

  

### 사용자 정의 이벤트(Custom Events)

---

이벤트 이름

- 컴포넌트 및 props와는 달리, 이벤트는 자동 대소문자 변환을 제공하지 않는다.
- 대소문자를 혼용하는 대신에 emit할 정확한 이벤트 이름을 작성하는 것을 권장
- v-on 이벤트 리스너는 항상 자동으로 소문자 변환되기 때문에 v-on:myEvent는 자동으로 v-on:myevent로 변환된다. 이름이 my-event일 경우 myEvent 이벤트를 들을 수 없다.
- 이러한 이유 때문에, 이벤트 이름에는 kebab-case를 사용하는 것이 권장됨.

![[Untitled 17.png]]

![[Untitled 18.png]]

  

### 하위에서 상위 컴포넌트로 event 전달

---

하위 컴포넌트에서 상위 컴포넌트가 지정한 이벤트를 발생 ($emit)

상위 컴포넌트는 하위 컴포넌트가 발생한 이벤트를 수신(on)하여 data 처리

![[Untitled 19.png]]

  

![[Untitled 20.png]]

  

### 비 상하위간 통신

---

비어 있는 Vue Instance 객체를 Event Bus로 사용

복잡해질 경우 상태관리 라이브러리인 Vuex 사용 권장

![[Untitled 21.png]]

![[Untitled 22.png]]

![[Untitled 23.png]]