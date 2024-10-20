---
type: Spring
archive: false
---
### 빈 생성 범위

---

싱글톤 빈 (Signleton Bean)

스프링 빈은 기본적으로 싱글톤으로 만들어짐 그러므로, 컨테이너가 제공하는 모든 빈의 인스턴스는 항상 동일함.

컨테이너가 항상 새로운 인스턴스를 반환하게 만들고 싶을 경우 Scope를 prototype으로 설정해야함.

![[Untitled 46.png|Untitled 46.png]]

  

### 빈 생성 범위 지정

---

![[Untitled 1 24.png|Untitled 1 24.png]]

  

- 스프링 빈 설정 메타 정보
    
    ![[Untitled 2 23.png|Untitled 2 23.png]]
    
      
    

### 스프링 빈 설정 : XML

---

XML 문서 형태로 빈의 설정 메타 정보를 기술

단순하며 사용하기 쉬움. 가장 많이 사용하는 방식

<bean> 태그를 통해 세밀한 제어 가능

![[Untitled 3 22.png|Untitled 3 22.png]]

  

### 스프링 빈 설정 : Annotation

---

어플리케이션의 규모가 커지고 빈의 개수가 많아질 경우 XML 파일을 관하는 것이 번거로움.

빈으로 사용될 클래스에 특별한 annotation을 부여해 주면 자동으로 빈 등록 가능

"오브젝트 빈 스캐너"로 "빈 스캐닝"을 통해 자동 등록

- 빈 스캐너는 기본적으로 클래스 이름을 빈의 아이디로 사용
- 정확히는 클래스 이름의 첫 글자만 소문자로 바꾼 것을 사용

![[Untitled 4 18.png|Untitled 4 18.png]]

  

Annotation으로 빈을 설정한 경우 반드시 component-scan을 설정해야 한다.

![[Untitled 5 16.png|Untitled 5 16.png]]

  

Stereotype annotation 종류

- 빈 자동등록에 사용할 수 있는 annotation
- 빈 자동인식을 위한 annotation이 여러가지인 이유
    - 계층별로 빈의 특성이나 종류를 구분
    - AOP Pointcut 표현식을 사용하면 특정 annotation이 달린 클래스만 설정 가능
    - 특정 게층의 빈에 부가기능을 부여

![[Untitled 6 13.png|Untitled 6 13.png]]

  

### Dependency Injection

---

객체 간의 의존관계를 자신이 아닌 외부의 조립기가 수행

제어의 역행(inversion of Control, IoC)이라는 의미로 사용

DI를 통해 시스템에 있는 각 객체를 조정하는 외부 개체가 객체들에게 생성시에 의존관계를 주어짐

느슨한 결합(loose coupling)의 주요 강점

- 객체는 인터페이스에 의한 의존 관계만을 알고 있으며, 이 의존 관계는 구현 클래스에 대한 차이를 모르는채 서로 다른 구현으로 대체가 가능

  

### 스프링의 DI 지원

---

Spring Container가 DI 조립기를 제공

- 스프링 설정 파일을 통하여 객체 간의 의존 관계를 설정
- Spring Container가 제공하는ㄴ API를 이용해 객체를 사용

  

### Spring 설정 : XML

---

Application에서 사용할 Spring 자원들을 설정하는 파일

Spring Container는 설정 파일에 설정된 내용을 읽어 Application에서 필요한 기능들을 제공

Root tag는 <beans>

파일명은 상관없다.

![[Untitled 7 11.png|Untitled 7 11.png]]

  

- 기본 설정 - 빈 객체 생성 및 주입
    
    주입 할 객체를 설정 파일에 설정
    
    - <bean> : 스프링 컨테이너가 관리할 Bean 객체를 설정
    
    기본 속성
    
    - name : 주입 받을 곳에서 호출 할 이름 설정
    - id : 주입 받을 곳에서 호출 할 이름 설정(유일 값)
    - class : 주입할 객체의 클래스
    - factory-method : Singleton 패턴트로 작성된 객체의 Factory 메소드 호출
    
    ![[Untitled 8 9.png|Untitled 8 9.png]]
    
      
    
- 기본 설정 - 빈 객체 얻기
    
    설정 파일에 설정한 bean을 Container가 제공하는 주입기 역할의 api를 통해 주입 받는다
    
    ![[Untitled 9 9.png|Untitled 9 9.png]]
    
      
    

### 스프링 빈 의존 관계 설정 - xml

---

Constructor 이용

- 객체 또는 값을 생성자를 통해 주입 받는다.
- <constructor-arg> : <bean>의 하위태그로 설정한 bean 객체 또는 값을 생성자를 통해 주입하도록 설정
    
    설정 방법 : <ref>, <value>와 같은 하위태그를 이용하여 설정하거나 또는 속성을 이용하여 설정
    
    1. 하위태그 이용
        
        객체 주입 시 : <ref bean="bean name" />
        
        문자열(String), primitive data 주입 시 : <value>값</value>
        
        type 속성 : 값은 기본적으로 String으로 처리, 값의 타입을 명시해야 하는 경우 사용  
        ex) <value type="int">10</value>  
        
    2. 속성 이용
        
        객체 주입 시 : <constructor-arg ref="bean anme" />
        
        문자열(String), primitive data 주입 시 : <constructor-arg value="값" />
        

![[Untitled 10 8.png|Untitled 10 8.png]]

![[Untitled 11 7.png|Untitled 11 7.png]]

![[Untitled 12 7.png|Untitled 12 7.png]]

![[Untitled 13 7.png|Untitled 13 7.png]]

![[Untitled 14 7.png|Untitled 14 7.png]]

![[Untitled 15 6.png|Untitled 15 6.png]]

![[Untitled 16 6.png|Untitled 16 6.png]]

  

Property 이용

- property를 통해 객체 또는 값을 주입 받는다.
    
    주의 : setter를 통해서는 한의 값만 받을 수 있다.
    
- <property> : <bean>의 하위태그로 설정한 bean 객체 또는 값을 property를 통해 주입하도록 설정
    
    설정 방법 : <ref>, <value>와 같은 하위태그를 히용하여 설정하거나 또는 속성을 이용하여 설정
    
    1. 하위 태그 이용
        
        객체 주입 시 : <ref bean="bean name" />
        
        문자열(String), primitive data 주입 시 : <value>값</value>
        
    2. 속성 이용 : name - 값을 주입할 property 이름(setter의 이름)
        
        객체 주입 시 : <property name="propertyname" ref="bean name" />
        
        문자열(String), primitive data 주입 시 : <property name="propertyname" value="값" />
        
    3. xml namespace를 이용하여 설정
        
        <bean> 태그의 스키마 설정에 namespace 등록
        
        Bean 설정 시 <bean> 태그의 속성으로 설정
        
        기본 데이터 주입 > p:propertyname="value"
        
        bean 주입 > p:propertyname-ref="bean_id"
        
    
      
    

![[Untitled 17 4.png|Untitled 17 4.png]]

![[Untitled 18 4.png|Untitled 18 4.png]]

![[Untitled 19 4.png|Untitled 19 4.png]]

![[Untitled 20 4.png|Untitled 20 4.png]]

  

Collection 계열 주입

- <constructor-arg> 또는 <property>의 하위 태그로 Collection 값을 설정하는 태그를 이용하여 값 주입 설정
- 설정 태그

![[Untitled 21 3.png|Untitled 21 3.png]]

![[Untitled 22 3.png|Untitled 22 3.png]]

![[Untitled 23 3.png|Untitled 23 3.png]]

![[Untitled 24 3.png|Untitled 24 3.png]]

![[Untitled 25 3.png|Untitled 25 3.png]]

  

### 스프링 빈 의존 관계설정 - annotation

---

- Annotation : 멤버 변수에 직접 정의하는 경우 setter method를 만들지 않아도 됨.

![[Untitled 26 3.png|Untitled 26 3.png]]

![[Untitled 27 2.png|Untitled 27 2.png]]

![[Untitled 28 2.png|Untitled 28 2.png]]

![[Untitled 29 2.png|Untitled 29 2.png]]

![[Untitled 30 2.png|Untitled 30 2.png]]

![[Untitled 31 2.png|Untitled 31 2.png]]

![[Untitled 32 2.png|Untitled 32 2.png]]

  

### 기타 설정

---

- 빈 객체의 생성단위
    
    BeanFactory를 통해 Bean을 요청 시 객체 생성의 범위(단위)를 설정
    
    <bean>의 scope 속성을 이용해 설정
    
    scope의 값
    
    ![[Untitled 33 2.png|Untitled 33 2.png]]
    
      
    
- Factory method로부터 빈(bean) 생성
    
    getBean()으로 호출 시 private 생성자도 호출하여 객체를 생성한다.
    
    그러므로 위의 상황에서 Factory method만 호출해야 객체를 얻을 수 있는 것은 아니다.
    
    ![[Untitled 34 2.png|Untitled 34 2.png]]
    
      
    

### 스프링 빈 생명 주기 (Life Cycle)

---

![[Untitled 35 2.png|Untitled 35 2.png]]

![[Untitled 36 2.png|Untitled 36 2.png]]