# RabbitMQ DLX를 사용하여 예외발생 시 무한 Retry를 제한하자.

![rw-book-cover](https://velog.velcdn.com/images/gjwjdghk123/post/a6c71cb5-b082-4fbf-a761-c6f880744780/image.png)

## Metadata
- Author: [[velog.io]]
- Full Title: RabbitMQ DLX를 사용하여 예외발생 시 무한 Retry를 제한하자.
- Category: #articles
- Document Tags:  #rabbitmq 
- Summary: RabbitMQ can endlessly retry message processing until it's successful, which may lead to problems if exceptions occur. To manage failures better, you can use a Dead Letter Exchange (DLX) that directs failed messages to a different queue for alternative processing. This helps prevent infinite retries and allows for more effective error handling.

## Full Document
[[Full Document Contents/RabbitMQ DLX를 사용하여 예외발생 시 무한 Retry를 제한하자..md|See full document content →]]

## Highlights
- 실패한 메세지 Retry하기
  오류 처리기를 직접 구현하는 방법도 존재하지만 스프링에서 제공하는 방법으로 간단하게 재처리 로직을 구성할 수 있습니다. ([View Highlight](https://read.readwise.io/read/01j6ea35n4fmdh9s0baya78msq))
- • initial-interval: 초기 간격
  • max-interval: 최대 간격
  • max-attempts: 최대 재시도 횟수
  • multiplier: 간격 증가율 ([View Highlight](https://read.readwise.io/read/01j6ea386k61v97xqnd9bdv3qa))
    - Note: rabbitmq retry prorperties
