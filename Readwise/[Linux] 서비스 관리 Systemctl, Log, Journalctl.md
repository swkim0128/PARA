# [Linux] 서비스 관리: Systemctl, Log, Journalctl

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[nayoungs]]
- Full Title: [Linux] 서비스 관리: Systemctl, Log, Journalctl
- Category: #articles
- Document Tags:  #linux 
- Summary: systemd is a daemon that replaces the init process and manages services in Linux. It collects logs through systemd-journald and rsyslog, which help track system events and issues. Users can view logs using commands like `systemctl` and `journalctl` for real-time monitoring and analysis.

## Full Document
[[Full Document Contents/[Linux] 서비스 관리 Systemctl, Log, Journalctl.md|See full document content →]]

## Highlights
- **🔹 unit 제어 서브 커맨드(sub-command)**
  • **sytemctl [sub-command] [unit]**
  • status : 상태확인
  • start : 시작
  • stop : 종료
  • restart : 재시작
  • **PID 변경됨**
  • 아예 프로세스를 껐다가 다시 키는 것
  • **변경된 설정을 시스템에 반영시킬 때마다 restart** 해줘야함
  • reload : 재설정
  • **main PID 변경 안됨**
  • enable : 활성화
  • 부팅할 때 시작
  • /etc/systemd/system/multi-user.target.wants/[유닛(unit)]에서 /user/lib/systemd/system/[유닛(unit)]로 **심볼릭 링크 연결**하는 것
  • 즉, **디렉토리(/etc/systemd/system)에서 원본 unit(/usr/lib/systemd)으로 연결**시킨다
  • 수동으로 심볼릭 링크 연결 시키는 것도 가능
  • ln -s 명령 사용
  • disable : 비활성화
  • 심볼릭 링크 없앰
  • start 명령을 통해 다시 실행 가능
  • mask : 마스크 설정
  • **/dev/null**에 심볼릭 링크 연결
  • start 명령으로도 실행 불가
  • unmask : 마스크 해제
  • list-dependencies : 종속성(의존성) 확인 ([View Highlight](https://read.readwise.io/read/01j4genafrqehh9dbtc580sedm))
