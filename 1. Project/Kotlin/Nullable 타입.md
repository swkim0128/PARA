코틀린의 **Nullable 타입**은 **Null 안전성**을 보장하기 위해 제공되는 강력한 기능입니다. 이는 **NullPointerException(NPE)**을 방지하고, 안전하게 Null 값을 처리할 수 있도록 설계되었습니다.

## 1. Nullable 타입이란?

- **Nullable 타입**은 변수가 null 값을 가질 수 있는지를 명시적으로 표현하는 타입입니다.
- **?**를 사용하여 Nullable 타입을 정의합니다.

예제

```kotlin
val nonNullable: String = "Hello" _// null 불가_
val nullable: String? = null      _// null 허용_
```

## 2. Null 안전성

코틀린은 기본적으로 변수에 Null 값을 허용하지 않습니다. 하지만, ?를 사용해 Nullable 타입을 정의하면 Null 값을 허용할 수 있습니다.

## 3. Nullable 타입 다루기

### 1. 안전 호출 연산자 (?.)

- **안전 호출 연산자**는 객체가 null인지 확인한 후에 프로퍼티나 메서드에 접근합니다.
- null인 경우, 호출을 무시하고 null을 반환합니다.

문법

```kotlin
nullableObject?.propertyOrMethod
```

예제

```kotlin
fun main() {
    val nullableString: String? = null
    println(nullableString?.length) _// 출력: null_

    val nonNullString: String? = "Kotlin"
    println(nonNullString?.length) _// 출력: 6_
}
```

### 2. 엘비스 연산자 (?:)

- **엘비스 연산자**는 Nullable 값이 null인 경우, 기본값을 반환합니다.
- a ?: b는 a가 null이 아니면 a를 반환하고, null이면 b를 반환합니다.
  
문법

```kotlin
nullableObject ?: defaultValue
```

예제

```kotlin
fun main() {
    val nullableString: String? = null
    val result = nullableString ?: "Default Value"
    println(result) _// 출력: Default Value_
}
```

### 3. 강제 호출 연산자 (!!)

- **강제 호출 연산자**는 Nullable 타입을 Non-Nullable 타입으로 변환합니다.
- 하지만, 해당 값이 null일 경우 **NullPointerException**이 발생합니다.

문법

```kotlin
nullableObject!!
```

예제

```kotlin
fun main() {
    val nullableString: String? = "Kotlin"
    println(nullableString!!.length) _// 출력: 6_

    val nullValue: String? = null
    _// println(nullValue!!.length) // NullPointerException 발생_
}
```

### 4. let 함수와 안전 호출 연산자

- let 함수는 객체가 null이 아닌 경우에만 특정 작업을 수행합니다.

문법

```kotlin
nullableObject?.let { 작업 }
```

예제

```kotlin
fun main() {
    val nullableString: String? = "Kotlin"
    nullableString?.let {
        println("Length: ${it.length}")
    }

    _// 출력: Length: 6_
}
```

### 5. Null 체크와 조건문

- Nullable 타입은 일반 조건문으로도 Null 체크가 가능합니다.

예제

```kotlin
fun main() {
    val nullableString: String? = null

    if (nullableString != null) {
        println("Length: ${nullableString.length}")
    } else {
        println("String is null")
    }
	
    _// 출력: String is null_
}
```

## 4. Nullable 타입의 기본 연산

### 1. 문자열의 길이

```kotlin
fun main() {
    val nullableString: String? = null
    println(nullableString?.length ?: 0) _// 출력: 0_
}
```

### 2. Nullable 리스트

```kotlin
fun main() {
    val nullableList: List<Int>? = null
    println(nullableList?.size ?: "Empty List") _// 출력: Empty List_
}
```

## 5. safe cast (as?)

- as?는 안전하게 타입을 변환하며, 변환이 불가능하면 null을 반환합니다.

문법

```kotlin
val value = object as? TargetType
```

예제

```kotlin
fun main() {
    val obj: Any = "Kotlin"
    val str: String? = obj as? String
    println(str) _// 출력: Kotlin_

    val int: Int? = obj as? Int
    println(int) _// 출력: null_
}
```

## 6. Nullable 타입의 확장 함수

예제: 기본값 설정

```kotlin
fun String?.orDefault(): String {
    return this ?: "Default Value"
}

fun main() {
    val nullableString: String? = null
    println(nullableString.orDefault()) _// 출력: Default Value_
}
```

## 7. Nullable 타입과 컬렉션

### 1. Nullable 컬렉션

```kotlin
fun main() {
    val nullableList: List<String?> = listOf("Alice", null, "Bob")
    nullableList.forEach {
        println(it?.toUpperCase() ?: "Unknown")
    }

    _// 출력:_
    _// ALICE_
    _// Unknown_
    _// BOB_
}
```

### 2. Non-Nullable 필터링

```kotlin
fun main() {
    val nullableList: List<String?> = listOf("Alice", null, "Bob")
    val filteredList = nullableList.filterNotNull()
    println(filteredList) _// 출력: [Alice, Bob]_
}
```

## 요약

| 기능        | 연산자 / 함수        | 설명                                         |
| --------- | --------------- | ------------------------------------------ |
| 안전 호출     | ?.              | Null 여부를 확인 후 안전하게 호출                      |
| 기본값 설정    | ?:              | Null인 경우 기본값 반환                            |
| 강제 호출     | !!              | Null 여부 확인 없이 호출 (NullPointerException 가능) |
| let 함수    | ?.let { }       | Null이 아닐 때 블록 실행                           |
| safe cast | as?             | 안전한 타입 변환                                  |
| 필터링       | filterNotNull() | Null이 아닌 요소만 필터링                           |

코틀린의 Nullable 타입은 NullPointerException을 효과적으로 방지하며, 안전하고 간결한 코드 작성을 돕습니다. 상황에 맞는 연산자와 함수들을 적절히 활용하면 안정성 높은 프로그램을 개발할 수 있습니다.
