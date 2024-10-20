---
type: JavaScript
archive: false
---
### jQuery DOM Event 처리

---

jQuery Event 처리

- jQuery Event로 기존 JavaScript DOM Event를 간편하게 처리, 연결 가능.
- 이벤트 핸들러를 할당, 해제할 수 있는 통합 메소드 제공.
- DOM Element의 이벤트 타입마다 여러 핸들러 할당 가능.
- click, mouseover 등과 같은 표준 이벤트 타입명을 사용
- 핸들러의 매개변수로 이벤트 인스턴스를 사용 가능.
- 자주 사용하는 이벤트 인스턴스의 프로퍼티 등에 일관된 이름 제공.
- 하나의 API로 표준 호환 브라우저와 IE 동시 지원.

  

### jQuery Event Binding

---

bind()  
  
  

unbind()

on()  
  
  
  
  

off()

선택된 DOM 객체의 이벤트에 지정한 핸들러를 연결하는 함수.  
동적으로 생성한 DOM객체에는 적용 X.  
bind(eventType, data, listener)  

객체 이벤트에서 지정한 핸들러를 지운다.

DOM 객체에 이벤트 핸들러를 연결.  
delegate 방식으로 사용할 경우 현재 존재하는 DOM 객체 뿐만 아니라 동적으로 생성한 DOM 객체에도 적용 가능.  
Event Delegate 방식은 부모 DOM 객체에 이벤트를 연결한 후 이를 하위 DOM 객체에 전달하는 방식으로 동적으로 적용 가능.  

DOM 객체의 이벤트를 제거

  

Simple Event Bind

DOM 객체에 이벤트를 간단하게 연결할 수 있는 다양한 함수를 제공.

![[Untitled 53.png|Untitled 53.png]]

  

one()

이벤트를 연결하고 한 번 실행 후 삭제하는 기능.

  

### Mouse Event

---

![[Untitled 1 31.png|Untitled 1 31.png]]

  

### Keyboard Event

---

![[Untitled 2 30.png|Untitled 2 30.png]]

  

### Window Event

---

![[Untitled 3 29.png|Untitled 3 29.png]]

  

### Input Event

---

주로 <form>, <input> 등에서 발생하는 입력 이벤트를 처리한다.

![[Untitled 4 25.png|Untitled 4 25.png]]