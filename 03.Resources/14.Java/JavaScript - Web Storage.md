---
type: JavaScript
archive: false
---
### Web Storage - localStroage

---

WebStorage API : LocalStorage.

- 데이터를 사용자 로컬에 보존하는 방식.
- 데이터를 저장, 덮어쓰기, 삭제 등 조작 가능.
- 자바스크립트(JavaScript)로 조작.
- 모바일에서도 사용 가능.

  

Cookie와의 차이점.

- 유효 기간의 없고 영구적으로 이용 가능
- 5MB 까지 사용 가능 (쿠키는 4KB가지)
- 필요할 때언제든 사용가능(쿠키는 서버 접속시에 자동 송신)

  

LocalStorage 기본 구성

- 키(key)와 값(value)을 하나의 세트로 저장.
- 도메인과 브라우저별로 저장.
- 값은 반드시 문자열로 저장됨.

  

LocalStorage에 data 추가 등.

```HTML
<script>
	function init() {
		localStorage.Test = 'Sample';
		localStorage["Test"] = 'Sample';
		localStroage.setItem("Test", "Sample");

		var val = localStorage.Test;
		var val = localStorage['Test'];
		var val = localStorage.getItem('Test');

		localStroage.removeItem("Test");

		localStroage.clear();		
</script>
```

  

### Web Storage - localStorage vs sessionStorage.

---

SessionStorage과 차이점.

- localStorage - 세션이 끊겨도 사용 가능.
- sessionStorage - 같은 세션만 사용 가능.

  

sessionStorage의 경우에는 동일한 세션에서만 사용 가능하지만 localStorage는 세션이 끊기거나 동일한 세션이 아니더라도 사용 가능.

  

### sessionStorage

---

SessionStorage 사용법.

- sessionStorage.setItem('key', value);
- sessionStorage.getItem('key');
- sessionStroage.removeItem('key');
- sessionStorage.clear();