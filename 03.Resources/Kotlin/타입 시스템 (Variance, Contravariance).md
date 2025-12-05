## 1. 코틀린의 타입 시스템 개요

코틀린의 타입 시스템에서는 **제네릭(Generic)을 사용할 때 타입의 변환(업캐스팅, 다운캐스팅)이 가능하도록 특정 키워드를 제공**한다.
이러한 타입 변환 방식은 공변성(Covariance), 반공변성(Contravariance), 무공변성(Invariance)**으로 구분된다.

타입 변환(Variance)이 필요한 이유

- 제네릭 클래스 간의 타입 변환을 안전하게 보장하기 위해 필요하다.
- 함수의 매개변수와 반환 타입을 올바르게 다루기 위해 사용된다.

## 2. 무공변성(Invariance)

기본적으로 제네릭 타입은 변환이 불가능하다.

예제: 일반적인 제네릭 클래스

```kotlin
class Box<T>(val value: T)

fun main() {
    val stringBox: Box<String> = Box("Hello")
    // val anyBox: Box<Any> = stringBox  ❌ 컴파일 오류 발생 (타입 변환 불가)
}
```

왜 오류가 발생하는가?

- Box\<T\>는 기본적으로 무공변적(Invariant)이므로 **Box\<String\>을 Box\<Any\>로 변환할 수 없다.
- 해결 방법: 공변성(out) 또는 반공변성(in) 키워드 사용.

## 3. 공변성(Covariance) - out

공변성이란 **제네릭 타입이 상위 타입으로 변환(업캐스팅)될 수 있도록 허용하는 것**이다.
코틀린에서는 out 키워드를 사용하여 **공변성을 적용할 수 있다**.

공변성 예제

```kotlin
interface Producer<out T> {
    fun produce(): T
}

class StringProducer : Producer<String> {
    override fun produce(): String = "Hello"
}

fun main() {
    val stringProducer: Producer<String> = StringProducer()
    val anyProducer: Producer<Any> = stringProducer  // ✅ 업캐스팅 허용
    println(anyProducer.produce()) // 출력: Hello
}
```

### 설명

- Producer\<out T\> → T는 공변성이 적용된 타입이다.
- Producer\<String\>을 Producer\<Any\>로 변환할 수 있다.
- out 키워드를 사용하면, 해당 타입은 “읽기 전용”이 된다.
- 즉, 반환(return)은 가능하지만, 값을 변경(setter)은 불가능하다.

### out 키워드의 제한

- out을 사용하면 **반환(return)은 가능하지만, 매개변수로 사용할 수 없다.**
- 예제:

```kotlin
interface Producer<out T> {
    fun produce(): T
    // fun consume(item: T) ❌ 컴파일 오류 발생 (매개변수 사용 불가)
}
```

✅ **공변성을 사용하는 대표적인 예:**

- List\<T\> → List\<String\>을 List\<Any\>로 변환 가능.

## 4. 반공변성(Contravariance) - in

반공변성이란 **제네릭 타입이 하위 타입으로 변환(다운캐스팅)될 수 있도록 허용하는 것**이다.
코틀린에서는 in 키워드를 사용하여 **반공변성을 적용할 수 있다**.

반공변성 예제

```kotlin
interface Consumer<in T> {
    fun consume(item: T)
}

class AnyConsumer : Consumer<Any> {
    override fun consume(item: Any) {
        println("Consumed: $item")
    }
}

fun main() {
    val anyConsumer: Consumer<Any> = AnyConsumer()
    val stringConsumer: Consumer<String> = anyConsumer // ✅ 다운캐스팅 허용
    stringConsumer.consume("Hello") // 출력: Consumed: Hello
}
```

### 설명

- Consumer\<in T\> → T는 반공변성이 적용된 타입이다.
- Consumer\<Any\>을 Consumer\<String\>으로 변환할 수 있다.
- in 키워드를 사용하면, 해당 타입은 “쓰기 전용”이 된다.
- 즉, 매개변수(parameter)로는 사용할 수 있지만, 반환(return)은 불가능하다.

### in 키워드의 제한

- in을 사용하면 **반환(return)은 불가능하다**.
- 예제:

```kotlin
interface Consumer<in T> {
    fun consume(item: T)
    // fun produce(): T ❌ 컴파일 오류 발생 (반환 불가능)
}
```

✅ 반공변성을 사용하는 대표적인 예:

- Comparator\<T\> → Comparator\<Any\>을 Comparator\<String\>으로 변환 가능.

## 5. in과 out을 동시에 사용할 수 없는 이유

T를 **in과 out 동시에 사용할 수 없다**.

```kotlin
class Container<T>(var item: T) // ❌ 컴파일 오류 발생
```

이유:

- in → 매개변수로 사용 (쓰기 가능)
- out → 반환값으로 사용 (읽기 가능)
- 하지만 var item: T는 **읽기와 쓰기가 모두 가능하므로 in과 out을 동시에 사용할 수 없다.**

✅ **대안:** invariant(무공변성)를 유지하거나, 별도의 타입을 분리해야 한다.

## 6. 공변성 & 반공변성 요약

| **개념**   | **키워드** | **변환 방향**                                | **사용 위치**                              | **예제**         |
| -------- | ------- | ---------------------------------------- | -------------------------------------- | -------------- |
| **공변성**  | out     | Producer<String> → Producer<Any> (업캐스팅)  | 반환 타입으로 사용 가능 (fun produce(): T)       | List<T>        |
| **반공변성** | in      | Consumer<Any> → Consumer<String> (다운캐스팅) | 매개변수 타입으로 사용 가능 (fun consume(item: T)) | Comparator<T>  |
| **무공변성** | 없음      | 변환 불가능                                   | 읽기/쓰기 둘 다 가능 (var item: T)             | MutableList<T> |

## 7. out과 in의 실제 사용 사례

### 1) List\<T\>는 out을 사용

- List\<T\>는 읽기 전용이므로 out 키워드가 적용된다.

```kotlin
val strings: List<String> = listOf("Kotlin", "Java")
val anyList: List<Any> = strings  // ✅ 업캐스팅 가능 (공변성 적용)
```

### 2) MutableList\<T\>는 무공변성

- MutableList\<T\>는 읽기/쓰기 둘 다 가능하므로 in과 out을 사용할 수 없다.

```kotlin
val strings: MutableList<String> = mutableListOf("Kotlin", "Java")
// val anyList: MutableList<Any> = strings ❌ 변환 불가능 (무공변성)
```

### 3) Comparator\<T\>는 in을 사용

- Comparator\<T\>는 비교할 때 매개변수로 T를 사용하므로 in 키워드를 사용할 수 있다.

```kotlin
val anyComparator: Comparator<Any> = Comparator { a, b -> a.hashCode() - b.hashCode() }
val stringComparator: Comparator<String> = anyComparator // ✅ 다운캐스팅 가능 (반공변성 적용)
```

## 8. 결론

- 기본적으로 제네릭 타입은 변환이 불가능(무공변성)하다.
- out을 사용하면 공변성을 제공하여 상위 타입으로 변환 가능.
- in을 사용하면 반공변성을 제공하여 하위 타입으로 변환 가능.
- 읽기 전용(Producer)에는 out, 쓰기 전용(Consumer)에는 in을 사용해야 한다.
- List\<T\>는 out을, Comparator\<T\>는 in을 사용한다.

💡 제네릭 타입을 설계할 때는 변환 방향을 고려하여 out과 in을 적절히 사용해야 한다! 🚀
