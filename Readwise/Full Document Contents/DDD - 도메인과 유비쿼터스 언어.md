# DDD - 도메인과 유비쿼터스 언어

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[JaeHoney]]
- Full Title: DDD - 도메인과 유비쿼터스 언어
- Category: #articles
- Document Tags:  #ddd 
- Summary: Using domain-specific terms in code is crucial for clarity and understanding. For example, replacing generic status codes with meaningful names helps developers grasp the logic without confusion. This approach not only improves code readability but also enhances collaboration among team members.
- URL: https://jaehoney.tistory.com/205

## Full Document
##### 도메인 용어

코드를 작성할 때 **도메인에서 사용하는 용어는 매우 중요**하다. 쇼핑몰 프로젝트에서 레거시한 DB 구조를 가지고 있다고 가정하자. Order 테이블에는 status라는 컬럼이 있다. status 컬럼에는 **"STEP1", "STEP2", "STEP3"... ,"STEP6"** 이라는 정보가 저장된다.

해당 코드를 Enum으로 다음과 같이 작성할 수 있다.

```
public Enum OrderStatus {
    STEP1, STEP2, STEP3, STEP4, STEP5, STEP6
}
```

실제 주문 상태는 ‘결제대기중’, ‘상품준비중’, ‘출고완료됨’, ‘배송중’, ‘배송완료’, '주문 취소'인데 기존의 DB에서 전체 상태를 6단계로 본 구조를 그대로 엔터티 속성으로 표현한 것이다.

해당 프로젝트를 맡은 작업자는 코드를 다음과 같이 작성할 수 있다.

```
if(state != OrderState.STEP1 && state != OrderState.STEP2) {
    // 처리
}
```

해당 로직이 어떤 처리를 하는 지 짐작이 가는가? 이 코드에서는 **도메인 규칙**이라는 중요한 개념이 빠졌다. 실제 이 코드의 의미를 이해하려면 STEP1과 STEP2가 각각 '결제 대기 중' 상태와 '상품 준비 중' 상태를 의미한다는 것을 알아야 한다.

다음 코드처럼 도메인 용어를 사용해서 OrderStatus를 구현하면 **해당 코드의 의미를 곰곰히 생각하고 들여다보는 아주 불필요한 노력을 하지 않아도 된다.**

```
public enum OrderState {
    PAYMENT_WAITNG, PREPARING, SHIPPED, DELIVERING, DELIVERY_COMPLETED, CANCLE
}
```

**도메인 용어를 최대한 코드에 반영하면 코드의 의미를 단번에 이해할 수 있다.** 즉, 코드를 분석하고 이해하는 시간과 노력을 줄이고 다른 곳에 더 집중할 수 있다. 도메인 언어를 사용하면 **협업할 때도 원활하게 소통**할 수 있다.

에릭 에반스는 도메인 주도 설계에서 언어의 중요함을 강조하기 위해 **유비쿼터스 언어(Ubiquitous language)**라는 용어를 사용한다. 전문가, 관계자, 개발자 등이 도메인과 관련된 **공통의 언어**를 만들고 이를 대화, 문서, 도메인 모델, 코드, 테스트 등 **모든 곳에서 같은 용어를 사용**한다.

##### 놓치기 쉬운 부분

도메인 모델이 상태를 검증하는 메서드를 구현할 때 is\_\_\_able이라는 메서드명으로 구현하는 경우가 많다. 아래의 메서드를 보자.

```
public void changeShippingInfo(ShippingInfo newShippingInfo) {
    if(!isShippingChangeable()) {
        throw new IllegalStateException("cant change shipping in " + state);
    }
    setShippingInfo(newShippingInfo);
}

private void isShippingChangeable() {
    return state == OrderStatus.PAYMENT_WAITING || state == OrderState.PREPARERING;
}
```

큰 문제는 없어 보인다. 하지만 '배송지 정보 변경 가능 여부 확인'을 하기 위해 isShippingChangeable() 메서드를 사용했는데 이런 형식으로 메서드를 사용하면 도메인을 파악하기 어렵다.

다음의 예시를 보자.

```
public void changeShippingInfo(ShippingInfo newShippingInfo) {
    verifyNotYetShipped();
    setShippingInfo(newShippingInfo);
}

private void verifyNotYetShipped() {
    if(state != OrderStatus.PAYMENT_WAITING && state != OrderState.PREPARERING) {
        return new IllegalStateException("aleady shipped");
    }
}
```

isShippingChangeable()대신에 verifyNotYetShipped()를 사용하면서 배송지 정보 변경은 출고 전에 가능하다는 요구사항을 잘 표현하고 있다.

도메인 용어를 코드에 최대한 표현하면 도메인을 효과적으로 이해할 수 있게 도와주고 협업과 소통을 용이하게 만든다.

##### Reference

* <http://www.yes24.com/Product/Goods/108431347>

###### '[Programming](https://jaehoney.tistory.com/category/Programming) > [DDD](https://jaehoney.tistory.com/category/Programming/DDD)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [DDD - JPA를 이용한 Repository, Entity 매핑 제대로 구현하기!](https://jaehoney.tistory.com/228) (0) | 2022.06.16 |
| [DDD - 애그리거트(Aggregate)를 잘 사용하는 방법들!](https://jaehoney.tistory.com/223) (0) | 2022.06.09 |
| [DDD - Infrastructure Layer 설계하는 방법 (+ DIP 제대로 사용하기)](https://jaehoney.tistory.com/221) (2) | 2022.06.05 |
| [DDD - 도메인이란 무엇인가? (+ 도메인 설계 예시)](https://jaehoney.tistory.com/203) (2) | 2022.05.24 |
