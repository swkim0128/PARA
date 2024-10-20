---
type: PHP
archive: false
---
## 클래스와 객체의 기초

---

### 클래스(class)와 객체(object)

객체(object)란 실생활에서 우리가 인식할 수 있는 사물로 이해할 수 있습니다.

이러한 객체의 상태(state)와 행동(behavior)은 각각 프로퍼티(property)와 메소드(method)로 구현됩니다.

또한, 객체(object)를 만들어 내기 위한 틀이나 설계도와 같은 개념이 바로 클래스(class)입니다.

즉, PHP에서는 클래스를 가지고 객체를 생성하여 사용하게 됩니다.

  

클래스(class)

- 차(Car)

프로퍼티(property)

- $car->modelName = "아반떼"
- $car->modelYear = 2016
- $car->color = "노란색"
- $car->maxSpeed = 180

메소드(method)

- $car->accelerate()
- $car->brake()

인스턴스(instance)

- 내 차(myCar)

  

> [!important]  
> 프로그래밍에서 인스턴스(instance)란 메모리에 생성된 객체를 의미합니다.  

  

### 객체 지향 프로그래밍(OOP, Object-Oriented Programming)

객체 지향 프로그래밍에서는 모든 데이터를 객체(object)로 취급하며, 객체가 바로 프로그래밍의 중심이 됩니다.

이로 인해 코드의 관리가 쉬워지고, 적은 노력으로도 손쉽게 코드를 변경, 유지 관리할 수 있게 됩니다.

객체 지향 프로그래밍이 가지는 특징은 다음과 같습니다.

1. 추상화(abstraction)
2. 캡슐화(encapsulation)
3. 정보 은닉(data hiding)
4. 상속성(inheritance)
5. 다형성(polymorphism)

  

## 클래스의 구조

---

### 클래스의 구조

PHP에서 클래스는 class 키워드를 사용하여 다음과 같이 선언합니다.

> [!important]  
> 문법class 클래스이름 {    클래스의 프로퍼티과 메소드의 정의;}  

  

PHP에서 클래스의 이름을 생성할 때는 반드시 다음 규칙을 지켜야만 합니다.

1. 클래스의 이름은 숫자와의 구분을 빠르게 하려고 숫자로 시작할 수 없습니다.
2. 클래스의 이름은 영문자(대소문자), 숫자, 언더스코어(_)로만 구성됩니다.
3. 클래스의 이름 사이에는 공백이 포함될 수 없습니다.
4. 클래스의 이름은 대소문자를 구분합니다.
5. PHP에서 미리 정의한 예약어(reserved word)는 클래스의 이름으로 사용할 수 없습니다.

클래스는 클래스만의 상수와 변수를 가질 수 있으며, 이것을 프로퍼티(property)이라고 합니다.

또한, 메서드(method)라고 불리는 연산을 정의할 수도 있습니다.

  

### 생성자(constructor)

클래스는 새로운 객체를 생성할 때마다 생성자(constructor)라는 메서드를 호출합니다.

생성자는 객체가 생성될 때마다 호출되어 해당 객체의 프로퍼티를 초기화하거나, 필요한 다른 객체를 생성하는 등의 초기화 작업을 수행합니다.

생성자는 다른 메소드와 같은 방식으로 선언되며, 매개변수를 가질 수도 있습니다.

PHP에서 생성자의 이름은 __construct()로 정해져 있습니다.

이러한 생성자는 객체가 생성될 때마다 자동으로 호출되므로, 사용자가 직접 호출할 필요가 없습니다.

> [!important]  
> 문법class 클래스이름 {    function __construct(매개변수1, 매개변수2, ...)    {        생성자가 호출될 때 실행될 코드;    }}  

  

### 소멸자(destructor)

소멸자(destructor)는 생성자와는 반대로 해당 객체를 더는 사용하지 않아 삭제할 때 호출합니다.

PHP에서 소멸자의 이름은 __desturct()로 정해져 있으며, 매개변수를 가질 수 없습니다.

> [!important]  
> 문법class 클래스이름 {    function __desturct()    {        소멸자가 호출될 때 실행될 코드;    }}  

  

## 클래스의 사용

---

### 인스턴스의 생성

클래스가 선언되고 나면, 선언된 클래스로부터 인스턴스를 생성할 수 있습니다.

PHP에서는 new 키워드를 사용하여 인스턴스를 생성할 수 있습니다.

이때 클래스 이름을 통해 생성자로 필요한 인수를 전달할 수 있습니다.

> [!important]  
> 문법$객체이름 = new 클래스이름(인수1, 인수2, ...);  

  

### 클래스 멤버에 접근

클래스의 프로퍼티에 접근하거나 메소드를 호출할 때는 화살표 기호(->)를 사용합니다.

객체의 이름 뒤에 화살표 기호(->)를 붙이고, 접근하려고 하는 프로퍼티나 호출하고자 하는 메소드의 이름을 사용하면 됩니다.

> [!important]  
> 문법$객체이름->프로퍼티이름;$객체이름->메소드이름;  

  

PHP에서는 프로퍼티와 메소드의 접근 범위를 제한할 수 있으므로, 클래스 외부에서는 접근 제어자에 따라 접근이 가능할 수도 있고 또는 불가능할 수도 있습니다.

또한, 객체 내부에서 해당 인스턴스의 프로퍼티에 접근하고 싶을 때는 특별한 변수인 $this를 사용할 수 있습니다.  
$this 변수는 해당 인스턴스가 바로 자기 자신을 가리키는 데 사용하는 변수입니다.  

> [!important]  
> 문법$this->프로퍼티이름;  

  

### 접근 제어(access modifier)

객체 지향 프로그래밍에서 정보 은닉(data hiding)이란 사용자가 굳이 알 필요가 없는 정보는 사용자로부터 숨겨야 한다는 개념입니다.  
그렇게 함으로써 사용자는 언제나 최소한의 정보만으로 프로그램을 손쉽게 사용할 수 있게 됩니다.  

PHP에서는 클래스 멤버에 public, private, protected 키워드를 사용하여 각각의 멤버에 대한 접근 제어를 명시할 수 있습니다.

public으로 선언된 멤버는 외부로 공개되며, 해당 객체를 사용하는 어디에서나 직접 접근할 수 있게 됩니다.

private로 선언된 멤버는 외부로 공개되지 않으며, 해당 클래스의 멤버에서만 접근할 수 있습니다.

protected로 선언된 멤버는 상위 클래스에 대해서는 public 멤버처럼 취급되며, 외부에서는 private 멤버처럼 취급됩니다.  
즉, 해당 클래스의 멤버와 해당 클래스를 상속받은 자식 클래스에서만 접근할 수 있습니다.  

var 키워드를 사용하여 클래스의 프로퍼티를 정의하면, 해당 프로퍼티의 접근 제어는 public으로 자동 정의됩니다.  
또한, 메소드를 작성할 때 접근 제어자를 생략하면 public으로 자동 정의됩니다.  

```PHP
class ClassName
{
    public $publicVar;
    private $privateVar;
    protected $protectedVar;

    public function __construct()
    {
        $this->publicVar = "public property<br>";
        $this->privateVar = "private property<br>";
        $this->protectedVar = "protected property<br>";
    }

    public function publicMethod()
    {
        echo "public method<br>";
    }
    protected function protectedMethod()
    {
        echo "protected method<br>";
    }
    private function privateMethod()
    {
        echo "private method<br>";
    }
}

$object = new ClassName();
echo $object->publicVar;      // 접근 가능
//echo $object->protectedVar; // 접근 불가능
//echo $object->privatev;     // 접근 불가능

$object->publicMethod();      // 호출 가능
//$object->protectedMethod(); // 호출 불가능
//$object->privateMethod();   // 호출 불가능
```

  

### 정보 은닉(data hiding)

클래스 외부에서는 접근 제어 때문에 private 멤버나 protected 멤버로는 직접 접근할 수 없습니다.

하지만 public 메소드를 사용하면 해당 클래스의 private 멤버나 protected 멤버에도 접근할 수 있습니다.

이렇게 public 메소드는 private 멤버나 protected 멤버와 프로그램 사이의 인터페이스(interface) 역할을 수행합니다.

이렇게 외부에서 바로 데이터로 접근하지 못하게 하는 것을 정보 은닉(data hiding)이라고 합니다.

```PHP
class ClassName
{
    private $privateVar; 

    public function __construct()
    {
        $this->privateVar = "private property";
    }

    public function getValue()
    {
        return $this->privateVar;
    }

    public function setValue($value)
    {
        $this->privateVar = $value;
    }
}
$object = new ClassName();
$object->setValue("hello"); // setValue() 함수를 통해 $private의 값을 변경할 수 있음.
echo $object->getValue;     // getValue() 함수를 통해 $private의 값을 출력할 수 있음.
```