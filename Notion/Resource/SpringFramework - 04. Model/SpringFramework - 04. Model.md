---
type: Spring
archive: false
---
### Model 생성

---

- View에 전달하는 데이터
    
    @RequestMapping annotation이 적용된 method의 Map, Model, ModelMap
    
    @RequestMapping method가 return하는 ModelAndView
    
    @ModelAttribute annotation이 적용된 method가 return한 객체
    
      
    
- Map, Model, ModelMap을 통한 설정
    
    method의 argument로 받는 방식
    
    ![[Untitled 63.png|Untitled 63.png]]
    
      
    
- Model interface 주요 method
    
    Model addAttribute(String name, Object value);
    
    Model addAttribute(Object value);
    
    Model addAllAttributes(Collection<?> values);
    
    Model addAllAttributes(Map<String, ?> attributes);
    
    Model mergeAttributes(Map<String, ?> attributes);
    
    boolean containsAttribute(String name);
    
      
    
- ModelAndView를 통한 Model 설정
    
    Controller에서 처리 결과를 보여줄 view와 view에 전달할 값(model)을 저장하는 용도로 사용
    
    setViewName(String newname);
    
    addObject(String name, Object value);
    
    ![[Untitled 1 40.png|Untitled 1 40.png]]
    
      
    
- @ModelAttribute annotation을 이용한 model data 처리
    
    @RequestMapping annotation이 직용되지 않은 별도 method로 ㅂ모델이 추가될 객체를 생성
    
    ![[Untitled 2 38.png|Untitled 2 38.png]]
    
      
    

### 요청 URL 매치

---

- 전체 경로와 Servlet 기반 경로 매칭
    
    DispatcherServlet은 DefaultAnnotationHandlerMapping Class를 기본으로 HandlerMapping 구현체로 사용
    
    Defulat로 Context 내의 경로가 아닌 Servlet 경로를 제외한 나머지 경로에 대해 mapping
    
    ![[Untitled 3 37.png|Untitled 3 37.png]]
    
      
    
- Servlet 기반 경로 매칭
    
    Servlet 경로를 포함한 전체 경로를 이용해서 매칭하려는 경우
    
    @RequestMapping("/product/lst")
    
    ![[Untitled 4 33.png|Untitled 4 33.png]]
    
      
    
- @PathVariable annotation을 이용한 URI 템플릿
    
    RESTful 방식
    
    - http://localhost/users/troment
    
    - http://localhost/product/
    
    - http://localhost/forum/board1/10
    
    @RequestMapping Annotation 값으로 {템플릿변수}를 사용
    
    @PathVariable Annotation을 이용해서 {템플릿변수}와 동일한 이름을 갖는 parameter를 추가
    
    ![[Untitled 5 29.png|Untitled 5 29.png]]
    
      
    
- @RequestMapping Annotation의 추가 설정 방법
    
    @RequestMapping Annotation을 class와 method에 함께 적용하는 경우
    
    ![[Untitled 6 26.png|Untitled 6 26.png]]
    
      
    
    Ant 스타일의 URI 패턴 지원
    
    ? : 하나의 문자열과 대치
    
    * : 하나 이상의 문자열과 대치
    
    ** : 하나 이상의 디렉토리와 대치
    
    ![[Untitled 7 23.png|Untitled 7 23.png]]