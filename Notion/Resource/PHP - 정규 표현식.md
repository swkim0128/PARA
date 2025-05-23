---
type: PHP
archive: false
---
## 정규 표현식의 개념

---

### 정규 표현식(regular expression)이란?

정규 표현식(regular expression)은 문자열에서 특정한 규칙을 가지는 문자열의 집합을 찾아내기 위한 검색 패턴입니다.  
이러한 검색 패턴은 모든 종류의 문자열 검색이나 교체 등의 작업에서 사용할 수 있습니다.  

PHP에서는 다음과 같은 두 가지의 정규 표현식을 지원합니다.

1. POSIX
2. PCRE(Perl-Compatible Regular Expression)

  

POSIX 정규 표현식은 배우기가 쉽고 실행 속도가 빠른 편입니다.

그에 비해 PCRE 정규 표현식은 POSIX 정규 표현식을 확장하였기에 더 강력하고 유연하게 동작합니다.

하지만 우리 수업에서는 좀 더 간단한 형식의 POSIX 표준 정규 표현식을 살펴볼 것입니다.

  

### 정규 표현식 리터럴

PHP에서 정규 표현식 리터럴은 다음 문법을 사용하여 표현합니다.

> [!important]  
> 문법/검색패턴/플래그  

정규 표현식 리터럴은 슬래시(/) 기호로 시작하여, 슬래시(/) 기호로 끝납니다.

또한, 필요에 따라 플래그를 추가하여 기본 검색 설정을 변경할 수도 있습니다.

  

### preg_match() 함수

preg_match() 함수는 해당 문자열에서 전달받은 정규 표현식과 일치하는 패턴을 검색합니다.

> [!important]  
> 문법preg_match($pattern, $subject [,$matches]);  

  

첫 번째 인수로 전달받은 정규 표현식에 해당하는 패턴을 두 번째 인수로 전달받은 문자열에서 검색합니다.  
이렇게 검색된 결과는 배열로 반환되며, 세 번째 인수로 반환값이 저장될 배열을 직접 전달할 수도 있습니다.  

preg_match() 함수는 정규 표현식에 해당하는 패턴이 검색되면, 더는 검색하지 않고 검색을 중단합니다.  
이 함수는 일치하는 패턴이 존재하면 1을 반환하고, 존재하지 않으면 0을 반환합니다.  

  

### 단순한 패턴 검색

정규 표현식을 사용하여 단순한 패턴을 검색하고자 할 때는 찾고자 하는 문자열을 직접 나열하면 됩니다.

예를 들어, 다음과 같은 정규 표현식은 정확히 "abc"라는 문자열만이 일치할 것입니다.

```PHP
/abc/

# 다음 예제는 정규 표현식을 이용한 단순한 패턴 검색 예제입니다.
$subject = "간장 공장 공장장은 강 공장장이고, 된장 공장 공장장은 장 공장장이다.";

if (preg_match('/공장/', $subject)) {
    echo "해당 문자열에서 '공장'을 발견했습니다.<br>";
} else {
    echo "해당 문자열에서 '공장'을 발견하지 못했습니다.<br>";
}

if (preg_match('/장공/', $subject)) {
    echo "해당 문자열에서 '장공'을 발견했습니다.<br>";
} else {
    echo "해당 문자열에서 '장공'을 발견하지 못했습니다.<br>";
}
```

  

위의 예제에서 첫 번째 정규 표현식은 해당 문자열이 "공장"이라는 부분 문자열을 포함하고 있으므로, 1을 반환합니다.  
하지만 두 번째 정규 표현식은 해당 문자열이 "장 공"이라는 부분 문자열은 포함하고 있지만, 정확히 "장공"이라는 부분 문자열을 포함하지 않으므로, 아무것도 일치하지 않습니다.  

preg_match() 메소드는 해당 문자열에서 인수로 전달받은 정규 표현식과 일치하는 부분 문자열을 찾지 못하면 0을 반환합니다.

  

### 플래그(flags)

정규 표현식 리터럴을 작성할 때 플래그를 사용하여 기본 검색 설정을 변경할 수 있습니다.

|플래그(flag)|설명|
|---|---|
|i|검색 패턴을 비교할 때 대소문자를 구분하지 않도록 설정함.|
|g|검색 패턴을 비교할 때 일치하는 모든 부분을 선택하도록 설정함.|
|m|검색 패턴을 비교할 때 여러 줄의 입력 문자열을 그 상태 그대로 여러 줄로 비교하도록 설정함.|
|y|대상 문자열의 현재 위치부터 비교를 시작하도록 설정함.|
|u|대상 문자열이 UTF-8로 인코딩된 것으로 설정함.|

```PHP
$subject = "bcabcAB";

// 기본 설정으로 검색 패턴을 비교할 때 대소문자를 구분함.
preg_match_all('/AB/', $subject, $matches_01);      // "AB"

// 검색 패턴을 비교할 때 대소문자를 구분하지 않도록 설정함.
preg_match_all('/AB/i', $subject, $matches_02); // "ab", "AB"
```

> [!important]  
> preg_match_all() 함수는 해당 문자열에서 전달받은 정규 표현식과 일치하는 패턴을 모두 검색하여, 세 번째 인수로 전달되는 배열에 저장합니다.  

  

## 정규 표현식의 기초

---

### 특수 문자(special characters)

정규 표현식을 사용하여 단순한 패턴을 검색하고자 할 때는 찾고자 하는 문자열을 직접 나열하면 됩니다.  
하지만 숫자만을 검색하거나, 띄어쓰기를 찾는 등 정확히 일치하는 패턴보다 더 복잡한 조건을 사용하려면 특수 문자를 사용해야 합니다.  
이렇게 정규 표현식에서 사용하는 특정 의미를 가지는 기호를 특수 문자 또는 메타(meta) 문자라고 합니다.  

정규 표현식에서 사용할 수 있는 대표적인 특수 문자는 다음과 같습니다.

|특수문자|설명|
|---|---|
|.|줄 바꿈 문자(\n)를 제외한 임의의 한 문자를 의미함.|
|?|해당 문자 패턴이 0번 또는 1번만 반복됨.|
|*|해당 문자 패턴이 0번 이상 반복됨.|
|+|해당 문자 패턴이 1번 이상 반복됨.|
|{...}|반복되는 횟수를 지정함.|
|^|문자열의 처음을 의미함.|
|$|문자열의 끝을 의미함.|
|\|특수문자를 무시함.|
|\||선택을 의미함. (OR)|
|(...)|그룹화의 시작과 끝을 의미함.|

```PHP
/.ap/         // 문자열 "ap" 앞에 임의의 한 문자가 등장하는 문자열 : aap, bap, cap, @ap, \#ap, ...
/a?b/         // b 앞에 a가 0번 또는 1번 등장하는 문자열 : b, ab
/a*b/         // b 앞에 a가 0번 이상 등장하는 문자열 : b, ab, aab, aaab, ...
/a+b/         // b 앞에 a가 1번 이상 등장하는 문자열 : ab, aab, aaab, aaaab, ...
/a{2,4}b/     // b 앞에 a가 2번 이상 4번 이하 등장하는 문자열 : aab, aaab, aaaab
/a{2,}b/      // b 앞에 a가 2번 이상 등장하는 문자열 : aab, aaab, aaaab, aaaaab, ...
/^abc/        // abc로 시작하는 문자열 : abc, abcd, abcdef, ...
/abc$/        // abc로 끝나는 문자열 : abc, zabc, xyzabc, ...
/abc|def|ghi/ // abc, def 또는 ghi 중 하나의 문자열
```

  

### 양화사(quantifier)

정규 표현식에서는 특수 문자로 수량을 나타내는 다양한 양화사를 사용할 수 있습니다.

- '*'는 바로 앞의 문자가 0번 이상 나타날 경우를 검색합니다. ({0, }와 같음)
- '+'는 바로 앞의 문자가 1번 이상 나타날 경우를 검색합니다. ({1, }과 같음)
- '?'는 바로 앞의 문자가 0번 또는 1번만 나타날 경우를 검색합니다. ({0,1}과 같음)
- '{n,m}'은 바로 앞의 문자가 반복되는 횟수를 지정합니다.

바로 앞의 문자가 최소 n번이상 최대 m번이하로 나타날 경우를 검색합니다. (n과 m은 반드시 양의 정수이어야만 함)

```PHP
$subject = "PHP is cooooool!";

// 문자 'l' 바로 앞에 문자 'o'가 0 또는 1번 나타나는 경우를 검색함.
preg_match_all('/o?l/', $subject, $match_01);

// 문자 'l' 바로 앞에 문자 'o'가 0번 이상 나타나는 경우를 검색함.
preg_match_all('/o*l/', $subject, $match_02);

// 문자 'l' 바로 앞에 문자 'o'가 1번 이상 나타나는 경우를 검색함.
preg_match_all('/o+l/', $subject, $match_03);

// 영문 소문자가 1번 이상 나타나는 경우를 검색함.
// 즉, 영문 소문자만으로 이루어진 부분 문자열을 검색함.
preg_match_all('/[a-z]+/', $subject, $match_04);


$subject = "PHP is cooooool!";

// 문자 'l' 바로 앞에 문자 'o'가 최소 2번 이상 최대 4번 이하로 나타나는 경우를 검색함.
preg_match_all('/o{2,4}l/', $subject, $match_01);
var_dump($match);

// 문자 'l' 바로 앞에 문자 'o'가 최소 2번 이상 나타나는 경우를 검색함.
preg_match_all('/o{2,}l/', $subject, $match_02);
var_dump($match);

// 문자 'l' 바로 앞에 문자 'o'가 정확히 6번 나타나는 경우를 검색함.
preg_match_all('/o{6}l/', $subject, $match_03);
```

  

### 위치 문자

정규 표현식에서는 해당 문자열에서 패턴을 검색할 단어의 위치까지 지정할 수 있습니다.

- '^'는 단어의 맨 앞에 위치한 해당 패턴만을 검색합니다.
- '$'는 단어의 맨 뒤에 위치한 해당 패턴만을 검색합니다.

```PHP
$subject = "abcdef defabc";

// 단어가 문자열 "abc"로 시작하는 경우를 검색하여, 해당 부분 문자열을 'ABC'로 대체함.
$match_01 = preg_replace('/^abc/', 'ABC',$subject);

// 단어가 문자열 "abc"로 끝나는 경우를 검색하여, 해당 부분 문자열을 'ABC'로 대체함.
$match_02 = preg_replace('/abc$/', 'ABC', $subject);
```

> [!important]  
> preg_replace() 함수는 해당 문자열에서 전달받은 정규 표현식과 일치하는 패턴을 검색하여, 해당 부분을 두 번째 인수로 전달되는 문자열로 대체한 새로운 문자열을 반환합니다.  

  

### 선택 문자

정규 표현식에서는 특수문자 '|'를 사용하여 여러 개의 검색 패턴을 사용할 수 있습니다.

즉, 특수문자 '|'로 구분된 정규 표현식 중 어느 하나에만 일치해도 검색됩니다.

```PHP
$subject = "ABCdefGHIjkl";

// 문자열 'abc' 또는 'def' 또는 'jkl'만을 검색함.
// 즉, 위의 세 문자열 중 어느 하나에만 일치해도 검색됨.
preg_match_all('/abc|def|jkl/', $subject, $match);
```

  

### 문자 클래스(character class)

문자 클래스(character class)란 정규 표현식에서 명시된 범위에 해당하는 한 문자만을 선택하기 위해 사용되는 문자입니다.

이러한 문자 클래스는 꺾쇠 괄호([])를 사용하여 표현합니다.

```PHP
/[0-3]/        // 0부터 3까지의 숫자에 해당하는 한 문자
/[a-z]/        // 영문 소문자에 해당하는 한 문자
/[0-9a-zA-Z]/  // 숫자 또는 영문 대소문자에 해당하는 한 문자

$subject = "@ap";

preg_match("/.ap/", $subject, $match_01);        // "ap" 문자열 앞에 임의의 한 문자가 나타나는 경우를 검색함.
preg_match("/[a-zA-Z]ap/", $subject, $match_01); // "ap" 문자열 앞에 영문자 한 문자가 나타나는 경우를 검색함.
```

  

위의 예제에서 사용된 특수 문자 '.'는 줄 바꿈 문자를 제외한 임의의 문자 하나를 의미합니다.

이 문자를 잘 사용하면, 검색하고자 하는 문자의 범위를 더욱 제한할 수 있습니다.

  

### POSIX 문자 클래스

앞서 살펴본 문자 클래스 이외에도 POSIX 정규 표현식에서만 사용할 수 있는 문자 클래스가 존재합니다.

POSIX에서만 사용할 수 있는 문자 클래스는 다음과 같습니다.

|문자 클래스|설명|
|---|---|
|[:alnum:]|영문자와 숫자에 포함되는지를 확인함.|
|[:alpha:]|영문 대소문자에 포함되는지를 확인함.|
|[:lower:]|영문 소문자에 포함되는지를 확인함.|
|[:upper:]|영문 대문자에 포함되는지를 확인함.|
|[:digit:]|십진법 숫자에 포함되는지를 확인함.|
|[:xdigit]|16진법 숫자나 문자에 포함되는지를 확인함.|
|[:punct:]|구두점에 포함되는지를 확인함.|
|[:blank:]|탭과 띄어쓰기에 포함되는지를 확인함.|
|[:space:]|공백 문자에 포함되는지를 확인함.|
|[:cntrl:]|제어 문자에 포함되는지를 확인함.|
|[:print:]|출력할 수 있는 문자에 포함되는지를 확인함.|
|[:graph:]|띄어쓰기를 제외한 모든 출력할 수 있는 문자에 포함되는지를 확인함.|

위의 표와 같이 POSIX에서만 사용할 수 있는 문자 클래스는 기본적으로 꺾쇠 괄호([])를 포함하고 있습니다.

따라서 이러한 POSIX 전용 문자 클래스는 다음과 같이 꺾쇠 괄호를 두 번 사용하여 표현됩니다.

```PHP
/[[:alpha:]][[:digit:]]/ // 첫 번째 문자가 영문자이고, 두 번째 문자가 숫자인 길이가 2인 문자열
                         // a1, a2, ..., b1, b2, ...

$subject = "Hello PHP is cool!";

// 첫 번째와 세 번째 문자가 영문 소문자이고, 두 번째 문자가 띄어쓰기인 경우를 검색함.
preg_match_all('/[[:lower:]][[:space:]][[:lower:]]/', $subject, $match_01);

// 첫 번째 문자가 영문 소문자이고, 두 번째 문자가 띄어쓰기, 세 번째 문자가 영문 대문자인 경우를 검색함.
preg_match('/[[:lower:]][[:space:]][[:upper:]]/', $subject, $match_02);
```

  

## 정규 표현식의 활용

---

### 정규 표현식의 활용

앞서 살펴본 정규 표현식을 활용하면, 다음과 같은 데이터가 해당 형식에 맞는지를 손쉽게 확인할 수 있습니다.

1. 전화번호

2. 이메일 주소

  

### 전화번호 확인

정규 표현식을 이용하면 해당 전화번호가 유효한 형식의 전화번호인지를 확인할 수 있습니다.

> [!important]  
> 정규 표현식① /^[[:digit:]]{2}\-[[:digit:]]{4}\-[[:digit:]]{4}/     // 02-1234-5678, ...② /^[[:digit:]]{2,3}\-[[:digit:]]{3,4}\-[[:digit:]]{4}/ // 02-1234-5678, 031-123-5678, 010-1234-5678, ...  

  

①번 정규 표현식은 전화번호의 맨 앞자리가 2자리이고, 국번이 4자리인 전화번호만을 검색할 수 있습니다.

하지만 지역번호나 핸드폰의 경우에는 전화번호의 맨 앞자리가 3자리이며, 국번이 3자리인 전화번호도 아직 존재합니다.

따라서 ②번 정규 표현식과 같이 전화번호의 맨 앞자리가 2자리나 3자리이고, 국번도 3자리나 4자리인 전화번호까지 검색할 수 있도록 해야합니다.

```PHP
$tel = "02-1234-5678";
$cell = "010-1234-5678";

$pattern_01 = "/^[[:digit:]]{2}\-[[:digit:]]{4}\-[[:digit:]]{4}/";
if (preg_match($pattern_01, $tel, $matches_01)) {
    var_dump($matches_01);
} else {
    echo "{$tel}은 유효한 형식의 전화번호가 아닙니다.<br>";
}

if (preg_match($pattern_01, $cell, $matches_02)) {
    var_dump($matches_02);
} else {
    echo "{$cell}은 유효한 형식의 전화번호가 아닙니다.<br>";
}

$pattern_02 = "/^[[:digit:]]{2,3}\-[[:digit:]]{3,4}\-[[:digit:]]{4}/";
if (preg_match($pattern_02, $tel, $matches_03)) {
    var_dump($matches_03);
} else {
    echo "{$tel}은 유효한 형식의 전화번호가 아닙니다.<br>";
}

if (preg_match($pattern_02, $cell, $matches_04)) {
    var_dump($matches_04);
} else {
    echo "{$cell}은 유효한 형식의 전화번호가 아닙니다.<br>";
}
```

> [!important]  
> 정규 표현식에서 '\'문자 바로 뒤에 일반 문자가 나오면, 해당 문자는  특수 문자로 인식됩니다.또한, '\'문자 바로 뒤에 특수 문자가 나오면, 해당 문자는 일반 문자로 인식됩니다.위의 예제에서 사용된 '-'문자는 범위를 나타내는 특수 문자이므로, '\-'는 단순히 전화번호에서 사용되는 '-'기호로 인식됩니다.  

  

### 이메일 주소 확인

전화번호뿐만 아니라 이메일 주소도 특정 형식을 가지고 있습니다.

따라서 정규 표현식을 이용하면 해당 이메일 주소가 유효한 형식의 이메일 주소인지를 확인할 수 있습니다.

해당 전화번호가 유효한 형식의 전화번호인지를 다음 정규 표현식을 이용하여 확인할 수 있습니다.

> [!important]  
> 정규 표현식① /([0-9a-zA-Z_-]+)@([0-9a-zA-Z_-]+)\.([0-9a-zA-Z_-]+)/      // help@abcd.com, ...② /([0-9a-zA-Z_-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}/ // help@abcd.com, help@abcd.co.kr, ...  

  

위의 예제에서 사용된 다음 정규 표현식의 의미는 숫자나 영문 대소문자, 언더스코어(_) 또는 '-'기호를 포함한 문자가 1번 이상 반복되는 문자열을 의미합니다.

> [!important]  
> 정규 표현식[0-9a-zA-Z_-]+  

  

①번 정규 표현식은 '@'문자와 '.'문자를 각각 하나씩만 포함하는 이메일 주소만을 검색합니다.  
따라서 이 정규 표현식은 도메인 이름이 '.com'이나 '.net'과 같이 '.'문자를 하나만 포함하는 이메일 주소만 검색할 수 있습니다.  

즉, 위의 예제처럼 '.'문자를 2개 이상 포함하는 이메일 주소는 정확하게 인식하지 못합니다.  
그러므로 '.'문자를 2개 이상 포함하는 이메일 주소는 ②번 정규 표현식과 같이 좀 더 자세히 표현해야 합니다.  

다음 정규 표현식은 '.'문자로 시작하고, 숫자나 영문 대소문자, 언더스코어(_) 또는 '-'기호를 포함한 문자가 1번 이상 반복되는 문자열이 1번 또는 2번 반복되는 문자열을 의미합니다.

> [!important]  
> 정규 표현식(\.[0-9a-zA-Z_-]+){1,2}  

  

```PHP
$com = "help@abcd.com";
$co = "help@abcd.co.kr";

$pattern_01 = "/([0-9a-zA-Z_-]+)@([0-9a-zA-Z_-]+)\.([0-9a-zA-Z_-]+)/";
if (preg_match($pattern_01, $com, $matches_01)) {
    var_dump($matches_01[0]);
} else {
    echo "{$com}은 유효한 형식의 이메일 주소가 아닙니다.<br>";
}

if (preg_match($pattern_01, $co, $matches_02)) {
    var_dump($matches_02[0]);
} else {
    echo "{$co}은 유효한 형식의 이메일 주소가 아닙니다.<br>";
}

$pattern_02 = "/([0-9a-zA-Z_-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}/";
if (preg_match($pattern_02, $com, $matches_03)) {
	var_dump($matches_03[0]);
} else {
	echo "{$com}은 유효한 형식의 이메일 주소가 아닙니다.<br>";
} 

if (preg_match($pattern_02, $co, $matches_04)) {
    var_dump($matches_04[0]);
} else {
    echo "{$co}은 유효한 형식의 이메일 주소가 아닙니다.<br>";
}

# PHP에서는 유효한 형식의 이메일 주소인지를 확인하기 위해 정규 표현식뿐만 아니라 filter_var() 함수를 제공하고 있습니다.
$com = "help@abcd.com";
$co = "help@abcd.co.kr";

if (filter_var($com, FILTER_VALIDATE_EMAIL)) {
    echo $com;
} else {
    echo "{$com}은 유효한 형식의 이메일 주소가 아닙니다.<br>";
}

if (filter_var($co, FILTER_VALIDATE_EMAIL)) {
    echo $co;
} else {
    echo "{$co}은 유효한 형식의 이메일 주소가 아닙니다.<br>";
}
```

filter_var() 함수에 대한 더 자세한 사항은 PHP Form 입력 형식 검증 수업에서 확인할 수 있습니다.

  

### 한글 확인

정규 표현식에서는 영문자뿐만 아니라 한글도 사용할 수 있습니다.

해당 문자가 한글인지를 확인하는 정규 표현식은 다음과 같습니다.

> [!important]  
> 정규 표현식① /[가-힣]/                // 한글 소리 마디② /[\\x{ac00}-\\x{d7af}]/u // 한글 소리 마디의 유니코드 범위 목록값  

  

한글 소리 마디(hangul syllables)란 초성 19개, 중성 21개, 종성 28개로 이루어지는 총 11,172개의 한글 문자를 가리킵니다.

위의 ①번과 ②번 정규 표현식은 둘 다 현대 한글에서 표현할 수 있는 11,172개의 한글 소리 마디를 모두 검색할 수 있습니다.

이 두 정규 표현식은 대부분의 경우 잘 동작하겠지만, ①번 정규 표현식은 언어 설정이 한글이 아닌 시스템에서는 동작이 안 될 수도 있습니다.

②번 정규 표현식처럼 'u'플래그를 추가하여 해당 정규 표현식 문자열을 UTF-8로 인코딩된 것처럼 취급할 수 있습니다.

```PHP
$eng = "gil-dong Hong";
$kor = "홍길동";

$pattern = "/[가-힣]+/"; // 한글 소리 마디
if (preg_match($pattern, $eng, $matches_01)) {
    var_dump($matches_01);
} else {
    echo "{$eng}에는 한글이 포함되어 있지 않습니다.<br>";
}

if (preg_match($pattern, $kor, $matches_02)) {
    var_dump($matches_02);
} else {
    echo "{$eng}에는 한글이 포함되어 있지 않습니다.<br>";
}

# 다음 예제는 해당 문자열에서 한글만을 제거하는 예제입니다.
$text = "123가나abc다라";
$pattern = "/[\\x{ac00}-\\x{d7af}]+/u";         // 한글 소리 마디(UTF-8)

$arr = preg_match_all('/./u', $text, $matches); // 줄 바꿈 문자(\n)를 제외한 임의의 한 문자씩 검색함.
echo preg_replace($pattern, '', $text);         // 해당 문자가 한글이면, 빈 문자열로 대체함.
```