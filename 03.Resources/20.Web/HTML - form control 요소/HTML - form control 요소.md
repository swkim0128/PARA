---
type: HTML/CSS
archive: false
---
### 개요

---

사용자로부터 데이터를 입력 받아 서버에서 처리하기 위한 용도로 사용.

사용자의 요청에 따라 서버는 HTML form을 전달(회원가입양식, 검색 양식 등).

사용자는 HTML form에 적절한 데이터를 입력한 후 서버로 전송. 이를 submit이라 함.

서버는 사용자의 요청을 분석한 후 데이터를 등록하거나, 원하는 데이터를 조회하여 결과를 다시 반환.

  

사용자가 입력하기 위한 control 요소들은 모두 <form> tag 하위에 위치해야 서버로 전송됨.

각 control 요소마다 텍스트 입력, 버튼 클릭 등 다양한 형식으로 입력을 받는다.

  

tag명

<form>

<input>

<textarea>

<button>

<select>

<optgroup>

<option>

<label>  
  

<fieldset>

<legend>

설명

사용자에게 입력 받을 항목을 정의. form tag 내부에 여러 개의 control 요소를 포함.

텍스트 box, 체크 box, 라디오 버튼 등 사용자가 데이터를 입력할 수 있도록 함.

여러 줄의 문자를 입력할 수 있도록 함.

버튼을 표시

select box(드롭다운, 콤보box)를 표시.

select box의 각 항목들을 그룹화 함.

select box의 각 항목들을 정의 함.

마우스를 이용하여 <input> 항목을 선택 시 편리함을 제공. for 속성을 이용하여 다른 control 요소와 텍스트를 연결시켜서 더 편리하게 선택할 수 있도록 함.

입력 항목들을 그룹화 함

<fieldset>의 제목을 지정 함.

  

### form

---

사용자가 입력한 자료들을 어떤 방식으로 서버로 전달할 것인지 결정.

서버에서 어떤 프로그램을 이용해 처리할 것인지 결정

<form [속성="속성값"]> form control </form>

속성

  
  
method  
  
  

name  
  

action

target

autocomplete

설명

사용자가 입력한 내용을 서버 쪽 프로그램으로 어떻게 넘겨줄지 지정.  
GET : 주소 표시줄에 사용자가 입력한 내용이 표시. 256 ~ 2048bytes의 데이터만 서버로 전송.  
POST : 사용자의 입력을 표준 입력으로 넘겨주기 때문에 입력 내용의 길이에 제한이없다.  

form의 이름을 지정. 한 문서 안에 여러 개의 <form> 태그가 있을 경우, 구분자로 사용

<form> 태그 안의 내용들을 처리해 줄 서버상의 프로그램 지정(URL)

<action> 태그에서 지정한 스크립트 파일을 현재 창이 아닌 다른 위치에 열도록 지정

자동완성 기능 기본값 on

  

### label

---

form control에 레이블(텍스트)을 연결.

사용법

- <label [속성="속성값"]>레이블<input ...></label>
- <label for="id dlfma"><input id="id이름" [속성="속성값"]> </label>

  

### fieldset, legend

---

```HTML
<form>
	<fieldset>
		<legend>필수 입력</legend>
			<ul type="none">
				<li>
					<label for="userid">아이디 : </label><input type="text" id="userid" name="userid">
				</li>
				<li>
					<label for="pass">비밀번호 : </label><input type="text" id="pass" name="pass">
				</li>
			</ul>
	</fieldset>
	<fieldset>
		<legend>선택 입력</legend>
			<ul type="none">
				<li>
					<label for="phone">전화번호 : </label><input type="text" id="phone" name="phone">
				</li>
				<li>
					<label for="address">주소 : </label><input type="text" id="address" name="address">
				</li>
			</ul>
	</fieldset>
</form>
```

  

### input

---

<input> tag는 type 속성에 따라 여러 가지 형태로 화면에 표시.

<input type="유형" [속성="속성값"]>

id 속성은 여러 번 사용된 폼 요소를 구분하기 위해 사용.

id 속성 값은 최한 한 개 이상의 문자여야 하며 공백은 허용 X.

같은 html document에서 id는 하나의 값만 가능하고, name은 중복이 허용된다.

  

type

text

password

search

tel

url

email

datetime

datetime-local

date

month

week

time

number

range

color

checkbox

radio

file

submit

image

reset

button

hidden

설명

한 줄의 텍스트를 입력할 수 있는 텍스트 상자.

비밀번호를 입력할 수 있는 필드.(text가 '*'로 표시)

검색 상자.

전화번호를 입력할 수 있는 필드.

URL 주소를 입력할 수 있는 필드

메일 주소를 입력할 수 있는 필드.

국제 표준시(UTC)로 설정된 날짜와 시간(년, 월, 일, 시, 분, 초, 분할 초).

사용자 지역을 기준으로 날짜와 시간(년, 일, 시, 분, 초, 분할 초)

사용자 지역을 기준으로 날짜(년, 월, 일).

사용자 지역을 기준으로 날짜(년, 월).

사용자 지역을 기준으로 날짜(년, 주).

사용자 지역을 기준으로 시간(시, 분, 초 , 분할 초)

숫자를 조절할 수 있는 화살표.

숫자를 조절할 수 있는 슬라이드 막대.

색상 표.

주어진 항목에서 2개 이상 선택 가능한 체크박스(다중선택).

주어진 항목에서 1개만 선택할 수 있는 라디오 버튼(단일 선택).

파일을 첨부할 수 있는 버튼.

서버 전송 버튼.

submit + image.

리셋 버튼.

기능이 없는 버튼.

사용자에게는 보이지 않지만 서버로 넘겨지는 값을 설정.

  

### input - 속성

---

속성

name

size

value

maxlength

설명

textfield를 구별할 수 있도록 이름을 정함.

textfield의 길이를 지정. 화면에 몇 글자가 보이도록 할 것인지를 지정(글자수 제한 X).

textfield가 화면에 보일 때 textfield 부분에 표시 될 내용.

textfield에 입력할 수 있는 최대 문자수를 지정.

  

속성

autofocus  
  

placeholder  
  

readonly  
  

required  
  

  
min, max, step  
  

size, minlength,  
maxlength  

height, width

list

multiple

설명

페이지를 불러 오자마자 폼의 요소 중에서 원하는 요소에 마우스 커서를 표시.  
html5이전에는 자바스크립트로 구현.  

텍스트를 입력할 때 도움이 되도록 입력란에 적당한 힌트 내용을 표시.  
클릭시 자동으로 내용이 사라짐.  

입력란에 텍스트를 사용자가 직접 입력하지 못하게 읽기 전용으로 지정.  
readonly, readonly="readonly", readonly="true"로 표현.  

form에 data를 입력한 후 submit 클릭시 data를 서버로 전송하기 전 필수 입력 항목을 체크. required, requiered="required"로 표현.

min, max는 해당 필드의 최대, 최소값지정. step은 일정 간격 지정.  
type이 date, datetime, datetime-local, month, week, time, number, range에서 사용.  

minlegnth, maxlength는 텍스트 입력시 최대, 최소 길이 지정. size는 화면에 보여지는 글자의 길이 지정.

type="image"일 때 이미지의 너비와 높이를 지정.

<datelist>에 미리 정의해 놓은 옵션 값을 <input> 안에 나열해 보여줌.

type="email"이나 type="file"일 때 두 개 이상의 값을 입력. <input> 태그 안에 속성 이름만 표시하면 됨.

  

### 여러 data 나열

---

<select> - select box(dropdown)를 표시.

<option> - select box에 포함될 항목들을 정의.

![[Untitled 50.png|Untitled 50.png]]

<optgroup> - dropdown 목록에서 열 항목들을 몇 가지 그룹으로 묶을 경우.

![[Untitled 1 28.png|Untitled 1 28.png]]

  

**datalist**

<input>과 함계 사용하며 텍스트필드에 직접 값을 입력하는 것이 아니라 datalist의 선택 값이 텍스트 필드에 입력됨.

```HTML
<input type="text" list='datalist id'>
<datalist id='datalist id'>
	<option>...</option>
	<option>...</option>
	...
</datalist>
```

![[Untitled 2 27.png|Untitled 2 27.png]]

  

### 여러 줄 입력 - textarea

---

<textarea> tag는 여러 줄을 입력할 수 있는 box를 표시.

cols와 rows 속성은 text box의 크기를 지정.

<textarea></textarea> tag 사이의 문자열은 text box에 표시.

disabled 속성은 화면에 표시는 하되 데이터를 수정할 수 업도록 비활성화 상태로 표시

![[Untitled 3 26.png|Untitled 3 26.png]]

  

### 기타 form control

---

**button**

<button> 태그의 type 속성은 버튼이 활성화 되었을때 어떤 동작을 할지 지정. 기본은 submit

<button [type='submit | reset | button']>내용</button>

input과의 차이점은 <button> 태그는 contents를 포함할 수 있기 때문에 아이콘을 추가할 수 있고, CSS를 이용하여 원하는 형태로 꾸밀 수 있다.

![[Untitled 4 22.png|Untitled 4 22.png]]

  

**progress**

작업의 진행 상태를 표시.

작업의 시작을 0, 최종 완료를 최대값으로 설정.

<progress value='값' [max='값']></progress>

![[Untitled 5 20.png|Untitled 5 20.png]]

  

**meter**

값이 차지하는 크기 표시.

<pregress>와 결과 화면은 비슷하지만 차이점은 <progress>는 작업의 진행 상황을 나타내는 반면, <meter>는 전체 크기 중에서 얼마나 차지하는지를 표현.

<meter value='값' [속성='속성값']></meter>

![[Untitled 6 17.png|Untitled 6 17.png]]