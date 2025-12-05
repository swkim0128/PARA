---
type: Vue.js
archive: false
---
### vuex

---

Vue.js application에 대한 생태관리패턴 + 라이브러리

application 모든 component들의 중앙 저장소 역할 (데이터 관리)

상위(부모) 하위(자식)의 단계가 많이 복잡해 진다면 데이터의 전달하는 부분이 매우 복잡해 짐

application이 여러 구성 요소로 구성되고 더 커지는 경우 데이터를 공유하는 문제가 발생

![[Untitled 45.png|Untitled 45.png]]

![[Untitled 1 23.png|Untitled 1 23.png]]

![[Untitled 2 22.png|Untitled 2 22.png]]

  

### 상태관리패턴

---

![[Untitled 3 21.png|Untitled 3 21.png]]

  

### vuex의 핵심 컨셉 이해

---

![[Untitled 4 17.png|Untitled 4 17.png]]

  

### vuex 설치

---

- CDN
    
    <srcipt src="https://unpkg.com/vuex"></script>
    
- npm
    
    npm install vuex —save
    
      
    

### vuex 저장소 개념

---

- State : 단일 상태 트리를 사용. application마다 하나의 저장소를 관리(data)
- Getters : Vue Instacne 의 Computed와 같은 역할. State를 기반으로 계산(computed)
- Mutations : State의 상태를 변경하는 유일한 방법 (동기 methods)
- Actions : 상태를 변이 시키는 대신 액션으로 변이에 대한 커밋 처리 (비동기 methods)

  

### vuex 설정

---

- medule 시스템과 함께 사용시 Vue.use()를 통해 Vuex 설정
    
    ![[Untitled 5 15.png|Untitled 5 15.png]]
    

  

### 저장소(Store) - state

---

저장소에서 data 속성의 역할

application에서 공유해야 할 data를 관리

State에 접근하는 방식 : this.$store.state.data_name

  

### vuex Store - state

---

![[Untitled 6 12.png|Untitled 6 12.png]]

  

### 저장소 - Getters

---

- component가 vuex의 state를 직접 접근하는 코드가 중복된다면?
- 해결 : Store의 state를 참조하는 Getters를 활용
- 정의
    
    ![[Untitled 7 10.png|Untitled 7 10.png]]
    
- 사용
    
    this.$store.getters.countMsg;
    
      
    

### vuex Store - Getters

---

![[Untitled 8 8.png|Untitled 8 8.png]]

  

### 저장소 (Store) - mapGetters

---

- getters를 조금 더 간단하게 호출
- 주의 : Babel 관련 에러 발생시 해결
    
    ...mapGetters 관련
    
    es6 spread operation 관련 에러 발생
    
    ![[Untitled 9 8.png|Untitled 9 8.png]]
    
      
    

### 저장소 (Store) - Mutations

---

- State의 값을 변경하기 위해서 사용
- 각 컴포넌트에서 State의 값을 직접 변경하는 것은 권장하지 않는 방식
- State의 값의 추적을 위해 동기적 기능에 사용
- Mutations는 직접 호출이 불가능하고 store.commit('정의된 이름')으로 호출

  

### vuex Store - Mutations

---

![[Untitled 10 7.png|Untitled 10 7.png]]

  

### 저장소 (Store) - Actions

---

- 비동기 작업의 결과를 적용하려고 할 때 사용
- Mutations는 상태 관리를 위해 동기적으로 처리하고 비동기적인 처리는 Actions가 담당
- Actions는 비동기 로직의 처리가 종료되면 Mutations를 호출

  

![[Untitled 11 6.png|Untitled 11 6.png]]

  

### vuex 단계별 이해하기

---

- step00 : Vuex 적용전 코드
    
    ![[Untitled 12 6.png|Untitled 12 6.png]]
    
      
    
- step01 : vuex사용
    
    ![[Untitled 13 6.png|Untitled 13 6.png]]
    
    ![[Untitled 14 6.png|Untitled 14 6.png]]
    
    ![[Untitled 15 5.png|Untitled 15 5.png]]
    

  

### 저장소 (Store) - Getters 등록

---

- step02
    
    ![[Untitled 16 5.png|Untitled 16 5.png]]
    
    ![[Untitled 17 3.png|Untitled 17 3.png]]
    
      
    

### 저장소(Store) - mapGetters

---

- step03
    
    ![[Untitled 18 3.png|Untitled 18 3.png]]
    
    ![[Untitled 19 3.png|Untitled 19 3.png]]
    
    ![[Untitled 20 3.png|Untitled 20 3.png]]
    
      
    

### 저장소 (Store) - Mutations 등록

---

- step04
    
    ![[Untitled 21 2.png|Untitled 21 2.png]]
    
    ![[Untitled 22 2.png|Untitled 22 2.png]]
    
      
    
- step05
    
    ![[Untitled 23 2.png|Untitled 23 2.png]]
    
      
    

### 저장소 (Store) - Actions 등록

---

- step06
    
    ![[Untitled 24 2.png|Untitled 24 2.png]]
    
      
    

### 저장소 (Store) - Actions 호출

---

- step06
    
    ![[Untitled 25 2.png|Untitled 25 2.png]]
    
      
    

### 저장소 (Store) - mapActions

---

- step07
    
    ![[Untitled 26 2.png|Untitled 26 2.png]]