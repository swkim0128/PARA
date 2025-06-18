# DDD - 표현 영역과 응용 서비스! (+ 값 검증, 권한 검사, ...)

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[JaeHoney]]
- Full Title: DDD - 표현 영역과 응용 서비스! (+ 값 검증, 권한 검사, ...)
- Category: #articles
- Document Tags:  #ddd 
- Summary: This text summarizes key concepts from the "Domain-Driven Development" book, focusing on the roles of the presentation layer and application services. It explains how value validation and permission checks are divided between these layers to enhance user experience and security. Additionally, it discusses the implementation of read-only features and how they can simplify service code.
- URL: https://jaehoney.tistory.com/247

## Full Document
해당 포스팅은 **"도메인 주도 개발 시작하기"**라는 내용을 정리한 글입니다. 해당 도서는 아래 Link에서 확인할 수 있습니다.

-<http://www.yes24.com/Product/Goods/108431347>

##### 표현 영역

표현 영역의 책임은 크게 다음과 같다.

* 사용자가 시스템을 사용할 수 있는 흐름(화면)을 제공하고 제어한다.
* 사용자의 요청을 알맞은 응용 서비스에 전달하고 결과를 사용자에게 제공한다.
	+ 응용 서비스에서 익셉션이 발생 시 예외에 맞게 처리해서 사용자에게 노출한다.
* 사용자의 세션을 관리한다.

##### 값 검증

값 검증은 표현 영역과 응용 서비스에서 모두 수행할 수 있다. 원칙적으로 모든 값에 대한 검증은 응용 서비스에서 처리한다. 하지만 표현 영역은 잘못된 값이 존재하면 이를 사용자에게 알려주고 값을 다시 입력받아야 한다. 만약 응용 서비스에서 값을 검증하면 그에 따른 예외 처리를 위해 복잡한 try, catch문을 실행해야 한다는 단점이 있다.

응용 서비스에서 각 값이 유효한지 확인할 목적으로 Exception를 사용하면 사용자에게 좋지 않은 경험을 제공한다는 것이다.

사용자는 폼에 값을 입력하고 전송했는데 잘못된 값이 있을 때 한 개 항목이 아닌 잘못된 항목을 모두 알고싶다. 그런데 응용 서비스에서 값을 검사하는 시점에는 한 항목에서 예외가 터지면 나머지 항목은 검사를 하지 않게 된다.

-> 이때는 Validation을 사용한다. 잘못된 값이 존재하면 List<ValidationError>에 추가해서 하나의 Exception으로 던진다.

```
List<ValidationError> errors = new ArrayList<>();
if(orderRequest == null) {
    errors.add(ValidationError.of("empty");
} else {
    if(orderRequest.getOrdererMemberId() == null) {
        errors.add(ValidationError.of("ordererMemberId", "empty");
    }
    if(orderRequest.getOrderProducts() == null) {
        errors.add(ValidationError.of("orderProducts", "empty");
    }
    ... 구현
}

if(!errors.isEmpty()) throw new ValidationErrorException(errors);
```

표현 영역과 응용 서비스가 값 검사를 나눠서 수행할 수도 있다. 표현 영역에서 필수 값과 값의 형식을 검사한다. 응용 서비스는 ID 중복 여부와 같은 논리적 오류만 검사하면 된다.

* 표현 영역: 필수 값, 값의 형식, 범위 등을 검증한다.
* 응용 서비스: 데이터의 존재 유무와 같은 논리적 오류를 검증한다.

##### 권한 검사

권한 검사란 사용자 A가 특정 기능을 사용할 수 있는 지 확인하는 것이다.

권한 검사는 아래의 세 곳에서 수행할 수 있다.

* 표현 영역
* 응용 서비스
* 도메인

표현 영역에서 할 수 있는 기본적인 검사는 인증된 사용자인지 검사하는 것이다. 가령, 회원 정보 변경의 경우 다수의 URL로의 접근 중 인증된 사용자의 접근만 허가해야 한다. 예를 들어 아래와 같이 접근을 제어할 수 있다.

* URL을 처리하는 컨트롤러에 웹 요청을 전달하기 전에 인증 여부를 검사한다.
* 인증된 사용자가 아닐 경우 로그인 화면으로 Redirect 시킨다.

이런 접근 제어를 하기에 좋은 위치가 서블릿 필터(Servlet Filter)이다. 서블릿 필터에서 해당 용청을 인증 필터 이후에 권한 검사 필터를 태워서 인증 여부를 검사하면 된다.

Spring Security를 사용하면 웹 접근에 원하는 지점에 필터를 두고 사용할 수 있다. 추가로 단순한 시스템은 인증 여부만 검사하면 되지만, 어떤 시스템은 관리자 여부를 확인하기도 하고 특정 역할을 확인하기도 한다. Spring Security 같은 프레임워크는 이러한 다양한 상황을 충족하기 위해 유연하고 확장 가능한 구조를 갖고 있다.

만약 URL만으로 접근 제어를 할 수 없는 경우 응용 서비스의 메서드 단위로 권한 검사를 수행해야 한다. 하지만 응용 서비스 메서드가 권한 검사를 꼭 직접 수행해야 하는 것은 아니다. Spring Security는 AOP를 활용해서 애노테이션으로 권한 검사를 할 수 있는 기능을 제공한다.

```
public class BlockMemberService {
    private MemberRepository memberRepository;    
    
    @PreAuthorize("hasRole('ADMIN')")
    public void block(String memberId) {
    	Member member = memberRepository.findById(memberId);
    	if (member == null) throw new NoMemberException();
    	member.block();
    	...
    }
}
```

개별 도메인 객체 단위로 권한 검사를 하는 경우 구현이 더 복잡하다. 게시글 삭제는 본인 또는 관리자 역할을 가진 사용자만 할 수 있다. 이 경우 직접 권한 검사 로직을 구현해야 한다.

```
public class DeleteArticleService {
    public void delete(String userId, Long articleId) {
    	Article article = articleRepository.findById(articleId);
    	checkArticleExistence(article);
    	permissionService.checkDeletePermission(userId, article);
    	article.markDeleted();
    }
    ...
}
```

스프링 시큐리티와 같은 보안 프레임워크를 확장해서 개별 도메인 객체 수준의 권한 검사 기능을 프레임워크에 통합할 수도 있다. 다만 도메인에 맞게 보안 프레임워크를 확장하려면 프레임워크에 대한 높은 이해가 필요하다.

##### 조회 전용 기능

서비스에서 조회 전용 기능을 사용하면 서비스 코드가 다음과 같이 단순히 조회 전용 기능을 호출하는 형태로 끝날 수 있다.

```
public class OrderListService {
    public List<OrderView> getOrderList(String ordererId) {
    	return orderViewDao.selectByOrderer(ordererId);
    }
}
```

서비스에서 수행하는 추가적인 로직이 없고 단일 쿼리만 실행하는 조회 전용 기능이어서 트랜잭션도 필요없다. 이 경우라면 굳이 서비스를 만들 필요 없이 표현 영역에서 바로 조회 전용 기능을 사용해도 문제가 없다.

```
public class OrderController {
    private OrderViewDao orderViewDao;
    
    @RequestMapping("/myorders")
    public String list(ModelMap model) {
    	String ordererId = SecurityContext.getAuthentication().getId();
    	List<OrderView> orders = orderViewDao.selectByOrderer(ordererId);
    	model.addAttribute("orders", orders);
    	return "order/list";
    }
...
```

##### Reference

* <https://incheol-jung.gitbook.io/docs/study/ddd-start/6>
* <http://www.yes24.com/Product/Goods/108431347>
