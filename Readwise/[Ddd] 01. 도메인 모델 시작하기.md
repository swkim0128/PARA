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
[[Full Document Contents/[Ddd] 01. 도메인 모델 시작하기.md|See full document content →]]

## Highlights
- • **표현** ( Presentation )
  • 사용자의 요청을 처리하고 사용자에게 정보를 보여준다. 외부 시스템이 사용자가 될 수 도 있다.
  • 화면의 요청 / 응답을 처리하는 곳이다.
  • Controller
  • **응용** ( Application )
  • 사용자가 요청한 기능을 실행한다. 업무 로직을 직접 구현하지 않으며 도메인 계층을 조합해서 기능을 실행한다.
  • 기능 별로 구분지어 처리하는 곳이다.
  • Handler
  • **도메인** ( Domain )
  • 시스템이 제공할 도메인 규칙을 구현한다.
  • Entity, domain Service, Repository
  • **인프라스트럭처** ( Infrastructure )
  • 데이터베이스나 메시징 시스템과 같은 외부 시스템과의 연동을 처리한다.
  • Repository, Event ([View Highlight](https://read.readwise.io/read/01jvs2ptsa29qkhf1yyj8rqzxg))
- **도메인 모델 도출**
  • 도메인을 모델링할 때 기본이 되는 작업은 모델을 구성하는 핵심 구성요소, 규칙, 기능을 찾는 것이다. ([View Highlight](https://read.readwise.io/read/01jvs2k0xyapjccvaex3pvxsg6))
