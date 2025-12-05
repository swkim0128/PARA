---
type: Spring
archive: false
---
### Web Architecture

---

![[Untitled 48.png|Untitled 48.png]]

  

- eclipse setting
    
    ![[Untitled 1 26.png|Untitled 1 26.png]]
    
    ![[Untitled 2 25.png|Untitled 2 25.png]]
    
      
    

### project 구조

---

![[Untitled 3 24.png|Untitled 3 24.png]]

  

### [HelloSsafy.java](http://HelloSsafy.java) 생성

---

![[Untitled 4 20.png|Untitled 4 20.png]]

  

### Servlet

---

자바 서블릿(Java Servlet)은 자바를 사용하여 웹페이즈를 동적으로 생성하는 서버 측 프로그램 혹은 그 사양을 말하며, 흔히 "서블릿"이라 불린다. 자바 서블릿은 웹 서버의 성능을 향상하기 위해 사용되는 자바 클래스의 일종이다. 서블릿은 JSP와 비슷한 점이 있지만, JSP가 HTML 문서 안에 Java 코드를 포함하고 있는 반면, 서블릿은 자바 코드 안에 HTML을 포함하고 있다는 차이점이 있다.

  

### Servlet Process

---

![[Untitled 5 18.png|Untitled 5 18.png]]

  

### Servlet API

---

![[Untitled 6 15.png|Untitled 6 15.png]]

  

### Servlet's Life-Cycle

---

Servlet class는 javaSE에서의 class와는 다르게 main method가 없다. 즉 객체의 생성부터 사용(method call)의 주체가 사용자가 아닌 Servlet Container에게 있다.

Client가 요청을 하게 되면 Servlet Container는 Servlet객체를 생성(한번만)하고, 초기화(한번만) 하며 요청에 대한 처리(요청시마다 반복)를 하게 된다. 또한 Servlet객체가 필요 없게 되면 제거하는 일까지 Container가 담당하게 된다.

![[Untitled 7 13.png|Untitled 7 13.png]]

  

### Servlet Parameter

---

![[Untitled 8 11.png|Untitled 8 11.png]]

  

### URL

---

![[Untitled 9 11.png|Untitled 9 11.png]]