---
type: Linux
archive: false
---
## 정규 표현식과 검색도구

### 정규 표현식

정규 표현식이란?

정규 표현식은 다른 문자열을 검색하거나 치환할 목적으로 고안된 특수한 문자열  
grep, sed, awk 등 가장 강력한 유닉스 명령행 도구 중 일부는 정규 표현식을 사용함.  
  
[regexr.com](https://regexr.com/) # 정규 표현식 테스트 사이트

|기호|내용|기호2|내용2|
|---|---|---|---|
|[[abc]]|a, b 또는 c의 단일 문자|[^abc]|a, b 또는 c를 제외 모든 문자|
|[[a-z]]|범위의 모든 단일 문자 az|[a-zA-Z]|az 또는 AZ 범위 모든 문자|
|[[Resource/Linux Shell Script - 정규 표현식과 검색도구/Untitled/\|]]|라인의 시작|$|줄의 끝|
|[[Resource/Linux Shell Script - 정규 표현식과 검색도구/\|]]|모든 단일 문자|\s|공백 문자|
|[[S]]|비공백 문자|\d|임의의 숫자|
|[[D]]|임의의 비 숫자|\w|모든 단어 문자(문자, 숫자, 밑줄)|
|[[W]]|비 단어 문자|\b|모든 단어 경계|
|[[(...)]]|동봉 된 모든 것을 캡처하십시오|(a\|b)|
|[[a]]|0 또는 하나의|a*|0개 이상의|
|[[a+]]|하나 이상의|a{3}|정확히 3|
|[[a{3,}]]|3개 이상의|a{3,6}|3 ~ 6개 사이|

  
  

  

**명령어(grep)**

  

**명령어(sed)**

  

**중괄호 확장**

```Bash
$ touch noname{1, 2, 3, 4, 5, 6, 7, 8, 9}
$ ls 
noname1 noname3 noname5 noname7 noname9
noname2 noname4 noname6 noname8 shell_cmd
$ mkdir dir{1..9}
$ ls
dir1 dir4 ...
$ mkdir -p newproject/{lib,doc/{dpf,ppt,doc},src,include/sys,bin}
$ tree newproject/
newproject/
|..

$ length=40
$ eval printf -v line '%.0s-' {1..$length}  
# eval을 사용하면 입력 라인이 
# 두 번 구문 분석됩니다. 코드를 동적으로 평가하는 데 사용됩니다. 
# 중괄호 확장안에서는 `변수 확장`이 일어나지 못한다.
$ cp president.txt{,.bak}
$ ls president.txt*
president.txt president.txt.bak
```

  

**명령 대체**

```Bash
$ LANG=C; date
Wed Aug...
$ LANG=C; echo "today is $(date)"
today is Wed Aug...
$ LANG=C; echo "today is `date`"
today is Wed Aug...

$ export DIR1="$( cd dir1 || { mkdir dir1 && cd dir1;}; pwd )"
-bash: cd: dir1: No such file or directory
$ echo $DIR1
.../dir1
```

  

**로그인쉘과 비 로그인쉘**

텍스트 콘솔이나 SSH 또는 su -를 사용하여 로그인하면 대화형 로그인 쉘이 생깁니다. 그래픽 모드(X 디스플레이 관리자에서)로 로그인하면 로그인 셸을 얻지 않고, 세션 관리자나 창 관리자를 얻습니다.  
기존 세션 (화면, X 터미널, Emacs 터미널 버퍼, 다른 쉘 내부의 셸)에서 터미널에서 셸을 시작하면, 대화령 비 로그인 쉘이 생성됩니다.  
쉘이 명령행에서 스크립트 또는 명령을 전달하면, 쉘은 비 대화식 비 로그인 쉘입니다. 그러한 셸은 항상 실행됩니다.  
  
`shopt`를 사용하여 로그인 쉘에 있는지 확인할 수 있습니다.

```Bash
$ shopt -q login_shell && echo 'login' || echo 'not-login'
```

  

**산술 확장**

```Bash
$ v1=12
$ v2=$((v1+34))
$ echo $v2
46
$ v3=$(($v1+$v2)); echo $v3
58
$ v3=$((v1+v2)); echo $v3
58
$ ((v3++))
$ echo $v3
59
$ ((v3+=1)); echo $v3
60
$ if true; then echo true; fi
true
$ if ((true)); then echo true; fi
$ if ((0)); then echo true; fi
$ if ((1)); then echo true; fi
true
$ if $((true)); then echo true; fi
0: command not found
```

  

**exit와 종료상태**

  

**논리 연산 &&와 ||**

```Bash
$ command1 || command2
# command1이 성공적으로 실행되지 않은 경우에만 command2를 실행합니다.
$ command1 && command2
# command1이 성공적으로 실행된 경우에만 command2를 실행합니다.
```

  

**명령분리자 ;**

줄바꿈 문자가 발생할 때 명령 분리자(;)를 떠올리자

```Bash
$ if true; then echo true; fi
true
$ if true \
> then echo true
> fi
true

$ tool=saw; echo $tool
saw
$ tool=hammer echo $tool
saw
$ echo $tool
saw
```

  

**인라인그룹 {..}**

```Bash
$ ls dir3 && echo "dir directory is here" || mkdir dir3 && echo "dir directory is made"
ls: cannot access dir3: No such file or directory
dir directory is made
$ ls dir3 && echo "dir directory is here" || { mkdir dir3 && echo "dir directory is made" ;}
# dir3를 찾으면 "dir directory is here" 아니면 dir3를 생성하고 "dir directory is made"
dir directory is here
```

중괄호 닫기 ;}전에 세미콜론을 잊지맙시다.