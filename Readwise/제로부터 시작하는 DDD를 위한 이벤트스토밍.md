# 제로부터 시작하는 DDD를 위한 이벤트스토밍

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbawua1%2FbtskuPD11m7%2FUZFaMCKxFrn4Ok0OzTOaaK%2Fimg.png)

## Metadata
- Author: [[커스텀 리]]
- Full Title: 제로부터 시작하는 DDD를 위한 이벤트스토밍
- Category: #articles
- Document Tags: [[event storming]] 
- Summary: 이 글에서는 도메인 주도 설계(DDD)와 이벤트 스토밍의 중요성을 설명하고 있습니다. 이벤트 스토밍은 서비스의 이벤트를 시각적으로 표현하여 비즈니스 로직을 이해하는 데 도움을 줍니다. 이를 통해 개발팀은 시스템의 복잡성을 효과적으로 관리할 수 있습니다.
- URL: https://custom-li.tistory.com/207

## Highlights
- 고객은 렌트한 자동차를 반환할 수 있어야 한다. ([View Highlight](https://read.readwise.io/read/01jj8tqfc6beegqwvva0bykb7z))
## New highlights added February 7, 2025 at 4:03 AM
- Domain Event
  도메인에서 실제로 발생하는 “**결과**”이다. ([View Highlight](https://read.readwise.io/read/01jkcgx1j0vk6y687fh4s8tpn4))
- 실제 요청사항을 통해 발생한 **결과**를 “**도메인 이벤트(Domain Event)**”라고 부르게 되는데, 이는 서비스에서 발생한 사실, 결과, 특정행위의 Output을 표현하기위해 사용된다. ([View Highlight](https://read.readwise.io/read/01jkcgxex4h1znyqgdmeawsk4g))
    - Note: 도메인 이벤트 설명
- Command
  도메인에서 특정 주체가 요청하는 “**행위**”이다. ([View Highlight](https://read.readwise.io/read/01jkcgxt9kexrsh7ha4eqpnvxp))
- 대표적으로 커맨드는 입력(Input), API, UI 버튼 등을 표현하는데 사용되며, 파란색 스티커를 사용하여 표현하고, 현재형을 이용해 이름을 정의하게 된다. ([View Highlight](https://read.readwise.io/read/01jkcgyzb9s1xy230df5xnchev))
    - Note: 커맨드 설명
- Actor
  커맨드를 발생시키는 “**주체**”를 표현할 때 사용 ([View Highlight](https://read.readwise.io/read/01jkcgztrm3xts6wemr4ehnwf8))
- Policy
  이벤트 조건에 따라 발생하는 “**새로운 커맨드**”를 나타낸다. ([View Highlight](https://read.readwise.io/read/01jkch08yjm46p8r0ypbraey7j))
- “고객이 주문 **요청(Command)** → 주문 **완료(Event)** → 알림 생성 **요청(Policy)** → 알림 **발송(Event)**”으로 정리할 수 있다. 여기서 이벤트로 인해 발생하는 요청 사항을 “**정책(Policy)**”이라고 부르며, 라일락 색의 스티커를 사용하여 표현 ([View Highlight](https://read.readwise.io/read/01jkch36evwadz1mzhdytvxj5r))
    - Note: 정책 설명
- ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcWgzbR%2FbtskizPQjPF%2Fhvv6zZoAJlgCi742kCi8mk%2Fimg.png)
  External System
  도메인 이벤트가 호출하거나 관계가 있는 “**외부 시스템**”을 표현할 때 사용한다. ([View Highlight](https://read.readwise.io/read/01jkch3x9xazz4rjnm64nqx9qt))
- Aggregate
  도메인 이벤트와 커맨드가 처리하게되는 “**데이터**”이다. ([View Highlight](https://read.readwise.io/read/01jkch4cjc365gpw0pnbx8169g))
- 자동차 대여점에서는 해당 요청을 처리하기 위해 필요한 자동차의 상세한 정보(차종, 연식, 주행거리 등)가 필요하게 된다. 이러한 데이터를 “**어그리게이트(Aggregate)**” ([View Highlight](https://read.readwise.io/read/01jkch7wft10t9kbp8hsvbf23y))
    - Note: Aggregate 설명
- ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbH8swT%2Fbtsklo1BvpP%2F3jBj3zSrgrTPOFs8DwN3q0%2Fimg.png)
  Bounded Context
  “**도메인**” 그 자체를 나타낸다. ([View Highlight](https://read.readwise.io/read/01jkch7gektc6qjj128csbpj6n))
- • **도메인 이벤트(Domain Event) 도출**
  • **이벤트에 따른 정책(Policy) 도출**
  • **커맨드(Command)와 액터(Actor) 식별**
  • **어그리게이트(Aggregate) 매핑**
  • **바운디드 컨텍스트(Bound Context) 식별**
  • **컨텍스트 매핑(Context Mapping)** ([View Highlight](https://read.readwise.io/read/01jkcha6xhwjhq99e37bqhz30y))
    - Note: 이벤트 스토밍 과정
- “**도메인 이벤트(Domain Event) 도출**” 단계는 서비스에서 발생할 수 있는 비즈니스 이벤트를 분석하는 단계이다. 이번 요구사항을 기반으로는 “렌트 요청”, “렌트 반환”, “렌트 수락”, “렌트 거절”, “알림 발송” 등 총 5개의 이벤트를 도출하게 되었다. ([View Highlight](https://read.readwise.io/read/01jkcq65ybyg4gz4b6enb55wr9))
    - Note: 도메인 이벤트 추출 단계, 
      도메인 이벤트 추출 예시
- “**이벤트에 따른 정책(Policy) 도출**” 단계는 도메인 이벤트 발생 후 그에 따라 추가적으로 반응하는 행위인 정책(Policy)을 도출하는 단계이다.
  고객이 “자동차 렌트 요청”을 하면, 대여점에는 “렌트 요청 생성”이 발생하며, 고객 또는 대여점이 렌트를 “수락”, “거절”, “반환” 하게된다면, “렌트 상태 변경”이 발생하게 될 것이다. 또한 상태 변경시마다 알림이 전송되어 “알림 발송”도 함께 발생하게 될 것이다. ([View Highlight](https://read.readwise.io/read/01jkcq96a1g1k5jw1ef0sa31y6))
    - Note: 이벤트 추출 후 정책 도출 단계
      정책 도출 예시
- “**커맨드(Command)와 액터(Actor) 식별**” 단계는 도메인 이벤트를 발생시키는 “**행위**”인 커맨드(Command)와 행위를 수행하는 “**주체**”인 액터(Actor) 도출하는 단계이다. ([View Highlight](https://read.readwise.io/read/01jkcqaeg69chmefsqmsagxe1e))
    - Note: 3단계, 커맨드와 액터 식별
- “**어그리게이트(Aggregate) 매핑**” 단계는 커맨드와 이벤트가 사용하는 데이터를 정의하는 단계이다. 이번 사례에서는 간략하게 “**고객(Customer)**”, “**매장(Store)**”, “**알림(Notification)**”등의 대표적인 데이터를 사용하였지만, 세부 단계에서는 어그리게이트 내부에서 사용하는 상세 데이터도 함께 지정하여 더욱 명확한 이벤트 스토밍을 진행 ([View Highlight](https://read.readwise.io/read/01jkcqcvmjx8d4z1zsd5padbf4))
    - Note: 4단계, 어그리게이트 매핑 단계
      커맨드와 이벤트가 사용하는 데이터를 정의
- **“바운디드 컨텍스트(Bound Context)**” 단계는 지금까지의 결과물들을 바운디드 컨텍스트를 이용해 묶어주는 단계이다. 이벤트 스토밍이 완료되었을 때, 이 단계에서 생성된 바운디드 컨텍스트들은 각각의 마이크로 서비스가 될 가능성이 있다. ([View Highlight](https://read.readwise.io/read/01jkcqenrcw03agee8pbvd87jt))
    - Note: 5단계, 바운디드 콘텍스트 단계
      4단계까지 나온 결과물을 다운디드 콘텍스트를 이용하여 묶어줌
- 마지막으로 “**컨텍스트 매핑(Context Mapping)**” 단계는 최종적으로 구성요소간의 관계를 설정하는 단계이다. 이 단계에서는 고려하지 못했던 외부 시스템(External System)이나, 추가적으로 도출된 도메인 이벤트나 커맨드 등을 포함하여 전체 시스템을 검토 ([View Highlight](https://read.readwise.io/read/01jkcqhdkyavj6bqk4qhy4jebj))
