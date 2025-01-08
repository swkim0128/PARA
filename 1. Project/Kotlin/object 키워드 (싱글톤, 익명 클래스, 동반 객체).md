## 1. 싱글톤 객체 (Singleton)

- **싱글톤 객체**는 클래스의 인스턴스를 단 하나만 생성하도록 보장하는 객체입니다.
- 코틀린에서는 object 키워드를 사용하여 간단하게 싱글톤을 구현할 수 있습니다.

### 싱글톤 객체 정의

문법

```kotlin
object 객체이름 {
    // 속성과 메서드 정의
}
```

예제

```kotlin
object Logger {
    fun log(message: String) {
        println("Log: $message")
    }
}

fun main() {
    Logger.log("Hello, Singleton!") // 출력: Log: Hello, Singleton!
}
```

### 특징

- object 키워드를 사용하여 정의된 객체는 프로그램에서 하나만 존재합니다.
- Logger는 전역적으로 접근 가능하며, Logger 객체를 직접 호출하여 사용합니다.

## 2. 익명 클래스 (Anonymous Class)

- **익명 클래스**는 특정 인터페이스나 클래스를 구현해야 하지만, 별도의 클래스를 정의하지 않고 즉시 객체를 생성하는 데 사용됩니다.
- object 키워드를 사용하여 익명 클래스를 생성할 수 있습니다.

### 익명 클래스 정의

문법

```kotlin
interface 인터페이스이름 {
    fun 메서드이름()
}

val 익명객체 = object : 인터페이스이름 {
    override fun 메서드이름() {
        // 구현
    }
}
```

예제

```kotlin
interface ClickListener {
    fun onClick()
}

fun setClickListener(listener: ClickListener) {
    listener.onClick()
}

fun main() {
    setClickListener(object : ClickListener {
        override fun onClick() {
            println("Button clicked!")
        }
    })
}
```

### 특징

- 익명 클래스는 한 번만 사용되는 간단한 구현체를 작성할 때 유용합니다.
- 객체를 생성하며 인터페이스나 추상 클래스를 구현합니다.

## 3. 동반 객체 (Companion Object)

- **동반 객체**는 클래스 내부에 선언된 객체로, 해당 클래스와 동반되어 사용됩니다.
- **정적 메서드와 유사한 역할**을 하며, 클래스의 특정 기능을 클래스 이름으로 바로 호출할 수 있습니다.

### 동반 객체 정의

문법

```kolin
class 클래스이름 {
    companion object {
        // 정적 메서드와 속성 정의
    }
}
```

예제

```kolin
class MathUtils {
    companion object {
        fun add(a: Int, b: Int): Int {
            return a + b
        }
    }
}

fun main() {
    val result = MathUtils.add(5, 3)
    println("Result: $result") // 출력: Result: 8
}
```

### 동반 객체 이름 지정

- 동반 객체에 이름을 부여할 수도 있습니다.

```kotlin
class MathUtils {
    companion object Calculator {
        fun add(a: Int, b: Int): Int {
            return a + b
        }
    }
}

fun main() {
    val result = MathUtils.Calculator.add(5, 3)
    println("Result: $result") // 출력: Result: 8
}
```

### 동반 객체와 팩토리 패턴

• 동반 객체는 **팩토리 패턴**을 구현할 때 자주 사용됩니다.

```kotlin
class User private constructor(val name: String) {
    companion object {
        fun create(name: String): User {
            return User(name)
        }
    }
}

fun main() {
    val user = User.create("Alice")
    println("User name: ${user.name}") // 출력: User name: Alice
}
```

### 동반 객체와 인터페이스 구현

- 동반 객체는 인터페이스를 구현할 수 있습니다.

```kotlin
interface Factory<T> {
    fun create(): T
}

class Product {
    companion object : Factory<Product> {
        override fun create(): Product {
            return Product()
        }
    }
}

fun main() {
    val product = Product.create()
    println(product) // 출력: Product@<hash_code>
}
```

## 4. object 키워드 활용 요약

| 사용 사례  | 설명                                         |
| ------ | ------------------------------------------ |
| 싱글톤 객체 | 프로그램 내에서 단 하나만 존재하는 객체 생성                  |
| 익명 클래스 | 인터페이스나 추상 클래스의 간단한 구현체를 즉시 생성              |
| 동반 객체  | 클래스와 관련된 정적 메서드와 속성을 정의하며, 팩토리 패턴 등에 활용 가능 |

## 5. 싱글톤, 익명 클래스, 동반 객체의 비교

| 특징       | 싱글톤 객체      | 익명 클래스                 | 동반 객체                    |
| -------- | ----------- | ---------------------- | ------------------------ |
| 생성 방식    | object 키워드  | object :로 인터페이스/클래스 구현 | 클래스 내부의 companion object |
| 사용 목적    | 전역적이고 단일 객체 | 일회성 인터페이스/클래스 구현       | 클래스와 관련된 정적 속성/메서드       |
| 사용 가능 횟수 | 여러 번 사용 가능  | 한 번 사용 후 재사용 어려움       | 여러 번 사용 가능               |

코틀린의 object 키워드는 **싱글톤**, **익명 클래스**, **동반 객체** 구현을 간단하고 효율적으로 지원합니다. 이를 적절히 활용하면 코드의 가독성과 유지보수성을 높일 수 있습니다.
