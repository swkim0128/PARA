# [RabbitMQ] Prefetch와 성능

![rw-book-cover](https://velog.velcdn.com/images/sdb016/post/e02a9695-2e04-4219-b17a-be60462a7a29/image.png)

## Metadata
- Author: [[velog.io]]
- Full Title: [RabbitMQ] Prefetch와 성능
- Category: #articles
- Document Tags:  #rabbitmq 
- Summary: Prefetch controls how many messages RabbitMQ sends to a consumer's memory at once, affecting processing speed. Adjusting the prefetch value can improve performance, especially when there are multiple consumers. You can set a single prefetch value for all consumers or customize it for each consumer in your application.

## Full Document
[[Full Document Contents/[RabbitMQ] Prefetch와 성능.md|See full document content →]]

## Highlights
- 어플리케이션 전체에서 동일한 Prefetch 값을 설정하는 방법 ([View Highlight](https://read.readwise.io/read/01j6e91jrr2j9hwh4q2gxabddq))
    - Note: simple prefetch
- Consumer 별로 다른 prefetch 값을 설정하는 방법 ([View Highlight](https://read.readwise.io/read/01j6e913tnrn5asmk9k9yryj4k))
    - Note: multiple prefetch
