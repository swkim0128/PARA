---
type: Spring
archive: false
---
### File Upload

---

- pom.xml : commons-fileupload library 추가
    
    ![[Untitled 47.png|Untitled 47.png]]
    

  

- servlet-context.xml
- property
    
    maxUploadSize : 최대 업로드 가능한 파일의 바이트크기
    
    maxInMemorySize : 디스크에 임시 파일을 생성하기 전에 메모리에 보관할 수 이쓴ㄴ 최대 바이트 크기
    
    ![[Untitled 1 25.png|Untitled 1 25.png]]
    
      
    
- write.jsp : form 설정
    
    ![[Untitled 2 24.png|Untitled 2 24.png]]
    
      
    
- GuestBookController.java
    
    ![[Untitled 3 23.png|Untitled 3 23.png]]
    
      
    
- FileInfoDto.java
    
    ![[Untitled 4 19.png|Untitled 4 19.png]]
    
      
    
- GuestBookController.java
    
    ![[Untitled 5 17.png|Untitled 5 17.png]]
    
    ![[Untitled 6 14.png|Untitled 6 14.png]]
    
      
    
- GuestBookServiceImpl.java
    
    ![[Untitled 7 12.png|Untitled 7 12.png]]
    
      
    
- guestbook.xml
    
    ![[Untitled 8 10.png|Untitled 8 10.png]]
    
    ![[Untitled 9 10.png|Untitled 9 10.png]]
    
    ![[Untitled 10 9.png|Untitled 10 9.png]]