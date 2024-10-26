# [스프링부트 (5)] Spring Boot 로그 설정(1) - Logback

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbBxGTT%2FbtqB1F65XTP%2FxN7RNbSQ6Ln6ENTCEGpkT1%2Fimg.png)

## Metadata
- Author: [[갓대희]]
- Full Title: [스프링부트 (5)] Spring Boot 로그 설정(1) - Logback
- Category: #articles
- Document Tags: [[spring boot]] 
- Summary: 이번 포스팅은 스프링 부트 로그 설정에 대한 내용을 다루고 있습니다. 로그백은 log4j, log4j2와 비교했을 때 더 훌륭한 성능을 보여주는 로깅 프레임워크입니다. 스프링 부트에서는 logback-spring.xml 파일을 사용하여 로깅을 수행하며, 설정 파일은 우선순위에 따라 읽힙니다. 로그 레벨은 ERROR, WARN, INFO, DEBUG, TRACE로 구분되며, 각 레벨에 따라 설정된 로그를 출력합니다. 로그를 찍기 위해 LoggerFactory를 사용하여 로거 객체를 불러온 후, 해당 객체를 이용하여 로그를 출력할 수 있습니다.
- URL: https://goddaehee.tistory.com/206

## Highlights
- - 참고 순서
  1) classpath(resources디렉토리 밑)에 **logback-spring.xml파일**이 있으면 설정파일을 읽어간다. 
  2) logback-spring.xml파일이 없다면 **.yml(.properties)파일**의 설정을 읽어간다. 
  3) logback-spring.xml파일과 .yml(.properties)파일이 동시에 있으면 .yml(.properties) 설정 파일을 적용 후 **xml파일이 적용**된다. ([View Highlight](https://read.readwise.io/read/01hxrdmwjqt0hs0sw6smpnt0tm))
- - logback-spring.xml 파일을 resources 디렉토리에 만들어서 참조한다. ([View Highlight](https://read.readwise.io/read/01hpg2vg89ffvxb3w1a4kqkeac))
    - Note: spring boot에서 가져오는 resource 디렉토리 밑에 logback-spring.xml 파일을 생성하면 자동적으로 참조
- - 참고 순서
  1) classpath(resources디렉토리 밑)에 **logback-spring.xml파일**이 있으면 설정파일을 읽어간다. 
  2) logback-spring.xml파일이 없다면 **.yml(.properties)파일**의 설정을 읽어간다. 
  3) logback-spring.xml파일과 .yml(.properties)파일이 동시에 있으면 .yml(.properties) 설정 파일을 적용 후 **xml파일이 적용**된다. ([View Highlight](https://read.readwise.io/read/01hpg2wxtawkyr5rp8y90rz396))
- **▶ TRACE  <  DEBUG  <  INFO  <  WARN  <  ERROR**
  **1) ERROR : 요청을 처리하는 중 오류가 발생한 경우 표시한다.**
  2) WARN  : 처리 가능한 문제, 향후 시스템 에러의 원인이 될 수 있는 경고성 메시지를 나타낸다.
  3) INFO  : 상태변경과 같은 정보성 로그를 표시한다. 
  4) DEBUG : 프로그램을 디버깅하기 위한 정보를 표시한다.  
  5) TRACE : 추적 레벨은 Debug보다 훨씬 상세한 정보를 나타낸다. ([View Highlight](https://read.readwise.io/read/01hpg2y068ekgm1sn7c9h2931k))
    - Note: spring boot log level 설명
- **1) appender** 
  - log의 형태를 설정, 로그 메시지가 출력될 대상을 결정하는 요소 ([View Highlight](https://read.readwise.io/read/01hpg343mks93swv90rxkfdsnx))
- - appender의 class의 종류
  1) ch.qos.logback.core.ConsoleAppender : **콘솔**에 로그를 찍음, 로그를 OutputStream에 작성하여 콘솔에 출력되도록 한다.
  2) ch.qos.logback.core.FileAppender : **파일**에 로그를 찍음, 최대 보관 일 수 등를 지정할 수 있다.
  3) ch.qos.logback.core.rolling.RollingFileAppender : **여러개의 파일**을 롤링, 순회하면서 로그를 찍는다.(FileAppender를 상속 받는다. 지정 용량이 넘어간 Log File을 넘버링 하여 나누어 저장할 수 있다.)
  4) ch.qos.logback.classic.net.SMTPAppender : 로그를 **메일**에 찍어 보낸다.
  5) ch.qos.logback.classic.db.DBAppender : **DB**(데이터베이스)에 로그를 찍는다. ([View Highlight](https://read.readwise.io/read/01hpg34dbmcts2ras2gpwvvdbb))
    - Note: logback-spring.xml <appender> 설정
- ※ Logback-spring.xml은 **appender**와 **logger** 크게 두개로 구분된 ([View Highlight](https://read.readwise.io/read/01hq2gvk3tgwz0sx6gjgpnn5wc))
