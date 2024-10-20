---
type: HTML/CSS
archive: false
---
## CSS 링크

링크(link)에는 color, font-family, background 속성 등 CSS의 다양한 속성들을 적용할 수 있습니다.

또한, text-decoration 속성값을 none으로 설정하여, 링크가 연결된 텍스트의 밑줄을 제거할 수도 있습니다.

```HTML
<style>
a {
background-color: **\#FFFFE0**;
color: darkslategray;
font-size: **1.3em**;
text-decoration: none;
}
</style>
```

### 링크(link)의 상태

---

링크는 총 5가지의 상태를 가지며, 각 상태마다 다른 스타일을 적용할 수 있습니다.

1. link : 링크의 기본 상태이며, 사용자가 아직 한 번도 해당 링크를 통해 연결된 페이지를 방문하지 않은 상태입니다.

2. visited : 사용자가 한 번이라도 해당 링크를 통해 연결된 페이지를 방문한 상태입니다.

3. hover : 사용자의 마우스 커서가 링크 위에 올라가 있는 상태입니다.

4. active : 사용자가 마우스로 링크를 클릭하고 있는 상태입니다.

5. focus : 키보드나 마우스의 이벤트(event) 또는 다른 형태로 해당 요소가 포커스(focus)를 가지고 있는 상태입니다.

```HTML
<style>
a:link { color: olive; }
a:visited { color: brown; }
a:hover { color: coral; }
a:active { color: khaki; }
</style>
```

### 링크를 활용한 버튼(Button)

---

CSS를 이용하면 간단하게 링크를 버튼처럼 만들 수 있습니다.

```HTML
<style>
a:link, a:visited {
background-color: **\#FFA500**;
color: maroon;
padding: **15px** **25px**;
text-align: center;
text-decoration: none;
display: inline-block;
}
a:hover, a:active { background-color: **\#FF4500**; }
</style>
```

  

## CSS 리스트

> [!important]  
> CSS를 이용하면 리스트에 다양한 효과를 적용할 수 있습니다.순서가 없는 리스트(unordered list)순서가 있는 리스트(ordered list)정의 리스트(definition list)  

CSS에서 사용할 수 있는 list-style 속성은 다음과 같습니다.

1. list-style-type

2. list-style-image

3. list-style-position

### list-style-type 속성

---

리스트 요소의 앞에 위치하는 숫자나 기호를 마커(marker)라고 합니다.

list-style-type 속성을 이용하면 리스트에 다양한 마커(marker)를 적용할 수 있습니다.

```HTML
<style>
.circle { list-style-type: circle; }
.square { list-style-type: square; }
.upperAlpha { list-style-type: upper-alpha; }
.lowerRoman { list-style-type: lower-roman; }
</style>
```

사용할 수 있는 마커(marker)에 대한 더 자세한 사항은 HTML 리스트 수업에서 확인할 수 있습니다.

[HTML 리스트 수업 확인 =>](http://www.tcpschool.com/html/html_basic_lists)

### list-style-image 속성

---

list-style-image 속성을 이용하면 마커(marker)로 자신만의 이미지를 사용할 수 있습니다.

```HTML
<style>
.imageMarker { list-style-image: url("/examples/images/img_list_marker.png"); }
</style>
```

### list-style-position 속성

---

list-style-position 속성을 이용하면 리스트 요소의 위치를 설정할 수 있습니다.

list-style-position 속성의 기본 속성값은 outside로 설정되어 있습니다.

```HTML
<style>
.outside { list-style-position: outside; }
.inside { list-style-position: inside; }
</style>
```

### list-style 속성 한 번에 적용하기

---

위에서 언급한 모든 list-style 속성을 이용한 스타일을 한 줄에 설정할 수 있습니다.

```HTML
<style>
ul { list-style: square inside url("/examples/images/img_list_marker.png"); }
</style>
```

### 리스트에 배경색 적용

---

CSS를 사용하면 리스트 전체뿐만 아니라 리스트 요소별로도 각각의 배경색을 설정할 수 있습니다.

```HTML
<style>
ul { background: **\#D2691E**; padding: **15px**; }
ol { background: **\#6495ED**; padding: **15px**; }
ul li { background: **\#DEB887**; margin: **5px**; }
ol li { background: **\#00FFFF**; margin-left: **15px**; }
</style>
```

### CSS list-style 속성

---

|속성|설명|
|---|---|
|list-style|모든 list-style 속성을 이용한 스타일을 한 줄에 설정할 수 있음.|
|list-style-type|리스트 요소의 마커(marker)를 설정함.|
|list-style-image|리스트 요소의 마커로 사용할 이미지를 설정함.|
|list-style-position|리스트 요소의 위치를 설정함.|

  

## CSS 테이블

CSS를 이용하면 다양한 형태의 테이블을 만들 수 있습니다.

|border|border-collapse|border-spacing|
|---|---|---|
|caption-side|empty-cells|table-layout|

테이블에 다음 속성을 사용하여 CSS 스타일을 적용할 수 있습니다.

1. border

2. border-collapse

3. border-spacing

4. caption-side

5. empty-cells

6. table-layout

### border 속성

---

border 속성으로 테이블의 테두리(border)를 설정할 수 있습니다.

이 속성을 명시하지 않으면 해당 테이블은 기본 설정으로 빈 테두리를 가지게 됩니다.

```HTML
<style>
table, th, td { border: **2px** solid orange; }
</style>
```

위의 예제에서 테이블의 테두리(border)가 두 줄씩 나타나는 이유는 <th>태그와 <td>태그가 각각 자신만의 테두리를 가지고 있기 때문입니다.

위와 같이 두 줄로 표현되는 테두리를 한 줄로 설정하려면 border-collapse 속성을 사용해야 합니다.

### border-collapse 속성

---

border-collapse 속성값을 collapse로 설정하면 해당 테이블의 테두리는 한 줄로 표현됩니다.

이 속성을 명시하지 않으면 해당 테이블은 기본 설정으로 테이블 요소별 테두리를 모두 표현하게 됩니다.

```HTML
<style>
table, th, td { border: **2px** solid orange; }
table { border-collapse: collapse; }
</style>
```

### border-spacing 속성

---

border-spacing 속성은 테이블 요소(th, td)간의 여백을 설정해 줍니다.

```HTML
<style>
table, th, td { border: **1px** solid black; }
table { width: **100%**; border-collapse: seperate; border-spacing: **20px** **30px**; }
</style>
```

### text-align 속성

---

text-align 속성은 테이블 요소(th, td) 내부에서 텍스트의 수평 방향 정렬을 설정합니다.

<th>태그 내부는 가운데 정렬이, <td>태그 내부는 왼쪽 정렬이 기본 설정입니다.

```HTML
<style>
table, th, td { border: **1px** solid black; }
table { border-collapse: collapse; width: **100%**; }
th { text-align: left; }
td { text-align: center; }
</style>
```

### vertical-align 속성

---

vertical-align 속성은 테이블 요소(th, td) 내부에서 텍스트의 수직 방향 정렬을 설정합니다.

<th>태그와 <td>태그 모두 가운데 정렬이 기본 설정입니다.

```HTML
<style>
table, th, td { border: **1px** solid black; }
table { border-collapse: collapse; width: **100%**; }
th { vertical-align: top; height: **50px**; }
td { vertical-align: bottom; height: **50px**; }
</style>
```

### 다양한 형태의 테이블 예제

---

CSS를 이용하면 HTML 기본 테이블을 훨씬 더 다양한 모습으로 설정할 수 있습니다.

다음 예제는 <th>태그와 <td>태그에 border-bottom 속성을 사용하여 수평 나눔선만으로 만든 테이블입니다.

```HTML
<style>
table { border-collapse: collapse; width: **100%**; }
th, td { padding: **10px**; border-bottom: **1px** solid **\#CD5C5C**; }
</style>
```

다음 예제는 :hover 선택자를 이용하여 <tr>태그에 마우스를 올리면 행 전체가 하이라이트 되도록 만든 테이블입니다.

```HTML
<style>
table { border-collapse: collapse; width: **100%**; }
th, td { padding: **10px**; border-bottom: **1px** solid **\#CD5C5C**; }
tr:hover { background-color: **\#F5F5F5**; }
</style>
```

:hover 선택자에 대한 더 자세한 사항은 CSS 동적 의사 클래스 수업에서 확인할 수 있습니다.

[CSS 동적 의사 클래스 수업 확인 =>](http://www.tcpschool.com/css/css_selector_dynamic)

다음 예제는 background-color 속성과 :nth-child 선택자를 사용하여 얼룩무늬 효과를 설정한 테이블입니다.

```HTML
<style>
table { border-collapse: collapse; width: **100%**; }
th, td { padding: **10px**; }
tr:nth-child(odd) { background-color: **\#F3F3F3**; }
</style>
```

:nth-child 선택자에 대한 더 자세한 사항은 CSS 구조 의사 클래스 수업에서 확인할 수 있습니다.

[CSS 구조 의사 클래스 수업 확인 =>](http://www.tcpschool.com/css/css_selector_structure)

### CSS table 속성

---

|속성|설명|
|---|---|
|border|모든 border 속성을 이용한 스타일을 한 줄에 설정할 수 있음.|
|border-collapse|테이블의 테두리를 한 줄로 나타낼지를 설정함.|
|border-spacing|테이블 요소(th, td)간의 여백을 설정함.|
|caption-side|테이블의 캡션(caption)을 설정함.|
|empty-cells|테이블 내의 빈 셀(cell)들의 테두리 및 배경색을 표현할지 안 할지를 설정함.|
|table-layout|테이블에 사용되는 레이아웃 알고리즘을 설정함.|

  

## CSS 이미지 스프라이트

### CSS 이미지 스프라이트(Image Sprite)

---

이미지 스프라이트(image sprite)란 여러 개의 이미지를 하나의 이미지로 합쳐서 관리하는 이미지를 의미합니다.

웹 페이지에 이미지가 사용될 경우 해당 이미지를 다운받기 위해 웹 브라우저는 서버에 이미지를 요청하게 됩니다.

하지만 사용된 이미지가 많을 경우 웹 브라우저는 서버에 해당 이미지의 수만큼 요청해야만 하므로 웹 페이지의 로딩 시간이 오래 걸리게 됩니다.

이미지 스프라이트(image sprite)를 사용하면 이미지를 다운받기 위한 서버 요청을 단 몇 번으로 줄일 수 있습니다.

모바일 환경과 같이 한정된 자원을 사용하는 플랫폼(platform)에서는 웹 페이지의 로딩 시간을 단축해주는 효과가 있습니다.

또한, 많은 이미지 파일을 관리하는 대신 몇 개의 스프라이트 이미지(sprite image) 파일만을 관리하면 되므로 매우 간편합니다.

다음 예제는 하나의 이미지를 가지고 네 개의 아이콘을 만드는 예제입니다.

네 개의 아이콘을 만들기 위해 네 개의 이미지를 사용하는 것이 아닌 다음 이미지 하나만을 가지고 작업하게 됩니다.

[![](http://www.tcpschool.com/lectures/img_css_image_sprites.png)](http://www.tcpschool.com/lectures/img_css_image_sprites.png)

```HTML
<style>
.up, .down, .right, .left { background: url("/examples/images/img_image_sprites.png") no-repeat; }
.up { width: **21px**; height: **20px**; background-position: **0** **0**; }
.down { width: 21px; height: 20px; background-position: -21px 0; }
.right { width: 22px; height: 20px; background-position: -42px 0; }
.left { width: 22px; height: 20px; background-position: -65px 0; }
</style>
```