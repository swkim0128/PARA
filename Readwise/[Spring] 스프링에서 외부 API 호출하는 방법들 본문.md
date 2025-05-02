# [Spring] 스프링에서 외부 API 호출하는 방법들 본문

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcTvfR5%2FbtshAARNUMb%2FLk55rgIXnVR4ROqjzsMOS0%2Fimg.png)

## Metadata
- Author: [[Kangjieun11]]
- Full Title: [Spring] 스프링에서 외부 API 호출하는 방법들 본문
- Category: #articles
- Summary: 외부 API를 호출하는 방법들에는 HttpURLConnection/URLConnection, HttpClient, RestTemplate, WebClient, OpenFeign이 있다. HttpURLConnection/URLConnection은 순수 자바로 HTTP 통신이 가능하지만 오래된 자바 버전에서 사용되며 동기적인 통신을 기본으로 한다. HttpClient는 Apache HTTP 컴포넌트로 객체 생성이 쉽고 간결하지만 코드가 반복적이고 길다. RestTemplate은 스프링에서 제공하는 템플릿으로 사용하기 편하고 직관적이지만 동기적인 방식을 사용하며 커넥션 풀을 기본적으로 사용하지 않아서 연결할 때마다 로컬 포트를 열고 tcp connection을 맺어야 한다. WebClient는 스프링 5부터 도입된 웹 클라이언트 라이브러리로 비동기/논블로킹 방식을 지원하며 높은 처리량과 확장성을 지원한다. OpenFeign은 선언적 웹서비스 클라이언트로 어노테이션을 사용하여 인터페이스에 구현이 가능하다.

## Full Document
[[Full Document Contents/[Spring] 스프링에서 외부 API 호출하는 방법들 본문.md|See full document content →]]

## Highlights
- **spring RestTemplate** 
  **스프링에서 제공하는 http 통신에 유용하게 사용가능한 템플릿이다.** ([View Highlight](https://read.readwise.io/read/01hhgtf0ddtrtyr35ckwbgn0sh))
- **특징**
  • 스프링3.0에서 추가되었다.
  • org.springframework.http.client 패키지에 존재
  • HpptClient를 추상화해서 제공한다.
  • 대부분이 다른 API를 호출할 때 RestTemplate를 사용한다.
  • HTTP요청 후 JSON, XML, String 과 같은 응답을 받을 수 있다.
  • Blocking 기반의 동기방식을 사용한다.
  • HTTP 서버와의 통신을 단순화하고 Restful 원칙을 지킨다. 
  • header, content-type등을 설정하며 외부 API를 호출한다.
  • 서버-서버 통신에 사용한다. ([View Highlight](https://read.readwise.io/read/01hhgtfnctdvsh7ymsay6a2784))
    - Note: spring rest template 특징
- **webClient** 
  스프링 5부터 도입된 웹 클라이언트 라이브러리
  비동기/논블로킹 방식으로 외부 API를 호출할 수 있다. ([View Highlight](https://read.readwise.io/read/01hhgtge0j243fymxyd780mx6e))
- 비동기/논블로킹 방식을 지원하여, 높은 처리량과 확장성을 지원한다.
  리액티브 프로그래밍을 할 수 있다. 데이터 스트림을 효과적으로 처리할 수 있다. ([View Highlight](https://read.readwise.io/read/01hhgtgprc7f23dy9qxfh4qndk))
    - Note: spring webclient 장점
