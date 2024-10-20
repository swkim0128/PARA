---
type: PHP
archive: false
---
## PHP Mail

---

php email 보내는 방법에 대한 내용

php 내의 함수를 사용하는 방법과 라이브러리 PHPMailer를 사용하는 방법이 있다.

PHPMailer의 경우 다른 이메일 smtp 서버를 사용하여 메일을 보내는 방식이다.

  

## PHP mail

---

`주의` 내부 smtp 서버가 필요하다.

```PHP
$to      = $email; // Send email to our user
$subject = 'Signup | Verification'; // Give the email a subject 
$message = '
 
Thanks for signing up!
Your account has been created, you can login with the following credentials after you have activated your account by pressing the url below.
 
------------------------
Username: '.$name.'
Password: '.$password.'
------------------------
 
Please click this link to activate your account:
http://www.yourwebsite.com/verify.php?email='.$email.'&hash='.$hash.'
 
'; // Our message above including the link
                     
$headers = 'From:noreply@yourwebsite.com' . "\r\n"; // Set from headers
mail($to, $subject, $message, $headers); // Send our email
```

  

## PHPMailer

---

### 설치

[https://github.com/PHPMailer/PHPMailer](https://github.com/PHPMailer/PHPMailer) - release - download

mv project_root / inc /

  

### 이메일 보내기

```PHP
<?php
require_once $_SERVER['DOCUMENT_ROOT'] . '/inc/PHPMailer/src/PHPMailer.php';
require_once $_SERVER['DOCUMENT_ROOT'] . '/inc/PHPMailer/src/SMTP.php';
require_once $_SERVER['DOCUMENT_ROOT'] . '/inc/PHPMailer/src/Exception.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

$mail = new PHPMailer(true);

try {
    $mail->isSMTP();
    $mail->Host     = 'smtp.naver.com';
    $mail->SMTPAuth = true;
    $mail->Username = 'id';
    $mail->Password = '*********';
    $mail->CharSet  = 'utf-8';
    $mail->Encoding = 'base64';
    $mail->SMTPSecure = 'ssl';
    $mail->Port     = 465;

    $mail->setFrom('swkim0128@naver.com', 'danawa');
    $mail->addAddress($email);

    $mail->isHTML(true);
    $mail->Subject  = '다나와 이메일 인증';
    $mail->Body     = "다나와 이메일 인증입니다.
        아래 링크를 클릭해 이메일 인증을 진행하세요.
        http://localhost/index.php/auth/verify?email={$email}&hash={$hash}";

    $mail->send();
} catch (Exception $ex) {
    echo "<script>
        alert('{$ex}');
    </script>";
}
```