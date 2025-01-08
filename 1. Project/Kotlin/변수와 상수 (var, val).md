---
tags:
  - kotlin
---

코틀린에서 변수와 상수는 var와 val 키워드를 사용하여 선언합니다. 이를 통해 값이 변경 가능한지 여부를 명확히 구분할 수 있습니다.

## 변수 선언 (var)

- var는 **변경 가능한 변수**를 선언할 때 사용합니다.
- 변수를 선언한 후 값을 **재할당**할 수 있습니다.

### 문법

```kotlin
var 변수명: 데이터타입 = 초기값
```

예제

```kotlin
var age: Int = 25
println(age) // 출력: 25
age = 30
println(age) // 출력: 30
```

### 특징

- 타입을 명시하거나, 초기값에 따라 타입을 자동으로 추론할 수 있습니다.
- 값이 동적으로 변경될 가능성이 있는 데이터를 저장할 때 적합합니다.
- 재할당은 가능하지만, 변수의 타입은 고정됩니다.

## 상수 선언 (val)

- val은 **변경 불가능한 변수(상수)**를 선언할 때 사용합니다.
- 선언 이후 값을 **재할당할 수 없습니다**.

### 문법

```kotlin
val 변수명: 데이터타입 = 초기값
```

예제

```kotlin
val name: String = "Alice"
println(name) // 출력: Alice

// name = "Bob" // 오류: Val cannot be reassigned
```

### 특징

- 초기화된 값을 변경할 수 없습니다.
- 코드의 안정성을 높이고, 불필요한 오류를 방지합니다.
- 객체의 참조는 변경할 수 없지만, 객체 내부의 값은 변경될 수 있습니다.

## val과 var의 차이점

| 키워드 | 재할당 가능 여부 | 사용 용도            |
| --- | --------- | ---------------- |
| val | 불가능       | 변경되지 않을 값을 저장할 때 |
| var | 가능        | 변경 가능한 값을 저장할 때  |

## 타입 추론

- 코틀린은 변수의 타입을 명시하지 않아도, 초기값을 기반으로 타입을 추론합니다.
- 타입을 명시하지 않은 경우, 코틀린 컴파일러가 자동으로 변수의 타입을 설정합니다.

예제

```kotlin
val number = 10      // Int로 추론
val message = "Hello" // String으로 추론
var isKotlin = true  // Boolean으로 추론
```

## 초기화 없이 변수 선언

- 코틀린에서는 변수를 선언할 때 **초기값**이 반드시 필요합니다.
- 초기값 없이 변수를 선언하려면 lateinit 또는 **lazy**를 사용해야 합니다.

### lateinit 사용 예제

- 초기화를 나중에 수행하고 싶은 경우.
- Primitive 타입(예: Int, Double)에서는 사용 불가.

```kotlin
lateinit var name: String
fun initializeName() {
    name = "Kotlin"
    println(name) // 출력: Kotlin
}
```

### lazy 사용 예제

- 호출 시점에 초기화를 수행하고자 할 때.

```kotlin
val greeting: String by lazy {
    println("Initializing...")
    "Hello, Kotlin!"
}

fun main() {
    println(greeting) // "Initializing..." 출력 후 "Hello, Kotlin!" 출력
    println(greeting) // "Hello, Kotlin!"만 출력
}
```

## 참조 대상의 불변성

- val은 변수의 참조를 변경할 수 없지만, 참조하는 객체 내부의 값은 변경될 수 있습니다.
- 예제:

```kotlin
val list = mutableListOf(1, 2, 3)
list.add(4) // 내부 값 변경 가능
println(list) // 출력: [1, 2, 3, 4]
// list = mutableListOf(5, 6, 7) // 컴파일 오류: Val cannot be reassigned
```

## 요약

- var: 값을 변경할 수 있는 변수.
- val: 값을 변경할 수 없는 상수.
- 타입 추론 및 lateinit, lazy를 통해 코드의 간결성과 효율성을 높일 수 있습니다.
