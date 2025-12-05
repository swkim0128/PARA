---
type: Java
archive: false
---
java.util패키지를 중심으로 실제 프로그래밍에 자주 사용되는 클래스들을 골라서 다음과 같이 세가지 그룹으로 나누어 설명.

> 1. 컬렉션 프레임웍(Collection Framework)  
> - 다수의 데이터를 쉽게 처리할 수 있는 표준화된 방법을 제공하는 클래스들  
> 2. 유용한 클래스 - 알아두면 ㅈ호은 자주 쓰이는 클래스들  
> 3. 형식화 클래스 - 데이터를 표준화된 형식으로 출력하는데 도움을 주는 클래스들  

  

## 컬렉션 프레임웍(Collection Framework)

컬렉션 프레임웍이란, '데이터 군을 저장하는(Vector와 같은) 클래스들을 표준화한 설계'를 뜻한다. 컬렉션(Collection)은 다수의 데이터, 즉 데이터 그룹을 프레임웍은 표준화된 프로그래밍 방식을 의미한다.

  

### 컬렉션 프레임웍의 핵심 인터페이스 - List, Set, Map

---

컬렉션 프레임웍에서는 컬렉션(데이터 그룹)을 크게 3가지 타입이 존재한다고 인식하고 각 컬렉션을 다루는데 필요한 기능을 가진 3개의 인터페이스를 정의하였다. 그리고 인터페이스 List와 Set의 공통된 부분을 다시 뽑아서 새로운 인터페이스인 Colleciton을 추가로 정의

Map인터페이스는 이들과는 전혀 다른 형태로 컬렉션(데이터 군)을 다루기 때문에 같은 상속계층도에 포함되지 못했다.

List

Set

Map

순서가 있는 데이터의 집합, 데이터의 중복을 허용한다.

순서를 유지하지 않는 데이터의 집합, 데이터의 중복을 허용하지 않는다.

키(key)와 값(value)의 쌍(pair)으로 이루어진 데이터의 집합  
순서는 유지되지 않으며, 키는 중복을 허용하지 않고, 값은 중복을 허용한다.  

  

**Collection인터페이스**

Collection인터페이스에 정의된 메서드

  

**List인터페이스**

중복을 허용하면서 저장순서가 유지되는 컬렉션을 구현하는데 사용된다. 구현한 클래스로는 ArrayList, LinkedList, Vector, Stack 등이 있다.

  

**Set인터페이스**

중복을 허용하지 않고 저장순서가 유지되지 않는 컬렉션 클래스를 구현하는데 사용된다. Set인터페이스를 구현한 클래스로는 HashSet, TreeSet 등이 있다.

  

**Map인터페이스**

Map인터페이스는 키(key)와 값(value)을 하나의 쌍으로 묶어서 저장하는 컬렉션 클래스를 구현하는 데 사용된다. 키는 중복될 수 없지만 값은 중복을 허용한다. 기존에 저장된 데이터와 중복된 키와 값을 저장하면 기존의 값은 없어지고 마지막에 저장된 값이 남게 된다. Map인터페이스를 구현한 클래스로는 Hashtable, HasMap, LinkedHashMap, SortedMap, TreeMap 등이 있다.

  

**Map.Entry인터페이스**

Map.Entry인터페이스는 Map인터펭스의 내부 인터페이스이다. 내부 클래스(inner class)와 같이 언터페이스도 이처럼 인터페이스 안에 인터페이스를 정의하는 내부 인터페이스(inner interface)를 정의하는 것이 가능하다.  
Map에 저장되는 key-value쌍을 다루기 위해 내부적으로 Entry인터페이스를 정의해 놓았다. 이것은 보다 객체지향적으로 설계하도록 유도하기 위한 것으로 Map인터페이스를 구현하는 클래스에서는 Map.Entry인터페이스도 함께 구현해야한다.  

  

### 동기화(Synchronization)

---

멀티쓰레드(multi-thread) 프로그래밍에서는 하나의 객체를 여러 쓰레드가 동시에 접근할 수 있기 때문에 딩터의 일관성(consistency)을 유지하기 위해서는 동기화(synchronization)가 필요하다.

새로 추가된 ArrayList와 HashMap과 같은 컬렉션은 동기활르 자체적으로 처리하지 않고 필요한 경우네만 java.util.Collections클래스의 동기화 메서드를 이용해서 동기화처리가 가능하도록 변경하였다.  
이 밖에도 여러 가지 이유로, 가능하면 Vector보다는 ArrayList를, Hashtable보다는 HashMap을 사용하는 것이 바람직하다.  

  

### Vector와 ArrayList

---

이 둘은 List인터페이스를 구현하기 때문에 데이터의 저장순서가 유지되고 중복을 허용한다는 공통적인 특징을 갖는다.

ArrayList는 기존의 Vector를 개선한 것으로 Vector와 구현원리와 기능적인 측면에서 동일하다고 할 수 있다. 앞에서 얘기했던 것과 같이 Vector는 기존에 작성된 소스와의 호환성을 위해서 계속 남겨 두고 있을 뿐이기 때문에 가능하면 Vector보다는 ArrayList를 사용하자.

  

공통점

- List 인터페이스를 구현한다.  
저장순서가 유지되고 중복을 허용한다.  

- 데이터의 저장 공간으로 배열을 사용한다.

차이점

- Vector는 멀티쓰레드에 대한 동기화가 되어 있으나 ArrayList는 그렇지 않다.

  

### LinkedList

---

배열은 가장 기본적인 형태의 자료구조로 구조가 간단하며 사용하기 쉽고 데이터를 읽어 오는데 걸리는 시간(접근시간, access time)이 가장 빠르다는 장점을 가지고 있지만 다음과 같은 단점도 가지고 있다.

> 1. 크기를 변경할 수 없다.  
> - 크기를 변경할 수 없기 때문에 새로운 배열을 생성해서 데이터를 복사하는 작업이 필요하다.  
> - 실행속도를 향상시키기 위해서는 충분히 큰 크기의 배열을 생성해야하므로 메모리가 낭비된다.  
>   
> 2. 비순차적인 데이터의 추가 또는 삭제에 시간이 많이 걸린다.  
> - 차례대로 데이터를 추가하고 마지막에서부터 데이터를 삭제하는 것은 빠르지만,  
> - 배열의 중간에 데이터를 추가하려면, 빈자리를 만들기 위해 다른 데이터들을 복사해서 이용해야 한다.  

이러한 배열의 단점을 보완하기 위해서 링크드리스트(linked list)라는 자료구조가 고안되었다. 배열은 모든 데이터가 연속적으로 존재하지만 링크드리스트는 분연속적으로 존재하는 데이터를 서로 연결(link)한 형태로 구성되어 있다.

```Java
class Node {
	Node next;    // 다음 요소의 주소를 저장
	Object obj;   // 데이터를 저장
}
```

  

링크드리스트는 이동방향이 단방향이기 때문에 다음 요소에 대한 접그은 쉽지만 이전요소에 대한 접근은 어렵다. 이 점을 보완한 것이 더블 링크드리스트(이중 연견리스트, doubly linked list)이다.

```Java
class Node {
	Node next;    // 다음 요소의 주소를 저장
	Node previous;  // 이전 요소의 주소를 저장
	Object obj;     // 데이터를 저장
}
```

  

더블 링크드리스트의 접근성을 보다 향상시킨 것이 더블 써큘러 링크드리스트(이중 원형 연결리스트, doubly circular linked list)

실제로 LinkedList클래스는 이름과 달리 링크드리스트가 아닌 더블 써큘러 링크드리스트로 구현했는데, 이는 링크드리스트의 단점인 낮은 접근성(accessability)을 높이기 위한 것.

  

1. 순차적으로 추가/삭제하는 경우에는 ArrayList가 LinkedList보다 빠르다.
2. 중간 데이터를 추가/삭제하는 경우에는 LinkedList가 ArrayList보다 빠르다.

  

### Stack과 Queue

---

순차적으로 데이터를 추가하고 삭제하는 스택에는 ArrayList와 같은 배열기반의 컬렉션 클래스가 적합하지만, 큐는 데이터를 꺼낼 때 항상 첫 번째 저장된 데이터를 삭제하므로 데이터의 추가/삭제가 쉬운 LinkedList로 구현하는 것이 더 적합.

  

### Enumeration, Iterator, Listlterator

---

Enumeration, Iterator, Listlterator는 모두 컬렉션에 저장된 요소를 접근하는데 사용되는 인터페이스이다. Enumeration은 Iterator의 구버전이며, ListIterator는 Iterator의기능을 향상 시킨 것이다.

  

**Iterator**

컬렉션 프레임웍에서는 컬렉션에 저장된 요소들을 읽어오는 방법을 표준화하였다. 컬렉션에 저장된 각 요소에 접근하는 기능을 가진 Iterator인터페이스를 정의하고, Collection인터페이스에는 Iterator(Iterator를 구현한 클래스의 인스턴스)를 반환하는 iterator()를 정의하고 있다.

```Java
public interface Iterator {
	boolean hasNext();
	Object next();
	void remove();
}

public interface Collection {
	...
	public Iterator iterator();
	...
}
```

List나 Set인터페이스를 구현하는 컬렉션은 iterator()가 각 컬렉션의 특징에 알맞게 작성되어 있다. 컬렉션 클래스에 대해 interator()를 호출하여 Iterator를 얻은 다음 반복문(주로 while문)을 사용해서 컬렉션클래스의 요소들을 읽어 올 수 있다.

```Java
List list = new ArrayList();

Iterator it = list.iterator();
while(it.hasNext()) {
	System.out.println(it.next());
}
```

  

Map인터페이스를 구현한 컬렉션 클래스는 키(key)와 값(value)을 쌍(pair)으로 저장하고 있기 때문에 iterator()를 직접 호출할 수 없고, 그 대신 keySet()이나 entrySet()과 같은 메서드를 통해서 키와 값을 각각 따로 Set의 형태로 얻어 온 후에 다시 iterator()를 호출해야 Iterator를 얻을 수 있다.

```Java
Map map = new HashMap();
...
Iterator it = map.keySet().iterator();
```

  

**Enumeration과 ListIterator**

Enumeration은 컬렉션 프레임웍이 만들어지기 이전에 사용하던 것으로 iterator의 구버전이라고 생각하면 된다. 이전 버전으로 작성된 소스와의 호환을 위해서 남겨 두고 있을뿐이므로 가능하면 Enumeration대신 Iterator를 사용하자.

ListIterator는 Iterator를 상속받아서 기능을 추가한 것으로, 컬렉션의 요소에 접근할 때 Iterator는 단방향으로만 이동할 수 있는 데 반해 ListIterator는 양방향으로의 이동이 가능하다. 다만, ArrayList나 LinkedList와 같이 List인터페이스를 구현한 컬렉션에서만 사용할 수 있다.

메서드 중에서 '선택적 기능(optional operation)'이라고 표시된 것들은 반드시 구현하지 않아도 된다. 예를 들어 Iterator인터페이스를 구현하는 클래스에서 remove()는 선택적인 기능이므로 구현하지 않아도 괜찮다. 그렇다하더라도 인터페이스로부터 상속받은 메서드는 추상메서드라 메서드의 몸통(body)을 반드시 만들어 주어야 하므로 다음과 같이 처리한다.

```Java
public void remove() {
	throw new UnsupportedOperationException();
}
```

  

### HashSet

---

HashSet은 Set인터페이스를 구현한 가장 대표적인 컬렉션이며, Set인터페이스의 특징대로 HashSet은 중복된 요소를 저장하지 않는다.  
HashSet에 새로운 요소를 추가할 때는 add메서드나 addAll메소드를 사용하는데, 만일 HashSet에 이미 저장되어 있는 요소와 중복된 요소를 추가하고자 한다면 이 메서드들은 false를 반환함으로써 중복된 요소이기 때문에 추가에 실패했다는 것을 알린다.  

ArrayList와 같이 List인터페이스를 구현한 컬렉션과 달리 HashSet은 저장순서를 유지하지 않으므로 저장순서를 유지하고자 한다면 LinkedHashSet을 사용해야한다.

  

- 오버라이딩을 통해 작성된 hashCode메서드는 다음의 세 가지 조건을 만족 시켜야 한다.
    
    1. 실행 중인 어플리케이션 내의 동일한 객체에 대해서 여러번 hashCode()를 호출해도 동일한 int값을 반환해야 한다. 하지만, 실행시마다 동일한 int값을 반환할 필요는 없다.(단, equals메서드의 구현에 사용된 멤버변수의 값이 바뀌지 않았다고 가정한다.)
    2. equals메서드를 이용한 비교에 의해서 true를 얻은 두 객체에 대해 각각 hashCode()를 호출해서 얻은 결과는 반드시 같아야 한다.
    3. equals메서드를 호출했을 때 false를 반환하는 두 객체는 hashCode() 호출에 대해 값은 int값을 반환하는 경우가 있어도 괜찮지만, 해싱(hashing)을 사용하는 컬렉션의 성능을 향상시키기 위해서는 다른 int값을 반환하는 것이 좋다.
    
      
    

### TreeSet

---

TreeSet은 이진검색트리(binarysearch tree)라는 자료구조의 형태로 데이터를 저장하는 컬렉션 클래스이다. 이진검색트리는 정렬, 검색, 범위검색(range search)에 뛰어난 성능을 보이는 자료구조이며 TreeSet은 이진검색트리의 성능을 향상시킨 '레드-블랙 트리(Red-Black tree)'로 구현되어 있다.  
그리고 Set인터페이스를 구현했으므로 중복된 데이터의 저장을 허용하지 않으며 정렬된 위치에 저장하므로 저장순서를 유지하지도 않는다.  

  

트리는 데이터를 순차적으로 저장하는 것이 아니라 저장위치를 찾아서 저장해야하고, 삭제하는 경우 트리의 일부를 재구성해야하므로 링크드리스트보다 데이터의 추가삭제시간은 더 걸린다. 그 대신 배열이나 링크드리스트에 비해 검새고가 정렬기능은 훨씬 뛰어나다.

> 이진검색트리(binary search tree)는  
> - 모든 노드는 최대 두 개의 자식 노드를 가질 수 있다.  
> - 왼쪽 자식노드의 값은 부모노드의 값보다 작고 오른쪽자식노드의 값은 부모노드의 값보다 커야한다.  
> - 노드의 추가 삭제에 시간이 걸린다.(순차적으로 젖아하지 않으므로)  
> - 검색과 정렬에 유리하다.  

  

### Comparator와 Comparable

---

Comparator와 Comparable은 모두 인터페이스로 객체들을 정렬 또는 이진검색트리를 구성하는데 필요한 메서드를 정의하고 있다.  
Comparable을 구현하고 있는 클래스들은 같은 타입의 인스턴스끼리 서로 비교할 수 있는 클래스들, 주로 Integer와 같은 wrapper클래스(Boolean제외)와 String, Date, File과 가은 것들이며 기본적으로 오름차순, 즉 작은 값에서부터 근 값의 순으로 정렬되도록 구현되어 있다. 그래서 Comparable을 구현한 클래스는 정렬이 가능하다는 것을 의미한다.  

만일 Comparable을 구현하지 않은 클래스의 인스턴스를 TreeSet에 담는 다면 어떻게 될까? 정렬기준이 없기 때문에 당연히 알아서 정렬되지 않을 뿐더러 컴파일 에러는 발생하지 않지만 실행 시 에러가 발생한다.

> Comparable - 기본 정렬기준을 구현하는데 사용.  
> Compartor - 기본 정렬기준 외에 다른 기준으로 정렬하고자할 때 사용  

  

Comparator와 Comparable의 실제 소스는 다음과 같다.

```Java
public interface Comparator {
	int compare(Object o1, Object o2);
	boolean equals(Object obj);
}

public interface Comparable {
	public int compareTo(Object o);
}
```

compare()와 compareTo()는 선언형태와 이름이 약간 다를 뿐 두 객체를 비교한다는 같은 기능을 목적으로 고안된 것이다. compareTo()의 반환값은 int이지만 실제로는 비교하는 두 객체가 같으면 0, 비교하는 값보다 작으면 음수, 크면 양수를 반환하도록 구현해야한다. 이와 마찬가지로 compare()도 객체를 비교해서 음수, 0, 양수 중의 하나를 반환하도록 구현해야한다.

  

- TreeSet을 생성할 때 Comparator를 지정해주지 않으면 저장하는 객체(주로 Comparable을 구현한 클래스의 객체)에 구현된 정렬방식에 따라 정렬하여 저장하게 된다. 그러나 Comparator를 지정해주면 지정된 Compartor에 구현된 정렬방식에 따라 정렬하여 저장한다.

  

### Hashtable과 HashMap

---

Hashtable과 HashMap의 관계는 Vector와 ArrayList의 관계와 같아서 Hashtable보다는 새로운 버번인 HashMap을 사용할 것을 권한다.  
HashMap은 Map을 구현했으므로 앞에서 살펴본 Map의 특징, 키(key)와 값(value)을 묶어서 하나의 데이터(entry)로 저장한다는 특징을 갖는다. 그리고 해싱(hashing)을 사용하기 때문에 많은 양의 데이터를 검색하는데 있어서 뛰어난 성능을 보인다.  

  

```Java
public class HashMap extends AbstarctMap implements Map, Cloneable, Serializable {
	transient Entry[] table;
	...
	static class Entry implements Map.Entry {
		final Object key;
		Object value;
		...
	}
}
```

HashMap은 Entry라는 내부 클래스를 정의하고, 다시 Entry타입의 배열을 선언하고 있다.

> 키(key) - 컬렉션 내의 키(key) 중에서 유일해야 한다.  
> 값(value) - 키(key)와 달리 데이터의 중복을 허용한다.  

  

- 해싱(hashing)이란 해시함수(hash function)를 이용해서 데이터를 해시테이블(hash table)에 쩌아하고 검색하는 기법. 해시함수는 데이터가 저장되어 있는 곳을 알려 주기 때문에 다량의 데이터 중에서도 원하는 데이터를 빠르게 찾을 수 있다.

  

### TreeMap

---

이진검색트리의 형태로 키와 값의 쌍으로 이루어진 데이터를 저장한다. 그래서 검색과 정렬에 적합한 컬렉션 클래스이다. 범위검색이나 정렬이 필요한 경우에는 TreeMap을 사용하자.

  

### Properties

---

Properties는 HashMap의 구버전인 Hashtable을 상속받아 구현한 것으로, Hashtable은 키와 값을 (Object, Object)의 형태로 저장하는데 비해 Properties는 (String, String)의 형태로 젖아하는 보다 단순화된 컬렉션클래스이다.  
주로 어플리케이션의 환경설정과 관련된 속성(property)을 저장하는데 사용되며 데이터를 파일로부터 읽고 쓰는 편리한 기능을 제공한다.  

데이터를 저장하는데 사용되는 setProperty()는 단순히 Hashtable의 put메서드를 호출할 뿐이다. 그리고 setProperty()는 기존에 같은 키로 저장된 값이 있는 경우 그 값을 Object타입으로 반환하며, 그렇지 않을 때는 null을 반환한다.  
getProperty()는 Properties에 저장된 값을 읽어오는 일을 하는데, 만일 읽어오려는 키가 존재하지 않으면 지정된 기본값(defaultValue)을 반환한다.  

  

Properties는 Hashtable을 상속받아 구현한 것이라 Map의 특성상 저장순서를 유지하지 않는다.  
Properties는 컬렉션프레임웍 이전의 구버전이므로 Iterator가 아닌 Enumeration을 사용한다.  
그리고 list메서드를 이용하면 Properties에 저장된 모든 데이터를 화면 또는 파일에 편리하게 출력할 수 있다.  

  

### 컬렉션 클래스 정리 & 요약

---

컬렉션

ArrayList  
  

LinkedList

HashMap  
  

TreeMap

Stack

Queue

Properties

HashSet

TreeSet

LinkedHashMap  
LinkedHashSet  

특 징

배열기반, 데이터의 추가와 삭제에 불리, 순차적인 추가삭제는 제일 빠름.  
임의의 요소에 대한 접근성(accessibility)이 뛰어남.  

연결기반, 데이터의 추가와 삭제에 유리, 임의의 요소에 대한 접근성이 좋지 않다.

배열과 연결이 결합된 형태, 추가, 삭제, 검색, 접근성이 모두 뛰어남. 검색에는 최고성능을 보인다.

연결기반, 정렬과 검색(특히 범위검색)에 적합. 검색성능은 HashMap보다 떨어짐

Vector를 상속받아 구현

LinkedList가 Queue인터페이스르 구현

Hashtable을 상속받아 구현

HashMap을 이용해서 구현

TreeMap을 이용해서 구현

HashMap과 HashSet에 저장순서유지기능을 추가하였음.

  

## 유용한 클래스들

### Calendar와 Date

---

자바에서는 날짜와 시간에 관련된 데이터를 쉽게 처리할 수 있도록 Calendar나 Date를 제공. 가능하면 Date보다는 Calendar를 사용하도록 하자.

> 1. Calendar를 Date로 변환  
> Calendar cal = Calendar.getInstance();  
> ...  
> Date d = new Date(cal.getTimeInMillis()); // Date(long date)  
>   
> 2. Date를 Calendar로 변환  
> Date d = new Date();  
> ...  
> Calendar cal = Calendar.getInstance();  
> cal.setTime(d);  

  

Calendar는 추상클래스이기 때문에 직접 객체를 생성할 수 없고, 메서드를 통해서 완전히 구현된 클래스의 인스턴스를 얻어야 한다.

```Java
Calendar cal = new Calendar();    // 에러!!! 추상클래스는 인스턴스를 생성할 수 없다.

// OK, getInstance()메서드는 Calendar 클래스를 구현한 클래스의 인스턴스를 반환한다.
Calendar cal = Calendar.getInstance();
```

  

Calendar를 상속받아 완전히 구현한 클래스로는 GregorianCalendar와 BuddhistCalendar가 있는데 getInstance()는 시스템의 국가와 지역설정을 확인해서 태국인 경우에는 BuddhistCalendar의 인스턴슬르 반환하고, 그 외에는 GregorianCalendar의 인스턴스를 반환한다.

  

getInstance()를 통해서 얻은 인스턴스는 기본적으로 현재 시스템의 날짜와 시간에 대한 정보를 담고 있다. 원하는 날짜나 시간으로 설정하려면 set메서드를 사용하면 된다.

get메서드의 매개변수로 사용되는 int값들은 Calendar에 정의된 static상수이다.

> System.out.println("월(0-11, 0:1월) : " + today.get(Calendar.MONTH));

한가지 주의해야할 것은 get(Calendar.MONTH)로 얻어오는 값의 범위가 1 ~ 12가 아닌 0~11이라는 것이다.

  

### Random

---

난수를 얻는 방법을 생각하면 Math.random()이 떠오를 것이다. 그리고 Random클ㄹ새를 사용하는 방법도 있는데, 몇가지 추가적인 기능을 제외하고는 Math.random()과 다르지 않다.

그래서 대부분의 경우 Math.random()만 사용해도 난수를 얻는데 별 어려움이 ㅇ벗기 때문에 가능하면 Random 보다는 Math.random()을 사용할 것을 권한다.

  

### 정규식(Regular Expression) - Pattern. Match

---

정슈식이란 텍스트 데이터 중에서 원하는 조건(패턴, pattern)과 일치하는 문자열을 찾아내기 위해 사용하는 것으로 미리 정의된 기호와 문자를 이용해서 작성한 문자열을 말한다.

> 1. 정규식을 매개변수로 Pattern클래스의 static메서드인 Pattern compile(String regex)을 호출하여 Pattern인스턴스를 얻는다.  
> Pattern p = Pattern.compile("c[a-z]*");  
>   
> 2. 정규식으로 비교할 대상을 매개변수로 Pattern클래스의 Matcher matcher(CharSequenceinput)를 호출해서 Matcher인스턴슬르 얻는다.  
> Matcher m = p.matcher(data[i]);  
>   
> 3. Matcher인스턴스에 boolean matches()를 호출해서 정규식에 부합하는지 확인한다.  
> if(m.matches())  

  

Matcher의 find()로 정규식과 일치하는 부분을 찾으면, 그 위치를 start()와 end()로 알아낼 수 있고 appendReplacement(StringBuffer sb, Stringreplacement)를 이용해서 원하는 문자열(replacement)로 치환할 수 있다. 치환된 결과는 StringBuffer인 sb에 저장되는데 sb에 저장되는 내용을 단계별로 살펴보면 이해하기 쉬울 것이다.

> 1. 문자열 source에서 "broken"을 m.find()로 찾은 후 첫 번째로 m.appendReplacement(sb, "drunken");가 호출되면 source의 시작부터 "broken"을 찾은 위치까지의 내요에 "drunkne"을 더해서 저장한다.  
> - sb에 저장된 내용 : "A drunken"  
> 2. m.find()는 첫 번째로 발견된 위치의 끝에서부터 다시 검색을 시작하여 두 번째 "broken"을 찾게 된다. 다시 m.appendReplacement(sb, "drunken");가 호출  
> - sb에 젖아된 내용 : "A drunken hand works, but not a drunken"  
> 3. m.appendTail(sb);이 호출되면 마지막으로 치환된 이후의 부분을 sb에 덧붙인다.  
> - sb에 저장된 내용 : "A drunken hand workds, but not a drunken heart."  

  

### Scanner

---

Scanner는 화면, 파일, 문자열과 같은 입력소스로부터 문자데이터를 읽어오는데 도움을 줄 목적으로 JDK1.5부터 추가되었다.  
Scanner에는 다음과 같은 생성자를 지원하기 때문에 다양한 입력소스로부터 데이터를 읽을 수 있다.  

> Scanner(String source)  
> Scanner(File source)  
> Scanner(File source, String charsetName)  
> Scanner(InputStream source, String charsetName)  
> Scanner(Readable source)  
> Scanner(ReadableByteChannel source)  
> Scanner(ReadableByteChannel source, String charsetName)  

  

Scanner는 정규식 표현(Regular expression)을 이용한 라인단위의 검색을 지원하며 구분(delimiter)에도 정규식 표현을 사용할 수 있어서 복잡한 형태의 구분자도 처리가 가능하다.

> Scanner useDelimiter(Pattern pattern)  
> Scanner useDelimiter(String pattern)  

  

### StringTokenizer

---

StringTokenizer는 긴 문자열을 지정된 구분자(delimiter)를 기준으로 토큰(token)이라는 여러 개의 작은 분자열로 잘라내는 데 사용된다.  
StringTokenizer를 이용하는 방법 이외에도 String의 split(String regex)를 사용해서 String[] result = "100,200,300,400".split(",")와 같이 하거나 Scanner의 Scanner(String source)와 Scanner useDelimiter(String pattern)를 사용해서 Scanner sc2 = new Scanner("100,200,300,400").useDelimiter(","); 와 같이 할 수 도 있지만 이 두 가지 방법은 정규식 표현(Regular expression)을 사용해야 하므로 정규식 표현에 익숙하지 않은 경우 StringTokenizer를 사용하는 것이 간단하면서도 명확한 결과를 얻을 수 있을 것이다.  

StringTokenizer는 구분자로 단 하나의 문자 밖에 사용하지 못하기 때문에 보다 복잡한 형태의 구분자로 문자열을 나누어야 할 때는 Scanner나 split메서드를 사용해야 할 것이다.

  

## 형식화 클래스

형식화 클래스는 java.text패키지에 포함되어 있으며 숫자, 날짜, 텍스트 데이터를 일정한 형식에 맞게 표현할 수 있는 방법을 객체지향적으로 설계하여 표준화하였다.

  

### DecimalFormat

---

형식화 클래스 중에서 숫자를 형식화 하는데 사용되는 것이 DecimalFormat이다. DecimalFormat을 이용하면 숫자 데이터를 정수, 부동소수점, 금액 등의 다양한 형식으로 표현할 수 있으며, 반대로 일정한 형식의 텍스트 데이터를 숫자로 쉽게 변환하는 것도 가능하다.

  

기호

  
0  
  

  
#  
  

.

-  
  

,  
  

  
  
  
E  
  
  
  
  

;  
  

%

₩u2030

₩u00A4

`

의미

  
10진수(값이 없을 때는 0)  
  

  
10진수  
  

소수점

음수부호  
  

단위 구분자  
  

  
  
  
지수기호  
  
  
  
  

패턴 구분자  
  

퍼센트

퍼밀(퍼센트 x 10)

통화

escape문자

패턴

0  
0.0  
000000000.0000  

#  
#.#  
######.####  

#.#

#.\#-  
-#.#  

#,###.##  
#,####.##  

\#E0  
0E0  
#\#E0  
00E0  
###\#E0  
0000E0  
#.\#E0  
0.0E0  

#,###.##+;#,###.#\#-  
  

#.#%

#.#₩u2030

₩u00A4 #,###

'#'#,###  
''#,###  

결과(1234567.89)

1234568  
1234567.9  
001234567.8900  

1234568  
1234567.9  
1234567.89  

1234567.9

1234567.9-  
-1234567.9  

1,234,567.89  
123,4567.89  

.1E7  
1E6  
1.2E6  
12E5  
123.5E4  
1235E3  
1.2E6  
1.2E6  

1,234,567.89+  
1,234,567.89-  

123456789%

1234567890%

₩ 1,234,568

\#1,234,568  
'1,234,568  

  

  

### SimpleDateFormat

---

Date와 Calendar만으로는 날짜 데이터를 원하는 형태로 다양하게 출력하는 것은 불편하고 복잡하다. 그러나 SimpleDateFormat을 사용하면 이러한 문제들이 간단하게 해결된다.

```Java
Date today = new Date();
SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd");

// 오늘 날짜를 yyyy-MM-dd형태로 변환하여 변환한다.
String result = df.format(today);
```

  

### ChoiceFormat

---

ChoiceFormat은 특정 범위에 속하는 값을 문자열로 변환해준다. 연속적 또는 불연속적인 범위의 값들을 처리하는 데 있어서 if 문이나 switch문은 적절하지 못한 경우가 많다. 이럴 때 ChoiceFormat을 잘 사용하면 복잡하게 처리될 수밖에 없었던 코드를 간단하고 직관적으로 만들 수 있다.

그 외에도 활용하기에 따라 if문과 switch문을 대신해서 다양한 용도로 유용하게 쓰일 수 있으므로 잘 알아두도록 하자.

```Java
double[] limits = {60, 70, 80, 90};
String[] grades = {"D", "C", "B", "A"};

int [] scores = {100, 96, 88, 70, 52, 60, 70};

ChoiceFormat form = new ChoiceFormat(limits, grades);

for (int i = 0; i < scores.length; i++) {
	System.out.println(scores[i] + ":" + form.format(scores[i]));
}
```

  

### MessageFormat

---

MessageFormat은 데이터를 정해진 양식에 맞게 출력할 수 있도록 도와준다. 데이터가 들어갈 자리를 마련해 놓은 양식을 미리 작성하고 프로그램을 이용해서 다수의 데이터를 같은 양식으로 출력할 때 사용하면 좋다.

  

## 제네릭스(Generics)

제네릭스는, JDK1.5에서의 가장 큰 변화 중의 하나로, 다양한 타입의 객체들을 다루는 메서드나 컬렉션 클래스에 컴파일 시의 타입 체크(compile-time type check)를 해주는 기능이다. 객체의 타입을 컴파일 시에 체크하기 때문에 객체의 타입 안정성을 높이고 형변환의 번거로움이 줄어든다.

> > 제네릭스의 장점  
> 1. 타입 안정성을 제공한다.  
> 2. 타입체크와 형변환을 생략할 수 있으므로 코드가 간결해 진다.  

  

### ArrayList<E>

---

  

### Iterator<E>

---

  

### Comparable<T>과 Collections.sort()

---

  

### HashMap<K,V>

---