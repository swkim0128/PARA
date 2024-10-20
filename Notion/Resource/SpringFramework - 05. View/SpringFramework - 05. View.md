---
type: Spring
archive: false
---
### View 지정

---

- Controller에서는 처리 결괄르 보여줄 View이름이나 객체를 리턴하고, DispatcherServlet은 View이름이나 View객체를 이용하여 view를 생성
    
    명시적 지정
    
    자동 지정
    
    ![[Untitled 43.png|Untitled 43.png]]
    

  

- ViewResolver : 논리적 view 와 실제 JSP 파일 mapping
    
    servlet-context.xml
    
    ![[Untitled 1 21.png|Untitled 1 21.png]]
    
      
    
- View 이름 명시적 지정
    
    ModelAndView와 String 리턴 타입
    
    ![[Untitled 2 20.png|Untitled 2 20.png]]
    
      
    
- View 자동 지정
    
    RequestToViewnameTranslator를 이용하여 URL로 부터 view 이름을 결정.
    
    자동 지정 유형
    
    ![[Untitled 3 19.png|Untitled 3 19.png]]
    
      
    
- redirect view
    
    View 이름에 "redirect:"접두어를 붙이면, 지정한 페이지로 redirect 됨.
    
    redirect:/board/list.html?pg=1
    
    redirect:http://localhost/board/list.html?pg=1
    
    ![[Untitled 4 15.png|Untitled 4 15.png]]