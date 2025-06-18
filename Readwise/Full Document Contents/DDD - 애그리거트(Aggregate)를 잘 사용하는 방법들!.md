# DDD - 애그리거트(Aggregate)를 잘 사용하는 방법들!

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcPHQuf%2FbtrDYL5IbB3%2F4Gex8OKyXz5s0Wl2Kk1IkK%2Fimg.png)

## Metadata
- Author: [[Jae Honey]]
- Full Title: DDD - 애그리거트(Aggregate)를 잘 사용하는 방법들!
- Category: #articles
- Document Tags:  #ddd 
- Summary: This text explains how to effectively use aggregates in domain-driven design. Aggregates help simplify complex domains by grouping related models, ensuring consistency and managing their lifecycle together. The aggregate root manages the domain rules and prevents direct changes to its components, promoting a clearer and more maintainable structure.
- URL: https://jaehoney.tistory.com/223

## Full Document
해당 포스팅은 **"도메인 주도 개발 시작하기"**라는 내용을 정리한 글입니다. 해당 도서는 아래 Link에서 확인할 수 있습니다.

-<http://www.yes24.com/Product/Goods/108431347>

#### 애그리거트

온라인 쇼핑몰 시스템을 개발할 때 다음 그림과 같이 **상위 수준의 개념을 이용해서 전체 모델을 정리**하면 전반적인 관계를 이해하는데 도움이 된다. 아래 그림을 보면 주문은 회원, 상품, 결제와 관련이 있다는 것을 쉽게 파악할 수 있다.

![](https://blog.kakaocdn.net/dn/cPHQuf/btrDYL5IbB3/4Gex8OKyXz5s0Wl2Kk1IkK/img.png)
다음은 상위 수준 모델을 개별 객체 단위로 다시 그린 것이다. 해당 그림은 **상위 수준에서의 개념 이해 없이 도출하려면 시간이 더 오래 걸린다.** 더 많은 코드를 보고 도메인 전문가와 더 많은 대화를 나눠야 비로소 상위 수준에서 모델 간의 관계가 이해되기 시작한다.

![](https://blog.kakaocdn.net/dn/pE6mx/btrDZvuNVFl/uVBqCbEY38XEKd8KZiWT7k/img.png)
백 개 이상의 테이블을 한 장의 ERD에 표시하면 **개별 테이블 간의 관계를 파악**하느라 **큰 틀에서 데이터 구조를 이해하기 어렵다.** 도메인 객체 모델도 마찬가지로 복잡해지면 **개별 구성요소 위주로 모델을 이해하게 되고 전반적인 구조나 큰 수준에서 도메인 간의 관계를 파악하기 어렵다.**

**주요 도메인 요소 간의 관계를 파악하기 어렵다는 것은 곧 코드를 변경하고 확장하는 것이 어려워진다는 것을 의미**한다.

상위 수준에서 모델이 어떻게 엮여 있는지 알아야 전체 모델을 망가뜨리지 않으면서 추가 요구사항을 모델에 반영할 수 있는데 세부적인 모델만 이해한 상태로는 코드를 수정하기 두렵기 때문에 코드 변경을 최대한 회피하는 쪽으로 요구사항을 협의하게 된다.

복잡한 도메인을 이해하고 관리하기 쉬운 단위로 만들려면 상위 수준에서 모델을 조망할 수 있는 방법이 필요한데 그 방법이 바로 **애그리거트**이다. 동일한 모델이지만 **애그리거트를 사용함으로써 모델 간의 관계를 개별 모델 수준과 상위 수준에서 모두 이해**할 수 있다.

![](https://blog.kakaocdn.net/dn/Ic6gP/btrDZHVshY9/OxCB1YyuFzoXUAY843xArK/img.png)
**애그리거트는** 모델을 이해하는데 도움을 줄 뿐만 아니라 **일관성을 관리하는 기준**이 된다. 애그리거트 단위로 일관성을 관리하기에 복잡한 도메인을 **단순한 구조**로 만들어줘서 **도메인 모델**을 보다 잘 이해할 수 있다. 복잡도가 낮아지는 만큼 **도메인 기능 확장과 변경을 더 쉽게 할 수 있다.**

애그리거트는 관련된 모델을 하나로 모았기 때문에 한 애그리거트에 속한 객체는 **유사하거나 동일한 라이프 사이클**을 갖는다. 도메인 규칙에 따라 최초 주문 시점에 일부 객체를 만들 필요가 없는 경우는 있지만 애그리거트에 속한 구성요소는 대부분 함께 생성되고 함께 제거된다.

무엇보다 애그리거트는 경계를 갖는다. **한 애그리거트에 속한 객체는 다른 애그리거트를 관리하지 않는다.** 이는 기능을 구현할 때 단위를 결정할 수 있게 가이드라인을 준다.

**오해**

흔히 'A가 B를 갖는다'로 설계할 수 있는 요구사항이 있다면 A와 B를 한 애그리거트로 묶어서 생각하기 쉽다. 하지만 **A가 B를 갖는다고 해서 반드시 A와 B를 한 애그리거트로 묶어야 하는 것은 아니다**.

가령 상품과 리뷰가 있을 때 상품과 리뷰는 **함께 생성되지도, 함께 변경되지도 않는다.** 그리고 **상품을 변경하는 것은 상품 담당자지만 리뷰를 변경하는 것은 고객**이다.

![](https://blog.kakaocdn.net/dn/b4Icco/btrDYK6O1vq/CzCEBXGSK4QntZaQ34IlNK/img.png)
이 경우 상품과 리뷰는 서로 다른 애그리거트에 속한다. 처음 도메인 모델을 만들기 시작하면 큰 애그리거트로 보이는 것들이 많지만, 경험이 생기고 도메인 규칙을 제대로 이해하면 **다수의 애그리거트가 한 개의 엔터티 객체만 갖는 경우가 많다.**

##### 애그리거트 루트

애그리거트는 여러 객체로 구성되기 때문에 한 객체만 상태가 정상이면 안 된다. **도메인 규칙을 지키기 위해 애그리거트에 속한 모든 객체가 정상 상태를 가져야 한다.**

가령, 주문 목록을 변경하면 주문의 totalAmount(주문 금액)도 다시 계산해서 맞춰야 한다. 그래서 **애그리거트 전체를 관리할 주체가 필요**한데 이 책임을 지는 것이 바로 **애그리거트의 루트 엔터티**이다.

![](https://blog.kakaocdn.net/dn/b0RPnx/btrD2HHOjkN/aXNTdrtNVIUjjNltPKj0rk/img.png)
주문 애그리거트에서 루트 역할을 하는 엔터티는 Order이다. OrderLine, ShippingInfo, Orderer 등 주문 애그리거트에 속한 모델은 루트인 Order에 직접 또는 간접적으로 속하게 된다.

##### 도메인 규칙과 일관성

애그리거트 루트가 단순히 애그리거트에 속한 객체를 포함하는 것으로 끝나는 것은 아니다. 애그리거트 루트의 핵심 역할은 **애그리거트의 일관성이 깨지지 않도록 하는 것**이다. 이를 위해 애그리거트 루트는 애그리거트가 제공해야 할 도메인 기능을 구현한다. 예를 들어 주문 애그리거트의 배송지 변경, 상품 변경과 같은 기능을 애그리거트 루트인 Order가 가진 메서드로 제공한다.

애그리거트 루트가 아닌 다른 객체가 애그리거트에 속한 객체를 직접 변경하면 안된다. 이는 애그리거트 루트가 강제하는 규칙을 적용할 수 없어 모델의 일관성을 깨는 원인이 된다.

```
ShippingInfo si = order.getShippingInfo();
si.setAddress(newAddress);
```

이 코드는 애그리거트 루트인 Order에서 ShippingInfo 를 가져와 직접 정보를 변경하고 있다. 주문 상태에 상관없이 배송지 변경하는데 이는 도메인 규칙을 무시하고 직접 DB 테이블의 데이터에 Update를 날리는 것과 같다.

일관성을 지키기 위해서는 다음과 같이 상태를 확인하는 로직을 서비스에 구현할 수 있다. 하지만 이렇게 되면 **동일한 검사 로직을 여러 Application Layer 서비스에서 중복으로 구현할 가능성이 높아진다.**

```
ShippingInfo shippingInfo = order.getShippingInfo();

// 주요 도메인 로직이 중복될 수 있음
if(state != OrderState.PATMENT_WATTING && state != OderState.WATTING) {
	throw new IllegalArguementException();
}
shippingInfo.setAddress(newAddress);
```

불필요한 중복을 피하고 애그리거트 루트를 통해서만 도메인 로직을 구현하게 만들려면 도메인 모델에 대한 다음의 두가지를 습관적으로 적용해야 한다.

* 단순히 필드를 변경하는 set 메서드를 공개(public) 범위로 만들지 않는다.
* 밸류 타입은 불변으로 구현한다.

**공개(public) setter**는 **중요 도메인의 의미나 의도를 표현하지 못하고** **도메인 로직이 도메인 객체가 아닌 Application 영역이나 Presentation 영역으로 분산**시킨다. 도메인 로직이 한 곳에 응집되지 않으므로 유지보수할 때 더 많은 시간과 노력이 필요하다. cancel, changePassword처럼 의미가 드러나는 이름을 사용하는 것이 바람직하다.

밸류는 불변 타입으로 구현한다. 밸류 객체의 값을 변경할 수 없으면 애그리거트 루트에서 밸류 객체를 구해도 값을 변경할 수 없기 때문에 애그리거트 외부에서 밸류 객체 상태를 변경할 수 없다. 즉, 애그리거트의 일관성이 꺠질 가능성이 그만큼 줄어든다.

```
public Order {
    private ShippingInfo shippingInfo;
    public void changeshippingInfo(ShippingInfo newShippingInfo) {
        verifyNotYetShipped();
        setShippingInfo(newShippingInfo);
    }
    //  set 메서드의 접근 허용 범위는 private이다.
    private void setShippingInfo(ShippingInfo newShippingInfo) {
        //  밸류가 불변이면, 새로운 객체를 할당해서 값을 변경해야 한다.
        //  불변이므로 this.shippingInfo.setAddress(newShippedInfo.getAddress())와 같은 코드를 사용할 수 없다.
        this.shippingInfo = newShippingInfo;
    }
}
```

두 가지 원칙을 지킨 예시이다. 도메인 규칙을 올바르게만 구현하면 애그리거트 전체의 일관성을 올바르게 유지할 수 있다.

##### 애그리거트 루트의 기능 구현

애그리거트 루트는 애그리거트 내부의 다른 객체를 조합해서 기능을 완성한다. 예를 들어 Order는 총 주문 금액을 구하기 위해 OrderLine 목록을 사용한다.

```
public class Order{
    private Money totalAmounts;
    private List<OrderLine> orderLines;
   
    private void calculateTotalAmounts() {
       	int sum = orderLines.stream()
                .mapToInt(ol -> ol.getPrice() * ol.quantity())
                .sum();
        this.totalAmounts = new Money(sum);
    }
}
```

애그리거트 루트는 **기능 실행을 위임**하기도 한다. 다음의 경우 Order의 changeOrderLines 메서드는 다음과 같이 내부의 orderLines 필드에 상태 변경을 위임하는 방식으로 기능을 구현한다.

```
public class Order{
    private OrderLines orderLines; 
    
    public void changeOrderLines(List<OrderLine> newLines){
    	orderLines.changeOrderLines(newLines);
        this.totalAmounts = orderLines.getTotalAmounts(); 
    }
}
```

##### 트랜잭션 범위

트랜잭션 범위는 작을수록 좋다. **잠금 대상이 많아진다는 것은 그만큼 동시에 처리할 수 있는 트랜잭션 개수가 줄어든다는 것**을 뜻하고 이는 전체적인 성능(처리량)을 떨어뜨린다.

동일하게 **한 트랜잭션**에서는 **한 개의 애그리거트만 수정**해야 한다. 이는 **애그리거트에서 다른 애그리거트를 변경하지 않는다는 것**을 뜻한다. 한 애그리거트에서 다른 애그리거트까지 변경하게 된다면 자신의 책임 범위를 넘어 다른 애그리거트의 상태까지 관리하게 되는데 이는 최대한 서로 독립적이어야 하는데 애그리거트의 결합도가 높아지게 된다.

부득이하게 한 트랜잭션에 두 개의 이상의 애그리거트를 수정해야 한다면 애그리거트에서 다른 애그리거트를 직접 수정하지 말고 **Application 서비스에서 두 애그리거트를 수정하도록 구현**해야한다.

도메인 이벤트를 사용하면 한 트랜젝션에 한개의 애그리거트를 수정하면서도 동기나 비동기로 다른 애그리거트 상태를 변경하는 코드를 작성할 수 있다. 이에 대해서는 다음에 다룬다.

일반적으로 한 트랜잭션에서 한 개의 애그리거트를 변경하는 것을 권장하지만 다음의 경우에는 한 트랜잭션에서 두 개 이상의 애그리거트를 변경하는 것을 고려할 수 있다.

* 팀 표준: 팀이나 조직 표준에 따라 usecase 와 관련된 Application 서비스의 기능을 한 트랜잭션으로 실행해야하는 경우가 있다. DB가 다른 경우 글로벌 트랜잭션을 반드시 사용하도록 규칙을 정하는 곳도 있다.
* 기술 제약: 기술적 제약으로 인해 이벤트 방식을 도입할 수 없는 경우 한 트랜잭션에서 다수의 애그리거트를 수정해서 일관성을 처리해야 한다.
* UI 구현의 편리: 운영자의 편리함을 위해 주문 목록 화면에서 여러 주문의 상태를 한 번에 변경하고 싶을 것이다. 이 경우 한 트랜잭션에서 여러 주문 애그리거트의 상태를 변경해야 한다.

##### 리포지터리와 애그리거트

애그리거트는 개념상 완전한 한 개의 도메인 모델을 표현하므로 객체의 영속성을 처리하는 리포지터리(Repository)는 애그리거트 단위로 존재한다.

Order, OrderLine을 물리적으로 각각의 별도 DB 테이블에 저장하더라도 Order가 애그리거트 루트이고 OrderLine은 애그리거트에 속하는 구성 요소이므로 Order를 위한 리포지터리만 존재한다.

새로운 애그리거트를 만들면 저장소에 애그리거트 전체를 영속화하고 애그리거트를 사용하려면 저장소에서 애그리거트를 읽어야 하므로 적어도 다음의 두 메서드를 제공해야 한다.

* save: 애그리거트 저장
* findById: ID로 애그리거트를 구함

어떤 기술을 이용해 리포지터리를 구현하느냐에 따라 애그리거트의 구현도 영향을 받는다. **JPA**를 사용하면 데이터베이스 관계형 모델에 객체 도메인 모델을 맞춰야할 가능성이 있다.

애그리거트는 개념적으로 하나이므로 리포지터리는 **애그리거트 전체를 영속화**해야 한다. 즉 Order 애그리거트와 관련된 테이블이 세 개라면 리포지터리를 통해 Order 애그리거트를 저장할 때 애그리거트 루트와 매핑되는 테이블 뿐만 아니라 **애그리거트에 속한 모든 구성요소**를 위한 테이블에 데이터를 저장해야 한다.

```
// 리포지터리에 애그리거트를 저장하면 애그리거트 전체를 영속화해야 한다.
orderRepository.save(order);
```

동일하게 애그리거트를 구하는 리포지터리 메서드는 **완전한 애그리거트를 제공**해야 한다.

```
// 리포지터리는 완전한 order를 제공해야 한다.
Order order = orderRepository.findById(orderId);

// order가 온전한 애그리거트가 아니면 기능 실행 도중 NullPointerException 등이 발생한다.
order.cancel();
```

##### ID를 이용한 애그리거트 참조

한 애그리거트에서 다른 애그리거트 참조한다는 것은 애그리거트의 루트를 참조한다는 것과 같다. **애그리거트 간의 참조는 필드를 통해 쉽게 구현**할 수 있다. 다음 그림은 Orerer가 주문한 회원을 참조하기 위해 회원 애그리거트 루트인 Member를 필드로 참조하는 것을 나타낸다.

![](https://blog.kakaocdn.net/dn/ApBTu/btrDZuCIrNm/8BXAKrkmUwHGkZnHMSCa7k/img.png)
필드를 이용해 다른 애그리거트를 직접 참조하는 것은 개발자에게 구현의 편리함을 제공한다. JPA를 사용하면 @ManyToOne, @OneToOne과 같은 애노테이션을 이용해서 연관된 객체를 로딩하는 기능을 제공하고 있으므로 필드를 이용해서 다른 애그리거트를 쉽게 참조할 수 있다.

ORM 기술 덕에 애그리거트 루트에 대한 참조를 쉽게 구현할 수 있고, get 메서드를 통해 애그리거트 참조를 사용하면 다른 애그리거트의 데이터를 객체 탐색을 통해 조회할 수 있지만, **필드를 이용한 애그리거트 참조는 아래와 같은 문제를 일으킬 수 있다.**

* 편한 탐색 오용
* 성능에 대한 고민
* 확장 어려움

가장 큰 문제는 **편리함 오용**이다. **한 애그리거트에서 다른 애그리거트 객체에 접근하면 상태를 변경할 수 있게 된다.** 이런 부분은 애그리거트 간의 **의존 결합도를 높여서 변경을 어렵게** 만든다. 두 번째는 **지연 로딩과 즉시 로딩 등을 고민**하게 만든다는 점이고, 마지막 문제는 **확장**이다. 부하 분산을 위해 **시스템을 분리하기가 어려워진다.**

이런 세 가지 문제를 완화할 수 있는 것이 **ID를 이용해서 다른 애그리거트를 간접적으로 참조**하는 것이다. 요즘은 JPA 컨퍼런스에서 많이 얘기가 나오고 있는 부분이다.

![](https://blog.kakaocdn.net/dn/bZAnDJ/btrDWJ0Pdcv/UHnrRG2nOtkT3SZfkeetPk/img.png)
**ID만 참조**하면 모든 객체가 참조로 연결되지 않고 **한 애그리거트에 속한 객체들만 참조로 연결**된다. 지연 로딩과 즉시 로딩을 고민할 필요도 없고 **애그리거트간의 경계를 명확히 하고 모델의 복잡도를 낮추는 효과**가 있다.

참조하는 애그리거트가 필요하면 Application 서비스에서 아이디를 이용해서 로딩하면 된다.

```
public class ChangeOrderService {
    @Transactional
    public void changeShippingInfo(OrderId id, ShippingInfo newShippingInfo,
            boolean useNewShippingAddrAsMemberAddr) {
        Order order = orderRepository.findById(id);
        if (order == null) throw new OrderNotFoundException();
        order.changeShippingInfo(newShippingInfo);
        if (useNewshippingAddrAsMemberAddr) {
            //  ID를 이용해서 참조하는 애그리거트를 구한다.
            Member member = customerRepository.findById(order.getOrderer().getMemberId());
            member.changeAddress(newShippingInfo.getAddress());
        }
    }
}
```

ID를 이용한 참조 방식을 사용하면 위에서 언급한 장점과 더불어 애그리거트별로 다른 구현 기술을 사용하는 것도 가능해진다.

예를 들어 뎅이터 무결성이 중요한 주문 애그리거트는 RDBMS에 저장하고 조회 성능이 중요한 상품 애그리거트를 NoSQL에 저장하고 각각의 Repository 구현체를 사용할 수 있다.

##### ID를 이용한 참조와 조회 성능

다른 애그리거트를 ID로 참조하면 참조하는 여러 애그리거트를 읽어야 할 때 조회 속도가 문제가 될 수 있다. 한 번에 모든 데이터를 조인으로 가져올 수 있음에도, 주문마다 상품 정보를 읽어오는 쿼리를 실행하는 **N+1 문제**가 발생할 수 있다.

```
Customer customer = customerRepository.findById(ordererId);
List<Order> orders = orderRepository.findByOrderer(ordererId);
List<OrderView> dtos = orders.stream()
        .map(order -> {
           ProductId prodId = order.getOrderLines().get(0).getProductId();
           //  각 주문마다 첫 번째 주문 상품 정보 로딩 위한 쿼리 실행
           Product product = productRepository.findById(prodId);
           return new OrderView(order, customer, product);
        }).collect(toList());
```

이 경우에는 **[객체 참조 방식 + 즉시로딩]**을 사용하지 않고 **[ID 참조 방식]**을 사용했기 때문에 발생하는 문제이다. 이를 개선하려면 별도의 DAO를 만들어서 Join을 이용한 전용 조회 쿼리를 사용하면 된다.

```
@Repository
public class JpaOrderViewDao implements OrderViewDao {
    @PersistenceContext
    private EntityManager em;

    @Override
    public List<OrderView> selectByOrder(String ordererId) {
        String selectQuery =
            "select new com.myshop.order.application.dto.OrderView(o, m, p) " +
            "from Order o join o.orderLines ol, Member m, Product p " +
            "where o.orderer.memberId.id = :ordererId " +
            "and o.orderer.memberId = m.id " +
            "and index(ol) = 0 " +
            "and ol.productId = p.id " +
            "order by o.number.number desc";

        TypedQuery<OrderView> query = em.createQuery(selectQuery, OrderView.class);
        query.setParameter("ordererId", ordererId);
        return query.getResultList();
    }
}
```

위 코드는 JPA를 사용해서 특정 사용자의 주문 내역을 보는 코드이다. 이 JPQL은 **Order 애그리거트와 Member 애그리거트, Product 애그리거트를 조인으로 한번에 조회**한다.

JPA를 사용하면 각 객체 간 모든 연관을 지연/즉시로딩으로 어떻게든 처리하고 싶은 욕구가 생길텐데 이는 실용적이지 않다. ID를 참조하여 애그리거트를 참조해도 한 번의 쿼리로 필요한 데이터를 로딩하는 것이 가능하다.

하지만, 만약 애그리거트마다 다른 저장소를 사용하는 경우라면 한 번의 쿼리로 관련 애그리거트를 조회할 수 없으므로 성능을 높이기 위해 **캐시**를 적용하거나 **조회 전용 저장소**를 구성한다. 코드가 복잡해진다는 단점이 있지만 시스템의 처리량을 높일 수 있다.

##### 애그리거트 간 집합 연관

애그리거트 간 1:N, M:N 연관에 대해 살펴보자. 이 두 연관은 **컬렉션**을 이용한 연관이다. 카테고리와 상품간의 연관이 대표적이다. 한 카테고리에 여러 상품이 속할 수 있으니 **1:N** 관계이다.

```
public class Category {
    
    private Set<Product> products;  //  다른 애그리거트에 대한 1:N 연관
    
    // ... 생략
}
```

보통 목록 관련 요구사항은 한 번에 전체 상품을 보여주기보다는 페이징을 이용해 제품을 나눠서 보여준다. 이 요구사항은 카테고리 입장에서 다음과 같은 방식으로 구현할 수 있다.

```
public class Category {
    private Set<Product> products;
    // ...
    public List<Product> getProducts(int page, int size) {
        List<Product> sortedProducts = sortById(products);
        return sortedProducts.subList((page - 1) * size, page * size);
    }
}
```

문제는 이 코드를 실제 DBMS와 연동해서 구현하면 Category에 속한 모든 Product를 조회하면서 성능에 심각한 문제를 일으킨다.

따라서 개념적으로는 애그리거트 간에 1:N 연관이 있더라도 **성능상 문제로 인해 애그리거트 간의 1:N 연관을 실제 구현에 반영하지 않는다.** 이때는 상품 입장에서 자신이 속한 카테고리를 N:1 로 연관지어 구하면 된다.

카테고리에 속한 상품 목록을 제공하는 Application 서비스는 ProductRepository를 이용해 **CategoryId가 지정한 카테고리 식별자인 Product 목록을 구한다.**

```
public class Product {
    // ...
    private CateogryId category;
    //...
}

public class ProductListService {
    public Page<Product> getProductOfCategory(Long categoryId, int page, int size) {
        Category category = categoryRepository.findById(categoryId);
        checkCategory(category);
        List<Product> products = productRepository.findByCategoryId(category.getId(), page, size);
        int totalCount = productRepository.countByCategoryId(category.getId());
        return new Page(page, size, totalCount, products);
    }
}
```

**M:N**

M:N 연관은 개념적으로 양쪽 애그리거트에 컬랙션으로 연관을 만든다. 앞서 1-N 연관처럼 **M-N 연관도 실제 요구사항을 고려해서 M-N 연관을 구현에 포함시킬지 결정**해야 한다.

보통 특정 카테고리에 속한 **상품 목록을 보여줄 때 각 상품이 속한 모든 카테고리 정보를 다 노출하지는 않는다.** 제품이 속한 모든 카테고리가 필요한 화면은 **상품 상세 화면**이다.

이러한 특징을 고려할 때 카테고리에서 상품으로의 연관은 필요하지 않다. **상품에서 카테고리로의 집합 연관만 존재**하면 된다.

즉 개념적으로 상품과 카테고리의 양방향 M-N 연관이 존재하지만 실제 구현에서는 상품에서 카테고리로의 단방향 M-N 연관만 적용하면 되는 것이다.

```
public class Product {
    private Set<CategoryId> categoryIds;
    // ...
}
```

RDBMS를 이용해 M:N 연관을 구현하려면 다음과 같이 조인 테이블을 사용한다.

![](https://blog.kakaocdn.net/dn/Wdf3K/btrEjjNykHK/baBryKXHtUh4ekeK6ZPPu1/img.png)
JPA를 이용하면 다음과 같은 매핑 설정을 사용해 ID 참조를 이용한 M-N 단방향 연관을 구현할 수 있다.

```
@Entity
@Table(name = "product")
public class Product {
    @EmbeddedId
    private ProductId id;
    
    @ElementCollection
    @CollectionTable(name = "product_category",
        joinColumns = @JoinColumn(name = "product_id"))
    private Sets<CategoryId> categoryIds;
    //...
}
```

이 매핑은 카테고리 ID목록을 보관하기 위해 밸류 타입에 대한 컬렉션 매핑을 이용했다. 이 매핑을 사용하면 JPQL의 member of 연산자를 이용해서 특정 Category에 속한 Product 목록을 구하는 기능을 구현할 수 있다.

```
@Repository
public class JpaProductRepository implements ProductRepository {
    @PersistenceContext
    private EntityManager entityManager;

    @Override
    public List<Product> findByCategoryId(CategoryId categoryid, int page, int size) {
        TypedQuery<Product> query = entityManager.createQuery(
            "select p from Product p " + 
            "where :catId member of p.categoryIds order by p.id.id desc", Product.class);
        query.setParameter("catId", categoryId);
        query.setFirstResult((page - 1) * size);
        query.setMaxResults(size);
        return query.getResultList();
    }
}
```

이 코드에서 `:catId member of p.categoryIds`는 categoryIds 컬렉션에 catId로 지정한 값이 존재하는지를 검사하기 위한 검색 조건이다. 응용 서비스는 이 기능을 사용해서 지정한 카테고리에 속한 Product 목록을 구할 수 있다.

##### 애그리거트를 팩토리로 사용하기

만약 고객이 특정 상점을 여러 차례 신고해서 해당 상점에서 더 이상 상품을 등록을 할 수 없도록 차단된 상태라고 해보자. 상품 등록 기능은 상점 계정이 차단 상태가 아닌 경우에만 상품을 구현할 수 있다.

```
public class RegisterProductService {
    public ProductId registerNewProduct(NewProductRequest req) {
        Store store = storeRepository.findStoreById(req.getStoreId());
        checkNull(account);
        if(account.isBlocked()) {
            throw new StoreBlockedExeption();
        }
        ProductId id = productRepository.nextId();
        Product product = store.createProduct(id, store.getId(), ...생략);
        productRepository.save(product);
        return id;
    }
}
```

이 코드는 Product를 생성 가능한지 판단하는 코드와 Product를 생성하는 코드가 분리되어 있다. 코드가 나빠 보이지는 않지만 **중요한 도메인 로직 처리가 응용 서비스에 노출**되었다.

이 도메인 기능을 넣기 위한 별도의 도메인 서비스나 팩토리 클래스를 만들 수도 있지만 **이 기능을 Store 애그리거트에 구현**할 수도 있다.

```
public class Store {
    public Product createProduct(ProductId newProductId, ...) {
        if (isBlocked()) throw new StoreBlockedException();
        return new Product(newProductId, getId(), ...);
    }
}
```

Store 애그리거트의 createProduct()는 Product 애그리거트를 생성하는 **팩토리** 역할을 한다. 이제 Application 서비스에서는 팩토리 기능을 이용하여 Product를 생성하면 된다.

```
public class RegisterProductService {
    public ProductId registerNewProduct(NewProductRequest req) {
        Store store = storeRepository.findStoreById(req.getStoreId());
        checkNull(store);
        ProductId id = productRepository.nextId();
        Product product = store.createProduct(id, /*...*/);
        productRepository.save(product);
        return id;
    }
}
```

응용 서비스에서 더 이상 Store의 상태를 확인하지 않고 해당 로직은 Store 도메인이 구현하고 있다. 이제 **Product 생성 가능 여부를 확인하는 도메인 로직을 변경해도 도메인 영역의 Store만 변경하면 되고 Application 서비스는 영향을 받지 않는다.** 도메인 응집도도 높아졌다.

이것이 애그리거트를 팩토리로 사용할 때 얻을 수 있는 장점이다.

추가로 만약 Store 애그리거트가 Product 애그리거트를 생성할 때 더 많은 정보를 알아야 한다면 Store 애그리거트에서 Product 애그리거트를 직접 생성하지 않고 **다른 팩토리에 위임**하는 방법도 있다.

```
public class Store {
    public Product createProduct(ProductId newProductId, ProductInfo pi) {
        if (isBlocked()) throw new StoreBlockedException();
        return new ProductFactory.create(newProductId, getId(), pi);
    }
}
```

다른 팩토리에 위임하더라도 차단 상태의 상점은 상품을 만들 수 없다는 도메인 로직은 한곳에 계속 위치하게 된다.

##### Reference

* <https://velog.io/@freesky/DDD-Start-%EC%95%A0%EA%B7%B8%EB%A6%AC%EA%B1%B0%ED%8A%B8>
* <http://www.yes24.com/Product/Goods/108431347>

 [저작자표시](https://creativecommons.org/licenses/by/4.0/deed.ko)
