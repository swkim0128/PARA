
코틀린의 **Sealed 클래스(봉인 클래스)**는 **상속이 가능한 클래스이지만, 상속할 수 있는 하위 클래스를 제한하는 기능을 가진 클래스**입니다.

이는 enum class와 abstract class의 장점을 결합한 형태로, **계층 구조를 갖는 데이터 모델을 정의할 때 유용**합니다.

## 1. Sealed 클래스란?

- sealed 키워드를 사용하여 선언.
- 같은 **파일 내에서만 하위 클래스를 정의**할 수 있음.
- **when 표현식에서 모든 경우를 처리했는지 컴파일러가 검사**해줌.

기본 문법

```kotlin
sealed class 클래스이름 {
    class 하위클래스1 : 클래스이름()
    class 하위클래스2 : 클래스이름()
}
```

## 2. Sealed 클래스 기본 예제

```kotlin
sealed class Shape {
    class Circle(val radius: Double) : Shape()
    class Rectangle(val width: Double, val height: Double) : Shape()
}

fun describe(shape: Shape): String {
    return when (shape) {
        is Shape.Circle -> "원의 반지름: ${shape.radius}"
        is Shape.Rectangle -> "사각형의 크기: ${shape.width} x ${shape.height}"
    }
}

fun main() {
    val circle = Shape.Circle(5.0)
    val rectangle = Shape.Rectangle(4.0, 6.0)

    println(describe(circle)) // 출력: 원의 반지름: 5.0
    println(describe(rectangle)) // 출력: 사각형의 크기: 4.0 x 6.0
}
```

✅ **Sealed 클래스는 when과 함께 사용하면 else 없이 모든 경우를 반드시 처리해야 함.**
✅ **각 하위 클래스는 Shape을 상속받아 다른 동작을 정의할 수 있음.**

## 3. sealed class vs enum class

| **구분**      | **Sealed 클래스**      | **Enum 클래스**        |
| ----------- | ------------------- | ------------------- |
| **상속 여부**   | 하위 클래스 상속 가능        | 불가능                 |
| **데이터 포함**  | 여러 개의 프로퍼티 포함 가능    | 단일 인스턴스만 가능         |
| **인스턴스 생성** | 하위 클래스의 인스턴스 생성 가능  | Enum 상수만 사용 가능      |
| **확장성**     | 새로운 서브클래스를 추가할 수 있음 | Enum 값 추가 가능하지만 제한적 |

차이점 예제

```kotlin
enum class Color {
    RED, GREEN, BLUE
}

sealed class Shape {
    class Circle(val radius: Double) : Shape()
}
```

✅ **enum class는 단순한 값의 열거형**
✅ **sealed class는 데이터와 동작을 포함하는 계층 구조 모델링 가능**

## 4. Sealed 클래스에서 object 사용

object를 사용하면 **싱글톤 형태의 하위 클래스**를 만들 수 있음.

예제

```kotlin
sealed class NetworkState {
    object Loading : NetworkState()
    object Success : NetworkState()
    data class Error(val message: String) : NetworkState()
}

fun handleState(state: NetworkState) {
    when (state) {
        is NetworkState.Loading -> println("로딩 중...")
        is NetworkState.Success -> println("성공!")
        is NetworkState.Error -> println("오류 발생: ${state.message}")
    }
}

fun main() {
    handleState(NetworkState.Loading) // 출력: 로딩 중...
    handleState(NetworkState.Success) // 출력: 성공!
    handleState(NetworkState.Error("네트워크 연결 실패")) // 출력: 오류 발생: 네트워크 연결 실패
}
```

✅ **object를 사용하면 인스턴스를 생성할 필요 없이 싱글톤처럼 사용할 수 있음.**
✅ **하위 클래스 중 Error만 data class로 정의하여 추가적인 데이터를 포함하도록 구현.**

## 5. Sealed 인터페이스 (sealed interface)

- 코틀린 1.5부터 **인터페이스에도 sealed 적용 가능**.
- sealed interface는 **다른 파일에서도 구현 가능**(클래스와 차이점).

예제

```kotlin
sealed interface Animal

class Dog : Animal
class Cat : Animal
```

✅ **Sealed 인터페이스는 여러 파일에서 구현 가능하지만, Sealed 클래스는 같은 파일에서만 가능!**

## 6. Sealed 클래스의 활용 사례

### (1) 네트워크 응답 처리

```kotlin
sealed class ApiResponse<out T> {
    object Loading : ApiResponse<Nothing>()
    data class Success<T>(val data: T) : ApiResponse<T>()
    data class Error(val errorMessage: String) : ApiResponse<Nothing>()
}

fun handleResponse(response: ApiResponse<String>) {
    when (response) {
        is ApiResponse.Loading -> println("로딩 중...")
        is ApiResponse.Success -> println("데이터: ${response.data}")
        is ApiResponse.Error -> println("오류 발생: ${response.errorMessage}")
    }
}

fun main() {
    handleResponse(ApiResponse.Loading) // 출력: 로딩 중...
    handleResponse(ApiResponse.Success("API 데이터")) // 출력: 데이터: API 데이터
    handleResponse(ApiResponse.Error("서버 오류")) // 출력: 오류 발생: 서버 오류
}
```

✅ **서버 응답을 Loading, Success, Error 상태로 관리 가능**
✅ **when을 사용하면 모든 상태를 처리할 수 있음**

### (2) 사용자 입력 처리

```kotlin
sealed class UserAction {
    object Click : UserAction()
    object LongPress : UserAction()
    data class Swipe(val direction: String) : UserAction()
}

fun handleAction(action: UserAction) {
    when (action) {
        is UserAction.Click -> println("클릭")
        is UserAction.LongPress -> println("길게 누름")
        is UserAction.Swipe -> println("스와이프 방향: ${action.direction}")
    }
}

fun main() {
    handleAction(UserAction.Click) // 출력: 클릭
    handleAction(UserAction.Swipe("오른쪽")) // 출력: 스와이프 방향: 오른쪽
}
```

✅ **사용자 액션을 Click, LongPress, Swipe 등으로 정의 가능**
✅ **각 이벤트를 when을 통해 처리할 수 있어 가독성 높아짐**

## 7. Sealed 클래스 요약

| **기능**           | **설명**                        | **예제**                                           |
| ---------------- | ----------------------------- | ------------------------------------------------ |
| **정의**           | 특정 클래스의 하위 클래스를 제한            | sealed class Shape                               |
| **파일 제한**        | 같은 파일 내에서만 하위 클래스 정의 가능       | sealed class Status { class Success : Status() } |
| **when 사용**      | when에서 else 없이 모든 경우 처리 가능    | when(status) { is Success -> ... }               |
| **싱글톤 형태**       | object를 사용하여 하나의 인스턴스만 유지     | object Loading : State()                         |
| **데이터 포함**       | data class를 사용하여 데이터 전달 가능    | data class Error(val msg: String) : State()      |
| **Sealed 인터페이스** | 코틀린 1.5부터 지원 (다른 파일에서도 구현 가능) | sealed interface Animal { class Dog : Animal }   |

## **8. 결론**

✅ **Sealed 클래스는 enum class보다 더 유연한 계층 구조를 가질 수 있음.**
✅ **서브클래스를 제한하여 안전한 타입 설계를 가능하게 함.**
✅ **when과 함께 사용하면 모든 상태를 명확하게 정의할 수 있음.**
✅ **네트워크 응답 처리, 상태 관리, 사용자 입력 이벤트 처리 등 다양한 상황에서 유용하게 활용 가능.**

💡 **Sealed 클래스를 활용하면 코드의 가독성을 높이고, 타입 안정성을 확보할 수 있습니다! 🚀**
