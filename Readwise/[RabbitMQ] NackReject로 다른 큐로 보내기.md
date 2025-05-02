# [RabbitMQ] Nack/Reject로 다른 큐로 보내기

![rw-book-cover](https://blog.leocat.kr/assets/img/logo-high-resolution.png)

## Metadata
- Author: [[스뎅(thDeng)]]
- Full Title: [RabbitMQ] Nack/Reject로 다른 큐로 보내기
- Category: #articles
- Document Tags:  #rabbitmq 
- Summary: RabbitMQ로 메시지를 처리할 때 문제가 발생하면, 다음 메시지를 처리하기 위해 현재 메시지를 건너뛰어야 할 수 있습니다. 임시로 다른 API 호출이나 연결 문제가 있는 메시지는 나중에 재시도해서 처리할 수 있기 때문에 문제가 되는 메시지는 잠시 다른 곳에 보관됩니다. 이를 위해 queue에 dead letter 설정을 해주고, nack나 reject를 보내면 됩니다. 샘플 코드를 통해 dead letter 설정과 nack/reject 처리 방법을 확인할 수 있습니다.

## Full Document
[[Full Document Contents/[RabbitMQ] NackReject로 다른 큐로 보내기.md|See full document content →]]

## Highlights
- `nack`나 `reject`를 보낼 때 `requeue=false`로 설정하지 않으면, 이 메시지는 큐의 원래 위치로 돌아가게 된다. ([View Highlight](https://read.readwise.io/read/01hnvxgqef7gytqbkbang7gj1q))
- RabbitMQ에서 requeue는 가능한 메시지의 원래 위치에 넣게 된다. ([View Highlight](https://read.readwise.io/read/01hnvxh3fkhab6pyz7dm2ytahs))
