# DDD(Domain Driven Design) - 도메인 주도 설계란? 마이크로서비스의 관점에서

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FDGjcq%2FbtqDrkuPoSh%2Fj7ajq9sc6HCh1CxHtCet50%2Fimg.jpg)

## Metadata
- Author: [[TISTORY]]
- Full Title: DDD(Domain Driven Design) - 도메인 주도 설계란? 마이크로서비스의 관점에서
- Category: #articles
- Document Tags:  #ddd 
- Summary: Domain Driven Design (DDD) focuses on designing software around the domain, or real-world events, by identifying and organizing objects that interact with each other. It emphasizes that the role of these objects can change depending on the context. A key challenge in DDD is designing aggregates, which help clarify how objects are grouped and interact within a domain.
- URL: https://huisam.tistory.com/entry/DDD

## Full Document
![](https://img1.daumcdn.net/thumb/R750x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FDGjcq%2FbtqDrkuPoSh%2Fj7ajq9sc6HCh1CxHtCet50%2Fimg.jpg)
**목차** 

도메인 주도 설계를 이해하기 위해서는 객체지향을 먼저 이해할 필요가 있습니다

객체지향에서의 핵심은 뭘까요?

> 객체지향에서의 핵심은 실세계의 객체(물건, 사람, 주문 .... 주도적으로 뭔가를 생산하는 주체) 들이  
> 서로간의 상호작용을 바탕으로 책임,협력,역할 의 관점을 가지고 메세지를 교환하는 것이다.

객체지향에서의 핵심은 결국 **객체(무언가를 만드는 주체)** 라고 할 수 있습니다

*그렇다면 이 객체들을 어떻게 하면 추려낼 수 있을까요?*

*어떻게 하면 어떤 객체가 필요한지 알 수 있을까요?*

*어떻게 하면 이 객체들이 서로 상호작용할 수 있을까요?*

여러 방법들이 있겠지만, 이것을 해결해줄 수 있는 것이 바로

**도메인 주도 설계**입니다

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FDGjcq%2FbtqDrkuPoSh%2Fj7ajq9sc6HCh1CxHtCet50%2Fimg.jpg)도메인 주도 설계 
쉽게 말하면, 도메인을 중심으로 설계해 나가는 것을 의미합니다.

그렇다면 도메인이 뭘까요?

도메인은 **실세계에서 사건이 발생하는 집합**이라고 생각하면 쉽습니다

옷 쇼핑몰을 한번 예로 들어볼까요?

옷 쇼핑몰에서는 손님들이 주문하는 도메인(Order Domain)이 있을 수 있고,

점주입장에서 옷들을 관리하는 도메인(Manage Domain)이 있을 수 있고,

쇼핑몰 입장에서 월세, 관리비 등 건물에 대한 관리를 담당하는 도메인(Building Domain)이 있을 수 있습니다.

**이러한 여러가지 도메인들이 서로 상호작용 하며, 설계하는 것이 바로 도메인 주도 설계입니다.**

이 도메인 주도 설계에서의 특징은

같은 객체(Object or Class)가 여러 개가 존재할 수 있다는 것이에요!

주문 도메인에서의 옷은 손님들에게 팔기 위한 객체 정보(name, price .. etc)들을 담고 있지만,

옷을 관리하는 도메인에서는 옷은 점주 입장에서 관리하기 위한 객체 정보(madeTime, size, madeCountry ... etc)들을 위주로 담고 있습니다.

다시 말해서 **문맥(Context)**에 따라 객체(Object)의 역할은 바뀐다는 것이에요!

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc1PGG5%2FbtqDvgknEsi%2FfFMbAtKjDxnsP8hi3YAaZ0%2Fimg.png)context의 관점에서 
즉 어떠한 상황에서 바라볼 것인가?

에 대해서 조금 더 생각해볼 필요가 있다는 거에요!

흔히 이것을 **Bounded Context**라고 부르기도 한답니다

Bounded Context에 따라서 Model들의 역할은 완벽히 달라지고, 책임 또한 달라지게 되는 것이죠

그래서 이를 외부로(public)으로 노출시키지 않고, package-private으로 내부에서만 알 수 있게 하는 것이에요

이러한 관점을 더 나아가서 직접 서비스에 적용시킨 것이 바로 **MircoService(마이크로서비스)**입니다

다시 말해서, 서로 다른 도메인 영역에 영향을 끼치기 위해서는 API 호출로 해야 된다는 말이에요

즉, 각각의 **도메인은 서로 철저히 분리**되고, **높은 응집력과 낮은 결합도**로 **변경과 확장에 용이한 설계**를 얻게 됩니다

그렇다면 이러한 도메인 주도 설계를 어떻게 할까요?

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FNlWw9%2FbtqDr97HXRt%2FqzhwhwYYG42mKhmKCDzsn1%2Fimg.png)DDD Architecture 
크게 3가지 Layer로 구분하는 것이 핵심인데요,

1. Application Layer: 주로 도메인과 Repository를 바탕으로 실제 서비스(API)를 제공하는 계층이에요
2. Domain Layer: Entity, VO(Value Object)를 활용하여 도메인 로직이 진행되는 계층이에요
3. Infrastructure Layer: 쉽게 말하면 외부와의 통신(ORM, DB, NoSql)을 담당하는 계층이에요

하지만 이러한 의문이 들 수 있어요

*Entity는 뭐고 VO는 뭐지?? 같은거 아닌가??*

Entity는 고유 식별자(primary Key)를 바탕으로 객체의 정체성을 부여하고,

VO(Value Object)는 상태(Attribute)를 바탕으로 객체의 정체성을 부여해요!

Java로 쉽게 설명하자면, equals HashCode를 **id로만 하면 Entity**, **상태에 대한 모든 정보로 하면 VO** 입니다!

각각의 도메인들을 위와 같은 Layer로 철저히 분리해서 만드는 것이 DDD(Domain Driven Design)의 핵심 설계 방식입니다

설계한 도메인들을 모듈(Module)별로 분리하는 것이 마이크로서비스(MicroService)구요

DDD(Domain Driven Design)에서 핵심은 **결국 도메인을 서비스로 별로 분리하라** 에요!

하지만 모든 도메인에서 많은 객체(Object or Class)들을 다루고 있다면,

유지보수 혹은 기능확장적 부분에서 많이 어려움을 겪을 수 밖에 없어요

객체간의 상호작용은 점점 복잡해질 것이고, 어떤 객체가 도메인을 대표하는 객체인지 모르기 때문이죠.

그렇다고 객체마다 Repository를 하나씩 다 만드는 것은 DDD가 가지는 장점을 내세울 수 없게 됩니다.

*모든 Entity를 Infracstructure와 엮을거면 마이크로서비스로 쪼갠 의미가 없죠 ㅎㅎ*

*--> 사실 의미는 있습니다만, 마이크로서비스로써의 장점이 없다는 말과 동일해요*

여기서 등장하는 것이 바로 **Aggregate(집합)**입니다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FMhHoE%2FbtqDvyZtluZ%2FgPBxMT0sJx8o4Fjpk2MxGK%2Fimg.png)Aggregate 
정말 정말 정말 쉽게 말하면, 각각의 도메인 영역을 대표하는 객체가 바로 Aggregate입니다.

그렇게 되면, 각각의 **도메인에 Repository로 묶어야 하는 객체(Entity)**가 명확해지기 때문이죠

Top-Down 방식으로 계층을 타고타고 내려갈 때 어떤 Entity를 만들기 위해 도메인이 이루어져 있는지

명확하게 들어오기도 한답니다!

위의 예시에서는 Order라는 Domain에서 Order라는 Entity를 만들기 위해

다양한 객체(Object or Class)들이 상호 협력하고 있는 관계를 볼 수 있습니다!

이 Aggregate를 설계하는 과정이 정말 어렵고, 개발자에게 힘든 숙제중 하나입니다.

명확하게 설계하는 것이 생각보다 어렵거든요 ㅎㅎ

사실 이 글을 작성하게 된 계기는 마이크로서비스에 대한 의문점이 많이 들었기 때문이에요

**왜 마이크로서비스여야 되지?** 하는 생각이 정말 많이 들었는데,

이에 대한 해답을 말하지 못하는 제 모습을 보면서 한번쯤 정리하고 싶었어요 ㅎㅎ

Cloud 환경도 Container가 대세가 되었고, 그렇기 때문에 마이크로서비스가 더 의미있다고 생각해요

기존에는 Hypervisor기반의 모놀리식 아키텍쳐였다면, 지금은 Domain Service를 중심으로 Containter를 Scale In / Out 하는 Ops환경이 대세가 되었기 때문이에요

서비스들을 쪼개고 쪼개서 시장의 빠른 변화에 민첩하게 대응하기 위함이죠 ㅎㅎ

물론 시장의 변화도 빠르게 반영하는 것도 중요하지만, 지금은 **DevOps**의 시대이기 때문에인것도 가장 큰 것 같아요!

개발해서 빌드 배포 PRD환경에 제공하는 이 모든 시간을 단축시키고 자동화하는 것이 정말 중요하기 때문이죠 ㅎㅎ

**사람을 쓰지 않고, 개발자가 운영을 할 수 있으니까요**

###### 참고

|  |  |
| --- | --- |
| [Backend 서버 개발시에 유용한 Intellij 인텔리제이 플러그인 추천](https://huisam.tistory.com/entry/intllij-plugins) (1) | 2022.10.03 |
| [Agile이란? - 애자일 개발 방법론에 대해서](https://huisam.tistory.com/entry/Agile) (0) | 2020.02.19 |
| [짧은 우아한 테크코스(Wootech) 후기](https://huisam.tistory.com/entry/Wootech) (0) | 2019.06.17 |
| [[개발방법론] - Java를 올바르게 개발하자!](https://huisam.tistory.com/entry/Java-Code-Convention) (0) | 2019.04.06 |
| [Socket(TCP) 통신을 이용한 Chatting Project 만들기](https://huisam.tistory.com/entry/SocketTCP-%ED%86%B5%EC%8B%A0%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-Chatting-Project-%EB%A7%8C%EB%93%A4%EA%B8%B0) (0) | 2019.02.19 |

도메인 주도 설계를 이해하기 위해서는 객체지향을 먼저 이해할 필요가 있습니다

객체지향에서의 핵심은 뭘까요?

> 객체지향에서의 핵심은 실세계의 객체(물건, 사람, 주문 .... 주도적으로 뭔가를 생산하는 주체) 들이  
> 서로간의 상호작용을 바탕으로 책임,협력,역할 의 관점을 가지고 메세지를 교환하는 것이다.

객체지향에서의 핵심은 결국 **객체(무언가를 만드는 주체)** 라고 할 수 있습니다

*그렇다면 이 객체들을 어떻게 하면 추려낼 수 있을까요?*

*어떻게 하면 어떤 객체가 필요한지 알 수 있을까요?*

*어떻게 하면 이 객체들이 서로 상호작용할 수 있을까요?*

여러 방법들이 있겠지만, 이것을 해결해줄 수 있는 것이 바로

**도메인 주도 설계**입니다

![](https://blog.kakaocdn.net/dn/DGjcq/btqDrkuPoSh/j7ajq9sc6HCh1CxHtCet50/img.jpg)도메인 주도 설계 
쉽게 말하면, 도메인을 중심으로 설계해 나가는 것을 의미합니다.

그렇다면 도메인이 뭘까요?

도메인은 **실세계에서 사건이 발생하는 집합**이라고 생각하면 쉽습니다

옷 쇼핑몰을 한번 예로 들어볼까요?

옷 쇼핑몰에서는 손님들이 주문하는 도메인(Order Domain)이 있을 수 있고,

점주입장에서 옷들을 관리하는 도메인(Manage Domain)이 있을 수 있고,

쇼핑몰 입장에서 월세, 관리비 등 건물에 대한 관리를 담당하는 도메인(Building Domain)이 있을 수 있습니다.

**이러한 여러가지 도메인들이 서로 상호작용 하며, 설계하는 것이 바로 도메인 주도 설계입니다.**

이 도메인 주도 설계에서의 특징은

같은 객체(Object or Class)가 여러 개가 존재할 수 있다는 것이에요!

주문 도메인에서의 옷은 손님들에게 팔기 위한 객체 정보(name, price .. etc)들을 담고 있지만,

옷을 관리하는 도메인에서는 옷은 점주 입장에서 관리하기 위한 객체 정보(madeTime, size, madeCountry ... etc)들을 위주로 담고 있습니다.

다시 말해서 **문맥(Context)**에 따라 객체(Object)의 역할은 바뀐다는 것이에요!

![](https://blog.kakaocdn.net/dn/c1PGG5/btqDvgknEsi/fFMbAtKjDxnsP8hi3YAaZ0/img.png)context의 관점에서 
즉 어떠한 상황에서 바라볼 것인가?

에 대해서 조금 더 생각해볼 필요가 있다는 거에요!

흔히 이것을 **Bounded Context**라고 부르기도 한답니다

Bounded Context에 따라서 Model들의 역할은 완벽히 달라지고, 책임 또한 달라지게 되는 것이죠

그래서 이를 외부로(public)으로 노출시키지 않고, package-private으로 내부에서만 알 수 있게 하는 것이에요

이러한 관점을 더 나아가서 직접 서비스에 적용시킨 것이 바로 **MircoService(마이크로서비스)**입니다

다시 말해서, 서로 다른 도메인 영역에 영향을 끼치기 위해서는 API 호출로 해야 된다는 말이에요

즉, 각각의 **도메인은 서로 철저히 분리**되고, **높은 응집력과 낮은 결합도**로 **변경과 확장에 용이한 설계**를 얻게 됩니다

그렇다면 이러한 도메인 주도 설계를 어떻게 할까요?

![](https://blog.kakaocdn.net/dn/NlWw9/btqDr97HXRt/qzhwhwYYG42mKhmKCDzsn1/img.png)DDD Architecture 
크게 3가지 Layer로 구분하는 것이 핵심인데요,

1. Application Layer: 주로 도메인과 Repository를 바탕으로 실제 서비스(API)를 제공하는 계층이에요
2. Domain Layer: Entity, VO(Value Object)를 활용하여 도메인 로직이 진행되는 계층이에요
3. Infrastructure Layer: 쉽게 말하면 외부와의 통신(ORM, DB, NoSql)을 담당하는 계층이에요

하지만 이러한 의문이 들 수 있어요

*Entity는 뭐고 VO는 뭐지?? 같은거 아닌가??*

Entity는 고유 식별자(primary Key)를 바탕으로 객체의 정체성을 부여하고,

VO(Value Object)는 상태(Attribute)를 바탕으로 객체의 정체성을 부여해요!

Java로 쉽게 설명하자면, equals HashCode를 **id로만 하면 Entity**, **상태에 대한 모든 정보로 하면 VO** 입니다!

각각의 도메인들을 위와 같은 Layer로 철저히 분리해서 만드는 것이 DDD(Domain Driven Design)의 핵심 설계 방식입니다

설계한 도메인들을 모듈(Module)별로 분리하는 것이 마이크로서비스(MicroService)구요

DDD(Domain Driven Design)에서 핵심은 **결국 도메인을 서비스로 별로 분리하라** 에요!

하지만 모든 도메인에서 많은 객체(Object or Class)들을 다루고 있다면,

유지보수 혹은 기능확장적 부분에서 많이 어려움을 겪을 수 밖에 없어요

객체간의 상호작용은 점점 복잡해질 것이고, 어떤 객체가 도메인을 대표하는 객체인지 모르기 때문이죠.

그렇다고 객체마다 Repository를 하나씩 다 만드는 것은 DDD가 가지는 장점을 내세울 수 없게 됩니다.

*모든 Entity를 Infracstructure와 엮을거면 마이크로서비스로 쪼갠 의미가 없죠 ㅎㅎ*

*--> 사실 의미는 있습니다만, 마이크로서비스로써의 장점이 없다는 말과 동일해요*

여기서 등장하는 것이 바로 **Aggregate(집합)**입니다.

![](https://blog.kakaocdn.net/dn/MhHoE/btqDvyZtluZ/gPBxMT0sJx8o4Fjpk2MxGK/img.png)Aggregate 
정말 정말 정말 쉽게 말하면, 각각의 도메인 영역을 대표하는 객체가 바로 Aggregate입니다.

그렇게 되면, 각각의 **도메인에 Repository로 묶어야 하는 객체(Entity)**가 명확해지기 때문이죠

Top-Down 방식으로 계층을 타고타고 내려갈 때 어떤 Entity를 만들기 위해 도메인이 이루어져 있는지

명확하게 들어오기도 한답니다!

위의 예시에서는 Order라는 Domain에서 Order라는 Entity를 만들기 위해

다양한 객체(Object or Class)들이 상호 협력하고 있는 관계를 볼 수 있습니다!

이 Aggregate를 설계하는 과정이 정말 어렵고, 개발자에게 힘든 숙제중 하나입니다.

명확하게 설계하는 것이 생각보다 어렵거든요 ㅎㅎ

사실 이 글을 작성하게 된 계기는 마이크로서비스에 대한 의문점이 많이 들었기 때문이에요

**왜 마이크로서비스여야 되지?** 하는 생각이 정말 많이 들었는데,

이에 대한 해답을 말하지 못하는 제 모습을 보면서 한번쯤 정리하고 싶었어요 ㅎㅎ

Cloud 환경도 Container가 대세가 되었고, 그렇기 때문에 마이크로서비스가 더 의미있다고 생각해요

기존에는 Hypervisor기반의 모놀리식 아키텍쳐였다면, 지금은 Domain Service를 중심으로 Containter를 Scale In / Out 하는 Ops환경이 대세가 되었기 때문이에요

서비스들을 쪼개고 쪼개서 시장의 빠른 변화에 민첩하게 대응하기 위함이죠 ㅎㅎ

물론 시장의 변화도 빠르게 반영하는 것도 중요하지만, 지금은 **DevOps**의 시대이기 때문에인것도 가장 큰 것 같아요!

개발해서 빌드 배포 PRD환경에 제공하는 이 모든 시간을 단축시키고 자동화하는 것이 정말 중요하기 때문이죠 ㅎㅎ

**사람을 쓰지 않고, 개발자가 운영을 할 수 있으니까요**

###### 참고

|  |  |
| --- | --- |
| [Backend 서버 개발시에 유용한 Intellij 인텔리제이 플러그인 추천](https://huisam.tistory.com/entry/intllij-plugins) (1) | 2022.10.03 |
| [짧은 우아한 테크코스(Wootech) 후기](https://huisam.tistory.com/entry/Wootech) (0) | 2019.06.17 |
| [[개발방법론] - Java를 올바르게 개발하자!](https://huisam.tistory.com/entry/Java-Code-Convention) (0) | 2019.04.06 |
| [Socket(TCP) 통신을 이용한 Chatting Project 만들기](https://huisam.tistory.com/entry/SocketTCP-%ED%86%B5%EC%8B%A0%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-Chatting-Project-%EB%A7%8C%EB%93%A4%EA%B8%B0) (0) | 2019.02.19 |
