---
type: Vue.js
archive: false
---
### vue-router

---

라우팅 : 웹 페이지 간의 이동 방법

Vue.js의 공식 라우터

라우터는 컴포넌트와 매핑

Vue를 이용한 SPA를 제작할 때 유용

URL에 따라 컴포넌트를 연결하고 설정된 컴포넌트를 보여준다.

https://router.vuejs.org/kr

  

### vue-router 설치

---

CDN 방식

<script src="https://cdn.jsdelivr.net/npm/vue/dist.vue.js"></script>

<script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>

  

NPM 방식

npm install vue-router

  

### vue-router 연결

---

'routes' 옵션과 함께 router instance 생성

![[Untitled 32.png|Untitled 32.png]]

  

### vue-router 이동 및 렌더링

---

네비게이션을 위해 router-link 컴포넌트를 사용

속성은 'to' prop을 사용

기본적으로 '<router-link>'는 '<a>' 태그로 렌더링

![[Untitled 1 12.png|Untitled 1 12.png]]

  

현재 라우트에 맞는 컴포넌트가 렌더링된다.

![[Untitled 2 11.png|Untitled 2 11.png]]

![[Untitled 3 10.png|Untitled 3 10.png]]

![[Untitled 4 8.png|Untitled 4 8.png]]

  

### $router, $route

---

라우터 설정

![[Untitled 5 7.png|Untitled 5 7.png]]

라우터 링크

![[Untitled 6 5.png|Untitled 6 5.png]]

전체 라우터 정보

![[Untitled 7 4.png|Untitled 7 4.png]]

현재 호출된 해당 라우터 정보

![[Untitled 8 4.png|Untitled 8 4.png]]

  

### vue-router 이동 및 렌더링

---

![[Untitled 9 4.png|Untitled 9 4.png]]

  

![[Untitled 10 4.png|Untitled 10 4.png]]

  

### 이름을 가지는 라우트

---

라우트는 연결하거나 탐색을 수행할 때 이름이 있는 라우트를 사용

Router Instance를 생성하는 동안 routes 옵션에 지정

![[Untitled 11 3.png|Untitled 11 3.png]]

![[Untitled 12 3.png|Untitled 12 3.png]]

![[Untitled 13 3.png|Untitled 13 3.png]]

  

### 프로그래밍 방식 라우터

---

<router-link>를 사용하여 선언적 네비게이션용 anchor 태그를 만드는 것 외에도 라우터의 instance method를 사용하여 프로그래밍으로 수행

![[Untitled 14 3.png|Untitled 14 3.png]]

![[Untitled 15 2.png|Untitled 15 2.png]]

![[Untitled 16 2.png|Untitled 16 2.png]]

  

### 중첩된 라우트

---

앱 UI는 일반적으로 여러 단계로 중첩 된 컴포넌트 구조임.

URL의 세그먼트가 중첩된 컴포넌트의 특정 구조와 일치하는 것을 활용

![[Untitled 17 2.png|Untitled 17 2.png]]

![[Untitled 18 2.png|Untitled 18 2.png]]

![[Untitled 19 2.png|Untitled 19 2.png]]

  

### 라우트 리다이렉트

---

![[Untitled 20 2.png|Untitled 20 2.png]]