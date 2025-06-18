# DDD - 이벤트란 무엇인가 ?! (+ 마이크로 서비스 간 트랜잭션 처리)

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fk8yse%2FbtrIfSdRQkS%2FV2WRKrXN6zpKVktRZILOk1%2Fimg.png)

## Metadata
- Author: [[JaeHoney]]
- Full Title: DDD - 이벤트란 무엇인가 ?! (+ 마이크로 서비스 간 트랜잭션 처리)
- Category: #articles
- Document Tags:  #ddd 
- Summary: 이 글은 도메인 주도 개발에서 이벤트의 중요성과 비동기 이벤트 처리 방법을 설명합니다. 이벤트를 사용하면 시스템 간의 결합을 줄이고 기능 확장이 용이해집니다. 또한, 트랜잭션 처리 시 외부 서비스의 영향을 최소화하는 방법도 제시합니다.
- URL: https://jaehoney.tistory.com/254

## Full Document
해당 포스팅은 **"도메인 주도 개발 시작하기"**라는 내용을 정리한 글입니다. 해당 도서는 아래 Link에서 확인할 수 있습니다.

-<http://www.yes24.com/Product/Goods/108431347>

##### 시스템 간 강결합 문제

쇼핑몰에서 구매를 취소하려면 환불을 처리해야 한다. 이때 환불 기능을 실행하는 주체가 도메인 엔터티가 될 수 있다. 아래와 같이 환불 기능을 제공하는 도메인 서비스를 파라미터로 전달받아 사용할 수 있다.

```
public class Order {

    // 외부 서비스를 실행하기 위해 도메인 서비스를 파라미터로 전달 받음
    public void cancel(RefundService refundService) {
        // 주문과 관련된 로직
        verifyNotYetShipped();
        this.state = OrderState.CANCELED;
        
        this.refundStatus = State.REFUND_STARTED;
        // 결제와 관련된 로직
        try {
            refundService.refund(getPaymentId());
            this.refundStatus = State.REFUND_COMPLETED;
        } catch (Exception e) {
            ...
        }
    }
}
```

반면 응용 서비스에서 환불 기능을 실행할 수도 있다.

```
public class CancelOrderService {
    private RefundService refundService;

    @Transactional
    public void cancel(OrderNo orderNo) {
        Order order = findOrder(orderNo);
        order.cancel();

        order.refundStarted();
        try {
            refundService.refund(order.getPaymentId());
            order.refundCompleted();
        } catch (Exception e) {
            ...
        }
    }
}
```

문제는 결제 시스템은 외부에 존재한다는 점이다. 즉, RefundService는 외부에 있는 결제 시스템이 제공하는 환불 서비스를 호출한다. 이때 두 가지 문제가 발생할 수 있다.

* 외부 서비스가 정상이 아닐 경우 트랜잭션 처리가 애매하다. 다음의 두 방법을 고려할 수 있다.  

	1. 주문 취소 트랜잭션을 롤백하는 방식
	2. 주문은 취소 상태로 변경하고 환불만 나중에 다시 시도하는 방식
* 환불을 처리하는 외부 시스템의 응답 시간이 길어지면 그만큼 대기 시간도 길어진다.
	+ 즉, 외부 서비스 성능에 의해 시스템이 직접적인 영향을 받게 된다.

만약 주문 취소 처리 뿐만 아니라 취소 내용을 통지해야하는 서비스까지 기능이 추가된다면 어떻게 될까? 외부 서비스는 두 개로 증가하고, 트랜잭션 처리가 더 복잡해진다.

이런 문제가 발생하는 원인은 주문 바운디드 컨텍스트와 결제 바운디드 컨텍스트 간의 강결합(high coupling) 때문이다. 강한 결합을 없앨 수 있는 방법이 하나 있는데, 바로 **이벤트**를 사용하는 것이다. 특히 비동기 이벤트를 사용하면 두 시스템 간의 결합을 크게 낮출 수 있다.

한번 익숙해지면 모든 연동을 이벤트와 비동기로 처리하고 싶을 정도로 강력하고 매력적인 것이 이벤트이다.

##### 이벤트

이벤트(event)는 '과거에 발생한 어떤 일'을 의미한다. 예를 들어 주문 취소 이벤트가 발생했다고 말할 수 있다.

이벤트는 발생하는 것에 끝나지 않는다. 이벤트가 발생하면 원하는 동작을 수행하는 기능을 구현한다. 아래 코드는 jQuery에서 클릭 이벤트가 발생했을 때 해당 이벤트에 반응하여 경고 창을 출력한다.

```
$("#myBtn").click(function(evt){
    alert("경고");
});
```

도메인 모델에서도 도메인의 상태 변경을 이벤트로 표현할 수 있다. 즉, 아래와 같은 처리가 가능해진다.

('주문 취소 이벤트가 발생할 때 -> '이메일을 보낸다')

![](https://blog.kakaocdn.net/dn/k8yse/btrIfSdRQkS/V2WRKrXN6zpKVktRZILOk1/img.png)
이벤트 모델에 이벤트를 도입하려면 네 개의 구성요소를 구현해야 한다.

* 이벤트
	+ 이벤트 생성 주체의 상태 변경
* 이벤트 생성 주체
	+ 엔터티, 밸류, 도메인 서비스와 같은 도메인 객체
* 이벤트 디스패처(퍼블리셔)
	+ 이벤트 생성 주체의 이벤트를 전달 받아서 핸들러에 이벤트를 전파
* 이벤트 핸들러(구독자)
	+ 이벤트 생성 주체가 발생한 이벤트에 반응해서 원하는 기능을 실행

이때 이벤트는 다음의 구성 요소를 포함한다.

* 이벤트 종류 - 클래스 이름으로 이벤트 종류를 포함
* 이벤트 발생 시간
* 추가 데이터 - 주문번호, 신규 배송지 정보 등 이벤트와 관련된 정보

배송지를 변경할 때 발생하는 이벤트를 생각해 보자. 이 이벤트를 위한 클래스는 다음과 같이 작성할 수 있다.

```
public class ShippingInfoChangedEvent {
    
    private String orderNumber;
    private long timestamp;
    private ShippingInfo newShippingInfo;
    
    // 생성자, Getter
}
```

클래스 이름의 'Changed'에서 과거 시제를 사용했는데 이벤트는 현재 기준으로 과거(바로 직전이라도)에 벌어진 것을 표현하기 때문에 이벤트 이름에는 과거 시제를 사용한다.

그리고 이벤트 디스패처로 이벤트를 전파할 Events 클래스를 구현한다.

```
public class Events {
    private static ApplicationEventPublisher publisher;

    static void setPublisher(ApplicationEventPublisher publisher) {
        Events.publisher = publisher;
    }

    public static void raise(Object event) {
        if (publisher != null) {
            publisher.publishEvent(event);
        }
    }
}
```

Events.raise()는 이벤트 디스패처(ApplicationEventPublisher)를 통해 이벤트를 전파하는 기능을 제공한다. ApplicationEvent Publisher 객체는 setPublisher() 메서드를 통해 전달받는다.

```
@Configuration
public class EventsConfiguration {
    @Autowired
    private ApplicationContext applicationContext;

    @Bean
    public InitializingBean eventsInitializer() {
        return () -> Events.setPublisher(applicationContext);
    }
}
```

참고로 ApplicationContext는 ApplicationEventPublisher를 상속하고 있으므로 ApplicationContext를 전달했다.

해당 이벤트를 발생하는 주체는 Order 애그리거트다. Order 애그리거트의 배송지 변경 기능을 구현한 메서드는 해당 이벤트를 발생시킨다.

```
public class Order {
    public void changeShippingInfo(ShippingInfo newShippingInfo) {
        verifyNotYetShipped();
        setShippingInfo(newShippingInfo);
        Events.raise(new ShippingInfoChangedEvent(number, newShippingInfo));
    }
    ...
}
```

ShippingInfoChangedEvent를 처리하는 핸들러는 디스패처로부터 이벤트를 전달받아 필요한 작업을 수행한다. 예를 들어 변경된 배송지 정보를 물류 서비스에 전송하는 핸들러는 다음과 같이 구현할 수 있다.

```
public class ShippingInfoChangedHandler {
    
    @EventListener(ShippingInfoChangedEvent.class)
    public void handle(ShppingInfoChangedEvent evt) {
        shippingInfoSynchronizer.sync(
          evt.getOrderNumber(),
          evt,getNewShippingInfo());
    }

}
```

해당 이벤트는 이벤트 핸들러가 작업을 수행하는 데 필요한 데이터를 담고 있다. 만약 데이터가 부족하다면 관련 API를 호출하거나 DB에서 데이터를 직접 읽어와야 한다.

##### 이벤트 용도

이벤트는 크게 두 가지로 쓰인다.

1. Trigger
	* 도메인의 상태가 바뀔 때마다 다른 후처리가 필요한 경우이다.  
	
		+ 주문 상태가 취소로 변경되었을 때 결제 서비스에 환불처리를 위한 메시지를 전송하게 처리할 수 있다.
		+ 주문이 완료되었을 때 SMS 서비스에 발송을 요청할 수 있다.
	* 즉, 강결합을 제거할 수 있고 관점이 분리된다.
2. Sync
	* 서로 다른 시스템 간의 데이터 동기화  
	
		+ 배송지를 변경하면 외부 배송 서비스에 바뀐 배송지 정보를 전송해야 한다.

이벤트를 사용하면 서로 다른 도메인 간에 로직이 섞이는 것을 방지할 수 있다.

그리고 이벤트 핸들러를 사용하면 기능 확장도 용이하다.

-> ex. 구매 로직을 전혀 건드리지 않아도 이벤트 핸들러를 통해 이메일 발송을 처리할 수 있다.

![](https://blog.kakaocdn.net/dn/oeYmF/btrImPWyHsN/Lyf7floEHBVCqcumcCJ3K0/img.png)
##### 트랜잭션 처리

이벤트를 사용해서 강결합 문제는 해소했지만 아직 남아 있는 문제가 하나 있다. 바로 외부 서비스에 영향을 받는 문제이다.

```
// 1. 응용 서비스 코드
@Transactional // 외부 연동 과정에서 익셉션이 발생하면 트랜잭션 처리는?
public void cancel(OrderNo orderNo, Canceller canceller) {
    Order order = orderRepository.findById(orderNo);
    order.cancel();
}

// 2. 이벤트를 처리하는 코드
@Service
public class OrderCanceledEventHandler {
    private RefundService refundService;

    public OrderCanceledEventHandler(RefundService refundService) {
        this.refundService = refundService;
    }

    @EventListener(OrderCanceledEvent.class)
    public void handle(OrderCanceledEvent event) {
        refundService.refund(event.getOrderNumber()); // 외부 서비스가 느려지거나 익셉션이 발생하면?
    }
}
```

refundService.refund()는 외부 환불 서비스와 연동된다. 해당 서비스가 갑자기 느려지면 cancel() 메서드도 함께 느려진다. 즉, 외부 서비스의 성능 저하가 내 시스템의 성능 저하로 연결된다는 것을 의미한다.

트랜잭션도 문제가 된다. 외부 서비스에서 익셉션이 터지면 cancel() 메서드를 롤백해야 하는지에 대한 문제이다. 이에 대한 방법은 이벤트를 비동기로 처리하거나 이벤트와 트랜잭션을 연계하는 것이다.

##### 비동기 이벤트 처리

회원 가입 신청을 하면 검증을 위해 이메일 보내는 서비스가 많다. 이메일은 몇 초, 10~20초 후에 도착해도 문제 되지 않는다. 이메일을 받지 못하면 다시 받을 수 있는 기능을 이용하면 된다.

비슷하게 결제 시스템 조차도 바로 환불 처리를 하지 않아도 된다. 주문 취소를 동작한 후에 결제 취소는 나중에 이루어져도 문제 없을 수 있다.

이때 'A 하면 일정 시간 안에 B 하라'는 이벤트를 비동기로 사용할 수 있다.

이벤트를 비동기로 구현하는 방법은 다음과 같이 나눌 수 있다.

* 로컬 핸들러를 비동기로 실행
* 메시지 큐 사용
* 이벤트 저장소와 이벤트 포워더 사용
* 이벤트 저장소와 이벤트 제공 API 사용

###### 로컬 핸들러 비동기 실행

이벤트 핸들러를 별도 스레드로 실행하는 방법이다. 스프링이 제공하는 @Async 애노테이션을 사용하면 간단하게 이벤트 핸들러를 비동기로 구현할 수 있다.

이를 위해 다음 두 가지 작업만 하면된다.

1. @EnableAsync 애노테이션을 사용해서 비동기 기능을 활성화한다.

```
@SpringBootApplication
@EnableAsync
public class ShopApplication {

    public static void main(String[] args) {
        SpringApplication.run(ShopApplication.class, args);
    }

}
```

2. 이벤트 핸들러 메서드에 @Async 애노테이션을 붙인다.

```
@Service
public class OrderCanceledEventHandler {

    @Async
    @EventListener(OrderCanceledEvent.class)
    public void handle(OrderCanceledEvent event) {
        refundService.refund(event.getOrderNumber());
    }
}
```

스프링은 OrderCanceledEvent가 발생하면 handle() 메서드를 별도 스레드를 이용해서 비동기로 실행한다.

###### 메시징 시스템을 이용한 비동기 구현

카프카(Kafka)나 래빗MQ(RabbitMQ)와 같은 메시징 시스템을 사용하는 것이다.

이벤트가 발생하면 이벤트 디스패처는 이벤트를 메시지 큐에 보낸다. 메시지 리스너는 알맞은 이벤트 핸들러를 이용해서 메시지를 처리한다.

![](https://blog.kakaocdn.net/dn/qpIUt/btrIMBilEbh/NYKsG51N6Nkth2Gt9314ik/img.png)
해당 과정은 별도의 스레드나 프로세스로 처리된다.

메시지 큐를 사용하면 일반적으로 이벤트를 발생시키는 주체와 이벤트 핸들러가 별도 프로세스에서 동작한다. 이는 이벤트 발생 JVM과 이벤트 처리 JVM이 다르다는 것을 의미한다.

-> 동일한 JVM에서 이벤트 발생 주체와 이벤트 핸들러가 메시지 큐를 이용해서 이벤트를 주고받을 수 있지만 시스템을 복잡하게 만들 뿐이다.

해당 방법은 MSA 형태로 각 앱 서버가 분리되어 있을 때 사용하기 좋은 방법이다.

###### 이벤트 저장소를 이용한 비동기 처리

이벤트를 비동기로 처리하는 또 다른 방법은 이벤트를 일단 DB에 저장한 뒤에 별도 프로그램을 이용해서 이벤트 핸들러에 전달하는 방법이다.

이벤트가 발생하면 핸들러는 DB에 이벤트를 저장한다. 각 프로세스는 해당 DB에 저장된 이벤트를 실행하면 되므로 처리가 될 때까지 이벤트를 읽어와 실행하면 된다. 즉, 데이터가 누락되거나 손실될 위험이 적다.

**[1. 이벤트 포워더를 사용한 방법]**

포워더는 주기적으로 이벤트 저장소에서 이벤트를 가져와 이벤트 핸들러를 실행한다.

![](https://blog.kakaocdn.net/dn/Giaui/btrIEckwOt2/oev9FKwXNRz3zOwDGkl82K/img.png)
포워더는 별도 스레드를 이용하기 때문에 이벤트 발행과 처리가 비동기로 처리된다.

**[2. 이벤트 제공 API를 사용한 방법]**

![](https://blog.kakaocdn.net/dn/dMXaS4/btrIH6YaiM8/NDp1hbE8nJ0mXKN5VR7Lnk/img.png)
포워더 방식과 API 방식의 차이점은 이벤트를 전달하는 방식에 있다. 포워더 방식이 포워더를 이용해서 이벤트를 외부에 전달한다면, API 방식은 외부 핸들러가 API 서버를 통해 이벤트 목록을 가져간다.

##### 이벤트 적용 시 추가 고려 사항

같은 앱 서버 내에서 다른 애그리거트의 이벤트를 참고하는 것은 어렵지 않다.

마이크로 서비스 간 메시징 시스템이나 포워더를 사용해서 이벤트를 처리할 경우에는 전송 실패나 손실이 발생할 수 있다.

* 전송 실패를 얼마나 허용할 것인지에 대한 정책이 필요
	+ 다시 전송을 시도하게만 처리하면 무한정 실패하면서 해당 이벤트 때문에 다른 이벤트를 실행할 수 없을 수 있다.
	+ 예를 들어, 동일 이벤트를 전송하는 데 3회 실패했다면 해당 이벤트는 로그를 남기고 넘어가는 방식의 구현이 필요하다.
* 이벤트 손실에 대한 정책이 필요
	+ 이벤트 저장소를 사용하는 방식은 이벤트 발생과 저장을 한 트랜잭션으로 처리하기 때문에 안전하다.
	+ 로컬 핸들러를 이용해서 이벤트를 비동기로 처리할 경우 이벤트 처리에 실패하면 이벤트를 유실하게 된다.
* 이벤트 순서에 대한 처리가 필요
	+ 이벤트 발생 순서대로 외부 시스템에 전달해야 할 경우 이벤트 저장소를 이용하는 것이 좋다.
	+ 메시징 시스템의 경우 이벤트 발생 순서와 메시지 전달 순서가 다를 수도 있다.
	+ 많이 사용되는 방법 중 마지막으로 처리한 이벤트의 순번을 기억해두었다가 해당보다 이전의 이벤트는 무시하는 방법이 있다.
* 이벤트 핸들러는 멱등성을 가지는 것이 좋다.
	+ 만약 이벤트 핸들러가 이벤트의 문자열을 추가하는 처리를 한다면 시스템 장애로 인해 같은 이벤트가 중복되었을 때 문자열이 두 번 추가될 수 있다.
	+ 따라서 특정 문자열이 추가된 문자열을 이벤트로 넘겨서 여러 번 처리가 되더라도 동일한 결과를 갖게 하는 것이 바람직하다.

##### 이벤트 처리와 DB 트랜잭션 고려

주문 취소와 환불 기능을 다음과 같이 이벤트를 이용해서 구현했다고 하자.

* 주문 취소 기능은 주문 취소 이벤트를 발생시킨다.
* 주문 취소 이벤트 핸들러는 환불 서비스에 환불 처리를 요청한다.
* 환불 서비스는 외부 API를 호출해서 결제를 취소한다.

만약 여기서 주문 취소 기능에서 DB에 업데이트 시키는 부분이 실패해서 예외가 터졌다고 가정하자. 즉, 외부 시스템에 환불 요청은 보냈는데 DB에는 주문 완료 상태로 남아있는 문제가 발생할 수 있다.

이를 해결하기 위한 방법으로 트랜잭션이 성공했을 때만 이벤트 핸들러를 실행하는 방법이 있다.

스프링은 @TransactionalEventListenter 애너테이션을 지원한다. 이 애너테이션은 스프링 트랜잭션 상태에 따라 이벤트 핸들러를 실행할 수 있게 한다.

```
@Async
@TransactionalEventListener(
        classes = OrderCanceledEvent.class,
        phase = TransactionPhase.AFTER_COMMIT
)
public void handle(OrderCanceledEvent event) {
    refundService.refund(event.getOrderNumber());
}
```

phase 속성 값으로 TransactionPhase.AFTER\_COMMIT을 지정했다. 이 값을 사용하면 스프링은 트랜잭션 커밋에 성공한 뒤에 핸들러 메서드를 실행한다. 즉, 중간에 예외가 터져서 트랜잭션이 롤백되면 핸들러 메서드를 실행하지 않게 된다.

이제 트랜잭션 실패에 대한 고민이 줄었으니 이벤트 처리 실패에 대해서 재처리 방식을 결정하면 된다.

##### Reference

* <http://www.yes24.com/Product/Goods/108431347>

###### '[Programming](https://jaehoney.tistory.com/category/Programming) > [DDD](https://jaehoney.tistory.com/category/Programming/DDD)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [DDD - CQRS란 무엇인가?!](https://jaehoney.tistory.com/255) (0) | 2022.08.08 |
| [DDD - 바운디드 컨텍스트란 무엇인가 ?!](https://jaehoney.tistory.com/252) (0) | 2022.07.25 |
| [DDD - 트랜잭션과 잠금을 관리하는 다양한 방법!](https://jaehoney.tistory.com/251) (0) | 2022.07.19 |
| [DDD - 도메인 서비스란 무엇인가 ?! (+ 다수의 애그리거트를 참조하는 방법)](https://jaehoney.tistory.com/248) (0) | 2022.07.14 |
| [DDD - 표현 영역과 응용 서비스! (+ 값 검증, 권한 검사, ...)](https://jaehoney.tistory.com/247) (6) | 2022.07.13 |
