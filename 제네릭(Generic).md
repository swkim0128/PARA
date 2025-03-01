## 1. 제네릭(Generic)이란?

제네릭(Generic)은 **클래스, 함수, 인터페이스에서 타입을 변수처럼 다룰 수 있도록 하는 기능**이다.
즉, **코드를 재사용할 수 있도록 타입을 일반화**하는 방식이다.

제네릭을 사용하는 이유:
- ✅ **코드의 재사용성 증가** (여러 타입을 처리할 수 있음)
- ✅ **타입 안정성 보장** (컴파일 시 타입 체크)
- ✅ **불필요한 캐스팅 제거** (명시적 타입 변환이 필요 없음)

## 2. 제네릭 기본 문법

제네릭 타입은 \<T\> 형식으로 정의되며, T는 타입을 의미하는 **타입 매개변수(Type Parameter)**이다.

제네릭 클래스 예제

```kotlin
class Box<T>(val value: T) {
    fun getValue(): T = value
}

fun main() {
    val intBox = Box(10)
    val stringBox = Box("Hello")

    println(intBox.getValue()) // 출력: 10
    println(stringBox.getValue()) // 출력: Hello
}
```

### 설명

- Box\<T\> → T는 임의의 타입을 의미하며, 실제 사용 시 타입이 결정됨.
- Box(10) → T는 Int 타입.
- Box("Hello") → T는 String 타입.

## 3. 제네릭 함수

제네릭은 클래스뿐만 아니라 **함수에도 적용 가능**하다.

제네릭 함수 예제

```kotlin
fun <T> printItem(item: T) {
    println(item)
}

fun main() {
    printItem(100)  // 출력: 100
    printItem("Kotlin")  // 출력: Kotlin
    printItem(3.14)  // 출력: 3.14
}
```

### 설명

• \<T\> → 제네릭 타입 선언.
• printItem(item: T) → T 타입의 매개변수를 받아 출력.
• 호출할 때 **타입을 지정하지 않아도 자동 추론됨**.

## 4. 제네릭 타입 제약 (타입 상한 제한)

제네릭 타입에 특정 타입만 허용하고 싶을 때 T : 상위타입 형식으로 제한할 수 있다.

제네릭 타입 제한 예제

```kotlin
fun <T : Number> doubleValue(value: T): Double {
    return value.toDouble() * 2
}

fun main() {
    println(doubleValue(10))  // 출력: 20.0
    println(doubleValue(3.5))  // 출력: 7.0
    // println(doubleValue("Hello"))  // 오류 발생 (Number 타입이 아님)
}
```

### 설명

• \<T : Number\> → T는 Number 타입만 허용 (Int, Double, Float 등 가능).
• toDouble() 메서드를 사용할 수 있음 (Number를 상속하는 타입이기 때문).

## 5. 제네릭 가변성 (Variance)

코틀린에서는 **공변성(Covariance)과 반공변성(Contravariance)을 키워드로 명확히 지정**할 수 있다.

### 1) 공변성 (out)

- **읽기 전용(생산자) → out 사용**
- List\<T\> 같은 읽기 전용 컬렉션에서 사용됨.

```kotlin
interface Producer<out T> {
    fun produce(): T
}

class StringProducer : Producer<String> {
    override fun produce(): String = "Hello"
}

fun main() {
    val producer: Producer<String> = StringProducer()
    val anyProducer: Producer<Any> = producer // ✅ 공변성 허용
    println(anyProducer.produce()) // 출력: Hello
}
```

설명

- Producer\<out T\> → T를 반환하는 역할만 함 (읽기 전용).
- Producer\<String\>을 Producer\<Any\>로 업캐스팅 가능.

### 2) 반공변성 (in)

- **쓰기 전용(소비자) → in 사용**
- Comparator\<T\> 같은 타입 비교에서 사용됨.

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
    val stringConsumer: Consumer<String> = anyConsumer // ✅ 반공변성 허용
    stringConsumer.consume("Hello") // 출력: Consumed: Hello
}
```

설명

- Consumer\<in T\> → T를 받아서 처리하는 역할 (쓰기 전용).
- Consumer\<Any\>를 Consumer\<String\>으로 다운캐스팅 가능.

### 3) 무공변성 (Invariant)

- T를 in과 out 모두 사용하는 경우.

```kotlin
class Container<T>(var item: T)
```

- **T를 in과 out 동시에 사용하면 타입 변환 불가능.**
- Container\<String\>을 Container\<Any\>로 변환할 수 없음.

## 6. 스타 프로젝션 (*)

타입을 알 수 없을 때 *(스타 프로젝션)를 사용하여 **안전하게 처리**할 수 있다.

```kotlin
fun printList(list: List<*>) {
    for (item in list) {
        println(item)
    }
}

fun main() {
    val numbers: List<Int> = listOf(1, 2, 3)
    val strings: List<String> = listOf("A", "B", "C")

    printList(numbers) // 출력: 1, 2, 3
    printList(strings) // 출력: A, B, C
}
```

설명

- List<*> → **제네릭 타입을 알 수 없지만 읽기 가능**.
- for (item in list)을 통해 안전하게 사용 가능.

## 7. 제네릭을 활용한 컬렉션 변환

제네릭을 사용하여 **컬렉션을 변환하는 함수**를 쉽게 만들 수 있다.

```kotlin
fun <T, R> transformList(input: List<T>, transformer: (T) -> R): List<R> {
    return input.map(transformer)
}

fun main() {
    val numbers = listOf(1, 2, 3)
    val squaredNumbers = transformList(numbers) { it * it }

    println(squaredNumbers) // 출력: [1, 4, 9]
}
```

설명

- List\<T\>를 List\<R\>로 변환하는 일반적인 함수.
- map()을 사용하여 변환.

## 8. 제네릭 클래스의 타입 매개변수 제한 (where)

여러 타입 제약을 적용하려면 where을 사용할 수 있다.

```kotlin
fun <T> ensureNumber(value: T) where T : Number, T : Comparable<T> {
    println("$value is a valid number")
}

fun main() {
    ensureNumber(10)  // 정상 동작
    ensureNumber(3.14)  // 정상 동작
    // ensureNumber("Hello")  // 오류 발생
}
```

설명

- where T : Number, T : Comparable\<T\> → T는 Number이면서 Comparable을 구현해야 함.

## 9. 결론

- 제네릭은 **클래스, 함수의 타입을 일반화하여 재사용성을 높이는 기능**.
- \<T\>를 사용하여 **제네릭 클래스 및 함수 정의 가능**.
- **제네릭 타입 제약**을 사용하여 특정 타입만 허용 가능.
- out(공변성), in(반공변성)을 활용하여 **타입 변환 유연성을 높일 수 있음**.
- List<*> 같은 **스타 프로젝션을 사용하면 타입을 모를 때 안전하게 처리 가능**.

제네릭을 활용하면 **유연하고 안전한 타입 설계가 가능하다.** 🚀
