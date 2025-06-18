# [GitHub] 아이디/패스워드 입력 없이 사용하는 방법

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdjN0H6%2Fbtsi9REjqCW%2FjjuygQES6aRsI4ahkfONTk%2Fimg.png)

## Metadata
- Author: [[쫄리_]]
- Full Title: [GitHub] 아이디/패스워드 입력 없이 사용하는 방법
- Category: #articles
- Document Tags:  #git 
- Summary: This text explains how to use Git without entering your GitHub credentials every time. It describes a risky method of embedding your login information in the repository URL and safer methods using Git's credential helper to cache or store credentials. The safest option is to use the OS's Keychain to manage your credentials securely.
- URL: https://creative103.tistory.com/86

## Full Document
[[Full Document Contents/[GitHub] 아이디패스워드 입력 없이 사용하는 방법.md|See full document content →]]

## Highlights
- **Git Credential / cache**
  만약 id와 password를 짧은 시간 동안 반복적으로 입력하는 일을 피하고 싶다면 credential.helper를 cache로 설정 ([View Highlight](https://read.readwise.io/read/01jvr8y8dg5gpr07bk1whzjr9y))
- git config --global credential.helper cache ([View Highlight](https://read.readwise.io/read/01jvr905t01ma4wnecb7qa7663))
    - Note: git credential / cache
- git config credential.helper 'cache --timeout=300' ([View Highlight](https://read.readwise.io/read/01jvr90phzz5dm00zkf23ne445))
    - Note: git credential / cache time
- **Git Credential / Keychain**
  **git config --global credential.helper wincred**
  credential.helper를 store로 지정했을 때의 문제는 파일에 로그인 정보가 그대로 저장된다는 점이다.
  이를 좀 더 안전하게 사용하려면 OS 자체에서 지원한는 Keychain 시스템을 이용하 ([View Highlight](https://read.readwise.io/read/01jvr8zqxjjwtxp09mb6z066wz))
    - Note: git credential / keychain
- # for windows git config --global credential.helper wincred ([View Highlight](https://read.readwise.io/read/01jvr92s810keyt9cpznqfqaf0))
    - Note: git credential / keychain for window
- # for Mac git config --global credential.helper osxkeychain ([View Highlight](https://read.readwise.io/read/01jvr92aghaff0c78qwvttf5qt))
    - Note: git credential / keychain for mac
