---
type: Vue.js
archive: false
---
### Vue method

---

Vue Instance는 생성과 관련된 data 및 method의 정의 가능

method안에서 data를 "this.데이터이름"으로 접근 가능

![[Untitled 61.png|Untitled 61.png]]

![[Untitled 1 38.png|Untitled 1 38.png]]

  

### Vue filter

---

filter를 이용하여 표현식에 새로운 결과 형식을 적용

중괄호 보간법 [ {{}} ] 또는 v-bind 속성에서 사용이 가능

![[Untitled 2 37.png|Untitled 2 37.png]]

  

![[Untitled 3 36.png|Untitled 3 36.png]]

  

### Vue filter 사용 예

---

![[Untitled 4 32.png|Untitled 4 32.png]]

  

### Vue computed 속성

---

특정 데이터의 변경사항을 실시간으로 처리

캐싱을 이용하여 데이터의 변경이 없을 경우 캐싱된 데이터를 반환

Setter와 Getter를 직접 지정할 수 있음

작성은 method 형태로 작성하지만 Vue에서 proxy 처리하여 property처럼 사용

  

### Vue computed VS method 차이점

---

computed 속성은 Vue 인스턴스가 생성될 때, data의 message값을 받아 reversedMsg를 계산하여 저장해 놓는다.(캐싱)  
 ※ 위의 코드에서 reversedMsg를 한 번 실행하는 것과 같다.  

method는 reversedMsg()를 사용하려고 할 때 마다 계산한다.  
※ 위의 코드에서 reversedMsg()를 세 번 실행하는 것과 같다.  

  

![[Untitled 5 28.png|Untitled 5 28.png]]

  

### Vue watch 속성

---

Vue Instance의 특정 property가 변경될 때 실행할 콜백 함수 설정

![[Untitled 6 25.png|Untitled 6 25.png]]

![[Untitled 7 22.png|Untitled 7 22.png]]

  

### Vue event

---

Dom Event를 청취하기 위해 v-on directive 사용

inline event handling

method를 이용한 event handling

  

### Vue event 청취 : v-on

---

v-on directive를 사용하여 DOM 이벤트를 듣고 트리거 될 때 JavaScript를 실행할 수 있다.

![[Untitled 8 20.png|Untitled 8 20.png]]

  

### method event handler

---

이벤트 발생 시 처리 로직을 v-on에 넣기 힘들다 이 때문에 v-on에서는 이벤트 발생 시 처리해야 하는 method의 이름을 받아 처리

![[Untitled 9 19.png|Untitled 9 19.png]]

  

### inline method handler

---

메소드 이름을 직접 바인딩하는 대신 인라인 JavaScript 구문에 메소드를 사용할 수 도 있다.

원본 DOM 이벤트에 엑세스 해야 하는 경우 특별한 $event 변수를 사용해 메소드에 전달할 수도 있다.

![[Untitled 10 17.png|Untitled 10 17.png]]

  

### 이벤트 수식어 (Event Modifier)

---

event.preventDefault()와 같이 method내에서 작업을 할 수도 있지만 method는 DOM의 이벤트를 처리하는 것보다 data 처리를 위한 로직만 작업하는 것이 좋다.

이 문제를 해결하기 위해, Vue는 v-on 이벤트에 이벤트 수식어를 제공한다.

수식어는 점으로 표시된 접미사이다.

![[Untitled 11 14.png|Untitled 11 14.png]]

  

![[Untitled 12 13.png|Untitled 12 13.png]]

  

### 키 수식어 (Key Modifier)

---

Vue는 키 이벤트를 수신할 때 v-on에 대한 키 수식어를 추가할 수 있다.

![[Untitled 13 12.png|Untitled 13 12.png]]

key code

![[Untitled 14 11.png|Untitled 14 11.png]]

  

![[Untitled 15 9.png|Untitled 15 9.png]]

  

### ref, $refs

---

뷰에서는 $refs 속성을 이용해 DOM에 접근할 수 있다.

단, 뷰의 가장 중요한 목적 중 하나는 개발자가 DOM을 다루지 않게 하는 것이므로, 되도록 ==ref를 사용하는 것을 피하는 것이 좋다.==

![[Untitled 16 8.png|Untitled 16 8.png]]

  

### class binding

---

element의 class와 style을 변경

v-bind : class는 조건에 따라 class를 적용할 수 있다.

![[Untitled 17 6.png|Untitled 17 6.png]]

![[Untitled 18 5.png|Untitled 18 5.png]]

  

### 폼 입력 바인딩 (Form Input Bindings)

---

v-model directive를 사용하여 폼 input과 textarea element에 양방향 데이터 바인딩을 생성할 수 있다.

- text와 textarea 태그는 value 속성과 input 이벤트를 사용한다.
- 체크박스들과 라디오 버튼들은 checked 속성과 change 이벤트를 사용한다.
- Select 태그는 value를 prop으로, change를 이벤트로 사용한다.

  

### form - text, textarea

---

문자열.(text)

![[Untitled 19 5.png|Untitled 19 5.png]]

  

여러 줄을 가진 문장 (textarea)

- 텍스트 영역의 보간 (<textarea> {{ text }} </textarea>)은 작동하지 않는다. → v-model를 사용

![[Untitled 20 5.png|Untitled 20 5.png]]

  

![[Untitled 21 4.png|Untitled 21 4.png]]

  

### form - checkbox

---

하나의 체크박스는 단일 boolean 값을 갖는다.

![[Untitled 22 4.png|Untitled 22 4.png]]

  

여러 개의 체크박스는 같은 배열을 바인딩 할 수 있다.

배열의 값과 checkbox의 value 속성이 같을 경우 체크 처리됨.

![[Untitled 23 4.png|Untitled 23 4.png]]

  

### form - radio

---

radio의 경우 선택된 항목의 value 속성의 값을 관리

![[Untitled 24 4.png|Untitled 24 4.png]]

![[Untitled 25 4.png|Untitled 25 4.png]]

  

### form - select

---

select box일 경우 선택된 항목의 value 속성의 값을 관리

v-model 표현식의 초기 값이 어떤 옵션에도 없으면, `<select>` element는 "선택없음" 상태로 렌더링된다.

![[Untitled 26 4.png|Untitled 26 4.png]]

![[Untitled 27 3.png|Untitled 27 3.png]]

  

### form - select (multiple)

---

![[Untitled 28 3.png|Untitled 28 3.png]]

  

v-for를 이용한 동적 option 렌더링

![[Untitled 29 3.png|Untitled 29 3.png]]

  

### form - 수식어 (Modifiers)

---

- .lazy
    
    .lazy 수식어를 추가하여 change 이벤트 이후 에 동기화 할 수 있습니다.
    
    ![[Untitled 30 3.png|Untitled 30 3.png]]
    
      
    
- .number
    
    사용자 입력이 자동으로 숫자로 형 변환 되기를 원하면, v-model이 관리하는 input에 number 수식어를 추가하면 된다.
    
    ![[Untitled 31 3.png|Untitled 31 3.png]]
    
      
    
- .trim
    
    v-model이 관리하는 input을 자동으로 trim하기 원하면, trim 수정자를 추가하면 된다.
    
    ![[Untitled 32 3.png|Untitled 32 3.png]]