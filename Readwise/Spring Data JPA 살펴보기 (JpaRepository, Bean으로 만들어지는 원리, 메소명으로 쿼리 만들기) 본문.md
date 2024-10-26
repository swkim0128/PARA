# Spring Data JPA 살펴보기 (JpaRepository, Bean으로 만들어지는 원리, 메소명으로 쿼리 만들기) 본문

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FTMGdK%2FbtrpU0gQiFD%2FZI88KKgKa0FaGjykQ26IR0%2Fimg.png)

## Metadata
- Author: [[빨간색소년]]
- Full Title: Spring Data JPA 살펴보기 (JpaRepository, Bean으로 만들어지는 원리, 메소명으로 쿼리 만들기) 본문
- Category: #articles
- Document Tags: [[jpa]] [[spring boot]] 
- Summary: 참조문서 https://docs.spring.io/spring-data/jpa/docs/2.5.2/reference/html/#reference https://arahansa.github.io/docs_spring/jpa.html 1. 개요 Repository 추상화를 통해 interface 선언만으로도 JPA 사용 가능 만약, Spring Data JPA 를 사용하지 않는다면, javax.persistence 패키지의 EntityManager 를 사용하거나 JPQL을 이용해서 쿼리를 날렸어야 했음. JpaRepository 상속 메소드 이름으로 쿼리 생성 지원 이외에도 다양한 지원(페이징, 정렬, 도메인 클래스 변환) 2. JpaRepository 살펴보기 JpaRepository는 CrudReposi..
- URL: https://sjh836.tistory.com/190

## Highlights
- 아래 spring data JPA는 아래의 RepositoryFactorySupport 를 사용해서, Proxy 객체를 bean 으로 등록한다. ([View Highlight](https://read.readwise.io/read/01hcev3we1atx791ey7acafq9t))
