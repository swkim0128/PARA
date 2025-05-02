# [HTTP] User-Agent를 읽는 법

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[softserve]]
- Full Title: [HTTP] User-Agent를 읽는 법
- Category: #articles
- Summary: 웹 개발을 하다보면 접속 환경과 관련된 이슈가 종종 발생합니다. 그럴 때는 로그에 남아 있는 클라이언트의 정보를 유용하게 활용할 수 있습니다. 사용자의 접속 환경 정보는 요청 헤더 Request header 의 User-Agent, UA가 가지고 있습니다. UA는 클라이언트의 브라우저, 운영체제 종류에 따라 다른 웹 페이지를 보여주거나, 통계를 내는 등 다양한 용도로 활용할 수 있습니다. 브라우저를 열고 개발자 도구의 콘솔에서 navigator.userAgent 를 입력하면 다음과 같은 결과를 출력해 줍니다. Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.3..

## Full Document
[[Full Document Contents/[HTTP] User-Agent를 읽는 법.md|See full document content →]]

## Highlights
- Mozilla/5.0 (Windows NT 10.0; Win64; x64) ([View Highlight](https://read.readwise.io/read/01hdfqevjx6dcdneyq3wy83j0r))
    - Note: 브라우저 구분을 위해 나타내는 정보
      괄호 안에는 운영체제 정보가 들어가 있다.
- AppleWebKit/537.36 (KHTML, like Gecko) ([View Highlight](https://read.readwise.io/read/01hdfqghn7e3gmkxtdmm49sr1p))
    - Note: 렌더링 관련 정보, 브라우저의 핵심
- Chrome/111.0.0.0 Safari/537.36 ([View Highlight](https://read.readwise.io/read/01hdfqhc55pt9q6q24w4wvkwh7))
    - Note: 브라우저 정보, 앞에 있는 정보가 사용중인 브라우저이고, 뒤에 있는 브라우저는 호환되는 브라우저를 뜻한다.
