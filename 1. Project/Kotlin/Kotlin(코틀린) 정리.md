# 코틀린 문법 정리 목차

## 1. 코틀린 소개

- 코틀린의 특징과 장점
- JVM과의 연동
- 코틀린 개발 환경 설정 (IntelliJ, Android Studio 등)

## 2. 기본 문법

- 변수와 상수 (var, val)
- 기본 자료형 (숫자, 문자열, 배열 등)
- 함수 정의와 호출
- 주석 처리 방법

## 3. 흐름 제어

- 조건문 (if, else, when)
- 반복문 (for, while, do-while)
- 예외 처리 (try, catch, finally)

## 4. 클래스와 객체

- 클래스 정의
- 생성자 (주 생성자, 부 생성자)
- 프로퍼티와 메서드
- 클래스 상속 및 다형성
- 데이터 클래스
- object 키워드 (싱글톤, 익명 클래스, 동반 객체)

## 5. 함수형 프로그래밍

- 고차 함수와 람다 표현식
- 확장 함수
- 컬렉션 함수 (map, filter, reduce 등)
- inlining 함수

## 6. Null 안전성

- Nullable 타입
- 안전 호출 연산자 (`?.`)
- 엘비스 연산자 (`?:`)
- Not-null 단언 (`!!`)

## 7. 컬렉션

- 리스트, 세트, 맵
- Mutable과 Immutable 컬렉션
- 컬렉션 처리 방법 (map, filter 등)

## 8. 기타 유용한 문법

- 범위 연산자 (`..`, `rangeTo`, `step`)
- 문자열 템플릿
- 타입 캐스팅 (`as`, `is` 연산자)
- 스마트 캐스트
- Enum 클래스
- Sealed 클래스

## 9. 코루틴 (Coroutines)

- 코루틴의 개념과 사용 이유
- `suspend` 함수
- `launch`와 `async`
- 코루틴 스코프와 컨텍스트

## 10. 고급 문법

- 제네릭(Generic)
- reified 타입 파라미터
- 인라인 함수
- 타입 시스템 (Variance, Contravariance)

## 11. 표준 라이브러리 활용

- 표준 라이브러리 개요
- 유용한 표준 함수 (apply, let, run, with, also)
- 파일 입출력
- 컬렉션 라이브러리

## 12. 안드로이드 개발에서의 코틀린

- Android에서 Kotlin 사용하기
- Kotlin Android Extensions
- ViewModel 및 LiveData와의 연동

## 13. 코틀린 문법 참조 사이트 목록

1. **Kotlin 공식 문서**

- 사이트: [https://kotlinlang.org/docs/home.html](https://kotlinlang.org/docs/home.html)
- 설명: 코틀린 공식 사이트로, 코틀린 문법과 언어의 전반적인 기능을 체계적으로 설명하는 문서입니다. 예제 코드와 함께 자세한 설명을 제공합니다.

2. **JetBrains Kotlin Documentation**

- 사이트: [https://kotlinlang.org](https://kotlinlang.org)
- 설명: JetBrains에서 제공하는 코틀린 공식 문서로, 코틀린 언어의 문법뿐만 아니라 코루틴, 멀티플랫폼, 코틀린/JS 등 다양한 주제에 대한 문서를 확인할 수 있습니다.

3. **Exercism (Kotlin Track)**

- 사이트: [https://exercism.org/tracks/kotlin](https://exercism.org/tracks/kotlin)
- 설명: 코틀린 실습 문제를 제공하는 사이트로, 각 문제를 풀며 코틀린 문법을 익힐 수 있습니다. 커뮤니티 리뷰를 통해 코드를 개선할 수 있습니다.

4. **Kotlin Koans**

- 사이트: [https://play.kotlinlang.org/koans](https://play.kotlinlang.org/koans)
- 설명: 코틀린을 학습할 수 있는 단계별 문제 모음집으로, 웹에서 코드를 실행하면서 실습할 수 있습니다. 초보자부터 고급 사용자까지 모두에게 유용합니다.

5. **Codecademy - Learn Kotlin**

- 사이트: [https://www.codecademy.com/learn/learn-kotlin](https://www.codecademy.com/learn/learn-kotlin)
- 설명: Codecademy에서 제공하는 코틀린 입문 과정으로, 기초 문법을 배울 수 있는 코스 형태의 학습을 제공합니다.

6. **Kotlin Playground**

- 사이트: [https://play.kotlinlang.org](https://play.kotlinlang.org)
- 설명: 웹 브라우저에서 코틀린 코드를 바로 작성하고 실행할 수 있는 환경입니다. 코드를 실시간으로 테스트해볼 수 있어 학습에 매우 유용합니다.

7. **Baeldung - Kotlin Tutorials**

- 사이트: [https://www.baeldung.com/kotlin](https://www.baeldung.com/kotlin)
- 설명: 코틀린의 다양한 주제와 기능에 대해 심도 있게 다루는 튜토리얼을 제공합니다. 초보자뿐만 아니라 중급자에게도 유용한 자료가 많습니다.

8. **Programiz - Kotlin Tutorial**

- 사이트: [https://www.programiz.com/kotlin-programming](https://www.programiz.com/kotlin-programming)
- 설명: 간단하고 명확하게 코틀린 문법을 설명하는 튜토리얼 사이트입니다. 코틀린의 기본 문법을 쉽게 학습할 수 있습니다.

9. **Kotlin Documentation - Android Developers**

- 사이트: [https://developer.android.com/kotlin](https://developer.android.com/kotlin)
- 설명: 안드로이드 개발에서 코틀린을 활용하는 방법에 대한 공식 문서로, 코틀린과 안드로이드의 통합된 사용법을 학습할 수 있습니다.

10. **Kotlin by Example**

- 사이트: [https://play.kotlinlang.org/byExample](https://play.kotlinlang.org/byExample)
- 설명: 코틀린의 주요 기능을 간단한 예제를 통해 빠르게 학습할 수 있는 사이트입니다. 예제를 바로 실행하며 이해할 수 있어 매우 직관적입니다.
