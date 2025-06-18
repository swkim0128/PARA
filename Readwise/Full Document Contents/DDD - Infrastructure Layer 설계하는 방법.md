# DDD - Infrastructure Layer 설계하는 방법

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcsfDUH%2FbtrDZu3jue1%2Fnpva9u8PHSdEneCQZryCz0%2Fimg.png)

## Metadata
- Author: [[JaeHoney]]
- Full Title: DDD - Infrastructure Layer 설계하는 방법
- Category: #articles
- Document Tags:  #ddd 
- Summary: The article discusses how to design the Infrastructure Layer in Domain-Driven Development (DDD) while properly applying the Dependency Inversion Principle (DIP). It emphasizes that high-level modules should depend on low-level modules through interfaces to facilitate testing and flexibility. Additionally, it notes that the Infrastructure Layer supports other layers without affecting their definitions, allowing for easier implementation changes.
- URL: https://jaehoney.tistory.com/221

## Full Document
해당 포스팅은 **"도메인 주도 개발 시작하기"**라는 내용을 정리한 글입니다. 해당 도서는 아래 Link에서 확인할 수 있습니다.

- <http://www.yes24.com/Product/Goods/108431347>

#### Layer Architecture

아래는 계층 구조 아키텍처를 도식화한 그림이다.

![](https://blog.kakaocdn.net/dn/csfDUH/btrDZu3jue1/npva9u8PHSdEneCQZryCz0/img.png)
위의 계층 구조 아키텍처는 다음의 특징이 있다.

* 도메인의 복잡도에 따라 응용과 도메인을 분리하기도 하고 한 계층으로 합치기도 한다.
* 상위 계층에서 하위 계층으로 의존만 존재하고 하위 계층은 상위 계층에 의존하지 않는다.
* 응용계층이 도메인 뿐만 아니라 Infrastructure에 의존하기도 한다.
	+ **Infrastructure에 의존하면 테스트하기 어렵다.**
	+ **기능 확장이 어렵다.**
	+ 해결 방법은 **DIP**를 적용하는 것이다.

#### DIP(Dependency Inversion Principle)

DIP 원칙은 저수준 모듈이 고수준 모듈에 의존하게 해야 한다는 원칙이다. 즉, 의존 역전 원칙이라 부른다.

아래는 DIP를 잘 지킨 프로젝트 구조 예시이다.

![](https://blog.kakaocdn.net/dn/cyXQle/btrDZuPOZQA/OM1MOYtBPPaTfxcO1rGqG1/img.png)
만약 OrderService가 바로 **MybatisOrdersRepository를 의존**했다고 상상해보자. MybatisRepository를 JpaRepository나 QuerydslRepository로 **변경하기가 꺼려진다.**

추가로 MybatisRepository를 **의존하는 Service의 테스트를 진행하기도 어렵다.** 반면, DIP 원칙을 지키고 **인터페이스에만 의존한다면 해당 인터페이스의 구현체를 테스트용 대역 객체로 사용해 테스트가 가능**해진다.

예시에서는 이러한 문제에 대한 해결책으로 DIP를 훌륭하게 적용했다.

##### Infrastructure에서 고수준 모듈 구현

방금 언급한 DIP를 적용한 구조를 다시 보자. **Application Layer와 Domain Layer는 각 Layer에 속하는 저수준 모듈인 Interface에 의존**하고 있고, **저수준 모듈인 구현체를 Infrastructure Layer에서 구현**한다.

이러한 구조를 지킨다면 아키텍처 수준에서는 Infrastructure 영역이 Application 영역과 Domain 영역에 의존(상속)하는 구조가 된다.

![](https://blog.kakaocdn.net/dn/2KHJy/btrDYLYyvUV/6aqgMfxJvsPCy1AkaWe8O0/img.png)
외부 영역인 Infrastructure 영역이 변경되어도 **도메인이나 응용 영역에 정의한 인터페이스를 상속받아 구현**하고 있기 때문에, **도메인과 응용 영역에 영향을 주지 않거나 최소화**할 수 있고, **구현 기술을 변경하기가 용이**해진다.

##### DIP 주의 사항

아래는 잘못된 DIP 적용의 예시이다.

![](https://blog.kakaocdn.net/dn/dLBO6G/btrDWS5cDPs/NFPi5tOK09gWD8nM2YbAWk/img.png)
여기서 잘못된 점은 **DIP를 단순히 인터페이스와 구현 클래스의 분리로만 생각했기 때문**이다. 이는 명백히 잘못되었다.

DIP란 본래 저수준 모듈이 고수준 모듈에 의존하는 것을 말한다. 즉, **저수준 모듈인 할인 금액 계산을 추상화하는 인터페이스**는 **고수준 모듈인 CalculateDiscountService 관점으로 봤을 때** **단순히 할인 금액을 계산해주는 인터페이스**인 것이지 룰 엔진을 사용하거나 직접 연산을 사용하는 지는 중요하지 않다.

즉, **RuleEngine**은 인터페이스이지만 **고수준 모듈인 도메인 관점이 아닌** **엔진이라는 저수준 모듈 관점에서 도출**된 것이다. **DIP를 적용할 때 하위 기능을 추상화한 인터페이스는 고수준 모듈 관점에서만 도출**하여야 한다.

##### Aggregate 간의 요청

추가로 주의할 점은 외부(External) Module, System, API 등에 의존해야만 Infrastructure에 해당하는 것은 아니다.

Infrastructure Layer는 다른 Layer(Domain Layer와 Application Layer)에서 자신의 기능을 온전히 수행할 수 있도록 지원해주는 역할을 한다.

다른 Aggregate에 요청을 보내는 역할을 Infrastructure Layer에서 수행할 수 있다.

아래 클래스는 Order 애그리거트의 Infrastructure Layer에 해당한다.

```
@Service
class OrdererServiceImpl implements OrdererService {
    private MemberQueryService memberQueryService;

    public OrdererServiceImpl(MemberQueryService memberQueryService) {
        this.memberQueryService = memberQueryService;
    }

    @Override
    public Orderer createOrderer(MemberId ordererMemberId) {
        MemberData memberData = memberQueryService.getMemberData(ordererMemberId.getId());
        return new Orderer(MemberId.of(memberData.getId()), memberData.getName());
    }
}
```

해당 클래스는 Member 애그리거트에 요청해서 Order 애그리거트에서 사용할 Orderer를 생성하는 기능을 제공한다.

추가로 해당 클래스의 접근 제한자는 package-private으로 클래스 접근 제한자 중 가장 좁은 범위를 가짐으로써 외부인 InfraStructure에 의존하여 DIP를 깨뜨리는 것을 하지 못하게 강제할 수 있다.

##### Reference

* <https://nesoy.github.io/articles/2018-08/DDD-Architecture>

###### '[Programming](https://jaehoney.tistory.com/category/Programming) > [DDD](https://jaehoney.tistory.com/category/Programming/DDD)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [DDD - JPA를 이용한 Repository, Entity 매핑 제대로 구현하기!](https://jaehoney.tistory.com/228) (0) | 2022.06.16 |
| [DDD - 애그리거트(Aggregate)를 잘 사용하는 방법들!](https://jaehoney.tistory.com/223) (0) | 2022.06.09 |
| [DDD - 도메인과 유비쿼터스 언어](https://jaehoney.tistory.com/205) (0) | 2022.05.24 |
| [DDD - 엔터티와 밸류](https://jaehoney.tistory.com/204) (0) | 2022.05.24 |
| [DDD - 도메인이란 무엇인가? (+ 도메인 설계 예시)](https://jaehoney.tistory.com/203) (2) | 2022.05.24 |
