
코틀린의 **Not-null 단언(!!) 연산자**는 **Nullable 타입을 강제로 Non-null 타입으로 변환하는 연산자**입니다. 즉, 해당 변수가 null이 아닐 것이라고 확신할 때 사용합니다. 하지만, 변수가 null이면 **NullPointerException(NPE)**이 발생할 수 있으므로 주의해야 합니다.

## 1. !! 연산자의 기본 문법

```kotlin
val nonNullValue: Type = nullableValue!!
```

- nullableValue가 null이 아니라면 값을 정상적으로 반환합니다.
- nullableValue가 null이면 **NullPointerException 발생**.

## 2. !! 연산자 사용 예제

### 1. 기본적인 사용

```kotlin
fun main() {
    val name: String? = "Kotlin"
    val length: Int = name!!.length // 강제 호출
    println(length) // 출력: 6
}
```

- name이 null이 아니므로 length가 정상적으로 호출됨.

### 2. null일 경우 예외 발생

```kotlin
fun main() {
    val name: String? = null
    val length: Int = name!!.length // NullPointerException 발생
    println(length)
}
```

- name이 null이므로 **런타임 오류 (NullPointerException)** 발생.

**⚠️ !! 연산자는 null이 들어올 가능성이 있을 때 사용하면 앱이 충돌할 수 있음!**

## 3. !! 연산자와 ?., ?: 연산자 비교

| 연산자 | 설명                      | 예제                             |
| --- | ----------------------- | ------------------------------ |
| ?.  | null이면 연산을 중단하고 null 반환 | val length = name?.length      |
| ?:  | null이면 기본값 반환           | val length = name?.length ?: 0 |
| !!  | 강제 호출 (NPE 발생 가능)       | val length = name!!.length     |

### 1. !! vs ?.

```kotlin
fun main() {
    val name: String? = null

    // 안전 호출 연산자 (?.)
    println(name?.length) // 출력: null

    // 강제 호출 연산자 (!!)
    println(name!!.length) // NullPointerException 발생
}
```

**👉 ?. 연산자를 사용하면 null일 때도 안전하게 처리할 수 있음.**

### 2. !! vs ?:

```kotlin
fun main() {
    val name: String? = null

    // 엘비스 연산자 (기본값 제공)
    val length = name?.length ?: 0
    println(length) // 출력: 0

    // 강제 호출 연산자 (!!)
    println(name!!.length) // NullPointerException 발생
}
```

**👉 ?: 연산자를 사용하면 기본값을 설정할 수 있어 null 오류를 방지할 수 있음.**

## 4. !! 연산자 사용을 피해야 하는 경우

### 1. null 가능성이 있는 변수에서 !! 사용

```kotlin
val userInput: String? = getUserInput() // 외부 입력값
val length = userInput!!.length // NullPointerException 발생 가능
```

✅ **해결 방법**: ?. 또는 ?: 사용

```kotlin
val length = userInput?.length ?: 0
```

### 2. API 응답 처리 시 !! 사용

```kotlin
fun fetchData(): String? {
    return null // API 응답이 null일 가능성 있음
}

fun main() {
    val data = fetchData()!!
    println(data) // NullPointerException 발생 가능
}
```

✅ **해결 방법**: ?:로 기본값 제공

```kotlin
val data = fetchData() ?: "No Data"
```

## 5. !! 연산자를 안전하게 사용하는 경우

✅ **명확하게 null이 아님을 보장할 수 있을 때만 사용해야 합니다.**

### 1. null이 아님을 확인한 후 !! 사용

```kotlin
fun main() {
    val name: String? = "Kotlin"

    if (name != null) {
        val length = name!!.length // 안전하게 사용 가능
        println(length) // 출력: 6
    }
}
```

### 2. 테스트나 단위 테스트에서 !! 사용

- 테스트 코드에서 !!을 사용하여 null이 아니어야 하는 경우 강제 검증할 수 있음.

```kotlin
fun main() {
    val result: String? = "Test Passed"
    require(result!!.isNotEmpty()) // NullPointerException 발생 시 테스트 실패
}
```

## 6. !! 연산자 사용 요약

| 사용 상황                   | 해결 방법                 |
| ----------------------- | --------------------- |
| null 가능성이 있는 변수에서 !! 사용 | ?., ?: 연산자를 사용        |
| API 응답 처리               | 기본값 (?: "Default") 제공 |
| null 체크 없이 !! 사용        | 명확한 null 체크 후 !! 사용   |

✅ **최대한 !! 사용을 피하고 ?., ?: 등의 안전한 방법을 사용하자!** 🚀
