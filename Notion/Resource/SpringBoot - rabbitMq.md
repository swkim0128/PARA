---
type: Spring
archive: false
---
## SpringBoot RabbitMQ Properties List

|   |   |   |
|---|---|---|
|Property명|설명|기본값|
|`spring.rabbitmq.host`|RabbitMQ 서버 호스트|`localhost`|
|`spring.rabbitmq.port`|RabbitMQ 서버 포트|`5672`|
|`spring.rabbitmq.username`|브로커 인증에 사용되는 로그인 사용자||
|`spring.rabbitmq.password`|브로커 인증에 사용되는 로그인 암호||
|`spring.rabbitmq.virtual-host`|브로커에 연결할 가상 호스트|`/`|
|`spring.rabbitmq.dynamic`|`AmqpAdmin` 빈을 자동으로 생성할지 여부|`true`|
|`spring.rabbitmq.connection-timeout`|연결 시간 초과 시간|`60000` (1분)|
|`spring.rabbitmq.cache.channel.size`|캐시에 보존할 채널 수||
|`spring.rabbitmq.cache.connection.mode`|연결 팩토리 캐시 모드|`CHANNEL`|
|`spring.rabbitmq.cache.connection.size`|캐시할 연결 수|`1`|
|`spring.rabbitmq.cache.channel.checkout-timeout`|캐시에서 채널을 얻기 위한 대기 시간||
|`spring.rabbitmq.template.mandatory`|필수 메시지를 사용할지 여부||
|`spring.rabbitmq.template.receive-timeout`|메시지 수신 시간 초과 시간|`0` (무한대)|
|`spring.rabbitmq.template.reply-timeout`|`RabbitTemplate\#sendAndReceive`를 사용할 때 응답 대기 시간 초과 시간|`5000`|
|`spring.rabbitmq.template.retry.enabled`|재시도가 활성화되었는지 여부|`false`|
|`spring.rabbitmq.template.retry.max-attempts`|메시지를 게시하는 최대 시도 횟수||
|`spring.rabbitmq.template.retry.initial-interval`|첫 번째 재시도 전 대기 시간||
|`spring.rabbitmq.template.retry.multiplier`|재시도마다 대기 시간을 곱하는 값||
|`spring.rabbitmq.template.retry.max-interval`|재시도 간 최대 대기 시간||
|`spring.rabbitmq.template.retry.stateless`|상태 없는 재시도 사용 여부|`false`|
|`spring.rabbitmq.template.routing-key`|기본 라우팅 키||
|`spring.rabbitmq.template.exchange`|기본 교환||
|`spring.rabbitmq.template.default-retryable`|기본적으로 메시지를 재시도할 수 있는지 여부|`false`|
|`spring.rabbitmq.listener.simple.auto-startup`|컨테이너를 자동으로 시작할지 여부|`true`|
|`spring.rabbitmq.listener.simple.acknowledge-mode`|컨테이너의 Acknowledge 모드|`AUTO`|
|`spring.rabbitmq.listener.simple.concurrency`|시작할 동시 소비자 수||
|`spring.rabbitmq.listener.simple.max-concurrency`|최대 동시 소비자 수||
|`spring.rabbitmq.listener.simple.prefetch`|사전 가져올 메시지 수||
|`spring.rabbitmq.listener.simple.transaction-size`|트랜잭션에서 처리할 메시지 수||
|`spring.rabbitmq.listener.simple.default-requeue-rejected`|거부된 전송을 다시 큐에 추가할지 여부|`true`|
|`spring.rabbitmq.listener.simple.default-delivery-mode`|기본 전달 모드|`PERSISTENT`|
|`spring.rabbitmq.listener.simple.retry.enabled`|재시도가 활성화되었는지 여부|`false`|
|`spring.rabbitmq.listener.simple.retry.max-attempts`|메시지를 게시하는 최대 시도 횟수||
|`spring.rabbitmq.listener.simple.retry.initial-interval`|첫 번째 재시도 전 대기 시간||
|`spring.rabbitmq.listener.simple.retry.multiplier`|재시도마다 대기 시간을 곱하는 값||
|`spring.rabbitmq.listener.simple.retry.max-interval`|재시도 간 최대 대기 시간||
|`spring.rabbitmq.listener.simple.retry.stateless`|상태 없는 재시도 사용 여부|`false`|
|`spring.rabbitmq.listener.simple.default-retryable`|기본적으로 메시지를 재시도할 수 있는지 여부|`false`|
|`spring.rabbitmq.listener.simple.missing-queues-fatal`|누락된 큐가 치명적인지 여부|`true`|
|`spring.rabbitmq.listener.simple.auto-declare`|요소(큐, 교환, 바인딩)가 누락되었을 때 자동으로 선언할지 여부|`true`|
|`spring.rabbitmq.listener.simple.idle-event-interval`|컨테이너 이벤트 간 시간 간격||
|`spring.rabbitmq.listener.simple.retry-template`|전달 재시도에 사용할 `RetryTemplate` 빈에 대한 참조||
|`spring.rabbitmq.listener.simple.recovery-interval`|복구 시도 간 시간 간격||
|`spring.rabbitmq.listener.direct.acknowledge-mode`|컨테이너의 Acknowledge 모드|`AUTO`|
|`spring.rabbitmq.listener.direct.auto-startup`|컨테이너를 자동으로 시작할지 여부|`true`|
|`spring.rabbitmq.listener.direct.prefetch`|사전 가져올 메시지 수||
|`spring.rabbitmq.listener.direct.default-requeue-rejected`|거부된 전송을 다시 큐에 추가할지 여부|`true`|
|`spring.rabbitmq.listener.direct.consumers-per-queue`|각 큐에 대한 소비자 수||
|`spring.rabbitmq.listener.direct.expose-listener-channel`|리스너 채널을 노출할지 여부||
|`spring.rabbitmq.listener.direct.default-retryable`|기본적으로 메시지를 재시도할 수 있는지 여부|`false`|
|`spring.rabbitmq.listener.direct.missing-queues-fatal`|누락된 큐가 치명적인지 여부|`true`|
|`spring.rabbitmq.listener.direct.auto-declare`|요소(큐, 교환, 바인딩)가 누락되었을 때 자동으로 선언할지 여부|`true`|
|`spring.rabbitmq.listener.direct.idle-event-interval`|컨테이너 이벤트 간 시간 간격||
|`spring.rabbitmq.listener.direct.retry-template`|전달 재시도에 사용할 RetryTemplate 빈에 대한 참조||
|`spring.rabbitmq.listener.direct.recovery-interval`|복구 시도 간 시간 간격||
|`spring.rabbitmq.listener.direct.retry.enabled`|재시도가 활성화되었는지 여부|`false`|
|`spring.rabbitmq.listener.direct.retry.max-attempts`|메시지를 게시하는 최대 시도 횟수||
|`spring.rabbitmq.listener.direct.retry.initial-interval`|첫 번째 재시도 전 대기 시간||
|`spring.rabbitmq.listener.direct.retry.multiplier`|재시도마다 대기 시간을 곱하는 값||
|`spring.rabbitmq.listener.direct.retry.max-interval`|재시도 간 최대 대기 시간||
|`spring.rabbitmq.listener.direct.retry.stateless`|상태 없는 재시도 사용 여부|`false`|
|`spring.rabbitmq.ssl.algorithm`|사용할 SSL 알고리즘||
|`spring.rabbitmq.ssl.enabled`|SSL 지원 사용 여부|`false`|
|`spring.rabbitmq.ssl.enabled-protocols`|사용 가능한 SSL 프로토콜||
|`spring.rabbitmq.ssl.key-store`|SSL 인증서를 보유한 키 스토어 경로||
|`spring.rabbitmq.ssl.key-store-type`|키 스토어 유형||
|`spring.rabbitmq.ssl.key-store-password`|키 스토어에 액세스할 때 사용되는 암호||
|`spring.rabbitmq.ssl.key-store-provider`|키 스토어 공급자||
|`spring.rabbitmq.ssl.trust-store`|SSL 인증서를 보유한 트러스트 스토어||
|`spring.rabbitmq.ssl.trust-store-type`|트러스트 스토어 유형||
|`spring.rabbitmq.ssl.trust-store-password`|트러스트 스토어에 액세스할 때 사용되는 암호||
|`spring.rabbitmq.ssl.trust-store-provider`|트러스트 스토어 공급자||
|`spring.rabbitmq.ssl.verify-hostname`|호스트 이름 확인을 활성화할지 여부|`true`|