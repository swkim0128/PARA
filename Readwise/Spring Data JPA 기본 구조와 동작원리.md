# Spring Data JPA 기본 구조와 동작원리

![rw-book-cover](https://img1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/7hZs/image/w2GywwwAifbWrXPHcZ1cNsP4Xso.jpg)

## Metadata
- Author: [[anonymDev]]
- Full Title: Spring Data JPA 기본 구조와 동작원리
- Category: #articles
- Document Tags:  #jpa  #spring boot 
- Summary: hibernate 코드로 이해하는 Spring Data JPA | Spring Data JPA(이하 스프링 JPA)는 Spring Data의 모듈로 JPA 기반의 데이터 접근 레이어(Data Access Layer)를 편하게 구현할 수 있도록 지원하는 프레임워크이다. 관계형 데이터베이스 기반의 데이터베이스를 활용해서 개발하는 스프링 프레임워크와 함께 널리 사용하는 모듈이다.  스프링 JPA는 Hibernate(이하 하이버

## Full Document
[[Full Document Contents/Spring Data JPA 기본 구조와 동작원리.md|See full document content →]]

## Highlights
- JpaRepository.save() 메서드를 호출해서 신규 생성한 엔티티를 저장하면 SessionImpl의 persist()가 호출된다 ([View Highlight](https://read.readwise.io/read/01hcc7r3956twa5h7a6scc9hfs))
- Persist 역시 이벤트로 발행되며 기본 리스너로 DefaultPersistEventListener가 등록돼있다. ([View Highlight](https://read.readwise.io/read/01hcc7rvkkwzv18jww574h55py))
- 신규 엔티티가 영속화되기 위해 데이터베이스 삽입(INSERT) 해야 한다. 이때 INSERT 명령이 바로 실행되지 않고 [ActionQueue](https://github.com/hibernate/hibernate-orm/blob/5b907ae8b13628baca432dd7269732e602a956b5/hibernate-core/src/main/java/org/hibernate/engine/spi/ActionQueue.java#L69)에 EntityInsertAction을 Enque 한다 ([코드](https://github.com/hibernate/hibernate-orm/blob/5b907ae8b13628baca432dd7269732e602a956b5/hibernate-core/src/main/java/org/hibernate/event/internal/AbstractSaveEventListener.java#L286)). ([View Highlight](https://read.readwise.io/read/01hcc823qerx0f0140ty7f86pv))
