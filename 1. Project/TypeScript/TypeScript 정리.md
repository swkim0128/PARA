# TypeScript 정리 목차

## 1. 타입스크립트 소개

- 타입스크립트란 무엇인가
- 자바스크립트와의 차이점
- 타입스크립트의 장점과 단점
- 타입스크립트 설치 및 설정

## 2. 타입스크립트의 기본 문법

- 기본 타입 (string, number, boolean 등)
- 배열과 튜플
- 객체 타입 정의
- `any`와 `unknown` 타입
- `null`, `undefined`, `void` 타입

## 3. 타입 추론 (Type Inference)

- 타입 추론의 기본 개념
- 타입 추론과 명시적 타입 지정
- 타입 좁히기 (Type Narrowing)

## 4. 함수

- 함수의 타입 선언
- 선택적 매개변수와 기본 매개변수
- 함수 타입 (콜백 함수)
- 함수 오버로드 (Function Overloading)
- 화살표 함수에서의 타입 지정

## 5. 인터페이스와 타입 별칭

- 인터페이스의 개념과 사용법
- 인터페이스 상속
- 타입 별칭 (Type Alias)
- 인터섹션 타입과 유니언 타입

## 6. 제네릭(Generic)

- 제네릭의 개념과 필요성
- 제네릭 함수와 클래스
- 제네릭 제약 조건 (Constraints)
- 제네릭 타입 추론

## 7. 고급 타입

- 유니언 타입(Union Types)과 교차 타입(Intersection Types)
- 리터럴 타입(Literal Types)
- 조건부 타입 (Conditional Types)
- 맵드 타입(Mapped Types)과 인덱스 시그니처
- 타입 가드(Type Guards)

## 8. 클래스

- 클래스와 인터페이스
- 접근 제한자 (`public`, `private`, `protected`)
- 클래스 상속과 `super`
- 추상 클래스 (Abstract Class)
- `readonly` 프로퍼티와 메서드

## 9. 모듈과 네임스페이스

- 모듈 시스템 (`import`, `export`)
- 모듈 간 상호작용
- 네임스페이스 (Namespace)
- 외부 모듈 사용 (`@types`와 DefinitelyTyped)

## 10. 타입스크립트에서의 DOM 조작

- DOM 요소의 타입 지정
- 타입 단언 (Type Assertion)
- `HTMLElement`, `HTMLInputElement` 등 구체적 타입
- 이벤트 처리와 이벤트 객체 타입 지정

## 11. 유틸리티 타입 (Utility Types)

- `Partial`, `Required`, `Readonly`, `Pick`, `Omit`
- `Record` 타입과 `Exclude`, `Extract`
- `NonNullable`, `ReturnType`, `Parameters`

## 12. 타입스크립트와 자바스크립트 통합

- 자바스크립트 라이브러리와의 통합
- 자바스크립트로 작성된 코드에 타입 적용
- 자바스크립트 파일에 타입 정의 (`.d.ts`)
- JSDoc을 사용한 타입스크립트 지원

## 13. 타입스크립트의 컴파일러 옵션

- `tsconfig.json` 설정
- 중요한 컴파일러 옵션 (`strict`, `target`, `module` 등)
- 소스 맵(Source Map)과 디버깅

## 14. 타입스크립트와 테스트

- 타입스크립트에서 테스트 도구 설정
- Jest와 타입스크립트 통합
- 타입스크립트 코드 테스트하기

## 15. 타입스크립트와 프레임워크

- 타입스크립트와 React
- 타입스크립트와 Node.js
- 타입스크립트와 Angular
- 타입스크립트와 Vue.js

## 16. 타입스크립트의 고급 기능

- `keyof`와 인덱스 타입 쿼리
- `infer` 키워드와 타입 추론
- 템플릿 리터럴 타입 (Template Literal Types)
- 네버 타입 (`never`)

## 17. 타입스크립트의 성능 최적화

- 타입스크립트 코드 최적화 전략
- 타입스크립트 컴파일 성능 최적화
- 대규모 프로젝트에서의 타입 관리

## 18. 타입스크립트와 배포

- 타입스크립트 코드를 자바스크립트로 컴파일하기
- 번들링 도구와 타입스크립트 (Webpack, Rollup, Parcel)
- 타입스크립트 코드의 배포 전략
