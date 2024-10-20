---
type: PHP
archive: false
---
## Form 처리

---

### Form 처리

HTML form 요소가 전송한 데이터를 처리하기 위해서는 PHP와 같은 서버 사이드 스크립트 언어를 사용해야 합니다.

다음 예제는 form 요소를 이용하여 사용자로부터 이름과 이메일을 입력받는 예제입니다.

```PHP
<html>
<body>
    <form action="request.php" method="post">
        이름 : <input type="text" name="name"><br>
        이메일 : <input type="text" name="email"><br>
        <input type="submit">
    </form>
</body>
</html>
```

  

위의 예제처럼 form 요소의 action 속성값에는 form 요소를 처리할 서버의 PHP 스크립트 파일 주소를 명시합니다.  
그리고 전송(submit) 버튼을 누르면 PHP 스크립트로 form 요소를 통해 입력된 이름과 이메일 주소의 데이터가 전송됩니다.  

다음 예제는 form 요소에서 전송한 데이터를 처리하는 PHP 스크립트의 예제입니다.

```PHP
$name = $_POST["name"];
$email = $_POST["email"];

echo $name."님의 이메일 주소는 ".$email."입니다.";
```

  

위의 예제처럼 form 요소에 포함된 input 요소의 name 속성값은 PHP 스크립트에서도 똑같이 사용됩니다.

  

### HTTP 요청 방식

클라이언트인 브라우저가 서버에 HTTP 요청을 보낼 때는 다음 방식 중 하나를 사용합니다.

1. GET 방식
2. POST 방식

  

두 방식 모두 form 요소를 통해 입력받은 데이터를 연관 배열에 담아 전송합니다.

이 연관 배열의 키값은 input 요소의 name 속성값이 되며, 값은 사용자가 입력한 데이터가 됩니다.

또한, 미리 선언된 전역 변수인 슈퍼 글로벌 배열($_GET, $_POST)을 사용하므로, 어디에서든 제약 없이 접근할 수 있습니다.

  

> [!important]  
> $_GET과 $_POST와 같은 슈퍼 글로벌 배열은 PHP 4.1.0부터 제공됩니다.  
  
> [!important]  
> input 요소의 name 속성값과 연관 배열의 키값은 모두 대소문자를 구분하니 주의해야 합니다.  

  

### GET 방식

GET 방식은 주소에 데이터(data)를 추가하여 전달하는 방식입니다.

GET 방식의 HTTP 요청은 브라우저에 의해 캐시되어(cached) 저장됩니다.

또한, GET 방식은 보통 쿼리 문자열(query string)에 포함되어 전송되므로, 길이의 제한이 있습니다.

따라서 보안상 취약점이 존재하므로, 중요한 데이터는 POST 방식을 사용하여 요청하는 것이 좋습니다.

  

### POST 방식

POST 방식은 데이터(data)를 별도로 첨부하여 전달하는 방식입니다.

POST 방식의 HTTP 요청은 브라우저에 의해 캐시되지 않으므로, 브라우저 히스토리에도 남지 않습니다.

또한, POST 방식의 HTTP 요청에 의한 데이터는 쿼리 문자열과는 별도로 전송됩니다.

따라서 데이터의 길이에 대한 제한도 없으며, GET 방식보다 보안성이 높습니다.

  

## Form 검증

---

### Form 검증(validation)

HTML form 요소는 텍스트 입력, 체크박스, 라디오 버튼 등 다양한 input 요소를 포함할 수 있습니다.  
이러한 input 요소별로 사용자가 입력한 데이터가 적합한 데이터인지를 검사하는 검증 규칙을 설정할 수 있습니다.  

다음 예제는 여러 예제에서 계속 사용하게 될 form 요소를 이용한 간단한 회원 가입 양식 예제입니다.

```PHP
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
    이름 : <input type="text" name="name">
    성별 :
    <input type="radio" name="gender" value="female">여자
    <input type="radio" name="gender" value="male">남자
    이메일 : <input type="text" name="email">
    홈페이지 : <input type="text" name="website">
    관심 있는 분야 :
    <input type="checkbox" name="favtopic[]" value="movie"> 영화
    <input type="checkbox" name="favtopic[]" value="music"> 음악
    <input type="checkbox" name="favtopic[]" value="game"> 게임
    <input type="checkbox" name="favtopic[]" value="coding"> 코딩
    기타 : <textarea name="comment"></textarea>
    <input type="submit" value="전송">
</form>
```

  

위의 form 예제에서는 method 속성값으로 "post"를 사용하여 POST 방식으로 HTTP 요청을 보내게 됩니다.  
또한, form 요소의 action 속성값으로는 다음과 같은 PHP 코드를 사용하고 있습니다.  

```PHP
<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>
```

  

위의 예제에서 사용된 $_SERVER는 PHP에서 제공하는 슈퍼 글로벌로 인덱스로 "PHP_SELF"를 사용하면, 현재 실행 중인 PHP 스크립트의 파일 이름을 반환합니다.

htmlspecialchars() 함수는 인수로 전달받은 문자열에 포함된 특수 문자들을 HTML 엔티티로 변환해 줍니다.  
이 함수를 사용함으로써 입력 문자열에 사용자가 안 좋은 의도로 HTML 코드를 삽입하는 것을 막을 수 있습니다.  

따라서 위의 PHP 코드를 action 속성값으로 사용하면, 해당 form 요소로 입력받은 데이터를 다른 페이지로 전송하지 않고 현재 페이지로 보내게 됩니다.

  

다음 예제는 사용자가 form 요소를 통해 입력한 데이터를 해당 페이지 자체에서 처리하는 예제입니다.

```PHP
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $gender = $_POST["gender"];
    $email = $_POST["email"];
    $website = $_POST["website"];
    $favtopic = $_POST["favtopic"];
    $comment = $_POST["comment"];
}
```

  

위의 예제에서 사용된 $_SERVER["REQUEST_METHOD"]는 페이지에 접근하기 위해 사용된 HTTP 요청 방식을 반환합니다.  
따라서 위의 예제는 POST 방식의 HTTP 요청에서만 동작할 것입니다.  

위의 예제에서 PHP 스크립트로 처리된 결과를 보여주는 코드는 다음과 같습니다.

```PHP
echo "<h2>입력된 회원 정보</h2>";
echo "이름 : ".$name."<br>";
echo "성별 : ".$gender."<br>";
echo "이메일 : ".$email."<br>";
echo "홈페이지 : ".$website."<br>";
echo "관심 있는 분야 : ";

if (!empty($favtopic)) {
    foreach ($favtopic as $value) {
        echo $value." ";
    }
}

echo "<br>기타 : ".$comment; ?>
```

  

위의 예제에서 관심있는 분야는 HTML 체크 박스를 통해 여러 입력을 동시에 전달받습니다.  
따라서 변수 $favtopic은 배열을 사용하여 입력된 값들을 보여주게 됩니다.  

하지만 만약 사용자가 체크 박스를 하나도 선택하지 않은 상태에서 입력을 전송하게 되면, 배열을 사용한 코드에서는 오류가 발생할 것입니다.  
따라서 위와 같이 먼저 empty() 함수를 사용하여 입력된 값이 하나라도 있는지를 검사한 후에 코드를 실행해야 안전합니다.  

  

## Form 필수 입력 검증

---

### 필수 입력 검증

필수 입력 검증이란 사용자가 반드시 입력해야 하는 필수 input 요소에 데이터가 모두 입력되었는지를 검증하는 것입니다.

```PHP
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 이름에 대한 필수 입력 검증
    if (empty($_POST["name"])) {
        $nameMsg = "이름을 입력해 주세요!";
    } else {
        $name = $_POST["name"];
    }

    // 성별에 대한 필수 입력 검증
①  if (!isset($_POST["gender"]) || $_POST["gender"]==false) {
        $genderMsg = "성별을 선택해 주세요!";
    } else {
        $gender = $_POST["gender"];
    }

    $email = $_POST["email"];
    $website = $_POST["website"];

    // 관심 있는 분야에 대한 필수 입력 검증
    if (empty($_POST["favtopic"])) {
        $favtopicMsg = "하나 이상 골라주세요!";
    } else {
        $favtopic = $_POST["favtopic"];
    }

    $comment = $_POST["comment"];
}
```

  

위의 예제는 서버로 전달된 입력 데이터를 empty() 함수나 isset() 함수로 검사하여 필수 입력에 해당하는 데이터가 비어있다면 특정 메시지를 출력합니다.

PHP에서 empty() 함수는 다음 구문과 완전히 같은 동작을 합니다.

> [!important]  
> empty()!isset($var) || $var==false  

  

따라서 ①번 라인의 isset() 함수가 포함된 구문은 다음과 같은 empty() 함수로 대체할 수 있습니다.

```PHP
if (empty($_POST["gender"])) {
```

  

위의 예제는 전송받은 데이터를 서버 사이드에서 검증하여 필수 입력 데이터의 입력 여부를 검사하는 예제입니다.

이러한 필수 입력 검증은 클라이언트 사이드에서도 HTML의 required 속성을 이용하여 수행할 수 있습니다.

  

위의 예제에서는 필수 입력 검증을 통해 필수 입력에 해당하는 데이터가 비어있으면, 다음 코드에 특정 메시지를 출력합니다.

```PHP
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
    <p class="alert">* : 필수 입력 사항</p>
    이름 : <input type="text" name="name"><span class="alert"> * <?php echo $nameMsg ?></span>
    성별 :
    <input type="radio" name="gender" value="female">여자
    <input type="radio" name="gender" value="male">남자 <span class="alert"> * <?php echo $genderMsg ?></span>
    이메일 : <input type="text" name="email">
    홈페이지 : <input type="text" name="website">
    관심 있는 분야 :
    <input type="checkbox" name="favtopic[]" value="movie"> 영화
    <input type="checkbox" name="favtopic[]" value="music"> 음악
    <input type="checkbox" name="favtopic[]" value="game"> 게임
    <input type="checkbox" name="favtopic[]" value="coding"> 코딩
    <span class="alert"> * <?php echo $favtopicMsg ?></span>
    기타 : <textarea name="comment"></textarea>
    <input type="submit" value="전송">
</form>
```

  

## Form 입력 형식 검증

---

### 입력 형식 검증

이메일 주소는 '@'문자와 '.'문자를 포함하는 유효한 이메일 주소의 형식이 따로 존재합니다.

입력 형식 검증이란 사용자가 입력한 데이터가 이러한 형식에 맞는 유효한 데이터인가를 검증하는 것입니다.

다음 예제는 앞선 예제에 이름, 이메일, 홈페이지에 대해 입력 형식 검증을 추가한 예제입니다.

```PHP
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["name"])) {
        $nameMsg = "이름을 입력해 주세요!";
    } else {
        $name = $_POST["name"];

        // 이름의 입력 형식 검증
①      if (!preg_match("/^[a-zA-Z가-힣 ]*$/", $name)) {
            $nameMsg = "영문자와 한글만 가능합니다!";
        }
    }
...
    if (empty($_POST["email"])) {
        $emailMsg = "";
    } else {
        $email = $_POST["email"];

        // 이메일의 입력 형식 검증
②      if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $emailMsg = "이메일을 정확히 입력해 주세요!";
        }
    }

    if (empty($_POST["website"])) {
        $websiteMsg = "";
    } else {
        $website = $_POST["website"];

        // 홈페이지 URL 주소의 입력 형식 검증
③      if (!filter_var($email, FILTER_VALIDATE_URL)) {
            $websiteMsg = "홈페이지의 주소를 정확히 입력해 주세요!";
        }
    }
...
}
```

  

### 이름 입력 형식 검증

위의 예제에서 이름에는 영문자와 한글 그리고 띄어쓰기만으로 사용할 수 있도록 하고 있습니다.  
이름과 같은 입력 형식 검증은 정규 표현식을 사용하여 검증할 수 있습니다.  

PHP에서는 preg_match() 함수를 사용하여 정규 표현식을 이용한 검증을 할 수 있습니다.  
이 함수는 전달받은 정규 표현식에 해당하는 패턴이 존재하면 true를 반환하고, 존재하지 않으면 false를 반환합니다.  

```PHP
if (empty($_POST["name"])) {
	$nameMsg = "이름을 입력해 주세요!";
} else {
	$name = $_POST["name"];

	// 이름의 입력 형식 검증
① if (!preg_match("/^[a-zA-Z가-힣 ]*$/", $name)) {
		$nameMsg = "영문자와 한글만 가능합니다!";
	}
}
```

  

①번 라인에서 사용된 정규 표현식 "/^[a-zA-Z가-힣 ]*$/"의 의미는 영문 소문자와 영문 대문자, 한글 그리고 띄어쓰기만으로 이루어진 문자열을 의미합니다.

따라서 ①번 라인에서는 변수 $name의 값이 이러한 정규 표현식에 해당하는 문자열인지를 검사하고 있습니다.

  

### 이메일과 URL 주소 입력 형식 검증

PHP에서는 이메일과 URL 주소에 대한 입력 형식 검증에 사용할 수 있는 filter_var() 함수를 제공하고 있습니다.

filter_var() 함수는 해당 변수가 전달받은 검증 필터(validate filter)에 맞는 유효한 값인지를 검사하는 함수입니다.

PHP에서 사용할 수 있는 검증 필터는 다음과 같습니다.

|   |   |
|---|---|
|검증 필터|설명|
|FILTER_VALIDATE_BOOLEAN|해당 변수가 "1", "true", "on", "yes"인 경우에만 true를 반환하고, 나머지는 전부 false를 반환함.|
|FILTER_VALIDATE_EMAIL|해당 변수가 유효한 이메일 주소인지를 검증함.|
|FILTER_VALIDATE_FLOAT|해당 변수가 float 타입인지를 검증함.|
|FILTER_VALIDATE_INT|해당 변수가 int 타입인지를 검증함.|
|FILTER_VALIDATE_IP|해당 변수가 유효한 IP 주소인지를 검증함.|
|FILTER_VALIDATE_MAC|해당 변수가 유효한 MAC 주소인지를 검증함.|
|FILTER_VALIDATE_REGEXP|해당 변수를 펄 호환 정규 표현식(Perl-Compatible Regular Expression, PCRE)으로 검증함.|
|FILTER_VALIDATE_URL|해당 변수가 유효한 URL 주소인지를 검증함.|

> [!important]  
> MAC 주소란 네트워크 인터페이스에 할당된 고유 식별자로, 간단히 말해 컴퓨터가 가지고 있는 자신만의 고유 번호를 의미합니다.  
  
> [!important]  
> 펄 호환 정규 표현식(PCRE)이란 펄 프로그래밍 언어의 정규 표현식 기능에 착안하여 만든 정규 표현식으로, 기존의 POSIX 정규 표현식보다 훨씬 더 강력하고 유연하게 동작합니다.  

```PHP
if (empty($_POST["email"])) {
	$emailMsg = "";
} else {
  $email = $_POST["email"];

  // 이메일의 입력 형식 검증
② if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
      $emailMsg = "이메일을 정확히 입력해 주세요!";
    }
  }

	if (empty($_POST["website"])) {
    $websiteMsg = "";
  } else {
    $website = $_POST["website"];

  // 홈페이지 URL 주소의 입력 형식 검증
③ if (!filter_var($website, FILTER_VALIDATE_URL)) {
    $websiteMsg = "홈페이지의 주소를 정확히 입력해 주세요!";
  }
}
```

  

②번 라인에서는 filter_var() 함수에 인수로 FILTER_VALIDATE_EMAIL 검증 필터를 전달합니다.  
따라서 변수 $email에 저장된 값이 유효한 이메일 주소인가를 검증하고, 유효한 이메일 주소라면 true를 반환할 것입니다.  

③번 라인에서는 filter_var() 함수에 인수로 FILTER_VALIDATE_URL 검증 필터를 전달합니다.  
따라서 변수 $website에 저장된 값이 유효한 URL 주소인가를 검증하고, 유효한 URL 주소라면 true를 반환할 것입니다.