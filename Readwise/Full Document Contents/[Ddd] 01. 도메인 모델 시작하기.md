# [Ddd] 01. 도메인 모델 시작하기

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FtDUSF%2Fbtsb2ThsFOR%2FfCT4GU41fKYU8fGYY6vUk0%2Fimg.png)

## Metadata
- Author: [[솔솔]]
- Full Title: [Ddd] 01. 도메인 모델 시작하기
- Category: #articles
- Document Tags:  #ddd 
- Summary: 이 게시글은 "도메인 주도 개발 시작하기 : DDD 핵심 개념 정리부터 구현까지" 최범균 님의 책을 기반으로 작성하였습니다. DDD란? Domain Driven Design 의 약어 도메인 주도 설계로 도메인을 중점으로 설계하는 방식이다. 도메인이란? 우리가 온라인 서점을 구현해야한다고 가정해보면, 온라인 서점은 구현해야 할 소프트웨어의 대상 온라인 서점 안에는 책을 판매하는 데 필요한 상품 조회, 구매, 결제, 배송 추적 등의 기능이 필요 소프트웨어로 해결하고자 하는 문제 영역인 온라인 서점이 도메인에 해당한다. 도메인의 특징 한 도메인은 다시 하위 도메인으로 나뉠 수 있다. ex) 온라인 서점 도메인의 하위 도메인으로 회원, 카탈로그, 주문, 정산, 배송 등등 카탈로그 하위 도메인은 고객에게 구매할 ..
- URL: https://ddol.tistory.com/62

## Full Document
이 게시글은 "도메인 주도 개발 시작하기 : DDD 핵심 개념 정리부터 구현까지" 최범균 님의 책을 기반으로 작성하였습니다.

**DDD란?**

Domain Driven Design 의 약어

도메인 주도 설계로 도메인을 중점으로 설계하는 방식이다.

**도메인이란?**

우리가 온라인 서점을 구현해야한다고 가정해보면, 온라인 서점은 구현해야 할 소프트웨어의 대상

온라인 서점 안에는 책을 판매하는 데 필요한 상품 조회, 구매, 결제, 배송 추적 등의 기능이 필요

소프트웨어로 해결하고자 하는 문제 영역인 온라인 서점이 도메인에 해당한다.

**도메인의 특징**

![](https://blog.kakaocdn.net/dn/nFjQE/btsb1QSKOaJ/0NKWTWYC1HMAgbY5agf5Q1/img.png)
* 한 도메인은 다시 하위 도메인으로 나뉠 수 있다.
	+ ex) 온라인 서점 도메인의 하위 도메인으로 회원, 카탈로그, 주문, 정산, 배송 등등  
	
		- 카탈로그 하위 도메인은 고객에게 구매할 수 있는 상품 목록을 제공
		- 주문 하위 도메인은 고객의 주문을 처리
		- 혜택 하위 도메인은 쿠폰이나 특별 할인과 같은 서비스 제공
		- 배송 하위 도메인은 고객에게 구매한 상품을 전달하는 일련의 과정을 처리
* 한 하위 도메인은 다른 하위 도메인과 연동하여 완전한 기능을 제공한다.
	+ ex) 고객이 물건을 구매하면 주문, 결제, 배송, 혜택 하위 도메인의 기능이 엮이게 된다.

![](https://blog.kakaocdn.net/dn/cD147q/btsbSFSETDk/KPQfZgnfgKBZyFfnQX4aq1/img.png)
* 특정 도메인을 위한 소프트웨어라고 해서 도메인이 제공해야 할 모든 기능을 직접 구현하는 것은 아니다.
	+ 많은 온라인 쇼핑몰이 자체적으로 구축하는 것이 아니라 외부 배송 업체, 외부 결제 업체 시스템의 필요한 기능만 일부 연동한다.
* 도메인마다 고정된 하위 도메인이 존재하는 것은 아니다. 하위 도메인을 어떻게 구성할지 여부는 상황에 따라 달라진다.
	+ 기업 고객을 대상으로 대형 장비를 판매하는 곳은 온라인으로 카탈로그를 제공하고 주문서를 받는 정도만 필요할 것이고, 온라인 결제나 배송 추적과 같은 기능을 제공할 필요가 없다.
	+ 반면 의류나 액세서리처럼 일반 고객을 대상으로 물건을 판매한다면 카탈로그, 리뷰, 주문, 결제, 배송, 회원 기능 등이 필요할 것이다.

**도메인 모델**

* 특정 도메인을 개념적으로 표현한 것이다.
* 도메인 모델을 사용하면 여러 관계자들이 동일한 모습으로 도메인을 이해하고 도메인 지식을 공유하는 데 도움이 된다.
	+ 도메인 모델을 표현할 때 클래스 다이어그램이나 상태 다이어그램과 같은 UML 표기법만 사용해야 하는 것은 아니다.
	+ 도메인을 이해하는 데 도움이 된다면 표현 방식이 무엇인지는 중요하지 않다.
* 도메인 모델은 기본적으로 도메인 자체를 이해하기 위한 개념 모델이다.
	+ 개념 모델을 이용해서 바로 코드를 작성할 수 있는 것은 아니기에 구현 기술에 맞는 구현 모델이 따로 필요하다.
	+ 개념 모델과 구현 모델은 서로 다른 것이지만 구현 모델이 개념 모델을 최대한 따르도록 할 수는 있다.
* 하위 도메인과 모델
	+ 각 도메인에 따라 용어 의미가 결정되므로 여러 하위 도메인을 하나의 다이어그램에 모델링하면 안된다.
		- ex) 카탈로그 도메인와 배송 도메인 모델을 구분하지 않고 하나의 다이어그램에 함께 표시하게 되면, 이 안에서의 상품은 카탈로그의 상품과 배송의 상품 의미를 함께 제공하기때문에 온전한 카탈로그 도메인을 이해하는 데 방해가 된다.
	+ 모델의 각 구성요소는 **특정 도메인으로 한정할 때 비로소 의미가 완전해지기 때문에 각 하위 도메인마다 별도로 모델을 만들어야 한다.**

**도메인 모델 패턴**

일반적인 애플리케이션의 아키텍처는 네 개의 영역으로 구성된다.

\* 아키텍처란? 시스템, 소프트웨어 또는 하드웨어의 구조 또는 설계를 의미

* **표현** ( Presentation )
	+ 사용자의 요청을 처리하고 사용자에게 정보를 보여준다. 외부 시스템이 사용자가 될 수 도 있다.
	+ 화면의 요청 / 응답을 처리하는 곳이다.
	+ Controller
* **응용** ( Application )
	+ 사용자가 요청한 기능을 실행한다. 업무 로직을 직접 구현하지 않으며 도메인 계층을 조합해서 기능을 실행한다.
	+ 기능 별로 구분지어 처리하는 곳이다.
	+ Handler
* **도메인** ( Domain )
	+ 시스템이 제공할 도메인 규칙을 구현한다.
	+ Entity, domain Service, Repository
* **인프라스트럭처** ( Infrastructure )
	+ 데이터베이스나 메시징 시스템과 같은 외부 시스템과의 연동을 처리한다.
	+ Repository, Event

여기서 사용되는 도메인은 **도메인 모델 패턴을 의미**한다.

도메인 모델 패턴은 **도메인 계층을 객체 지향 기법으로 구현하는 패턴**이다.

\* 객체 지향 프로그래밍 (OOP - Object Oriented Programing)

객체를 중점으로 프로젝트를 구성한다.

이 객체는 상태와 행위를 가지며, 다른 객체와 상호작용하며 문제를 해결한다.

상태는 객체의 속성, 행위는 객체가 수행하는 작업을 뜻한다.

도메인 모델 패턴이 생소해 어렵게 느껴질 수 있지만 아래의 예제 소스로 이해하면 간단하다.

예제 소스는 주문 도메인의 일부 기능을 도메인 모델 패턴으로 구현한 것이다.

주문 상태가 주문 대기 중(PAYMENT\_WATING), 상품 준비 중(PREPARING)일 경우에만 배송지를 변경할 수 있다.

아래의 소스를 보면 배송지 정보 변경 가능 여부를 OrderStatus 클래스에서 isShippingChangeable()을 통해 체크하고 있다.

```
public class Order {
	private OrderStatus state;
    private ShippingInfo shippingInfo;
    
    public void changeShippingInfo(ShippingInfo newShippingInfo) {
    	if (!state.isShippingChangeable()) {
        	throw new IllegalStateException("can't change shipping in " + state);
        }
        this.shippingInfo = newShippingInfo;
    }
}

public enum OrderState {
	PAYMENT_WAITING {
    	public boolean isShippingChangeable() {
        	return true;
        }
    },
    PREPARING {
    	public boolean isShippingChangeable() {
        	return true;
        }
    },
    SHIPPED, DELIVERING, DELIVERY_COMPLETED;
    
    public boolean isShippingChangeable() {
        return false;
    }
}
```

큰 틀에서 보면 OrderStatus는 Order에 속한 데이터이므로 배송지 정보 변경 가능 여부 판단하는 소스를 Order로 이동할 수 있다.

Order로 이동한 것이 아래 소스이다.

```
public class Order {
	private OrderStatus state;
    private ShippingInfo shippingInfo;
    
    public void changeShippingInfo(ShippingInfo newShippingInfo) {
    	if (!isShippingChangeable()) {
        	throw new IllegalStateException("can't change shipping in " + state);
        }
        this.shippingInfo = newShippingInfo;
    }
    
    private boolean isShippingChangeable() {
    	return state == OrderStatus.PAYMENT_WAITING ||
        	state == OrderStatus.PREPARING;
    }
}

public enum OrderState {
	PAYMENT_WAITING, PREPARING, SHIPPED, DELIVERING, DELIVERY_COMPLETED;
}
```

현재 배송지 변경이 가능한지 판단하는 규칙으로 주문 상태만을 바라보지만, 추후 확장성을 고려하여 도메인에서 처리해야한다.

****핵심 규칙을 구현한 코드는 도메인 모델에만 위치하기 때문에**규칙이 바뀌거나 규칙을 확장해야 할 때 다른 코드에 영향을 덜 주고 변경 내역을 모델에 반영할 수 있게 된다.**

**개념 모델과 구현 모델**

* 개념 모델은 순수하게 문제를 분석한 결과물이다.
* 데이터베이스, 트랜잭션 처리, 성능, 구현 기술과 같은 것을 고려하고 있지 않기 때문에 실제 코드를 작성할 때 개념 모델을 있는 그대로 사용할 수 없다.
* 개념 모델을 구현 가능한 형태의 모델로 전환하는 과정을 거치게 된다.

**도메인 모델 도출**

* 도메인을 모델링할 때 기본이 되는 작업은 모델을 구성하는 핵심 구성요소, 규칙, 기능을 찾는 것이다.
* 이 과정은 **요구사항에서 출발**한다.

```
1. 최소 한 종류 이상의 상품을 주문해야 한다.
2. 한 상품을 한 개 이상 주문할 수 있다.
3. 총 주문 금약은 각 상품의 구매 가격 합을 모두 더한 금액이다.
4. 각 상품의 구매 가격 합은 상품 가격에 구매 개수를 곱한 값이다.
5. 주문할 때 배송지 정보를 반드시 지정해야 한다.
6. 배송지 정보는 받는 사람 이름, 전화번호, 주소로 구성된다.
7. 출고를 하면 배송지를 변경할 수 없다.
8. 출고 전에 주문을 취소할 수 있다.
9. 고객이 결제를 완료하기 전에는 상품을 준비하지 않는다.
```

* 주문 도메인과 관련된 몇가지 **요구사항을 나열하였을 때,** '출고 상태로 변경하기', '배송지 정보 변경하기', '주문 취소하기', '결제 완료하기' **기능을 제공**한다는 것이다.
* 이러한 **기능은 메서드로 추가**할 수 있고, **어떤 데이터로 구성**되는지 알 수 있다.
	+ 한 상품(product)을 얼마에(price) 몇 개 살지(quantity)를 담고 있고 구매 가격을 구하는 calculateAmounts() 로직을 구현할 수 있다.
* 요구사항을 통해 **각 항목간의** **관계**를 알 수 있다.
	+ Order는 한 개 이상의 OrderLine을 가질 수 있으므로 Order를 생성할 때 OrderLine 목록을 List로 전달한다.
* 도메인을 구현하다 보면 **특정 조건이나 상태에 따라** 제약이나 규칙이 달리 적용되는 경우가 많다.

**엔티티와 밸류**

* 도출한 모델은 **엔티티**(Entity)와 **밸류**(Value)로 구분할 수 있다.
* 엔티티와 밸류를 제대로 구분해야 도메인을 올바르게 설계하고 구현할 수 있기 때문에 이 둘의 차이를 명확하게 이해하는 것은 도메인을 구현하는 데 있어 중요하다.

**엔티티 타입**

* 각 엔티티는 서로 다른 식별자를 갖는다.
	+ ex) 주문 도메인에서 각 주문마다 서로 다른 주문번호가 존재하는데 이렇게 서로 다른 주문번호가 주문의 식별자가 된다.
* 식별자는 바뀌지 않고 고유해야 한다.
	+ 두 엔티티 객체의 식별자가 같으면 두 엔티티는 같다고 판단한다.
	+ equals() 와 hashCode() 메서드를 구현할 수 있다.

\* hashCode() : 객체의 해시 코드를 반환하는 메서드로 일반적으로 고유한 값이어야 하지만 서로 다른 객체의 해시 코드가 같을 수도 있다.

이를 해시 충돌이라고 하며, 충돌이 발생하는 경우 자료구조에서 성능이 저하될 수 있다. 해시 충돌을 최소화하기 위해 해시 함수의 품질을 높이는 것이 중요하다.

**엔티티의 식별자 생성**

엔티티의 식별자 생성하는 시점은 도메인의 특징과 기술에 따라 달라진다.

* **특정 규칙에 따라 생성**
	+ yyyyMMddHHmmss + 규칙 값
* **UUID나 Nano ID와 같은 고유 식별자 생성기 사용**
	+ 자바에서 제공하는 java.util.UUID를 사용하여 UUID를 생성할 수 있다.
* **값을 직접 입력**
	+ 회원의 아이디나 이메일과 같은 식별자로 직접 입력한다.
	+ 단, 중복해서 입력되지 않도록 사전에 방지하는 것이 중요하다.
* **일련번호 사용**
	+ 시퀀스나 DB의 자동 증가 칼럼 사용
		- ex) Auto Increament
	+ 자동 증가 칼럼은 DB 테이블에 데이터를 삽입하기 전 까지는 식별자를 알 수 없다.

**밸류 타입 Value**

* 개념적으로 완전한 하나를 표현할 때 사용한다.
	+ 아래 예제 코드처럼 받는사람 이름, 받는사람 핸드폰 번호는 하나의 밸류로 묶어 받는사람으로 표현할 수 있다.

```
public class ShippingInfo {
	private String receiverName;
    private String receiverPhoneNumber;
    private String shippingAddress1;
    private String shippingAddress2;
    private String shippingZipcode;
}

Value 사용하기
public class ShippingInfo {
	private Receiver receiver;
    private Address address;
}

public class Receiver {
	private String name;
    private String phoneNumber;
}

public class Address {
	private String address1;
    private String address2;
    private String zipcode;
}
```

* 밸류 타입이 꼭 두 개 이상의 데이터를 가져야 하는 것은 아니다.  

	+ 의미를 명확하게 하기 위해 private int price; 를 private Money price; 로 선언하여 사용할 수 도 있다.

```
public class Order {
//	private int price;
	private Money price;
}

public class Money {
	private int value;
}
```

* 밸류 타입을 불변으로 구현하는 이유 ( 불변 : 데이터 변경 기능을 제공하지 않는 타입)
	+ 안전한 코드를 작성할 수 있다.
	+ 데이터를 변경할 때는 set을 사용하지않고 new를 사용해 새로운 객체를 생성해서 반환한다.
		- set을 사용하여 값을 변경하게 되면 다른 참조 된 값과 데이터 일관성 문제가 발생할 수 있다.

**엔티티 식별자와 밸류 타입**

* 엔티티의 식별자의 실제 데이터는 String과 같은 문자열로 구성된 경우가 많다.
* 이렇게 되면 파악하는데 어려움이 있어 밸류를 사용하여 더욱 의미가 잘 드러나도록 할 수 있다.
* 아래 예제 코드를 보면 첫번째 id를 보는 것 보단 두번째 id를 보았을 때 더욱 명확하기 때문이다.

```
public class Order {
	private String id;
}

public class Order {
	private OrderNo id;
}
```

**도메인 모델에 set 메서드 넣지 않기**

* 도메인 모델에 get/set 메서드를 무조건 추가하는 것은 좋지 않은 버릇이다.
* 특히 set 메서드는 도메인의 핵심 개념이나 의도를 코드에서 사라지게 한다.
* 도메인 객체를 생성할 때 온전하지 않은 상태가 될 수 있다.
* 생성자를 사용하여 불완전한 상태로 사용되는 것을 막아야한다.
* 부득이하게 set 메서드를 사용해야한다면 private을 사용하여 외부에서 접근하지 못하도록 한다.

**DTO의 get/set 메서드**

* DTO는 Data Transfer Object 의 약자로 프레젠테이션 계층과 도메인 계층이 데이터를 서로 주고받을 때 사용하는 일종의 구조체
* 오래전 사용했던 프레임워크는 요청 파라미터나 DB 칼럼의 값을 설정할 때 set 메서드를 필요로 했기 때문에 어쩔 수 없이 get/set 메서드를 구현해야 했다.
* DTO가 도메인 로직을 담고 있지는 않기에 get/set 메서드를 제공해도 도메인 객체의데이터 일관성에 영향을 줄 가능성이 높지 않다.
* 요즘 개발 프레임워크나 개발 도구는 set 메서드가 아닌 private 필드에 직접 값을 할당할 수 있는 기능을 제공하고 있어 set 메서드 없이도 데이터를 전달 받을 수 있다.
* 이렇게 하면 DTO도 불변 객체가 되어 불변의 장점을 DTO까지 확장할 수 있다.

**도메인 용어와 유비쿼터스 언어**

코드를 작성할 때 도메인에서 사용하는 용어는 매우 중요하다.

```
public enum OrderState {
	STEP1, STEP2, STEP3, STEP4, STEP5, STEP6
}
```

주문 상태 값을 STEP1 ~ 6 으로 정의했을 때, 이 값을 이해하려면 STEP1 ~ 6이 무엇을 의미하는지 한참 걸린다.

```
public enum OrderState {
	PAYMENT_WAITING, PREPARING, SHIPPED, DELIVERING, DELIVERY_COMPLETED;
}
```

STEP1 ~ 6 이 아닌 도메인에서 사용하는 용어를 최대한 코드에 반영하면 코드를 도메인 용어로 해석하거나 도메인 용어를 코드로 해석하는 과정이 줄어든다.

이는 코드의 가독성을 높여서 코드를 분석하고 이해하는 시간을 줄여준다.

최대한 도메인 용어를 사용해서 도메인 규칙을 코드로 작성하게 되므로 의미를 변환하는 과정에서 발생하는 버그도 줄어든다.

에릭 에반스는 도메인 주도 설계에서 언어의 중요함을 강조하기 위해 유비쿼터스 언어라는 용어를 사용했다.

전문가, 관계자, 개발자가 도메인과 관련된 공통의 언어를 만들고 이를 대화, 문서, 도메인 모델, 코드, 테스트 등 모든 곳에서 같은 용어를 사용한다.

이렇게 하면 소통 과정에서 발생하는 용어의 모호함을 줄일 수 있고 개발자는 도메인과 코드 사이에서 불필요한 해석 과정을 줄일 수 있다.

[[ DDD ] 02. 아키텍처 개요

이 게시글은 "도메인 주도 개발 시작하기 : DDD 핵심 개념 정리부터 구현까지" 최범균 님의 책을 기반으로 작성하였습니다. [DDD] 01. 도메인 모델 시작하기 이 게시글은 "도메인 주도 개발 시작하기

ddol.tistory.com](https://ddol.tistory.com/63)
###### '[DDD](https://ddol.tistory.com/category/DDD)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [[ DDD ] 03. 애그리거트](https://ddol.tistory.com/65) (1) | 2023.05.02 |
| [[ DDD ] 02. 아키텍처 개요](https://ddol.tistory.com/63) (1) | 2023.04.30 |
