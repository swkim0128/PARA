---
type: Server
archive: false
---
## WebRTC

---

WebRTC(Web Real-Time Communication)는 웹 어플리케이션과 사이트가 중간자 없이 브라우저 간 오디오나 영상 미디어를 포착하고, 자유로운 스트림과 더불어 임의의 데이터 교환 기능도 제공.

주로 화상 컨퍼런스, 파일 공유, 화면 공유, 방송 등에 쓰입니다.

  

[WebRTC API] [https://developer.mozilla.org/ko/docs/Web/APIWebRTC_API](https://developer.mozilla.org/ko/docs/Web/APIWebRTC_API)

[WebRTC 실시간 데이터 교환] [https://wormwlrm.github.io/2021/01/24/Introducing-WebRTC.html](https://wormwlrm.github.io/2021/01/24/Introducing-WebRTC.html)

[WebRTC STUN, TURN 서버] [https://andonekwon.tistory.com/59](https://andonekwon.tistory.com/59)

  

## STUN/TURN

---

일반적으로 우리가 사용하는 인터넷 네트워크에는 방화벽이 존재하며, NAT(Network Address Translation)를 사용하여 서로 다른 네트워크 상의 서버, 호스트 등이 일부 내부 네트워크를 통해 서로 매핑하여 통신하는 방식을 이용하고 있다.

WebRTC는 시그널링(Signaling)이라는 통신 절차를 통해 P2P(Peer to Peer)로 통신하며, 이 때 방화벽 뒤에 숨은 네트워크에 속한 클라이언트 Private IP 간의 P2P 통신은 불가한 경우가 발생합니다. 바로 이 때 STUN 또는 TURN 서버가 필요합니다.

  

### STUN(Session Traversal Utilities for NAT)

---

STUN 서버는 UDP 프로토콜 기반으로 동작하며, 클라이언트의 Public IP를 확인하여 시그널링 수행할 수 있도록 합니다. Signaling Server 또는 Kurento 미디어 서버가 될 것입니다.

  

### TURN(Traversal Using Relays around NAT)

---

TURN 서버는 클라이언트들이 서로 통신할 때 Public 망에 존재하는 TURN 서버를 경유하도록하여 미디어 스트리밍을 릴레이하도록 Peer 와 Peer가 통신할 수 있도록 해줍니다. TURN은 STUN의 확장 개념이며, 클라이언트가 서로 다른 NAT 또는 방화벽 뒤에 일을 때, NAT 또는 방화벽을 쉰회하며 클라이언트가 중개 서버를 통해 데이터를 주고 받을 수 있도록 합니다.

  

## Kurento 미디어 서버

---

Kurento 미디어 서버는 오픈 소스 프로젝트로 WebRTC의 사양이 모두 구현된 WebRTC 미디어 서버와 클라이언트 API를 제공하는 패키지이며, WebRTC 화상 어플리케이션의 기능 개발을 지원합니다.