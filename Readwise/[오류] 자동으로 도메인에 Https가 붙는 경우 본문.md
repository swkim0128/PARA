# [오류] 자동으로 도메인에 Https가 붙는 경우 본문

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[보통사람]]
- Full Title: [오류] 자동으로 도메인에 Https가 붙는 경우 본문
- Category: #articles
- Summary: 1. 오류 개발서버 https 적용으로 아래와 같이 http 요청 블락 에러가 발생하였다. This request has been blocked; the content must be served over HTTPS. 그래서 아래의 메타 태그를 추가해 줬다. 하지만 개발서버 https 적용을 해제하면서부터 화면 접속시 자동으로 https:// 로 붙어서 js, css를 읽는 경우가 발생하였다. 2. 원인 https때문에 추가했던 메타 태그의 문제로, content-security-policy를 설정할 경우 자동으로 https로 호출해 주는 것이었다. The HTTP Content-Security-Policy (CSP) upgrade-insecure-requests directive instructs use..

## Full Document
[[Full Document Contents/[오류] 자동으로 도메인에 Https가 붙는 경우 본문.md|See full document content →]]

## Highlights
- content-security-policy를 설정할 경우 자동으로 https로 호출해 주는 것 ([View Highlight](https://read.readwise.io/read/01hdg2bhhh8zss4d5rty20y0gg))
