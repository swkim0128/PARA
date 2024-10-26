# Systemctl 작성 방법

![rw-book-cover](https://images.velog.io/velog.png)

## Metadata
- Author: [[velog.io]]
- Full Title: Systemctl 작성 방법
- Category: #articles
- Document Tags: [[linux]] 
- Summary: systemctl은 Linux에서 서비스와 시스템 상태를 관리하는 명령줄 도구입니다. 사용자는 systemctl을 통해 서비스를 시작, 중지, 재시작 및 활성화할 수 있으며, 서비스가 중단되면 자동으로 재실행됩니다. autoStart는 부팅 시 한 번만 실행되며, 지속적으로 실행해야 하는 서비스는 systemctl로 관리해야 합니다.
- URL: https://velog.io/@sk1440sk/systemctl-%EC%9E%91%EC%84%B1-%EB%B0%A9%EB%B2%95

## Highlights
- 네트워크를 먼저 설정하도록 한다는 뜻으로 인터넷이 연결된 후에 서비스를 실행하겠다는 ([View Highlight](https://read.readwise.io/read/01j463232v26ea6yanzkb6zkyn))
- 4. 서비스 활성화
  `sudo systemctl enable windows.service` ([View Highlight](https://read.readwise.io/read/01j4gf29pc4t00j8svtx5bsw39))
    - Note: systemctl service 활성화 명령어
