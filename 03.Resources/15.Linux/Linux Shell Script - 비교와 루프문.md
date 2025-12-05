---
type: Linux
archive: false
---
## 비교와 루프문

---

**조건문(if..else..fi)**

```Bash
$ if true; then
> echo true
> else
> echo false
> fi
true

$ if true; then echo true; else echo false; fi
true

# style1
$ if COMMANDS
$ then OTHER COMMANDS
$ fi

# style2
$ if COMMANDS
$ then
$ OTHER COMMANDS
$ fi

# style3
$ if COMMANDS; then
$ OTHER COMMANDS
$ fi
```

  

**[..]vs[[..]]**

```Bash
$ tom="Tom hanks"
$ deniro="Robert Deniro"
$ [ $tom > $deniro ]
-bash: $deniro: ambiguous redirect
# [..] 안에서는 >< 문자가 리다이렉트로 해석된다.

$ [[ $tom > $deniro ]]
$ echo $?
0

$ [ $tom = $deniro ]
-bash: [: too many arguments
$ [ "$tom" = "$deniro" ]
$ [ "Tom hanks" = "Robert Deniro" ]
$ [[ $tom = $deniro ]]; echo $?
1
```

  

**인용부호 사용시 주의사항**

```Bash
$ VAR=; if [ $VAR = "" ]; then echo true; else echo false; fi
-bash: [: =: unary operator expected
false
$ VAR=; if [ "$VAR" = "" ]; then echo true; else echo false; fi
true
$ VAR=; if [[ $VAR = "" ]]; then echo true; else echo false; fi
true
```

  

**비교 메타 문자열**

```Bash
# hello.txt.bak 파일이 없을 경우에 `cp` 명령어 실행
$ if [ ! -f "hello.txt.bak"" ]; then
>    cp "hello.txt" "hello.txt.bak"
> fi

$ if (( $? )); then
>     echo 'Please run using "bash" or "sh", but not "." or "source"' > &2
>     exit 1
> fi

# 어던 경로에 파일 여부가 있는 지 확인함.
$ if [[ $(ls -A) ]]; then
>     echo "there are files"
> else
>     echo "no files found"
> fi   
```

  

**비교 메타 문자열**

#### [ 을 이용한 TEST

|이름|Description|
|---|---|
|[[-e FILE]]|파일이 있는 경우 True입니다.|
|[[-f FILE]]|파일이 일반 파일인 경우 True입니다.|
|[[-d FILE]]|파일이 디렉터리인 경우 True입니다.|
|[[-h FILE]]|파일이 심볼 링크인 경우 True입니다.|
|[[-p PIPE]]|파이프가 있는 경우 True입니다.|
|[[-r FILE]]|사용자가 파일을 읽을 수 있는 경우 True입니다.|
|[[-s FILE]]|파일이 존재하며 비어 있지 않은 경우 True입니다.|
|[[-t FD]]|터미널에서 FD가 열려 있는 경우 True입니다.|
|[[-w FILE]]|사용자가 파일을 쓸 수 있는 경우 True입니다.|
|[[-x FILE]]|파일이 실행 가능한 경우 True입니다.|
|[[-O FILE]]|파일이 사용자가 효과적으로 소유하는 경우 True입니다.|
|[[-G FILE]]|파일이 그룹에 의해 효과적으로 소유되는 경우 True입니다.|
|[[FILE -nt FILE]]|첫 번째 파일이 두 번째 파일보다 최신이면 True입니다.|
|[[FILE -ot FILE]]|첫 번째 파일이 두 번째 파일보다 오래된 경우 True입니다.|
|[[-z STRING]]|문자열이 비어 있으면 True입니다.(길이가 0임)|
|[[-n STRING]]|문자열이 비어 있지 않은 경우 True입니다.(길이 0이 아님)|
|[[STRING = STRING]]|첫 번째 문자열이 두 번째 문자열과 동일한 경우 True입니다.|
|[[STRING != STRING]]|첫 번째 문자열이 두 번째 문자열과 동일하지 않은 경우 True입니다.|
|[[STRING STRING]]|첫 번째 문자열이 두 번째 문자열보다 먼저 정렬되는 경우 True입니다.|
|[[STRING STRING 2]]|첫 번째 문자열이 두 번째 문자열 뒤에 정렬되는 경우 True입니다.|
|[[EXPR -a EXPR]]|두 식이 모두 참이면 참입니다. (logical AND)|
|[[EXPR -o EXPR]]|두 식 중 하나가 참이면 참입니다. (logical OR)|
|[[! EXPR]]|표현식의 결과를 반전합니다. (logical NOT)|
|[[INT -eq INT]]|두 정수가 동일한 경우 True입니다.|
|[[INT -ne INT]]|정수가 동일하지 않은 경우 True입니다.|
|[[INT -lt INT]]|첫 번째 정수가 두 번째 정수보다 작은 경우 True입니다.|
|[[INT -gt INT]]|첫 번째 정수가 두 번째 정수보다 큰 경우 True입니다.|
|[[INT -le INT]]|첫 번째 정수가 두 번째 정수보다 작거나 같으면 True입니다.|
|[[INT -ge INT]]|첫 번째 정수가 두 번째 정수보다 크거나 같은 경우 True입니다.|

  
  

#### [[ 을 이용한 TEST

|이름|Description|
|---|---|
|[[STRING = (or ==) PATTERN]]|`[` 과 같은 문자열 비교는 아니지만 패턴 일치가 수행됩니다. 문자열이 글로브 패턴과 일치하는 경우 True입니다.|
|[[STRING != PATTERN]]|`[` 과 같은 문자열 비교는 아니지만 패턴 일치가 수행됩니다. 문자열이 글로브 패턴과 일치하지 않는 경우 True입니다.|
|[[STRING =~ REGEX]]|문자열이 regex 패턴과 일치하는 경우 True입니다.|
|[[( EXPR )]]|괄호를 사용하여 평가 우선 순위를 변경할 수 있습니다.|
|[[EXPR && EXPR]]|테스트의 `-a` 연산자와 매우 유사하지만 첫 번째 표현식이 이미 거짓으로 판명되면 두 번째 표현식을 평가하지 않습니다.|
|[[EXPR EXPR]]|테스트의 `-o` 연산자와 매우 유사하지만 첫 번째 표현식이 이미 사실인 경우 두 번째 표현식을 평가하지 않습니다.|

  
  

- [ ] 보다는 [[ ]] 를 사용하는 것이 좋습니다.

  

**case**

```Bash
$ read -p "Enter any string: "
Enter any string: abc
$ case $REPLY in
>     +([[:digit:]]) ) echo "digits";;
>     *) echo "not digits";;
> esac
not digits
```

  

**getopts**

```Bash
# 사용자에게 전달인자를 전달받아 사용하는 옵션
```

  

**select**

```Bash
$ movies=("Avengers" "Matrix" "Titanic")
$ PS3="Please select your favorite movie: "
$ select movie in ${movies[@]}
> do
>     echo "$movie selected"
> done

$ movies=("Avengers" "Matrix" "Titanic", "None")
$ PS3="Please select your favorite movie: "
$ select movie in ${movies[@]}
> do
>     case $movie in
>       "None") echo "My favorite movie is not on the list. quit"; break;;
>       *) echo "$movie selected";;
>     esac
> done
```

  

**while 루프**

```Bash
$ while true; do
> echo "hello world"
> sleep 1
> done

$ while true; do
> echo -n -e "\a";
> sleep 1;
> done

$ count=10
$ for no in `eval echo {0..$count}`; do
> echo $no
> done
```

  

**for..in 루프**

```Bash
$ classroom=(desk pen note chair book)
$ echo ${ classroot[@] }
desk pen note chair book
$ for i in ${ !classroom[@]}; do  
# ${!classroom[@}}에서 !: 배열의 인덱스 참조 배열의 요소를 가져오는 것이 아니고 인덱스 값을 얻어오는 방법
>     if ["${classroom[$i]}" = 'pen']; then
>       classroom[$i]=''
>     fi
> done
```

  

**for((;;)) 루프**

```Bash
$ mystr="Hello world"
$ for(( i=0; i<${\#mystr}; i++)); do
>     c="${mystr:$i:1}"
>     echo "$c"
> done
```

  

**루프문과 glob**

```Bash
$ for file in $(ls *.mp3); do
>     rm "$file"
error
# 공백 문자에 의해 단어 하나씩 인식되어 삭제됨.

$ for file in "$(ls *.mp3)"; do
>     rm "$file";
> done
error
# 인용부호에 의해 mp3 파일들이 각각의 파일로 인식되는 것이 아닌 전체 문장인 하나의 파일로 인식

$ for file in *.mp3
> do rm "%file"
> done
success
# 쉘 스크립트에서 인용부호를 사용해야 할 때와 사용하지 않아야 할 때를 구분할 줄 아는 것이
# 매우 중요합니다.
```

  

**명령어(date)**

```Bash
$ date +"%Y-%m-%d"
$ date +"%Y/%m/%d"
$ date +"%Y-%m-%d %r"
$ date +"%Y-%m-%d %H:%M"
```

  

**명령어(seq)**

```Bash
$ seq 0 2 10
```