---
type: JavaScript
archive: false
---
### DOM 탐색

---

javaScript에서 DOM 탐색

DOM 객체는 JavaScript를 사용하여 DOM을 탐색하고 조작하는 API를 제공.

주로 document 객체를 사용하여 요소의 id, class, name 또는 태그 이름을 이용하여 DOM 요소를 탐색.

탐색한 DOM 요소 객체를 통해, 필요한 정보를 조회하거나 조작할 수 있다.

그러나, DOM 객체에서 제공하는 API를 사용하면, 단순한 작업임에도 적지 않은 코드를 작성해야 한다.

![[Untitled 36.png|Untitled 36.png]]

  

jQuery에서 DOM 탐색.

jQuery는 DOM 탐색을 위하여 CSS에서 사용하는 Selector 표현 방식을 사용.

브라우저가 표준 CSS 선택자를 올바르게 구현하지 않았더라도, jQuery는 W3C 표준에 맞게 요소를 탐색.

jQuery Selector는 CSS Selectro와 jQuery에서 정의한 다양한 방법으로 DOM 요소를 탐색.

jQuery는 DOM 탐색 결과로 패러세트(Wrapper set)라는 DOM을 래핑한 객체를 반환

![[Untitled 1 15.png|Untitled 1 15.png]]

  

### 선택자(Selector)

---

Selector를 이용한 DOM Element의 검색.

- CSS 문법을 확장해서 태그를 찾는 selector 제공
- 특정 브라우저에 의존적인 스크립팅을 벗어 날 수 있음.

  

jQuery function의 기본 형식

![[Untitled 2 14.png|Untitled 2 14.png]]

  

### DOM 요소 탐색 - 요소 선택자(Element Selector)

---

jQuery 선택자(Selector)는 DOM 객체를 탐색하여 래퍼세트 객체로 반환.

jQuery 선택자에는 요소, ID, 클래스, 다중, 복합 그리고 모두 선택자 등이 있다.

selector 종류

All selector

ID selector

Element selector

Class selector

Multiple selector

selector 표현방법

$(*)

$("\#id")

$("elementName")

$(".className")

$("selector1, selector2, selector3, ...")

  

### DOM 계층 구조 탐색 - Hierarchy Selector

---

jQuery는 HTML DOM 계층 구조에 접근하고 제어하는 쉬운 방법을 제공.

DOM을 탐색할 때, 트리 형태의 DOM 계층구조를 이해하는 것은 중요.

DOM 계층 구조가 나타내는 다양한 관계를 이해하면 DOM을 탐색하는데 도움.

DOM 요소들은 수평적으로 형제요소, 수직적으로는 부모, 자식, 자손, 조상요소로 관계를 구분.

![[Untitled 3 13.png|Untitled 3 13.png]]

  

$("Parent > child")는 자식 선택자로, 바로 인접한 하위 자식들을 탐색

$("Ancestor Descendant")는 자손 선택자로, 모든 하위 자식들을 탐색

$("Previous + Next")는 인접 선택자로, 인접한 바로 다음 형재를 탐색

$("Previous ~ Next")는 형제 선택자로, Next에 대한 모든 형제들을 탐색.

  

### DOM 속성 탐색 - 속성선택자(Attribute Selector).

---

![[Untitled 4 11.png|Untitled 4 11.png]]

  

### DOM 속성 탐색 - 필터선택자(Filter Selector).

---

![[Untitled 5 10.png|Untitled 5 10.png]]

  

### DOM 속성 탐색 - 위치기반 필터선택자.

---

![[Untitled 6 8.png|Untitled 6 8.png]]

  

### DOM 속성 탐색 - 함수기반 필터선택자.

---

![[Untitled 7 7.png|Untitled 7 7.png]]

  

### jQuery method - 래퍼세트와 메소드

---

jQuery는 선택자를 통해 탐색한 DOM 객체들을 래퍼세트라는 특별한 배열 객체에 담아 반환합니다.

jQuery는 선택된 DOM 객체가 없는 경우에도, 비어있는 래퍼세트 객체를 반환합니다.

래퍼세트 객체에는 내포된 DOM 객체들을 처리하는 다양한 메소드가 있습니다.

이러한 jQuery 메소드는 플러그-인 확장을 통해 추가할 수 있습니다.

![[Untitled 8 6.png|Untitled 8 6.png]]

  

### jQuery method - 계층 구조 탐색.

---

jQuery는 선택자를 통해 탐색한 DOM 객체들을 래퍼세트라는 특별한 배열 객체에 담아 반환합니다.

jQuery는 선택된 DOM 객체가 없는 경우에도, 비어있는 래퍼세트 객체를 반환합니다.

래퍼세트 객체에는 내포된 DOM 객체들을 처리하는 다양한 메소드가 있습니다.

이러한 jQuery 메소드는 플러그-인 확장을 통해 추가할 수 있습니다.

![[Untitled 9 6.png|Untitled 9 6.png]]

  

### jQuery method - 요소 반복.

---

jQuery.each() 함수는 배열이나 객체를 반복적으로 처리할 때 사용.

콜백 함수는두 개의 매개변수(index: 배열 인덱스, item: 반복하는 요소객체)를 갖는다.

![[Untitled 10 5.png|Untitled 10 5.png]]

![[Untitled 11 4.png|Untitled 11 4.png]]

  

### jQuery method - 필터 함수.

---

filter()는 래퍼 세트에 포함된 DOM 요소를 주어진 조건으로 걸러내는 메소드.

![[Untitled 12 4.png|Untitled 12 4.png]]

![[Untitled 13 4.png|Untitled 13 4.png]]

  

### jQuery method - 위치기반 함수

---

위치 기반 함수는 HTML DOM 객체의 특정 위치를 선택할 수 있는 함수.

![[Untitled 14 4.png|Untitled 14 4.png]]

  

### jQuery method - 래퍼세트에 요소 추가 / 삭제.

---

jQuery는 래퍼세트에 요소를 추가하거나 특정 요소를 삭제하는 메소드를 제공합니다.

add() 메소드는 래퍼세트에 주어진 조건을 만족하는 요소를 추가한 새로운 래퍼세트를 반환합니다.

not() 메소드는 래퍼세트에서 주어진 조건에 해당하는 요소를 제거한 새로운 래퍼세트를 반환합니다.

![[Untitled 15 3.png|Untitled 15 3.png]]

  

### jQuery method - DOM 요소 판별.

---

is() 메소드는 기존 래퍼세트가 주어진 선택자와 일치하는지 여부를 반환.

![[Untitled 16 3.png|Untitled 16 3.png]]

  

### jQuery method - 자손 요소 탐색

---

$(selector).find(selector);

find() 메소드는 래퍼세트의 모든 요소들에 대하여 주어진 선택자를 만족하는 모든 자손 요소를 선택.