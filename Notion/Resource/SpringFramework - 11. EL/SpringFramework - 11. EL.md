---
type: Spring
archive: false
---
### EL(Expression Language)

---

EL은 표현을 위한 언어로 JSP 스크립트의 표현식을 대신하여속성 값을 쉽게 출력하도록 고안된 language이다.

즉 표현식 (<%=%>)를 대체할 수 있다.

EL 표현식에서 도트 연산자 왼쪽은 반드시 [java.util.Map](http://java.util.Map) 객체 또는 Java Bean객체여야 한다.

EL 표현식에서 도트 연산자 오른쪽은 반드시 맵의 키이거나 Bean 프로퍼티여야 한다.

EL에서 제공하는 기능.

- JSP의 네가지 기본 객체가 제공하는 영역의 속성 사용.
- 자바 클래스 메소드 호출 기능.
- 표현 언어만의 기본 객체 제공
- 수치, 관계, 논리 연산 제공

  

### EL 문법

---

![[Untitled 52.png|Untitled 52.png]]

  

### EL 문법 : [] 연산자

---

EL에는 Dot 표기법 외에 [] 연산자를 사용하여 객체의 값에 접근할 수 있다.

[] 연산자 안의 값이 문자열인 경우, 이것은 맵의 키가 될 수도 있고, Bean 프로퍼티나 리스트 및 배열의 인텍스가 될 수 있다.

배열과 리스트인 경우, 문자로 된 인덱스 값은 숫자로 변경하여 처리합니다.

![[Untitled 1 30.png|Untitled 1 30.png]]

  

### EL 내장 객체

---

![[Untitled 2 29.png|Untitled 2 29.png]]

  

EL 내장객체는 JSP 페이지의 EL 표현식에서 사용할 수 있는 객체

![[Untitled 3 28.png|Untitled 3 28.png]]

  

### EL 사용

---

pageContext를 제외한 모든 EL 내장 객체는 Map이다.

그러므로 key와 value의 쌍으로 값을 저장하고 있다.

기본 문법

![[Untitled 4 24.png|Untitled 4 24.png]]

  

### EL에서 객체 접근

---

request.setAttribute("userinfo", "안효인");

1. ${requestScope.userinfo}
2. ${pageContext.request.userinfo}, ${userinfo}
    
    > property이름만 사용 할 경우 자동으로 pageScope > requestScope > sessionScope > applicationScope 순으로 객체를 찾음.
    

url?name=안효인&fruit=사과&fruit=바나나

1. ${param.name}
2. ${paramValues.fruit[0]}. ${paramValues.fruit[1]}

![[Untitled 5 22.png|Untitled 5 22.png]]

  

${cookie.id.value}

1. Cookie가 null이라면 null return.
2. null이 아니라면 id를 검사 후 null이라면 null return.
3. null이 아니라면 value값 검사.
    
    ✲ EL은 값이 null이라도 null을 출력하지 않는다. (공백)
    

![[Untitled 6 19.png|Untitled 6 19.png]]

  

### EL Operator(연산자).

---

![[Untitled 7 16.png|Untitled 7 16.png]]

  

### EL에서 객체 method 호출.

---

![[Untitled 8 14.png|Untitled 8 14.png]]