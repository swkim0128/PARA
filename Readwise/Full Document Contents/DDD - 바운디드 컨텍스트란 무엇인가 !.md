# DDD - 바운디드 컨텍스트란 무엇인가 ?!

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FP0g6Y%2FbtrHCnAd1pe%2F85wbYZ1kMYNqrkzqv8tRe0%2Fimg.png)

## Metadata
- Author: [[JaeHoney]]
- Full Title: DDD - 바운디드 컨텍스트란 무엇인가 ?!
- Category: #articles
- Document Tags:  #ddd 
- Summary: 바운디드 컨텍스트는 도메인 모델의 경계를 설정하며, 각 컨텍스트는 서로 다른 요구사항과 기능을 가집니다. 이를 통해 시스템을 더 작은 단위로 나누어 유지보수를 쉽게 하고, 변경이 다른 영역에 영향을 미치지 않도록 합니다. 바운디드 컨텍스트를 활용하면 마이크로서비스 아키텍처와 잘 어울려 깔끔한 설계를 할 수 있습니다.
- URL: https://jaehoney.tistory.com/252

## Full Document
해당 포스팅은 **"도메인 주도 개발 시작하기"**라는 내용을 정리한 글입니다. 해당 도서는 아래 Link에서 확인할 수 있습니다.

-<http://www.yes24.com/Product/Goods/108431347>

##### 도메인 모델과 경계

도메인 모델을 만들 때 빠지기 쉬운 함정이 도메인을 완벽하게 표현하는 단일 모델을 만드는 시도를 하는 것이다.

한 도메인은 여러 하위 도메인으로 구분되기 때문에 한 개의 모델로 여러 하위 도메인을 모두 표현하려고 시도하면 하위 도메인을 공동체에 협력하는 자율적인 객체가 아닌 수동적인 개체로 만들어 버린다. 이는 OOP에 명백히 어긋나며 하위 도메인의 개념과 요구사항을 반영하기 어렵게 된다.

모델은 특정한 컨텍스트(문맥)에서 완전한 의미를 갖는다. 같은 제품이라도 카탈로그 컨텍스트와 재고 컨텍스트는 의미가 서로 다르다. 이렇게 구분되는 경계를 갖는 컨텍스트를 DDD에서는 **바운디드 컨텍스트(Bounded Context)**라고 한다.

바운디드 컨텍스트 단위로 패키지를 나누고 개발했을 때 아래의 장점이 있다.

* 시스템을 더 작은 단위로 한 눈에 알아볼 수 있다.
* 각 도메인 모델의 책임이 작아지므로 코드가 간결해진다.
* 바운디드 컨텍스트 간 책임이 명확해서 유지보수가 용이하다.
* 변경이 컨텍스트 외부로 무분별하게 전파되지 않는다.

나중에 언급하겠지만 MSA 분리가 매우 용이하다는 장점도 있다.

> 좋은 아키텍처는 시스템이 모노리틱 구조로 태어나서 단일 파일로 배포되더라도, 이후에는 독립적으로 배포 가능한 단위들의 집합으로 성장하고, 또 독립적인 서비스나 마이크로서비스 수준까지 성장할 수 있도록 만들어져야한다. 또한 좋은 아키텍처라면 나중에 상황이 바뀌었을 때 이 진행 방향을 거꾸로 돌려 원래 형태인 모노리틱 구조로 되돌릴 수도 있어야 한다 ― 클린 아키텍처

##### 바운디드 컨텍스트

바운디드 컨텍스트는 모델의 경계를 결정하며 한 개의 바운디드 컨텍스트는 논리적으로 한 개의 모델을 갖는다.

바운디드 컨텍스트는 용어를 기준으로 구분한다. 카탈로그 컨텍스트와 재고 컨텍스트는 서로 다른 용어를 사용하므로 서로 다른 컨텍스트로 분리할 수 있다.

바운디드 컨텍스트에서 개발할 때 주의할 점은 모델이 섞이지 않도록 하는 것이다. 바운디드 컨텍스트는 서로 다른 패키지에서 개발하고 서로의 영역이 명확해야 한다.

아래의 예시를 보자.

![](https://blog.kakaocdn.net/dn/P0g6Y/btrHCnAd1pe/85wbYZ1kMYNqrkzqv8tRe0/img.png)
카탈로그의 Product는 상품이 속할 Category와 연관을 갖지만 재고의 Product는 카탈로그의 Category와 연관을 맺지 않는다. 즉, 각자의 바운디드 컨텍스트에 있는 Product 엔터티는 개념이 서로 다르다.

마찬가지로 회원에 있는 Member는 비밀번호 수정이나 프로필 관리 등을 할 수 있을 것이다. 주문 바운디드 컨텍스트에서는 Member 대신 Orderer라는 엔터티를 사용하는데 Orderer는 비밀번호 수정이나 프로필 관리를 할 수 없다. Member와 Orderer는 모두 DB의 Member 테이블을 표현하지만 제공하는 기능이 서로 다르다.

##### 바운디드 컨텍스트 구조

바운디드 컨텍스트가 도메인 모델만 포함하는 것은 아니다.

바운디드 컨텍스트는 도메인 기능을 사용자에게 제공하는 데 필요한 표현 영역, 응용 서비스, 인프라스트럭쳐 영역을 모두 포함한다. 도메인 모델의 데이터 구조가 바뀌면 DB 테이블 스키마도 변경되므로 테이블도 바운디드 컨텍스트에 포함한다.

![](https://blog.kakaocdn.net/dn/bP7GY3/btrHIX2lldX/XwByJbUk3ykBFaT1IiHKK1/img.png)
즉, 바운디드 컨텍스트는 도메인 기능을 제공하는 데 필요한 모든 요소를 포함한다.

각 바운디드 컨텍스트는 서로 다른 구현 기술을 사용할 수도 있다. 하나의 바운디드 컨텍스트에서 두 방식을 혼합해서 사용할 수도 있다. (CQRS 패턴, ...)

##### 바운디드 컨텍스트 간 통합

쇼핑 사이트에서 매출 증대를 위해 카탈로그 하위 도메인에 개인화 추천 기능을 도입했다고 하자. 추천 시스템을 담당하는 팀이 새로 생겨서 해당 팀에서 주도적으로 추천 시스템을 만들기로 했다.

이렇게 되면 카탈로그 하위 도메인에 추천 기능을 위한 바운디드 컨텍스트가 생긴다.

![](https://blog.kakaocdn.net/dn/m2YXu/btrHK2g17N0/UDhMkVhZfkx9ZsrtexCC2k/img.png)
두 팀이 관련된 바운디드 컨텍스트를 개발하면 자연스럽게 두 바운디드 컨텍스트 간 **통합**이 발생한다. 통합이 필요한 기능은 다음과 같다.

* 사용자가 제품 상세 페이지를 볼 때 해당 상품과 유사한 상품 목록을 하단에 보여준다.

이는 다음과 같이 구현할 수 있다.

* 사용자가 카탈로그 바운디드 컨텍스트에 추천 목록 제품을 요청
* 카탈로그 바운디드 컨텍스트는 추천 바운디드 컨텍스트에게 추천 정보를 요청
* 카탈로그 바운디드 컨텍스트는 사용자에게 추천 정보를 제공

이때 중요한 점은 카탈로그 컨텍스트와 추천 컨텍스트의 도메인 모델이 서로 다르다는 점이다. 카탈로그는 제품을 중심으로 도메인 모델을 구현하지만 추천은 추천 연산을 위한 모델을 구현한다.

예를 들어 추천에서 제공하는 상품 모델은 상품의 상세 정보를 포함하지 않으며 추천 순위와 같은 데이터를 담게 된다.

카탈로그 시스템은 추천 시스템에서 받은 상품 모델을 사용하기보다는 카탈로그 도메인 모델을 사용해서 추천 상품을 표현해야 한다. 즉 다음과 같이 카탈로그의 모델을 기반으로 하는 도메인 서비스를 사용해서 추천 기능을 표현해야 한다.

```
public interface ProductRecommendationService {
    List<Product> getRecommendationOf(ProductId id);
}
```

도메인 서비스를 구현한 클래스는 인프라스트럭처 영역에 위치한다. 이 클래스는 외부 시스템과의 연동을 처리하고 외부 시스템의 모델과 현재 도메인 모델 간의 변환을 책임진다.

![](https://blog.kakaocdn.net/dn/drlAWe/btrHJZd3E6W/qssMkWU1kkxpEk4YW9KATk/img.png)
RecSystemClient는 외부 추천 시스템이 제공하는 REST API를 이용해서 특정 상품을 위한 추천 상품 목록을 로딩한다. 해당 응답은 카탈로그 도메인 모델과 일치하지 않을 수 있다.

```
{
    {itemID: 'PROD-1000', type: 'PRODUCT', rank: 100},
    {itemID: 'PROD-1001', type: 'PRODUCT', rank: 54}
}
```

RecSystemClient가 REST API를 통해 데이터를 읽어오고 카탈로그에 맞는 도메인으로 변환한다. 아래는 해당 코드를 나타낸 것이다.

```
public class RecSystemClient implements ProductRecommendationService {
    private ProductRepository productRepository;
    
    @Override
    public List<Product> getRecommendationOf(ProductId id) {
        List<Recommendation> items = getRecItems(id.getValue());
        return toProducts(items);
    }
    
    private List<RecommendationItem> getRecItems(String itemId) {
        return externalRecClient.getRecs(itemId);
    }
    
    private List<Product> toProducts(List<RecommendationItem> items) {
        return items.stream()
                .map(item -> toProductId(item.getItemId())
                .map(prodId -> productRepository.findById(prodId))
                .collect(toList());
    }
    
    private ProductId toProductId(String itemId) {
        return new ProductId(itemId);
    }
}
```

해당 코드의 책임이 많다고 생각되면 외부 클라이언트를 호출하는 부분과 Recommandation을 Product로 변환하는 부분을 나누면 된다.

가령 Translator라는 별도 클래스를 만들고 RecSystemClient에서 의존하게 구현하는 것도 가능하다.

> <참고> 마이크로 서비스와 바운디드 컨텍스트  
>   
> MSA는 단순 유행을 지나 많은 기업에서 자리를 잡아가고 있다. 넷플릭스나 아마존 뿐 아니라 국내에도 많은 기업이 MSA를 수용하고 있다. MSA는 REST API나 메시징 큐를 이용해서 통신하는 구조를 가진다.  
>   
> 이런 마이크로 서비스의 특징은 DDD의 바운디드 컨텍스트와 잘 어울린다. 각 바운디드 컨텍스트는 모델의 경계를 형성하는데 바운디드 컨텍스트를 마이크로 서비스로 구현하면 자연스럽게 컨텍스트별로 서비스가 분리된다. 즉, 코드 수준에서도 컨텍스트를 분리하여 깔끔한 설계를 만들게 된다.

##### 컨텍스트 맵

개별 바운디드 컨텍스트에 매몰되어서 전체를 못보게 되는 경우가 종종 있다.

컨텍스트 맵은 화이트보드나 PPT와 같은 도구를 사용해 매우 간단하게 바운디드 컨텍스트간의 관계를 그릴 수 있다.

![](https://blog.kakaocdn.net/dn/dQOxs6/btrHPfgVLmq/DQTwc8zJsXte2eKTOUdUjk/img.png)
그림의 OHS는 오픈 호스트 서비스이며, 하류 컴포넌트의 요구사항을 수용하는 단일 API를 만들고 개방해서 하류 컴포넌트에게 협력하는 것을 의미한다.

ACL은 안티코럽션 계층을 나타낸다. 이는 외부 시스템과의 연동을 처리할 때 외부 시스템의 도메인 모델이 내 모델의 도메인 모델을 침범하지 않도록 막아주는 역할을 한다.

예를 들어, Order는 Member가 자신의 도메인 모델에 침범하지 않도록 Orderer라는 도메인 모델로 변환을 수행해주는 안티코럽션 계층을 사용할 수 있다.

컨텍스트 맵은 시스템의 전체 구조를 보여준다. 이는 하위 도메인과 일치하지 않는 바운디드 컨텍스트를 찾아 도메인에 맞게 바운디드 컨텍스트를 조절하고 파악하는 데 도움을 준다.

##### Reference

###### '[Programming](https://jaehoney.tistory.com/category/Programming) > [DDD](https://jaehoney.tistory.com/category/Programming/DDD)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [DDD - CQRS란 무엇인가?!](https://jaehoney.tistory.com/255) (0) | 2022.08.08 |
| [DDD - 이벤트란 무엇인가 ?! (+ 마이크로 서비스 간 트랜잭션 처리)](https://jaehoney.tistory.com/254) (0) | 2022.08.03 |
| [DDD - 트랜잭션과 잠금을 관리하는 다양한 방법!](https://jaehoney.tistory.com/251) (0) | 2022.07.19 |
| [DDD - 도메인 서비스란 무엇인가 ?! (+ 다수의 애그리거트를 참조하는 방법)](https://jaehoney.tistory.com/248) (0) | 2022.07.14 |
| [DDD - 표현 영역과 응용 서비스! (+ 값 검증, 권한 검사, ...)](https://jaehoney.tistory.com/247) (6) | 2022.07.13 |
