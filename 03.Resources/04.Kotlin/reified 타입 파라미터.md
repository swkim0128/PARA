코틀린의 **reified(실체화된) 타입 파라미터**는 **인라인 함수에서만 사용 가능한 제네릭 타입으로, 런타임 시점에도 타입 정보를 유지할 수 있는 기능**이다.

왜 reified가 필요한가?

- 제네릭 타입은 기본적으로 런타임에 타입 정보가 지워진다(타입 소거, Type Erasure)
- 일반적인 제네릭 함수에서는 T::class와 같은 타입 정보를 사용할 수 없다.
- 하지만, reified를 사용하면 T::class를 런타임에서도 사용할 수 있다.

## 1. reified가 없는 일반적인 제네릭 함수

```kotlin
inline fun <T> getClassType(): Class<T> {
    return T::class.java // ❌ 컴파일 오류 (T는 런타임에 타입 소거됨)
}
```

오류 발생: T::class 또는 T::class.java를 사용할 수 없다.

이유:

- 제네릭 타입 T는 컴파일 시점에는 존재하지만, 런타임에서는 타입 정보가 사라진다(타입 소거, Type Erasure).
- 따라서 T::class 같은 런타임 타입 참조가 불가능하다.

## 2. reified를 사용한 제네릭 함수

reified 키워드를 사용하면 타입 소거를 방지하고, 런타임에서도 타입 정보를 유지할 수 있다.

예제: reified 적용

```kotlin
inline fun <reified T> getClassType(): Class<T> {
    return T::class.java // ✅ 정상 동작
}

fun main() {
    println(getClassType<String>()) // 출력: class java.lang.String
    println(getClassType<Int>()) // 출력: int
}
```

설명:

- \<reified T\> → T를 실체화(reified)하여 런타임에도 타입을 유지할 수 있게 함.
- T::class.java → 컴파일 오류 없이 정상적으로 실행 가능.

## 3. reified를 활용한 is 연산자 사용

일반적인 제네릭 함수에서는 is 연산자를 사용할 수 없지만, reified를 사용하면 가능하다.

예제: is 연산자 사용

```kotlin
inline fun <reified T> checkType(value: Any) {
    if (value is T) {
        println("값은 ${T::class.simpleName} 타입입니다.")
    } else {
        println("값은 ${T::class.simpleName} 타입이 아닙니다.")
    }
}

fun main() {
    checkType<String>("Hello") // 출력: 값은 String 타입입니다.
    checkType<Int>(42) // 출력: 값은 Int 타입입니다.
    checkType<Double>("Hello") // 출력: 값은 Double 타입이 아닙니다.
}
```

설명

- is T → 런타임 타입 체크 가능
- T::class.simpleName → 제네릭 타입의 클래스 정보를 가져올 수 있음.

## 4. reified와 함께 JSON 변환 활용

실제 개발에서는 reified를 JSON 변환과 같은 작업에 많이 활용할 수 있다.

예제: JSON 문자열을 객체로 변환하기

```kotlin
import com.google.gson.Gson

inline fun <reified T> fromJson(json: String): T {
    return Gson().fromJson(json, T::class.java)
}

fun main() {
    val json = """{"name":"Alice", "age":25}"""
    
    data class User(val name: String, val age: Int)
    
    val user = fromJson<User>(json)
    println(user) // 출력: User(name=Alice, age=25)
}
```

설명

- Gson().fromJson(json, T::class.java) → 제네릭 타입을 유지하면서 객체로 변환 가능
- reified 없이 T::class.java를 사용할 경우 컴파일 오류가 발생함.

## 5. reified와 inline의 관계

- reified는 반드시 inline 함수에서만 사용할 수 있다.
- 이유: 인라인 함수는 호출될 때 코드가 그대로 복사되므로, 제네릭 타입을 유지할 수 있다.

예제: reified 없이 사용하려고 하면?

```kotlin
fun <reified T> getClassType(): Class<T> {
    return T::class.java // ❌ 컴파일 오류 발생 (reified는 inline 함수에서만 사용 가능)
}
```

해결 방법: inline을 추가하면 정상 동작.

```kotlin
inline fun <reified T> getClassType(): Class<T> {
    return T::class.java // ✅ 정상 동작
}
```

## 6. reified를 사용하지 않고 타입 정보를 전달하는 방법

- reified를 사용할 수 없는 경우(비인라인 함수)에는 **클래스 타입을 인자로 전달하는 방법**이 있다.

```kotlin
fun <T> getClassType(clazz: Class<T>): Class<T> {
    return clazz
}

fun main() {
    println(getClassType(String::class.java)) // 출력: class java.lang.String
}
```

하지만, reified를 사용하면 더 간결한 코드 작성이 가능하다.

## 7. reified 요약

| **개념**          | **설명**                                               |
| --------------- | ---------------------------------------------------- |
| **reified의 역할** | 제네릭 타입을 **런타임까지 유지**할 수 있도록 함                        |
| **필요한 이유**      | 일반적인 제네릭 타입은 런타임에서 **타입 정보가 사라지기 때문** (Type Erasure) |
| **사용 가능한 곳**    | **inline 함수 내에서만 사용 가능**                             |
| **사용 예시**       | T::class, T::class.java, is T 연산자 사용 가능              |
| **대체 방법**       | Class<T>를 함수 인자로 전달                                  |

## 8. 결론

- reified를 사용하면 제네릭 타입을 런타임까지 유지할 수 있다.
- reified는 반드시 inline 함수와 함께 사용해야 한다.
- reified를 사용하면 T::class, T::class.java, is T 같은 기능을 사용할 수 있다.
- JSON 변환, 타입 검사 등 런타임 타입이 필요한 경우 유용하게 활용 가능하다.

💡 reified를 활용하면 타입 정보를 유지하면서 더 간결하고 강력한 코드를 작성할 수 있다! 🚀
