# Annotation 동작 원리와 사용법

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FULfwE%2FbtqPxdot2FM%2FQAEYbfGk6Hzx5y7l9244O1%2Fimg.png)

## Metadata
- Author: [[nova_dev]]
- Full Title: Annotation 동작 원리와 사용법
- Category: #articles
- Document Tags:  #annotation  #spring boot 
- Summary: Annotation 동작 원리와 사용법 Spring Boot를 사용하다 보면 @Component, @Controller, @Repository, @Transactional, @Aspect 등 다양한 어노테이션을 사용하게 된다. 그럼 이런 어노테이션이 실제로는 어떻게 동작하는 것인지, 내가 만약 새로운 어노테이션을 만들어서 사용하고 싶다면 어떻게 하면 되는 것인지에 대해 알아보자. 1. Annotation 이란? 우선 어노테이션 자체는 주석과도 같다. (실제로 번역기를 돌려도 주석으로 나온다.) 즉, 코드 사이에 주석처럼 쓰이면서 특별한 의미, 기능을 수행하도록 하는 기술로 프로그램에게 추가적인 정보를 제공해주는 메타 데이터이다. 2. 어노테이션의 용도 컴파일러에게 코드 작성 문법 에러를 체크하도록 정보를..

## Full Document
[[Full Document Contents/Annotation 동작 원리와 사용법.md|See full document content →]]

## Highlights
- 어노테이션 자체는 주석과도 같다. (실제로 번역기를 돌려도 주석으로 나온다.) ([View Highlight](https://read.readwise.io/read/01hckm1ee1sjfdnbahz196bx6d))
- 코드 사이에 주석처럼 쓰이면서 특별한 의미, 기능을 수행하도록 하는 기술로 프로그램에게 추가적인 정보를 제공해주는 메타 데이터 ([View Highlight](https://read.readwise.io/read/01hckm1nwem0w1wavvdta2sf3p))
- • 컴파일러에게 코드 작성 문법 에러를 체크하도록 정보를 제공한다.
  • 소프트웨어 개발툴이 빌드나 배치 시 코드를 자동으로 생성할 수 있도록 정보를 제공한다.
  • 런타임 시 특정 기능을 실행하도록 정보를 제공한다. ([View Highlight](https://read.readwise.io/read/01hckm25wfz03y9tf0rbqx2y9m))
    - Note: 어노테이션의 용도
- 어노테이션 파일을 정의하는데 필요한 것은 총 **세 가지**다. 
  (1) Target (어노테이션의 적용 대상) 
  (2) Retention (어노테이션이 유지되는 대상) 
  (3) Annotation Name (class가 아닌 @interface로 정의된 어노테이션 이름) ([View Highlight](https://read.readwise.io/read/01hckm34agv45272wm9z0q1dy4))
