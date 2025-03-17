
코틀린의 컬렉션(Collection)은 **불변(Immutable)**과 **가변(Mutable)** 두 가지 종류가 있습니다.

- **Immutable 컬렉션**: 컬렉션을 생성한 후 **변경할 수 없음** (읽기 전용)
- **Mutable 컬렉션**: 요소를 **추가, 수정, 삭제 가능**

## 1. 불변(Immutable) 컬렉션

- **요소를 추가하거나 변경할 수 없음.**
- listOf(), setOf(), mapOf() 함수를 사용하여 생성.

예제

```kotlin
fun main() {
    val fruits = listOf("Apple", "Banana", "Cherry")
    
    println(fruits[0]) // 출력: Apple
    println(fruits.size) // 출력: 3
}
```

🚫 **불변 리스트에서는 add(), remove() 등의 메서드를 사용할 수 없음.**

```kotlin
fun main() {
    val fruits = listOf("Apple", "Banana", "Cherry")
    // fruits.add("Orange")  // 컴파일 오류 발생!
    // fruits[0] = "Grape"   // 컴파일 오류 발생!
}
```

## 2. 가변(Mutable) 컬렉션

- **요소를 추가, 수정, 삭제할 수 있음.**
- mutableListOf(), mutableSetOf(), mutableMapOf() 사용.

예제

```kotlin
fun main() {
    val animals = mutableListOf("Dog", "Cat", "Horse")

    animals.add("Elephant") // 요소 추가
    animals.remove("Cat") // 요소 삭제
    animals[0] = "Tiger" // 값 변경

    println(animals) // 출력: [Tiger, Horse, Elephant]
}
```

## 3. Immutable vs Mutable 컬렉션 비교

| 컬렉션 종류             | 생성 방법           | 요소 추가 | 요소 수정 | 요소 삭제 |
| ------------------ | --------------- | ----- | ----- | ----- |
| **Immutable List** | listOf()        | ❌ 불가능 | ❌ 불가능 | ❌ 불가능 |
| **Mutable List**   | mutableListOf() | ✅ 가능  | ✅ 가능  | ✅ 가능  |
| **Immutable Set**  | setOf()         | ❌ 불가능 | ❌ 불가능 | ❌ 불가능 |
| **Mutable Set**    | mutableSetOf()  | ✅ 가능  | ✅ 가능  | ✅ 가능  |
| **Immutable Map**  | mapOf()         | ❌ 불가능 | ❌ 불가능 | ❌ 불가능 |
| **Mutable Map**    | mutableMapOf()  | ✅ 가능  | ✅ 가능  | ✅ 가능  |

## 4. 불변 컬렉션을 가변 컬렉션으로 변환

불변 컬렉션을 가변 컬렉션으로 변환하려면 toMutableList(), toMutableSet(), toMutableMap()을 사용합니다.

예제

```kotlin
fun main() {
    val fruits = listOf("Apple", "Banana", "Cherry")
    val mutableFruits = fruits.toMutableList() // 가변 리스트로 변환

    mutableFruits.add("Orange")
    println(mutableFruits) // 출력: [Apple, Banana, Cherry, Orange]
}
```

## 5. 가변 컬렉션을 불변 컬렉션으로 변환

가변 컬렉션을 불변 컬렉션으로 변환하려면 toList(), toSet(), toMap()을 사용합니다.

예제

```kotlin
fun main() {
    val mutableNumbers = mutableListOf(1, 2, 3, 4)
    val immutableNumbers = mutableNumbers.toList() // 불변 리스트로 변환

    // immutableNumbers.add(5) // 컴파일 오류 발생!
    println(immutableNumbers) // 출력: [1, 2, 3, 4]
}
```

## 6. Mutable vs Immutable 사용 가이드

✅ **Immutable 컬렉션 사용이 권장되는 경우**:

- 변경이 필요 없는 데이터를 다룰 때
- 멀티스레드 환경에서 안전하게 사용할 때
- 불필요한 데이터 변경을 방지하고 가독성을 높일 때

✅ **Mutable 컬렉션 사용이 권장되는 경우**:

- 리스트나 맵의 요소를 동적으로 추가/삭제해야 할 때
- 값이 변경될 가능성이 높은 경우

## 7. Immutable 컬렉션의 제한 사항과 해결 방법

🚫 **Immutable 컬렉션은 요소 변경이 불가능하지만, MutableList로 변환하여 변경할 수 있음.**

```kotlin
fun main() {
    val immutableList = listOf("A", "B", "C")
    val mutableList = immutableList.toMutableList()

    mutableList.add("D")
    println(mutableList) // 출력: [A, B, C, D]
}
```

## 8. Immutable 컬렉션의 실제 사용 예제

**불변 리스트를 활용한 안전한 데이터 처리**

```kotlin
fun getFruits(): List<String> {
    return listOf("Apple", "Banana", "Cherry")
}

fun main() {
    val fruits = getFruits()
    println(fruits) // 출력: [Apple, Banana, Cherry]
}
```

- getFruits()는 불변 리스트를 반환하므로, 외부에서 리스트를 변경할 수 없음.

## 9. Mutable 컬렉션을 함수에서 다룰 때 주의할 점

가변 컬렉션을 함수에서 사용할 때는 **원본 데이터가 변경될 위험**이 있습니다.

```kotlin
fun modifyList(list: MutableList<String>) {
    list.add("Orange")
}

fun main() {
    val fruits = mutableListOf("Apple", "Banana", "Cherry")
    modifyList(fruits)
    println(fruits) // 출력: [Apple, Banana, Cherry, Orange]
}
```

✅ **원본 데이터를 보호하려면 불변 컬렉션을 사용하거나, 복사본을 만들어 사용해야 합니다.**

```kotlin
fun modifyListSafe(list: List<String>): List<String> {
    val newList = list.toMutableList()
    newList.add("Orange")
    return newList
}

fun main() {
    val fruits = listOf("Apple", "Banana", "Cherry")
    val newFruits = modifyListSafe(fruits)
    println(newFruits) // 출력: [Apple, Banana, Cherry, Orange]
}
```

## 10. 결론

| **특징**         | **Immutable 컬렉션**                 | **Mutable 컬렉션**     |
| -------------- | --------------------------------- | ------------------- |
| 요소 추가/삭제 가능 여부 | ❌ 불가능                             | ✅ 가능                |
| 스레드 안전성        | ✅ 높음                              | ❌ 낮음                |
| 데이터 보호         | ✅ 가능                              | ❌ 조작 가능             |
| 변환 가능 여부       | ✅ toMutableList(), toMutableSet() | ✅ toList(), toSet() |

**👉 언제 Immutable 컬렉션을 사용해야 할까?**

- 데이터를 안전하게 유지해야 하는 경우 (예: API 응답)
- 불필요한 변경을 방지하고, 코드 가독성을 높이고 싶은 경우

**👉 언제 Mutable 컬렉션을 사용해야 할까?**

- 리스트에 요소를 동적으로 추가/삭제해야 하는 경우
- 컬렉션을 변경할 필요가 있는 경우

**🎯 결론: Immutable 컬렉션을 기본으로 사용하고, 필요한 경우에만 Mutable 컬렉션을 사용하자!** 🚀
