---
type: Spring
archive: false
---
### JSP

---

자바 서버 페이지(JavaServer Page, JSP)는 HTML내에 자바 코드를 사입하여 웹 서버에서 동적으로 웹 페이지를 생성하여 웹 브라우저에 돌려주는 언어이다. Java EE 스펙 중 일부로 웹 어플리케이션 서버에서 동작한다.

자바 서버페이지는 실행 시에는 자바 서블릿으로 변환된 후 실행되므로 서블릿과 거의 유사하다고 볼 수 있다. 하지만, 서블릿과는 달리 HTML 표준에 따라 작성되므로 웹 디자인하기 편리하다. 1999년 썬 마이크로시스템즈에 의해 배포되었으며 이와 비슷한 구조로 PHP, ASP, [ASP.NET](http://ASP.NET) 등이 있다.

아파치 스트럿츠나 자카르타 프로젝트의 JSTL 등의 JSP 태그 라이브러리를 사용하는 경우에는 자바 코딩없이 태그만으로 간략히 기술이 가능하므로 생선성을 높일 수 있다.

  

### JSP Process

---

![[Untitled 55.png|Untitled 55.png]]

  

### Declaration

---

JSP 스크립팅 요소(Scripting Element) - 선언

멤버변수 선언이나 메소드를 선언하는 영역.

```Java
<%! 멤버변수와 method 작성 %>
<%!
	String name;

	public void init() {
		name = "test";
	}
%>
```

  

JSP 스크립팅 요소(Scripting Element) - 스크립트릿

Client 요청 시 매번 호출 영역으로, Servlet으로 변환 시 service() method에 해당되는 영역.

request, response에 관련된 코드 구현

```Java
<% java code %>
<%
	for (int dan = 2; dan < 10; dan++) {
		out.println("<tr>");
		String classname = dan % 2 == 0 ? "color1" : "color2";
		for (int i = 1; i < 10; i++) {
			out.println("<td class=\"" + classname + "\">" + dan + 
							" * " + i + " = " + dan * i + "</td>");
		}
		out.println("</tr>");
	}
%>
```

  

JSP 스크립팅 요소(Scripting Element) - 표현식

데이터를 브라우저에 출력할 때 사용

```Java
<%= 문자열 %>
안녕 <%= 문자열 %>!!!
```

![[Untitled 1 33.png|Untitled 1 33.png]]

  

JSP 스크립팅 요소(Scripting Element) - 주석

코드 상에서 부가 설명을 작성.

```Java
<%-- 주석 할 code --%>
<%-- JSP 주석 --%>
<%
/*
Java 주석
*/
%>
```

  

### Directive(JSP 지시자)

---

1. page Directive
    
    컨테이너에게 현재 JSP 페이지를 어떻게 처리할 것인가에 대한 정보를 제공한다.
    
    ![[Untitled 2 32.png|Untitled 2 32.png]]
    
2. include Directive
    
    특정 jsp file을 페이지에 포함.
    
    여러 jsp 페이지에서 반복적으로 사용되는 부분을 jsp file로 만든 후 반복 영역에 include 시켜 반복되는 코드를 줄일 수 있다.
    
    ![[Untitled 3 31.png|Untitled 3 31.png]]
    
3. taglib Directive
    
    JSTL 또는 사용자에 의해서 만든 커스텀 태그(custom tag)를 이용할 때 사용되며
    
    JSP 페이지 내에 불필요한 자바코드를 줄일 수 있다.
    
    ![[Untitled 4 27.png|Untitled 4 27.png]]
    
      
    

### Directive - page

---

![[Untitled 5 24.png|Untitled 5 24.png]]

![[Untitled 6 21.png|Untitled 6 21.png]]

  

### 기본객체

---

![[Untitled 7 18.png|Untitled 7 18.png]]

![[Untitled 8 16.png|Untitled 8 16.png]]

  

### 기본객체 Scope

---

![[Untitled 9 15.png|Untitled 9 15.png]]

![[Untitled 10 13.png|Untitled 10 13.png]]

  

### Web Page 이동

---

![[Untitled 11 11.png|Untitled 11 11.png]]