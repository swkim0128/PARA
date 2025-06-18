# DDD - 엔터티와 밸류

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZjK3Y%2FbtrC0MC2UGm%2FIbj51pp7uqsCtl8UM10Ehk%2Fimg.png)

## Metadata
- Author: [[JaeHoney]]
- Full Title: DDD - 엔터티와 밸류
- Category: #articles
- Document Tags:  #ddd 
- Summary: The text explains the distinction between entities and value types in domain-driven design (DDD). Entities have unique identifiers, like an order number, while value types represent a complete concept, such as a receiver or an address. Understanding these differences is crucial for correctly designing and implementing a domain model.
- URL: https://jaehoney.tistory.com/204

## Full Document
Programming/DDD

##### 엔터티와 밸류

도출한 도메인 모델은 크게 **엔터티(Entity**)와 **밸류(Value)**로 구분할 수 있다.

주문 도메인에서 만든 모델은 다음과 같다. 엔터티도 존재하고 밸류도 존재한다.

![](https://blog.kakaocdn.net/dn/ZjK3Y/btrC0MC2UGm/Ibj51pp7uqsCtl8UM10Ehk/img.png)
엔터티와 밸류를 제대로 구분해야 도메인을 올바르게 설계하고 구현할 수 있기에 이 둘의 차이를 명확하게 이해하는 것은 도메인을 구현하는 데 있어 중요하다.

##### 엔터티

엔터티의 가장 큰 특징은 **식별자**를 가진다는 것이다. 식별자는 엔티티의 객체마다 고유해서 각 엔티티는 서로 다른 식별자를 갖는다. 주문 도메인에서 각 주문은 주문번호를 갖는데 이 주문번호는 각 주문마다 서로 다르다. 따라서 주문번호가 주문의 식별자가 된다.

주문 도메인 모델에서 주문에 해당하는 클래스가 Order이므로 Order가 엔티티가 되며 주문번호를 속성으로 갖게 된다. 주문에서 배송지 주소가 바뀌거나 상태가 바뀌더라도 주문번호가 바뀌지 않는 것 처럼 엔티티의 식별자는 바뀌지 않는다.

엔티티를 생성하고 엔티티의 속성을 바꾸고 엔티티를 삭제할 때가지 식별자는 유지된다. 엔티티의 **식별자는 바뀌지 않고 고유**하다. 그래서 두 엔티티 객체의 식별자가 같으면 두 엔티티는 같다고 판단할 수 있다. 엔티티의 구현한 클래스는 식별자를 이용해서 equals()메서드와 hashCode()메서드를 구현할 수 있다.

```
public class Order {
    private String orderNumber;

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null) return false;
        if(obj.getClass() != Order.class) return false;
        Order other = (Order)obj;
        if(this.orderNumber == null) return false;
        return this.orderNumber.equals(other.orderNumber);
    }
    
    
    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((orderNumber == null) ?  0: orderNumber.hashCode());
        return result;
    }
}
```

##### 밸류타입

ShippingInfo 클래스는 다음과 같이 받는 사람과 주소에 대한 데이터를 갖고 있다.

```
public class ShippingInfo {
    // 받는 사람
    private String receiverName;
    private String receiverPhoneNumber;
  
    // 주소
    private String shippingAddress1;
    private String shippingAddress2;
    private String shippingZipcode;
}
```

ShippingInfo 클래스의 receiverName 필드와 receiverPhoneNumber 필드는 서로 다른 두 데이터를 담고 있지만 두 필드는 개념적으로 받는 사람을 의미한다. 두 필드는 실제로 하나의 개념을 표현하고 있다.

shippingAddress1 필드 shippingAddress2 필드, shippingZipcode 필드도 주소라는 하나의 개념을 표현한다. 밸류타입은 개념적으로 완전한 하나를 표현할 때 사용한다.

여기서 받는 사람을 위한 밸류 타입으로 Receiver를 만들 수 있다.

```
public class Receiver {
    private String name;
    private String phoneNumber;
  
    public Receiver(String name, String phoneNumber) {
        this.name = name;
        this.phoneNumber = phoneNumber;
    }
  
    public String getName() {
        return name;
    }
  
    public String getPhoneNumber() {
        return phoneNumber;
    }
}
```

Receiver는 '받는 사람'이라는 도메인 개념을 표현한다. 앞서 ShippingInfo의 receiverName필드와 receiverPhoneNumber 필드가 이름을 갖고 받는 사람과 관련된 데이터라는 것을 유추한다면 Receiver는 그 자체로 받는 사람을 뜻한다. 이렇게 적절한 **밸류 타입을 사용함으로써 개념적으로 완전한 하나를 잘 표현할 수 있다.**

ShippingInfo의 주소 관련 데이터도 다음의 Address 밸류타입을 사용해서 보다 명확하게 표현할 수 있다.

```
public class Address {
    private String address1;
    private String address2;
    private String zipCode;
    
    //  ...equals() 재정의
}
```

이제 밸류타입을 통해 ShippingInfo 클래스를 다시 구현해보자.

```
public class ShippingInfo {
    private Receiver receiver;
    private Address address;
    
    //  ...equals() 재정의
}
```

##### 밸류 타입은 반드시 여러 개의 데이터 ?

**밸류타입이 꼭 두개 이상의 데이터를 가져야 하는 것은 아니다.** 의미를 명확하게 표현하기 위해 밸류 타입을 사용하는 경우도 있다. 주문 항목을 뜻하는 OrderLine을 보자.

```
public class OrderLine {
    private Product product;
    private int price;
    private int quantity;
    private int amounts;
}
```

OrderLine의 price와 amounts는 int 타입의 숫자를 사용하고 있지만 이들은 '돈'을 의미하고 있다. **돈을 의미하는 Money 타입**을 만들어서 사용하면 코드를 이해하는데 도움이 된다.

```
public class Money {
    private int value;
    
    public Money(int value) {
        this.value = value;
    }
    
    public int getValue() {
        return value;
    }
}
```

다음은 Money를 사용하도록 OrderLine을 변경한다. Money타입을 사용해서 price나 amounts가 금액을 의미한다는 것을 쉽게 알수 있다.

```
public class OrderLine {
    private Product product;
    private Money price;
    private int quantity;
    private Money amounts;
}
```

밸류타입의 또 다른 장점은 **밸류 타입을 위한 기능을 추가** 할 수 있다는 것이다. 다음과 같이 Money 타입은 돈 계산을 위한 기능을 추가할 수 있다.

```
public class Money {
    private int value;

    ... 생성자, getter()

    public Money add(Money money) {
        return new Money(this.value + money.value);
    }

    public Money multiply(int multiplier) {
        return new Money(value * multiplier) ;
    }
}
```

int를 필드로 가지고 단순 정수 연산을 할 때 보다 더 좋은 가독성을 가진다.

##### 도메인 모델에 set 메서드 넣지 않기

get/set을 도메인 모델에서 남발하지 않아야 한다는 것은 다들 알 것이다. 우리는 변경 가능한 값에 대해서만 set 메서드를 사용한다. 그런데, 변경 가능한 값이어도 set 메서드를 사용할 때는 각별히 주의해야 한다.

**set 메서드는 도메인의 핵심 개념이나 의도를 코드에서 사라지게 한다.** 다음의 예시를 보자.

```
public class Order {

    ...
    
    public void setOrderState(OrderState state) {
        this.state = state;
    }

    public void setShippingInfo(ShippingInfo shippingInfo) {
        this.shippingInfo = shippingInfo;
    }
}
```

changeShippingInfo()가 배송지 정보를 새로 변경한다는 의미를 가졌다면 setShippingInfo()메서드는 단순히 배송지 값을 설정한다는 것을 뜻한다. complatePayment()는 결제가 완료 햇다는 의미를 갖는 반면에 setOrderState()는 단순히 주문 상태값을 설정한다는 것을 뜻한다.

도메인을 위주로 구현한다면 **주문 상태 수정보다는 결제 완료가 더 자연스럽다.** complatePayment()는 결제 완료와 관련된 처리 코드를 함께 구현하기 때문에 결제 완료와 관련된 도메인 지식을 코드로 구현하는 것이 자연스럽다. setOrderState()는 단순히 상태 값만 변경할지 아니면 상태값에 따라 다른 처리를 위한 코드를 함께 구현할지 애매하다.

이렇게 습관적으로 구현하던 **set 메서드는 필드값만 변경하고 끝나기 때문에 상태 변경과 관련된 도메인 지식이 코드에서 사라지게 된다.**set메서드의 또 다른 문제는 **도메인 객체를 생성할 때 완전한 상태가 아닐 수도 있다는 것**이다. 비즈니스 로직을 검사하는 코드를 set 메서드에 위치하는 것은 이상하다. 그러면 Service Layer나 다른 곳에서 검사를 한 후 set 메서드를 호출하는 방식으로 구현해야 한다. 그러면 **해당 도메인 객체는 외부 결합도가 높아지고 자율적인 객체가 아니게 된다.**

다른 예시를 보자.

```
public class Order {
    public Order(Orderer orderer, List<OrderLine> orderLines,
            ShippingInfo shippingInfo, OrderState state) {
        setOrderer(orderer);
        setOrderLines(orderLines);
        ...
    }

    private void setOrderer(Orderer orderer) {
        if(orderer == null) {
            throw new IllegalArgumentException("no orderer");
        }
        this.orderer = orderer;
    }

    private void setOrderLines(List<OrderLine> orderLines) {
        verifyAtLeastOneOrMoreOrderLines(orderLines);
        this.orderLines = orderLines;
        calculateTotalAmounts();
    }
    ...
}
```

이 코드의 set메서드는 앞서 언급한 set 메서드와 중요한 차이점이 있는데 범위가 **private**라는 점이다. 이 코드에서 set 메서드는 **클래스 내부**에서 데이터를 변경할 목적으로 사용된다.

접근 제한자가 private이기 때문에 외부에서 데이터를 변경할 목적으로 set 메서드를 사용할 수 없다. **불변** 밸류 타입을 사용하면 자연스럽게 밸류 타입에는 set메서드를 구현하지 않는다. set 메서드를 구현해야 할 특별한 이유가 없다면 불변 타입의 장점을 살릴 수 있도록 밸류 타입은 불변으로 구현한다.

##### Reference

* <https://velog.io/@freesky/DDD-Start-Domain-2>
* <http://www.yes24.com/Product/Goods/108431347>

###### '[Programming](https://jaehoney.tistory.com/category/Programming) > [DDD](https://jaehoney.tistory.com/category/Programming/DDD)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [DDD - JPA를 이용한 Repository, Entity 매핑 제대로 구현하기!](https://jaehoney.tistory.com/228) (0) | 2022.06.16 |
| [DDD - 애그리거트(Aggregate)를 잘 사용하는 방법들!](https://jaehoney.tistory.com/223) (0) | 2022.06.09 |
| [DDD - Infrastructure Layer 설계하는 방법 (+ DIP 제대로 사용하기)](https://jaehoney.tistory.com/221) (2) | 2022.06.05 |
| [DDD - 도메인이란 무엇인가? (+ 도메인 설계 예시)](https://jaehoney.tistory.com/203) (2) | 2022.05.24 |
