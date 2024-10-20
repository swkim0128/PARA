---
type: HTML/CSS
archive: false
---
## 반응 형 웹

### 반응형 웹의 장단점

---

모든 스마트 기기에서 접속 가능

반응형 웹에서 사용하는 기술들은 W3C에서 웹 표준으로 지정한 HTML과 CSS로 이루어져 있음.

스마트 워치 같은 웨어러블 기기 뿐 아니라 스마트 TV나 게임 콘솔 등 웹표준을 지원하는 모든 기기 사용가능.

  

가로 모드에 맞추어 레이아웃 변경 가능

스마트 폰이나 태블릿에서 가로 모드로 돌렸을 때 너비 값이 커지면 그에 맞추어 레이아웃을 자동으로 변경.

  

사이트 유지, 관리 용이

PC용 Mobile용 코드가 따로 잇는 것이 아니기 때문에 유지, 관리가 쉽다.

서버 쪽 코드가 아닌 HTML과 CSS로만 되어 있어 복잡하지 않다.

  

### 뷰포트(viewport)

---

PC화면에 보이는 내용을 모바일 기기에서 그래도 볼 수 없는 이유는 PC화면과 모바일 화면의 픽셀 표현 방법이 다르기 때문

뷰포트를 지정하면 접속한 기기 화면에 맞추어 확대 또는 축소해 표시할 수 있다.

이때 '뷰포트'란 스마트폰 화면에서 실제 내용이 표시되는 영역을 말한다.

웹킷(webkit) 기반인 모바일 브라우저들의 기본 뷰포트 너비는 980px이다. 화면의 크기를 고려하여 320px로 맞추어 웹사이트를 제작하더라도 스마트폰의 모바일 브라우저의 기본 뷰포트 너비가 980px이므로 글씨와 그림은 작아진다.

이를 해겷하기 위해 뷰포트를 지정.

  

- 뷰포트 지정
    
    ![[Untitled 41.png|Untitled 41.png]]
    
    ![[Untitled 1 19.png|Untitled 1 19.png]]
    

  

## Bootstrap

### Bootstrap

---

Bootstrap은 빠르고 쉬운 웹 개발을 위한 무료 프런트 엔드 프레임 워크이다.

Bootstrap은 typography, forms, buttons, tables, navigation, model, image 및 기타 여러 가지를 위한 HTML 및 CSS 기반 디자인 템플릿과 선택적 JavaScript플러그인이 포함되어 있다.

Bootstrap은 또한 반응 형 디자인을 쉽게 만들 수 있는 기능을 제공한다.

  

### Bootstrap 장점

---

사용하기 쉬움 : HTML과 CSS에 대한 기본적인 지식만 잇으면 누구나 Bootstrap을 사용할 수 있다.

반응 형 기능 : Bootstrap의 반응 형 CSS는 휴대폰, 태블릿 및 데스크톱에 맞게 조정된다.

모바일 우선 접근 방식 : Bootstrap에서 모바일 우선 스타일은 핵심 프레임 워크의 일부이다.

브라우저 호환성 : Bootstrap 4는 모든 최신 브라우저와 호환된다.

  

### Bootstrap 사용

---

![[Untitled 2 18.png|Untitled 2 18.png]]

  

### Container

---

.container 클래스는 반응 형 고정 저비 컨테이너를 제공

.container-fluid 클래스는 부포트의 전체 너비에 걸쳐 있는 전체 너비 컨테이너를 제공

![[Untitled 3 17.png|Untitled 3 17.png]]

  

### Grid System

---

부트 스트랩의 그리드 시스템은 플렉스 박스로 구축되어 페이지에 최대 12개의 열을 허용한다.

12개 열을 모두 개별적으로 상요하지 않으려면 열을 함께 그룹화하여 더 넓은 열을 만들 수 있다.

![[Untitled 4 13.png|Untitled 4 13.png]]

  

### Grid class

---

![[Untitled 5 12.png|Untitled 5 12.png]]

![[Untitled 6 10.png|Untitled 6 10.png]]