---
type: Spring
archive: false
---
### JSTL(Jsp Standard Tag Library)

---

자바서버 페이지 표준 태그 라이브러리(JavaServer Pages Standard Tag Library, 약칭 JSTL)은 Java EE 기반의 웹 애플리케이션 개발 플랫폼을 위한 컴포넌트 모음이다. JSTL은 XML 데이터 처리와 조건문, 반복문, 국제화와 지역화 같은 일을 처리하기 위한 JSP 태그 라이브러리를 추가하여 JSP 사양을 확장했다. JSTL은 JSR 52로서 JCP 하에서 개발되었으며, 2006년 5월 8일에 JSTL 1.2가 출시 되었다.

JSTL은 JSP 페이지 내에서 자바 코드를 바로 사용하지 않고 로직을 내장하는 효율적인 방법을 제공한다. 표준화된 태그 셋을 사용하여 자바 코드가 들락거리는 것보다 더 코드의 유지보수와 응용 소프트웨어 코드와 사용자 인터페이스 간의 관심사의 분리로 이어지게 한다.

  

- custom tag : 개발자가 직접 태그를 작성할 수 있는 기능을 제공.
- custom tag 중에서 많이 사용되는 것들을 모아서 JSTL이라는 규약을 만듦.
- 논리적인 판단, 반복문의 처리, 데이터베이스 등의 처리를 할 수 있다.
- JSP 2.1 ~ JSP 2.2와 호환되는 JSTL 버전은 1.2이다.
- JSTL은 JSP 페이지에서 스크립트 트릿을 사용하지 않고 액션을 통해 간단하게 처리할 수 있는 방법을 제공.
- JSTL에는 다양한 액션이 있으며, EL과 함께 사용하여 코드를 간결하게 작성할 수 있다.
- [https://mvnrepository.com/artifact/javax.servlet/jstl](https://mvnrepository.com/artifact/javax.servlet/jstl) >> jstl-1.2.jar download

  

### JSTL Tag

---

directive 선언 형식 : <%@ taglib prefix="prefix" uri="uri" %>

![[Untitled 42.png|Untitled 42.png]]

  

### JSTL - core tag.

---

선언 : <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

![[Untitled 1 20.png|Untitled 1 20.png]]

  

### 변수 선언 : <c:set>

---

<c:set> 액션은 변수나 특정 객체의 프로퍼티에 값을 할당할 때 사용.

value 속성의 값이나 액션의 Body content로 값을 설정.

var 속성은 변수를 나타내며, 변수의 생존 범위는 scope 속성으로 설정. (디폴트는 page)

특정 객체의 프로퍼티에 값을 할당할 때는 target 속성에 객체를 설정하고 property에 프로퍼티명을 설정.

![[Untitled 2 19.png|Untitled 2 19.png]]

  

### 예외 : <c:catch>

---

기본적으로 JSP 페이지는 예외가 발생하면 지정된 오류페이지를 통해 처리한다.

<c:catch> 액션은 JSP 페이지에서 예외가 발생할 만한 코들르 오류 페이지로 넘기지 않고 직접 처리할 때 사용.

var 속성에는 발생한 예외를 담을 page 생존범위 변수를 지정.

<c:catch>와 <c:if> 액션을 함께 사용하며 Java 코드의 try-catch와 같은 기능을 구현할 수 있다.

![[Untitled 3 18.png|Untitled 3 18.png]]

  

### 조건문 : <c:if>, <c:choose><c:when><c:otherwise>

---

<c:if> 액션은 test 속성에 지정된 표현식을 평가하여 결과가 true인 경우 액션에 Body 컨텐츠를 수행

<c:if> 액션의 var 속성은 표현식의 평가 결과인 Boolean 값을 담을 변수를 나타내며, 변수의 생존 범위는 scope 속성으로 설정.

<c:choose><c:when><c:otherwise> 액션을 사용하면 if, else if, else 와 같이 처리할 수 있다.

![[Untitled 4 14.png|Untitled 4 14.png]]

  

### 반복문 : <c:forEach>

---

<c:forEach> 액션은 컬렉션에 있는 항목들에 대하여 액션의 Body 컨텐츠를 반복하여 수행.

컬렉션에는 Array, Collection, Map 또는 콤마로 분리된 문자열이 올 수 있다.

var 속성에는 반복에 대한 현재 항목을 다믄ㄴ 변수를 지정하고 items 속성은 반복할 항목들을 갖는 컬렉션을 지정.

varStatus 속성에 지정한 변수를 통해 현재 반복의 상태를 알 수 있다.

![[Untitled 5 13.png|Untitled 5 13.png]]