---
type: Spring
archive: false
---
### MVC(Model-View-Controller) Pattern

---

- Model
    
    어플리케이션 상태의 캡슐화
    
    상태 쿼리에 대한 응답
    
    어플리케이션의 기능 표현
    
    변경을 view에 통지
    
- View
    
    모델을 화면에 시작적으로 표현
    
    모델에게 업데이트 요청
    
    사용자의 입력을 컨트롤러에 전달
    
    컨트롤러가 view를 선택하도록 허용
    
- Controller
    
    어플리케이션의 행위 정의
    
    사용자 액션을 모델 업데이트와 mapping
    
    응답에 대한 view 선택
    
      
    

어플리케이션의 확장을 위해 Model, View, Controller 세가지 영역으로 분리

컴포넌트의 변경이 다른 영역 컴포넌트에 영향을 미치지 않음(유지보수 용이)

컴포넌트 간의 결합성이 낮아 프로그램 수정이 용이(확장성이 뛰어남)

  

- 장점
    
    화면과 비즈니스 로직을 분리해서 작업 가능
    
    영역별 개발로 인하여 확장성이 뛰어남
    
    표준화된 코드를 사용하므로 공동작업이 용이하고 유지보수성이 좋음
    
      
    
- 단점
    
    개발과정이 복잡해 초기 개발 속도가 늦음
    
    초보자가 이해하고 개발하기에 다소 어려움
    
      
    

### Model2 (Web MVC) 요청 흐름

---

![[Untitled 65.png|Untitled 65.png]]

  

### Spring MVC

---

- 특징
    
    Spring은 DI나 AOP같은 기능 뿐만 아니라, Servlet 기반의 WEB 개발을 위한 MVC Framework를 제공
    
    Spring MVC는 Model2 Architecture와 Front Controller Pattern을 Framework차원에서 제공
    
    Spring MVC Framework는 Spring을 기반으로 하고 있기 때문에 Spring이 제공하는 Transaction 처리나 DI 및 AOP 등을 손쉽게 사용
    
      
    
- Spring MVC 구성요소
    
    ![[Untitled 1 42.png|Untitled 1 42.png]]
    
    ![[Untitled 2 39.png|Untitled 2 39.png]]
    
      
    

### Spring MVC 요청 흐름

---

![[Untitled 3 38.png|Untitled 3 38.png]]

  

### Spring MVC

---

![[Untitled 4 34.png|Untitled 4 34.png]]

![[Untitled 5 30.png|Untitled 5 30.png]]

  

### Spring MVC 구현

---

- Spring MVC를 이용한 Application 구현 Step
    
    web.xml에 DispatcherServlet 등록 및 Spring 설정파일 등록
    
    설정 파일에 HandlerMapping 설정
    
    Controller 구현 및 Context 설정 파일(servlet-context.xml)에 등록
    
    Controller와 JSP의 연결을 위해 View Resolver 설정
    
    JSP 코드 작성
    
      
    
- Controller 작성
    
    좋은 디자인은 Controller가 많은 일을 하지 않고 Service에 처리를 위임
    
    ![[Untitled 6 27.png|Untitled 6 27.png]]
    
      
    
- web.xml - DispatcherServlet 설정
    
    ![[Untitled 7 24.png|Untitled 7 24.png]]
    
    ![[Untitled 8 21.png|Untitled 8 21.png]]
    
    ![[Untitled 9 20.png|Untitled 9 20.png]]
    
      
    
- web.xml - 최상위 Root ContextLoader 설정
    
    ![[Untitled 10 18.png|Untitled 10 18.png]]
    
      
    
- Application Context 분리
    
    ![[Untitled 11 15.png|Untitled 11 15.png]]
    

![[Untitled 12 14.png|Untitled 12 14.png]]

![[Untitled 13 13.png|Untitled 13 13.png]]

  

### Spring Web Application의 동작 원리

---

![[Untitled 14 12.png|Untitled 14 12.png]]

  

실행 순서

1. 웹 어플리케이션이 실행되면 Tomcat(WAS)에 의해 web.xml이 로딩
2. web.xml에 등록되어 있는 ContextLoaderListener(Java Class)가 생성. ContextLoaderListener class는 ServletContextListener interface를 구현하고 있으며, ApplicationContext를 생성하는 역할을 수행
3. 생성된 ContextLoaderListener는 root-context.xml을 loading
4. root-context.xml에 등록되어 있는 Spring Container가 구동.. 이 때 개발자가 작성한 Business Logic(Service)에 대한 부분과 Database Logic(DAO), VO 객체들이 생성
5. Client로 부터 요청(reqeust)가 들어옴
6. DispatcherServlet(Servlet)이 생성. DispatcherServlet은 FrontController의 역할을 수행  
    Client로부터 요청 온 메시지를 분석하여 알맞은 PageController에게 전달하고 응답을 받아 요청에 따른 응답을 어떻게 할 지 결정. 실질적인 작업은 PageController에서 이루어 진다.  
    이러한 클래스들을 HandlerMapping, ViewResolver Class라고 함.  
    
7. DispatcherServlet은 servlet-context.xml을 loading
8. 두 번째 Spring Container가 구동되며 응답에 맞는 PageController들이 동작, 이 때 첫 번째 Spring Container가 구동되면서 생성된 DAO, VO, Service 클래스들과 협업하여 알맞은 작업을 처리