# HTTP와 HTTPS를 구분해서 이미지, CSS, Javascript 로딩하기

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[▒▒ 코딩하는 녀석 ▒▒]]
- Full Title: HTTP와 HTTPS를 구분해서 이미지, CSS, Javascript 로딩하기
- Category: #articles
- Document Tags: [[https]] 
- Summary: 다른 브라우저에서는 별 문제 없는데 IE에서는 스키마가 https 로 된 홈페이지에서 http로 이미지나 CSS, Javascript등의 리소스를 로딩하면 경고가 발생한다. 그래서 현재 주소에 따라 리소스의 주소를 적을때 https인지 http인지 잘 구분해서 적어줘야 한다. 사실 나는 별로 납득가지 않는데, 일반적으로 암호화 대상이 되는 데이터는 HTML에 거의 다 들어있고, 혹은 폼을 통해 전송하는 데이터에 들어있지 화면을 꾸미는 이미지, CSS, ... 등(이하 리소스 resource)에 들어있는게 아니기 때문이다. 따라서 경고를 안 내는게 맞는 것 같다. 아무튼 이런 상황에서 HTTPS인 페이지와 HTTP인 페이지별로 따로 모든 리소스의 경로를 구분해서 줘야 할까? 당연히 그럴필요 없어서 글 쓴다..
- URL: https://devman.tistory.com/entry/HTTP%EC%99%80-HTTPS%EB%A5%BC-%EA%B5%AC%EB%B6%84%ED%95%B4%EC%84%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-CSS-Javascript-%EB%A1%9C%EB%94%A9%ED%95%98%EA%B8%B0

## Highlights
- http: 혹은 https: 같은 스키마를 제외하고 //도메인주소/경로를 적는것이 스키마에 상대적인 주소 ([View Highlight](https://read.readwise.io/read/01hdg3yvjh8m1vg9hbxhbnev81))
- 조건: 브라우저기반 작동시에만 사용할 것. HTML 이메일에 이 방식을 사용하면 보장 못함! ([View Highlight](https://read.readwise.io/read/01hdg3zpfr49fra6s07kar7zsh))
