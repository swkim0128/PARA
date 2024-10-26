# [Spring Boot] 외부에서 설정 주입하기

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article4.6bc1851654a0.png)

## Metadata
- Author: [[latera.kr]]
- Full Title: [Spring Boot] 외부에서 설정 주입하기
- Category: #articles
- Document Tags: [[spring boot]] 
- Summary: (jar 내부와 같은)애플리케이션 클래스패스에서 name의 기본 프로퍼티 값을 제공하는 application. properties을 가질 수 있습니다.
- URL: https://www.latera.kr/reference/java/2019-09-29-spring-boot-config-externalize/

## Highlights
- Spring Boot는 값의 오버라이딩을 구분하도록 설계된 까다로운 순서의 `PropertySource`를 사용합니다. 프로퍼티는 다음의 순서로 고려됩니다.
  1. 홈 디렉터리(개발 도구가 활성화된 경우 `~/.spring-boot-devtools.properties`)의 [개발 도구 전역 설정 프로퍼티](https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-devtools.html#using-boot-devtools-globalsettings)
  2. 테스트의 [`@TestPropertySource`](https://docs.spring.io/spring/docs/5.1.9.RELEASE/javadoc-api/org/springframework/test/context/TestPropertySource.html) 어노테이션.
  3. 테스트의 `properties` 애트리뷰트. [`@SpringBootTest`](https://docs.spring.io/spring-boot/docs/2.1.7.RELEASE/api/org/springframework/boot/test/context/SpringBootTest.html)와 [애플리케이션의 특정 부분을 테스트하기 위한 테스트 어노테이션](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-testing.html#boot-features-testing-spring-boot-applications-testing-autoconfigured-tests)에서 사용 가능.
  4. 커맨드 라인 인자.
  5. `SPRING_APPLICATION_JSON`의 프로퍼티(환경 변수나 시스템 프로퍼티에 삽입된 인라인 JSON).
  6. `ServletConfig` 초기 파라미터.
  7. `ServletContext` 초기 파라미터.
  8. `java:comp/env`의 JNDI 애트리뷰트.
  9. Java 시스템 프로퍼티(`System.getProperties()`).
  10. OS 환경 변수
  11. `random.*` 에 프로퍼티를 가진`RandomValuePropertySource`.
  12. 패키지된 jar 외부의 [프로파일 지정 애플리케이션 프로퍼티](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html#boot-features-external-config-profile-specific-properties)(`application-{profile}.properties`와 YAML 형식).
  13. 패키지된 jar 내부의 [프로파일 지정 애플리케이션 프로퍼티](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html#boot-features-external-config-profile-specific-properties)(`application-{profile}.properties`와 YAML 형식).
  14. 패키지된 jar 외부의 애플리케이션 프로퍼티(`application-{profile}.properties`와 YAML 형식).
  15. 패키지된 jar 내부의 애플리케이션 프로퍼티(`application-{profile}.properties`와 YAML 형식).
  16. `@Configuration` 클래스의 `@PropertySource` 어노테이션
  17. (`SpringApplication.setDefaultProperties`에 의해 명시된) 기본 프로퍼티. ([View Highlight](https://read.readwise.io/read/01hdnfk010snh4sv3st0bpf498))
    - Note: spring boot properties 설정 우선순위
- • `.properties` 파일
  • YAML 파일
  • 환경 변수
  • 커맨드 라인 인자 ([View Highlight](https://read.readwise.io/read/01herterzdm6j7tkjr4gawqr9s))
    - Note: spring boot application property 설정 가능한 방법 목록
