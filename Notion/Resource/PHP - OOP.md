---
type: PHP
archive: false
---
## 상속

---

### 상속(inheritance)이란?

상속(inheritance)이란 기존의 클래스에 기능을 추가하거나 재정의하여 새로운 클래스를 만드는 것을 의미합니다.  
이러한 상속은 캡슐화, 추상화와 더불어 객체 지향 프로그래밍을 구성하는 중요한 특징 중 하나입니다.  

상속을 이용하면 기존에 정의되어 있는 클래스의 모든 프로퍼티와 메소드를 물려받아, 새로운 클래스를 생성합니다.  
이때 기존에 미리 정의되어 있던 클래스를 부모 클래스(parent class) 또는 상위 클래스(super class)라고 합니다.  
그리고 상속을 통해 새롭게 작성되는 클래스를 자식 클래스(child class) 또는 하위 클래스(sub class)라고 합니다.  

  

### 상속(inheritance)

PHP에서는 상속(inheritance)을 통해 클래스 간의 계층 관계를 만들 수 있습니다.  
자식(child) 클래스는 부모(parent) 클래스의 모든 public, protected 멤버를 상속받게 됩니다.  

PHP에서는 extend 키워드를 사용하여 상속을 정의합니다.

다음 예제는 A 클래스를 상속받는 B 클래스를 정의하는 예제입니다.

```PHP
class B extends A {
    B 클래스만의 프로퍼티와 메소드;
}
```

  

위의 예제에서 B 클래스는 A 클래스의 자식 클래스가 되고, 반대로 A 클래스는 B 클래스의 부모 클래스가 됩니다.  
B 클래스는 A 클래스의 private 멤버를 제외한 모든 프로퍼티와 메소드를 상속받아 사용할 수 있습니다.  
여기에 필요하다면 자신만의 프로퍼티와 메소드를 추가할 수 있습니다.  

이렇게 상속을 이용하면 기존에 작성된 클래스를 손쉽게 재활용할 수 있습니다.  
또한, 공통적인 부분은 부모 클래스에 미리 작성하여, 자식 클래스에서 중복되는 부분을 제거할 수도 있습니다.  

PHP에서는 둘 이상의 부모 클래스에서 프로퍼티와 메소드를 상속받을 수는 없습니다.  
하나의 부모 클래스가 여러 자식 클래스를 가질 수는 있지만, 자식 클래스는 오직 부모 클래스를 하나만 가질 수 있습니다.  

  

### 오버라이딩(overriding)

오버라이딩(overriding)이란 이미 정의된 메소드를 같은 이름의 메소드로 다시 정의하는 것이라고 할 수 있습니다.  
즉, 메소드 오버라이딩이란 상속받은 부모 클래스의 메소드를 재정의하여 사용하는 것을 의미합니다.  

PHP에서는 부모 클래스의 메소드와 이름만 작성하면, 해당 메소드를 오버라이딩할 수 있습니다.

```PHP
class A
{
    public $property = "class A";
    public function showProperty()
    {
        echo $this->property."<br>";
    }
}

class B extends A                    // 클래스 A를 상속 받음.
{
    public $property = "class B";
    public function showProperty()   // 클래스 A의 메소드를 오버라이딩
    {
        echo "hello ".$this->property."<br>";
    }
}

$a = new A();
$a->showProperty();                  // 클래스 A의 메소드 호출
$b = new B();
$b->showProperty();                  // 클래스 B의 메소드 호출
```

  

위의 예제에서 자식 클래스인 B 클래스는 부모 클래스인 A 클래스로부터 상속받은 showProperty() 메소드를 오버라이딩하여 사용합니다.  
따라서 B 클래스의 인스턴스인 $b에서 showProperty() 함수를 호출하면, 오버라이딩된 B 클래스의 showProperty() 함수가 호출됩니다.  

  

## 정적 멤버

---

### static 키워드

클래스를 정의할 때 static 키워드를 사용한 프로퍼티와 메소드는 해당 클래스의 인스턴스를 생성하지 않아도 접근할 수 있게 됩니다.  
이러한 프로퍼티와 메소드를 정적 멤버(static member)라고 합니다.  

이러한 정적 멤버의 특징은 다음과 같습니다.

1. static 키워드로 선언된 정적 프로퍼티는 인스턴스화된 객체에서는 접근할 수 없습니다.
2. static 키워드로 선언된 정적 메소드는 인스턴스화된 객체에서도 접근할 수 있습니다.
3. 정적 메소드 내에서는 $this 의사 변수를 사용할 수 없습니다.

  

```PHP
class StaticMember
{
    public static $staticProperty = "static property";
    public static function showProperty()
    {
        echo self::$staticProperty;."<br>";
    }
}

echo StaticMember::showProperty();  // 호출 가능
echo StaticMember::$staticProperty; // 접근 가능

$var = new StaticMember();          // 인스턴스 생성
echo $var->showProperty();          // 호출 가능
//echo $var->$staticProperty;       // 접근 불가능
```

  

위의 예제에서 정적 메소드인 showProperty() 메소드에서는 자신을 가리키는 $this 의사 변수를 사용할 수 없습니다.

따라서 self 키워드와 함께 범위 지정 연산자를 사용하여 프로퍼티에 접근하고 있습니다.

또한, 생성된 인스턴스에서는 정적 프로퍼티에 접근할 수 없음을 보여주고 있습니다.

  

### 범위 지정 연산자(::)

클래스의 프로퍼티나 메소드에 접근하기 위해서는 인스턴스를 생성하고, 화살표 연산자(->)를 사용해야 합니다.

하지만 단순히 클래스의 정의 내에서 프로퍼티나 메소드를 사용하고 싶을 때는 범위 지정 연산자(::)를 사용할 수 있습니다.

범위 지정 연산자(::)는 클래스의 상수, 정적(static) 멤버 또는 재정의된 멤버에 접근할 수 있게 해줍니다.

클래스의 정의 외부에서 위와 같은 멤버에 접근할 때는 클래스의 이름을 사용해야 합니다.

```PHP
echo OtherClassName::CONSTANT;
```

  

또한, 다음 키워드를 사용하면 클래스의 정의 내에서 특정 프로퍼티나 메소드에 접근할 수 있습니다.

1. self : 자기 자신에 접근할 때
2. parent : 부모 클래스에 접근할 때

```PHP
echo self::$property;
echo parent::CONSTANT;
```

  

## 인터페이스

---

### 추상 메소드(abstract method)

추상 메소드(abstract method)란 자식 클래스에서 반드시 오버라이딩해야만 사용할 수 있는 메소드를 의미합니다.  
이러한 추상 메소드는 선언부만이 존재하며, 구현부는 작성되어 있지 않습니다.  
바로 이 작성되어 있지 않은 구현부를 자식 클래스에서 오버라이딩하여 사용하는 것입니다.  

> [!important]  
> 문법abstract 접근제어자 function 메소드이름();  

  

### 추상 클래스(abstract class)

PHP에서는 최소한 하나 이상의 추상 메소드를 포함하는 클래스를 추상 클래스(abstract class)라고 합니다.  
이러한 추상 클래스는 객체 지향 프로그래밍에서 중요한 특징인 다형성을 가진 메소드의 집합을 정의할 수 있게 해줍니다.  
즉, 반드시 사용되어야 하는 메소드를 추상 클래스에 추상 메소드로 선언해 놓으면, 이 클래스를 상속받는 모든 클래스에서는 이 추상 메소드를 반드시 재정의해야 합니다.  

```PHP
abstract class AbstractClass            // 추상 클래스
{
    abstract protected function move(); // 추상 메소드
    abstract protected function stop();

    public function start() // 공통 메소드
    {
        ...
    }
}
```

  

이러한 추상 클래스는 동작이 정의되어 있지 않은 추상 메소드를 포함하고 있으므로, 인스턴스를 생성할 수 없습니다.

추상 클래스는 먼저 상속을 통해 자식 클래스를 만들고, 만든 자식 클래스에서 추상 클래스의 모든 추상 메소드를 오버라이딩하고 나서야 비로소 자식 클래스의 인스턴스를 생성할 수 있게 됩니다.

  

### 인터페이스(interface)

PHP에서 인터페이스(interface)란 다른 클래스를 작성할 때 기본이 되는 틀을 제공하면서, 다른 클래스 사이의 중간 매개 역할도 담당하는 일종의 추상 클래스를 의미합니다.

인터페이스를 사용하면 클래스가 반드시 구현해야 할 메소드가 어떻게 동작하는지를 알 필요 없이 다른 부분의 코드를 작성할 수 있습니다.

이러한 인터페이스는 메소드의 구현부가 정의되어 있지 않은 추상 메소드들로 구성되어 있으며, 내부의 모든 추상 메소드는 public 메소드입니다.

PHP에서는 interface 키워드를 사용하여 인터페이스를 정의합니다.

> [!important]  
> 문법interface 인터페이스이름 {    구현할 메소드;}  

  

이렇게 정의된 인터페이스는 implements 키워드를 사용하여 구현할 수 있습니다.  
인터페이스를 구현하는 클래스는 인터페이스의 모든 메소드를 구현해야 합니다.  
이렇게 구현되는 메소드는 인터페이스에서 정의된 형태와 완전히 같은 형태로 정의되어야 합니다.  

인터페이스의 모든 메소드는 클래스 안에서 모두 구현되어야 합니다.

```PHP
interface Transport              // 인터페이스의 정의
{
    public function move();      // 구현할 메소드
    public function stop();
}

class Car implements Transport   // Transport 인터페이스를 구현하는 Car 클래스
{
    function move()              // 메소드 구현
    {
        ...
    }

    function stop()              // 메소드 구현
    {
        ...
    }
}

# 인터페이스(interface)도 클래스처럼 extends 키워드를 사용하여 상속받을 수 있습니다.
interface Transport                  // 인터페이스의 정의
{
    public function move();          // 구현할 메소드
    public function stop();          // 구현할 메소드
}

interface Overland extends Transport // Transport 인터페이스를 상속받는 Overland 인터페이스
{
    public function highpass();      // 구현할 메소드
}

class Car implements Overload        // Overland 인터페이스를 구현하는 Car 클래스
{
    function move()                  // 메소드 구현
    {
        ...
    }

    function stop()                  // 메소드 구현
    {
        ...
    }

    function highpass()              // 메소드 구현
    {
        ...
    }
}
```

> [!important]  
> PHP 인터페이스는 클래스와는 달리 각각의 인터페이스를 쉼표(,)로 구분하여 여러 개의 인터페이스를 동시에 상속받을 수 있습니다.  

  

## 오버로딩

---

### 다형성(polymorphism)

다형성(polymorphism)이란 하나의 프로퍼티가 여러 가지 상태를 가질 수 있는 것을 의미합니다.

PHP에서는 이러한 다형성을 오버로딩(overloading)과 지연 정적 바인딩(late static bindings)을 통해 구현하고 있습니다.

다형성은 상속, 추상화와 더불어 객체 지향 프로그래밍을 구성하는 중요한 특징 중 하나입니다.

  

### 오버로딩(overloading)

다른 대부분의 객체 지향 프로그래밍 언어에서 오버로딩(overloading)은 매개변수의 개수와 타입을 달리하여 같은 이름의 메소드를 중복하여 정의하는 것을 의미합니다.  
하지만 PHP에서는 다른 언어와는 달리 프로퍼티나 메소드를 동적으로 '생성한다'는 의미로 오버로딩을 사용합니다.  

이렇게 동적으로 생성된 멤버는 해당 클래스의 매직 메소드(magic method)를 통해 다양한 형태로 처리할 수 있습니다.  
이때 오버로딩되는 메소드는 반드시 public으로 정의되어야만 합니다.  

> [!important]  
> 매직 메소드(magic method)란 PHP에서 특수한 기능을 위해 미리 정의한 메소드를 가리킵니다.이러한 매직 메소드는 메소드 이름과 매개변수, 반환 타입, 호출의 타이밍만이 정해져 있으며, 그 내용은 사용자가 직접 작성하여 사용할 수 있습니다.PHP에서 모든 매직 메소드의 이름은 두 개의 언더스코어(__)로 시작합니다.  

  

### 프로퍼티 오버로딩(property overloading)

PHP에서는 접근 불가 프로퍼티(inaccessible property)를 오버로딩하기 위해 다음과 같은 매직 메소드를 구현해야 합니다.

> [!important]  
> 매직 메소드의 원형public void __set(string $name, mixed $value)public mixed __get(string $name)public bool __isset(string $name)public bool __unset(string $name)  

  

1. __set() 메소드는 접근 불가 프로퍼티의 값을 설정할 때 호출됩니다.
2. __get() 메소드는 접근 불가 프로퍼티의 값을 읽을 때 호출됩니다.
3. __isset() 메소드는 접근 불가 프로퍼티에 대해 isset() 함수나 empty() 함수가 호출될 때 호출됩니다.
4. __unset() 메소드는 접근 불가 프로퍼티에 대해 unset() 함수가 호출될 때 호출됩니다.

  

> [!important]  
> 접근불가 프로퍼티(inaccessible property)란 현재 영역에서는 정의되어 있지 않거나, 접근 제어로 인해 보이지 않는 프로퍼티를 의미합니다.  

```PHP
class PropertyOverloading
{
private $data = array(); // 오버로딩된 변수가 저장될 배열 생성
public $declared = 10;   // public으로 선언된 프로퍼티
private $hidden = 20;    // private로 선언된 프로퍼티

public function __set($name, $value)
{
    echo "$name 프로퍼티를 {$value}의 값으로 생성합니다!";
    $this->data[$name] = $value;
}

public function __get($name)
{
    echo "$name 프로퍼티의 값을 읽습니다!<br>";

    if (array_key_exists($name, $this->data)) {
        return $this->data[$name];
    } else {
        return null;
    }
}
public function __isset($name)
{
    echo "$name 프로퍼티가 설정되어 있는지 확인합니다!<br>";
    return isset($this->data[$name]);
}
public function __unset($name)
{
    echo "$name 프로퍼티를 해지합니다!";
    unset($this->data[$name]);
}
}

$obj = new PropertyOverloading(); // PropertyOverloading 객체 생성

① $obj->prop = 1;              // 동적 프로퍼티 생성
② echo $obj->prop;             // 동적 프로퍼티에 접근
③ var_dump(isset($obj->prop)); // 동적 프로퍼티로 isset() 함수 호출
④ unset($obj->prop);           // 동적 프로퍼티로 unset() 함수 호출
⑤ var_dump(isset($obj->prop)); // 동적 프로퍼티로 isset() 함수 호출

⑥ echo $obj->declared; // 선언된 프로퍼티는 오버로딩을 사용하지 않음.
⑦ echo $obj->hidden;   // private로 선언된 프로퍼티는 클래스 외부에서 접근할 수 없으므로, 오버로딩을 사용함.
```

  

위의 예제에서는 프로퍼티를 오버로딩하기 위해 __set(), __get(), __isset(), __unset() 메소드를 구현하고 있습니다.

①번 라인에서는 동적으로 프로퍼티를 생성하고, ②번 라인에서는 그 값에 접근합니다.

③과 ⑤번 라인에서는 생성된 동적 프로퍼티를 isset() 함수에 인수로 전달하고, ④번 라인에서는 unset() 함수에 인수로 전달합니다.

이때 ①번부터 ⑤번 라인까지의 모든 동작은 앞서 구현한 네 가지 메소드가 상황에 맞게 자동 호출됨으로써 이루어집니다.

하지만 ⑥번 라인과 같이 일반적인 방법으로 선언된 프로퍼티에 접근할 때는 __get() 메소드를 호출하지 않습니다.

다만, ⑦번 라인처럼 private로 선언된 프로퍼티는 클래스 외부에서는 접근할 수 없으므로, __get() 메소드를 호출하게 됩니다.

> [!important]  
> array_key_exists() 함수는 인수로 전달받은 키가 해당 배열에 저장되어 있으면 true를 반환하고, 저장되어 있지 않으면 false를 반환하는 함수입니다.  

  

### 메소드 오버로딩(method overloading)

PHP에서는 접근불가 메소드(inaccessible method)를 오버로딩하기 위해 다음과 같은 매직 메소드를 구현해야 합니다.

> [!important]  
> 매직 메소드의 원형1. public mixed __call(string $name, array $arguments)2. public static mixed __callStatic(string $name, array $arguments)  

  

1. __call() 메소드는 클래스 영역에서 접근 불가 메소드를 호출할 때 호출됩니다.

2. __callStatic() 메소드는 정적(static) 영역에서 접근 불가 메소드를 호출할 때 호출됩니다.

```PHP
class MethodOverloading
{
    public function __call($name, $arguments)
    {
        echo join(", ", $arguments)."에서 접근 불가 메소드를 호출합니다!";
    }

    public static function __callStatic($name, $arguments)
    {
        echo join(", ", $arguments)."에서 접근 불가 메소드를 호출합니다!";
    }
}

$obj = new MethodOverloading();             // MethodOverloading 객체 생성

① $obj->testMethod("클래스 영역");            // 클래스 영역에서 접근 불가 메소드 호출
② MethodOverloading::testMethod("정적 영역"); // 정적 영역에서 접근 불가 메소드 호출
```

  

위의 예제에서는 메소드를 오버로딩하기 위해 __call()과 __callStatic() 메소드를 구현하고 있습니다.

①번 라인에서는 동적으로 testMethod() 메소드를 생성하고, 바로 그 값에 접근합니다.

이때 클래스 영역에서 생성된 동적 메소드에 접근하므로, 사용자가 구현한 __call() 메소드가 호출됩니다.

②번 라인에서는 MethodOverloading 클래스의 정적 영역에서 동적 메소드에 접근합니다.

이때 정적 영역에서 생성된 동적 메소드에 접근하므로, 사용자가 구현한 __callStatic() 메소드가 호출됩니다.

  

## 늦은 정적 바인딩

---

### 바인딩(binding)

바인딩(binding)이란 프로그램에 사용된 구성 요소의 실제 값 또는 프로퍼티를 결정짓는 행위를 의미합니다.  
예를 들어 함수를 호출하는 부분에서 실제 함수가 위치한 메모리를 연결하는 것도 바로 바인딩입니다.  

이러한 바인딩은 크게 다음과 같이 구분할 수 있습니다.

1. 정적 바인딩(static binding) : 실행 시간 전에 일어나고, 실행 시간에는 변하지 않은 상태로 유지되는 바인딩임.
2. 동적 바인딩(dynamic binding) : 실행 시간에 이루어지거나 실행 시간에 변경되는 바인딩임.  
    이러한 동적 바인딩은 늦은 바인딩(late binding)이라고도 불립니다.  
    

하지만 PHP에서는 정적 바인딩과 동적 바인딩의 중간 정도 수준인 늦은 정적 바인딩(LSB)을 제공하고 있습니다.

  

### 늦은 정적 바인딩(late static bindings, LSB)

PHP 5.3.0부터 제공되는 늦은 정적 바인딩(LSB)은 static 키워드와 함께 범위 지정 연산자(::)를 사용하여 수행할 수 있습니다.  
늦은 정적 바인딩은 마지막으로 호출한 비전송 호출(non-forwarding call)의 클래스 이름을 저장하여 동작합니다.  
이때 정적 메소드 호출에서는 범위 지정 연산자(::) 좌측에 명시된 클래스 이름을 저장하며, 비정적 메소드 호출에서는 해당 객체의 클래스 이름을 저장합니다.  

static::은 정의된 클래스를 컴파일 시간에 결정할 수 없고, 프로그램 실행 시 전달되는 정보로 결정하므로 늦은 바인딩입니다.  
또한, 정적 메소드 호출에도 사용할 수 있으므로 정적 바인딩이기도 합니다.  

> [!important]  
> 범위 지정 연산자(::, scope resolution operator)는 클래스의 상수, 정적(static) 멤버 또는 재정의된 멤버에 접근할 수 있도록 해주는 연산자입니다.  

  

### 정적 메소드 호출에서의 늦은 정적 바인딩

다음 예제는 self 키워드와 함께 범위 지정 연산자(::)를 사용하여 정적 메소드를 호출하는 예제입니다.

```PHP
class A
{
    public static function className()
    {
        echo __CLASS__;
    }

    public static function printClass()
    {
        self::className();
    }
}

class B extends A
{
    public static function className()
    {
        echo __CLASS__;
    }
}

① B::printClass(); // A
```

  

위의 예제에서 ①번 라인의 실행 결과는 클래스 A를 출력합니다.

즉, 클래스 B에서 printClass() 메소드를 호출하지만, 이 메소드는 클래스 A에서 정의되므로 클래스 A를 출력하게 됩니다.

이처럼 현재 클래스를 참조하는 self::와 상수 __CLASS__는 사용하는 메소드가 어디에 정의되어 있는가에 따라 그 값이 결정됩니다.

하지만 늦은 정적 바인딩을 사용하면, 클래스 B에서 호출한 printClass() 메소드가 현재 클래스로 클래스 B를 참조하게 할 수 있습니다.

다음 예제는 static 키워드와 함께 범위 지정 연산자(::)를 사용하여 정적 메소드를 호출하는 예제입니다.

```PHP
class A
{
    public static function className()
    {
        echo __CLASS__;
    }

    public static function printClass()
    {
        static::className();
    }
}

class B extends A
{
    public static function className()
    {
        echo __CLASS__;
    }
}

① B::printClass(); // B
```

  

위의 예제에서 ①번 라인의 실행 결과는 클래스 B를 출력합니다.

printClass() 메소드가 클래스 A에서 정의되지만, 클래스 B에서 이 메소드를 호출하므로 클래스 B를 출력하게 됩니다.

이처럼 static 키워드와 범위 지정 연산자(::)를 함께 사용하면 늦은 정적 바인딩을 수행할 수 있습니다.

  

### 비정적 메소드 호출에서의 늦은 정적 바인딩

다음 예제는 static 키워드와 함께 범위 지정 연산자(::)를 사용하여 비정적 메소드를 호출하는 예제입니다.

```PHP
class A
{
    private function className()
    {
        echo __CLASS__."<br>";
    }

    public function printClass()
    {
①      $this->className();
②      static::className();
    }
}

class B extends A
{
    // className() 메소드는 클래스 B로 복사되므로,
    // className() 메소드의 유효 범위는 여전히 클래스 A임.
}

class C extends A
{
    private function className()
    {
        // 기존의 className() 메소드가 이 메소드로 대체되므로,
        // className() 메소드의 유효 범위는 이제부터 클래스 C가 됨.
    }
}


$b = new B();
③ $b->printClass(); // A
                     // A

$c = new C();
④ $c->printClass(); // A
                     // Fatal error : Call to private method C::className() from context 'A'
```

  

위의 예제에서 className() 메소드는 클래스 A에서 처음으로 정의됩니다.

그리고서 클래스 B가 클래스 A를 상속받지만, 클래스 B에서 className() 메소드를 재정의하지는 않습니다.

따라서 className() 메소드의 유효 범위는 여전히 클래스 A가 되며, ③번 라인의 결과처럼 변수 $this나 static::은 모두 클래스 A를 가리키게 됩니다.

하지만 클래스 C가 클래스 A를 상속받으면서 className() 메소드를 재정의합니다.

따라서 className() 메소드의 유효 범위는 이제부터 클래스 C로 변경될 것입니다.

그러므로 ④번 라인의 결과처럼 변수 $this는 여전히 클래스 A를 가리키겠지만, static::은 클래스 C를 가리키게 될 것입니다.