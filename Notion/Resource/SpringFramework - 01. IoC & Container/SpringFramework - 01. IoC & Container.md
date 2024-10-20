---
type: Spring
archive: false
---
## IoC & Container

### IoC (Inversion of Control, 제어의 역행)

---

IoC/DI

객체지향 언어에서 Object 간의 연결 관계를 런타임에 결정

객체 간의 관계가 느슨하게 연결됨(loose coupling)

IoC의 구현 방법 중 하나가 DI

  

IoC 유형

---

![[Untitled 39.png|Untitled 39.png]]

  

- Dependency Lookup
    
    컨테이너가 lookup contenxt를 통해서 필요한 Resource나 Object를 얻는 방식.
    
    JNDI 이외의 방법을 사용한다면 JNDI 관련 코드를 오브젝트 내에서 일일이 변경해 주어야 함
    
    Lookup 한 Object를 필요한 타입으로 Casting 해 주어야 함.
    
    Naming Exception을 처리하기 위한 로직이 필요
    
- Dependency Injection
    
    Object에 lookup 코드를 사용하지 않고 컨테이너가 직접 의존 구조를 Object에 설정 할 수 있도록 지정해 주는 방식
    
    Object가 컨테이너의 조재 여부를 알 필요가 없음
    
    Lookup 관련된 코드들이 Object 내에서 사라짐
    
    Setter Injection과 Constructor Inject
    
      
    

### Container

---

- Container란?
    
    객체의 생성, 사용 소멸에 해당하는 라이프 사이클을 담당
    
    라이프사이클을 기본으로 애플리케이션 사용에 필요한 주요 기능을 제공
    
- Container 기능
    
    라이프사이클 관리
    
    Dependency 객체 제공
    
    Thread 관리
    
    기타 애플리케이션 실행에 필요한 환경
    
- Container 필요성
    
    비즈니스 로직 외에 부가적인 기능들에 대해서는 독립적으로 관리되도록 하기 위함
    
    서비스 look up이나 Configuration에 대한 일관성을 갖기 위함
    
    서비스 객체를 사용하기 위해 각각 Factory 또는 Singleton 패턴을 직접 구현하지 않아도 됨
    
- IoC Container
    
    오브젝트의 생성과 관계설정, 사용, 제거등의 작업을 애플리케이션 코드 대신 독립된 컨테이너가 담당
    
    컨테이너가 코드 대신 오브젝트에 대한 제어권을 갖고 있어 IoC라고 부름
    
    이런 이유로, 스프링 컨테이너를 IoC컨테이너라고 부르기도 함.
    
    스프링에서 IoC를 담당하는 컨테이너에는 BeanFactory, ApplicatoinContext가 있음.
    
- Spring DI Container
    
    Spring DI Container가 관리하는 객체를 빈(Bean)이라 하고, 이 빈들의 생명주기(Life-Cycle)를 관리하는 의미로 빈팩토리(BeanFactory)라 한다.
    
    Bean Factory에 여러 가지 컨테이너 기능을 추가하여 ApplicationContext라 한다.
    
    ![[Untitled 1 17.png|Untitled 1 17.png]]
    
    ![[Untitled 2 16.png|Untitled 2 16.png]]
    
      
    

### IoC 개념

---

객체 제어 방식

- 기존 : 필요한 위치에서 개발자가 필요한 객체 생성 로직 구현
- IoC : 객체 생성을 Container 에게 위임하여 처리

  

IoC 사용에 따른 장점

- 객체 간의 결합도를 떨어뜨릴 수 있음 (loose coupling)

  

객체간 결합도가 높으면?

- 해당 클래스가 유지보수 될때 그 클래스와 결합된 다른 클래스도 같이 유지 보수 되어야 할 가능성이 높음.

  

객체간 강한 결합

- 클래스 호출 방식
- 클래스 내에 선언과 구현이 모두 되어 있기 때문에 다양한 형태로 변화가 불가능
    
    ![[Untitled 3 15.png|Untitled 3 15.png]]
    
      
    

객체 간의 강한 결합을 다형성을 통해 결합도를 낮춤.

- 인터페이스 호출 방식
- 구현 클래스 교체가 용이하여 당야한 형태로 변화가능
- 하지만 인터페이스 교체 시 호출 클래스도 수정해야 함.
    
    ![[Untitled 4 12.png|Untitled 4 12.png]]
    

  

객체 간의 강한 결합을 Factory를 통해 결합도를 낮춤

- 팩토리 호출 방식
- 팩토리 방식은 팩토리가 구현 클래스를 생성하므로 클래스는 픽토리를 호출
- 인터페이스 변경 시 팩토리만 수정하면 됨. 호출 클래스에는 영향을 미치지 않음
- 하지만 클래스에 팩토리를 호출하는 소스가 들어가야함. 그것 자체가 팩토리에 의존함을 의미한다.
    
    ![[Untitled 5 11.png|Untitled 5 11.png]]
    
      
    

객체 간의 강한 결합을 Assembler를 통해 결합도를 낮춤

- IoC 호출 방식
- 팩토리 패턴의 장점을 더하여 어떠한 겻에도 의존하지 않은 형태가 됨.
- 실행시점(Runtime)에 클래스 간의 관계가 형성이 됨
    
    ![[Untitled 6 9.png|Untitled 6 9.png]]
    
      
    

### Spring DI 용어 정리

---

- 빈(Bean)
    
    스프링이 IoC 방식으로 관리하는 오브젝트를 말한다.
    
    스프링이 직접 그 생성과 제어를 담당하는 오브젝트만을 Bean이라고 부른다.
    
- 빈 팩토리(BeanFactory)
    
    스프링이 IoC를 담당하는 핵심 컨테이너
    
    Bean을 등록, 생성, 조회, 반환하는 기능을 담당
    
    일반적으로 BeanFactory를 바로 사용하지 않고 이를 확장한 ApplicationContext를 이용한다.
    
- 애플리케이션 컨텍스트(ApplicationContext)
    
    BeanFactory를 확장한 IoC 컨테이너이다.
    
    Bean을 등록하고 관리하는 기본적인 기능은 BeanFactory와 동일하다
    
    스프링이 제공하는 가종 부가 서비스를 추가로 제공한다.
    
    BeanFactory라고 부를 때는 주로 빈의 생성과 제어의 관점에서 이야기하는 것이고, 애플리케이션 컨텍스트라고 할 때는 스프링이 제공하는 애플리케이션 지원 기능을 모두 포함해서 이야기하는 것이라고 보면 된다.
    
- 설정 정보 / 설정 메타 정보(configuration metadata)
    
    스프링의 설정정보란 ApplicationContext 또는 BeanFactory가 IoC를 적용하기 위해 사용하는 메타 정보를 말한다. 이는 구성 정보 내지는 형상정보라는 의미이다.
    
    설정 정보는 IoC 컨테이너에 의해 관리되는 Bean객체를 생성하고 구성할 때 사용됨.
    
- 스프링 프레임워크
    
    스프링 프레임워크는 IoC컨테이너, ApplicationContext를 포함해서 스프링이 제공하는 모든 기능을 통틀어 말할 때 주로 사용된다.
    
      
    

### Spring Container

---

![[Untitled 7 8.png|Untitled 7 8.png]]