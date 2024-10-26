# Systemd Service

![rw-book-cover](https://velog.velcdn.com/images/markyang92/post/0cdbd0e5-c0ec-4357-866e-92b799f47c4d/img60.png)

## Metadata
- Author: [[velog.io]]
- Full Title: Systemd Service
- Category: #articles
- Document Tags: [[linux]] 
- Summary: The text explains how to create and manage systemd services, using ssh.service as an example. It covers key sections like [Unit], [Service], and [Install], detailing their purposes and configurations. Additionally, it illustrates how to enable and start services while explaining dependencies and service types.
- URL: https://velog.io/@markyang92/systemd-timer

## Highlights
- 서비스 소속 **Target Unit**설정 및 **부팅 시** Unit이 *enable, disable* 을 위한 섹션 ([View Highlight](https://read.readwise.io/read/01j4gcebdpyf9jhph7pwq48swt))
    - Note: [install] 섹션 관련 설명
- WantedBy : Unit이 어떻게 활성화(enable)될 것인지에 대한 부분 ([View Highlight](https://read.readwise.io/read/01j4gch22mcz0hv1aesj6q0sed))
    - Note: Install 섹션, WantedBy 설정 설명
- **`$ sudo systemctl enable`** 명령어로 **Unit**을 **enable**할 때, **등록에 필요한 유닛**을 지정한다.
  • Dependency Check라 생각
  • **`/etc/systemd/system/지명.target.wants`**에 들어간다.
  • 부팅 시, 속한 .wants에 따라 실행되게한다. ([View Highlight](https://read.readwise.io/read/01j4gckjmndk7gf3s59wbmsf05))
    - Note: Install 섹션, WantedBy 설정 설명 2
- **실제 `ssh.service`의 위치**: `/usr/lib/systemd/system/ssh.service` ([View Highlight](https://read.readwise.io/read/01j4ggeady9zvzmm8jdqz0x8h8))
    - Note: multi-user.target으로 설정할 경우, 등록되는 위치
- 3-1. `/etc/systemd/system/multi-user.target.wants/`에 ssh.service 소프트링크 생성 
  3-2. `/etc/systemd/system/`에 `systemd`가 알아먹을 수 있게, `Alias=sshd.service`대로 
  sshd.service 가 생성되어, **sshd**라는 이름으로도 접근 할 수 있는 것임 ([View Highlight](https://read.readwise.io/read/01j4ggmy1ssw7712t7671t4snp))
    - Note: 실제 생성위치 : /usr/lib/systemd/system/
      소프트링크 생성위치 : /etc/systemd/system/multi-user.tartget.wants
      Alias 링크 생성위치 : /etc/systemd/system
- Alias
  • [Install]
  • Alias: Unit ***alias*** 이름 지정
  • **`$ sudo systemctl enable 'alias'`** 접근 가능
  • ***alias*** 이름은 Unit 파일 확장자를 가지고 있어야한다.
  • service, socket, mount, swap 등.
  • e.g.
  • 서비스 이름: **httpd.service**시, 
  Alias=`[Alias Name].service` ([View Highlight](https://read.readwise.io/read/01j4ggwm4d6k27d2tzecebm80d))
