# Git 한글 파일명 깨짐 해결

![rw-book-cover](https://velog.velcdn.com/images/im-yeobi/post/0c64f15f-ab26-4a92-86c5-f5c3043b4517/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-11-02%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%203.35.50.png)

## Metadata
- Author: [[velog.io]]
- Full Title: Git 한글 파일명 깨짐 해결
- Category: #articles
- Document Tags:  #git 
- Summary: VSCode 코드에서 터미널을 이용해 git 명령을 쳤는데 다음과 같이 파일명의 한글이 깨지는 현상이 발생했다.

찾아봤더니 git의 core.quotePath 옵션이 기본적으로 true로 설정되어 있어서 파일 이름을 출력할 때 ""(double quotation)으로

## Full Document
[[Full Document Contents/Git 한글 파일명 깨짐 해결.md|See full document content →]]

## Highlights
- [git의 core.quotePath 옵션](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corequotePath)이 기본적으로 true로 설정되어 있어서 파일 이름을 출력할 때 `""(double quotation)`으로 감싸고 C언어에서 `\(escape character)` 문자가 동작하는 것과 동일하게 보여지는 것이라고 한다. ([View Highlight](https://read.readwise.io/read/01hc1ywqy5f7thahg0827s1g2p))
- git config core.quotepath false ([View Highlight](https://read.readwise.io/read/01hc1yx5df01f1869n44fyb7f1))
