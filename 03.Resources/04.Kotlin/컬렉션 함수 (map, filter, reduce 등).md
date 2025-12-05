## 1. map

### 설명

- 컬렉션의 각 요소를 변환하여 새로운 컬렉션을 생성합니다.

### 문법

```kotlin
collection.map { 변환할 로직 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)
	
    // 각 요소를 두 배로 변환
    val doubled = numbers.map { it * 2 }
    println(doubled) // 출력: [2, 4, 6, 8, 10]

    // 문자열 변환_
    val strings = numbers.map { "Number $it" }
    println(strings) // 출력: [Number 1, Number 2, Number 3, Number 4, Number 5]
}
```

## 2. filter

### 설명

- 조건에 맞는 요소만 걸러내 새로운 컬렉션을 생성합니다.

### 문법

```kotlin
collection.filter { 조건식 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    // 짝수만 필터링
    val evenNumbers = numbers.filter { it % 2 == 0 }
    println(evenNumbers) // 출력: [2, 4]

    // 3보다 큰 값 필터링
    val greaterThanThree = numbers.filter { it > 3 }
    println(greaterThanThree) // 출력: [4, 5]
}
```

## 3. reduce

### 설명

- 컬렉션의 요소를 누적하여 단일 값으로 축약합니다.
- 초기값 없이 사용되며, 첫 번째 요소를 기본값으로 사용합니다.

### 문법

```kotlin
collection.reduce { 누적값, 현재값 -> 계산식 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    // 합계 계산
    val sum = numbers.reduce { acc, num -> acc + num }
    println(sum) // 출력: 15

    // 곱 계산
    val product = numbers.reduce { acc, num -> acc * num }
    println(product) // 출력: 120
}
```

## 4. fold

### 설명

- reduce와 유사하지만, 초기값을 지정할 수 있습니다.

### 문법

```kotlin
collection.fold(초기값) { 누적값, 현재값 -> 계산식 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    // 합계 계산 (초기값 10 추가)
    val sum = numbers.fold(10) { acc, num -> acc + num }
    println(sum) // 출력: 25

    // 문자열 연결
    val joined = numbers.fold("Numbers:") { acc, num -> "$acc $num" }
    println(joined) // 출력: Numbers: 1 2 3 4 5
}
```

## 5. forEach

### 설명

- 각 요소에 대해 특정 작업을 수행하지만, 결과를 반환하지 않습니다.

### 문법

```kotlin
collection.forEach { 작업 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    // 각 요소 출력
    numbers.forEach { println(it) }
}
```

## 6. find

### 설명

- 조건에 맞는 첫 번째 요소를 반환합니다. 조건에 맞는 값이 없으면 null을 반환합니다.

### 문법

```kotlin
collection.find { 조건식 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    // 3보다 큰 첫 번째 값 찾기
    val result = numbers.find { it > 3 }
    println(result) // 출력: 4
}
```

## 7. groupBy

### 설명

- 특정 기준에 따라 요소를 그룹화하여 맵(Map) 형태로 반환합니다.

### 문법

```kotlin
collection.groupBy { 기준 }
```

예제

```kotlin
fun main() {
    val names = listOf("Alice", "Bob", "Charlie", "David")

    // 이름 길이로 그룹화
    val grouped = names.groupBy { it.length }
    println(grouped) // 출력: {5=[Alice, David], 3=[Bob], 7=[Charlie]}
}
```

## 8. flatMap

### 설명

- 각 요소를 변환하고, 변환된 결과를 단일 컬렉션으로 평면화합니다.

### 문법

```kotlin
collection.flatMap { 변환 로직 }
```

예제

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3)

    // 각 요소를 1부터 요소까지의 리스트로 변환 후 평면화
    val result = numbers.flatMap { (1..it).toList() }
    println(result) // 출력: [1, 1, 2, 1, 2, 3]
}
```

## 9. zip

### 설명

- 두 컬렉션을 짝지어 새로운 컬렉션을 만듭니다.

### 문법

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

## 컬렉션 함수 비교 요약

| 함수      | 역할                       | 반환값              |
| ------- | ------------------------ | ---------------- |
| map     | 각 요소를 변환하여 새로운 컬렉션 생성    | 변환된 요소로 이루어진 컬렉션 |
| filter  | 조건을 만족하는 요소만 걸러냄         | 조건을 만족하는 요소의 컬렉션 |
| reduce  | 요소를 누적하여 단일 값으로 축약       | 단일 값             |
| fold    | 초기값과 함께 요소를 누적하여 단일 값 생성 | 단일 값             |
| forEach | 각 요소에 대해 작업 수행           | 반환값 없음           |
| find    | 조건을 만족하는 첫 번째 요소 반환      | 요소 또는 null       |
| groupBy | 특정 기준으로 그룹화              | Map<Key, List>   |
| flatMap | 각 요소를 변환 후 평면화           | 변환된 요소의 단일 컬렉션   |
| zip     | 두 컬렉션을 짝지어 새로운 컬렉션 생성    | List<Pair<T, R>> |

코틀린의 컬렉션 함수는 고차 함수와 람다 표현식을 결합하여 데이터를 변환하거나 필터링, 축약하는 작업을 간결하고 효율적으로 처리할 수 있습니다.
