
코루틴에서 **비동기 작업을 실행하는 두 가지 주요 방식**은 launch와 async다.

두 방식 모두 코루틴을 생성하지만, **launch는 결과를 반환하지 않고**, **async는 결과를 반환하며 await()를 사용하여 값을 가져올 수 있다.**

## 1. launch와 async의 차이점

| **비교 항목** | launch                    | async                     |
| --------- | ------------------------- | ------------------------- |
| 반환 값      | Job 객체 반환 (결과 없음)         | Deferred<T> 객체 반환 (결과 있음) |
| 실행 방식     | 독립적인 비동기 실행               | 값을 반환하는 비동기 실행            |
| 실행 결과     | 단순 실행 후 완료                | .await() 호출 시 값 반환        |
| 예외 처리     | 즉시 예외 발생                  | .await() 호출 시 예외 발생       |
| 사용 예      | 로그 출력, UI 업데이트, 네트워크 요청 등 | 계산 결과를 반환해야 하는 경우         |

## 2. launch 사용법 (결과 반환 없음)

launch는 비동기적으로 실행되지만, 결과를 반환하지 않는다.
주로 백그라운드 작업, 로그 출력, 데이터 저장 등의 작업에서 사용된다.

### launch 예제

```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val job = launch {
        delay(1000L) // 1초 대기
        println("launch 실행 완료!")
    }
    
    println("메인 실행 중...")
    job.join() // 코루틴이 끝날 때까지 대기
}
```

출력 결과:

```plain text
메인 실행 중...
(1초 후)
launch 실행 완료!
```

### launch 특징

- launch는 **결과 값을 반환하지 않음** (Job 객체 반환).
- job.join()을 사용하면 **해당 작업이 완료될 때까지 기다릴 수 있음**.

## 3. async 사용법 (결과 반환 가능)

async는 비동기적으로 실행하면서 결과 값을 반환하는 작업에 사용된다.
.await()을 사용하여 값을 가져올 수 있다.

### async 예제

```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val deferred = async {
        delay(1000L) // 1초 대기
        "async 실행 완료!"
    }

    println("메인 실행 중...")
    println(deferred.await()) // 결과를 기다린 후 출력
}
```

출력 결과:

```plain text
메인 실행 중...
(1초 후)
async 실행 완료!
```

### async 특징

- async는 비동기적으로 값을 계산하고 결과를 반환함 (Deferred\<T\> 반환).
- .await()을 호출하면 **해당 값이 준비될 때까지 기다린 후 반환**.

## **4. launch vs async 실행 흐름 비교**

### launch

```kotlin
fun main() = runBlocking {
    launch {
        delay(1000L)
        println("launch 실행 완료!")
    }
    println("메인 실행 중...")
}
```

출력:

```plain text 
메인 실행 중...
(1초 후)
launch 실행 완료!
```

- launch는 백그라운드에서 실행되며 결과 반환이 필요하지 않다.

### async

```kotlin
fun main() = runBlocking {
    val result = async {
        delay(1000L)
        "결과 반환 완료!"
    }
    println("메인 실행 중...")
    println(result.await()) // 결과를 기다린 후 출력
}
```

출력:

```plain text
메인 실행 중...
(1초 후)
결과 반환 완료!
```

- async는 값을 반환해야 하므로 await()을 호출해야 한다.

## 5. 여러 개의 비동기 작업 실행 (async 활용)

병렬 실행 예제

```kotlin
import kotlinx.coroutines.*

suspend fun fetchData1(): String {
    delay(1000L)
    return "데이터 1"
}

suspend fun fetchData2(): String {
    delay(2000L)
    return "데이터 2"
}

fun main() = runBlocking {
    val result1 = async { fetchData1() }
    val result2 = async { fetchData2() }

    println("데이터 로드 중...")
    println("${result1.await()} + ${result2.await()}")
}
```

출력:

```plain text
데이터 로드 중...
(1초 후)
(1초 후)
데이터 1 + 데이터 2
```

- async는 **각각의 작업을 병렬로 실행할 수 있음**.

## 6. async에서 start()를 사용한 즉시 실행

기본적으로 async는 **await()을 호출할 때 실행이 시작**되지만,
.start()를 호출하면 **즉시 실행된다.**

```kotlin
fun main() = runBlocking {
    val deferred = async(start = CoroutineStart.LAZY) {
        delay(1000L)
        "지연 실행 완료!"
    }

    delay(500L)
    println("메인 실행 중...")
    println(deferred.await()) // 여기서 실행됨
}
```

출력:

```
메인 실행 중...
(1초 후)
지연 실행 완료!
```

## **7. launch와 async의 예외 처리 차이**

- launch는 **예외 발생 시 즉시 프로그램이 종료됨**.
- async는 **예외가 발생해도 await()을 호출할 때 예외가 발생함**.

launch 예외 처리

```kotlin
fun main() = runBlocking {
    val job = launch {
        throw Exception("launch 예외 발생!")
    }
    job.join()
    println("실행되지 않음")
}
```

- launch에서 예외 발생 시 **즉시 프로그램이 종료됨**.

async 예외 처리

```kotlin
fun main() = runBlocking {
    val deferred = async {
        throw Exception("async 예외 발생!")
    }
    
    try {
        println(deferred.await()) // 예외 발생 지점
    } catch (e: Exception) {
        println("예외 처리됨: ${e.message}")
    }
}
```

출력:

```plain text
예외 처리됨: async 예외 발생!
```

- async의 예외는 .await()을 호출할 때 발생하므로 예외 처리가 가능함.

## 8. 결론: 언제 launch와 async를 사용할까?

| **사용 목적**     | launch               | async            |
| ------------- | -------------------- | ---------------- |
| 실행 후 결과 필요 여부 | ❌ 필요 없음              | ✅ 필요함            |
| 반환 값          | 없음 (Job)             | 있음 (Deferred<T>) |
| 실행 방식         | 독립적 실행               | 병렬 실행 후 결과 반환    |
| 예외 처리         | 즉시 발생                | .await() 호출 시 발생 |
| 주요 사용 사례      | 로그, UI 업데이트, 네트워크 요청 | 데이터 로드, 계산 작업    |

**launch는 백그라운드 작업을 실행할 때**,
**async는 비동기 계산 결과가 필요할 때 사용하면 된다.**

## 9. 최종 요약

- launch는 **결과 반환 없이 비동기 실행 (UI 업데이트, 로그 출력)**
- async는 **결과를 반환하는 비동기 실행 (await() 필요)**
- launch는 예외 발생 시 **즉시 종료**, async는 **.await() 호출 시 예외 발생**
- async는 **동시에 여러 작업을 실행할 때 유용** (병렬 실행 가능)

코루틴을 활용하면 **효율적이고 가독성 높은 비동기 프로그래밍을 구현할 수 있다.**
