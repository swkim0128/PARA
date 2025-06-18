# (4) Ddd의 서비스/팩토리/패키지 - 코드를 작성하는 세부 방법들 본문

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcSvnOs%2FbtruWjCyhes%2FwY9uQO4YxDNDLavZzhmKIk%2Fimg.jpg)

## Metadata
- Author: [[TISTORY]]
- Full Title: (4) Ddd의 서비스/팩토리/패키지 - 코드를 작성하는 세부 방법들 본문
- Category: #articles
- Document Tags:  #ddd 
- Summary: The text explains how to implement Domain-Driven Design (DDD) concepts like domain services, application services, factories, and package organization in code. It emphasizes the importance of placing domain logic within domain objects and using services to handle complex operations. The article also highlights the need for a structured package organization that reflects DDD principles, moving away from traditional methods.
- URL: https://appleg1226.tistory.com/44

## Full Document
#### Easy Understanding

**[Study](https://appleg1226.tistory.com/category/Study)**

##### (4) DDD의 서비스/팩토리/패키지 - 코드를 작성하는 세부 방법들

appleg1226 2022. 3. 2. 23:09 

![](https://blog.kakaocdn.net/dn/cSvnOs/btruWjCyhes/wY9uQO4YxDNDLavZzhmKIk/img.jpg)
이전까지는 DDD의 도메인 / 컨텍스트를 어떻게 클래스로 구현하는지 정리했다면,

이번에는 이런 도메인 객체들을 이용하는 방법과 도움이 되는 요소들에 대해서 간단하게 정리하려고 한다.

여러 도메인 로직을 엮거나 변환하는 등 도메인 로직을 조작하는데 활용하는 **'도메인 서비스'**

실제 사용자의 유스케이스, 유저 인터페이스 로직을 구현하는 **'어플리케이션 서비스'**

new로 객체를 생성하지 않고 대리 생성을 담당하는 메서드인 **'팩토리'**

그리고 이런 것들을 어떻게 자바 **'패키지'**로 구분하는지

에 대해서 정리해보았다.

이전에는 애그리거트 내부에서 도메인 로직을 구현했으니,

이번에는 위의 4가지 방법들을 이용해서 도메인 로직을 외부에 제공하는지까지 확인하게 될 것이다.

#### **1. 도메인 서비스**

DDD의 Service는 스프링에서 말하는 서비스와 정확한 개념은 다르다.

하지만 DDD의 서비스는 아마도 Spring의 **@Service** 어노테이션을 붙여서 구현하게 될 가능성이 높다.

이전에 스프링 개발을 할때는 습관처럼

> 1. User 클래스 작성   
> 2. UserRepository 클래스 작성  
> 3. UserService 클래스 작성

처럼 서비스를 작성하게 되었는데, 이 UserService와 같은 역할을 하는 Service가 아님은 확실하다.

그렇다면 도메인 서비스는 도대체 어떤 일을 하는걸까?

DDD에서 가장 중요한 것은 도메인 관련된 로직은 모조리 도메인 객체에 넣는 것이다.

가능하다면 여기에 넣어야 한다.

하지만 상황에 따라서 이럴 경우에는 도메인 서비스를 작성하면 좋다.

**- 어쩔 수 없이 각 도메인 객체에서 그 로직을 수행할 수 없을 때**

**- 여러 도메인들 간에 어떻게 처리해야 할지 애매할 때**

책에서는 대략 다음과 같은 상황에 사용할 것을 이야기한다.

**- 어떤 도메인 객체를 다른 도메인 객체로 변경하는 경우**

> ex) Payment라는 도메인을 가지고 Purchase라는 도메인으로 변환하는 경우

**- 하나 이상의 도메인 객체를 사용할 때**

> ex) Item, User 도메인이 있고 두 도메인 정보를 이용해서 '유저가 이 아이템을 샀을 때의 잔액 계산하기'

도메인 로직과 관련된 서비스는 대략 이런 느낌이다.

무엇인가를 계산하거나, 상태를 변경을 대신 해준다면 도메인 서비스 클래스이다.

> PurchaseFeeCalculator(구매시 어떤 비용을 계산해주는 클래스)  
> UserAuthorizationSupport(유저 권한을 체크해주는 클래스)  
> PointUsePriorityResolver(포인트 사용 우선순위를 반환해주는 클래스)

위의 클래스들의 안에는 애그리거트의 계산 또는 변화와 관련된 로직들이 존재할 것이다.

*이런 도메인 서비스는 그럼 interface로 생성해야할까, 아니면 class로 바로 생성해도 될까?*

이건 책에서는 호불호의 영역이라고 말한다.

마틴 파울러도 분리된 인터페이스를 무조건 사용하라고 말하지는 않는다.

결합분리의 목표가 분명할 때 유용하기 때문에,

그렇지 않다면 단순하게 구현체 하나만 단독으로 사용해도 된다고 한다.

#### **2. 어플리케이션 서비스**

책에서 반 버논은 어플리케이션의 의미에 이렇게 설명하고 있다.

**- 핵심 도메인 모델과 상호 교류하며 이를 지원하기 위해 잘 조합된 컴포넌트의 집합**

**- 각각의 영역에 어떤 것들이 들어가는지는 어플리케이션마다 다르며, 사용하는 아키텍처가 무엇인지에 따라서도 달라진다**

어플리케이션 서비스는 도메인 로직의 **유스케이스를 담당**하는 레이어이다.

내부에서 다양한 도메인 로직들을 엮어서 사용자의 유스케이스를 구현한다.

예를 들면, 어떤 유저가 어떤 아이템을 구매한다고 하면

> 1. 인증을 진행하고   
> 2. 트랜잭션을 시작하고  
> 3. 아이템 정보를 가져와야 하고  
> 4. 유저 정보를 가져와야 하고  
> 5. 아이템에 대한 결제 요청을 PG사에 보내고  
> 6. 아이템을 유저 계정에 귀속시키고  
> (+ 또 다른 무엇인가를 해야할지도 모른다)

이런 것들을 어플리케이션 서비스에서 담당하면 된다.

아니면 여러 애그리거트의 **데이터를 묶어서** 보내줘야 하는 경우에도 사용이 된다.

뷰 영역 쪽에서 원하는 데이터를 여러 번 호출하지 않도록 한 번에 묶어서 보내주는 경우가 포함된다.

> ex) 입금 기록, 출금 기록, 송금 기록 등을 엮어서 하나의 데이터 타입으로 묶어 클라이언트에게 전달한다.

또한 가장 많이 나타나는 예시는 **트랜잭션, 인증** 등이다.

스프링에서는 @PreAuthorize, @Transactional 같은 어노테이션들을 달아서 구현하기도 한다.

어플리케이션 서비스에서는 **메서드 시그니처(매개변수, 반환값의 타입 같은 것들)**를

최대한 도메인에 의존적이지 않도록 하는 것이 좋다.

예를 들면 다음과 같이 매개변수에 도메인 객체가 포함된 건 좋은 구현이 아니다.

```
public void registerAccount(Account account);
```

이럴 때는, 다음과 같이 도메인 의존적이지 않은 데이터를 사용해야 하며, primitive 타입 같은 것들을 사용하면 좋다.

```
public void registerAccount(accountId id, String password, String nickname);
```

매개변수가 많다면 아예 DTO를 사용하는 것도 방법이다.

```
public void resgiterAccount(createAccountDto dto);
```

#### **3. 팩토리**

팩토리 메서드를 DDD에서는 어떤 식으로 구현하면 좋을까?

크게 몇 가지 방법이 있다.

###### **1. Domain 객체 내에서의 팩토리**

값 객체나 세부 엔터티들은 내부에서 팩토리 메서드를 구현할 수 있다.

이전에 factory 객체를 이용해서 하는 것보다는 더욱 도메인 로직과 액션을 반영한 메서드 이름을 짓게 된다.

```
// 1
Discussion disc = forum.startDiscussion();

// 2
Game game = room.startGame();

// 3
Call call = phone.startCall(PhoneNumber number);
```

###### **2. Domain Service의 팩토리**

request DTO를 도메인 객체로 변환한다든지 할 때 사용할 수 있다.

그외에 도메인 서비스에서 담당할 일은 별로 없어보인다.

```
userConversionService.hostFrom(requestDto dto);
```

(아무래도 이 과정에서 MapStruct 같은 것들을 사용하게 될 듯.)

위의 것들이 일반적인 팩토리와 다른 점이라면,

클래스에 Factory라는 이름이 명시적으로 들어가지는 않는다는 점이 눈에 띈다.

그렇지만 상황에 따라서 정적 Factory 클래스가 필요하다면 사용해도 문제는 없을 것 같다.

(다만 도메인과 상관이 있으며, 도메인 객체에 메서드를 집어넣을 수 있으면 최대한 넣을 것)

#### **4. 패키지**

여기에서 패키지는 자바의 그 패키지이다.

스프링을 개발할 때 튜토리얼에서는 보통 다음처럼 패키지를 구성했다.

> - DDDStudySpringApplication.java  
> - controller  
> - service  
> - domain  
> - config

그러나 DDD에서는 이런 방식을 DDD적인 방식으로 재편하게 된다.

다음의 예시를 가지고 설명해 보자면

> com.study.ddd.domain.model.book

- com.study: 회사 이름 등이 포함된 패키지 접두사

- ddd: 바운디드 컨텍스트 이름

- domain: 도메인 계층이라는 뜻. 같은 레벨에는 application, infra 같은 패키지들이 존재하게 된다.

- model: 도메인의 모델을 구현하고 있다는 것을 명시적으로 나타낸다.(없어도 되지만, 저자는 있도록 하기를 강조한다)

- book: aggregate의 이름으로 구성한다. 이 안에 엔터티, 값객체, 도메인 서비스 등이 들어가게 된다.

그런데 DDD 관련 패키지에 관한 예시를 찾아보니,

패키지 구조가 비슷하지만 조금씩 다른 것을 확인할 수 있었다.

근데 그건 DDD에서는 크게 문제는 없는 것 같다.

왜냐하면 DDD의 핵심은 전략적 패턴, 즉 도메인 모델링 파트이기 때문이다.

기술적 구현은 여러 방법론이 있음을 인정하는 방법론이기에 가능하다.

적어도 한 controller 패키지 안에 모든 controller를 때려박는 예전의 습관만 버려도 반은 성공일듯하다.

###### '[Study](https://appleg1226.tistory.com/category/Study)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [DDD를 적용한 간단한 결제 컨텍스트 개발해보기(with CQRS)](https://appleg1226.tistory.com/46) (0) | 2022.04.03 |
| [(5) DDD와 아키텍처 - Layered, Hexagonal, CQRS, Event-Sourcing](https://appleg1226.tistory.com/45) (0) | 2022.03.06 |
| [(3) DDD의 엔터티/값객체/애그리거트/리파지토리 - 코드에서 객체 정의하기](https://appleg1226.tistory.com/43) (1) | 2022.02.20 |
| [(2) DDD의 도메인과 바운디드 컨텍스트 - 개발보다는 설계부터!](https://appleg1226.tistory.com/41) (3) | 2022.02.12 |
| [(1) DDD란 무엇인가 - 데이터 중심 개발과 도메인 중심 개발](https://appleg1226.tistory.com/40) (3) | 2022.02.06 |
