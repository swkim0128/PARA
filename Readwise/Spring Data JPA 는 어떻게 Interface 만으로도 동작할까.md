# Spring Data JPA 는 어떻게 Interface 만으로도 동작할까?

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbQySU1%2Fbtrk6jL8jmg%2FUuYC9cEeWGtR3QadxGlBCK%2Fimg.png)

## Metadata
- Author: [[TISTORY]]
- Full Title: Spring Data JPA 는 어떻게 Interface 만으로도 동작할까?
- Category: #articles
- Document Tags:  #jpa  #spring boot 
- Summary: Spring Data JPA를 공부하면서 궁금한 것이 있었습니다. public interface MemberRepository extends JpaRepository { List findAllByName(String name); } 위와 같이 MemberRepository는 인터페이스고, @Repository 애노테이션을 붙여 놓지도 않았는데, 다음과 같은 코드가 가능했습니다. @Service public class MemberService { private final MemberRepository memberRepository; public MemberService(MemberRepository memberRepository) { this.memberRepository = memberRepository..

## Full Document
[[Full Document Contents/Spring Data JPA 는 어떻게 Interface 만으로도 동작할까.md|See full document content →]]

## Highlights
- memberRepository의 실제 객체를 보니 Proxy가 주입되어 있습니다. 그리고 그 Proxy는 SimpleJpaRepository를 타겟으로 가지고 있습니다. 결과적으로 다음과 같은 구조인 셈입니다. ([View Highlight](https://read.readwise.io/read/01hcetae67rrmgnagdqq7ee143))
- 동적으로 프록시를 생성하는 기능의 핵심은 바로 '리플렉션'입니다. ([View Highlight](https://read.readwise.io/read/01hcetbzmvyxdkbcjh3c0c5nsf))
- interface는 MemberRepository, target은 SimpleJpaRepository인 것을 확인할 수 있습니다. 이러한 과정을 보면 스프링은 MemberRepository를 구현하는 객체를 생성해주고 있었습니다. ([View Highlight](https://read.readwise.io/read/01hcetx5nbfkz32vr0rn8ty65x))
- 스프링은 사용자가 정의한 Repository 인터페이스를 구현하고 SimpleJpaRepository를 target으로 포함하는 Proxy를 동적으로 만들어준다 ([View Highlight](https://read.readwise.io/read/01hcetxjs3cztseh67z076b5pm))
