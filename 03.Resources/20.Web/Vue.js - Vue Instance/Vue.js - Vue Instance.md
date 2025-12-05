---
type: Vue.js
archive: false
---
### Vue Instance 생성

---

![[Untitled 33.png|Untitled 33.png]]

  

### Vue Instance의 유효범위

---

Vue Instance를 생성하면 HTML의 특정 범위 안에서만 옵션 속성들이 적용

el 속성과 밀접한 관계가 있다.

![[Untitled 1 13.png|Untitled 1 13.png]]

![[Untitled 2 12.png|Untitled 2 12.png]]

  

- 유효범위를 벗어난 경우
    
    ![[Untitled 3 11.png|Untitled 3 11.png]]
    
      
    

### Vue Instance Life Cycle

---

![[Untitled 4 9.png|Untitled 4 9.png]]

- Life Cycle은 크게 나누면 Instance의 생성, 생성된 Instance를 화면에 부착, 화면에 부착된 Instance의 내용이 갱신, Instance가 제거되는 소멸의 4단계로 나뉜다.
    
    ![[Untitled 5 8.png|Untitled 5 8.png]]
    
      
    

### Life Cycle Hooks Ex

---

![[Untitled 6 6.png|Untitled 6 6.png]]

![[Untitled 7 5.png|Untitled 7 5.png]]