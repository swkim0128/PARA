## 1. if-else

if-else는 조건에 따라 코드를 실행하거나 다른 경로를 선택할 수 있도록 합니다. 코틀린의 if 문은 표현식으로 사용할 수 있어 값을 반환합니다.

### 기본 문법

```kotlin
if (조건) {
    // 조건이 참일 때 실행_
} else {
    // 조건이 거짓일 때 실행_
}
```

### 1. 조건에 따른 실행

```kotlin
fun main() {
    val num = 10

    if (num > 0) {
        println("Positive number")
    } else if (num == 0) {
        println("Zero")
    } else {
        println("Negative number")
    }
}
```

### 2. 표현식으로 사용

if 문을 표현식으로 사용하여 값을 반환할 수 있습니다.

```kotlin
fun main() {
    val num = 10
    val result = if (num > 0) {
        "Positive"
    } else {
        "Negative"
    }

    println(result) _// 출력: Positive_
}
```

### 3. 단일 조건 처리

중괄호 {}는 단일 구문일 경우 생략할 수 있습니다.

```kotlin
val num = 5
if (num % 2 == 0) println("Even") else println("Odd")
```

## 2. when

when은 자바의 switch 문과 유사하며, 더 강력하고 간결한 조건문입니다. 단일 값, 범위, 타입 등 다양한 조건을 처리할 수 있습니다.

### 기본 문법

```kotlin
when (값) {
    조건1 -> 실행할 코드
    조건2 -> 실행할 코드
    else -> 실행할 코드 (기본값, 생략 가능)
}
```

### 1. 값에 따라 처리

```kotlin
fun main() {
    val num = 2

    when (num) {
        1 -> println("One")
        2 -> println("Two")
        3 -> println("Three")
        else -> println("Other")
    }
}
```

### 2. 범위 사용

in 키워드를 사용하여 값이 특정 범위에 속하는지 확인할 수 있습니다.

```kotlin
fun main() {
    val num = 15

    when (num) {
        in 1..10 -> println("1부터 10 사이의 숫자")
        in 11..20 -> println("11부터 20 사이의 숫자")
        else -> println("20 이상의 숫자")
    }
}
```

### 3. 여러 조건을 묶어서 처리

쉼표(,)로 조건을 나열하여 동일한 결과를 처리할 수 있습니다.

```kotlin
fun main() {
    val num = 2

    when (num) {
        1, 3, 5, 7, 9 -> println("Odd number")
        2, 4, 6, 8, 10 -> println("Even number")
        else -> println("Not between 1 and 10")
    }
}
```

### 4. 타입 검사

is 키워드를 사용하여 값의 타입을 검사할 수 있습니다.

```kotlin
fun main() {
    val value: Any = "Hello"

    when (value) {
        is String -> println("It is a String with length ${value.length}")
        is Int -> println("It is an Integer")
        else -> println("Unknown type")
    }
}
```

### 5. 표현식으로 사용

when도 if와 마찬가지로 값을 반환할 수 있습니다.

```kotlin
fun main() {
    val num = 3

    val result = when (num) {
        1 -> "One"
        2 -> "Two"
        else -> "Unknown"
    }

    println(result) // 출력: Unknown
}
```

## 3. if-else와 when의 비교

| 특징        | if-else   | when                    |
| --------- | --------- | ----------------------- |
| 사용 용도     | 간단한 조건 처리 | 여러 조건 처리, 값에 따른 분기      |
| 표현식 사용 여부 | 가능        | 가능                      |
| 복잡한 조건 처리 | 어려움       | 다양한 조건(값, 범위, 타입) 처리 가능 |

## 요약

1. if-else

- 간단한 조건을 처리하거나 표현식으로 값을 반환할 때 사용.
- 중첩 조건이 많아질수록 코드가 복잡해질 수 있음.

2. when

- 다중 조건을 처리하거나 값, 범위, 타입에 따라 분기할 때 사용.
- 간결하고 가독성이 뛰어나며 switch 문보다 강력함.

코틀린에서는 상황에 따라 if-else와 when을 적절히 활용하여 코드의 가독성과 효율성을 높일 수 있습니다.
