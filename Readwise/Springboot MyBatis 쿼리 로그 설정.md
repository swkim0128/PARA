# Springboot MyBatis 쿼리 로그 설정

![rw-book-cover](https://velog.velcdn.com/images/harpuria/post/b6ec1158-06d5-44fe-bc92-c6a712f66385/unnamed.png)

## Metadata
- Author: [[velog.io]]
- Full Title: Springboot MyBatis 쿼리 로그 설정
- Category: #articles
- Document Tags:  #spring boot 
- Summary: To set up query logging in Spring Boot with MyBatis, add the log4jdbc dependency and configure the datasource in the application.properties file. You can customize logging levels for different SQL operations using either properties or a logback.xml file. Create a log4jdbc.log4j2.properties file to specify the logging behavior and maximum line length for SQL output.

## Full Document
[[Full Document Contents/Springboot MyBatis 쿼리 로그 설정.md|See full document content →]]

## Highlights
- • jdbc.sqlonly - SQL 문을 보여준다.
  • jdbc.sqltiming - SQL 문과 이 SQL 문을 수행하는 시간(ms)을 같이 보여준다.
  • jdbc.audit - ResultSet 을 제외한 모든 JDBC 호출 정보를 로그로 보여준다. 상당히 많은 양의 로그가 나오기 때문에 권장하지 않음.
  • jdbc.resultset - ResultSet 을 포함한 모든 JDBC 호출 정보를 로그로 보여준다. audit 처럼 많은 로그가 나오기 때문에 권장하지 않음.
  • jdbc.resultsettable - SQL 의 결과로 조회된 데이터를 table 형태로 로그를 보여준다.
  • jdbc.connection - DB 연결, 연결 해제와 관련된 로그를 보여준다 ([View Highlight](https://read.readwise.io/read/01je3rnwyjfp9s72rrd0pwsp0y))
