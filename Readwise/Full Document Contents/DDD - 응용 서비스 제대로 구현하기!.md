# DDD - 응용 서비스 제대로 구현하기!

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FL4koA%2FbtrFi9YrqKU%2FzJXNl4Kbsbnfos2QXK0dp0%2Fimg.png)

## Metadata
- Author: [[JaeHoney]]
- Full Title: DDD - 응용 서비스 제대로 구현하기!
- Category: #articles
- Document Tags:  #ddd 
- Summary: 이 글은 도메인 주도 개발에서 응용 서비스의 역할과 구현 방법에 대해 설명합니다. 응용 서비스는 사용자 요청을 처리하고 도메인 객체와 표현 영역을 연결하는 중요한 역할을 합니다. 도메인 로직은 응용 서비스에 포함되지 않아야 하며, 이를 통해 코드 중복을 줄이고 유지 보수를 쉽게 해야 합니다.
- URL: https://jaehoney.tistory.com/231

## Full Document
해당 포스팅은 **"도메인 주도 개발 시작하기"**라는 내용을 정리한 글입니다. 해당 도서는 아래 Link에서 확인할 수 있습니다.

-<http://www.yes24.com/Product/Goods/108431347>

##### 표현 영역과 응용 영역

도메인 영역을 잘 만들었어도 도메인이 제 기능을 하려면 사용자와 도메인을 연결해주는 매개체가 필요하다. 응용 영역과 표현 영역은 **사용자와 도메인을 연결**해 주는 매개체 역할을 한다.

![](https://blog.kakaocdn.net/dn/L4koA/btrFi9YrqKU/zJXNl4Kbsbnfos2QXK0dp0/img.png)
표현 영역은 사용자의 요청을 해석한다. 해석된 메시지를 이용해서 사용자가 실행하고 싶은 기능을 제공하는 것은 응용 서비스가 담당한다. 즉, 실제 사용자가 원하는 기능을 제공하는 것은 응용 영역에 위치한 서비스이다.

##### 응용 서비스의 역할

**응용 서비스**는 **사용자(클라이언트)가 요청한 기능을 실행**한다. 응용 서비스는 사용자의 요청을 처리하기 위해 **리포지터리에서 도메인 객체를 가져와 사용**한다.

응용 서비스의 주요 역할은 도메인 객체를 사용해서 사용자의 요청을 처리하는 것이므로 표현(사용자) 영역 입장에서 보았을 때 응용 서비스는 도메인 영역과 표현 영역을 연결해 주는 **창구** 역할을 한다.

응용 서비스는 주로 **도메인 객체 간의 흐름을 제어**하기 때문에 다음과 같이 단순한 형태를 갖는다.

```
public Result doSomeFunc(SomeReq req) {
    // 1. 리포지터리에서 애그리거트를 구한다
    SomeAgg agg = someAggRepository.findById(req.getId());
    checkNull(agg);

    // 2. 애그리거트의 도메인 기능을 실행한다
    agg.doFunc(req.getValue());

    // 3. 결과를 리턴한다
    return createSuccessResult(agg);
}
```

새로운 애그리거트를 생성하는 응용 서비스 역시 간단하다.

```
public Result doSomeCreation(CreationSomeReq req) {
    // 1. 데이터 중복 등 데이터가 유효한지 검사한다
    checkValid(req);

    // 2. 애그리거트를 생성한다
    SomeAgg newAgg = createSome(req);

    // 3. 리포지터리에 애그리거트를 저장한다
    someAggRepository.save(newAgg);

    // 4. 결과를 리턴한다.
    return createSuccessResult(newAgg);
}
```

응용 서비스가 복잡하다면 응용 서비스에서 도메인 로직의 일부를 구현하고 있을 가능성이 높다. **응용 서비스가 도메인 로직을 일부 구현하면 코드 중복, 로직 분산 등 코드 품질에 안 좋은 영향**을 줄 수 있다.

###### 도메인 로직 넣지 않기

**도메인 로직이 응용 서비스에 있으면** 코드 관리가 힘들어진다. 어떤 도메인이 유효한 지 검사하는 로직을 응용 서비스에서 가진다고 생각해보자. 해당 도메인의 유효 여부를 검사하기 위해**해당 응용 서비스를 의존하거나 재구현해야 하는 일이 발생**한다.

아래는 응용 서비스에서 도메인 로직을 구현한 예이다.

```
public class ChangePasswordService {

    public void changePassword(String memberId, String oldPw, String newPw) {
        Member member = memberRepository.findById(memberId);
        checkMember(member);

        if (!passwordEncoder.matchs(oldPw, member.getPassword())) {
            throw new BadPasswordException();
        }
        member.setPassword(newPw);
    }
}
```

패스워드 여부가 일치하는 지 검증하는 부분은 다른 응용 서비스에서도 동일하게 구현하여야 한다. 즉, 코드가 중복되고 로직이 분산된다. 또는 응용 서비스에서 메서드를 추출한 후 해당 응용 서비스를 의존하면 되지만 의존하는 객체와 영역이 무의미하게 많아지므로 좋은 설계가 될 수 없다.

이는 **도메인 로직**이므로 **도메인 영역**에서 제공한다.

```
public class Member {

    public void changePassword(String oldPw, String newPw) {
        if (!matchPassword(oldPw)) throw new BadPasswordException();
        setPassword(newPw);
    }

    // 현재 암호와 일치하는지 검사하는 도메인 로직
    public boolean matchPassword(String pwd) {
        return passwordEncoder.matchs(pwd);
    }

    private void setPassword(String newPw) {
        if (isEmpty(newPw)) throw new IllegalArgumentException("no new password");
        this.password = newPw;
    }
}
```

이후 응용 서비스에서는 간단하게 메서드를 제공할 수 있다.

```
public class ChangePasswordService {

    public void changePassword(String memberId, String oldPw, String newPw) {
        Member member = memberRepository.findById(memberId);
        checkMember(member);
        member.changePassword(oldPw, newPw);
    }
    ...
}
```

소프트웨어의 가치를 높이려면 도메인 로직을 도메인 영역에 모아서 **코드 중복을 줄이고 응집도를 높여야 한다.**

##### 응용 서비스의 구현

응용 서비스는 포현 영역과 도메인 영역을 연결하는 매개체 역할을 하는데 이는 디자인 패턴에서 **파사드(facade)**와 같은 역할을 한다. 응용 서비스 자체는 복잡한 로직을 수행하지 않기 때문에 응용 서비스의 구현은 어렵지 않다.

응용 서비스를 구현할 때 몇 가지 고려할 사항에 대해 살펴보자.

###### 응용 서비스의 크기

회원 도메인을 생각해보자. 응용 서비스는 회원 가입하기, 회원 탈퇴하기, 회원 암호 변경하기, 비밀번호 초기화하기와 같은 기능을 구현하게 된다. 이때 두 가지 방법 중 한 가지 방식으로 구현한다.

* 한 응용 서비스 클래스에 회원 도메인의 모든 기능 구현하기
* 구분되는 기능별로 응용 서비스 클래스를 따로 구현하기

**한 응용 서비스 클래스에 모든 기능을 구현**하게 되면 코드 중복을 제거할 수 있다. 간단하게 메서드를 추출해서 private method를 구현해서 호출하면 된다. 반면, **한 서비스 클래스의 크기가 너무 커진다는 것이 단점**이다. **코드 크기가 커지면 연관성이 적은 코드가 한 클래스에 함께 위치**하게 되어서 **코드를 읽기 힘들게 만든다.**

구분 되는 기능별로 **응용 서비스 클래스를 분리**하면 클래스에서 **필요한 코드만 모이기 시작해서 코드 품질이 좋아지는 효과**가 일어난다. **읽기도 훨씬 깔끔하다는 장점**이 있다.

공통 로직에 대해 코드 중복이 발생할 수 있는데 **별도 클래스에 공통 로직을 구현**해서 코드가 중복되는 것을 방지할 수 있다. static 클래스로 구현하므로 Repository 참조를 매개변수로 받는다.

```
// 각 응용 서비스에서 공통되는 로직을 별도 클래스로 구현
public final class MemberServiceHelper {
    public static Member findExistingMember(MemberRepository repo, String memberId) {
        Member member = memberRepository.findById(memberId);
        if(member == null) {
            throw new NoMemberException(memberId);
        }
        return member;
    }
}
```

이후 Password를 변경하는 서비스 클래스만 따로 정의할 수 있다. **static import**를 사용해서 공통 로직을 구현한 클래스를 가져온다.

```
import static com.myshop.member.application.MemberServiceHelper.*;

public class ChangePasswordService {

    private MemberRepository memberRepository;

    public void changePassword(String memberId, String oldPw, String newPw) {
        Member member = findExistingMember(memberRepository, memberId);
        member.setPassword(newPw);
    }
}
```

결과적으로 한 클래스가 여러 역할을 갖는 것보다 각 클래스마다 구분되는 역할을 갖게 되어 더 관리하기가 수월해진다.

##### 응용서비스의 인터페이스와 클래스

응용 서비스를 구현할 때 논쟁이 될 만한 것이 인터페이스가 필요한 지 여부이다. 다음과 같이 인터페이스를 만들고 이를 상속한 클래스를 만드는 것이 필요할까?

```
public interface ChangePasswordService {
    public void changePassword(String memberId, String curPw, String newPw);
}

public class ChasngePasswordServiceImpl implements ChangePasswordService {
    ...구현
}
```

인터페이스가 필요한 몇 가지 상황이 있다. 예시를 보자.

* 구현 클래스가 여러 개인 경우

구현 클래스가 여러 개이고 런타임에 구현 객체를 교체해야 할 때 인터페이스를 유용하게 사용할 수 있다. 하지만 응용 서비스는 런타임에 교체하는 경우가 거의 없고 서비스 구현 클래스가 두 개인 경우도 드물다.

즉, 인터페이스와 구현 클래스를 따로 구현하면 **소스 파일만 많아지고 구현 클래스에 대한 간접 참조가 증가**해서 **전체 구조가 복잡**해진다. 따라서 인터페이스가 명확하게 필요한 상황이 아니라면 좋은 설계라고 볼 수 없다.

(단위 테스트를 위해 응용 서비스 클래스의 가짜 객체가 필요한데 이를 위해 인터페이스를 추가할 수도 있다. 하지만 Mockito와 같은 테스트 도구는 클래스에 대해서도 테스트용 대역 객체를 만들 수 있다.)

##### 파라미터와 값 리턴

응용 서비스는 사용자가 요구한 기능을 실행하는데 필요한 값을 파라미터로 전달받는다. 아래는 암호 변경 기능을 구현한 예시이다.

```
public class ChangePasswordService {
    public MemberNo changePassword(ChangePasswordRequest req) {
        ... 구현
        return memberNo;
    }
}
```

주의할 점은 **애그리거트 객체를 그대로 반환하면 안된다는 점**이다. 이는 표현 계층까지도 도메인 로직을 실행하는 역할을 가져간다는 의미가 된다. 즉, 응집도가 낮아지고 유지보수가 힘들어지는 결과를 초래할 수 있다. 응용 서비스는 표현 영역에서 필요한 데이터만 반환한다.

추가로 응용 서비스는 표현 계층에 의존해서는 안된다. 아래의 예시를 보자.

```
public class AuthenticationService {
    public void authenticate(HttpServletRequest request) {
       // ... 구현
    }
}
```

표현 계층의 HttpServletRequest를 응용 서비스 영역에서 파라미터로 받으면서 심각한 문제가 발생한다.

* 응용 서비스만 단독으로 테스트하기 어렵다.
* 표현 영역의 구현이 변경되면 응용 서비스도 영향을 받는다.
* 응용 서비스가 표현 영역의 역할을 대신하는 것이 가능해진다.
* 표현 영역의 상태를 응용 서비스가 변경하는 것이 가능해진다.

즉, 응용 서비스가 표현 영역을 의존하면서 표현 영역의 응집도가 낮아지고, 코드 유집 보수 비용이 증가되고 위험이 발생한다.

##### Reference

* <http://www.yes24.com/Product/Goods/108431347>

###### '[Programming](https://jaehoney.tistory.com/category/Programming) > [DDD](https://jaehoney.tistory.com/category/Programming/DDD)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [DDD - 도메인 서비스란 무엇인가 ?! (+ 다수의 애그리거트를 참조하는 방법)](https://jaehoney.tistory.com/248) (0) | 2022.07.14 |
| [DDD - 표현 영역과 응용 서비스! (+ 값 검증, 권한 검사, ...)](https://jaehoney.tistory.com/247) (6) | 2022.07.13 |
| [DDD - JPA를 이용한 Repository, Entity 매핑 제대로 구현하기!](https://jaehoney.tistory.com/228) (0) | 2022.06.16 |
| [DDD - 애그리거트(Aggregate)를 잘 사용하는 방법들!](https://jaehoney.tistory.com/223) (0) | 2022.06.09 |
| [DDD - Infrastructure Layer 설계하는 방법 (+ DIP 제대로 사용하기)](https://jaehoney.tistory.com/221) (2) | 2022.06.05 |
