
코틀린에서 **타입 캐스팅(Type Casting)**은 객체의 타입을 변환할 때 사용됩니다. 코틀린은 타입 안전성을 보장하기 위해 **안전한 타입 변환을 위한 연산자**를 제공합니다.

## 1. is 연산자 (타입 검사)

- **is 연산자는 객체가 특정 타입인지 확인할 때 사용**됩니다.
- 타입이 일치하면 true, 그렇지 않으면 false를 반환합니다.

### (1) 기본 사용법

```kotlin
fun main() {
    val value: Any = "Hello, Kotlin!"

    if (value is String) {
        println(value.length) // 출력: 14
    }
}
```

- value가 String 타입인지 검사한 후, length 프로퍼티를 안전하게 사용.

### (2) is 연산자와 !is (부정형)

```kotlin
fun main() {
    val num: Any = 42

    if (num !is String) {
        println("num은 String이 아닙니다.") // 출력됨
    }
}
```

- !is를 사용하면 **특정 타입이 아닐 때** 조건을 실행할 수 있음.

## 2. as 연산자 (명시적 타입 변환)

- **as 연산자는 객체를 특정 타입으로 변환할 때 사용**됩니다.
- **실패하면 ClassCastException이 발생**하므로 사용 시 주의가 필요합니다.

### (1) 기본 사용법

```kotlin
fun main() {
    val value: Any = "Kotlin"
    val text: String = value as String // 명시적 캐스팅
    println(text) // 출력: Kotlin
}
```

- value를 String으로 변환 후 출력.

### (2) 잘못된 as 사용 예시

```kotlin
fun main() {
    val number: Any = 100
    val text: String = number as String // 런타임 오류 발생 (ClassCastException)
    println(text)
}
```

🚫 **타입이 맞지 않으면 ClassCastException이 발생하므로 주의해야 합니다.**

## 3. as? 연산자 (안전한 캐스팅)

- **캐스팅 실패 시 null을 반환**하는 안전한 캐스팅 연산자입니다.
- as 연산자와 달리 **예외가 발생하지 않음**.

### (1) as?를 사용한 안전한 타입 변환

```kotlin
fun main() {
    val number: Any = 100
    val text: String? = number as? String // 안전한 캐스팅 (null 반환)
    
    println(text) // 출력: null
}
```

🚀 as?를 사용하면 잘못된 캐스팅 시 **예외 없이 null을 반환**하므로 더욱 안전함.

## 4. is와 스마트 캐스트 (Smart Cast)

- **is 연산자로 타입을 검사하면 자동으로 스마트 캐스트가 적용**됩니다.
- **명시적 캐스팅 없이 해당 타입의 메서드나 프로퍼티를 사용할 수 있음.**

### (1) 스마트 캐스트 예제

```kotlin
fun printLength(value: Any) {
    if (value is String) {
        println(value.length) // 자동으로 String으로 캐스팅됨
    }
}

fun main() {
    printLength("Hello, Kotlin!") // 출력: 14
}
```

- **is 연산자로 타입 검사를 하면 자동으로 String으로 변환되어 length 호출 가능**.

### (2) when과 함께 사용

```kotlin
fun describe(value: Any): String {
    return when (value) {
        is String -> "문자열입니다: ${value.length} 글자"
        is Int -> "정수입니다: $value"
        is Double -> "실수입니다: $value"
        else -> "알 수 없는 타입입니다."
    }
}

fun main() {
    println(describe("Kotlin")) // 출력: 문자열입니다: 6 글자
    println(describe(42)) // 출력: 정수입니다: 42
    println(describe(3.14)) // 출력: 실수입니다: 3.14
}
```

- when을 사용하면 다양한 타입을 깔끔하게 처리 가능.

## 5. 타입 캐스팅 예제 정리

| **연산자** | **설명**              | **사용 예제**                          | **예외 발생 가능 여부** |
| ------- | ------------------- | ---------------------------------- | --------------- |
| is      | 객체가 특정 타입인지 확인      | if (obj is String) { ... }         | ❌               |
| !is     | 특정 타입이 아닐 경우 실행     | if (obj !is Int) { ... }           | ❌               |
| as      | 명시적 타입 변환           | val text: String = obj as String   | ✅ (타입 불일치 시)    |
| as?     | 안전한 타입 변환 (null 반환) | val text: String? = obj as? String | ❌               |

## 6. 결론

✅ **is 연산자로 안전하게 타입 확인 가능 (스마트 캐스트 적용됨)**
✅ **as 연산자는 ClassCastException 발생 가능, 주의해야 함**
✅ **as? 연산자는 실패 시 null 반환하므로 안전한 캐스팅이 필요할 때 사용**
✅ **when과 is를 함께 사용하면 다양한 타입을 깔끔하게 처리 가능**

**💡 as 대신 as?를 적극 활용하여 안전한 캐스팅을 수행하는 것이 권장됩니다! 🚀**
