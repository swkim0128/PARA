
코틀린의 **컬렉션 처리 함수**는 데이터를 효율적으로 변환, 필터링 및 집계하는 기능을 제공합니다. map, filter, reduce, forEach 등의 함수를 사용하면 컬렉션을 간결하고 가독성 있게 처리할 수 있습니다.

## 1. map - 컬렉션 변환

- 컬렉션의 **각 요소를 변환**하여 새로운 컬렉션을 생성합니다.

문법

```kotlin
collection.map { 변환할 로직 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    val doubled = numbers.map { it * 2 }
    println(doubled) // 출력: [2, 4, 6, 8, 10]

    val strings = numbers.map { "Number $it" }
    println(strings) // 출력: [Number 1, Number 2, Number 3, Number 4, Number 5]
}
```

## 2. filter - 조건에 맞는 요소 추출

- 특정 조건을 만족하는 요소만 포함하는 새로운 컬렉션을 생성합니다.

문법

```kotlin
collection.filter { 조건식 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    val evenNumbers = numbers.filter { it % 2 == 0 }
    println(evenNumbers) // 출력: [2, 4]

    val greaterThanThree = numbers.filter { it > 3 }
    println(greaterThanThree) // 출력: [4, 5]
}
```

## 3. forEach - 각 요소에 대한 작업 수행

- 컬렉션의 **각 요소에 대해 특정 작업을 수행**하지만, 결과를 반환하지 않습니다.

문법

```kotlin
collection.forEach { 작업 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    numbers.forEach { println(it) }
}
```

## 4. reduce - 요소를 누적하여 하나의 값으로 축약

- **초기값 없이** 컬렉션을 하나의 값으로 축약합니다.
- 첫 번째 요소를 기본값으로 사용.

문법

```kotlin
collection.reduce { 누적값, 현재값 -> 계산식 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    val sum = numbers.reduce { acc, num -> acc + num }
    println(sum) // 출력: 15

    val product = numbers.reduce { acc, num -> acc * num }
    println(product) // 출력: 120
}
```

## 5. fold - 초기값과 함께 누적 연산 수행

- **초기값을 설정하여** 컬렉션을 하나의 값으로 축약합니다.

문법

```kotlin
collection.fold(초기값) { 누적값, 현재값 -> 계산식 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    val sum = numbers.fold(10) { acc, num -> acc + num }
    println(sum) // 출력: 25

    val joined = numbers.fold("Numbers:") { acc, num -> "$acc $num" }
    println(joined) // 출력: Numbers: 1 2 3 4 5
}
```

## 6. find - 조건을 만족하는 첫 번째 요소 찾기

- **조건을 만족하는 첫 번째 요소를 반환**하며, 없으면 null을 반환합니다.

문법

```kotlin
collection.find { 조건식 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    val result = numbers.find { it > 3 }
    println(result) // 출력: 4
}
```

## 7. groupBy - 특정 기준으로 그룹화

- 컬렉션을 특정 기준에 따라 **그룹화하여 Map 형태로 반환**합니다.

문법

```kotlin
collection.groupBy { 기준 }
```

예제

```kotlin
fun main() {
    val names = listOf("Alice", "Bob", "Charlie", "David")

    val grouped = names.groupBy { it.length }
    println(grouped) // 출력: {5=[Alice, David], 3=[Bob], 7=[Charlie]}
}
```

## 8. flatMap - 각 요소를 변환하고 평탄화

- 각 요소를 변환 후, **결과를 하나의 리스트로 평탄화(flatten)** 합니다.

문법

```kotlin
collection.flatMap { 변환 로직 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3)

    val result = numbers.flatMap { (1..it).toList() }
    println(result) // 출력: [1, 1, 2, 1, 2, 3]
}
```

## 9. zip - 두 컬렉션을 짝지어 새로운 컬렉션 생성

- 두 컬렉션을 짝지어 **Pair로 이루어진 리스트를 생성**합니다.

문법

```kotlin
collection1.zip(collection2)
```

예제

```kotlin
fun main() {
    val names = listOf("Alice", "Bob", "Charlie")
    val ages = listOf(25, 30, 35)

    val paired = names.zip(ages)
    println(paired) // 출력: [(Alice, 25), (Bob, 30), (Charlie, 35)]
}
```

## 10. 컬렉션 처리 함수 비교 요약

| **함수**  | **역할**                   | **반환값**          |
| ------- | ------------------------ | ---------------- |
| map     | 각 요소를 변환하여 새로운 컬렉션 생성    | 변환된 요소로 이루어진 컬렉션 |
| filter  | 조건을 만족하는 요소만 걸러냄         | 조건을 만족하는 요소의 컬렉션 |
| forEach | 각 요소에 대해 작업 수행           | 반환값 없음           |
| reduce  | 요소를 누적하여 단일 값으로 축약       | 단일 값             |
| fold    | 초기값과 함께 요소를 누적하여 단일 값 생성 | 단일 값             |
| find    | 조건을 만족하는 첫 번째 요소 반환      | 요소 또는 null       |
| groupBy | 특정 기준으로 그룹화              | Map<Key, List>   |
| flatMap | 각 요소를 변환 후 평탄화           | 변환된 요소의 단일 컬렉션   |
| zip     | 두 컬렉션을 짝지어 새로운 컬렉션 생성    | List<Pair<T, R>> |

## 결론

✅ map과 filter를 활용하면 데이터를 쉽게 변환하고 필터링할 수 있음
✅ reduce와 fold를 사용하면 컬렉션을 하나의 값으로 축약 가능
✅ groupBy를 사용하면 데이터를 특정 기준으로 그룹화 가능
✅ flatMap과 zip을 활용하면 컬렉션을 더욱 유연하게 변형 가능

**🎯 코틀린의 컬렉션 함수들을 적절히 활용하면 코드의 가독성과 효율성을 높일 수 있습니다! 🚀**
