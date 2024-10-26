# [Java] Mockito 사용법 (3) - 스터빙

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fdccflr%2FbtqU92Ra8DB%2F6AwINudZl3UG1VYNvJkFZ1%2Fimg.png)

## Metadata
- Author: [[노력남자]]
- Full Title: [Java] Mockito 사용법 (3) - 스터빙
- Category: #articles
- Document Tags: [[spring boot]] [[unit test]] 
- Summary: The text explains the concept of stubbing in Mockito and how to use it for defining return values of mock object methods. It demonstrates using OngoingStubbing and Stubber methods for stubbing in Mockito with examples. The text also mentions how OngoingStubbing allows method chaining for defining different stubbing for each method call.
- URL: https://effortguy.tistory.com/143

## Highlights
- 테스트 스텁은 테스트 중에 만들어진 호출에 대해 **미리 준비된 답변**을 제공하는 것 ([View Highlight](https://read.readwise.io/read/01hx8j26rqzzm7j11v57gp4n8t))
- **mock 객체의 메소드를 실행했을 때 어떤 리턴 값을 리턴할지를 정의**하는 것 ([View Highlight](https://read.readwise.io/read/01hx8j2egdvw4v9na35z039hsp))
    - Note: stubbing의 의미
- Mockito에선 when 메소드를 이용해서 스터빙을 지원 ([View Highlight](https://read.readwise.io/read/01hx8j32hy02dfcef8kzf2r1pa))
- OngoingStubbing 메소드란 **when에 넣은 메소드의 리턴 값을 정의해주는 메소드** ([View Highlight](https://read.readwise.io/read/01hx8j3tp8bcdw2rdkwk6f8q7e))
    - Note: OngoingStubbing method 정의
- Stubber 메소드는 OngoingStubbing과 다르게 when에 스터빙할 클래스를 넣고 그 후에 메소드를 호출 ([View Highlight](https://read.readwise.io/read/01hx8j56s17cwgzw1z8gcxp4xb))
- 그 이유는 스터빙이 반드시 실행되야 하는 경우 사용하는 메소드이기 때문 ([View Highlight](https://read.readwise.io/read/01hx8j5m5v5rm3669f4j28af5w))
    - Note: Stubber method 사용이유
- 또한, **리턴 타입인 void 메소드 테스트**가 가능 ([View Highlight](https://read.readwise.io/read/01hx8j76dw9jwjs526r6nhqmpk))
    - Note: Stubber method 사용이유2
