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
#### **배경**

git을 사용하다보면 github, bitbucket 등의 remote repository를 사용하게 된다.

이 때 remote repo의 주소가 ssl로 되어 있다면 상관 없지만,

https로 되어 있는 경우에는 clone, push, pull 등 동작마다 remote repo에 접근하기 위한 로그인 정보를 입력해 주어야 한다.

관리해야할 repo가 많거나, 어플리케이션을 통해 컨트롤 해야 하는 경우에 이러한 과정을 생략하고 싶을 때가 있다.

#### **방법 1. 쉽지만 위험한 방법**

이런 경우 remote repo 주소 자체에 접속 정보를 직접 넣어줄 수 있다.

아래와 같이 하면 별도로 접속 정보를 입력하지 않아도 된다.

```
git clone https://<ID>:<PASSWORD>@myrepo.github.com/coolproject.git

```

이 방법을 사용하면 password가 그대로 노출되게 되므로 위험할 수 있다.

만약 그래도 사용해야 한다면 [personal access token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)을 생성하여 <PASSWORD> 대신 사용하자.

#### **방법 2. 안전하고 공식적인 방법**

git에서는 이런 문제를 도와주기 위해 credential이라는 기능을 제공하고 있다.

이 기능을 사용하면 로그인 정보를 저장해 두었다가 다시 입력하지 않아도 사용할 수 있게 해 준다.

크게 cache와 store 두 가지 방법이 있다.

##### **Git Credential / cache**

만약 id와 password를 짧은 시간 동안 반복적으로 입력하는 일을 피하고 싶다면 credential.helper를 cache로 설정할 수 있다. ( ☞[git-credential-cache](https://git-scm.com/docs/git-credential-cache) )

```
# git config 업데이트
git config --global credential.helper cache
# git config --global --list
# ☞ credential.helper=cache

```

이렇게 하면 ID와 PASSWORD 같은 인증정보를 Disk에 저장하지는 않고 메모리에서 15분 까지만 유지한다.

한 번 입력된 인증 정보는 15분 동안 다시 묻지 않는다.

시간을 연장하려면 다음과 같이 옵션을 준다.

```
git config credential.helper 'cache --timeout=300'
```

##### **Git Credential / store**

사용자이름과 암호 같은 인증정보를 Disk에 저장하고 계속 유지하고 싶을 때도 있다.

이 때는 credential.helper를 store로 지정한다.

아래와 같이 옵션을 수정해 주면 한 번 로그인 된 정보는 자동으로 저장되어 다음부터 묻지 않는다.

로그인 정보는 ~/.git-credentials에 저장되게 된다.

```
# git config 업데이트
git config --global credential.helper store
# git config --global --list
# ☞ credential.helper=store
```

##### **Git Credential / Keychain**

**git config --global credential.helper wincred**

credential.helper를 store로 지정했을 때의 문제는 파일에 로그인 정보가 그대로 저장된다는 점이다.

이를 좀 더 안전하게 사용하려면 OS 자체에서 지원한는 Keychain 시스템을 이용하면 된다.

mac이나 windows에는 OS 자체에서 제공하는 Keychain 시스템이 있다.

git credential 정보를 이곳에 저장할 수 있다.

```
# for windows
git config --global credential.helper wincred
# git config --global --list
# ☞ credential.helper=wincred

```

※ 이 정보는 windows의 [“자격 증명 관리자(Credential Manager)”](https://support.microsoft.com/ko-kr/help/4026814/windows-accessing-credential-manager)에서 확인할 수 있다.

만약 remote repo의 비밀번호를 수정하였다면 이 “자격 증명 관리자”에서 해당 정보를 삭제해 주어야 한다.

```
# for Mac
git config --global credential.helper osxkeychain
```

##### **설정 상태 확인**

현재 설정 상태를 확인해고 싶다면 아래와 같이 할 수 있다.

```
# local 설정
git config  --list
# Global 설정
git config --global --list
```

![](https://blog.kakaocdn.net/dn/bvKtbX/btsmGBx1ooj/mrFRU1JS1jzs0kSHEVLFO0/img.png)
![](https://blog.kakaocdn.net/dn/djN0H6/btsi9REjqCW/jjuygQES6aRsI4ahkfONTk/img.png)
###### '[📌 GitHub](https://creative103.tistory.com/category/%F0%9F%93%8C%20GitHub)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [[GitHub] 깃배쉬(Git Bash)로 깃허브에 코드 올리기 & 코드 업데이트하기 (깃허브 잔디심기)](https://creative103.tistory.com/113) (0) | 2024.05.13 |
| [[GitHub] 깃허브(Github) 프로필 꾸미기 (Readme.md)](https://creative103.tistory.com/93) (0) | 2023.07.19 |
| [[GitHub] Access token 만들어 적용하기](https://creative103.tistory.com/84) (0) | 2023.06.08 |
| [[GitHub] 레포지를 간편하게 VS Code 스타일로 보는 방법 (깃허브 .)](https://creative103.tistory.com/72) (0) | 2023.04.23 |
