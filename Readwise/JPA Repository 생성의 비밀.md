# JPA Repository 생성의 비밀

![rw-book-cover](https://img1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/7hZs/image/h0Ars9FQnnRlQZhY-gnZV0vWxyI.JPG)

## Metadata
- Author: [[anonymDev]]
- Full Title: JPA Repository 생성의 비밀
- Category: #articles
- Document Tags: [[jpa]] [[spring boot]] 
- Summary: JPA Repository 생성은 spring-data-jpa를 사용하면 인터페이스로 선언해서 사용할 수 있다. 하지만 메서드들은 직접 구현하지 않아도 된다. 대신 SimpleJpaRepository에 구현되어 있다. JpaRepositoryFactory 클래스가 개발자가 정의한 인터페이스를 참조하여 JpaRepository를 대신 구현하며, RepositoryFactorySupport를 확장하여 getRepository를 상속 받는다. 최종적으로 Bean으로 생성되는 CountryRepository는 Proxy Repository 인스턴스이며, SimpleJpaRepository가 뒤에서 JpaRepository 인터페이스의 실 구현체를 제공한다.
- URL: https://brunch.co.kr/@anonymdevoo/40

## Highlights
- spring-data-jpa에는 JPARepository를 생성하는 JpaRepositoryFactory 클래스가 존재하는데 개발자가 정의한 CountryRepository 인터페이스를 참조하여 JpaRepository를 대신 구현하는 역할을 한다. ([View Highlight](https://read.readwise.io/read/01hccaz0j2wbmx9m8r2ymxz7h8))
- RepositoryFactorySupport는 전달받은 Repository 인터페이스로 Proxy 인스턴스를 생성하는 추상 클래스이다. ([View Highlight](https://read.readwise.io/read/01hccb04q34wrv8jxkjq992959))
- CountryRepository 인터페이스는 자체는 사실 껍데기에 불과하다. spring-data-jpa에는 JPARepository를 생성하는 JpaRepositoryFactory 클래스가 존재하는데 개발자가 정의한 CountryRepository 인터페이스를 참조하여 JpaRepository를 대신 구현하는 역할을 한다. ([View Highlight](https://read.readwise.io/read/01hcet4m3sfbe083f28n14h78h))
- RepositoryFactorySupport를 확장하여 다양한 spring-data-XXX에서 Repository를 생성한다. RepositoryFactorySupport에는 getRepository라는 Repository 인스턴스를 생성하는 메서드가 기본으로 정의돼 있다. ([View Highlight](https://read.readwise.io/read/01hccb1fq4w7wd1dsq5p6k05nf))
- 이 메서드는 Repository 인터페이스를 구현한 Proxy를 생성한다. JpaRepositoryFactory는 부모 클래스의 메서드인 getRepository를 상속 받는다. ([View Highlight](https://read.readwise.io/read/01hceva0stmm3axkwfemtczfbx))
- spring-data-jpa는 JpaRepositoryFactory가 추상 메서드인 getRepositoryBaseClass를 SimpleJpaRepository.class를 반환하도록 오버라이드 했다. ([View Highlight](https://read.readwise.io/read/01hcewjd4xs4fxer0rv7akmj4a))
    - Note: JpaRepository로 생성이 될 경우 프록시 패턴에서 실행하는 구현체를 SimpleJpaRepository 객체로 반환
- Proxy 인스턴스의 target이 TargetRepository였구나! 즉 Proxy로 생성된 Repository 인스턴스의 target 인스턴스가 SimpleJpaRepository의 인스턴스였다는걸 알게 됐다. 그렇다면 **SimpleJpaRepository가 뒤에서 JpaRepository 인터페이스의 실 구현체를 제공한다는 의미이다**. ([View Highlight](https://read.readwise.io/read/01hcexshwz3ehzernmft54xgkk))
- 1. 최종적으로 Bean으로 생성되는 CountryRepository는 Proxy 인스턴스이다(Proxy Repository).
  2. JpaRepository는 Proxy 인스턴스의 Target을 SimpleJpaRepository.class의 인스턴스로 주입한다.
  3. Proxy Repository 인스턴스 내부에서 SimpleJpaRepository(target)가 실 구현체를 실행한다. ([View Highlight](https://read.readwise.io/read/01hcexsyvw4239cyhqznbcr8c0))
