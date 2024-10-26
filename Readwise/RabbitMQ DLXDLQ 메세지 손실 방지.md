# RabbitMQ DLX/DLQ 메세지 손실 방지

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[신나게개발썰]]
- Full Title: RabbitMQ DLX/DLQ 메세지 손실 방지
- Category: #articles
- Summary: This text explains how to prevent message loss in RabbitMQ when restarting by configuring DLX and DLQ to store messages on disk using the durability and autoDelete options. It also discusses how to make Exchange/Queue configurations persistent by setting these options to true and false, respectively. Additionally, it highlights the importance of proper configuration when using annotations or the org.springframework.amqp.core package to create Queues.
- URL: https://devssul.tistory.com/30

## Highlights
- RabbitMQ 서버가 재시작 되었을 때 메세지가 없어지는 현상을 방지하기 위해선
  • Exchange/Queue 설정의 Durability값이 true인지와 Auto delete값이 false인지 확인
  • 메세지를 발송 할 때 메세지의 Delivery mode가 2인지 확인
  • 1 메모리 저장(손실 발생)
  • 2 디스크 저장(손실 없음) ([View Highlight](https://read.readwise.io/read/01j0340fjt0v0g2fqbmqdb8dj5))
- `@Exchange` 어노테이션의 기본 값은 디스크 저장 방식이고 `@Queue` 어노테이션은 Queue 이름(value 혹은 name 값)을 지정 하거나 durable 값에 true, autoDelete 값에 false로 지정해야 한다. ([View Highlight](https://read.readwise.io/read/01j03392yxjygjkyh257pmv0pb))
- 프로세스에서 오류나 예외가 발생해서 메시지를 재처리 해야 하는 경우 reject을 하게 되는데 reject를 하게 되면 다시 원래 Queue로 돌아가기 때문에 재처리 해야 할 메세지와 신규 메세지가 혼합되면서 처리 효율성이 떨어질 수 있습니다. 이때 DLX/DLQ를 구성하게 되면 reject된 메세지는 원래 Queue로 돌아가지 않고 DLX/DLQ로 가게 됩니다. ([View Highlight](https://read.readwise.io/read/01j033a29bntryj3qacjt1erpq))
