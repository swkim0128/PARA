# [DDD] Domain Model, Aggregate, Bounded Context

![rw-book-cover](https://velog.velcdn.com/images/daehoon12/post/06320433-421a-47bd-a415-ffff95cf4221/image.png)

## Metadata
- Author: [[velog.io]]
- Full Title: [DDD] Domain Model, Aggregate, Bounded Context
- Category: #articles
- Document Tags:  #ddd 
- Summary: Domain-Driven Design divides complex systems into smaller parts called aggregates and bounded contexts to manage complexity and maintain data consistency. Aggregates group related objects with a root entity that controls their lifecycle and enforces domain rules. Bounded contexts define clear boundaries where specific domain models apply, helping teams work independently without confusion over terms or responsibilities.
- URL: https://velog.io/@daehoon12/DDD-Domain-Model-Aggregate-Bounded-Context

## Full Document
### 트랜잭션 스크립트 패턴 Vs. 도메인 모델 패턴

#### 트랜잭션 스크립트 패턴

![](https://velog.velcdn.com/images/daehoon12/post/964a7b31-05dd-43b9-8815-e784ec4d8813/image.png)
* 비즈니스 로직을 요청 타입별로 **하나씩 매핑된 절차적 트랜잭션 스크립트 뭉치**로 구성한다.
	+ 일반적으로 동작을 하는 클래스: `OrderService`, `OrderDao`
	+ 상태가 있는 클래스: `Order`

#### 도메인 모델 패턴

![](https://velog.velcdn.com/images/daehoon12/post/bfb46a5b-1fb2-443c-941a-9e6ac88d67a3/image.png)
* 비즈니스 로직을 **상태와 동작**을 가진 클래스로 구성된 객체 모델로 구성한다.
	+ 동작만 있는 클래스: `OrderService`, `OrderRepository`
	+ 상태만 있는 클래스: `DeliveryInformation`,
	+ 동작과 상태를 갖는 클래스 (도메인 모델): `Order`
* 대부분의 클래스는 상태와 동작을 가진다.

트랜잭션 스크립트 패턴을 적용하면 `OrderService` 클래스는 각 요청 및 시스템 작업마다 하나의 메서드를 갖게 두지만, **도메인 모델 패턴을 적용하면 서비스 메서드가 단순해진다**

##### 도메인 모델 패턴의 장점

* 설계를 이해/관리하기 쉽다. -> 모두를 관리하는 하나의 거대한 클래스 대신 소수의 책임만 맡은 여러 클래스들로 구성되기 때문
* 테스트가 쉬움. -> 각 클래스를 독립적으로 테스트할 수 있다.
* 잘 알려진 설계 패턴을 응용할 수 있기 때문에 확장에 용이 -> 전략 패턴, 템플릿 메서드 패턴을 적용하여 코드를 변경하지 않아도 컴포넌트 확장 가능

즉, **높은 응집력과 낮은 결합도**로 각각의 도메인을 서로 철저히 분리하고 변경과 확장에 용이한 설계를 얻게된다.

```
@Entity
@Table(name = "members")
class Member(
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Long = 0,

    @Column(nullable = false)
    var name: String,

    @Column(nullable = false, unique = true)
    var email: String,

    @Column(nullable = false)
    private var password: String
) {
    fun checkPassword(inputPassword: String, passwordEncoder: BCryptPasswordEncoder): Boolean {
        return passwordEncoder.matches(inputPassword, this.password)
    }
}

@Service
class TransactionScriptLoginService(
  private val memberRepository: MemberRepository,
  private val passwordEncoder: BCryptPasswordEncoder
) { 
  fun login(email: String, password: String): Boolean {
    memberRepository.findByEmail(email)?.let { member ->
      if (passwordEncoder.matches(password, member.password)) {
        return true
      }
      return false
    }
    return false
  }
}
  @Service
  class DomainModelLoginService(
    private val memberRepository: MemberRepository,
    private val passwordEncoder: BCryptPasswordEncoder
  ) {
    fun login(email: String, password: String)
        = memberRepository.findByEmail(email)?.let { member ->
      member.checkPassword(password, passwordEncoder)
    } ?: false
  }
```

문제: 두 개의 서비스 코드 중 더 깔끔해 보이는 것을 고르시오.

### DDD 개요

* DDD(Domain-Driven Design) 또는 도메인 주도 설계라고 부른다. **도메인 패턴**을 중심에 놓고 설계하는 방식을 일컫는다.
* DDD는 **복잡한 비즈니스 로직을 개발하기 위해 OOD를 개선한 접근 방식**
	+ 각 서비스는 자체 도메인 모델을 가지며, 애플리케이션 전체 도메인 모델의 문제점을 방지할 수 있다.
	+ **하위 도메인**과 이와 연관된 **Bounded Context 개념**은 DDD 패턴의 메인 전략들
* 아래는 DDD에서 도메인 모델을 구축하는 데 흔히 쓰이는 빌딩 블록
	+ 엔티티 (Entity): 영속성 신원을 가진 객체. 두 엔티티가 속성 값이 동일해도 엄연히 다른 객체. 자바에서는 JPA에 `@Entity`를 붙여 DDD 엔티티를 나타냄
	+ 값 객체 (Value Object): 여러 값을 모아 놓은 객체. 속성 값이 동일한 두 값 객체는 서로 바꾸어 사용할 수 있다. (예: 통화와 금액으로 구성된 Money 클래스)
	+ 팩토리 (Factory): 일반 생성자로 직접 만들기에 복잡한 객체 생성 로직이 구현된 객체 또는 메서드. 인스턴스로 생성할 구상 클래스를 감출 수 있으며, 클래스의 정적 메서드로 구현할 수 있음.
	+ 리포지터리 (Repository): 엔티티를 저장하는 DB 접근 로직을 캡슐화한 객체
	+ 서비스 (Service): 엔티티, 밸류 객체에 속하지 않은 비즈니스 로직 구현 객체

#### DDD 계층

![](https://velog.velcdn.com/images/daehoon12/post/06320433-421a-47bd-a415-ffff95cf4221/image.png)
* **표현 계층 (Presentation Layer): 사용자의 요청에 대해 해석하고 응답하는 일을 책임지는 계층**이다.
	+ 사용자에게 UI를 제공하거나 클라이언트에 응답을 다시 보내는 역할을 하는 모든 클래스가 포함된다.
	+ 백엔드 어플리케이션의 경우 presentation layer는 아래와 같은 역할을 한다
		- cilent로부터 request를 받고 response를 return하는 API 정의
		- api route별 로깅, 보안 등의 전처리
* **응용 계층 (Application Layer)**
	+ **소프트웨어가 비즈니스 로직을 정의하고 정상적으로 수행될 수 있도록 도메인 계층과 인프라스트럭쳐 계층을 연결해주는 역할을 하는 계층**이다.
	+ **은 정보를 가지고 있지 않게 유지하는 것이 중요하다.** 실질적인 데이터의 상태 변화 등의 처리는 도메인 계층에서 진행할 수 있도록 위임 하는것이 중요하다.
	+ 응용 계층에서 진행하는 일은 일반적으로 **transaction 관리, DTO 변환, 그리고 모듈간의 연계** 이렇게 3가지를 들 수 있다.
* **도메인 계층 (Domain Layer)**
	+ **비즈니스 규칙, 정보에 대한 실질적인 도메인에 대한 정보**를 가지고 있으며, 이 모든것을 책임지는 계층이다. 이 계층에서는 **업무 상황을 반영하여 상태를 제어하는 역할에 집중하는 계층**이다.
* **인프라스트럭처 계층**(영속성 계층)
	+ **상위 계층을 지원하는 일반화된 기술적 기능을 제공하는 계층**이다. **일반적으로 외부 시스템을 호출한다거나 하는 역할을 담당**한다. **해당 계층에서 얻어온 정보를 응용계층 또는 도메인 계층에 전달하는 것을 주 역할로 담당**한다. (Repository)

#### Aggregate

![](https://velog.velcdn.com/images/daehoon12/post/0122f46b-18f9-41d0-892f-81513e9c306d/image.png)
* 복잡한 도메인을 이해하고 관리하기 쉬운 단위로 만들려면 상위 수준에서 모델을 조망할 수 있는 방법이 필요한데, 그 방법이 바로 애그리거트다. **애그리거트는 관련된 객체를 하나의 군으로 묶어 준다. 수많은 객체를 애그리거트로 묶어서 바라보면 상위 수준 에서 도메인 모델 간의 관계를 파악할 수 있다.**
* [그림 3.3]은 [그림 3.2]의 모델을 애그리거트 단위로 묶어서 다시 표현한 것이다. 동일한 모델이지만 **애그리거트를 사용함으로써 모델 간의 관계를 개별 모델 수준과 상위 수준에서 모두 이해할 수 있다.**  
 ![](https://velog.velcdn.com/images/daehoon12/post/c9d6de3e-a2fb-4f45-95bd-6e27ab2c2c6e/image.png)
* 애그리거트는 모델을 이해하는 데 도움을 줄 뿐만 아니라 **일관성을 관리하는 기준**도 된다. 모델을 보다 잘 이해할 수 있고 **애그리거트 단위로 일관성을 관리하기 때문에,** 애그리거트는 복잡한 도메인을 단순한 구조로 만들어준다. 복잡도가 낮아지는 만큼 도메인 기능을 확장하고 변경하는 데 필요한 노력 (개발 시간)도 줄어든다.
* 애그리거트는 관련된 모델을 하나로 모았기 때문에 **한 애그리거트에 속한 객체는 유사하거나 동일한 라이프 사이클을 갖는다.**
	+ 주문 애그리거트를 만들려면 Order, OrderLine, Orderer 와 같은 관련 객체를 함께 생성해야 한다.
	+ Order는 생성했는데 ShippingInfo는 만들지 않거 나 ShippingInfo를 생성하면서 Orderer를 생성하지 않는 경우는 없다. 도메인 규칙에 따라 최초 주문 시점에 일부 객체를 만들 필요가 없는 경우도 있지만 **애그리거트에 속한 구성요소는 대부분 함께 생성하고 함께 제거한다.**
* [그림 3.3]에서 보는 것처럼 애그리거트는 경계를 갖는다. 한 애그리거트에 속한 객체는 다른 애그리거트에 속하지 않는다. 애그리거트는 독립된 객체 군이며 각 애그리거트는 자기 자신을 관리할 뿐 다른 애그리거트를 관리하지 않는다.
	+ 예를 들어 주문 애그리거트는 배송지를 변경하거나 주문 상품 개수를 변경하는 등 자기 자신은 관리하지만, 주문 애그리거트에서 회원의 비밀번호를 변경하거나 상품의 가격을 변경하지는 않는다.
* **경계를 설정**할 때 기본이 되는 것은 **도메인 규칙과 요구사**항이다. **도메인 규칙에 따라 함께 생성되는 구성요소는 한 애그리거트에 속할 가능성이 높다.**
	+ 예를 들어 **주문할 상품 개수, 배송 지 정보, 주문자 정보는 주문 시점에 함께 생성되므로 이들은 한 애그리거트에 속한다.**
	+ 또한 OrderLine의 주문 상품 개수를 변경하면 도메인 규칙에 따라 Order의 총 주문 금액을 새로 계산해야 한다. 사용자 요구사항에 따라 주문 상품 개수와 배송지를 함께 변경하기도 한다. 이렇게 **함께 변경되는 빈도가 높은 객체는 한 애그리거트에 속할 가능성이 높다**.
* **흔히 'A가 B를 갖는다'로 설계할 수 있는 요구사항이 있다면 A와 B를 한 애그리거트로 묶어서 생각하기 쉽다.** 주문의 경우 Order가 ShippingInfo와 Orderer를 가지므로 이는 어느 정도 타당해 보인다. 하지만 A가 B를 갖는다'로 해석할 수 있는 요구사항이 있다고 하더라도 이것이 **반드시 A와 B가 한 애그리거트에 속한다는 것을 의미하는 것은 아니다.**
	+ 좋은 예가 상품과 리뷰다. 상품 상세 페이지에 들어가면 상품 상세 정보와 함께 리뷰 내용을 보여줘야 한다는 요구사항이 있을 때 **Product 엔티티와 Review 엔티티가 하나의 애그리거트에 속한다고 생각할 수 있다. 하지만 Product와 Review는 함께 생성되지 않고, 함께 변경되지도 않는다.** 게다가 **Product를 변경하는 주체가 상품 담당자라면 Review를 생성하고 변경하는 주체는 고객이다.**
	+ **Review의 변경이 Product에 영향을 주지 않고 반대로 Product의 변경이 Review에 영향을 주지 않기 때문**에 이 둘은 한 애그리거트에 속하기 보다는 [그림 3.3]에 표시한 것처럼 서로 다른 애그리거트에 속한다.

![](https://velog.velcdn.com/images/daehoon12/post/e6de82fd-dfe5-459b-a34a-d16e4fca4121/image.png)
* 처음 도메인 모델을 만들기 시작하면 큰 애그리거트로 보이는 것들이 많지만, **도메인에 대한 경험이 생기고 도메인 규칙을 제대로 이해할수록 애그리거트의 실제 크기는 줄어든다**. 그동안 경험을 비추어 보면 **다수의 애그리거트가 한 개의 엔티티 객체만 갖는 경우가 많았으며 두 개 이상의 엔티티로 구성되는 애그리거트는 드물었다.**

##### 루트 애그리거트

* 주문 애그리거트는 다음을 포함한다.
	+ 종 금액인 `totalAmounts`를 갖고 있는 `Order 엔티티`
	+ 개별 구매 상품의 개수인 `quantity`와 금액인 `price`를 갖고 있는 `OrderLine 밸류`
* 구매할 상품의 개수를 변경하면 한 `OrderLine`의 `quantity`를 변경하고 더불어 `Order`의 `totalAmounts`도 변경해야 한다. 그렇지 않으면 다음 도메인 규칙을 어기고 **데이터 일관성이 깨진다.**
	+ 주문 총 금액 = 상품의 주문 개수 X 가격의 합
* 애그리거트는 여러 객체로 구성되기 때문에 한 객체만 상태가 정상이면 안 된다. **도메인 규칙을 지키려면 애그리거트에 속한 모든 객체가 정상 상태를 가져야 한다.**
	+ 주문 애그리거트에서는 **OrderLine을 변경**하면 `**Order`의 `totalAmounts`도 다시 계산\*\*해서 총 금액이 맞아야 한다.
* 애그리거트에 속한 **모든 객체가 일관된 상태를 유지하려면 애그리거트 전체를 관리할 주체가 필요**한데, **이 책임을 지는 것이 바로 애그리거트의 루트 엔티티이다.** 애그리거트 루트 엔티티는 애그리거트의 대표 엔티티다. **애그리거트에 속한 객체는 애그리거트 루트 엔티티에 직접 또는 간접적으로 속하게 된다.**  
 ![](https://velog.velcdn.com/images/daehoon12/post/eb34b17d-2151-47e2-a67a-38e0ad2a1932/image.png)
* 주문 애그리거트에서 루트 역할을 하는 엔티티는 `Order`이다. `OrderLine, ShippingInfo, Orderer` 등 주문 애그리거트에 속한 모델은 `Order`에 직접 또는 간접적으로 속한다.

**애그리거트 규칙**

**규칙 #1: 애그리거트 루트만 참조해라**

* **데이터 일관성**을 지키기 위해 **외부 클래스는 반드시 에그리거트 루트 엔티티만 참조**할수 있게 제한해야 한다.

**규칙 #2: 애그리거트 간 참조는 반드시 기본 키를 사용해라**

![](https://velog.velcdn.com/images/daehoon12/post/d53d727b-336b-4372-a035-1f514881e107/image.png)
* 객체 참조 대신 레퍼런스 참조를 사용하면, 에그리거트는 **느슨하게 결합되고 경계가 분명해지기 때문에, 혹여 실수로 다른 애그리거트를 업데이트할 일이 일어나지 않음.**
* 애그리거트는 그 자체가 저장 단위이므로 저장 로직도 간단해진다. 그래서 **MongoDB 같은 NoSQL DB에 애그리거트를 저장하기가 한결 쉽다.**

**규칙 #3: 하나의 트랜잭션으로 하나의 애그리거트를 수정해라**

* 하나의 트랜잭션으로 오직 하나의 애그리거트만 생성/수정 해야한다.
* 단 이 규칙을 준수하려면 여러 애그리거트를 생성/수정하는 작업을 구현하기가 조금 복잡해진다. 하지만 사가로 해결 가능한 문제. 사가의 각 단계는 정확히 애그리거트 하나를 생성/수정한다.

![](https://velog.velcdn.com/images/daehoon12/post/164bab9e-1e68-4058-93df-dbbe7e8b02d8/image.png)
* 1번 트랜잭션은 서비스 A의 애그리거트 X를 업데이트 한다.
* 2~3번 트랜잭션은 모두 서비스 B에 있고, 2번 트랜잭션이 애그리거트 Y를, 3번 트랜잭션이 애그리거트 Z를 각각 업데이트 한다.
* 서비스 하나에서 여러 애그리거트에 걸쳐 일관성을 유지하는 또 다른 방법은 **여러 애그리거트를 한 트랜잭션으로 업데이트 하는 방법**이다. 가령 서비스 B에서 애그리거트 Y,Z를 한 트랜잭션으로 업데이트 하면 된다. 물론 트랜잭션이 잘 지원되는 **RDBMS에서 가능하고 NoSQL DB는 사가 외에 별 다른 수단이 존재하지 않는다.** (몽고도 트랜잭션 지원이 되는걸로 알긴 하는데..)

#### Domain Model과 Bounded Context

##### 도메인 모델과 경계

* **하나의 도메인은 다시 여러 하위 도메인으로 구분되기 때문**에 한 개의 모델로 여러 하위 도메인을 모두 표현하려고 시도하면 오히려 모든 하위 도메인에 맞지 않는 모델을 만들게 된다.
	+ 예를 들어 상품이라는 모델을 생각해 보자. 카탈로그에서 상품, 재고 관리에서 상품, 주문에서 상품, 배송에서 **상품은 이름만 같지 실제로 의미하는 것이 다르다.** 카탈로그에서의 상품은 상품 이미지, 상품명, 상품 가격, 옵션 목록, 상세 설명과 같은 **상품 정보가 위주**라면, 재고 관리에서는 **실존하는 개별 객체를 추적하기 위한 목적**으로 상품을 사용한다. 즉 **카탈로그에서는 물리적으로 한 개인 상품이 재고 관리에서는 여러 개 존재할 수 있다.**
	+ 논리적으로 같은 존재처럼 보이지만 **하위 도메인에 따라 다른 용어를 사용하는 경우**도 있다.  
	 카탈로그 도메인에서의 상품이 검색 도메인에서는 문서로 불리기도 한다. 비슷하게 시스템을 사용하는 사람을 회원 도메인에서는 회원이라고 부르지만, 주문 도메인에서는 주문자라고 부르고, 배송 도메인에서는 보내는 사람이라고 부르기도 한다.
* 이렇게 하위 도메인마다 같은 용어라도 의미가 다르고 같은 대상이라도 지칭하는 용어가 다를 수 있기 때문에 **한 개의 모델로 모든 하위 도메인을 표현하려는 시도는 올바른 방법이 아니며 표현할 수도 없다.**
* 하위 도메인마다 사용하는 용어가 다르기 때문에 올바른 도메인 모델을 개발하려면 **하위 도메인마다 모델을 만들어야 한다.** 각 모델은 **명시적으로 구분되는 경계**를 가져서 섞이지 않도록 해야 한다.
	+ 모델은 특정한 컨텍스트(문맥) 하에서 완전한 의미를 갖는다. 같은 상품이라도 **카탈로그 컨텍스트와 재고 컨텍스트에서 의미가 서로 다르다.** 이렇게 **구분되는 경계를 갖는 컨텍스트**를 DDD에서는 바**운디드 컨텍스트 (bounded Conext)**라고 부른다.

##### 바운디드 컨텍스트

* 바운디드 컨텍스트는 모델의 경계를 결정하며 한 개의 바운디드 컨텍스트는 논리적으로 한 개의 모델을 갖는다. 바운디드 컨텍스트는 **용어를 기준으로 구분**한다.
	+ 카탈로그 컨텍스트와 재고 컨텍스트는 서로 다른 용어를 사용하므로 이 용어를 기준으로 컨텍스트를 분리할 수 있다. 또 한 바운디드 컨텍스트는 실제로 사용자에게 기능을 제공하는 물리적 시스템으로 도메인 모델은 이 바운디드 컨텍스트 안에서 도메인을 구현한다.
* 이상적으로 하위 도메인과 바운디드 컨텍스트가 일대일 관계를 가지면 좋겠지만 현실은 그렇지 않을 때가 많다. 바운디드 컨텍스트는 **기업의 팀 조직 구조에 따라 결정되기도 한다.**
	+ 예를 들어 주문 하위 도메인이라도 **주문을 처리하는 팀**과 **복잡한 결제 금액 계산 로직을 구현하는 팀**이 따로 있다고 해보자. 이 경우 **주문 하위 도메인에 주문 바운디드 컨텍스트와 결제 금액 계산 바운디드 컨텍스트가 존재**하게 된다.
	+ 용어를 명확하게 구분하지 못해 두 하위 도메인을 하나의 바운드 컨텍스트에서 구현하기도 하는데, 예를 들어 카탈로그와 재고 관리가 아직 명확하게 구분되지 않은 경우 두 하위 도메인을 하나의 바운디드 컨텍스트에서 구현하기도 한다.

![](https://velog.velcdn.com/images/daehoon12/post/ec25d433-ab4e-484d-833a-d78361feb64f/image.png)
* 규모가 작은 기업은 전체 시스템을 한 개 팀에서 구현할 때도 있다. 예를 들어 소규모 쇼핑몰은 한 개의 웹 애플리케이션으로 온라인 쇼핑을 서비스하며 **하나의 시스템에서 회원, 카탈로그, 재고, 구매, 결제와 관련된 모든 기능을 제공**한다. **즉, 여러 하위 도메인을 한 개의 바운디드 컨텍스트에서 구현한다.**
* 여러 하위 도메인을 하나의 바운디드 컨텍스트에서 개발할 때 주의할 점은 **하위 도메인의 모델이 섞이지 않도록 하는 것이다**. 한 프로젝트에 각 하위 도메인의 모델이 위치하면 **아무래도 전체 하위 도메인을 위한 단일 모델을 만들고 싶은 유혹에 빠지기 쉽다**. 이런 유혹에 걸려들면 결과적으로 **도메인 모델이 개별 하위 도메인을 제대로 반영하지 못해서 하위 도메인별로 기능을 확장하기 어렵게 되고 이는 서비스 경쟁력을 떨어뜨리는 원인이 된다.**
* 비록 한 개의 바운디드 컨텍스트가 여러 하위 도메인을 포함하더라도 **하위 도메인마다 구분되는 패키지를 갖도록 구현해야 하며, 이렇게 함으로써 하위 도메인을 위한 모델이 서로 뒤섞이지 않고 하위 도메인마다 바운디드 컨텍스트를 갖는 효과를 낼 수 있다.** (그림 9.3)

![](https://velog.velcdn.com/images/daehoon12/post/231fdcff-4a78-4da8-9bdd-dd42a780132d/image.png)
* 바운디드 컨텍스트는 도메인 모델을 구분하는 경계가 되기 때문에 바운디드 컨텍스트는 **구현 하는 하위 도메인에 알맞은 모델을 포함**한다. 같은 사용자라 하더라도 주문 바운디드 컨텍스트와 회원 바운드 컨텍스트가 갖는 모델이 달라진다.
	+ 같은 상품이라도 카탈로그 바운드 컨텍스트의 Product와 재고 바운디드 컨텍스트의 Proudct는 각 컨텍스트에 맞는 모델을 갖는다. 따라서 **회원의 Member는 애그리거트 루트이지만 주문의 Orderer는 밸류**가 되고 **카탈로그의 Proudct는 상품이 속할 Category와 연관을 갖지만 재고의 Product는 카탈로그의 Category와 연관을 맺지 않는다**

![](https://velog.velcdn.com/images/daehoon12/post/cadec1c7-3ce2-4bed-ad7b-e52d164a258b/image.png)
**바운디드 컨텍스트 구현**

* 바운디드 컨텍스트가 도메인 모델만 포함하는 것은 아니다. 바운디드 컨텍스트는 **도메인 기능을 사용자에게 제공하는 데 필요한 표현 영역, 응용 서비스, 인프라스트럭처 영역을 모두 포함**한다. 도메인 모델의 데이터 구조가 바뀌면 DB 테이블 스키마도 함께 변경해야 하므로 테이블도 바운디드 컨텍스트에 포함된다

![](https://velog.velcdn.com/images/daehoon12/post/104bc9b5-3adb-4d76-a6ef-c147ef340e75/image.png)
* 또한 모든 바운디드 컨텍스트를 도메인 모델 패턴으로 개발할 필요는 없다. 상품의 리뷰가 복잡한 도메인 로직을 갖지 않는다면, 단순한 트랜잭션 스크립트 패턴으로 구현해도 된다.
* 트랜잭션 스크립트 패턴을 사용하면 도메인 기능이 서비스 계층에 흩어지게 되지만 도메인 기능 자체가 단순하면 코드를 유지-보수 하는데 큰 이슈가 되지는 않는다.

**DDD 관련하여 인프런 답변**  

[https://www.inflearn.com/questions/18866/객체들간의-연관관계-설정](https://www.inflearn.com/questions/18866/%EA%B0%9D%EC%B2%B4%EB%93%A4%EA%B0%84%EC%9D%98-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84-%EC%84%A4%EC%A0%95) (김영한님)  

[https://www.inflearn.com/questions/27918/도메인설계-관련-질문드립니다](https://www.inflearn.com/questions/27918/%EB%8F%84%EB%A9%94%EC%9D%B8%EC%84%A4%EA%B3%84-%EA%B4%80%EB%A0%A8-%EC%A7%88%EB%AC%B8%EB%93%9C%EB%A6%BD%EB%8B%88%EB%8B%A4) (김영한님)  

[https://www.inflearn.com/questions/117315/비지니스-로직구현-entity-vs-service](https://www.inflearn.com/questions/117315/%EB%B9%84%EC%A7%80%EB%8B%88%EC%8A%A4-%EB%A1%9C%EC%A7%81%EA%B5%AC%ED%98%84-entity-vs-service) (김영한님)  

[https://www.inflearn.com/questions/1081614/bounded-context-와-aggregate-질문있습니다](https://www.inflearn.com/questions/1081614/bounded-context-%EC%99%80-aggregate-%EC%A7%88%EB%AC%B8%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4) (애프터캠프님)
