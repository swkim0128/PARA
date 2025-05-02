# RabbitMQ 메세지에 자바 Object 담아 보내기

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[Rena B]]
- Full Title: RabbitMQ 메세지에 자바 Object 담아 보내기
- Category: #articles
- Document Tags:  #rabbitmq  #spring boot 
- Summary: Message Converters 자바 Object 타입을 메세지로 보내기 위해서는 메세지 컨버터가 필요하다. SimpleMessageConverter -> RabbitTemplate에 디폴트로 설정된 컨버터이다. 바이트-자바 스트링/ 바이트-자바 Object 간 변환이 가능하다. 하지만 공식문서에서 말하길 추천하는 컨버터는 아니다. 그 이유는 '자바'에만 한정되어 사용되기 때문에, 다른 언어와의 호환성이 나쁘기 때문이다. SerializerMessageConverter -> 위와 같은 이유로 비추. Jackson2JsonMessageConverter One rather common alternative that is more flexible and portable across different lang..

## Full Document
[[Full Document Contents/RabbitMQ 메세지에 자바 Object 담아 보내기.md|See full document content →]]

## Highlights
- SimpleMessageConverter
  -> RabbitTemplate에 디폴트로 설정된 컨버터이다. 바이트-자바 스트링/ 바이트-자바 Object 간 변환이 가능하다. 하지만 공식문서에서 말하길 추천하는 컨버터는 아니다. 그 이유는 '자바'에만 한정되어 사용되기 때문에, 다른 언어와의 호환성이 나쁘기 때문이다. ([View Highlight](https://read.readwise.io/read/01hcyb6zkmnbvy5pfpzyxnw96c))
- producer/consumer 공통 config
  - Jackson2JsonMessageConverter 빈 생성 ([View Highlight](https://read.readwise.io/read/01hcyb94fkbzxrcdhjs9x6158b))
