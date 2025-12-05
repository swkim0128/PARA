---
type: Java
archive: false
---
java.lang패키지는 자바프로그래밍에 가장 기본이 되는 클래스들을 포함하고 있다.그렇기 때문에 java.lang패키지의 클래스들은 import문 없이도 사용할 수 있도록 되어 있다.

  

## Object클래스

object클래스는 모든 클래스의 최고 조상이기 때문에 Object클래스의 멤버들은 모든 클래스에서 바로 사용 가능하다.

  

### equals메서드

---

매개변수로 객체의 참조변수를 받아서 비교하여 그 결과를 boolean값으로 알려 주는 역할.

```Java
public boolean equals(Object obj) {
	return (this==boj);
}
```

Object클래스로부터 상속받은 equals메서드는 결국 두 개의 참조변수가 같은 객체를 참조하고 있는지, 즉 두 참죠변수에 저장된 값(주소값)이 같은지를 판단하는 기능 밖에 할 수 없다는 것을 알 수 있다. equals메서드를 상속받은 클래스에서 오버라이딩하여 내용을 변경해야 한다.

자주 사용하는 String클래스 역시 Object클래스의 equals메서드를 그대로 사용하는 것이 아니라 이처럼 오버라이딩을 통해서 String인스턴스 갖는 문자열 값을 비교하도록 되어있다.

  

### hashCode메서드

---

이 메서드는 해싱(hashing)기법에 사용되는 해시함수(hash function)를 구현한 것이다.

일반적으로 해시코드가 같은 두 객체가 존재하는 것이 가능하지만, Object클래스에 정의된 hashCode메서드는 객체의 주소값을 이용해서 해시코드를 만들어 반환하기 때문에 한번의 실행에서 서로 다른 두 객체는 결코 같은 해시코들르 가질 수 없다.

클래스의 멤버변수 값으로 객체의 같고 다름을 판단해야하는 경우라면 hasCode메서드를 적절히 오버라이딩해야한다. 같은 객체라면 hashCode메서드를 호출했을 때의 결과값인 해시코드도 같아야 하기 때문이다.  
그래서 equals메서드를 오버라이딩하면서 hashCode메서드도 같이 오버라이딩하는 것이 일반적이다.  

String클래스는 문자열의 내용이 같으면, 동일한 해시코드를 반환하도록 hashCode메서드를 오버라이딩하였기 때문에, 문자열의 내용이 같은 str1과 str2에 대해 hashCode()

  

### toString메서드

---

toString()은 인스턴스에 대한 정보를 문자열(String)로 제공할 목적으로 정의한 것이다. Ojbect클래스에 정의된 toString()은 아래와 같다.

```Java
public String toString() {
	return getClass().getName() + "@"
				+ Integer.toHexString(hashCode());
}
```

  

### clone메서드

---

이 메서드는 자신을 복제하여 새로운 인스턴스를 생성하는 일을 한다. Object클래스에 정의된 clone메서드는 단순히 멤버변수의 값만을 복사하기 때문에 배열이나 인스턴스가 맴버로 정의되어 있는 클래스의 인스턴스는 완전한 복제가 이루어지지 않는다.  
예를 들어 배열의 경우, 복제된 인스턴스도 같은 배열의 주소를 갖기 때문에 복제된 이스턴스의 작업이 원래의 인스턴스에 영향을 미치게 된다. 이런 경우 clone메서드를 오버라이딩해서 새로운 배열을 생성하고 배열의 내용을 복하도록 해야 한다.  

  

## String클래스

### String클래스의 특징

---

String클래스에는 문자열을 저장하기 위해서 문자형 배열 변수(char[]) value를 인스턴스 변수로 정의해놓고 있다. 인스턴스 생성 시 생성자의 매개변수로 입력받는 문자열은 이 인스턴스변수(vlaue)에 문자형 배열(char[])로 저장되는 것이다.

```Java
public final class String implements java.io.Seriallizable, Comparable {
	/** The Vlaue is used for character storage. */
	private char[] value;
	...
```

한번 생성된 String인스턴스가 갖고 있는 문자열은 읽어 올 수만 있고, 변경할 수는 없다.  
예를 들어 아래의 코드와 같이 '+'연산자를 이용해서 문자열을 결합하는 경우 인스턴스 내의 문자열이 바뀌는 것이 아니라 새로운 문자열("ab")이 담긴 String인스턴스가 생성되는 것이다.  

```Java
String a = "a";
String b = "b";
String a = a + b;
```

덧셈연산자(+)를 사용해서 문자열을 결합하는 것은 매 연산 시마다 새로운 문자열을 가진 String인스턴스가 생성되어 메모리공간을 차지하게 되므로 가능한 한 결합횟수를 줄이는 것이 좋다.  
문자열간의 결합이나 추출 등 문자열을 다루는 작업이 많이 필요한 경우에는 String클래스 대신 StringBuffer클래스를 사용하는 것이 좋다.  

  

리터럴로 문자열을 생성했을 경우, 같은 내용의 문자열들은 모두 하나의 String인스턴스를 참조하도록 되어 있다. 그러나 String클래스의 생성자를 이용한 String인스턴스의 경우에는 new연산자에 의해서 메모리할당이 이루어지기 때문에 항상 새로운 String인스턴스가 생성된다.

  

```Java
class StringEx2 {
	public static void main(String args[]) {
		String s1 = "AAA";
		String s2 = "AAA";
		String s1 = "BBB";
		String s2 = "BBB";
	}
}
```

위의 예제를 컴파일 하면 StringEx2.class파일이 생성된다. 이 파일의 내용을 16진 코드에디터로 보면 "AAA", "BBB"가 있는 것을 발견할 수 있다.  
String리터럴들은 컴파일 시에 클래스파일에 저장된다. 위의 예제를 실행하게 되면 "AAA"라는 문자열을 담고 있는 String인스턴스가 하나 생성된 후, 참조변수 s1, s2, s3는 모두 이 String인스턴스를 참조하게 된다.  

  

✷ 넘어가도 되는 내용

String클래스의 intern()은 String인스턴스의 문자열을 'constant pool'에 등록하는 일을 한다. 등록하고자 하는 문자열이 'constant pool'에 이미 존재하는 경우에는 그 문자열의 주소값을 반환한다.

  

### 빈 문자열(empty string)

---

크기가 0인 배열이 존재할 수 있을까? 답은 'Yes'이다. char형 배열도 크기가 0인 배열을 생성할 수 있고, 이 배열을 내부적으로 가지고 잇는 문자열이 바로 빈 문자열이다.  
String s = "";과 같은 문장이 있을 때, 참조변수 s가 참조하고 있는 String인스턴스는 내부에 'new char[0]'과 같이 크기가 0인 char형 배열을 저장하고 있는 것이다.  

  

그러나 String s = "";과 같은 표현이 가능하다고 해서 char c = '';와 같은 표현도 가능한 것은 아니다.  
일반적으로 변수를 선언할 때, 각 타입의 기본값으로 초기화 하지만 String은 참조형 타입의 기본값인 null 보다는 빈 문자열로, char형은 기본값인 '₩u0000' 대신 공백으로 초기화 하는 것이 보통이다.  

  

## StringBuffer클래스

### SrtingBuffer클래스의 특징

---

내부적으로 문자열 편집을 위한 버퍼(buffer)를 가지고 있으며, StringBuffer인스턴스를 생성할 때 그 크기를 지정할 수 있다.

StringBuffer클래스는 String클래스와 같이 문자열을 저장하기 위한 char형 배열의 참조변수를 인스턴스변수로 선언해 놓고 있다. StringBuffer인스턴스가 생성될 때, char형 배열이 생성되며 이 때 생성된 char형 배열을 인스턴스변수 value가 참조하게 된다.

```Java
public final class StringBuffer implements java.io.Serializable
{
	private char[] value;
	...
}
```

  

### StringBuffer클래스의 생성자

---

StringBuffer클래스의 인스턴스를 생성할 때, 적절한 크기의 char형 배열이 생성되고, 이 배열은 문자열을 저장하고 편집하기 위한 공간(buffer)으로 사용된다.

  

### StringBuffer인스턴스의 비교

---

StringBuffer클래슨느 equals메서드를 오버라이딩하지 않아서 StringBuffer클래스의 equals메서드를 사용해도 등가비교연산자(==)로 비교한 것과 같은 결과를 얻는다.  
반면에 toString()은 오버라이딩되어 있어서 StringBuffer인스턴스에 toString()을 호출하면, 담고있는 문자열을 String으로 반환한다.  

그래서 StringBuffer인스턴스에 담긴 문자열을 비교하기 위해서는 StringBuffer인스턴스에 toString()을 호출해서 String인스턴스를 얻은 다음, 여기에 equals메서드를 사용해서 비교해야한다.

  

## Math클래스

### Math클래스

---

Math클래스는 기복적인 수학계산에 유용한 메서드로 구성되어 있다.

abs

ceil

floor

max

min

random

rint

round

주어진 값의 절대값을 반환한다.

주어진 값을 올림하여 반환한다.

주어진 값을 버림하여 반환한다.

주어진 두 값을 비교하여 큰 쪽을 반환한다.

주어진 두 값을 비교하여 큰 쪽을 반환한다.

0.0~1.0 범위의 임의의 double값을 반환한다. 1.0은 포함되지 않는다.

주어진 double값과 가장 가까운 정수값을 double형으로 반환한다.

소수점 첮째자리에서 반올림한 정수값(long)을 반환한다.

  

## Wrapper클래스

### wrapper클래스

---

기본형(primitive type) 변수도 때로는 객체로 다루어져야하는 경우가 있다. 예를 들면, 매개변수로 객체를 요구할 때, 기본형 값이 아닌 객체로 저장해야할 때, 객체간의 비교가 필요할 때 등등의 경우에는 기본형 값들을 객체로 변환하여 작업을 수행해야 한다.  
이 때 사용되는 것이 wrapper클래스이다. 8개의 기본형을 대표하는 8개의 wraper클래스가 있는데, 이 클래스들을 이용하면 기본형 값을 객체로 다룰 수 있다.  

wrapper클래스들은 모두 equals()가 오버라이딩되어 있어서 주소값이 아닌 객체가 가지고 있는 값을 비교한다.  
그 밖에도 wrapper클래스들은 MAX_VLAUE, MIN_VLAUE, SIZE, TYPE 등의 static멤버를 공통적으로 가지고 있다.  

  

### Number클래스

---

Number클래스는 추상클래스로 내부적으로 숫자를 멤버변수로 갖는 wrapper클래스들의 조상이다. Number클래스 자손으로 BigInteger와 BigDecimal 등이 있는데, BigInteger는 long으로도 다룰 수 없는 큰 범위의 정수를, BigDecimal은 double로도 다룰 수 없는 큰 범위의 부동 소수점수를 처리하기 위한 것으로 연산자의 역할을 대신하는 다양한 메서드를 제공한다.