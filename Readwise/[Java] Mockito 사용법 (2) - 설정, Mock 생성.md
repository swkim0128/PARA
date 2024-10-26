# [Java] Mockito 사용법 (2) - 설정, Mock 생성

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbvuoPu%2FbtqU0xooOfC%2FBahyUL5CKLXASpycTuZdtK%2Fimg.png)

## Metadata
- Author: [[노력남자]]
- Full Title: [Java] Mockito 사용법 (2) - 설정, Mock 생성
- Category: #articles
- Document Tags: [[spring boot]] [[unit test]] 
- Summary: This text explains how to configure Mockito and create mock objects using annotations like @Mock, @Spy, and @InjectMocks. 
@Mock is for creating fake objects that require stubbing, @Spy is for creating real objects with or without stubbing, and @InjectMocks is for automatically injecting mock objects.
By using these annotations, you can easily set up and manage dependencies in your test classes.
- URL: https://effortguy.tistory.com/142

## Highlights
- **@Mock**
  @Mock으로 만든 **mock 객체는 가짜 객체이며 그 안에 메소드 호출해서 사용하려면 반드시 스터빙(stubbing)**을 해야합니다. ([View Highlight](https://read.readwise.io/read/01hx8d8dyv1v58tb57fvpxwtf9))
- **@Spy**
  @Spy로 만든 **mock 객체는 진짜 객체이며 메소드 실행 시 스터빙을 하지 않으면 기존 객체의 로직을 실행한 값을, 스터빙을 한 경우엔 스터빙 값을 리턴** ([View Highlight](https://read.readwise.io/read/01hx8d8vzrj6nagbt2sgtar5r0))
- @InjectMock은 DI를 **@Mock이나 @Spy로 생성된 mock 객체를 자동으로 주입**해주는 어노테이션 ([View Highlight](https://read.readwise.io/read/01hx8d93tqscdgn1jeykr4njjp))
