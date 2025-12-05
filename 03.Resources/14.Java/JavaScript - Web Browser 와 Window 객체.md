---
type: JavaScript
archive: false
---
### Window 객체 개요

---

Window 객체는 웹 브라우저에서 작동하는 JavaScript의 최사위 전역객체이다.

Window 객체에는 브라우저와 관련된 여러 객체의 속성, 함수가 있다.

JavaScript에서 기본으로 제공하는 프로퍼티와 함수도 포함. (Number 객체, setInterval() 함수 등)

BOM(Browser Object Model)으로 불리기도 함.

  

### Window 객체 사용

---

window 객체의 함수를 호출하면 브라우저에서 제공하는 창을 open.

alert() : 브라우저의 알림창

confirm() : 브라우저의 확인 / 취소 선택창.

prompt() : 브라우저의 입력 창.

  

navigator

navigator 객체는 브라우저의 정보가 내장된 객체.

navigator의 정보로 서로 다른 브라우저를 구분할 수 있으며, 브라우저 별로 다르게 처리 가능.

HTML5에서는 위치 정보를 알려주는 역할 가능.

location

location 객체를 이용하여 현재 페이지 주소(URL)와 관련된 정보들을 알 수 있다.

- location.href : 프로퍼티에 값을 할당하지 않으면 현재 URL을 조회하고 값을 할당하면 할당된 URL로 페이지 이동.
- location.reload() : 현재 페이지를 새로고침.

history

history 객체는 브라우저의 페이지 이력을 담는 객체

- history.back() / history.forward() : 브라우저의 뒤로 가기 / 앞으로 가기 버튼과 같은 동작.

  

### 새 창 열기

---

window 객체의 open() 함수를 사용하면 새 창을 열 수 있다.

window.open('페이지 URL', '창이름', '특성', 히스토리 대체여부);

- 창이름(string) : open 할 대상(_blank, _self 등) 지정 혹은 창의 이름.
- 특성(string) : 새로 열릴 창의 너비, 높이 등의 특성 지정.
- 히스토리 대체 여부(Boolean) : 현재 페이지 히스토리에 덮어 쓸지 여부(true / false)

  

이벤트를 이용하여 특정 시점에 창을 열 수 있다.

- 페이지 로딩 완료 후 새 창 열기, 클릭할 때 새 창 열기 등.

window 객체의 close() 함수로 현재 창을 닫을 수 있다.

특히 브라우저에 내장 된 창이 아닌 JavaScript로 자체 구현한 팝업에서 필요.

  

window 객체의 opener 속성을 이용하면 부모 창(새 창을 연 창)을 컨트롤 가능.

- 부모 창에 값 전달.
- 부모 창을 새로 고침 하거나 페이지 이동.

opener 객체는 부모 창의 window 객체.

  

### Window 객체 프로퍼티

---

window 객체는 웹 브라우저에서는 구동 되는 JavaScript의 전역 객체.

document 객체는 HTML 문서와 관련된 객체로 가장 많이 사용하는 객체.

screen 객체는 화면의 가로, 세로 크기 정보를 알 수 있다.

pageYOffset 등과 scroll() 함수를 이용하면 현재 화면의 크기를 계산하여 페이지 단위로 스크롤 제어가 가능.

  

self

document

history

location

opener  
  

parent  
  

top

frames  
  

locationbar

menubar

현재 창 자신, window와 같음

document 객체

history 객체

location 객체

open()으로 열린 창에서 볼 때 자기를 연 창

프레임에서 현재프레임의 상위프레임

현재 프레임의 최상위 프레임

창안의 모든 프레임에 대한 배열 정보

location 바

창 메뉴바

statusbar

toolbar

personalbar

scrollbars

innerHeight  
  

innerWidth

outerHeight

outerWidth

pageXOffset  
  

pageYOffset  
  

창의 상태 바

창의 툴 바

창의 퍼스널 바

창의 스크롤 바

창 표시 영역의 높이(픽셀)

창 표시 영역의 너비

창 바깥쪽 둘레의 높이

창 바깥쪽 둘레의 너비

현재 나타나는 페이지의 X 위치

현재 나타나는 페이지의 Y 위치

  

### Window 객체 함수

---

브라우저에서 버튼으로 제공하는 기능인 find, stop, print와 같은 함수도 있다.

move 함수로 현재 열려 있는 창의 위치를 이동 가능.

alert()

confirm()

prompt()

open()

scroll()

find()

stop()

print()

moveBy()

moveTo()

경고용 대화상자를 보여줌

확인, 최소를 선택할 수 있는 대화상자를 보여줌.

입력창이 있는 대화 상자를 보여줌.

새로운 창을 오픈

창을 스크롤 함

항안에 지정된 문자열이 있는지 확인. 있으면 true, 없으면 false

불러오기를 중지

화면에 있는 내용을 프린터로 출력

창을 상대적 좌표로 이동. 수평방향과 수직방향의 이동량을 픽셀로 지정.

창을 절대적 좌표로 이동. 창의 왼쪽 상단 모서리를 기준으로 픽셀로 지정.

  

resize 함수로 현재 열려 있는 창의 크기 조절.

window 객체에는 브라우저와 관련 된 함수 뿐만 아니라 순수 JavaScript에서 필요한 객체나 함수 존재.

- setTimeout() 함수와 setInterval() 함수로 함수를 특정 시간 후 혹은 특정 시간마다 호출가능.
- eval() 함수는 문자열로 된 JavaScript 코드를 해석한 후 실행.

resizeBy()

resizeTo()

scrollBy()  
  

scrollTo()

setTimeout()

clearTimeout()

setInterval()

clearInterval()

eval()

창의 크기를 상대적인 좌표로 재설정.

창의 크기를 절대적인 좌표로 재설정. 창 크기를 픽셀로 지정.

창을 상대적인 좌표로 스크롤. 창의 표시영역의 수평방향과 수직방향에 대해 픽셀로 지정.

창을 절대적인 좌표를 스크롤 창의 왼쪽 상단 모서리를 기준으로 픽셀로 지정.

지정한 밀리초 시간이 흐른 후에 함수 호출.

setTimeout 함수를 정지.

지정한 밀리초 주기마다 함수를 반복적으로 호출.

setInterval 함수를 정지

문자열을 JavaScript 코드로 변환하여 실행.