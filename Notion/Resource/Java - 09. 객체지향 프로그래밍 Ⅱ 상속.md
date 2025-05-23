---
type: Java
archive: false
---
## 상속(ingeritance)

### 상속의 정의와 장점

---

상속이란, 기존의 클래스를 재사용하여 새로운 클래스를 작성하는 것이다. 적은 양의 코드로 새로운 클래스를 작성할 수 있고, 코드의 추가 및 변경이 용이하다.

```Java
class Child extends Parent {
	//...
}
```

이 두 클래스는 서로 상속 관계에 있다고 하며, 상속해주는 클래스를 '조상 클래스'라 하고 상속 받는 클래스를 '자손 클래스'라 한다.

> 조상 클래스 - 부모(parent)클래스, 상위(super)클래스, 기반(base)클래스  
> 자손 클래스 - 자식(child)클래스, 하위(sub)클래스, 파생된(derived) 클래스  

```Java
class Parent {}
class Child extends Parent {}
```

자손 클래스는 조상 클래스의 모든 멤버를 상속 받으므로 항상 조상 클래스보다 같거나 많은 멤버를 갖는다. 즉, 상속에 상속을 거듭할수록 상속받는 클래스의 멤버 개수는 점점 늘어나게 된다.

그래서 상속을 받는다는 것은 조상 클래스를 확장(extend)한다는 의미로 해석할 수도 있으며, 이것이 상속에 사용되는 키워드가 'extends'인 이유이기도 하다.

> - 생성자와 초기화 블럭은 상속되지 않는다. 멤버만 상속된다.  
> - 자손 클래스의 멤버 개수는 조상 클래스보다 항상 같거나 많다.  

> 자손 클래스의 인스턴스를 생성하면 조상 클래스의 멤버와 자손 클래스의 멤버가 합쳐진 하나의 인스턴스로 생성된다.

  

### 클래스간의 관계 - 포함관계

---

상속이외에도 클래스를 재사용하는 또 다른 방법이 있는데, 그 것은 클래스간에 '포함(Composite)'관계를 맺어 주는 것.

```Java
class Circle {
	int x;
	int y;
	int r;
}
```

```Java
class Circle {
	Point c = new Point();
	int r;
}
```

한 클래스를 작성하는 데 다른 클래스를 멤버변수로 정의하여 포함시키는 것은 좋은 생각.

  

### 클래스간의 관계 결정하기

---

'~은 ~이다(is-a)'와 '~은 ~을 가지고 있다(has-a)'를 넣어서 문장을 만들어 보면 클래스 간의 관계가 보다 명확해 진다.

> 원(Circle)은 점(Point)이다. - Circle is a Point  
> 원(Circle)은 점(Point)를 가지고 있다. - Circle has a Point  

클래스를 가지고 문장을 만들었을 때 '~은 ~이다.'라는 문장이 성립한다면, 서로 상속관계를 맺어 주고, '~은 ~을 가지고 있다.'는 문장이 성립한다면 포함관계를 맺어 주면 된다.

  

> 상속관계 - '~은 ~이다. (is-a)'  
> 포함관계 - '~은 ~을 가지고 있다. (has-a)'  

  

### 단일상속(single ingeritance)

---

C++에서는 여러 클래스로부터 상속받는 다중상속(multiple ingeritance)을 허용하지만 자바에서는 단일 상속만을 허용하기 때문에 하나 이상의 클래스로부터 상속을 받을 수 없다.

다중상속을 허용하면 여러 클래스로부터 상속받을 수 있기 때문에 복합적인 기능을 가진 클래스를 쉽게 작성할 수 있다는 장점이 있지만, 클래스간의 관계가 매우 복잡해 진다는 것과 서로 다른 클래스로부터 상속받은 멤버간의 이름이 같은 경우 구별할 수 있는 방법이 없다는 단점을 가지고 있다.

  

자바에서는 다중상속의 이러한 문제점을 해결하기 위해 다중상속의 장점을 포기하고 단일 상속만을 허용한다.  
단일 상속이 하나의 조상 클래스만을 가질 수 있기 때문에 다중상속에 비해 불편한 점도 있겠지만, 클래스 간의 관계가 보다 명확해지고 코드를 더욱 신뢰할 수 있게 만들어 준다는 점에서 다중상속보다 유리하다.  

  

### Object클래스 - 모든 클래스의 조상

---

Object클래스는 모든 클래스 상속계층도의 제일 위에 위치하는 조상클래스이다. 다른 클래스로부터 상속 받지 않는 모든 클래스들은 자동적으로 Object클래스로부터 상속받게 함으로써 이것을 가능하게 한다.

자바의 모든 클래스들은 Object클래스의 멤버들을 상속 받기 때문에 Object클래스에 정의된 멤버들을 사용할 수 있다.

Object클래스에는 toString(), equals()와 같은 모든 인스턴스가 가져야 할 기본적인 11개의 메서드가 정의

  

## package와 import

### 패키지(package)

---

패키지란, 클래스의 묶음이다. 패키지에는 클래스 또는 인터페이스를 포함 시킬 수 있으며, 서로 관련된 클래스들 끼리 그룹 단위로 묶어 놓음으로써 클래스를 효율적으로 관리할 수 있다.

클래스의 실제 이름(full name)은 패키지명을 포함한 것이다.  
예를 들면 String 클래스의 패키지명을 포함한 이름은 java.lang.String이다. 즉, java.lang 패키지에 속한 String 클래스라는 의미이다. 그래서 같은 이름의 클래스일 지라도 서로 다른 패키지에 속하면 패키지명으로 구별이 가능하다.  

**클래스가 물리적으로 하나의 클래스파일(.class)인 것과 같이 패키지는 물리적으로 하나의 디렉토리이다.**

예를 들어, java.lang.String클래스는 물리적으로 디렉토리 java의 서브디렉토리인 lang에 속한 String.class파일이다. 그리고 우리가 자주 사용하는 System클래스 역시 java.lang패키지에 속하므로 lang디렉토리에 포함되어 있다.  
String클래스는 rt.jar파일에 압축되어 있으며, 클래스와 관련 파일들을 압축한 것이 jar파일(*.jar)이며, jar파일은 'jar.exe'외에도 알집이나 winzip으로 압축을 풀 수 있다.  

> - 하나의 소스파일에는 첫 번째 문장으로 단 한 번의 패키지 선언만을 허용한다.  
> - 모든 클래스는 반드시 하나의 패키지에 속해야 한다.  
> - 패키지는 점(.)을 구분자로 하여 계층구조로 구성할 수 있다.  
> - 패키지는 물리적으로 클래스 파일(.class)을 포함하는 하나의 디렉토리이다.  

  

### 패키지의 선언

---

> package 패키지명;

패키지 선언문은 반드시 소스파일에서 주석과 공백을 제외한 첫 번째 문장이어야 하며, 하나의 소스파일에 단 한번만 선언될 수 있다.

패키지 명은 대소문자를 모두 허용하지만, 클래스명과 쉽게 구분하기 위해서 소문자로 하는 것을 원칙으로 하고 있다.

모든 클래스는 반드시 하나의 패키지에 포함되어야 하며, 자바에서는 기본적으로 제공하는 '이름없는 패키지(unnamed package)' 를 제공한다.

  

✲ 컴파일

```Bash
$ javac -d . PackageTest.java
```

'-d'옵션은 소스파일에 지정된 경로를 통해 패키지의 위치를 찾아서 클래스파일을 생성한다. 만일 지정된 패키지와 일치하는 디렉토리가 존재하지 않는다면 자동적으로 생성한다.

만일 '-d'옵션을 사용하지 않으면, 프로그래머가 직접 패키지의 계층구조에 맞게 디렉토리를 생성해야한다.

패키지의 루트 디렉토리를 클래스패스(classpath)에 포함시켜야 한다. 만약 [com.javachobo.book](http://com.javachobo.book) 패키지의 루트 디렉토리는 디렉토리 'com'의 상위 디렉토리인 해당 디렉토리이다.

이 디렉토리를 클래스패스에 포함시켜야만 실행 시 JVM이 PackageTest클래스를 찾을 수 있다.

  

- 클래스패스는 컴파일러(javac.exe)나 JVM 등이 클래스의 위치를 찾는데 사용되는 경로이다.

시스템변수에 클래스패스를 추가할 수 있으며, ';'를 구분자로 하여 여러 개의 경로를 클래스패스에 지정할 수 있다. 클래스패스를 지정해 주지 않으면 기본적으로 현재 디렉토리(.)가 클래스패스로 지정되지만, 클래스패스를 따로 지정해주는 경우에는 더 이상 현재 디렉토리가 자동적으로 클래스패스로 지정되지 않기 때문에 이처럼 별도로 추가를 해주어야 한다.

jar파일을 클래스패스에 추가하기 위해서는 경로와 파일명을 적어주어야 한다.

  

실행 시에는 PackageTest클래스의 패키지명을 모두 적어주어야 한다. JDK에 기본적으로 설정되어 있는 클래스패스를 이용하면 클래스패스를 따로 설정하지 않아도 된다. 새로 추가하고자 하는 클래스를 'JDK설치디렉토리\jre\classes' 디렉토리에, jar파일인 경우에는 'JDK설치디렉토리\jre\lib\ext' 디렉토리에 넣기만 하면 된다.

  

또는 실행 시에 '-cp' 옵션을 이용해서 일시적으로 클래스패스를 지정해 줄 수도 있다.

  

### import 문

---

클래스의 코드를 작성하기 전에 import문으로 사용하고자 하는 클래스의 패키지를 미리 명시해주면 소스코드에 사용되는 클래스이름에서 패키지명은 생략할 수 있다.

  

### import 문의 선언

---

> 일반적인 소스파일(*.java)의 구성은 다음의 순서로 되어 있다.  
> ➀ package문  
> ➁ import문  
> ➂ 클래스 선언  

> import 패키지명.클래스명;  
> import 패키지명.*;  

import문에서 클래스의 이름 대신 '*'을 사용하는 것이 하위 패키지의 클래스까지 포함하는 것은 아니다.

  

## 제어자(modifier)

### 제어자란?

제어자(modifier)는 클래스, 변수 또는 메서드의 선언부에 함께 사용되어 부가적인 의미를 부여한다. 제어자의 종류는 크게 접근 제어자와 그 외의 제어자로 나눌 수 있다.

> 접근 제어자 - public, protected, default, private  
> 그 외 - static, final, abstract, native, transient, synchronized, volatile, strictfp  

제어자는 클래스나 멤버변수와 메서드에 주로 사용되며, 하나의 대상에 대해서 여러 제어자를 조합하여 사용하는 것이 가능하다.

단, 접근 제어자는 한 번에 네 가지 중 하나만 선택해서 사용할 수 있다. 즉, 하나의 대상에 대해서 public과 private을 함께 사용할 수 없다는 것이다.

  

### static - 클래스의, 공통적인

---

static은 '클래스의' 또는 '공통적인'의 의미를 가지고 있다. static이 붙은 멤버변수와 메서드, 그리고 초기화 블럭은 인스턴스가 아닌 클래스에 관계된 것이기 때문에 인스턴스를 생성하지 않고도 사용할 수 있다.

> static이 사용될 수 있는 곳 - 멤버변수, 메서드, 초기화 블럭

  

### final - 마지막의 변경될 수 없는

---

final은 '마지막의' 또는 '변경될 수 없는'의 의미를 가지고 있으며 거의 모든 대상에 사용될 수 있다. 변수에 사용되면 값을 변경할 수 없는 상수가 되며, 메서드에 사용되면 오버라이딩을 할 수 없게 되고 클래스에 사용되면 자신을 확장하는 자손 클래스를 정의하지 못하게 된다.

> final이 사용될 수 있는 곳 - 클래스, 메서드, 멤버변수, 지역변수

클래스

메서드

멤버변수

지역변수

변경, 확장될 수 없는 클래스가 된다. final로 지정된 클래스는 조상클래스가 될 수 없다.

변경될수 없는 메서드, final로 지정된 메서드는 오버라이딩을 통해 재정의 될 수 없다.

  
변수 앞에 final이 붙으면, 값을 변경할 수 없는 상수가 된다.  

  

### 생성자를 이용한 final 멤버변수 초기화

---

final이 붙은 변수는 상수이므로 일반적으로 선언과 초기화를 동시에 하지만, 인스턴스변수의 경우 생성자에게 최고하 되도록 할 수 있다.

클래스 내에 매개변수를 갖는 생성자를 선언하여, 인스턴스를 생성할 때 final이 붙은 멤버변수를 초기화는데 필요한 값을 생성자의 매개변수로부터 제공받는 것.

이 기능을 활용하면 각 인스턴스마다 final이 붙은 멤버변수가 다른 값을 갖도록 하는 것이 가능하다.

  

### abstract - 추상의 미완성의

---

abstract는 ' 미완성'의 의미를 가지고 있다. 메서드의 선언부만 작성하고 실제 수행내용은 구현하지 않은 추상메서드를 선언하는데 사용된다.

> abstract가 사용될 수 있는 곳 - 클래스, 메서드

```Bash
abstract class AbstractTest {
	abstract void mvoe();
}
```

  

### 접근 제어자(access modifier)

---

접근 제어자는 멤버 또는 클래스에 사용되어, 해당하는 멤버 또는 클래스를 외부에서 접근하지 못하도록 제한하는 역할을 한다.

접근 제어자가 default임을 아리기 위해 실제로 default를 붙이지는 않는다. 클래스나 멤뼌수, 메서드, 생성자에 접근 제어자가 지정되어 있지 않다면, 접근 제어자가 default임을 뜻한다.

> 접근 제어자가 사용할 수 있는 곳 - 클래스, 멤버변수, 메서드, 생성자  
>   
> private - 싶은 클래스 내에서만 접근이 가능하다.  
> default - 같은 패키지 내에서만 접근이 가능하다.  
> protected - 같은 패키지 내에서, 그리고 다른 패키지의 자손클래스에서 접근이 가능하다.  
> public - 접근 제한이 전혀 없다.  

public은 접근 제한이 전혀 없는 것이고, private은 같은 클래스 내에서만 사용하도록 제한하는 가장 높은 제한이다. 그리고 default는 같은 패키지내의 클래스에서만 접근이 가능하도록 하는 것이다.

마지막으로 protected는 패키지에 관계없이 상속관계에 있는 자손클래스에서 접근할 수 있도록 하는 것이 제한목적이지만, 같은 패키지 내에서도 접근이 가능하다. 그래서 protected가 default보다 접근범위가 더 넓다.

  

### 접근 제어자를 이용한 캡슐화

---

클래스나 멤버, 주로 멤버에 접근 제어자를 사용하는 이유는 클래스의 내부에 선언된 데이터를 보호하기 위해서.

데이터가 유효한 값을 유지하도록, 또는 비밀번호와 같은 데이터를 외부에서 함부로 변경하지 못하도록 하기 위해서는 외부로부터의 접근을 제한하는 것이 필요하다.

또 다른 이유는 클래스 내에서만 사용되는, 내부 작업을 위해 임시로 사용되는 멤버변수나 부분작업을 처리하기 위한 메서드 등의 멤버들을 클래스 내부에 감추기 위해서이다.

> 접근 제어자를 사용하는 이유  
> - 외부로부터 데이터를 보호하기 위해서  
> - 외부에는 불필요한, 내부적으로만 사용되는 부분을 감추기 위해서  

  

### 생성자의 접근 제어자

---

생성자의 접근 제어자를 사용함으로써 인스턴스의 생성을 제한할 수 도 있다.

생성자의 접근 제어자를 private으로 지정하면, 외부에서 생성자에 접근할 수 없으므로 인턴스를 생성할 수 없게 된다. 그래도 클래스 내부에서는 인스턴스의 생성이 가능하다.

생성자를 통해 직접 인스턴슬르 생성하지 못하게 하고 pulbic메서드를 통해 인스턴스에 접근하게 함으로써 사용할 수 있는 인스턴스의 개수를 제한할 수 있다.

또 한 가지, 생성자가 private인 클래스는 다른 클래스의 조상이 될 수 없다. 왜냐하면 자손클래스의 인스턴스를 생성할 때 조상클래스의 생성자를 호출해야만 하는데 , 생성자의 저근 제어자가 private이므로 자손클래스에서 호출하는 것이 불가능하기 때문이다. 그래서 클래스 앞에 final을 더 추가하여 상속할 수 없는 클래스라는 것을 알리는 것이 좋다.

  

### 제어자(modifier)의 조합

---

> 1. 메서드에 static과 abstract를 함께 사용할 수 없다.  
> - static메서드는 몸통이 있는 메서드에만 사용할 수 있기 때문이다.  
> 2. 클래스에 abstract와 final을 동시에 사용할 수 없다.  
> - 클래스에 사용되는 final은 클래스를 확장할 수 없다는 의미이고 abstract는 상속을 통해서 완성되어야 한다는 의미이므로 서로 모순되기 때문이다.  
> 3. abstract메서드의 접근 제어자가 private일 수 없다.  
> - abstract메서드는 자손클랫에서 구현해주어야 하는데 접근 제어자가 private이면, 자손 클래스에서 접근할 수 없기 때문이다.  
> 4. 메서드에 private과 final을 가이 사용할 필요는 없다.  
> - 접근 제어자가 private인 메서드는 오버라딩될 수 없기 때문이다. 이 둘 중 하나만 사용해도 의미가 충분하다.