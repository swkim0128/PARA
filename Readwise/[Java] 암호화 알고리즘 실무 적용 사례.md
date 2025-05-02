# [Java] 암호화 알고리즘 실무 적용 사례

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F1yu25%2Fbtsp8YWVraX%2Fb0T2kbDWjY6UFM3Osz70ek%2Fimg.png)

## Metadata
- Author: [[개발자 Aiden]]
- Full Title: [Java] 암호화 알고리즘 실무 적용 사례
- Category: #articles
- Summary: 현대 IT 환경에서 데이터 보안은 중요한 문제입니다. 데이터 암호화는 개인 정보 유출로부터 보호하기 위한 핵심 대책입니다. 암호화 알고리즘은 데이터의 특성과 보안 요구에 따라 선택되며, 단방향 암호화와 양방향 암호화로 나눌 수 있습니다. 단방향 암호화는 데이터의 무결성을 보장하고, 양방향 암호화는 데이터의 비밀성을 유지합니다. 대표적인 암호화 알고리즘으로는 SHA, AES, RSA가 있습니다. 암호화를 적용할 때는 최신 보안 표준과 권장 사항을 준수하는 것이 중요합니다.

## Full Document
[[Full Document Contents/[Java] 암호화 알고리즘 실무 적용 사례.md|See full document content →]]

## Highlights
- **1. 단방향 암호화: 복호화 불가능**
  **데이터의 무결성 보장 
  **비밀번호와 같은 민감한 정보는 한 번 암호화되면 원래의 형태로 돌아갈 수 없어야 합니다. 이렇게 되면, 해커가 암호화된 데이터를 입수하더라도 원본 데이터를 알아내기 어렵습니다. ([View Highlight](https://read.readwise.io/read/01hmwew7vacppk91sy5jm7kb8m))
    - Note: * 해시 함수
      * 해시 함수 대표 알고리즘 : SHA, MD5
      * 메시지 인증코드(MAC)
- **2. 양방향 암호화: 복호화 가능**
  **데이터의 비밀성 유지** 
  데이터를 안전하게 전송하고, 필요할 때 원본 데이터로 복호화할 수 있어야 합니다. 이는 온라인 쇼핑몰에서 결제 정보를 안전하게 처리하는 경우 등에서 중요합니다. ([View Highlight](https://read.readwise.io/read/01hmwezpk5s1vtfmdh1vyj1h2e))
    - Note: * 대칭키 암호화 방식
      * 대칭키 대표 알고리즘 : AES, SEED
      * 비대칭키(공개키) 암호화 방식
      * 비대칭키 대표 알고리즘 : RSA
- **○ 대칭키 암호화 방식**
  • 대칭키 암호화는 하나의 키로 암호화와 복호화를 모두 수행합니다. 이 방식은 비대칭키 암호화 방식에 비해 속도가 빠르기 때문에 대량의 데이터를 실시간으로 암호화해야 하는 상황에서 유리합니다.
  • 빠른 암호화 속도가 필요한 스트리밍 서비스, 대용량 파일 전송 등에서 사용됩니다.
  • 대표 알고리즘 : AES, SEED ([View Highlight](https://read.readwise.io/read/01hmwf288p96sg426zjcnanrye))
- **○ 비대칭키(공개키) 암호화 방식**
  • 비대칭키 암호화는 암호화와 복호화에 각각 다른 키를 사용합니다. 이로 인해 키의 분실이나 탈취에 대한 위험이 크게 줄어들며 보안성이 높아집니다. 하지만 암호화 및 복호화 과정이 복잡하므로 속도는 대칭키 방식보다 느립니다.
  • SSL/TLS 인증서에서 웹사이트의 신뢰성을 보장하기 위해 사용됩니다. 또한 디지털 서명 및 인증서 발급 과정에서도 활용됩니다.
  • 대표 알고리즘 : RSA ([View Highlight](https://read.readwise.io/read/01hmwf2hfcrze6kjnhjedsag76))
