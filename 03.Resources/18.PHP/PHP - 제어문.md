---
type: PHP
archive: false
---
## 조건문

---

### PHP 표현식

표현식(expressions)은 PHP에서 가장 중요한 구성요소입니다.

표현식이란 모든 것이 값을 갖는다는 의미이며, PHP에서 사용하는 거의 모든 것이 표현식에 속합니다.

표현식에는 변수와 상수, 함수까지도 포함되며, 제어문이나 명령문도 모두 표현식에 속합니다.

  

### 제어문

표현식 중에서도 프로그램의 순차적인 흐름을 제어해야 할 때 사용하는 명령문을 제어문이라고 합니다.

이러한 제어문에는 조건문, 반복문 등이 포함됩니다.

  

### 조건문

조건문이란 프로그램 내에서 주어진 조건식의 결과에 따라 별도의 명령을 수행하도록 제어하는 명령문입니다.

조건문 중에서 가장 기본이 되는 명령문은 if 문입니다.

---

  

### if 문

if 문은 조건식의 결과가 참(true)이면 주어진 명령문을 실행하며, 거짓(false)이면 아무것도 실행하지 않습니다.

> [!important]  
> 문법if (조건식) {  조건식의 결과가 참일 때 실행하고자 하는 명령문;}  

```PHP
$num_01 = 10;
$num_02 = 20;
if ($num_01 == $num_02) {
    echo "{$num_01}과 {$num_02}은 같은 수입니다.";
}
if ($num_01 < $num_02) {
    echo "{$num_01}은 {$num_02}보다 작은 수입니다.";
}
if ($num_01 > $num_02) // 실행될 명령문이 한 줄뿐이라면 중괄호({})를 생략할 수 있음.
    echo "{$num_01}은 {$num_02}보다 큰 수입니다.";
```

  

### else 문

if 문과 같이 사용할 수 있는 else 문은 if 문의 조건식 결과가 거짓(false)일 때 주어진 명령문을 실행합니다.

> [!important]  
> 문법if (조건식) {    조건식의 결과가 참일 때 실행하고자 하는 명령문;} else {    조건식의 결과가 거짓일 때 실행하고자 하는 명령문;}  

```PHP
$num_01 = 20;
$num_02 = 20;
if ($num_01 == $num_02) {
    echo "{$num_01}과 {$num_02}은 같은 수입니다.";
}
else {
    if ($num_01 < $num_02)
        echo "{$num_01}은 {$num_02}보다 작은 수입니다.";
    else // $num_01 > $num_02
        echo "{$num_01}은 {$num_02}보다 큰 수입니다.";
}
```

  

### elseif 문

elseif 문은 if 문처럼 조건식을 설정할 수 있으므로, 중첩된 if 문을 좀 더 간결하게 표현할 수 있습니다.

하나의 조건문 안에서 if 문과 else 문은 단 한 번만 사용될 수 있습니다.

하지만 elseif 문은 여러 번 사용되어 다양한 조건을 설정할 수 있습니다.

  

> [!important]  
> C언어에서는 else if 문을 작성할 때 else와 if 사이에 반드시 공백이 있어야 합니다.하지만 PHP에서는 elseif와 else if를 둘 다 사용할 수 있습니다.  
  
> [!important]  
> 문법if (조건식1) {    조건식1의 결과가 참일 때 실행하고자 하는 명령문;}elseif (조건식2) {    조건식2의 결과가 참일 때 실행하고자 하는 명령문;}else {    조건식1의 결과도 거짓이고, 조건식2의 결과도 거짓일 때 실행하고자 하는 명령문;}  

```PHP
$num_01 = 30;
$num_02 = 20;
if ($num_01 == $num_02) {
    echo "{$num_01}과 {$num_02}은 같은 수입니다.";
}
elseif ($num_01 < $num_02) {
    echo "{$num_01}은 {$num_02}보다 작은 수입니다.";
}
else { // $num_01 > $num_02
    echo "{$num_01}은 {$num_02}보다 큰 수입니다.";
}
```

  

### 삼항 연산자에 의한 조건문

PHP에서는 C언어와 마찬가지로 간단한 if / else 문을 삼항 연산자를 이용하여 간단히 표현할 수 있습니다.

  

### switch 문

switch 문은 if / else 문과 마찬가지로 주어진 조건 값에 따라 프로그램이 다른 명령을 수행하도록 하는 조건문입니다.

이러한 switch 문은 if / else 문보다 가독성 측면에서 더 좋습니다.

  

> [!important]  
> 문법switch (조건 값) {    case 값1:        조건 값이 값1일 때 실행하고자 하는 명령문;        break;    case 값2:        조건 값이 값2일 때 실행하고자 하는 명령문;        break;    ...    default:        해당 case가 없을 때 실행하고자 하는 명령문;        break;}  

```PHP
$var = "오렌지";
switch ($var) {
    case "귤":
        echo "여기 있는 과일은 귤입니다.";
        break;
    case "사과":
        echo "여기 있는 과일은 사과입니다.";
        break;
    case "바나나":
        echo "여기 있는 과일은 바나나입니다.";
        break;
    default:
        echo "여기 있는 과일은 처음 보는 과일입니다.";
        break;
}
```

```PHP
$var = "아보카도";
switch ($var) {
    case "귤":
    case "사과":
    case "바나나":
    case "아보카도":
        echo "여기 있는 과일은 제가 먹어본 과일입니다.";
        break;
    case "파파야":
    case "두리안":
    case "석가":
        echo "여기 있는 과일은 제가 먹어보지 못한 과일입니다.";
        break;
    default:
        echo "여기 있는 것은 과일이 아닙니다.";
        break;
}
```

  

## 반복문

---

### 반복문

반복문이란 프로그램 내에서 같은 명령을 일정 횟수만큼 반복하여 수행하는 명령문입니다.

프로그램이 처리하는 대부분의 코드는 반복적인 형태가 많으므로, 반복문은 가장 많이 사용되는 명령문 중 하나입니다.

PHP에서 사용되는 대표적인 반복문의 형태는 다음과 같습니다.

1. while 문
2. do / while 문
3. for 문
4. foreach 문

  

### while 문

while 문은 특정 조건을 만족할 때까지 계속 주어진 명령문을 반복해서 실행하는 명령문입니다.

while 문을 순서도로 표현하면 다음 그림과 같이 표현할 수 있습니다.

[![](http://www.tcpschool.com/lectures/img_c_while.png)](http://www.tcpschool.com/lectures/img_c_while.png)

  

> [!important]  
> 문법while (조건식) { 조건식의 결과가 참인 동안 반복적으로 실행하고자 하는 명령문;}  

```PHP
$i = 0;
while ($i < 5) {
    echo ($i++)."<br>";
}
```

  

### do / while 문

while 문은 루프에 진입하기 전에 먼저 표현식부터 검사합니다.

하지만 do / while 문은 먼저 루프를 한 번 실행한 후에 표현식을 검사합니다.

즉, do / while 문은 표현식의 결과와 상관없이 무조건 한 번은 루프를 실행합니다.

do / while 문을 순서도로 표현하면 다음 그림과 같습니다.

[![](http://www.tcpschool.com/lectures/img_c_dowhile.png)](http://www.tcpschool.com/lectures/img_c_dowhile.png)

  

> [!important]  
> 문법do {    조건식의 결과가 참인 동안 반복적으로 실행하고자 하는 명령문;} while (조건식);  

```PHP
$i = 0;
$j = 0;
while ($i > 5) {
    echo "변수 i의 값은 ".(++$i)."입니다.<br>";
}
do { // do / while문은 조건식과 상관없이 반드시 한 번은 루프를 실행함
    echo "변수 j의 값은 ".(++$j)."입니다.<br>";
} while ($j > 5);
```

  

### for 문

for 문은 while 문과는 달리 자체적으로 초기식, 표현식, 증감식을 모두 포함하고 있는 반복문입니다.

따라서 while 문보다는 좀 더 간결하게 반복문을 표현할 수 있습니다.

for 문을 순서도로 표현하면 다음 그림과 같이 표현할 수 있습니다.

[![](http://www.tcpschool.com/lectures/img_c_for.png)](http://www.tcpschool.com/lectures/img_c_for.png)

  

> [!important]  
> 문법for (초기식; 조건식; 증감식) {    조건식의 결과가 참인 동안 반복적으로 실행하고자 하는 명령문;}  

```PHP
for ($i = 0; $i < 5; $i++) {
    echo "{$i}<br>";
}
```

  

### foreach 문

foreach 문은 일반적인 for 문과는 전혀 다른 형태의 반복문입니다.

foreach 문은 배열의 모든 요소를 손쉽게 순회할 수 있도록 해줍니다.

이 반복문은 루프마다 배열의 각 요소를 지정된 변수에 대입합니다.

이렇게 대입받은 변수를 이용하면 루프 안에서 배열의 각 요소에 순차적으로 접근할 수 있습니다.

따라서 foreach 문은 정확히 배열의 길이(length)만큼 반복됩니다.

  

> [!important]  
> 문법foreach (배열 as 값을저장할변수) {    실행하고자 하는 명령문;}  

```PHP
$arr = array(2, 4, 6, 8);
foreach ($arr as $value) {
    echo "변수 \$value의 현재값은 {$value}입니다.<br>";
}
unset($value);
```

> [!important]  
> 위의 예제에서 변수 $value는 foreach 문 내에서만 사용하는 변수입니다.따라서 foreach 문이 끝난 뒤에는 unset() 함수를 사용하여 해제해 주는 것이 좋습니다.  

  

```PHP
$arr = array(
    "둘" => 2,
    "넷" => 4,
    "여섯" => 6,
    "여덟" => 8,
);
foreach ($arr as $key => $value) {
    echo "배열 \$arr에서 키값 '{$key}'에 대한 값은 {$value}입니다.<br>";
}
unset($value);
```

  

## 기타 제어문

---

### 루프의 제어

일반적으로 조건식의 검사를 통해 루프로 진입하면, 다음 조건식을 검사하기 전까지 루프 안에 있는 모든 명령문을 실행합니다.

사용자는 continue 문과 break 문을 통해, 이러한 일반적인 루프의 흐름을 직접 제어할 수 있습니다.

  

### continue 문

continue 문은 루프 내에서 사용하여 해당 루프의 나머지 부분을 건너뛰고, 바로 다음 조건식의 판단으로 넘어가게 합니다.

보통 반복문 내에서 특정 조건에 대한 처리를 제외하고자 할 때 자주 사용됩니다.

> [!important]  
> 다른 언어와는 달리 PHP에서는 switch 문에도 continue를 사용할 수 있어, switch 문을 반복문처럼 사용할 수 있습니다.  

  

```PHP
$exceptNum = 4;
for ($i=0; $i<=100; $i++) {
    if ($i % $exceptNum == 0)
        continue;
    echo "{$i} ";
}
```

  

### break 문

break 문은 루프 내에서 사용합니다.

해당 반복문을 완전히 종료시키고, 반복문 다음에 위치한 명령문으로 이동시킵니다.

즉, 루프 내에서 조건식의 판단 결과에 상관없이, 반복문을 완전히 빠져나가고 싶을 때 사용합니다.

  

```PHP
$sum = 0;
$startNum = 1;
$endNum = 100;
$i = $startNum;
while (true) { // 일부러 만든 무한 루프임.
    $sum += $i;
    if ($i == $endNum)
        break;
    $i++;
}
echo "{$startNum}에서부터 {$endNum}까지 더한 값은 {$sum}입니다.";
```

  

### goto 문

goto 문은 프로그램의 흐름을 지정된 레이블(label)로 무조건 변경하는 명령문입니다.

goto 문은 다른 제어문과는 다르게 아무 조건 없이 제어를 옮겨줍니다.

따라서 가장 손쉽게 사용할 수 있지만, 반면에 프로그램의 흐름을 매우 복잡하게 만들기도 합니다.

이러한 단점 때문에 현재는 거의 사용하지 않습니다.

  

### 제어문의 대체 문법

PHP는 제어문을 위해 사용할 수 있는 또 하나의 대체 문법을 제공하고 있습니다.

이 대체 문법은 조건문에서는 if 문과 switch 문, 반복문에서는 while 문, for 문과 foreach 문에 사용할 수 있습니다.

대체 문법의 사용 방법은 우선 제어문의 여는 괄호({)를 콜론(:)으로 대체합니다.

그리고 닫는 괄호(})를 각각 endif;, endswitch;, endwhile;, endfor;, endforeach;로 대체하면 됩니다.

```PHP
<?php $var = 5; ?>
<?php if ($var > 6): ?>
변수의 값은 6보다 큽니다.   <!-- 이 부분은 HTML 구문임 -->
<?php elseif ($var == 6): ?>
변수의 값은 6입니다.        <!-- 이 부분은 HTML 구문임 -->
<?php elseif ($var < 6): ?>
변수의 값은 6보다 작습니다. <!-- 이 부분은 HTML 구문임 -->
<?php endif; ?>
```