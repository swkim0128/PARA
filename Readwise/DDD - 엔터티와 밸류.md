# DDD - 엔터티와 밸류

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZjK3Y%2FbtrC0MC2UGm%2FIbj51pp7uqsCtl8UM10Ehk%2Fimg.png)

## Metadata
- Author: [[JaeHoney]]
- Full Title: DDD - 엔터티와 밸류
- Category: #articles
- Document Tags:  #ddd 
- Summary: The text explains the distinction between entities and value types in domain-driven design (DDD). Entities have unique identifiers, like an order number, while value types represent a complete concept, such as a receiver or an address. Understanding these differences is crucial for correctly designing and implementing a domain model.
- URL: https://jaehoney.tistory.com/204

## Full Document
[[Full Document Contents/DDD - 엔터티와 밸류.md|See full document content →]]

## Highlights
- 엔터티
  엔터티의 가장 큰 특징은 **식별자**를 가진다는 것 ([View Highlight](https://read.readwise.io/read/01jvremaec4ck290ekryskvwj4))
- 엔티티의 **식별자는 바뀌지 않고 고유** ([View Highlight](https://read.readwise.io/read/01jvremjhqb04k1f32r2xhss60))
- 도메인 모델에 set 메서드 넣지 않기
  get/set을 도메인 모델에서 남발하지 않아야 한다는 것은 다들 알 것이다. 우리는 변경 가능한 값에 대해서만 set 메서드를 사용한다. 그런데, 변경 가능한 값이어도 set 메서드를 사용할 때는 각별히 주의 ([View Highlight](https://read.readwise.io/read/01jvrercbagdpn4bmckztw3qap))
