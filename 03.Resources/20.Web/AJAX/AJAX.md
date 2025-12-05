---
type: JavaScript
archive: false
---
### 소개

---

Ajax(Asynchronous JavaScript and XML)는 언어나 프레임워크가 아닌 구현하는 방식을 의미.

Ajax는 웹에서 화면을 갱신하지 않고 데이터를 서버로부터 가져와 처리하는 방법을 의미.

JavaScript의 XMLHttpRequest(XHR) 객체로 데이터를 전달하고 비동기 방식으로 결과를 조회.

화면 갱신이 없으므로 사용자 입장에서는 편리하지만, 동적으로 DOM을 구성해야 하므로 구현이 복잡.

  

일반 요청에 대한 응답.

- data를 입력 후 event 발생.
- Ajax를 적용하지 않은 요청은 서버에서 data를 이용하여 logic 처리.
- logic 처리에 대한 결과에 따라 응답 page를 생성하고 client에 전송(화면 전환이 일어 남)

  

Ajax 요청에 대한 응답

- data를 입력 후 event 발생
- Ajax를 적용하면 event 발생 시 서버에서 요청을 처리한 후 Text, XML 또는 JSON으로 응답
- client(Browser)에서는 이 응답 data를 이용하여 화면 전환없이 현재 페이지에서 동적으로 화면을 재구성.

  

### 서버와 클라이언트의 상호작용.

---

웹 화면을 구성하는 방식은 서버 중심의 상호 작용 방식과 클라이언트 중심의 상호작용 방시으로 구분.

서버 중심의 개발방식은 화면 구성이 서버에서 이루어 진다. (프리젠테이션 영역의 JSP나 PHP, ASP 등)

클라이언트 중심의 개발 방식은 클라이언트(웹 브라우저)에서 화면을 구성한다.(주로 JavaScript)

Ajax는 클라이언트 중심의 개발방식이며 비동기 요청보다는 동적 화면 구성이 관건임.

![[Untitled 56.png|Untitled 56.png]]

  

### JavaScript Ajax

---

XMLHttpRequest는 자바스크립트가 Ajax 방식으로 통신할 때 사용하는 객체.

XMLHttpRequest 객체는 Ajax 통신 시 전송방식, 경로, 서버로 전송할 data등 전송정보를 담는 역할.

실제 서버와의 통신은 브라우저의 Ajax엔진에서 수행.

직접 자바스크립트로 Ajax를 프로그래밍할 경우 브라우저 별로 통신방식이 달라 코드가 복잡해 진다.

  

JavaScript AJAX 적용 예

![[Untitled 1 34.png|Untitled 1 34.png]]

![[Untitled 2 33.png|Untitled 2 33.png]]

  

### jQuery AJAX 함수

---

$.ajax()

$.ajax() 함수는 jQuery에서 Ajax 기능을 제공하는 가장 기본적인 함수.

다른 함수들에 비하여 옵션을 다양하게 지정할 수 있으며 실무에서 가장 많이 사용.

함수의 옵션은 다양하지만 대부분 자동으로 지정하므로 생략 가능.

![[Untitled 3 32.png|Untitled 3 32.png]]

  

Server의 시간을 출력하는 예제

![[Untitled 4 28.png|Untitled 4 28.png]]

  

$.get(), $.post()

$.get(), $.post() 함수는 $.ajax() 의 옵션 속성 중 type 옵션이 미리 지정된 함수.

지정된 HTTP Method로 Ajax 통신을 하며 get()은 GET 방식을, post()는 POST 방식을 사용.

$.xxx(url, function (result, textStatus, jqXHR){});

$.xxx(url, data, function (result, textStatus, jqXHR){});

![[Untitled 5 25.png|Untitled 5 25.png]]

  

* GET 방식과 POST방식

GET 방식의 특징

- URL에 변수(데이터)를 포함시켜 요청한다.
- 데이터를 Header(헤더)에 포함하여 전송한다.
- URL에 데이터가 노출되어 보안에 취약하다.
- 전송하는 길이에 제한이 있다.
- 캐싱할 수 있다.

POST 방식의 특징

- URL에 변수(데이터)를 노출하지 않고 요청한다.
- 데이터를 Body에 포함시킨다.
- URL에 데이터가 노출되지 않아서 기본 보안은 되어있다.
- 전송하는 길이에 제한이 없다.
- 캐싱할 수 없다.

  

$(selector).load().

$.load() 함수는 서버로부터 내용을 조회하여, 선택자를 통해 탐색한 DOM 객체에 동적으로 삽입.

첫 번째 인자는 필수 값으로 HTML을 조회할 서버 URL을 지정.

두 번째 인자는 요청 시 서버에 전달할 데이터를 지정.

세 번째 인자는 서버와 통신을 완료한 후에 수행할 콜백함수를 지정.

![[Untitled 6 22.png|Untitled 6 22.png]]

  

### 데이터 전송 형식

---

server와 client는 주고 받을 data의 형식을 맞춰야 함.

대표적인 data형식은 CSV, XML, JSON 등이 있음.

  

1. CSV(Comma Separated Values)
    
    각 항목을 쉼표(,)로 구분해 데이터를 표현하는 방법.
    
    다른 두 형식에 비해 굉장히 짧다. 많은 양의 데이터 전송 시 유리.
    
    단 각각의 데이터가 어떤 내용인지 파악하기 어렵다. (서버와 클라이언트가 완벽히 데이터 구조를 공유할 경우 가능)
    
    ![[Untitled 7 19.png|Untitled 7 19.png]]
    
    ![[Untitled 8 17.png|Untitled 8 17.png]]
    
      
    
2. XML(eXtensible Markup Language)
    
    xml은 tag로 data를 표현함.
    
    tag를 보면 각 data가 무엇을 의미하는지 파악 가능.
    
    tag에 사용자 정의 속성을 넣을 수 있으므로 복잡한 data 전달 가능.
    
    ![[Untitled 9 16.png|Untitled 9 16.png]]
    
    ![[Untitled 10 14.png|Untitled 10 14.png]]
    
      
    

### 데이터 전송 형식

---

1. JSON (JavaScript Object Notation).
    
    CSV와 XML의 단점을 극복한 형식
    
    JavaScript에서 사용하는 객체의 형식으로 data를 표현.
    
    Ajax 사용시 거의 표준으로 사용되는 data표현 방식.
    
    ![[Untitled 11 12.png|Untitled 11 12.png]]
    
    ![[Untitled 12 11.png|Untitled 12 11.png]]
    
      
    

### Event 관리(전역함수)

---

Ajax는 서버와 통신하는 과정이 웹 브라우저 내부에서 이루어지므로 사용자가 진행상황을 알기 어렵다.

Ajax 저역함수를 사용하여 Ajax 처리 중에 진행 상태를 보여주는 기능을 구현할 수 있다.

jQuery는 Ajax 처리가 이루어지는 각 단계 별로 전역함수를 호출.

단, jQuery의 전역함수는 $.ajaxSetup() 함수에 global 프로퍼티 설정이 true인 경우에만 수행됨. (디폴트 : true)

![[Untitled 13 11.png|Untitled 13 11.png]]

  

- 로딩 화면 구현

![[Untitled 14 10.png|Untitled 14 10.png]]