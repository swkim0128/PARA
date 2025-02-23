## 1. suspend 함수 개념

suspend 함수는 **코루틴에서 실행될 수 있는 함수**로, **비동기 작업을 일시 중단(suspend)하고, 다시 재개(resume)할 수 있도록 설계된 함수**다.

특징:

- **일반 함수와 다르게, 코루틴 내에서 실행해야 한다.**
- **코루틴의 실행을 차단하지 않고 중단했다가 나중에 다시 실행할 수 있다.**
- **비동기 작업(네트워크 요청, 데이터베이스 연산 등)에서 사용된다.**

## 2. suspend 함수의 기본 사용법

```kotlin
import kotlinx.coroutines.*

suspend fun doWork() {
    delay(1000L) // 1초 동안 중단
    println("작업 완료!")
}

fun main() = runBlocking {
    doWork() // suspend 함수 호출
    println("메인 함수 종료")
}
```

출력 결과:

```plain text
(1초 후)
작업 완료!
메인 함수 종료
```

코드 설명:

- suspend fun doWork() → **일시 중단 가능한 함수**
- delay(1000L) → **1초 동안 중단되었다가 재개**
- runBlocking 내에서 실행 → suspend 함수는 반드시 **코루틴 내에서 호출**해야 한다.

## 3. suspend 함수의 실행 흐름

suspend 함수는 호출될 때 **현재 코루틴을 블로킹하지 않고, 실행을 중단(suspend)한 후, 특정 시점에서 다시 재개(resume)** 된다.

```kotlin
suspend fun process() {
    println("작업 시작")
    delay(2000L) // 2초 동안 중단됨
    println("작업 완료")
}
```

- delay(2000L)에서 **현재 코루틴이 중단되었다가**,
- 2초 후 **자동으로 다시 실행**된다.

## 4. suspend 함수와 withContext

suspend 함수는 일반적으로 **다른 코루틴 컨텍스트(스레드)에서 실행할 수 있다.**

이를 위해 withContext()를 사용하면 **코드를 특정 디스패처(Dispatchers)에서 실행하도록 변경할 수 있다.**

```kotlin
import kotlinx.coroutines.*

suspend fun fetchData(): String {
    return withContext(Dispatchers.IO) {
        delay(1000L) // 네트워크 요청을 가정
        "데이터 로드 완료"
    }
}

fun main() = runBlocking {
    println("데이터 요청 중...")
    val result = fetchData()
    println(result) // 출력: 데이터 로드 완료
}
```

withContext()의 역할

- Dispatchers.IO → I/O 작업(파일, 네트워크)을 실행하는 스레드에서 실행됨
- **코루틴을 블로킹하지 않고** 특정 스레드에서 작업을 실행

## 5. suspend 함수는 코루틴 내에서만 호출 가능

suspend 함수는 반드시 **코루틴 내부에서 호출해야 한다.**
즉, runBlocking 또는 launch, async 같은 **코루틴 빌더 내부에서 호출해야 함**.

```kotlin
suspend fun doSomething() {
    println("작업 수행 중...")
}

// 오류 발생: suspend 함수는 코루틴 내에서 호출해야 함
fun main() {
    doSomething() // ❌ 컴파일 오류 발생
}
```

올바른 호출 방식:

```
fun main() = runBlocking {
    doSomething() // ✅ 정상 동작
}
```

## 6. suspend 함수에서 다른 suspend 함수 호출

suspend 함수는 다른 suspend 함수를 호출할 수 있다.

```kotlin
import kotlinx.coroutines.*

suspend fun doWork() {
    delay(1000L)
    println("작업 완료!")
}

suspend fun process() {
    println("작업 시작")
    doWork() // 다른 suspend 함수 호출
    println("모든 작업 완료!")
}

fun main() = runBlocking {
    process()
}
```

출력 결과:

```plain text
작업 시작
(1초 후)
작업 완료!
모든 작업 완료!
```

## 7. suspend 함수와 launch, async 차이

- launch → 결과를 반환하지 않고, 백그라운드에서 실행.
- async → 결과를 반환하며, await()으로 값을 받을 수 있음.

```kotlin
import kotlinx.coroutines.*

suspend fun fetchData(): String {
    delay(1000L)
    return "데이터 가져오기 완료"
}

fun main() = runBlocking {
    val job = launch {
        println("launch 실행 중...")
        fetchData() // 실행되지만 결과 반환 없음
    }

    val result = async {
        fetchData() // 실행 후 결과 반환
    }.await()

    println(result) // 출력: 데이터 가져오기 완료
}
```

## 8. suspend 함수의 주요 특징 정리

| **개념**                  | **설명**                      |
| ----------------------- | --------------------------- |
| suspend 키워드             | 코루틴 내에서만 실행할 수 있는 함수        |
| delay(time)             | 일정 시간 동안 중단(suspend) 후 재개   |
| withContext(dispatcher) | 특정 디스패처(IO, Default 등)에서 실행 |
| launch {}               | 백그라운드에서 실행(결과 없음)           |
| async {}                | 비동기 실행 후 결과 반환 (await() 필요) |
| runBlocking {}          | 코루틴을 블로킹하며 실행               |

## 9. 결론

- suspend 함수는 **코루틴에서 실행되는 함수**이며, 실행을 일시 중단(suspend)했다가 나중에 재개(resume)할 수 있다.
- 일반 함수처럼 실행되지만, 내부적으로 **비동기적으로 처리되며, 실행을 차단하지 않는다.**
- withContext를 사용하면 특정 스레드에서 suspend 함수를 실행할 수 있다.
- suspend 함수는 반드시 코루틴 내부에서 실행해야 한다.

suspend 함수를 활용하면 가독성이 높고 효율적인 비동기 프로그래밍을 구현할 수 있다.
