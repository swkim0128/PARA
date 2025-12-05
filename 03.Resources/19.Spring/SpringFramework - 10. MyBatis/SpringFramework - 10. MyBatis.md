---
type: Spring
archive: false
---
### MyBatis 개요와 특징

---

- MyBatis는 Java Object와 SQL 문 상이의 자동 Mapping 기능을 지원하는 ORM Framework.
    
    https://blog.mybatis.org
    
    MyBatis는 SQL을 별도의 파일로 분리해서 처리
    
    Object - SQL 사이의 parameter mapping작업을 자동으로 해줌
    
    MyBatis는 Hibernate나 JPA(Java Persistence API)처럼 새로운 DB 프로그래밍 패러다임을 익혀야 하는 부담이 없이, 개발자가 익숙한 SQL을 그래로 이용하면서 JDBC 코드 작성의 불편함을 제거해 주고, 도메인 객체나 VO 객체를 중심으로 개발이 가능
    
      
    
- MyBatis 특징
    
    쉬운 접근성과 코드의 간결함  
    - 가장 간단한 persistence framework  
    - XML 형태로 서술된 JDBC 코드라 생각해도 될 만큼 JDBC의 모든 기능을 MyBatis가 대부분 제공  
    - 복잡한 JDBC 코드를 걷어내며 깔끔한 소스코드를 유지  
    - 수동적인 parameter 설정과 Query 결과에 대한 mapping 구문을 제거  
    
    SQL문과 프로그래밍 코드의 분리  
    - SQL에 변경이 있을 때마다 자바 코드를 수정하거나 컴파일 하지 않아도 됨  
    - SQL 작성과 관리 또는 검토를 DBA와 같은 개발자가 아닌 다른 살마에게 맡길 수 있음.  
    
    다양한 프로그래밍 언어로 구현 가능  
    - Java, C#, .NET, Ruby, ...  
    
      
    

### MyBatis와 MyBatis-Spring의 주요 Component

---

- MyBatis와 MyBatis-Spring을 사용한 DB Access Architecture.
    
    ![[Untitled 54.png|Untitled 54.png]]
    

  

- MyBatis를 사용하는 Data Access Layer
    
    ![[Untitled 1 32.png|Untitled 1 32.png]]
    
      
    
- MyBatis 3의 주요 Component
    
    ![[Untitled 2 31.png|Untitled 2 31.png]]
    
      
    
- MyBatis 3의 주요 Component의 역할
    
    ![[Untitled 3 30.png|Untitled 3 30.png]]
    
      
    
- MyBatis-Spring의 주요 Component
    
    ![[Untitled 4 26.png|Untitled 4 26.png]]
    
      
    
- MyBatis-Spring의 주요 Component의 역할
    
    ![[Untitled 5 23.png|Untitled 5 23.png]]
    
      
    

### MyBatis3의 Mapper Interface

---

- Mapper Interface
    
    Mapper Interface는 mapping 파일에 기재된 SQL을 호출하기 위한 Interface.  
    - Mapper Interface는 SQL을 호출하는 프로그램을 Type Safe하게 기술하기 위해 MyBatis 3.x부터 등장.  
    - Mapping 파일에 있는 SQL을 java interface를 통해 호출할 수 있도록 해 줌  
    
      
    
- Mapper Interface를 사용하지 않았을 경우
    
    ![[Untitled 6 20.png|Untitled 6 20.png]]
    
    ![[Untitled 7 17.png|Untitled 7 17.png]]
    
      
    

### MyBatis와 Spring의 연동

---

- 개요
    
    MyBatis를 Standalone 형태로 사용하는 경우, SqlSessionFactory 객체를 직접 사용
    
    스프링을 사용하는 경우, 스프링 컨테이너에 MyBatis 관련 빈을 등록하여 MyBatis를 사용
    
    또한 스프링에서 제공하는 트랜잭션 기능을 사용하면 손쉽게 트랜잭션 처리
    
    MyBatis를 스프링과 연동하기 위해서는 MyBatis에서 제공하는 Spring 연동 라이브러리가 필요
    
    ![[Untitled 8 15.png|Untitled 8 15.png]]
    
      
    
- DataSource 설정
    
    스프링을 사용하는 경우, 스프링에서 데이터 소스를 관리하므로 MyBatis 설정파일에서는 일부 설정을 생략
    
    스프링 환경 설펑 자일(application-context.xml)에 데이터소스를 설정
    
    데이터 소스는 dataSource 아이디를 가진 빈으로 데이터베이스 연결 정보를 가진 객체
    
    MyBatis와 스프링을 연동하면 데이터베이스 설정과 트랜잭션 처리는 스프링에서 관리
    
    ![[Untitled 9 14.png|Untitled 9 14.png]]
    
      
    
- 트랜잭션 관리자 설정
    
    transactionManager 아이디를 가진 빈은 트랜잭션을 관리하는 객체
    
    MyBatis는 JDBC를 그래로 사용하기 때문에 DataSourceTransactionManager 타입의 빈을 사용
    
    tx:annotation-driven 요소는 트랜잭션 관리 방법을 어노테이션으로 선언하도록 설정
    
    스프링은 메소드나 클래스에 @Transactional이 선언되어 있으면, AOP를 통해 트랜잭션을 처리
    
    ![[Untitled 10 12.png|Untitled 10 12.png]]
    
      
    
- SqlSessionFactoryBean 설정
    
    MyBatis 애플리케이션은 SqlSessionFactory를 중심으로 수행
    
    스프링에서 SqlSessionFactory 객체를 생성하기 위해서는 SqlSessionFactoryBean을 빈으로 등록해야 함.
    
    SqlSeesionFactoryBean을 빈으로 등록할 때, 사용할 데이터 소스와 mybatis 설정파일 정보가 필요
    
    ![[Untitled 11 10.png|Untitled 11 10.png]]
    
      
    
- mapper 빈 등록
    
    mapper 인터페이스를 사용하기 위해서 스캐너를 사용하여 자동으로 등록하거나, 직접 빈으로 등록.
    
    mapperSacnnerConfigurer을 설정하면, Mapper 인터페이스를 자동으로 검색하여 빈으로 등록  
    - basePackage로 패키지를 설정하면, 해당 패키지 하위의 모든 매퍼 인터페이스가 자동으로 등록  
    
    MapperFactoryBean 클래스는 매퍼 인터페이스를 직접 등록할 때 사용
    
    ![[Untitled 12 10.png|Untitled 12 10.png]]
    
      
    
- MyBatis Configuration 파일 예
    
    스프링을 사용하면 DB 접속정보 및 Mapper 관련 설정은 스프링 빈으로 등락하여 관리
    
    따라서, MyBatis 환결설정 파일에는 스프링에서 관리하지 않느 일부 정보만 설정
    
    예) typeAlias, typeHandler 등
    
    ![[Untitled 13 10.png|Untitled 13 10.png]]
    
      
    
- 데이터 접근 객체 구현
    
    데이터 접근 객체는 특정한 기술을 사용하여 데이터 저장소에 접근하는 방식을 구현한 객체
    
    @Repository은 데이터 접근 객체를 빈으로 등록하기 위해 사용하는 스프링에서 제공하는 어노테이션
    
    @Autowired 어노테이션을 통해, 사용하려는 Mapper 인터페이스를 데이터 접근 객체와 의존 관계를 설정