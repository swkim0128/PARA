# Https를 위한 SSL/TLS 핸드 셰이크 작동원리

![rw-book-cover](https://img1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/JqQ/image/DnsDAsjRc5UTdYGy-DROkYekDvw.png)

## Metadata
- Author: [[테크유람]]
- Full Title: Https를 위한 SSL/TLS 핸드 셰이크 작동원리
- Category: #articles
- Summary: HTTPS를 위한 SSL/TLS 핸드 셰이크 작동원리는 인터넷에서 안전한 통신을 위해 사용되는 HTTPS의 기술적인 원리를 설명하는 문서입니다. HTTPS는 SSL/TLS 전송 기술을 사용하여 통신을 암호화하는 방식이며, SSL/TLS 인증서를 사용하여 안전한 통신을 보장합니다. SSL/TLS 인증서에는 대칭키 암호화 방식과 공개키 암호화 방식이 사용되며, 핸드 셰이크 과정을 통해 브라우저와 웹 서버가 신분을 확인하고 통신을 시작합니다. 이를 통해 HTTPS는 인터넷 상에서 안전한 통신을 제공합니다.
- URL: https://brunch.co.kr/@sangjinkang/38

## Highlights
- **SSL 인증서와 SSL handshake에 탑재된 기술**
  SSL 인증서 관련 프로세스에는 아래와 같은 보안 기술이 탑재되어 있습니다.
  하나의 키(key)로 암호화/복호화를 수행하는 대칭키 암호화 방식
  한 쌍의 키 페어(key pair)로 암호화/복호화를 수행하는 비대칭키 암호화 방식
  통신 대상을 서로가 확인하는 신분 확인(authentication)
  믿을 수 있는 SSL 인증서를 위한 디지털 서명(digital signature)
  디지털 서명을 해주는 인증 기관(CA: Certificate Authority)
  공개키를 안전하게 전달하고 공유하기 위한 프로토콜
  암호화된 메시지의 변조 여부를 확인하는 메시지 무결성 알고리즘 ([View Highlight](https://read.readwise.io/read/01hmx8m1ge1m9wkp2mnchv1qaq))
- **대칭키 암호화 방식**
  대칭키 암호화 방식(symmetric-key algorithm)이란, 하나의 키(key)로 평문을 암호화하고, 다시 암호문을 원해의 평문으로 복호화할 때 사용하는 방식 ([View Highlight](https://read.readwise.io/read/01hmx8kvj3nvnrsgdah0n39znv))
- **공개키 암호화 방식(= 비대칭키 암호화 방식)** 
  공개키 암호화 방식(Public Key Cryptography)은 공개키, 개인키 이렇게 두 개의 키를 한 쌍(key pair)으로 각각 암호화/복호화에 사용 ([View Highlight](https://read.readwise.io/read/01hmx8m708cahq0a4596m1tyfp))
