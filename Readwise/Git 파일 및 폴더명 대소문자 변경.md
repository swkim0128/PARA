# Git 파일 및 폴더명 대소문자 변경

![rw-book-cover](https://images.velog.io/velog.png)

## Metadata
- Author: [[velog.io]]
- Full Title: Git 파일 및 폴더명 대소문자 변경
- Category: #articles
- Summary: Git은 기본적으로 파일 및 폴더명의 대소문자를 구분하지 않는다. 그래서 cat이라는 파일을 Cat으로 변경해도, Git은 감지하지 못한다. 이를 해결하기 위한 방법이 두가지가 있다.

## Full Document
[[Full Document Contents/Git 파일 및 폴더명 대소문자 변경.md|See full document content →]]

## Highlights
- git config core.ignorecase false
  첫번째 방법은 설정 자체를 바꾸는 것이다. `git config core.ignorecase false`을 git config에 등록해주면, git은 대소문자를 구분할 수 있게 된다. ([View Highlight](https://read.readwise.io/read/01hf3rm8bjz05ynmt5wna4dqz0))
- git mv
  두번째 방법은 설정은 그대로 둔 채로 파일 혹은 폴더를 변경하는 방법이다. 
  `git mv`는 리눅스의 mv와 동일한 역할이다. 다만, 이동하려는 객체가 git에 tracked된 상태여야 한다는 차이가 있다. ([View Highlight](https://read.readwise.io/read/01hf3rmhxz4537n7j0an4vwneb))
