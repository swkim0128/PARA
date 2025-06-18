# DDD - 애그리거트(Aggregate)를 잘 사용하는 방법들!

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcPHQuf%2FbtrDYL5IbB3%2F4Gex8OKyXz5s0Wl2Kk1IkK%2Fimg.png)

## Metadata
- Author: [[Jae Honey]]
- Full Title: DDD - 애그리거트(Aggregate)를 잘 사용하는 방법들!
- Category: #articles
- Document Tags:  #ddd 
- Summary: This text explains how to effectively use aggregates in domain-driven design. Aggregates help simplify complex domains by grouping related models, ensuring consistency and managing their lifecycle together. The aggregate root manages the domain rules and prevents direct changes to its components, promoting a clearer and more maintainable structure.
- URL: https://jaehoney.tistory.com/223

## Full Document
[[Full Document Contents/DDD - 애그리거트(Aggregate)를 잘 사용하는 방법들!.md|See full document content →]]

## Highlights
- 도메인 규칙을 지키기 위해 애그리거트에 속한 모든 객체가 정상 상태를 가져야 한다. ([View Highlight](https://read.readwise.io/read/01jvrf9x6wgccexk2qkvk30z5w))
- **애그리거트 전체를 관리할 주체가 필요**한데 이 책임을 지는 것이 바로 **애그리거트의 루트 엔터티** ([View Highlight](https://read.readwise.io/read/01jvrf9rb31gs1vy7qx308j2x3))
- 애그리거트 루트의 핵심 역할은 **애그리거트의 일관성이 깨지지 않도록 하는 것** ([View Highlight](https://read.readwise.io/read/01jvrfahssw68jda22nvdbfeg9))
- 애그리거트 루트는 애그리거트 내부의 다른 객체를 조합해서 기능을 완성 ([View Highlight](https://read.readwise.io/read/01jvrfckdqkz7rhh2p4k6jnemd))
- **한 트랜잭션**에서는 **한 개의 애그리거트만 수정**해야 한다. 이는 **애그리거트에서 다른 애그리거트를 변경하지 않는다는 것**을 뜻한다 ([View Highlight](https://read.readwise.io/read/01jvrfe5y93ypft7d6wq8f90qc))
- 가장 큰 문제는 **편리함 오용**이다. **한 애그리거트에서 다른 애그리거트 객체에 접근하면 상태를 변경할 수 있게 된다.** 이런 부분은 애그리거트 간의 **의존 결합도를 높여서 변경을 어렵게** 만든다. 두 번째는 **지연 로딩과 즉시 로딩 등을 고민**하게 만든다는 점이고, 마지막 문제는 **확장**이다. 부하 분산을 위해 **시스템을 분리하기가 어려워진다.** ([View Highlight](https://read.readwise.io/read/01jvrjhdeecg3k3sf95hxjj88h))
