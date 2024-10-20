---
type: Linux
archive: false
---
## 1. 쉘 기초 명령어

echo

**glob과 공백**

`*`: globe

인용문

[..]와 테스트

**명령어(wc)**

**명령어(tail)**

**명령어(pushd/popd)**

**명령어(printf)**

**명령어(read)**

## 2. 쉘 스크립트

### 쉘 스크립트란?

- 쉘(shell)은 명령 인터프리터(Command interpreter).
- 사용자가 운영 체제에 대화식(interactively) 으로 명령을 내리거나, 명령을 일괄(batch)적으로 실행할 수 있는 기능을 제공하는 응용 프로그램.

  

**쉬뱅 작성**

리눅스 스크립트의 #!로 시작되는 첫번째 줄  
스크립트를 읽는 인터프리터를 지정함  

```Shell
#!/bin/bash
#!/bin/sh
# 쉬뱅 예시.
```

DOS 스타일의 줄끝

  

  

**특수문자 종류**

- **공백(WHITE SPACE)**
    
    탭(Tab), 줄 바꿈(newline), 세로 탭, 양식 공급(form feed), 캐리지 리턴(Carriage Return) 또는 공백(White Space)  
    bash는 공백을 사용하여 단어의 시작과 끝을 결정.  
    사용자가 명령어을 입력할 시, 첫 번째 단어는 명령 이름이며, 추가 단어는 해당 명령에 대한 인수가 됨.  
    
- **확장(EXPANSION)**
    
    다양한 유형의 확장(Expansion)을 도입함.
    
    parameter expansion(파라미터 확장)  
    e.g. $var or ${var}  
    
    command substitution(명령 대체)  
    e.g. $(command)  
    
    arithmetic expansion(산술 확장)  
    e.g. $((expression))  
    
- **큰 따옴표(DOUBLE QUOTES)**
    
    그 안의 텍스트가 여러 단어나 인수로 분리되지 않도록 보호.  
    끈 따옴표 내의 문자들을 대체(Substitution)하는 것이 가능하다.  
    
    \(백 슬래시), $(달러), `(백틱)를 제외한 대부분의 다른 특수 문자의 의미는 억제됩니다.(즉, 일만분자로 해석)
    
- **작은 따옴표(SINGLE QUOTE)**
    
    문자 그대로의 의미를 갖도록 테스트를 보호하십시오  
    모든 특수 문자의 해석이 방지됩니다.(인용부호 안의 문자열 내용을 Bash가 해석하지 않습니다.)  
    특수 문자가 그대로 전달되고 여러 단어가 분할되지 않습니다.  
    
- **탈출(ESCAPE)**
    
    다음 문자가 특수 문자로 해석되는 것을 방지합니다.  
    끈 따옴표 안에서 작동하며 작은 따옴표로는 일반적으로 무시됩니다.  
    
- **주석(COMMENT)**
    
    '#' 문자의 도입은 그 행의 끝까지 모두 주석으로 처리됩니다.
    
- **테스트(TEST)**
    
    조건부 표현식이 'true'인지 'false'인지를 결정하기 위한 조건식의 평가.  
    테스트는 Bash에서 여러 조건을 평가하는데 사용됩니다.  
    
    [[]]
    
- **부정하다(NEGATE)**
    
    테스트나 종료 상태를 무효화하거나 되돌리기 위해 사용됩니다.
    
    !
    
- **방향재지정(REDIRECTION)**
    
    명령의 출력 또는 입력을 재지정합니다.
    
    ><
    
- **파이프(PIPE)**
    
    초기 명령의 출력을 2차 명령의 입력으로 재 지정합니다.
    
    |
    
- **명령 분리자(COMMAND SEPARATOR)**
    
    같은 줄에 있는 여러 명령을 구분하는 데 사용됩니다.
    
    ;
    
- **인라인 그룹(INLINE GROUP)**
    
    중괄호 안의 명령은 마치 하나의 명령처럼 취급됩니다.  
    Bash 구문이 하나의 명령만을 필요로 하고, 함수의 사용은 피하고 싶으 때, 이것을 사용하는 것이 편리합니다.  
    
    {}
    
- **서브 셸 그룹(SUB SHELL GROUP)**
    
    위와 비슷하지만 내부 명령이 서브 쉘에서 실행되는 경우  
    명령이 부작용을 일으키는 경우 샌드 박스처럼 많이 사용됩니다.(변수 변경하기 같은 경우)  
    현재의 쉘에는 영향을 주지 않습니다.  
    
    ()
    
- **산술 표현식(ARITHMETIC EXPRESSION)**
    
    산술 표현식에서 +, -, *, /와 같은 문자는 계산에 상요되는 수학 연산자입니다.  
    그것들을 다음과 같은 변수 할당에 사용할 수 있습니다. (( a=1 + 4 )).  
    테스트에도 사용합니다. if (( a < b ))  
    
- **산술 확장(ARITHMETIC EXPANSION)**
    
    위와 유사하지만 표현식은 산술 계산 결과로 대체됩니다.
    
    $(())
    
- **홈 디렉토리(HOME DIRECTORY)**
    
    ~(tild)는 홈 디렉터리를 나타냅니다.  
    그다음에 '/'이 올 때 '티드(~)'는 현재 사용자의 홈 디렉터리를 나타낸다.  
    도는 사용자 이름을 지정해야 합니다.  
    

**쉘 변수**

```Bash
$ animal=tiger  # 변수 초기화 시 = 사이에 공백이 있으면 안 됨. 공백문자주의, 알파벳 숫자 밑줄로 표현
$ echo "tigier's color is $color"  # 변수를 참조할 때에는 $이 필요.
```

---

**파라미터 대체와 인용부호**

```Bash
$ book="The old man and the sea.mp3"
$ rm "$book"

$ animal=Tiger; color=Red
$ echo "$animals $colors"  # error
$ echo "${animal}s vs. ${color}s" 
```

**매개변수 확장(PE)**

```Bash
$ testString="That that is is that that is not is not"
$ echo ${\#tehstString}
39
$ echo ${testString:0}
That that is is that that is not is not
$ echo ${testString:1}
hat that is is that that is not is not
$ echo ${testString:3}
t that is is that that is not is not
$ echo ${testString:3:3}
t t
$ echo ${testString\#T*is}  # That that is 삭제
is that that is not is not
$ echo ${testString#\#T*is}  # 대문자 T부터 시작해서 끝부분 is까지 포함되는 부분 전부 삭제 
# That that is is that that is not is 삭제
not
$ echo ${testString%is*not}  # 뒷부분 is not 삭제
That that is is that that is not
$ echo ${testString%%is*not}  # 뒷부분부터 is is that that is not is not 삭제
That that
$ echo ${testString//that}
That is is is not is not
$ echo ${testString/that/this}
That this is is that that is not is not
$ echo ${testString/[tT]hat/this}
this that is is that that is not is not
$ echo ${testString//[tT]hat/this}
this this is is this this is not is not
$ echo ${testString/\#That/this}
this that is is that that is not is not
$ echo ${testString/%not/NO}
That that is is that that is not is NO
```

#### 특수 매개 변수(SPECIAL PARAMETERS)

|이름|Usage|Description|
|---|---|---|
|[[0]]|$0|스크립트의 이름 또는 경로를 포함합니다.|
|[[1 2 etc]]|$1 etc|위치 매개 변수에는 현재 스크립트 또는 함수에 전달된 인수가 포합됩니다.|
|[[]]|"$*"|모든 위치 매개 변수의 모든 단어로 확장됩니다. 큰 따옴표를 붙이면, IFS 변소의 첫 번째 문자로 분뢰 된 모든 문자열을 포함하는 단일 문자열로 확장됩니다. (나중에 설명)|
|[[@]]|$@|모든 위치 매개 변수의 모든 단어로 확장됩니다. 큰 따옴표로 묶어서 개별 단어로모두 목록으로 확장합니다.|
|[[Resource/Linux Shell Script - 기본 개념/특수 매개 변수(SPECIAL PARAMETERS)/\|]]|$|위치 매개 변수의 수로 확장됩니다.|
|[[ 2]]|$?|가장 최근에 완료한 포 그라운드 명령의 종료 코드로 확장합니다.|
|[[$]]|$$|현재 쉘의 PID(프로세스 ID)으로 확장됩니다.|
|[[!]]|$!|백그라운드에서 가장 최근에 실행 된 명령의 PID로 확장합니다.|
|[[_]]|$_|실행된 마지막 명령의 마지막 인수로 확장합니다.|

  
  

  

---

#### 환경 변수(ENVIRONMENT VARIABLES)

|이름|Description|
|---|---|
|[[BASH_VERSION]]|Bash 버전을 설명하는 문자열을 포함합니다.|
|[[HOSTNAME]]|컴퓨터의 호스트 이름이 들어있습니다.|
|[[PPID]]|이 쉘의 부모 프로세스의 PID를 포함합니다.|
|[[PWD]]|현재 작업 디렉토리를 포함합니다.|
|[[RANDOM]]|0과 32767 사이의 (의사) 난수가 생성됩니다.|
|[[UID]]|현재 사용자의 ID 번호입니다.|
|[[COLUMNS]]|터미널의 한 줄에 들어갈 수 있는 문자 수|
|[[LINES]]|터미널에 들어갈 수 있는 줄 수|
|[[HOME]]|현재 사용자의 홈 디렉토리|
|[[PATH]]|경로 이름이 지정되지 않은 경우 명령을 찾기 위해 검색될 클론으로 구분된 경로 목록(alias, function, builtin 명령 또는 shell 키워드는 제외)|
|[[PS1]]|쉘 프롬프트의 형식을 설명하는 문자열을 포함합니다.|
|[[TMPDIR]]|쉘(임시 파일)을 저장하는 데 사용되는 디렉토리를 포함|

  
  

---

**글로브 패턴(GLOB PATTERNS)**

글로브(Glob)는 기본적으로 파일 이름 또는 다른 문자열을 일치시키는 데 사용할 수 있는 패턴입니다.  
글로브는 일반 문자와 메타 문자로 구성됩니다  
메타 문자는 특별한 의미를 갖는 문자입니다.  
이들은 globs에서 사용할 수 있는 메타 문자입니다.  

**글로브 패턴(GLOB PATTERNS)**

* : 널 문자열을 포함하여 모든 문자열과 일치합니다.

? : 모든 단일 문자와 일치합니다.

[...] : 둘러싸인 문자 중 하나와 일치합니다.

  

**확장 glob**

```Bash
$ shopt -s extglob  # 확장 glob를 사용하게 하는 옵션
$ echo !(*jpg|*bmp)
```

**확장된 글로브(EXTENDED GLOBS)**

?(list) : 주어진 패턴의 0 또는 1번 일치시킵니다.

*(list) : 주어진 패턴의 0 회 이상 일치

+(list) : 주어진 패턴의 하나 이상의 일치와 일치합니다.

@(list) : 주어진 패턴 중 하나와 일치합니다.

!(list) : 주어진 패턴을 제외한 모든 것을 일치시킵니다.

---

**declare**

```Bash
$ declare -a alnum=(a1 b1 c1 d1 e1 f1)  # -a : 배열 옵션
$ echo ${alnum[1]}
b1

$ declare -i inum=78  # $ -i : 정수형 옵션
$ inum=inum+1
$ echo $inum
79

$ declare -r rPi=3.14  # -r : 읽기 전용 변수 옵션
$ rPi=312  # 다른 값으로 재 초기화 불가능

$ declare -x xpath="${HOME}/Desktop/mydir"  # -x : 변수를 export 하는 옵션
$ export XPATH="${HOME/Desktop/mydir"  # 위 명령과 동일한 내용.
```

**명령어(tr)**

**명령어(cut)**