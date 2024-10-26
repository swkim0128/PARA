# M1, M2 Mac OS에서 Oracle DataBase 사용하기

![rw-book-cover](https://velog.velcdn.com/images/devsaza/post/09938226-8de2-4e5e-a67f-872803afa76d/image.png)

## Metadata
- Author: [[velog.io]]
- Full Title: M1, M2 Mac OS에서 Oracle DataBase 사용하기
- Category: #articles
- Document Tags: [[mac]] [[oracle]] 
- Summary: Oracle Database를 Mac에서 사용하기 위해 Docker를 통해 설치하는 방법에 대해 설명합니다. Colima와 Docker를 설치한 후, Colima를 x86_64 환경으로 실행합니다. 그런 다음, docker run 명령을 사용하여 Oracle 서버를 실행합니다. 성공적으로 실행되면 SQL plus를 실행하여 데이터베이스에 연결할 수 있습니다. 컨테이너를 종료하려면 docker stop 명령어를 사용하면 됩니다.
- URL: https://velog.io/@devsaza/M1-M2-Mac-OS%EC%97%90%EC%84%9C-Oracle-DB-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

## Highlights
- docker run \ --restart unless-stopped \ --name oracle2 \ -e ORACLE_PASSWORD=pass \ -p 1521:1521 \ -d \ gvenzl/oracle-xe ([View Highlight](https://read.readwise.io/read/01hmj8g0dkj8r54nvwq7hfghk7))
