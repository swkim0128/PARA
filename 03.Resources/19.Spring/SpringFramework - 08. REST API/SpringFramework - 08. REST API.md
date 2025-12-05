---
type: Spring
archive: false
---
## REST(Representational State Transfer) API

### OPEN API?? (Application Programming Interface)

---

OPEN API는 프로그래밍에서 사용할 수 있는 개방되어 있는 상태의 interface

naver, kakao 등 포털 서비스 사이트나 통계청, 기상청, 우체국 등과 같은 관공서, 공공 데이터 포털이 가지고 있는 데이터를 외부 응용 프로그램에서 사용할 수 있도록 OPEN API를 제공하고 있다.

OPEN API와 함께 거론되는 기술이 REST이며, 대부분의 OPEN API는 REST방식으로 지원.

  

### REST(Representational State Transfer)

---

2000년도 로이 필딩(Roy Fielding)의 박사학위 논문에 최초로 소개

REST는 Representational State Transfer의 약어로 하나의 URI는 하나의 고유한 리소스 (Resource)를 대표한도록 설계된다는 개념에 전송박식을 결합해서 원하는 작업을 지정한다.

![[Untitled 44.png|Untitled 44.png]]

웹의 장점을 최대한 활용할 수 있는 아키텍처(설계구조)로써 REST를 발표

HTTP URI를 통해 제어할 자원(Resource)를 명시하고, HTTP Method(GET, POST, PUT, DELETE)을 통해 해당 자원(Resource)를 제어하는 명령을 내리는 방식의 아키텍처

  

### REST 구성

---

- 자원 (Resource) - URI
- 행위 (verb) - HTTP Method
- 표현 (Representations)

잘 표현된 HTTP URI로 리소스를 정의하고 HTTP method로 리소스에 대한 행위를 정의한다.

리소스는 JSON, XML과 같은 여러 가지 언어로 표현할 수 있다.

  

### 기존 Service와 REST Service

---

- 기존 Service : 요청에 대한 처리를 한 후 가공된 data를 이용하여 특정 플랫폼에 적합한 형태의 View로 만들어서 반환
- REST Service : data 처리만 한다거나, 처리 후 반환될 data가 있다면 JSON이나 XML 형식으로 전달. View에 대해서는 신경 쓸 필요가 없다. >> 이러한 이유로 Open Api에서 많이 사용

![[Untitled 1 22.png|Untitled 1 22.png]]

  

### REST

---

기존의 전송방식과는 달리 서버는 요청으로 받은 리소스에 대해 순수한 데이터를 전송한다.

기존의 GET/POST 외에 PUT, DELETE 방식을 사용하여 리소스에 대한 CRUD 처리를 할 수 있다.

HTTP URI을 통해 제어할 자원(Resource)을 명시하고, HTTP METHOD(GET/POST/PUT/DELETE)를 통해 해당 자원(Resource)를 제어하는 명령을 내리는 방식의 Architecture이다.

가장 큰 단점은 딱 정해진 표준이 없어 '다들 이렇게 쓰더라' 정도의 암묵적인 표준만 정해져 있다.

- 하이픈(-)은 사용 가능하지만 언더바(_)는 사용하지 않는다.
- 특별한 경우를 제외하고 대문자 사용은 하지 않는다.(대소문자 구분을 하기 때문)
- URI 마지막에 슬래시(/)를 사용하지 않는다.
- 슬래시(/)로 계층 관계를 나타낸다.
- 확장자가 포함된 파일 이름을 직접 포함시키지 않는다.
- URI는 명사를 사용한다.

  

기존의 웹 접근 방식과 REST API 방식의 차이점

![[Untitled 2 21.png|Untitled 2 21.png]]

  

기존의 블로그등은 GET과 POST 만으로 자원에 대한 CRUD를 처리하며, URI는 액션을 나타냈다.

REST로 변경할 경우 4가지 method를 모두 사용하여 CRUD를 처리하며, URI는 제어하려는 자원을 나타낸다.

  

### REST API 설정

---

- Jackson library
    
    ![[Untitled 3 20.png|Untitled 3 20.png]]
    
      
    

### REST 관련 Annotation

---

![[Untitled 4 16.png|Untitled 4 16.png]]

  

### REST API 예

---

- list.jsp
    
    ![[Untitled 5 14.png|Untitled 5 14.png]]
    
      
    
- AdminController.java
    
    ![[Untitled 6 11.png|Untitled 6 11.png]]
    

  

![[Untitled 7 9.png|Untitled 7 9.png]]

![[Untitled 8 7.png|Untitled 8 7.png]]

![[Untitled 9 7.png|Untitled 9 7.png]]

![[Untitled 10 6.png|Untitled 10 6.png]]

![[Untitled 11 5.png|Untitled 11 5.png]]

![[Untitled 12 5.png|Untitled 12 5.png]]

![[Untitled 13 5.png|Untitled 13 5.png]]

![[Untitled 14 5.png|Untitled 14 5.png]]

![[Untitled 15 4.png|Untitled 15 4.png]]

![[Untitled 16 4.png|Untitled 16 4.png]]