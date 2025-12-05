---
type: PHP
archive: false
---
## 예외 처리

---

### 예외(exception)

예외(exception)란 프로그램이 실행 중에 발생하는 런타임 오류를 의미합니다.  
이러한 예외가 발생하지 않도록 미리 방지하는 것도 중요하지만, 발생한 예외를 처리하는 방법 또한 매우 중요합니다.  

예외 처리는 발생한 예외 상황을 처리할 수 있도록 코드 흐름을 바꾸는 행위를 의미합니다.  
PHP는 이러한 예외 처리를 위해 객체 지향적인 방법을 제공하고 있습니다.  
따라서 PHP에서 예외를 처리하는 방식은 쉽게 확장할 수 있으며, 관리하기도 매우 쉽습니다.  

  

### 예외 처리(exception handling)

PHP에서는 프로그램이 실행되는 도중 발생하는 예외를 처리하기 위해 try / catch / finally 문을 사용합니다.  
try 블록 내부에서 예외가 발생하면, 예외를 던지(throw)고, 잡아(catch)서 처리하는 구조입니다.  

자바와 같은 언어에서는 자동으로 예외를 던져 주지만, PHP는 예외를 수동으로만 던질 수 있습니다.  
PHP에서 throw 키워드를 사용하여 예외를 던질 수 있습니다.  

> [!important]  
> 문법throw 예외객체;  

  

이때 예외 객체는 반드시 Exception 클래스나 Exception 클래스를 상속받은 자식 클래스이어야 합니다.

예외가 던져지고 나면 실행 중인 코드는 중지되고, try 블록 아래에 위치한 catch 블록에서 해당 예외를 처리할 수 있습니다.  
만약 던져진 예외가 끝까지 처리되지 않으면, 치명적인 오류가 발생합니다.  

> [!important]  
> 문법try {    예외를 처리하길 원하는 실행 코드;} catch(예외객체 매개변수) {    예외가 발생할 경우에 실행될 코드;} finally {    try 블록이 종료되면 무조건 실행될 코드;}  

  

1. try 블록 : 기본적으로 맨 먼저 실행되는 코드이며, 여기에서 발생한 예외는 catch 블록에서 처리될 수 있습니다.
2. catch 블록 : try 블록에서 던져진 예외 코드나 Exception 객체를 인수로 전달받아 그 처리를 담당합니다.
3. finally 블록 : 이 블록은 try 블록에서 예외가 발생하건 안 하건 맨 마지막에 무조건 실행됩니다.

catch 블록과 finally 블록은 선택적인 옵션으로 반드시 사용할 필요는 없습니다.

  

### Exception 클래스

PHP는 미리 정의된 예외 클래스인 Exception 클래스를 제공하고 있습니다.  
Exception 클래스는 PHP 5에서 발생하는 모든 예외의 조상 클래스입니다.  
또한, PHP 7에서는 모든 사용자 지정 예외의 조상 클래스가 됩니다.  

> [!important]  
> PHP 7부터 Exception 클래스는 Throwable 인터페이스를 구현합니다.  

  

|프로퍼티|설명|
|---|---|
|$message|예외 메시지|
|$code|예외 코드|
|$file|예외가 발생한 파일명|
|$line|예외가 발생한 라인|

|메소드|설명|
|---|---|
|__construct()|생성자|
|getMessage()|예외 메시지를 반환함.|
|getCode()|예외 코드를 반환함.|
|getFile()|예외가 발생한 파일의 경로를 반환함.|
|getLine()|예외가 발생한 라인 번호를 반환함.|
|getTrace()|발생한 예외에 대한 정보를 포함한 배열(Exception stack trace)을 반환함.|
|getTraceAsString()|getTrace()의 결과를 문자열로 반환함.|
|__toString()|발생한 예외에 대한 정보를 문자열로 반환함.|

```PHP
try
{
    throw new Exception("예외 메시지"); // 예외 객체 던짐.
}
catch(Exception $ex)                    // 예외 처리
{
    echo $ex->getMessage()."<br>";
    echo "예외가 발생한 파일 경로 : ".$ex->getFile()."<br>";
    echo "예외가 발생한 라인 번호 : ".$ex->getLine();
}
```

  

## 사용자 정의 예외

---

### 사용자 정의 예외(user defined exception)

PHP에서는 Exception 클래스의 인스턴스뿐만 아니라, 사용자가 직접 정의한 예외 객체를 던질 수도 있습니다.  
이러한 사용자 정의 예외 클래스는 Exception 클래스를 상속받아 만들 수 있습니다.  

Exception 클래스를 상속받은 자식 클래스는 Exception 클래스의 모든 프로퍼티와 메소드에 접근할 수 있습니다.  
Exception 클래스의 모든 메소드는 __tostring() 메소드를 제외하고는 오버라이딩할 수는 없습니다.  
하지만 사용자 정의 예외 클래스에 사용자가 원하는 메소드를 추가할 수는 있습니다.  

```PHP
class CustomException extends Exception       // Exception 클래스를 상속 받아 예외 정의
{
    public function errorMessage()
    {
        $msg = $this->getMessage()."<br/>".
						"예외가 발생한 파일 경로 : ".$this->getFile()."<br/>".
						"예외가 발생한 라인 번호 : ".$this->getLine();
        return $msg;
    }
} try {
    throw new CustomException("예외 메시지"); // 예외 객체 던짐.
} catch (CustomException $ex)                    // 예외 처리
{
    echo $ex->errorMessage();
}
```

  

위의 예제는 try 블록에서 사용자가 직접 정의한 CustomException 객체를 던집니다.

던져진 예외 객체는 catch 블록에서 CustomException 클래스의 errorMessge() 메소드를 사용하여 처리하고 있습니다.

  

### 중첩 예외

PHP에서 예외 처리는 중첩될 수 있습니다.

즉, try 블록 안에 또 다른 try 블록을 정의할 수 있으며, 중첩 횟수에도 제한이 없습니다.

각 try 블록은 최소한 하나 이상의 catch 블록이나 finally 블록을 가져야만 합니다.

```PHP
try{
    try
    {
        throw new CustomException("예외 메시지"); // 예외 객체 던짐.
    }
    catch(CustomException $ex)                    // 예외 처리
    {
        throw $ex;                                // catch 블록에서 다시 예외 객체 던짐.
    }
} catch(Exception $ex)                              // 예외 처리
{
    echo $ex->getMessage();
}
```

  

위의 예제처럼 catch 블록 안에서도 다시 예외를 던질 수 있습니다.

이렇게 내부 catch 블록에서 다시 던져진 예외는 외부 catch 블록에서 처리됩니다.

위의 예제에서 다시 던져진 예외는 CustomException 클래스의 errorMessage() 메소드가 아닌 Exception 클래스의 getMessage() 메소드에 의해 처리됩니다.

  

### 다중 catch 문

하나의 try 블록은 여러 개의 catch 블록을 가질 수 있으며, 각각의 catch 블록이 다른 형태의 예외를 처리하도록 할 수 있습니다.  
예외가 발생하면 여러 catch 블록 중에서 던져진 예외 객체를 매개변수로 가지는 가장 처음의 catch 블록이 실행됩니다.  

```PHP
try{
    throw new CustomException("예외 메시지"); // 예외 객체 던짐.
} catch(customException $ex)                    // 던져진 예외는 이 곳에서 처리됨.
{
    echo $ex->errorMessage();
} catch(Exception $ex) {
    echo $ex->getMessage();
}
```

  

위의 예제처럼 Exception 클래스에 대한 catch 블록은 항상 맨 마지막에 위치해야 합니다.  
그렇지 않으면 해당 catch 블록이 발생하는 예외를 모두 처리할 것입니다.  
왜냐하면, PHP의 예외 객체는 모두 Exception 클래스에서 파생되기 때문입니다.  

위의 예제에서 던져진 customException 예외 객체는 첫 번째 catch 블록에서 처리됩니다.  
만약 첫 번째 catch 블록과 두 번째 catch 블록의 순서를 바꾸면, 던져진 예외 객체는 Exception 클래스의 getMessage() 메소드에 의해 처리될 것입니다.