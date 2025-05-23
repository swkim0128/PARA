---
type: PHP
archive: false
---
## 변수 관련 함수

---

### 변수의 타입 변경

gettype() 함수는 전달받은 변수의 타입을 반환합니다.

변수를 전달하면 타입에 따라 해당 타입의 이름을 문자열로 반환합니다.

단, float 형의 경우에는 "float"가 아닌 "double"을 반환하며, 표준 타입이 아닌 경우에는 "unknown type"을 반환합니다.

settype() 함수를 사용하면 전달받은 변수의 타입을 변경할 수 있습니다.

이때 변환할 타입으로는 boolean, integer, string, array, object를 사용할 수 있습니다.

또한, PHP 4.2.0부터는 float과 null 타입도 사용할 수 있습니다.

settype() 함수는 전달받은 변수의 타입을 성공적으로 변경하면 true를 반환하고, 그러지 못했을 경우에는 false를 반환합니다.

```PHP
$x = 5;
echo gettype($x);      // integer

settype($x, "string");
echo gettype($x);      // string
```

  

> [!important]  
> PHP 4.2.0부터는 "boolean" 대신에 "bool"을 사용할 수 있으며, "integer" 대신에 "int"를 대신 사용할 수 있습니다.  

  

gettype() 함수는 내부적으로 문자열을 비교하기 때문에 실행 속도가 느립니다.

또한, 앞으로 나올 PHP 버전에서 반환되는 문자열이 바뀔 수도 있으므로, 변수가 어떤 타입인지를 검사할 때에는 다음과 같은 함수를 사용하는 것이 더 좋습니다.

  

|함수|설명|
|---|---|
|is_array()|전달받은 변수의 타입이 배열인지를 확인함.|
|is_bool()|전달받은 변수의 타입이 논리형인지를 확인함.|
|is_callable()|변수의 내용을 함수처럼 호출할 수 있는지를 확인함.|
|is_float(),is_double(),is_real()|전달받은 변수의 타입이 실수인지를 확인함.|
|is_int(),is_integer(),is_long()|전달받은 변수의 타입이 정수인지를 확인함.|
|is_null()|전달받은 변수의 타입이 NULL인지를 확인함.|
|is_numeric()|전달받은 변수가 수나 숫자로 이루어진 문자열인지를 확인함.|
|is_object()|전달받은 변수의 타입이 객체인지를 확인함.|
|is_resource()|전달받은 변수의 타입이 자원인지를 확인함.|
|is_scalar()|전달받은 변수가 스칼라값인지를 확인함.|
|is_string()|전달받은 변수의 타입이 문자열인지를 확인함.|

> [!important]  
> is_scalar() 함수로 확인할 수 있는 PHP에서의 스칼라값은 integer, float, string, boolean 타입의 값을 의미합니다.PHP에서 array, object, resource 타입의 값은 스칼라값이 아닙니다.  

  

### 변수의 상태 변경

isset() 함수는 전달받은 변수가 선언되어 있는지를 검사합니다.  
선언된 변수가 존재하면 true를, 존재하지 않으면 false를 반환합니다.  

unset() 함수는 전달받은 변수를 제거합니다.

empty() 함수는 전달받은 변수가 비어있는지를 검사합니다.  
전달받은 변수가 존재하고, 해당 변수가 비어있지 않으면 false를 반환합니다.  

PHP에서는 다음과 같은 값을 가지는 변수를 비어있다고 인식합니다.

- 정수 0
- 실수 0.0
- 문자열 "0"
- 빈 문자열 ""
- null
- false
- 빈 배열 array()
- 초기화되지 않은 변수

  

```PHP
$var;
var_dump(isset($var)); // false
var_dump(empty($var)); // true

$var = 5;
var_dump(isset($var)); // true
var_dump(empty($var)); // false 

$var = 0;
var_dump(isset($var)); // true
var_dump(empty($var)); // true

unset($var);
var_dump(isset($var)); // false
var_dump(empty($var)); // true
```

  

위의 예제에서 변수 $var를 선언만 하고 초기화하지 않은 상태에서 isset() 함수에 인수로 전달하면 false를 반환합니다.  
하지만 초기화를 수행한 후에 isset() 함수에 인수로 전달하면 true를 반환합니다.  

단, 정수 0과 같이 비어있는 거로 간주하는 값으로 초기화된 변수는 empty() 함수가 true를 반환합니다.

이때 unset() 함수로 변수 자체를 삭제하고, isset() 함수에 인수로 전달하면 false를 반환합니다.

또한, 선언되지 않거나 삭제된 변수를 empty() 함수에 인수로 전달하면 true를 반환합니다.

이것은 empty() 함수가 내부적으로 다음과 같이 동작하기 때문입니다.

  

> [!important]  
> 문법!isset($var) | $var==false  

즉, empty() 함수는 변수가 존재하지 않거나, false 값을 가질 때 모두 true를 반환합니다.

  

### 특정 타입으로 변경

PHP에서는 변수를 특정 타입으로 변환하기 위해서 다음과 같은 함수를 제공합니다.

intval() 함수는 전달받은 변수에 해당하는 정수를 반환합니다.

floatval() 함수와 doubleval()함수는 전달받은 변수에 해당하는 실수를 반환합니다.

strval()은 전달받은 변수에 해당하는 문자열을 반환합니다.

  

```PHP
$x = "123.56789abc";
echo intval($x);   // 123
echo floatval($x); // 123.56789
echo strval($x);   // 123.56789abc
```

  

## 배열 관련 함수

---

### 배열의 생성

PHP에서 배열을 만들기 위해서는 array() 함수를 사용합니다.

```PHP
$arr = array(1, 2, 3, 4, 5);
```

  

### 배열 요소의 개수

count() 함수와 sizeof() 함수는 배열에 저장된 배열 요소의 개수를 반환합니다.

array_count_values() 함수는 전달받은 배열의 배열 요소 값을 모두 확인하여, 해당 값이 몇 번 등장하는지를 확인합니다.

그 후 배열 요소의 값을 키(key)로 하고, 해당 값의 등장 빈도를 값(value)으로 하는 연관 배열을 반환합니다.

```PHP
$arr = array(1, 5, 7, 3, 3, 1, 2);

echo "배열 요소의 수는 ".count($arr)."입니다.";  // 7echo "배열 요소의 수는 ".sizeof($arr)."입니다."; // 7

$acv = array_count_values($arr);                 // 1 : 2번, 5 : 1번, 7 : 1번, 3 : 2번, 2 : 1번
```

  

### 배열의 탐색

PHP 배열에는 현재 선택된 배열 요소가 어느 요소인지를 가리키는 포인터가 별도로 존재합니다.

이러한 내부 포인터를 배열 포인터라고 하며, 이 포인터는 배열이 생성되면 자동으로 배열의 첫 번째 요소를 가리킵니다.

current() 함수와 pos() 함수는 배열 포인터가 현재 가리키고 있는 요소를 반환합니다.

next() 함수는 우선 배열 포인터를 앞으로 하나 이동시킨 후에, 해당 요소를 반환합니다.

prev() 함수는 next() 함수와는 반대로 우선 배열 포인터를 뒤로 하나 이동시킨 후에, 해당 요소를 반환합니다.

each() 함수는 배열 포인터가 현재 가리키고 있는 요소의 키와 값을 연관 배열로 반환하고, 배열 포인터를 앞으로 하나 이동시킵니다.

reset() 함수는 배열 포인터가 첫 번째 배열 요소를 가리키도록 한 뒤에, 해당 요소의 값을 반환합니다.

end() 함수는 reset() 함수와는 반대로 배열 포인터가 마지막 배열 요소를 가리키도록 한 뒤에, 해당 요소의 값을 반환합니다.

```PHP
$arr = array(2, 3, 7, 4, 6);

$element = current($arr);  // 배열의 첫 번째 요소를 가리킴.
while($element) {          // 배열의 마지막 요소까지
    echo $element;         // 해당 요소의 값을 출력하고,
    $element = next($arr); // 다음 요소를 가리킨 후에 해당 요소를 반환함.
}                          // 2, 3, 7, 4, 6

$element = end($arr);      // 배열의 마지막 요소를 가리킴.
while($element) {          // 배열의 첫 번째 요소까지
    echo $element;         // 해당 요소의 값을 출력하고,
    $element = prev($arr); // 이전 요소를 가리킨 후에 해당 요소를 반환함.
}                          // 6, 4, 7, 3, 2
```

  

### 배열의 정렬

sort() 함수는 배열 요소들을 정렬 기준에 맞게 정렬합니다.

  

sort() 함수의 두 번째 인수로는 배열 요소를 정렬할 기준을 전달할 수 있습니다.

SORT_NUMERIC은 배열 요소를 숫자로 비교하며, SORT_STRING은 문자열로 비교하게 됩니다.

만약 정렬 기준을 전달하지 않으면, 배열 요소들의 타입을 변경하지 않고 그대로 비교하게 됩니다.

  

sort() 함수는 대소문자를 구별하며, 대문자가 소문자보다 앞쪽으로 정렬됩니다.

이 함수는 배열 요소의 정렬에 성공하면 true를 반환하고, 정렬에 실패하면 false를 반환합니다.

```PHP
$arr = array(3, 2, 7, 6, 4);
sort($arr); // 배열 정렬 -> 2, 3, 4, 6, 7

# 다음 예제는 sort() 함수를 호출하면서 정렬 기준을 인수로 함께 전달하는 예제입니다.
$arr = array(15, 2, 1, 21, 121);
① sort($arr, SORT_NUMERIC); // 배열 요소를 숫자로 비교함.   -> 1, 2, 15, 21, 121
② sort($arr, SORT_STRING);  // 배열 요소를 문자열로 비교함. -> 1, 121, 15, 2, 21
```

  

위 예제 ①번 라인의 sort() 함수는 배열 요소를 숫자로 인식하고, 서로를 비교하여 정렬합니다.

하지만 ②번 라인의 sort() 함수는 배열 요소를 문자열로 인식하고 서로를 비교합니다.

문자열끼리의 비교는 우선 첫 번째 문자를 서로 비교합니다.

따라서 첫 번째 문자가 '1'인 배열 요소들이 '2'인 배열 요소보다 앞쪽으로 정렬됩니다.

그다음에는 두 번째 문자를 서로 비교하게 되는데, 이때 두 번째 문자가 없는 배열 요소는 가장 앞쪽으로 정렬됩니다.

따라서 두 번째 문자가 '2'인 121이 두 번째 문자가 '5'인 15보다 앞쪽으로 위치하게 됩니다.

  

### 연관 배열의 정렬

연관 배열은 인덱스를 숫자가 아닌 문자열을 사용하므로, 키와 요소의 값으로 따로 정렬할 수 있습니다.

ksort() 함수는 각 요소의 키를 기준으로 정렬합니다.

또한, asort() 함수는 각 요소의 값을 기준으로 정렬합니다.

```PHP
$arr = array("apple" => 1000, "banana" => 2000, "orange" => 1500);

asort($arr); // 요소의 값을 기준으로 배열 정렬 -> apple, orange, banana
ksort($arr); // 키값을 기준으로 배열 정렬      -> apple, banana, orange
```

  

지금까지 살펴본 sort(), ksort(), asort() 함수는 모두 정렬 기준에 따라 오름차순으로 배열 요소를 정렬합니다.

따라서 배열 요소를 내림차순으로 정렬하기 위해서는 rsort(), krsort(), arsort() 함수를 사용해야만 합니다.

  

|함수|설명|
|---|---|
|array_multisort()|여러 배열이나 다차원 배열의 배열 요소를 정렬함.|
|natcasesort()|대소문자를 구분하지 않는 영문숫자 순(natural order)의 알고리즘으로 배열 요소를 정렬함.|
|natsort()|영문숫자 순(natural order)의 알고리즘으로 배열 요소를 정렬함.|
|usort()|사용자가 정의한 비교 함수를 사용하여, 배열 요소의 값을 기준으로 정렬함.|
|uksort()|사용자가 정의한 비교 함수를 사용하여, 배열 요소의 키를 기준으로 정렬함.|
|uasort()|사용자가 정의한 비교 함수를 사용하여, 인덱스 연관성을 유지한 채 배열 요소를 정렬함.|

  

### 배열 요소의 재배치

shuffle() 함수는 배열 요소를 섞은 뒤에 무작위로 재배치합니다.

```PHP
$arr = array(1, 2, 3, 4, 5);
shuffle($arr);              // 배열 요소를 무작위로 재배치함.

# array_reverse() 함수는 전달받은 배열의 순서를 역순으로 변경한 새로운 배열을 반환합니다.
$arr_01 = array(1, 2, 3, 4, 5);
$arr_02 = array_reverse($arr_01);       // 배열 요소를 역순으로 바꾼 새로운 배열을 반환함.

for($i = 0; $i < count($arr_02); $i++) { // 새로 생성된 배열인 $arr_02의 모든 요소를 출력함.
    echo $arr_02[$i].", ";              // 5, 4, 3, 2, 1
}

for($i = 0; $i < count($arr_01); $i++){ // 원본 배열인 $arr_01의 모든 요소를 출력함.
    echo $arr_01[$i].", ";              // 1, 2, 3, 4, 5
}
```

array_reverse() 함수는 원본 배열에는 영향을 주지 않는 함수입니다.

따라서 원본 배열과 순서가 정반대인 새로운 배열을 생성하여 반환합니다.

  

## 문자열 관련 함수

---

### 문자열의 길이

strlen() 함수는 전달받은 문자열의 길이를 반환합니다.

이때 문자열의 길이란 문자열에 포함된 문자의 개수를 의미합니다.

```PHP
$str = "12345678";
echo strlen($str); // 8
```

  

만약 strlen() 함수에 영문자만이 아닌 한글이 포함된 문자열이 전달되면, 문자열의 길이가 아닌 문자열의 총 바이트(byte) 수를 반환합니다.  
따라서 한글이 포함된 문자열의 정확한 문자열 길이를 반환받기 위해서는 mb_strlen() 함수를 사용해야 합니다.  

mb_strlen() 함수는 문자열뿐만 아니라 두 번째 인수로 인코딩 방식까지 전달받을 수 있습니다.  
이렇게 전달받은 인코딩 방식으로 해당 문자열을 해석하여 정확한 문자열의 길이를 반환해 줍니다.  
만약 두 번째 인수를 전달받지 못하면, 현재 시스템의 내부 인코딩 방식을 사용할 것입니다.  

  

```PHP
$str = "한글로된문자열";

echo strlen($str);             // 7 * 3 = 21
echo mb_strlen($str);          // 7 * 3 = 21
echo mb_strlen($str, "UTF-8"); // 7
```

> [!important]  
> UTF-8 인코딩 방식에서는 영문자는 한 문자당 1바이트, 한글은 한 문자당 3바이트로 표현됩니다.  

  

### 문자열 비교하기

strcmp() 함수는 전달받은 두 개의 문자열을 서로 비교합니다.  
첫 번째 인수의 문자열이 두 번째 인수의 문자열보다 크면 양수를, 작으면 음수를 반환합니다.  
또한, 두 문자열이 완전히 같으면 0을 반환합니다.  

이때 strcmp() 함수는 비교할 때 대소문자를 구분합니다.  
하지만 strncasecmp()함수를 사용하면 대소문자를 구분하지 않고 두 개의 문자열을 비교할 수 있습니다.  

strnatcmp() 함수는 strcmp() 함수와 비슷하며, strnatcasecmp() 함수는 strcasecmp() 함수와 비슷합니다.

차이점으로는 strnatcmp() 함수와 strnatcasecmp() 함수는 영숫자 순(natural ordering)으로 문자열을 비교한다는 점입니다.

  

```PHP
echo strcmp("abc", "ABC");     // 양수
echo strcasecmp("abc", "ABC"); // 0
echo strcmp("2", "10");        // 양수
echo strnatcmp("2", "10");     // 음수
```

위의 예제에서 strcmp() 함수는 "2"를 "10"보다 크다고 인식하지만, strnatcmp() 함수에서는 작다고 인식합니다.

  

### 특정 문자열 검색

strstr()함수와 strchr() 함수는 해당 문자열에서 전달받은 문자열과 처음으로 일치하는 부분을 찾습니다.  
해당 문자열에 일치하는 부분이 존재하면, 처음으로 일치하는 부분을 포함한 이후의 모든 문자를 같이 반환합니다.  

하지만 일치하는 부분이 존재하지 않으면 false를 반환합니다.

strrchr() 함수는 해당 문자열에서 전달받은 문자열과 마지막으로 일치하는 부분을 찾습니다.  
해당 문자열에 일치하는 부분이 존재하면, 마지막으로 일치하는 부분을 포함한 이후의 모든 문자를 같이 반환합니다.  
하지만 일치하는 부분이 존재하지 않으면 false를 반환합니다.  

stristr() 함수는 대소문자를 구분하지 않고 strstr() 함수와 같은 동작을 수행합니다.

```PHP
echo strstr("ABCabcDEFabc", "abc");   // abcDEFabc
echo strrchr("ABCabcDEFabc", "abc")"; // abc
echo stristr("ABCabcDEFabc", "abc");  // ABCabcDEFabc
```

  

### 특정 문자열 위치 찾기

strpos() 함수는 해당 문자열에서 전달받은 문자열과 처음으로 일치하는 부분의 시작 인덱스를 반환합니다.

strrpos() 함수는 해당 문자열에서 전달받은 문자열과 마지막으로 일치하는 부분의 시작 인덱스를 반환합니다.

```PHP
echo strpos("ABCabcDEFabc", "abc");  // 3
echo strrpos("ABCabcDEFabc", "abc"); // 9
```

> [!important]  
> PHP에서 숫자 인덱스는 언제나 0부터 시작합니다.  

  

### 문자열 추출하기

substr() 함수는 해당 문자열에서 특정 인덱스부터 전달받은 길이만큼의 일부분을 추출하여 반환합니다.

전달받은 인덱스가 양수인 경우에는 해당 인덱스부터 해당 문자열의 끝까지를 반환합니다.

만약 전달받은 인덱스가 음수라면 해당 문자열 끝부터 전달받은 음수의 절댓값만큼의 문자열을 반환합니다.

전달받은 길이가 양수인 경우에는 반환할 문자열의 길이를 나타냅니다.

만약 전달받은 길이가 음수라면 특정 인덱스부터 문자열 끝부터 전달받은 음수의 절댓값까지의 문자열을 반환합니다.

```PHP
$str = "Hello, World!";
echo substr($str, 3);     // 네 번째 문자부터 끝까지 출력
echo substr($str, -3);    // 끝에서부터 세 글자 출력
echo substr($str, 1, 5);  // 두 번째 문자부터 다섯 글자 출력
echo substr($str, 1, -5); // 두 번째 문자부터 뒤에서 여섯 번째 문자까지 출력
```

  

### 문자열 대소문자 바꾸기

strtolower() 함수는 전달받은 문자열의 모든 문자를 소문자로 바꿔줍니다.

또한, strtoupper() 함수는 전달받은 문자열의 모든 문자를 대문자로 바꿔줍니다.

ucfirst 함수()는 전달받은 문자열의 첫 번째 문자만을 대문자로 바꿔줍니다.

또한, ucwords() 함수는 전달받은 문자열에서 단어별로 첫 번째 문자만을 대문자로 바꿔줍니다.

```PHP
echo strtolower("HELLO, WORLD!"); // 모두 소문자로 바꿈.
echo strtoupper("hello, world!"); // 모두 대문자로 바꿈.
echo ucfirst("hello, world!");    // 문자열의 첫 번째 문자만 대문자로 바꿈.
echo ucwords("hello, world!");    // 각 단어의 첫 번째 문자를 대문자로 바꿈.
```

  

### 문자열 합치고 나누기

explode() 함수는 특정 문자를 기준으로 전달받은 문자열을 나누어서 하나의 배열로 반환합니다.

implode() 함수와 join() 함수는 전달받은 배열의 각 요소를 특정 문자를 사용하여 하나로 합쳐친 문자열로 반환합니다.

strtok() 함수는 전달받은 문자열을 특정 문자를 기준으로 토큰화합니다.

이 함수는 해당 문자열을 한 번에 모두 나누지 않고, 한 번에 하나씩만을 토큰화합니다.

첫 번째 토큰을 얻기 위해서는 strtok() 함수에 인수로 해당 문자열과 기준이 되는 문자를 함께 전달하면 됩니다.

그 이후에는 기준이 되는 문자만을 전달해주면 자동으로 두 번째 토큰을 반환합니다.

```PHP
$str = "hello, beautiful, world!";

$array = explode(',', $str);  // ','를 기준으로 문자열을 나눔.
echo $array[0];               // hello

echo $array[1];               // beautiful
echo $array[2];               // world!

$str2 = implode('!', $array); // '!'를 기준으로 문자열을 결합함.
echo $str2;                   // hello! beautiful! world!

$token = strtok($str2, '!');  // '!'를 기준으로 토큰화
echo $token;                  // hello
while($token != ""){          // 문자열이 끝날 때까지
    $token = strtok('!');     // '!'를 기준으로 토근화하고 출력함.
    echo $token;              // beautiful, world
}
```

  

### 문자열 대체하기

str_replace() 함수는 해당 문자열에서 전달받은 문자열을 모두 찾은 후에, 찾은 문자열을 대체 문자열로 교체합니다.

substr_replace() 함수는 해당 문자열에서 특정 위치의 문자들을 대체 문자열로 교체합니다.

substr_replace() 함수는 해당 문자열에서 교체를 시작할 부분의 인덱스를 세 번째 인수로 전달받습니다.

전달받은 인덱스가 0 또는 양수인 경우에는 해당 문자열의 앞에서부터, 음수인 경우에는 뒤에서부터 시작 인덱스를 찾습니다.

또한, 선택 사항으로 해당 문자열에서 교체할 부분의 길이를 네 번째 인수로 전달받을 수 있습니다.  
이때 길이를 전달하지 않으면 시작 인덱스부터 해당 문자열의 끝까지 모두 대체됩니다.  

전달된 길이가 양수이면, 시작 인덱스부터 교체할 글자의 개수를 나타냅니다.  
하지만 전달된 길이가 음수이면, 시작 인덱스부터 문자열 끝부터 음수의 절댓값까지의 문자열을 대체 문자열로 대체합니다.  
만약 길이로 0이 전달되면, 해당 문자열의 시작 인덱스에 대체 문자열을 삽입합니다.  

```PHP
$str = "hello, world!";
echo str_replace('o', '*', $str);      // 문자열의 모든 'o'를 '*'로 대체함.
echo substr_replace($str, '*', 2);     // 세 번째 문자부터 끝까지를 '*'로 대체함.
echo substr_replace($str, '*', -2);    // 끝에서 두 번째 문자부터 끝까지를 '*'로 대체함.
echo substr_replace($str, '*', 2, 4);  // 세 번째 문자부터 네 글자를 '*'로 대체함.
echo substr_replace($str, '*', 2, -4); // 세 번째 문자부터 끝에서 다섯 번째 문자까지를 '*'로 대체함.
echo substr_replace($str, '*', 2, 0);  // 두 번째 문자 뒤에 '*'을 삽입함.
```

  

### 문자열 다듬기

ltrim() 함수는 문자열 앞부분에 있는 공백을 제거하고, rtrim() 함수와 chop() 함수는 문자열 끝부분에 있는 공백을 제거합니다.

또한, trim() 함수는 문자열의 처음과 끝부분에 있는 공백을 모두 제거합니다.

이 함수들이 제거하는 문자는 다음과 같습니다.

- 띄어쓰기 " "
- 탭 문자 "\t"
- 줄 바꿈 문자 "\n", "\r"
- 널 문자 "\0"
- 수직 탭 문자 "\x0B"

  

```PHP
$str = "  hello, world!  ";
echo "'".ltrim($str)."'<br/>"; // 문자열의 처음 부분 공백을 모두 지움. 
echo "'".rtrim($str)."'<br/>"; // 문자열의 끝부분 공백을 모두 지움.
echo "'".trim($str)."'";       // 문자열의 처음과 끝부분 공백을 모두 지움.
```

  

## 날짜와 시간 관련 함수

---

### 날짜와 시간의 형식화

date() 함수는 전달받은 형식에 맞춰 날짜와 시간 정보를 문자열로 반환합니다.

date() 함수에 인수로 전달할 수 있는 날짜와 시간 표현의 형식은 다음과 같습니다.

  

|형태|설명|예시|
|---|---|---|
|d|날짜를 두 자리 숫자로 표현함.|00부터 31|
|D|요일을 세 개의 문자로 표현함.|Mon에서 Sun|
|j|날짜를 숫자로 표현함.|1부터 31|
|l(소문자 'L')|요일을 완전한 문자열로 표현함.|Sunday부터 Saturday|
|N|요일을 ISO-8601 숫자로 표현함. (PHP 5.1.0에서 추가됨)|1(월요일)부터 7(일요일)|
|S|날짜 뒤에 영어 서수를 붙임.|st, nd, rd, th, j|
|w|요일을 숫자로 표현함.|0(일요일)부터 6(토요일)|
|z|일 년 중 몇 번째 날인지를 숫자로 표현함.|0부터 365|
|W|일 년 중 몇 번째 주인지를 숫자로 표현함. (PHP 4.1.0에서 추가됨)|42(그 해의 42번째 주)|
|F|월을 완전한 문자열로 표현함.|January에서 December|
|m|월을 두 자리 숫자로 표현함.|01부터 12|
|M|월의 축약형을 세 개의 문자로 표현함.|Jan에서 Dec|
|n|월을 숫자로 표현함.|1부터 12|
|t|해당 월의 총일 수를 숫자로 표현함.|28부터 31|
|L|윤년 여부를 표현함.|윤년엔 1, 그 외엔 0|
|o|ISO-8601 연도값으로 Y값과 같은 값을 나타냄.하지만, W값이 이전 해나 다음 해에 포함되면, 연도를 이 값으로 사용함.(PHP 5.1.0에서 추가됨)|1999나 2003|
|Y|연도를 완전한 네 자리 숫자로 표현함.|1999나 2003|
|y|연도를 두 자리 숫자로 표현함.|99나 03|
|a|오전과 오후의 소문자를 표현함.|am 또는 pm|
|A|오전과 오후의 대문자를 표현함.|AM 또는 PM|
|B|견본 인터넷 시간을 표현함.|000에서 999|
|g|12시간 형식으로 시간을 표현함.|1부터 12|
|G|24시간 형식으로 시간을 표현함.|0부터 23|
|h|12시간 형식 시간을 두 자리 숫자로 표현함.|01부터 12|
|H|24시간 형식 시간을 두 자리 숫자로 표현함.|00부터 23|
|i|분을 두 자리 숫자로 표현함.|00부터 59|
|s|초를 두 자리 숫자로 표현함.|00부터 59|
|u|초를 마이크로초로 표현함. (PHP 5.2.2에서 추가됨)|54321|
|e|시간대(timezone) 식별자를 표현함. (PHP 5.1.0에서 추가됨)|UTC, GMT|
|I(대문자 i)|서머타임 적용 여부를 표현함.|서머타임이면 1, 아니면 0|
|O|그리니치 시각(GMT)과 시차를 표현함.|+0200|
|P|시와 분 사이에 콜론이 들어가는 그리니치 시각(GMT)과 시차를 표현함.|+02:00|
|T|시간대(timezone)를 나타내는 축약어임.|EST, MDT|
|Z|시간대(timezone)를 나타내는 오프셋 초를 표현함.UTC 서쪽은 항상 음수, UTC 동쪽은 항상 양수로 표현됨.|-43200부터 50400|
|c|ISO-8601 형식의 날짜를 표현함. (PHP 5에서 추가됨)|2004-02-12T15:19:21+00:00|
|r|RFC 2822 형식의 날짜를 표현함.|Thu, 21 Dec 2000 16:01:07 +0200|
|U|타임스탬프를 표현함.|time() 참조|

  

타임스탬프란 GMT 기준 1970년 1월 1일 0시 0분부터 지금까지의 시간을 초(second) 단위로 나타낸 것입니다.

date() 함수에서는 두 번째 인수로 타임스탬프값을 전달하지 않아도 되며, 이때는 현재 날짜와 시간을 사용하게 됩니다.

```PHP
echo date("Y/m/d h:i:s");
```

  

### 타임스탬프(timestamp)

mktime() 함수는 시, 분, 초, 월, 일, 연도를 인수로 전달받아서, 해당 날짜와 시간을 나타내는 타임스탬프(timestamp)를 반환합니다.

time() 함수는 인수를 전달받지 않고, 현재 날짜와 시간에 대한 타임스탬프를 반환합니다.

```PHP
echo mktime(0, 0, 0, 1, 1, 2000)."<br>";  // 2000년 1월 1일을 나타내는 타임스탬프
echo mktime()."<br>";                     // 현재 날짜와 시간을 나타내는 타임스탬프
echo time();                              // 현재 날짜와 시간을 나타내는 타임스탬프
```

  

mktime() 함수는 호출할 때 인수를 시, 분, 초, 월, 일, 연도순으로 전달해야 하며, 오른쪽부터 차례대로 생략할 수 있습니다.

이 함수에 인수를 전달하지 않으면, 현재 날짜와 시간에 대한 타임스탬프 값을 반환하며, 따라서 time() 함수와 같은 동작을 하게 됩니다.

  

### 날짜와 시간 정보

getdate() 함수는 인수로 전달받은 타임스탬프에 해당하는 정보를 연관 배열의 형태로 반환합니다.

getdate() 함수가 반환하는 연관 배열의 키와 값은 다음과 같습니다.

  

|키|값|
|---|---|
|seconds|해당 타임스탬프에 해당하는 초를 숫자로 저장함.|
|minutes|해당 타임스탬프에 해당하는 분을 숫자로 저장함.|
|hours|해당 타임스탬프에 해당하는 시간을 숫자로 저장함.|
|mday|해당 타임스탬프에 해당하는 일을 숫자로 저장함.|
|wday|해당 타임스탬프에 해당하는 요일을 숫자로 저장함.|
|mon|해당 타임스탬프에 해당하는 월을 숫자로 저장함.|
|year|해당 타임스탬프에 해당하는 연도를 네 자리의 숫자로 저장함.|
|yday|해당 타임스탬프에 해당하는 일자가 일 년 중 몇 번째 날인지를 숫자로 저장함.|
|weekday|해당 타임스탬프에 해당하는 요일을 완전한 문자열로 저장함.|
|month|해당 타임스탬프에 해당하는 월을 완전한 문자열로 저장함.|
|0|타임스탬프값을 저장함.|

  

인수를 전달하지 않으면 현재 날짜와 시간의 타임스탬프를 반환합니다.

```PHP
$array = getdate();

foreach ($array as $key => $value) {
    echo $key." ".$value."<br>";
}
```

  

### 타임 존(Time zone)

date_default_timezone_set() 함수는 해당 스크립트에서 사용되는 날짜와 시간에 관련된 모든 함수에서 사용될 타임 존을 설정합니다.

date_default_timezone_get() 함수는 현재 설정되어 있는 타임 존을 반환합니다.

```PHP
echo date_default_timezone_get()." : ".date("h:i:s"); // 현재 타임 존과 시간을 받아옴.
date_default_timezone_set("America/Los_Angeles");     // 타임 존을 변경함.
echo date_default_timezone_get()." : ".date("h:i:s");
```

> [!important]  
> 이 두 함수는 PHP 5.1.0부터 추가된 함수입니다.  

  

### 날짜의 유효성 검사

checkdate() 함수는 전달받은 날짜의 유효성을 검사합니다.  
이 함수에 인수로 월, 일, 연도를 전달하면, 해당 날짜가 유효한 날짜인지를 확인해 줍니다.  
이 함수는 윤년까지 고려하여 다음과 같은 사항들을 검사합니다.  

  

1. 월이 1월부터 12월까지인지를 검사합니다.
2. 일자가 해당 월에 존재하는 날짜인지를 검사합니다.
3. 연도가 0에서 32767까지의 정수인지를 검사합니다.

  

만약 전달받은 날짜가 유효하다면 true를 반환하고, 유효하지 않다면 false를 반환합니다.

```PHP
var_dump(checkdate(1, 31, 2000)); // 유효한 날짜
var_dump(checkdate(2, 31, 2000)); // 유효하지 않은 날짜
```

  

## 수학 관련 함수

---

### 최댓값과 최솟값

max() 함수는 전달받은 수 중에서 가장 큰 수를 반환하며, min() 함수는 가장 작은 수를 반환합니다.

```PHP
echo "1, 5, 7, 3, 2 중 가장 큰 값은 ".max(1, 5, 7, 3, 2)."입니다.";
echo "1, 5, 7, 3, 2 중 가장 작은 값은 ".min(1, 5, 7, 3, 2)."입니다.";
```

  

### 올림과 내림

floor() 함수는 인수로 전달받은 값과 같거나 작은 수 중에서 가장 큰 정수를 반환합니다.

또한, ceil() 함수는 반대로 인수로 전달받은 값과 같거나 큰 수 중에서 가장 작은 정수를 반환합니다.

PHP에서 소수점에서의 반올림은 round() 함수를 사용하여 수행할 수 있습니다.

```PHP
echo floor(10.95);  // 10 
echo floor(11.01);  // 11
echo floor(-10.95); // -11
echo floor(-11.01); // -12

echo ceil(10.95);   // 11
echo ceil(11.01);   // 12
echo ceil(11);      // 11
echo ceil(-10.95);  // -10
echo ceil(-11.01);  // -11

echo round(10.49);  // 10
echo round(10.5);   // 11
echo round(-10.5);  // -11
echo round(-10.51); // -11
```

> [!important]  
> floor(), ceil(), round() 함수의 반환값은 인수로 음수를 전달받을 때 특히 유의해서 고려해야 합니다.  

  

### 지수와 로그

pow() 함수는 전달받은 수의 거듭제곱을 반환합니다.

첫 번째 인수로는 밑수를 전달하고, 두 번째 인수로는 지수를 전달합니다.

exp() 함수는 인수로 지수를 전달받아, e의 거듭제곱을 계산하여 반환합니다.

log() 함수는 전달받은 수의 자연로그 값을 계산하여 반환합니다.

```PHP
echo "2의 3제곱은 ".pow(2, 3)."입니다.";
echo "e의 3제곱은 ".exp(3)."입니다.";
echo "log3은 ".log(3)."입니다.";
```

  

### 삼각 함수

PHP에서는 스크립트에서 간단히 삼각 함수를 사용할 수 있습니다.

sin() 함수는 전달받은 수의 사인값을, cos() 함수는 코사인값을, tan() 함수는 탄젠트값을 반환합니다.

```PHP
echo "sin3.14는 ".sin(pi()/2)."입니다."; // sin(π/2) == 1
echo "cos3.14는 ".cos(M_PI)."입니다.";   // cos(π) == -1
echo "tan3.14는 ".tan(M_PI/4)."입니다."; // tan(π/4) == 1
```

> [!important]  
> pi() 함수는 파이(π) 값을 반환하며, M_PI 상수와 같은 값을 반환합니다.  

  

### 기타 함수

abs() 함수는 전달받은 수의 절댓값을 반환합니다.

rand() 함수는 0보다 크거나 같고 getrandmax() 함수의 반환값보다 작은 하나의 정수를 무작위로 생성하여 반환합니다.

```PHP
echo "-3의 절댓값은 ".abs(-3)."입니다.";
echo "0부터 ".getrandmax()"까지의 정수를 하나 무작위로 생성합니다 : ".rand();
```

> [!important]  
> getrandmax() 함수는 rand() 함수로 생성할 수 있는 정수의 최댓값을 나타냅니다.