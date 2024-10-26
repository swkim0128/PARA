# [Message Queue]RabbitMQ를 사용해 메세지 주고 받기

![rw-book-cover](https://velog.velcdn.com/images/power0080/post/82206a29-e3c0-4138-8503-301d13fc8b3f/image.png)

## Metadata
- Author: [[velog.io]]
- Full Title: [Message Queue]RabbitMQ를 사용해 메세지 주고 받기
- Category: #articles
- Document Tags: [[rabbitmq]] 
- Summary: RabbitMQ is a popular open-source message queue system that can be easily set up using Docker to avoid complex installations. The guide explains how to create exchanges and queues, and bind them to handle message delivery efficiently. It also highlights the advantages of configuring RabbitMQ through code for better management and properties visibility.
- URL: https://velog.io/@power0080/Message-QueueRabbitMQ%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%B4-%EB%A9%94%EC%84%B8%EC%A7%80-%EC%A3%BC%EA%B3%A0-%EB%B0%9B%EA%B8%B0#4-rabbitlistener-%ED%99%9C%EC%9A%A9

## Highlights
- value : queue를 정의하는 attribute → `@Queue` 를 이용해 정의
  • `@Queue` 의 value : String으로 큐의 이름 지정 ⇒ 만약 지정한 이름의 queue가 존재하지 않는다면 해당 queue를 지정한 attribute의 값들에 따라 생성!(management를 쓰지 않고도 queue 생성 가능)
  • `@Queue` 의 durable : consumer의 처리를 기다리고 있는 메시지를 담고 있는 queue가 어떠한 이상으로 인해 죽어버리거나 재시작할 때 메시지가 소실될 수 있음 → 이 때 durable 속성을 true로 주면 이러한 상황이 발생했을 때 메시지를 유지할 수 있음(메시지 지속성 durablity 지정)
  • `@Queue` 의 exclusive : 큐 이름을 지정해주지 않았을 때, rabbitMQ에서 임의의 큐에 binding을 시킴. exclusive를 ture로 주면 임의의 큐와 consumer의 연결이 끊어졌을 때 해당 큐를 자동으로 제거함
  • `@Queue` 의 autoDelete : true를 주게 되면 consumer와 연결이 끊긴 큐를 자동 삭제(exclusive는 지정되지 않은 임의의 큐를 삭제함) ([View Highlight](https://read.readwise.io/read/01j6e86k43cdejnm3w24y4gwk2))
- exchange : exchange를 정의하는 attribute → `@Exchange` 를 이용해 정의
  • `@Exchange` 의 value : String으로 exchange의 이름 지정
  • `@Exchange` 의 type : exchange type을 지정, default 값은 “direct”
  • `@Exchange` 의 delayed : 메시지를 바로 큐에 보내는 게 아니라 일정 시간 후에 보내고자 할 때 사용. 값이 true라면 ‘x-delayed-message’ exchange에 메시지가 보내지고 일정 시간 후 큐로 메시지가 이동함. default 값은 false ([View Highlight](https://read.readwise.io/read/01j6e86r47hesmf4fxyzkdh5cp))
