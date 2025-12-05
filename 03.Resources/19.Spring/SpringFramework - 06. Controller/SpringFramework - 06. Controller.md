---
type: Spring
archive: false
---
### Controller

---

- @Controller와 @RequestMapping선언
    
    method 단위의 mapping이 가능
    
    DefaultAnnotationHandlerMapping과 AnnotationHandlerAdapter를 사용함
    
    - Spring 3.0 부터는 기본 설정이므로 별도의 추가 없이 사용 가능
    

![[Untitled 29.png|Untitled 29.png]]

  

- Controller Class는 Client의 요청을 처리
- @Controller 선언
    
    Class 타입에 적용
    
    Spring 3.0 부터는 @Controller 사용을 권장
    
      
    
- Controller Class 를 <bean>에 등록
    
    ![[Untitled 1 9.png|Untitled 1 9.png]]
    

  

- @Requestmapping 선언
    
    요청 URL mapping 정보를 설정
    
    클래스타입과 메소드에 설정 가능
    
    ![[Untitled 2 8.png|Untitled 2 8.png]]
    
      
    
- Controller method의 HTTP method에 한정
    
    같은 URL 요청에 대하여 HTTP method(GET, POST) 에따라 서로 다른 메소드를 mapping할 수 있음.
    
    ![[Untitled 3 8.png|Untitled 3 8.png]]
    
      
    
- 아래의 Controller에서 @RequestMapping annotation을 설정하지 않으면? HTTP ERROR 404
    
    ![[Untitled 4 6.png|Untitled 4 6.png]]
    
      
    
- Controller method의 parameter type
    
    Controller method의 parameter로 다양한 Object를 받을 수 있음.
    
    ![[Untitled 5 5.png|Untitled 5 5.png]]
    
      
    
- Controller emthod의 parameter type
    
    Controller method의 parameter로 다양한 Object를 받을 수 있음.
    
    ![[Untitled 6 4.png|Untitled 6 4.png]]
    
      
    
- @RequestParam annotation을 이용항 parameter mapping
    
    ![[Untitled 7 3.png|Untitled 7 3.png]]
    
      
    
- HTML form과 Command Object(DTO, VO..).
    
    SpringMVC는 form에 입력한 data를 JavaBean 객체를 이용해서 전송할 수 있음.
    
    ![[Untitled 8 3.png|Untitled 8 3.png]]
    
      
    
- Cammand 객체를 List로 받기
    
    ![[Untitled 9 3.png|Untitled 9 3.png]]
    
      
    
- View에서 Command 객체에 접근
    
    Command 객체는 자동으로 반환되는 Model에 추가됨.
    
    Controller의 @RequestMapping annotation method에서 전달받은 Command 객체에 접근
    
    ![[Untitled 10 3.png|Untitled 10 3.png]]
    
      
    

![[Untitled 11 2.png|Untitled 11 2.png]]

  

- @RequestBody parameter type
    
    ![[Untitled 12 2.png|Untitled 12 2.png]]
    
      
    
- Servlet API 사용
    
    HttpSession의 생성을 직접 제어해야 하는 경우
    
    Controller가 Cookie를 생성해야 하는 경우
    
    Servlet API를 선호하는 경우
    
    ![[Untitled 13 2.png|Untitled 13 2.png]]
    
      
    
- Controller Class에서 method의 return type 종류
    
    ![[Untitled 14 2.png|Untitled 14 2.png]]