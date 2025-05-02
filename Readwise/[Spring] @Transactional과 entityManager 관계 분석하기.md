# [Spring] @Transactional과 entityManager 관계 분석하기

![rw-book-cover](https://velog.velcdn.com/images/e1psycongr00/post/63416f57-c98f-4f42-af86-1015ecac1710/image.png)

## Metadata
- Author: [[velog.io]]
- Full Title: [Spring] @Transactional과 entityManager 관계 분석하기
- Category: #articles
- Document Tags:  #spring boot 
- Summary: The text discusses the relationship between the @Transactional annotation and the EntityManager in JPA, focusing on transaction management in Spring. It explains how AOP is used to manage transactions without modifying the method logic and highlights that each transaction creates a new EntityManager, which does not persist after the transaction ends. This means that if two transactions are used in one request, they will not share the same EntityManager, requiring careful management of entity states.

## Full Document
[[Full Document Contents/[Spring] @Transactional과 entityManager 관계 분석하기.md|See full document content →]]

## Highlights
- 인자로 다른 트랜잭션 내부에서 사용해도 persist 상태가 아니기 때문에 따로 merge를 해줘야 ([View Highlight](https://read.readwise.io/read/01je5tfzcny28jkyrfcjav45er))
