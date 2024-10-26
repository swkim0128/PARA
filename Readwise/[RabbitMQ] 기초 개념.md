# [RabbitMQ] 기초 개념

![rw-book-cover](https://velog.velcdn.com/images/sdb016/post/71ee0537-b4e2-4dee-abd5-ab00e167eb94/image.png)

## Metadata
- Author: [[velog.io]]
- Full Title: [RabbitMQ] 기초 개념
- Category: #articles
- Document Tags: [[rabbitmq]] 
- Summary: AMQP를 구현한 오픈소스 메세지 브로커이다.producers에서 consumers로 메세지(요청)를 전달할 때 중간에서 브로커 역할을 한다.사용하는 케이스는 다음과 같다.요청을 많은 사용자에게 전달할 때요청에 대한 처리시간이 길 때많은 작업이 요청되어 처리를 해야할 
- URL: https://velog.io/@sdb016/RabbitMQ-%EA%B8%B0%EC%B4%88-%EA%B0%9C%EB%85%90

## Highlights
- • Producer: 요청을 보내는 주체, 보내고자 하는 메세지를 exchange에 publish한다.
  • Consumer: producer로부터 메세지를 받아 처리하는 주체
  • Exchange: producer로부터 전달받은 메세지를 어떤 queue로 보낼지 결정하는 장소, 4가지 타입이 있음
  • Queue: consumer가 메세지를 consume하기 전까지 보관하는 장소
  • Binding: Exchange와 Queue의 관계, 보통 사용자가 특정 exchange가 특정 queue를 binding하도록 정의한다. (fanout 타입은 예외) ([View Highlight](https://read.readwise.io/read/01hckwy8gxr7zkp5h358v7dfwj))
- Binding은 Exchange와 Queue를 연결하는 관계 ([View Highlight](https://read.readwise.io/read/01hckwyq82epa76rpfxzbbknaj))
- Exchange는 다음과 같은 속성을 가진다.
  • Name: Exchange 이름
  • Type: 메시지 전달 방식
  • Direct
  • Fanout
  • Topic
  • Headers
  • Durability: 브로커가 재시작될 때 남아있는지 여부
  • Durable: 브로커가 재시작되어도 디스크에 저장되어 남아있음
  • Transient: 브로커가 재시작되면 사라짐
  • Auto-delete: 마지막 Queue 연결이 해제되면 삭제 ([View Highlight](https://read.readwise.io/read/01hckx061ep5bmk112491anefc))
- Queue는 다음과 같은 속성을 가진다.
  • Name: Queue 이름, `amq.`은 예약어로써 사용 불가
  • Durability: 브로커가 재시작될 때 남아있는지 여부
  • Durable: 브로커가 재시작되어도 디스크에 저장되어 남아있음
  • Transient: 브로커가 재시작되면 사라짐
  • Auto delete: 마지막 Consumer가 consume을 끝낼 경우 자동 삭제
  • Argument: 메시지 TTL, Max Length 같은 추가 기능 명시 ([View Highlight](https://read.readwise.io/read/01hckx0z5btg215p4h5n0s6rwn))
- Direct라우팅 키가 정확히 일치하는 Queue에 메시지 전송Topic라우팅 키 패턴이 일치하는 Queue에 메시지 전송Headers[key:value]로 이루어진 header값을 기준으로 일치하는 Queue에 메시지 전송Fanout해당 Exchange에 등록된 모든 Queue에 메시지 전송 ([View Highlight](https://read.readwise.io/read/01hckx1bwxga6wdya40hxmpt8p))
- 라우팅 키를 이용하여 메시지를 전달할 때 정확히 일치하는 Queue에만 전송 ([View Highlight](https://read.readwise.io/read/01hckx3rq1cagbtge0tjfk5e2x))
    - Note: direct exchange 규칙
- 라우팅 키의 패턴을 이용해 메시지를 라우팅한다. ([View Highlight](https://read.readwise.io/read/01hckx4pdcnvge7m41kdmtkv14))
    - Note: topic exchange 설정 규칙
- Topic과 유사한 방법이지만 라우팅을 위해 header를 사용한다는 점에서 차이가 있다. 
  producer에서 정의된 header의 key-value 쌍과 consumer에서 정의된 argument의 key-value 쌍이 일치하면 binding된다. ([View Highlight](https://read.readwise.io/read/01hckx65br5nx71jj175823eqp))
    - Note: headers exchange 규칙
- Exchange에 등록된 모든 Queue에 메시지를 전송한다. ([View Highlight](https://read.readwise.io/read/01hckx6rbv8g0y6dv192nfh64r))
    - Note: fanout exchange 규칙
