# [Git] SVN을 Git으로 Migration 하기

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fd0oJQs%2FbtrficeZsyf%2F8XnoeNTcsRTOaTXuK6HDwK%2Fimg.png)

## Metadata
- Author: [[오이가지아빠]]
- Full Title: [Git] SVN을 Git으로 Migration 하기
- Category: #articles
- Document Tags:  #git  #svn 
- Summary: #1. 사용자 정보 취합하기 SVN 소스를 git으로 전환하기 위해서는 일단 사용자 정보를 정리해야 합니다. 그냥 전환했다가는 커밋히스토리에 저장된 사용자 정보가 이상하게 보여지게 됩니다. 따라서 일단 전환하려는 SVN 에 커밋했던 사용자들의 정보를 git으로 매핑해주는 작업이 필요합니다. 적당한 곳에 폴더를 만들고 users.txt 파일에 다음과 같은 내용을 작성합니다. user1 = user1 user2 = user2 user3 = user3 . . . user10 = user10 왼쪽은 SVN id, 오른쪽은 그 사용자의 git id, email 정보입니다. 위처럼 저장한 파일을 생성하는 것이 1단계입니다. 이 단계에서 사용자가 누락되면 mig도중에 알려주긴 합니다만, 처음부터 다시 해야해서 귀찮으..

## Full Document
[[Full Document Contents/[Git] SVN을 Git으로 Migration 하기.md|See full document content →]]

## Highlights
- 적당한 곳에 폴더를 만들고 users.txt 파일에 다음과 같은 내용을 작성합니다. ([View Highlight](https://read.readwise.io/read/01hatxg3egm67b1f2d9eae1akh))
    - Note: svn 사용자 정보 작성
- 왼쪽은 SVN id, 오른쪽은 그 사용자의 git id, email 정보입니다. ([View Highlight](https://read.readwise.io/read/01hatxh5kg7qmkbnr70j2j5e98))
    - Note: svn 사용자 정보 작성
- git svn clone http://svnhost:port/저장소주소 --authors-file=users.txt --no-metadata ([View Highlight](https://read.readwise.io/read/01hatxhg1f9wd3sq34ptdr2ywn))
    - Note: svn -> git
