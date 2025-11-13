## 1. 인라인 함수란?

- **인라인 함수**는 inline 키워드를 사용하여 정의합니다.
- 함수 호출 대신 함수 본문을 호출 위치에 복사하여 실행합니다.
- 주로 **고차 함수(Higher-Order Functions)**에서 성능 최적화를 위해 사용됩니다.

## 2. 인라인 함수의 사용법

### 문법

```kotlin
inline fun 함수이름(매개변수: 타입): 반환타입 {
    // 함수 본문
}
```

예제: 일반 함수와 인라인 함수 비교

### 일반 함수

```kotlin
fun printMessage(message: () -> Unit) {
    message()
}

fun main() {
    printMessage { println("Hello, Kotlin!") }
}
```

### 인라인 함수

```kotlin
inline fun printMessage(message: () -> Unit) {
    message()
}

fun main() {
    printMessage { println("Hello, Kotlin!") }
}
```

차이점:

- 일반 함수는 호출 시 스택 메모리를 사용하여 함수를 호출하고 돌아옵니다.
- 인라인 함수는 함수 호출을 없애고, 본문을 호출 위치로 복사하여 성능 오버헤드를 줄입니다.

## 3. 인라인 함수의 주요 이점

### 1. 고차 함수의 성능 최적화:

- 고차 함수는 일반적으로 **런타임 비용**이 발생하지만, 인라인을 사용하면 이를 줄일 수 있습니다.

### 2. 람다 표현식과 결합:

- 람다를 매개변수로 사용하는 고차 함수에서 유용합니다.

### 3. 성능 개선:

- 작은 크기의 함수에서 호출 오버헤드를 제거하여 성능을 향상시킵니다.

## 4. noinline 키워드

- 특정 매개변수만 인라인되지 않도록 설정할 수 있습니다.
- 고차 함수에서 일부 람다 표현식을 인라인하지 않으려면 noinline을 사용합니다.

예제

```kotlin
inline fun execute(action: () -> Unit, noinline anotherAction: () -> Unit) {
    action() // 인라인 처리됨
    anotherAction() // 인라인 처리되지 않음
}

fun main() {
    execute(
        { println("This is inlined.") },
        { println("This is not inlined.") }
    )
}
```

## 5. crossinline 키워드

- **crossinline**은 람다 표현식에서 return 키워드를 사용하지 못하도록 방지합니다.
- 일반적으로 람다가 다른 컨텍스트로 전달될 때 사용됩니다.

예제

```kotlin
inline fun execute(crossinline action: () -> Unit) {
    val runnable = Runnable { action() }
    runnable.run()
}

fun main() {
    execute {
        println("Crossinline example")
        // return // 컴파일 오류
    }
}
```

## 6. reified 키워드와 인라인 함수

- **reified**는 제네릭 타입 정보를 런타임에 사용할 수 있게 해줍니다.
- 제네릭 타입은 기본적으로 **런타임에 지워지지만(type erasure)**, inline 함수와 함께 사용하면 이를 해결할 수 있습니다.

예제: reified를 사용한 타입 체크

```kotlin
inline fun <reified T> isType(value: Any): Boolean {
    return value is T
}

fun main() {
    println(isType<String>("Hello")) // 출력: true
    println(isType<Int>("Hello"))    // 출력: false
}
```

## 7. 인라인 함수 사용 시 주의사항

### 1. 함수 크기가 클 경우 성능 저하:

- 함수 본문이 크면 복사로 인해 바이너리 크기가 커지고 성능이 저하될 수 있습니다.

### 2. 디버깅 어려움:

- 인라인된 코드는 디버깅 시 호출 스택에서 보이지 않아 문제를 추적하기 어려울 수 있습니다.

### 3. 재귀 함수 사용 불가:

- 인라인 함수는 자기 자신을 호출할 수 없습니다.

예제: 재귀 함수에서 인라인 함수 사용 시 오류

```kotlin
inline fun recursiveFunction(n: Int) { _// 컴파일 오류 발생_
    if (n > 0) {
        recursiveFunction(n - 1)
    }
}
```

## 8. 인라인 함수와 일반 함수의 비교

| 특징    | 일반 함수         | 인라인 함수          |
| ----- | ------------- | --------------- |
| 호출 방식 | 호출 시 함수 스택 사용 | 호출 위치로 코드 복사    |
| 성능    | 호출 오버헤드 발생    | 호출 오버헤드 없음      |
| 코드 크기 | 일정            | 본문 크기만큼 바이너리 증가 |
| 디버깅   | 호출 스택 확인 가능   | 호출 스택에서 확인 어려움  |

## 9. 활용 사례

고차 함수 최적화

```kotlin
inline fun repeatAction(times: Int, action: () -> Unit) {
    for (i in 1..times) {
        action()
    }
}

fun main() {
    repeatAction(3) {
        println("Kotlin is awesome!")
    }
}
```

reified와 함께 제네릭 활용

```kotlin
inline fun <reified T> createInstance(): T {
    return T::class.java.newInstance()
}

fun main() {
    val list = createInstance<ArrayList<String>>()
    list.add("Hello")
    println(list) // 출력: [Hello]
}
```

## 요약

### 1. 인라인 함수:

- 함수 호출의 성능 오버헤드를 줄이기 위해 사용.
- 주로 고차 함수에서 람다 표현식과 결합하여 사용.

### 2. noinline:

- 특정 매개변수를 인라인하지 않도록 설정.

### 3. crossinline:

- 람다에서 return 사용을 방지.

### 4. reified:

- 제네릭 타입 정보를 런타임에 활용 가능.

인라인 함수는 적절히 사용하면 성능 최적화에 큰 도움을 줄 수 있지만, 함수의 크기와 사용 상황을 고려하여 사용하는 것이 중요합니다.
