---
type: Spring
archive: false
---
### HandlerInterceptor를 통한 요청 가로채기

---

Controller가 요청을 처리하기 전 / 후 처리

로깅, 모니터링 정보 수집, 접근 제어 처리 등의 실제 Business Logic과는 분리되어 처리해야 하는 기능들을 넣고 싶을 때 유용함

interceptor를 여러 개 설정할 수 있음(순서 주의)

  

### Interceptor

---

HandlerInterceptor 제공 method

![[Untitled 35.png|Untitled 35.png]]

  

### HandlerInterceptor를 통한 요청 가로채기

---

![[Untitled 1 14.png|Untitled 1 14.png]]

  

- HandlerInterceptor 인터페이스 구현
- HandlerInterceptor Adaptor 클래스 제공
    
    ![[Untitled 2 13.png|Untitled 2 13.png]]
    
      
    
- Interceptor 설정하기 : servlet-context.xml
    
    ![[Untitled 3 12.png|Untitled 3 12.png]]
    
- 위의 경우 요청 처리시 interceptor의 preHanle, postHandle, afterCompletion 함수의 호출 순서는
    
    Controller method 전/후/응답 완료 후 호출됨을 확인
    
    ![[Untitled 4 10.png|Untitled 4 10.png]]
    
      
    
- 여러 개의 interceptor 등록
    
    [EtcInterceptor.java](http://EtcInterceptor.java) interceptor 추가
    
    ![[Untitled 5 9.png|Untitled 5 9.png]]
    
      
    
- Interceptor 설정하기 : servlet-context.xml
    
    ![[Untitled 6 7.png|Untitled 6 7.png]]
    
      
    
- 위의 경우 요청 처리시 interceptor의 preHandle, postHandle, afterCompletion 함수의 호출 순서는?
    
    Interceptor 2개의 등록 수행 결과(순서확인)
    
    ![[Untitled 7 6.png|Untitled 7 6.png]]
    
      
    

### Interceptor - session check

---

- servlet-context.xml
    
    ![[Untitled 8 5.png|Untitled 8 5.png]]
    
      
    
- ConfirmInterceptor.java
    
    ![[Untitled 9 5.png|Untitled 9 5.png]]