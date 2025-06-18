# ㄷㄷㄷ: Domain Driven Design과 적용 사례 공유

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcfLXag%2FbtrQyXrxQom%2FHxL9O47HMnb2qNkMFZVb3K%2Fimg.jpg)

## Metadata
- Author: [[ENTER TECH]]
- Full Title: ㄷㄷㄷ: Domain Driven Design과 적용 사례 공유
- Category: #articles
- Document Tags:  #ddd 
- Summary: KakaoPage is transitioning from a monolithic system to a Micro Service Architecture (MSA) to improve resource management and maintenance. The team chose Domain Driven Design (DDD) for its focus on understanding business requirements and improving system design. This approach allows for better organization of code, easier maintenance, and flexibility in implementing new features.
- URL: https://kakaoentertainment-tech.tistory.com/95

## Full Document
![](https://blog.kakaocdn.net/dn/UCXee/btrNjSGC125/22kEMFrZ2GPwdpng8RdMbk/img.jpg)
카카오페이지 앱에는 수많은 종류의 콘텐츠들이 있습니다.

웹툰, 웹소설, 일반교양, 오디오, 동영상 등등..

이런 콘텐츠들은 카카오페이지에서 제공하는 파트너사이트라는 툴을 이용하여,

작품/회차의 제작, 파일 업로드, 판매, 공지, 예약 등의 다양한 기능을 수행하고 있습니다.

파트너사이트는 초기 카카오페이지 앱에서부터 함께 했던 서버라서 Monolithic한 형태로 되어있었는데요.

Monolithic한 형태의 단점인 리소스 관리, 유지보수의 어려움 등의 이유로

[MSA(Micro Service Architecture)](https://learn.microsoft.com/ko-kr/azure/architecture/guide/architecture-styles/microservices)로 전환해야 하는 상황이 되었습니다.

> **[돌발‼️]**  
> **상태 이상 : 'MSA가 아니면 죽음을' 발생‼️**

##### **🏷️ TDD vs BDD vs DDD**

먼저 MSA로의 전환을 위해서 저희 팀은 어떤 부분을 중점에 두고 설계를 할지 고민했는데요.

널리 알려진 세 가지 방식을 비교해봤습니다.

[![](https://blog.kakaocdn.net/dn/cfLXag/btrQyXrxQom/HxL9O47HMnb2qNkMFZVb3K/img.jpg)](https://www.mobilelive.ca/blog/value-of-tdd-bdd-ddd)TDD vs BDD vs DDD 
* 자동화된 테스트와 반복적인 설계 수정을 중점으로 수행하는 TDD
* 비즈니스와의 협업과 자동화된 테스트를 중점으로 수행하는 BDD
* 반복적인 설계 수정을 기반으로 비즈니스와의 협업을 중심으로 하는 DDD

이 세 가지 설계 방식 중, 저희는 [DDD(Domain Driven Design)를](https://en.wikipedia.org/wiki/Domain-driven_design) 선택했습니다.

그 이유는 아래와 같습니다.

* 완전히 새로운 시스템이 아닌 기존 시스템의 분해 및 개선 가능
* Business ↔︎ Development 간의 보편적인 이해와 전체적인 그림에 대한 동기화
* 새로운 요구사항에 대한 일정 및 리소스 관리

아무래도 자동화 테스트를 위해 테스트 케이스를 하나하나 새로 만드는 것보다는 기존 로직을 최대한 살리면서 진행할 수 있도록 했고,  

MSA를 진행하면서 신규 요구 사항들도 어느 정도 받아낼 수 있어야 했기 때문에, 기존 레거시 서버와 신규 MSA 서버들이 동시에 동작할 수 있도록 DDD와 더불어 점진적인 교체를 시도했습니다.

##### ****🏷️**Domain Driven Design**

그렇다면 DDD란 무엇일까요?

> 각각의 기능적인 문제 영역들을 도메인이라고 정의하고, 그렇게 정의된 도메인에 대한 로직을 중심으로 설계하는 것을 말합니다.

이러한 DDD에는 몇 가지 특징이 있습니다.

1. 데이터 중심이 아닌 도메인의 모델과 로직에 집중
2. 동일한 표현과 단어로 구성된 단일화된 언어체계의 사용
3. Software Entity와 Domain 간 개념을 일치하여, 도메인 모델부터 코드까지 항상 함께 움직이는 구조의 모델 지향

##### **🏷️ Terms of DDD**

DDD를 구현하기 위해서 중요한 개념 3가지가 있습니다.

1. Bounded-Context - 범위를 구분해 놓은, 하위 도메인 개념
2. Context Map - Bounded-Context 간의 관계를 보여주는 맵
3. Aggregate - 데이터 변경 단위, 라이프 사이클이 같은 도메인을 모아놓은 집합.

파트너사이트에서 제공하는 기능들을 예로 들어보면 다음과 같은 영역들이 있습니다.

이 영역들을 분류하여 서로에 대한 의존성을 줄이기 위해 일종의 경계를 구성하게 되는데요, 이걸 Bounded-Context라고 합니다.

![](https://blog.kakaocdn.net/dn/exwoTd/btrQC7NQgCz/1EGaqo3pB89wRtJfvgNJX0/img.png)![](https://blog.kakaocdn.net/dn/oYlC2/btrQCVGMfEs/uMpBAvgGBZNtDMHCrKOK20/img.png)Bounded-Context Example 
위에서 보는 것처럼 콘텐츠 제작/메타정보 관리/판매를 하나의 바운더리로 묶어 놓았고, 이것은 MSA상 하나의 서비스가 됩니다. 이렇게 분류된 Context들은 서로의 도메인을 철저히 분리하고 api를 통한 CRUD 등을 수행하게 될 것입니다.

분류된 Bounded-Context를 기반으로 서로의 관계를 보여주는 Context-Map은 다음과 같습니다.

![](https://blog.kakaocdn.net/dn/EIkxX/btrQyvPEeYh/O4iUAkEkUKSsiz1aghMnG0/img.png)Context Map Example 
Context Map을 보면서 up/down 스트림을 한눈에 볼 수 있게 했고, 전체적인 흐름을 예상할 수 있게 됩니다.

이 Context Map을 가지고 서비스들을 각각 구현을 하게 되었는데요. 서비스들이 가지고 있는 많은 객체들을 그대로 사용하는 것은 의미가 없기 때문에 각 도메인 영역을 대표하는 도메인 객체들의 집합을 설계를 하게 되었습니다.

![](https://blog.kakaocdn.net/dn/cZcLKU/btrQv0buxEI/drrzdN9KCGCdJTI1wWAhc0/img.png)Aggregate Example 
위에 보시는 다이어그램은 Video Proudct Aggregate의 예시입니다.

> Aggregate는 데이터 변경 단위, 라이프 사이클이 같은 도메인을 모아놓은 집합.

데이터의 변경 단위이고, 라이프 사이클이 같은 도메인들이기 때문에 Aggregate는 Root Entity를 통해서만 접근이 가능하도록 하고 해당 접근으로 인한 데이터의 변경은 내부의 모든 객체에 영향을 미치게 됩니다.

이렇게 Aggregate를 구성하게 되면, Video Product 내부 개별 객체의 상호작용보다는 외부의 다른 Aggregate나 객체들 사이의 관계를 조금 더 넓은 시야로 바라볼 수 있으며, 제약사항들을 하나의 맥락으로 관리할 수 있게 됩니다.

##### **🏷️ Hexagonal Architecture**

DDD를 구현하기 위해서 저희는 Hexagonal Architure를 사용하였는데, 포트라는 구현 개념을 명시하고 있습니다.   

그래서 Port-and-Adaptor Architecture라고도 불리는데요.  

전통적인 Layered Architecture의 경우 Business Logic이 거대해지면서 오염되는 경우가 염려되어 제외하였고, 포트와 어댑터라는 명확한 구현 개념이 포함되어 있기 때문에 선택하게 되었습니다.

![](https://blog.kakaocdn.net/dn/qfuoP/btrQC7m1wEm/EDkzs1ZSlNqYckVvuckjk1/img.png)Hexagonal Architecture 
포트와 어댑터는 포트로 들어오는 데이터를 어댑터를 통해 알맞게 변환해주는 역할을 하게 됩니다.

> Xbox나 플레이스테이션에서 HDMI 포트를 이용하여 비디오/오디오를 송출하고, USB 포트를 이용하여 컨트롤러를 붙이듯이..  
> 맞는 포트와 어댑터를 연결하면 어떤 식으로든 사용이 가능.

결국 **Hexagonal Architecture의 핵심은 비즈니스 로직이 표현 로직이나 데이터 접근 로직에 의존하지 않는 것**입니다.

##### **🏷️ Code Example**

Product라는 가상의 도메인을 가지고 샘플 코드를 구현해보겠습니다.

해당 도메인 안에는 sales info와 작품의 메타 정보, 그리고 작품이 가진 콘텐츠 파일 정보들이 있게 될 거예요.

또한 도메인 내부에서 작품을 판매 시작할 경우 필요한 유효성 검사와, 판매 시작 날짜에 대해 처리할 수 있도록 관련 기능도 들어가 있습니다.

Product Domain
해당 Product 도메인을 처리하는 과정입니다.

유저는 Controller를 통해서 작품 판매 시작 api로 요청을 하게 되고, 이 api에서는 Use Case에 정의된 ‘작품 판매’를 수행하게 됩니다.

![](https://blog.kakaocdn.net/dn/be4Jtr/btrQsF7gCXH/P134WKhcd4qS6r0X5R7M6k/img.png)Controller and Use Case 
Controller에서는 Use Case 내부에 정의된 saleProduct라는 메서드를 실행하게 되는데요.

이 메서드는 SaleService에 구현이 되어 있고, 실제 DB와의 통신은 Load/Save port에서 진행되게 됩니다.

![](https://blog.kakaocdn.net/dn/Z59L3/btrQDdna6fJ/OAnDgI0K5otvKlOXeeLHe0/img.png)SaleService 
같은 DB와의 CRUD인데 Load/Save Port를 나누어놓은 것은 조회 성능의 개선을 염두에 두었고,   

추후 Amazon SQS나 RabbitMQ 등을 사용하여 Event Driven 방식으로 변경할 예정이기 때문에 분리해놓았습니다.

이렇게 정의된 포트들은 앞서 이야기한 port-and-adapter 구조에 따라 Adapter에서 구현을 하게 되는데요.

![](https://blog.kakaocdn.net/dn/kQttm/btrQv0bKGL5/drXAjK0qZDK8yK2uiAhfV1/img.png)
코드에서 보시다시피 Adapter에 구현된 load/save에는 추가로 구현된 Mapper의 사용이 필요합니다.

DDD에서는 저장된 데이터를 그대로 사용하는 것이 아니라 도메인으로 변환하고 그 도메인을 중심으로 로직을 구성하기 때문에, DB에 저장된 데이터를 도메인에 맞게 mapping 해주는 과정이 필요하고 이것은 Mapper의 구현을 통해 이루어집니다.

즉, JpaEntity -> DomainEntity 그리고 DomainEntity -> JpaEntity로의 변환이 필요합니다.

![](https://blog.kakaocdn.net/dn/5i3TO/btrQuMdKT02/IpyRvkhagXsGixRc4eiYAk/img.png)
##### **🏷️ Happily Ever After**

이렇게 Domain Driven Design을 사용하여 아키텍처와 코드를 구현하였으니 모두 해결이 되었을까요?

> There is No Silver Bullet

MSA화 해서 불필요한 레거시를 제거하고, 도메인을 중점으로 오래오래 행복하게 살았으면 좋겠지만...

![](https://blog.kakaocdn.net/dn/cwmToU/btrQCVUI7dy/ckKr2enzvk7BiFwo5KOM5K/img.jpg)땅, 불, 바람, 물, 마음 다섯가지 서버 하나로 모으면.. 
MSA를 적용하면서 발생하는 개발 복잡도와 숙련도, 트랜잭션 관리, 배포 복잡도 등과 더불어 Mapper 등과 같이 Hexagonal Architecture 구현에서 생성되는 생각보다 많은 코드에 대한 어려움이 생겼습니다. 또한 각 도메인에 대한 높은 이해도가 필요하기 때문에 신규 도메인 혹은 기존 도메인의 수정이 필요할 때는 설계에 대한 검토를 충분히 하고서야 구현 작업을 할 수 있게 되었습니다.

그러나 이러한 단점들만 있는 건 아니겠죠? ~~(그랬음 안 했지..)~~

1. **도메인 간 관계가 복잡한 경우라도 큰 틀에서 정리가 가능**
2. **도메인의 분리에 따른 유지보수에 대한 편의성**
3. **새로운 기능 및 요구 사항에 대한 유연성**

기존 데이터들을 도메인으로 한 번 정제했기 때문에, 이러한 장점들이 생겨나게 되었습니다.

그뿐만 아니라 실제 코드를 구현하는 개발자 측면에서 보자면,

1. **Encapsulation**
2. **Loose coupling, High cohesion**
3. **Domain Logic의 분리로 Business Logic에 집중**
4. **코드 가독성**

Aggregate 사용으로 인한 도메인 캡슐화가 이루어졌고, Use Case/Port 사용 등으로 의존도를 낮추면서 각 로직들을 필요한 곳에 모아서 사용하여 응집도를 높이게 되었습니다.

그렇게 됨으로써 Business Logic에 집중하고 코드 가독성까지 덤으로 올라가는 효과가 생겨났습니다.

##### 마치며..

레거시 시스템의 전환은 으레 그렇듯이, 많은 시간과 고민이 필요하고 또한 고통스럽죠. 리소스는 항상 부족하고요.

~~(사람이 없어요. 시간이 없어요.)~~

오히려 그렇기 때문에 조금 더 공을 들여 도메인에 대해 이해하게 되는 DDD를 고민해볼 만하다고 생각합니다.

> **업적 달성! <DDD 시도>**

감사합니다!

![](https://blog.kakaocdn.net/dn/MAs1f/btrSbUs5n8t/Hvsmnwaq7uKISkYkVzo8E1/img.png)
###### '[Tech](https://kakaoentertainment-tech.tistory.com/category/Tech)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [라이브채팅 플랫폼 구현기 2탄 : 아키텍처 및 성능 테스트](https://kakaoentertainment-tech.tistory.com/110) (8) | 2023.03.07 |
| [라이브채팅 플랫폼 구현기 1탄 : 개발 언어 및 기반기술 조사](https://kakaoentertainment-tech.tistory.com/109) (3) | 2023.03.07 |
| [Technical Writing: 글로 하는 의사소통](https://kakaoentertainment-tech.tistory.com/97) (2) | 2022.12.09 |
| [섬세한 ISFP의 코드 가독성 개선 경험](https://kakaoentertainment-tech.tistory.com/96) (0) | 2022.12.08 |
| [카카오페이지는 BFF(Backend For Frontend)를 어떻게 적용했을까?](https://kakaoentertainment-tech.tistory.com/92) (0) | 2022.09.26 |
