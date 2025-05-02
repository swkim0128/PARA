# [PHP] Request가 HTTP인지 HTTPS인지 확인하는 방법 본문

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[devxpert.yoon]]
- Full Title: [PHP] Request가 HTTP인지 HTTPS인지 확인하는 방법 본문
- Category: #articles
- Document Tags:  #php 
- Summary: 서버 요청이 HTTP에서 이뤄지는지 HTTPS/SSL에서 이뤄지고 있는지 확인이 필요할 때가 있다.Global Vairable인 $_SERVER를 이용해 간단히 확인할 수 있다. function isHttpsRequest() {if ( (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') || $_SERVER['SERVER_PORT'] == 443) {return true; } return false; } HTTPS/SSL 요청은 아래 2가지 조건 중 하나라도 참인 경우로 판정한다. 1. $_SERVER['HTTPS'] 가 존재하면서, 그 값이 off가 아닌 경우 (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !=..

## Full Document
[[Full Document Contents/[PHP] Request가 HTTP인지 HTTPS인지 확인하는 방법 본문.md|See full document content →]]

## Highlights
- **1. $_SERVER['HTTPS'] 가 존재하면서, 그 값이 off가 아닌 경우**
  (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off')
  **2. $_SERVER['SERVER_PORT'] 가 443인 경우**
  $_SERVER['SERVER_PORT'] == 443 ([View Highlight](https://read.readwise.io/read/01hepb44hekde79f6z3mpdbbg2))
