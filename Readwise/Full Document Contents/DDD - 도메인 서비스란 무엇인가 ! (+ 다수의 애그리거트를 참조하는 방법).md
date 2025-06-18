# DDD - 도메인 서비스란 무엇인가 ?! (+ 다수의 애그리거트를 참조하는 방법)

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[JaeHoney]]
- Full Title: DDD - 도메인 서비스란 무엇인가 ?! (+ 다수의 애그리거트를 참조하는 방법)
- Category: #articles
- Document Tags:  #ddd 
- Summary: The text explains the concept of domain services in Domain-Driven Design (DDD), highlighting their role in handling complex calculations that involve multiple aggregates. It emphasizes that domain services should be stateless and separate from domain entities to keep the code clean and manageable. Additionally, it advises against tightly coupling domain services with specific technologies to maintain flexibility and facilitate test-driven development.
- URL: https://jaehoney.tistory.com/248

## Full Document
해당 포스팅은 **"도메인 주도 개발 시작하기"**라는 내용을 정리한 글입니다. 해당 도서는 아래 Link에서 확인할 수 있습니다.

-<http://www.yes24.com/Product/Goods/108431347>

##### 여러 애그리거트가 필요한 기능

도메인 영역의 코드를 작성하다 보면 한 애그리거트로 기능을 구현할 수 없을 때가 있다. 결제 금액 계산 로직의 예로 살펴보자.

* 상품 애그리거트 : 구매하는 상품의 가격이 필요하다. 또한 상품에 따라 배송비가 추가되기도 한다.
* 주문 애그리거트 : 상품별로 구매 개수가 필요하다.
* 할인 쿠폰 애그리거트 : 쿠폰별로 지정한 할인 금액이나 비율에 따라 주문 총 금액을 할인한다.
* 회원 애그리거트 : 회원 등급에 따라 추가 할인이 가능하다.

이 경우 실제 결제 금액을 계산하는 주체는 어떤 애그리거트일까?

생각해볼 수 있는 방법은 주문 애그리거트에서 필요한 데이터를 모두 가지도록 한 뒤 할인 금액 계산을 수행하는 것이다.

```
public class Order {
    ...
    private Orderer orderer;
    private List<OrderLine> orderLines;
    private List<Coupon> usedCoupons;
    
    private Money calculatePayAmounts() {
        Money totalAmounts = calculateTotalAmounts();
        // 쿠폰 별로 할인 금액 계산
        Money discount = counts.stream()
                .map(coupon -> calculateDiscount(coupon)
                .reduce(Money(0), (v1, v2) -> v1.add(v2));
        // 회원에 따른 추가 할인 계산
        Money membershipDiscount = calculateDiscount(orderer.getMember().getGrade());
        // 실제 결제 금액 계산
        return totalAmount.minus(discount).minus(membershipDiscount);
    }
    
    private Money calculateDiscount(Coupon coupon) {
        // orderLines의 각 상품에 대해 쿠폰을 적용해서 할인 금액을 계산하는 로직
        // 쿠폰의 적용 조건 등을 확인하는 코드
        // 정책에 따라 복잡한 if-else와 계산 코드
        ...
    }
    
    private Money caculateDiscount(MemberGrade grade) {
        // 등급에 따라 할인 금액 계산
        ...
    }
}
```

이렇게 **한 애그리거트에 넣기 애매한 도메인 기능을 억지로 특정 애그리거트에 구현하면 안된다.** 이는 코드가 길어지고 외부에 대한 의존이 높아지게 되며 코드를 복잡하게 만들고 도메인 개념이 가려지는 요인이 된다.

이러한 문제를 해결할 수 있는 좋은 방법은 도메인 기능을 별도 서비스로 구현하는 것이다.

##### 도메인 서비스

도메인 서비스는 **도메인 영역에 위치**한 도메인 로직을 표현할 때 사용한다. 주로 다음 상황에서 도메인 서비스를 사용한다.

* 계산 로직: 여러 애그리거트가 필요한 계산 로직이나 한 애그리거트에 넣기에는 다소 복잡한 계산 로직
* 외부 시스템 연동: 구현하기 위해 타 시스템을 사용해야 하는 도메인 로직

도메인 영역의 엔터티 요소와 도메인 서비스의 다른 점은 도메인 서비스는 상태 없이 로직만 구현한다는 점이다.

```
public class DiscountCalculationService {
    public Money calculateDiscountAmounts (List<OrderLine> orderLines,
            List<Coupon> coupons, MemberGrade grade) {
            
        Money couponDiscount = coupons.stream()
                .map(coupon -> calculateDiscount(coupon))
                .reduce(Money(0), (v1, v2) -> v1.add(v2));

        Money membershipDiscount = calculateDiscount(grade);
        
        return couponDiscount.add(menbershipDiscount);
    }
    private Money calculateDiscount(Coupon coupon) { ... }
    private Money calculateDiscount(MemberGrade grade) { ... }
}
```

할인 계산 서비스를 사용하는 주체는 애그리거트가 될 수도 있고 응용 서비스가 될 수도 있다. DiscountCalculationService를 전달하기만 하면 사용 주체는 애그리거트가 될 수 있다.

```
public class Order {
    public void calculateAmounts(
            DiscountCalculationService disCalSvc, MemberGrade grade) {
            
        Money totalAmounts = getTotalAmounts();
        Money discountAmounts =
            disCalSvc.calculateDiscountAmounts(this.orderLines, this.coupons, grade);
        this.paymentAmounts = totalAmounts.minus(discountAmounts);
    }
    ...
```

응용 서비스는 애그리거트 객체에 도메인 서비스를 전달한다.

```
public class OrderService {
    private DiscountCalculationService discountCalculationService;

    @Transactional
    public OrderNo placeOrder(OrderRequest orderRequest) {
    	OrderNo orderno = orderRepository.nextId();
    	Order order = createOrder(orderNo, orderRequest);
    	orderRepository.save(order);
    	// 응용 서비스 실행 후 표현 영역에서 필요한 값 리턴
    	return orderNo;
    }

    private Order createOrder(OrderNo orderNo, OrderRequest orderReq) {
    	Member member = findMember(orderReq.getOrdererId());
    	Order order = new Order(orderNo, orderReq.gerOrderLines(),
    	        orderReq.getCoupons(), createOrderer(member),
    	        orderReq.getShippingInfo());
    	order.calculateAmounts(this.discountCalculationService, member.getGrade());
    	return order;
    }
    ...
}
```

도메인 서비스를 도메인 객체가 의존하는 방법도 있다. 하지만 이는 좋은 방법이 아니다.

* 도메인 객체는 필드(Property)로 구성된 데이터와 메서드를 이용해서 개념적으로 하나인 모델을 표현한다.
	+ 도메인 서비스 필드는 데이터와 전혀 관계가 없다.
* 도메인 서비스는 일부 기능에만 필요하다. 일부 기능을 위해 의존을 주입할 이유는 없다.

반대로 도메인 서비스의 기능을 실행하기 위해 애그리거트를 전달하기도 한다.

```
public class TransferService {
    public void transfer(Account fromAcc, Account toAcc, Money amounts) {
        fromAcc.withdraw(amounts);
        toAcc.credit(amounts);
    }
}
```

응용 서비스는 두 Account를 도메인 서비스에 전달하고 TransferService는 계좌 이체 도메인 기능을 실행한다.

도메인 서비스는 도메인 로직을 수행하지 응용 로직을 수행하지 않는다. 트랜잭션 처리와 같은 로직은 응용 로직이므로 도메인 서비스가 아닌 응용 서비스에서 처리해야 한다.

도메인 로직과 응용 로직을 잘 파악해서 분리시키는 것이 좋은 코드를 만든다.

**<참고>**

> 도메인 서비스가 특정 기술에 의존하거나 외부 시스템의 API를 호출한다면 도메인 영역의 도메인 서비스는 인터페이스로 추상화 하고 Infrastructure 영역에서 구현해야 한다.  
>   
> 이를 통해 도메인 영역이 특정 구현에 종속되는 것을 방지할 수 있고 테스트 주도적인 개발이 가능하다.

##### Reference

* <https://incheol-jung.gitbook.io/docs/study/ddd-start/7>
* <https://kingds.tistory.com/112>

###### '[Programming](https://jaehoney.tistory.com/category/Programming) > [DDD](https://jaehoney.tistory.com/category/Programming/DDD)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [DDD - 바운디드 컨텍스트란 무엇인가 ?!](https://jaehoney.tistory.com/252) (0) | 2022.07.25 |
| [DDD - 트랜잭션과 잠금을 관리하는 다양한 방법!](https://jaehoney.tistory.com/251) (0) | 2022.07.19 |
| [DDD - 표현 영역과 응용 서비스! (+ 값 검증, 권한 검사, ...)](https://jaehoney.tistory.com/247) (6) | 2022.07.13 |
| [DDD - 응용 서비스 제대로 구현하기!](https://jaehoney.tistory.com/231) (0) | 2022.06.23 |
| [DDD - JPA를 이용한 Repository, Entity 매핑 제대로 구현하기!](https://jaehoney.tistory.com/228) (0) | 2022.06.16 |
