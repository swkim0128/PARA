---
type: Spring
archive: false
---
## 스프링 웹 계층

---

![[Untitled 30.png|Untitled 30.png]]

![[Untitled 1 10.png|Untitled 1 10.png]]

  

스프링의 계층은 Presentation Layer, Business Layer, Data Access Layer 크게 3가지로 나눌 수 있다.

  

### 프레젠테이션 계층

---

- 브라우저 상의 웹 클라이언트의 요청 및 응답을 처리
- 서비스 계층, 데이터 엑세스 계층에서 발생하는 Exception을 처리
- @Controller 어노테이션을 사용하여 작성된 Controller 클래스가 이 계층에 속함

  

### 서비스 계층

---

- 애플리케이션 비즈니스 로직 처리와 비즈니스와 관련된 도메인 모델의 적합성 검증
- 트랜잭션 관리
- 프레젠테이션 계층과 데이터 엑세스 계층 사이를 연결하는 역할로서 두 계층이 직접적으로 통신하지 않게 함
- Service 인터페이스와 @Service 어노테이션을 사용하여 작성된 Service 구현 클래스가 이 계층에 속함

  

### 데이터 엑세스 계층

---

- ORM (Mybatis, Hibernate)를 주로 사용하는 계층
- DAO 인터페이스와 @Repository 어노테이션을 사용하여 작성된 DAO 구현 클래스가 이 계층에 속함
- Dabase에 data를 CRUD(Create, Read, Update, Drop)하는 계층

  

### 도메인 모델 계층

---

- DB의 테이블과 매칭될 클래스
- Entity 클래스라고도 부른다.

  

### DTO(Data Tranfer Object)

---

- 각 계층간 데이터 교환을 위한 객체 (데이터를 주고 받을 포맷)
- Domain, VO라고도 부름
- DB에서 데이터를 얻어 Service, Controller 등으로 보낼 때 사용함
- 로직을 갖지 않고 순수하게 getter, setter 메소드를 가진다.

  

### DAO(Data Access Object)

---

- DB에 접근하는 객체, DB를 사용해 데이터를 조작하는 기능을 하는 객체 (MyBatis 사용시에 DAO or Mapper 사용)
- Repository라고도 부름(JPA 사용시 Repository 사용)
- Service 계층과 DB를 연결하는 고리 역할을 한다.

  

### Entity 클래스란?

---

- Domain 이라고도 부름 (JPA 사용할 때 사용)
- 실제 DB 테이블과 매칭될 클래스
- Entity 클래스 또는 가장 Core한 클래스라고 부름
- Domain 로직만을 가지고 있어야하며 Presentation Logic을 가지고 있어서는 안된다.

  

### Domain 클래스와 DTO 클래스를 분리하는 이유

---

- View Layer와 DB Layer의 역할을 철저하게 분리하기 위해서
- 테이블과 매핑되는 Entity 클래스가 변경되면 여러 클래스에 영향을 끼치게 되지만 View와 통신하는 DTO 클래스는 자주 변경되므로 분리해야 한다.
- 즉 DTO는 Domain Model을 복사한 형태로, 다양한 Presentation Logic을 추가한 정도로 사용하며 Domain Model 객체는 Persistent만을 위해서 사용한다.

  

![[Untitled 2 9.png|Untitled 2 9.png]]

![[Untitled 3 9.png|Untitled 3 9.png]]

  

### RestController와 @Service를 나누는 이유

---

- @Service를 만들어서 나누는 이유는 중복되는 코드가 생기기 때문이다.
    - 비즈니스 로직은 다른 요청 URL에서 사용해야 하는 경우가 있다. 만약 비즈니스 로직 코드가 컨트롤러에 구현되어 있는 경우, 다른 컨트롤러의 핸들러 메소드에서 똑같은 로직코드를 구현해야하니 중복코드가 발생하고 재사용성이 줄어든다.
- 중복되는 코드가 발생하면 따로 모듈화를 해서 나눠주는 것이 유지 보수하기 편리하다. (NodeJS => 모듈화)
- 모든 기능들을 세분화해서 @Service에 작성하게 되면 나중에는 서비스의 기능들을 조합만 해서 새로운 기능을 만들 수 있음
- 서비스에서 다른 서비스를 의존성 참조하는 것도 가능하다.

즉, 비즈니스 로직의 서비스 구현체에서 구현하는 이유는 바로 확장성과 재사용성 그리고 중복 코드의 제거이다.

  

  

## 프로젝트 구조

---

![[Untitled 4 7.png|Untitled 4 7.png]]

![[Untitled 5 6.png|Untitled 5 6.png]]