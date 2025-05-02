# Spring Boot에서 Amazon MQ의 RabbitMQ 연동

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)

## Metadata
- Author: [[Joo-Kwang Park]]
- Full Title: Spring Boot에서 Amazon MQ의 RabbitMQ 연동
- Category: #articles
- Document Tags:  #rabbitmq  #spring boot 
- Summary: RabbitMQ는 오픈소스 메세지 브로커 소프트웨어이다. 메세지 브로커를 사용하여 다양한 어플리케이션 간 통신을 지원할 수 있다. 언어와 상관없이 AMQP(Advanced Message Queuing Protocol)을 사용하므로 확장성이 좋다고 할 수 있다. 메세지 브로커는 RabbitMQ 뿐만 아니라 Redis, Apache ActiveMQ 등 다양한 소프트웨어가 존재한다. 각 소프트웨어마다 차이점이 있지만, RabbitMQ의 특징만 정리한다. RabbitMQ는 메세지 전달을 위한 큐를 가지고 있다. 큐는 하나만 구성이 될 수 있으며, 여러개의 큐를 관리할 수 있다. 뿐만 아니라 네임스페이스를 만들어서 큐를 그룹핑 할 수 있다. 토픽이라는 것이 있으며 MQTT(Message Queuing Telemetry Transport)와 같은 방식으로 메세지를 전달할 수 있다. 추후 RabbitMQ 에 대한 내용은 RabbitMQ Tutorial을 정리할 예정이다.

## Full Document
[[Full Document Contents/Spring Boot에서 Amazon MQ의 RabbitMQ 연동.md|See full document content →]]

## Highlights
- listener에서 acknowledge-mode가 manual인데, 스프링 부트에서 RabbitMQ Listener에서 메세지를 정상적으로 처리가 됐다는 ack을 수동으로 보내겠다는 의미이다. ([View Highlight](https://read.readwise.io/read/01hcyb0a7drc2wtmyz6ggr3jm4))
- 내부에서 처리하는 코드를 보면, channel.basicAck 라고 메세지를 정상적으로 받았다는 ack를 수동으로 보내는 것을 확인할 수 있다. 이렇게 처리하는 이유는 내부적인 exception 발생 시 메세지를 다시 처리 하기 위한 수단 ([View Highlight](https://read.readwise.io/read/01j02dbwgjrbjx00h7437ccrhx))
- RabbitHandler 어노테이션을 메소드에 달아주면, RabbitListener에 명시한 큐의 데이터를 처리할 수 있다. ([View Highlight](https://read.readwise.io/read/01hcyb5r12s0f2q2zmvphkzhyd))
