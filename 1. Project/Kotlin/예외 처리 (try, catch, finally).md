## 1. try-catch 블록

- try 블록에서 실행 중 예외(Exception)가 발생하면, catch 블록이 실행됩니다.
- 하나 이상의 catch 블록을 사용할 수 있으며, 특정 예외를 처리할 수도 있습니다.

### 기본 문법

```kotlin
try {
    // 예외가 발생할 수 있는 코드
} catch (e: ExceptionType) {
    // 예외 처리 코드
}
```

### 1. 기본 사용

```kotlin
fun main() {
    try {
        val result = 10 / 0 // ArithmeticException 발생
    } catch (e: ArithmeticException) {
        println("예외 발생: ${e.message}")
    }
}
```

출력:

```text
예외 발생: / by zero
```

### 2. 여러 catch 블록 사용

- 다양한 유형의 예외를 처리할 수 있습니다.

```kotlin
fun main() {
    try {
        val numbers = listOf(1, 2, 3)
        println(numbers[5]) // IndexOutOfBoundsException 발생
    } catch (e: IndexOutOfBoundsException) {
        println("인덱스가 잘못되었습니다: ${e.message}")
    } catch (e: Exception) {
        println("기타 예외 발생: ${e.message}")
    }
}
```

### 3. 예외의 부모 타입 처리

- 예외는 계층 구조를 가지며, 부모 타입의 catch 블록이 하위 타입의 예외를 처리할 수 있습니다.

```kotlin
fun main() {
    try {
        val result = "Kotlin".toInt() // NumberFormatException 발생
    } catch (e: Exception) {
        println("예외 발생: ${e.message}")
    }
}
```

## 2. finally 블록

- finally 블록은 예외 발생 여부와 관계없이 항상 실행됩니다.
- 주로 자원 해제나 정리 작업을 수행할 때 사용됩니다.

### 기본 문법

```kotlin
try {
    // 예외가 발생할 수 있는 코드
} catch (e: ExceptionType) {
    // 예외 처리 코드
} finally {
    // 항상 실행되는 코드
}
```

### 1. finally 사용

```kotlin
fun main() {
    try {
        val result = 10 / 2
        println("결과: $result")
    } catch (e: Exception) {
        println("예외 발생")
    } finally {
        println("프로그램 종료")
    }
}
```

**출력**:

```text
결과: 5
프로그램 종료
```

### 2. 예외가 발생했을 때의 finally

```kotlin
fun main() {
    try {
        val result = 10 / 0 _// 예외 발생_
    } catch (e: ArithmeticException) {
        println("예외 발생: ${e.message}")
    } finally {
        println("항상 실행됩니다.")
    }
}
```

출력:

```text
예외 발생: / by zero
항상 실행됩니다.
```

## 3. try 표현식

- 코틀린의 try는 **표현식**으로 사용할 수 있으며, 값을 반환할 수 있습니다.
- 예외가 발생하지 않으면 try 블록의 값을 반환하고, 예외가 발생하면 catch 블록의 값을 반환합니다.

```kotlin
fun main() {
    val result = try {
        val x = 10 / 2
        x // 반환값
    } catch (e: Exception) {
        -1 // 예외가 발생하면 반환할 값
    
  
    println("결과: $result")
}
```

출력:

```text
결과: 5
```

## 4. 예외 던지기 (throw)

- 예외를 수동으로 발생시키려면 throw 키워드를 사용합니다.

### 기본 문법

```kotlin
throw ExceptionType("예외 메시지")
```

예제

```kotlin
fun checkAge(age: Int) {
    if (age < 18) {
        throw IllegalArgumentException("나이는 18 이상이어야 합니다.")
    }
}

fun main() {
    try {
        checkAge(15)
    } catch (e: IllegalArgumentException) {
        println("예외 발생: ${e.message}")
    }
}
```

출력:

```text
예외 발생: 나이는 18 이상이어야 합니다.
```

## 5. 사용자 정의 예외

- 사용자 정의 예외를 생성하려면 Exception 클래스를 상속받아 커스텀 예외를 만들 수 있습니다.

예제

```kotlin
class CustomException(message: String): Exception(message)

fun main() {
    try {
        throw CustomException("사용자 정의 예외 발생")
    } catch (e: CustomException) {
        println("예외 처리: ${e.message}")
    }
}
```

출력:

```text
예외 처리: 사용자 정의 예외 발생
```

## 6. NullPointerException 방지

- 코틀린은 Null 안전성을 제공하며, try-catch 없이 안전 호출 연산자(?.)나 엘비스 연산자(?:)를 사용해 예외를 방지할 수 있습니다.

예제

```kotlin
fun main() {
    val nullableString: String? = null

    val length = nullableString?.length ?: -1
    println("문자열 길이: $length") // 출력: 문자열 길이: -1
}
```

## 요약

| 키워드     | 역할                        |
| ------- | ------------------------- |
| try     | 예외가 발생할 수 있는 코드를 실행       |
| catch   | 특정 예외를 처리                 |
| finally | 예외 발생 여부와 관계없이 항상 실행되는 코드 |
| throw   | 명시적으로 예외를 발생              |

코틀린의 예외 처리는 간결하고 표현식으로 사용할 수 있어, 효율적이고 안전하게 오류를 처리할 수 있습니다.
