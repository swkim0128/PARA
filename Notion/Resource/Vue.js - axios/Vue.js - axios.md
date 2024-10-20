---
type: Vue.js
archive: false
---
### HTTP 통신 : axios

---

Vue에서 권고하는 HTTP 통신 라이브러리는 axios이다.

Promise 기반의 HTTP 통신 라이브러리이며 상대적으로 다른 HTTP 통신 라이브러리들에 비해 문서화가 잘되어 있고 API가 다양하다.

https://github.com/axios/axios

> Promise란 서버에 데이터를 요청하여 받아오는 동작과 같은 비동기 로직 처리에 유용한 자바스크립트 라이브러리이다. 자바스크립트는 단일 스레드로 코드를 처리하기 때문에 특정 로직의 처리가 끝날 때까지 기다려 주지 않는다. 따라서 데이터를 요청하고 받아올 때까지 기다렸다가 화면에 나타내는 로직을 실행해야 할 때 주로 Promise를 활용한다. 그리고 데이터를 받아왔을 때 Promise로 데이터를 화면에 표시하거나 연산을 수행하는 등 특정 로직을 수행한다.

  

### axios 설치

---

CDN 방식

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

NPM 방식

npm install axios

  

### axios API

---

axios 대표 API

![[Untitled 60.png|Untitled 60.png]]

  

axios(config)

![[Untitled 1 37.png|Untitled 1 37.png]]

  

axios.get(url[, config])

![[Untitled 2 36.png|Untitled 2 36.png]]

  

axios.post(url[, config])

![[Untitled 3 35.png|Untitled 3 35.png]]

  

axios.put(url[, config])

![[Untitled 4 31.png|Untitled 4 31.png]]

  

==axios.delete(url[, config])==

![[Untitled 5 27.png|Untitled 5 27.png]]

  

### axios를 이용한 아파트 매매정보

---

![[Untitled 6 24.png|Untitled 6 24.png]]

![[Untitled 7 21.png|Untitled 7 21.png]]

  

### axios를 이용한 Spring REST API와의 통신

---

![[Untitled 8 19.png|Untitled 8 19.png]]

![[Untitled 9 18.png|Untitled 9 18.png]]

![[Untitled 10 16.png|Untitled 10 16.png]]