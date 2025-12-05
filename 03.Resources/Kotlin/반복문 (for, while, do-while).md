
코틀린은 다양한 반복문을 제공하며, 이를 사용해 특정 작업을 반복적으로 수행할 수 있습니다.

## 1. for 반복문

• 코틀린의 for문은 **범위**(range), **컬렉션**(예: 리스트, 배열) 또는 반복 가능한 객체를 순회하는 데 사용됩니다.

### 기본 문법

```kotlin
for (item in 범위) {
    // 실행할 코드
}
```

### 1. 범위를 사용한 반복

- in 키워드를 사용하여 지정된 범위를 순회합니다.

```kotlin
fun main() {
    for (i in 1..5) {
        println(i) // 출력: 1, 2, 3, 4, 5
    }
}
```

### 2. 범위의 증가 폭 설정

- step 키워드를 사용하여 증가 폭을 설정할 수 있습니다.

```kotlin
fun main() {
    for (i in 1..10 step 2) {
        println(i) // 출력: 1, 3, 5, 7, 9
    }
}
```

### 3. 역순 반복

- downTo를 사용하여 역순으로 반복할 수 있습니다.

```kotlin
fun main() {
    for (i in 5 downTo 1) {
        println(i) // 출력: 5, 4, 3, 2, 1
    }
}
```

### 4. 배열 또는 리스트를 순회

- 배열이나 리스트의 요소를 순회할 수 있습니다.

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5)

    for (num in numbers) {
        println(num)
    }
}
```

### 5. 인덱스와 값을 함께 사용

- withIndex를 사용하여 인덱스와 값을 함께 처리할 수 있습니다.

```kotlin
fun main() {
    val fruits = listOf("Apple", "Banana", "Cherry")

    for ((index, fruit) in fruits.withIndex()) {
        println("$index: $fruit")
    }
}
```

## 2. while 반복문

- while문은 조건이 참(true)인 동안 블록을 실행합니다.

### 기본 문법

```kotlin
while (조건) {
    // 실행할 코드
}
```

### 1. 기본 사용

```kotlin
fun main() {
    var i = 1

    while (i <= 5) {
        println(i) // 출력: 1, 2, 3, 4, 5
        i++
    }
}
```

### 2. 무한 루프

- 조건이 항상 참이면 무한 루프가 생성됩니다.

```kotlin
fun main() {
    var i = 1

    while (true) {
        println(i)
        if (i == 5) break // 루프 종료
        i++
    }
}
```

## 3. do-while 반복문

- do-while문은 조건을 검사하기 전에 블록을 먼저 실행합니다.
- 최소한 한 번은 실행되는 특징이 있습니다.

### 기본 문법

```kotlin
do {
    // 실행할 코드
} while (조건)
```

### 1. 기본 사용

```kotlin
fun main() {
    var i = 1

    do {
        println(i) // 출력: 1, 2, 3, 4, 5
        i++
    } while (i <= 5)
}
```

### 2. 조건이 처음부터 거짓일 경우

- 블록은 한 번 실행된 후 조건을 검사합니다.

```kotlin
fun main() {
    var i = 10

    do {
        println(i) // 출력: 10
    } while (i < 5)
}
```

## 반복문 제어 키워드

### 1. break

- 반복문을 즉시 종료합니다.

```kotlin
fun main() {
    for (i in 1..10) {
        if (i == 5) break
        println(i) // 출력: 1, 2, 3, 4
    }
}
```

### 2. continue

- 현재 반복을 건너뛰고 다음 반복을 실행합니다.

```kotlin
fun main() {
    for (i in 1..5) {
        if (i == 3) continue
        println(i) // 출력: 1, 2, 4, 5
    }
}
```

### 3. return

- 반복문을 포함하는 함수 전체를 종료합니다.

```kotlin
fun main() {
    for (i in 1..5) {
        if (i == 3) return
        println(i) // 출력: 1, 2
    }
}
```

## 요약

| 반복문      | 설명                                | 최소 실행 횟수 |
| -------- | --------------------------------- | -------- |
| for      | 범위, 리스트, 배열 등의 요소를 순회할 때 사용       | 0번       |
| while    | 조건이 참인 동안 반복                      | 0번       |
| do-while | 조건에 상관없이 최소 1번 실행 후, 조건이 참인 동안 반복 | 1번 이상    |

코틀린의 반복문은 직관적이고 간결하며, 다양한 조건과 데이터 구조를 처리하는 데 유용합니다. 상황에 따라 적합한 반복문을 선택하여 사용하세요.
