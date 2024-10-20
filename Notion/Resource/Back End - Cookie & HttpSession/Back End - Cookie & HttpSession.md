---
type: Spring
archive: false
---
## Session & Cookie

---

http protocol의 특징

client가 server에 요청.

server는 요청에 대한 처리를 한 후 clinet에 응답.

응답 후 연결을 해제 >> stateless

- 지속적인 연결로 인한 자원 낭비를 줄이기 위해 연결을 해제한다.
- 그러나 clinet와 server가 연결 상태를 유지해야 하는 경우가 문제가 발생(로그인정보등)
- 즉 client 단위로 상세 정보를 유지해야 하는 경우 Cookie와 Session이 사용된다.

HTTP protocol의 특징(약점)을 보완하기 위해 사용

  

### Cookie

---

Cookie? : javax.servlet.http.Cookie

- 서버에서 사용자의 컴퓨터에 저장하는 정보파일.
- 사용자가 별도의 요청을하지 않아도 브라우저는 request시 request Header를 넣어 자동으로 서버에 전송
- key와 value로 구성되고 String 형태로 이루어져 있음.
- Browser마다 저장되는 쿠키는 다르다(서버에서는 Browser가 다르면 다른 사용자로 인식)

  

Cookie의 사용 목적

- 세션 관리 : 사용자 아이디, 접속시간, 장바구니 등의 서버가 알아야 할 정보 저장.
- 개인화 : 사용자마다 다르게 그 사람에 적절한 페이지를 보여줄 수 있다.
- 트래킹 : 사용자의 행동과 패턴을 분석하고 기록

  

Cookie의 사용 예.

- id 저장(자동 로그인).
- 일주일간 다시 보지 않기.
- 최근 검색한 상품들을 광고에 추천.
- 쇼핑몰 장바구니 기능.

  

Cookie의 구성요소.

- 이름 : 여러 개의 쿠키가 client의 컴퓨터에 저장되므로 각 쿠키를 구별하는데 사용되는 이름
- 값 : 크키의 이름과 매핑되는 값
- 유효기간 : 쿠키의 유효기간
- 도메인 : 쿠키를 전송할 도메인
- 경로(path) : 쿠키를 전송할 요청 경로

  

Cookie의 동작 순서

- Client가 페이지를 요청.
- WAS는 Cookie를 생성
- HTTP Header에 Cookie를 넣어 응답
- Browser는 넘겨받은 Cookie를 PC에 저장하고, 다시 WAS가 요청할 때 요청과 함께 Cookie를 전송
- Browser가 종료되어도 Cookie의 만료 기간이 남아 있다면 Client는 계속 보관
- 동일 사이트 재방문시 Client의 PC에 해당 Cookie가 있는 경우, 요청 페이지와 함께 Cookie를 전송.

  

Cookie의 특징

- 이름, 값, 만료일(저장 기간 설정), 경로 정보로 구성되어 있다.
- 클라이언트에 총 300개의 쿠키를 저장할 수 있다.
- 하나의 도메인 당 20개의 쿠키를 가질 수 있다.
- 하나의 쿠키는 4KB까지 저장 가능하다.

  

Cookie의 설정.

- name이 userid인 Cookie의 값은 ssafy이고, 유효기간은 2020년 10월 15일이다.
- 유효도메인 및 경로는 [ssafy.com](http://ssafy.com) Domain의 /user Path가 된다.

![[Untitled 59.png|Untitled 59.png]]

  

Cookie의 주요 기능

![[Untitled 1 36.png|Untitled 1 36.png]]

  

### Session

---

session? : javax.servlet.http.HttpSession

- 방문자가 웹 서버에 접속해 있는 상태를 하나의 단위로 보고 그것을 세션이라 한다.
- WAS의 memory에 Object의 형태로 저장.
- memory가 허용하는 용량까지 제한 없이 저장 가능.

  

session의 사용 예

- site내에서 화면을 이동해도 로그이(사용자 정보)이 풀리지 않고 유지
- 장바구니

  

session의 동작 순서

- 클라이언트가 페이지를 요청.
- 서버는 접근한 클라이언트의 Request-Header 필드인 Cookie를 확인하여, 클라리언트가 해당 session-id를 보냈는지 확인.
- session-id가 존재하지 않는다면, 서버는 session-id를 생성해 클라이언트에게 돌려준다.
- 서버에서 클라이언트로 돌려준 session-id를 쿠키를 사용해 서버에 저장. 쿠키 이름 : JSESSIONID
- 클라이언트는 재 접속 시, 이 쿠키(JSESSIONID)를 이용하여 session-id 값을 서버에 전달.

  

session의 특징.

- 웹 서버에 웹 컨테이너의 상태를 유지하기 위한 정보를 저장.
- 웹 서버에 저장되는 쿠키(=세션 쿠키)
- 브라우저를 닫거나, 서버에서 세션을 삭제 했을 때만 삭제가 되므로, 쿠키보다 비교적 보안이 좋다.
- 저장 데이터에 제한이 없다.
- 각 클라이언트 고유 Session ID를 부여한다.
- Session ID로 클라이언트를 구분하여 각 클라이언트 요구에 맞는 서비스 제공.

  

session의 설정

- Browser당 하나의 JSESSIONID를 할당 받음.
- 아이디 또는 닉네임과 같이 로그인 했을 경우 자주 사용되는 정보를 session에 저장하면 DB를 접근할 필요가 없으므로 효율적이다.

![[Untitled 2 35.png|Untitled 2 35.png]]

  

HttpSession의 주요 기능

![[Untitled 3 34.png|Untitled 3 34.png]]

  

### Session & Cookie 정리

---

![[Untitled 4 30.png|Untitled 4 30.png]]