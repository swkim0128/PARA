# [PHP] 문자 인코딩 감지, 문자 Charset 확인 방법

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbrNz4d%2FbtrTMRC0SsP%2FjhSi04o8kia5djPg2RfYw0%2Fimg.png)

## Metadata
- Author: [[우월한하루]]
- Full Title: [PHP] 문자 인코딩 감지, 문자 Charset 확인 방법
- Category: #articles
- Document Tags:  #php 
- Summary: 문자 인코딩 감지 방법 $account_addr1 = mb_convert_encoding($account_addr1, "EUC-KR", "UTF-8"); $encodelist = array('ASCII','UTF-8','UTF-16LE','WINDOWS-1252','EUC-KR'); $test_en = mb_detect_encoding($account_addr1, $encodelist); echo""; exit(); 첫 번째 줄 mb_convert_encoding를 이용하여 인코딩을 "EUC-KR"로 변경함 mb_convert_encoding 사용법은 아래 링크로 들어가서 확인가능 https://jongs-story.tistory.com/3 [PHP] 특정 문자열만 인코딩 변환 시키는 방법 (base64..

## Full Document
[[Full Document Contents/[PHP] 문자 인코딩 감지, 문자 Charset 확인 방법.md|See full document content →]]

## Highlights
- mb_detect_encoding("감지하고 싶은 문자열", $encodelist); ([View Highlight](https://read.readwise.io/read/01hesgftfag6ch9rxw54nv4cy4))
    - Note: 인코딩 확인 함수
