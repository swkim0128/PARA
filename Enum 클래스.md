
코틀린의 **enum class(열거형 클래스)**는 **관련된 상수들을 하나의 타입으로 정의**할 때 사용됩니다.
이를 통해 **코드 가독성을 높이고, 타입 안정성을 보장하며, 특정 값의 집합을 표현하는데 유용**합니다.

## 1. Enum 클래스 기본 문법

- enum class 키워드를 사용하여 정의합니다.
- 각 상수(Constant)는 ,(콤마)로 구분되며, 대문자로 작성하는 것이 일반적입니다.

기본 예제

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}

fun main() {
    val direction: Direction = Direction.NORTH
    println(direction) // 출력: NORTH
}
```

✅ **각 상수는 객체로 취급되며, Direction.NORTH처럼 접근하여 사용할 수 있음.**

## 2. Enum 클래스의 프로퍼티와 메서드

Enum 클래스에는 **프로퍼티 및 메서드를 추가할 수 있습니다.**
각 상수에 대해 특정 값을 할당할 수도 있습니다.

(1) 프로퍼티 추가

```kotlin
enum class Color(val hex: String) {
    RED("#FF0000"),
    GREEN("#00FF00"),
    BLUE("#0000FF")
}

fun main() {
    println(Color.RED.hex) // 출력: #FF0000
}
```

✅ **각 상수에 hex라는 프로퍼티를 추가하고, 특정 값을 할당함.**

(2) 메서드 추가

Enum 클래스에는 **메서드를 정의할 수도 있습니다.**

```kotlin
enum class Color(val hex: String) {
    RED("#FF0000"),
    GREEN("#00FF00"),
    BLUE("#0000FF");

    fun printColor() {
        println("Color: $name, Hex: $hex")
    }
}

fun main() {
    Color.RED.printColor() // 출력: Color: RED, Hex: #FF0000
}
```

✅ **name 속성을 활용하여 각 상수의 이름을 출력할 수도 있음.**

## 3. values()와 valueOf() 사용

- **values()**: Enum 클래스의 모든 상수를 리스트로 가져옵니다.
- **valueOf("NAME")**: 해당 이름과 일치하는 Enum 상수를 가져옵니다.

```kotlin
fun main() {
    // 모든 Enum 상수 출력
    for (color in Color.values()) {
        println(color)
    }

    // 특정 이름으로 Enum 상수 가져오기
    val selectedColor = Color.valueOf("GREEN")
    println(selectedColor) // 출력: GREEN
}
```

✅ **values()와 valueOf()를 사용하면 Enum 값을 동적으로 다룰 수 있음.**

## **4. Enum 클래스에서 ordinal과 name 속성**

- **ordinal**: Enum 상수의 **인덱스(0부터 시작)**를 반환.
- **name**: Enum 상수의 **이름(문자열)**을 반환.

```kotlin
fun main() {
    val color = Color.BLUE
    println(color.name) // 출력: BLUE
    println(color.ordinal) // 출력: 2 (RED: 0, GREEN: 1, BLUE: 2)
}
```

✅ **Enum 상수의 순서를 알고 싶다면 ordinal 속성을 사용하면 됨.**

## 5. Enum 클래스에서 추상 메서드 사용

- Enum 클래스의 각 상수가 서로 다른 동작을 해야 할 때, **추상 메서드를 정의하고, 각 상수에서 구현**할 수 있습니다.

```kotlin
enum class Shape {
    CIRCLE {
        override fun area(size: Double) = 3.14 * size * size
    },
    SQUARE {
        override fun area(size: Double) = size * size
    };

    abstract fun area(size: Double): Double
}

fun main() {
    println(Shape.CIRCLE.area(5.0)) // 출력: 78.5
    println(Shape.SQUARE.area(4.0)) // 출력: 16.0
}
```

✅ **각 상수가 서로 다른 동작을 수행하도록 설정 가능.**

## 6. Enum 클래스를 활용한 when 표현식

- **Enum 클래스를 when과 함께 사용하면 가독성이 좋아짐.**

```kotlin
enum class Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
}

fun isWeekend(day: Day): Boolean {
    return when (day) {
        Day.SATURDAY, Day.SUNDAY -> true
        else -> false
    }
}

fun main() {
    println(isWeekend(Day.FRIDAY)) // 출력: false
    println(isWeekend(Day.SATURDAY)) // 출력: true
}
```

✅ **Enum을 when과 함께 사용하면 코드 가독성이 높아짐.**

## **7. 인터페이스 구현**

Enum 클래스에서도 **인터페이스를 구현할 수 있음**.

```kotlin
interface Printable {
    fun printInfo()
}

enum class Planet(val mass: Double) : Printable {
    EARTH(5.97),
    MARS(0.642);

    override fun printInfo() {
        println("$name의 질량: ${mass} x 10^24 kg")
    }
}

fun main() {
    Planet.EARTH.printInfo() // 출력: EARTH의 질량: 5.97 x 10^24 kg
}
```

✅ **Enum 클래스에서도 인터페이스를 구현하여, 공통 기능을 제공할 수 있음.**

## 8. Enum 클래스 요약

| **기능**        | **설명**              | **예제**                                               |
| ------------- | ------------------- | ---------------------------------------------------- |
| **기본 사용**     | Enum 클래스 정의         | enum class Direction { NORTH, SOUTH, EAST, WEST }    |
| **프로퍼티 추가**   | 각 상수에 값 추가          | enum class Color(val hex: String) { RED("#FF0000") } |
| **메서드 추가**    | Enum 내부에서 함수 정의     | fun printColor() { println(name) }                   |
| **values()**  | 모든 Enum 상수 반환       | Color.values()                                       |
| **valueOf()** | 이름으로 Enum 상수 찾기     | Color.valueOf("RED")                                 |
| **ordinal**   | Enum 상수의 인덱스        | Color.RED.ordinal (출력: 0)                            |
| **name**      | Enum 상수의 이름         | Color.RED.name (출력: "RED")                           |
| **추상 메서드**    | 각 상수별로 다른 동작 설정     | abstract fun action(): String                        |
| **인터페이스 구현**  | Enum 클래스에서 인터페이스 사용 | enum class Planet : Printable { ... }                |

## 9. 결론

✅ **Enum 클래스는 관련된 상수들을 그룹화하여 코드의 가독성을 높여줌.**
✅ **values()와 valueOf()를 사용하면 동적으로 Enum을 다룰 수 있음.**
✅ **ordinal과 name을 활용하면 Enum의 순서와 이름을 쉽게 확인 가능.**
✅ **인터페이스 구현, 추상 메서드 등을 사용하여 더욱 유연한 기능 확장 가능.**

💡 **Enum 클래스를 잘 활용하면 더욱 가독성 높은 코드를 작성할 수 있습니다! 🚀**
