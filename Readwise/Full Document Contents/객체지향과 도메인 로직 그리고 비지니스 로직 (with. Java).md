# 객체지향과 도메인 로직 그리고 비지니스 로직 (with. Java)

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbLB4wB%2FbtsIzn6Uie3%2FAAAAAAAAAAAAAAAAAAAAAAVmW9IG4rQFiotOgksj01bGJbwvCuLToX3fsJsmqsX0%2Fimg.jpg%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1753973999%26allow_ip%3D%26allow_referer%3D%26signature%3DtU%252FoW%252B5Kn6Bt1q0ttiqATV0BibA%253D)

## Metadata
- Author: [[Beekei]]
- Full Title: 객체지향과 도메인 로직 그리고 비지니스 로직 (with. Java)
- Category: #articles
- Document Tags:  #ddd 
- Summary: 객체 지향 프로그래밍에서는 동물처럼 공통된 특성을 가진 객체를 추상화하고 각 객체의 행동을 구현합니다. 도메인 로직은 현실 문제에 대한 해결책이고, 비즈니스 로직은 서비스 목적을 이루기 위한 구체적인 절차입니다. 좋은 코드를 위해 단순함을 유지하고 객체와 로직을 명확히 구분하는 것이 중요합니다.
- URL: https://devbksheen.tistory.com/entry/%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5%EA%B3%BC-%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%A1%9C%EC%A7%81-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EB%B9%84%EC%A7%80%EB%8B%88%EC%8A%A4-%EB%A1%9C%EC%A7%81

## Full Document
**목차** 

저는 코드를 구현할 때 할 때 단순함과 체크 포인트를 가장 중요하게 생각합니다.

체크 포인트란 신경 써야 하는 부분을 말하는데 체크 포인트를 없앨수록 단순함은 올라갈 것입니다.

그럼 어떻게 체크 포인트를 줄이고 단순함을 올릴 것이냐?

여러 가지 방법이 있겠지만 **가장 기본적인 객체 지향 프로그래밍과 도메인 로직, 비즈니스 로직을 구분 지어 코드를 작성하는 것**이라고 생각합니다.

(이제부터는 제 아주 주관적인 생각을 정리한 글입니다. 반박 시 여러분들 말씀이 다 맞습니다!)

이라고 합니다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbLB4wB%2FbtsIzn6Uie3%2FAAAAAAAAAAAAAAAAAAAAAAVmW9IG4rQFiotOgksj01bGJbwvCuLToX3fsJsmqsX0%2Fimg.jpg%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1753973999%26allow_ip%3D%26allow_referer%3D%26signature%3DtU%252FoW%252B5Kn6Bt1q0ttiqATV0BibA%253D)
말로는 잘 이해가 안 되시죠? 그럼 자세히 설명해 보겠습니다.

예를 들어 동물이라는 데이터가 있습니다. 동물에는 여러 가지 종류가 있겠죠.

다리가 4개인 동물, 날개가 있는 동물, 지느러미가 있는 동물

이렇게 케이스별로 3가지 인터페이스로 나누고 동물이라는 공통점을 상속받아 추상화할 수 있습니다.

```
// 동물
public interface Animal {

}

// 다리가 4개인 동물
public interface FourLeggedAnimal extends Animal {

}

// 날개가 있는 동물
public interface WingedAnimal extends Animal {

}

// 지느러미가 있는 동물
public interface FinnedAnimal extends Animal {

}
```

동물의 상태를 생각해 보면 살아있는 상태 <-> 죽은 상태를 생각해 볼 수 있습니다.

여기서 생각해야 하는 부분은 동물의 상태는 모든 동물에게 있을 수 있습니다.

다리가 4개가 있던 날개가 있던 지느러미가 있던 살아있거나 죽어있을 수 있습니다.

그럼 동물의 공통점으로 들어가니 최상위인 Animal 인터페이스에 구현해야 합니다.

```
// 동물
public interface Animal {
    boolean isLive(); // 생사 상태
}
```

행위로는 먹기, 달리기, 날기, 헤엄치기를 생각해 볼 수 있습니다.

먹기는 모든 동물이 가능하기 때문에 최상위인 Animal에 구현해야 하고

달리기는 다리가 4인 동물에, 날기는 날개가 있는 동물에, 헤엄치기는 지느러미가 있는 동물에게 구현해야 합니다.

```
// 동물
public interface Animal {
    boolean isLive(); // 생사 상태
    void eat(Animal animal); // 먹기
}

// 다리가 4개인 동물
public interface FourLeggedAnimal extends Animal {
    void run(); // 달리기
}

// 날개가 있는 동물
public interface WingedAnimal extends Animal {
    void fly(); // 날기
}

// 지느러미가 있는 동물
public interface FinnedAnimal extends Animal {
    void swim(); // 헤엄치기
}
```

자 그럼 상태와 행위를 갖도록 추상화는 끝났으니 객체를 생성해 봅시다.

이때 각 행위들을 객체에 따라 구현해 줍니다.

* 호랑이가 빠르게 달릴 수 있습니다.
* 독수리는 높게 날 수 있습니다.
* 연어는 강을 거꾸로 헤엄칠 수 있습니다.

```
// 호랑이 객체
public class Tiger implements FourLeggedAnimal {
    @Override
    boolean isLive() {
    	return this.statue == LIVE;
    }
    @Override
    void eat(Animal animal) {
        animal.status == DEATH;
        System.out.println("다른 동물 잡아먹기!!");
    }
    @Override
    void run() {
        System.out.println("빠르게 달리기!!");
    }
}

// 독수리 객체
public class Eagle implements WingedAnimal {
    @Override
    boolean isLive() {
    	return this.statue == LIVE;
    }
    @Override
    void eat(Animal animal) {
        System.out.println("다른 동물 잡아먹기!!");
    }
    @Override
    void fly() {
        System.out.println("높게 날기!!");
    }
}

// 연어 객체
public class Salmon implements FinnedAnimal {
    @Override
    boolean isLive() {
    	return this.statue == LIVE;
    }
    @Override
    void eat(Animal animal) {
        System.out.println("다른 동물 잡아먹기!!");
    }
    @Override
    void swim() {
        System.out.println("강을 거꾸로 헤엄치기!!");
    }
}

Tiger tiget = new Tiget(); // 호랑이 객체 생성
Eagle eagle = new Eagle(); // 독수리 객체 생성
Salmon salmon = new Salmon(); // 연어 객체 생성
```

이렇게 추상화하여 상태와 행위를 갖춘 객체를 생성했습니다!

이렇게 만들어진 객체들로 상호작용을 하며 로직을 구성해야 합니다.

만약 독수리가 헤엄치는 연어를 먹고 있었는데 갑자기 호랑이가 나타나 달려와 독수리가 날아서 도망가고 호랑이가 연어를 먹는 로직이 있다고 생각해 봅시다...ㅎ

코드로 작성하면 요렇게 될 것입니다.

```
// 독수리가
Eagle eagle = new Eagle();

// 헤엄치는 연어를
Salmon salmon = new Salmon();
salmon.swim();

// 먹고 있었는데
eagle.eat(salmon);

//  갑자기 호랑이가 나타나 달려와
Tiger tiget = new Tiget();
tiget.run();

// 독수리가 날아서 도망가고
eagle.fly();

// 호랑이가 연어를 먹는다
tiget.eat(salmon);

salmon.isLive(); // false ...ㅠㅠ
```

이렇게 코드를 객체지향 프로그래밍으로 작성하게 되면 굳이 주석을 달지 않아도 코드만 보고 어떤 로직인지 한눈에 파악이 되지 않나요?

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FWJwxa%2FbtsIBC9Q7rQ%2FAAAAAAAAAAAAAAAAAAAAAG8x2PqVpnxbdUxYA_IUBZUBDH0gaZHVg6WJKiJHOc0R%2Fimg.jpg%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1753973999%26allow_ip%3D%26allow_referer%3D%26signature%3DRmenQyYyO5jAi8%252FLmDI5R3Cjzyc%253D)아님 말고 
주의해야 할 점이 있습니다.

위에서 예를 들었을 때 호랑이는 빠르게 달릴 수 있습니다. 하지만 치타도, 표범도 빠르게 달릴 수 있죠

**생각 없이 코드를 작성할 때 자주 실수하는 부분이 객체가 중점이 되는 것이 아닌 달리는 기능이 중점이 돼버리고 맙니다.**

```
void 달리기(FourLeggedAnimal fourLeggedAnimal) {
    if (fourLeggedAnimal == 호랑이 || fourLeggedAnimal == 치타 || fourLeggedAnimal == 표범) {
        System.out.println("빠르게 달리기!!");
    } else {
        System.out.println("느리게 달리기!!");
    }
}
```

만약 이렇게 코드를 작성했다가 빠르게 달릴 수 있는 동물이 새로 생겼다면 해당 코드도 수정이 필요할 것입니다.

여기서 제가 처음에 말했던 체크 포인트가 늘어나는 것입니다.

추상화한 객체를 중심으로 코드를 작성하게 되면 호랑이인지, 치타인지, 표범인지 알 필요가 없게 됩니다.

```
public class 호랑이 implements FourLeggedAnimal {
    @Override
    void run() {
        System.out.println("빠르게 달리기!!");
    }
}

public class 치타 implements FourLeggedAnimal {
    @Override
    void run() {
        System.out.println("빠르게 달리기!!");
    }
}

public class 표범 implements FourLeggedAnimal {
    @Override
    void run() {
        System.out.println("빠르게 달리기!!");
    }
}

public class 거북이 implements FourLeggedAnimal {
    @Override
    void run() {
        System.out.println("느리게 달리기!!");
    }
}

void 달리기(FourLeggedAnimal fourLeggedAnimal) {
    fourLeggedAnimal.run();
}
```

또한 빠르게 달리는 객체가 추가되었을 때 다른 코드들은 건드릴 필요 없이 run 메서드만 구현 해준다면 로직이 실행되는데 문제가 없습니다.

만약 빠르게 달리기를 한 메서드로 사용하고 싶다면 FourLeggedAnimal를 상속받는 FastRunFourLeggedAnimal를 추상화하여 구현도 가능합니다.

```
public interface FastRunFourLeggedAnimal extends FourLeggedAnimal {
    default void run() {
        System.out.println("빠르게 달리기!!");
    }
}

public class 호랑이 implements FastRunFourLeggedAnimal {
    ...
}

public class 치타 implements FastRunFourLeggedAnimal {
    ...
}

public class 표범 implements FastRunFourLeggedAnimal {
    ...
}

호랑이.run(); // 빠르게 달리기!!
```

**항상 객체 지향 프로그래밍에서는 객체가 중점이 되어야 한다는 생각을 하며 코드를 작성해야 합니다.**

그래 이제 객체 지향 프로그래밍이 뭔지는 알겠어..!

여러 블로그나 유튜브를 찾아보면 도메인 로직과 비지니스 로직은 다음과 같다고 합니다.

> 소프트웨어 공학에서 도메인, 비즈니스라는 말은, '소프트웨어가 풀고자 하는 현실 세상의 문제'를 가리킨다.'도메인 로직'이나 '비즈니스 로직'이라고 말할 때는, 그 '현실 세상의 문제'를 해결하는 코드를 의미한다.   
> 도메인에 대한 해결책이나 설루션이라고 할 수 있다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FkNRnK%2FbtsIzNkwfwo%2FAAAAAAAAAAAAAAAAAAAAAEmHz2e6hxR9loHqXgoCP6S7VZ2NUrdu_KBajoa13j1V%2Fimg.jpg%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1753973999%26allow_ip%3D%26allow_referer%3D%26signature%3DdzoXUixD4k018URZBYaA7nPpZmc%253D)... 
이번에도 말로는 잘 이해가 되지 않습니다..

우리가 어떠한 서비스를 개발할 때 목적이 있을 것입니다.

예를 들면 배민은 음식을 더욱 쉽고 빠르고 간편하게 배달받기 위해, 당근마켓은 주위에 있는 중고물품을 쉽게 판매하고 구매하기 위해 만들었을 것입니다.

**그 목적을 이루기 위한 작성한 로직을 비지니스 로직이라고 하고, 여러 도메인 로직과 상호작용해 구현됩니다.**

**위에 객체지향에서 설명한세 번째. 객체들 간의 상호작용을 통해 로직을 구성과 매우 비슷하다는 것을 알 수 있습니다.**

배민을 예로 들었을 때 음식을 더욱 쉽고 빠르고 간편하게 배달받기 위해

"장바구니에 음식을 담고 결제를 하고 주문이 완료되면 배달원을 매칭해 배달을 시작하고 완료한다."는 비지니스 로직이 될 것입니다.

```
// 장바구니에 음식을 담고
장바구니.담기(음식);

// 결제를 하고
결제(장바구니);
결제.완료();

// 주문이 완료되면
주문.생성(장바구니, 결제);
주문.완료();

// 배달원를 매칭해 배달을 시작하고 완료한다.
주문.배달원매칭(배달원);
주문.배달시작();
주문.배달완료();
```

여기서 도메인 로직을 생각해 봤을 때 주문은 당연히 결제가 정상적으로 이루어지지 않았다면 완료 처리를 해서는 안됩니다.

그리고 주문 완료 처리가 되었을 때만 배달원을 매칭 해야합니다.

```
public class 주문 {
		
    private 주문상태;
    private 장바구니;
    private 결제;
    private 배달원;
    
    void 생성(장바구니, 결제) {
        this.주문상태 = 준비;
        this.장바구니 = 장바구니;
        this.결제 = 결제;
    }
    
    void 완료() {
    	if (this.장바구니.결제금액 == this.결제.결제금액 && this.결제.상태 == 완료) {
            this.주문상태 = 완료;
        } else {
            throw new 주문 완료처리 불가();
        }
    }
    
    void 배달원매칭(배달원) {
    	if (this.주문상태 == 완료) {
            this.배달원 = 배달원;
        } else {
            throw new 배달원 매칭 불가();
        }
    }
    
}
```

이렇게 **특정 도메인에만 속한 로직들을 도메인 로직이라고 합니다.**

비지니스 로직에서는 도메인에 속해있는 세세한 사항들을 모두 구현된 것이 아닌 목적을 이루기 위한 로직만 존재하게 됩니다.

**도메인 로직과 비지니스 로직을 나누는 이유는 명확하게 관심사를 분리하기 위해서입니다.**만약에 저 도메인 로직들을 비지니스 로직에 작성한다고 생각해 보면 매우 복잡해지고 재사용이 불가할 것입니다.

각기 도메인에 대한 로직이 분리되어 있기 때문에 도메인에 대한 지식을 알기 쉽고 단위 테스트를 진행하기도 쉽습니다.

또한 비지니스 로직도 단순화되어 유지보수에도 용의 하게 됩니다.

물론 개발을 하며 이 모든 것을 지키지엔 정말 어렵습니다.

그래도 좋은 코드를 작성하기 위해선 기본적인 것들을 공부하고 이해하고 매 순간 고민하며 코드를 작성해야 합니다.

저도 100% 모두 지킬 수 없지만 한줄 한줄 작성하며 어떻게 하면 더욱 단순화하여 체크포인트를 줄일 수 있을까를 고민하며

오늘도 키보드를 두들기고 있습니다... 그럼 20000

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FdaRqQE%2FbtsIAOi7Uia%2FAAAAAAAAAAAAAAAAAAAAALquE1aWVIU9Wz_97c7iUhMTE4zZGxdmn07V9K7HP8Hn%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1753973999%26allow_ip%3D%26allow_referer%3D%26signature%3DVVvWzdfzeJW6yCuS5wrDiA4O2XU%253D)진짜 힘들다 
저는 코드를 구현할 때 할 때 단순함과 체크 포인트를 가장 중요하게 생각합니다.

체크 포인트란 신경 써야 하는 부분을 말하는데 체크 포인트를 없앨수록 단순함은 올라갈 것입니다.

그럼 어떻게 체크 포인트를 줄이고 단순함을 올릴 것이냐?

여러 가지 방법이 있겠지만 **가장 기본적인 객체 지향 프로그래밍과 도메인 로직, 비즈니스 로직을 구분 지어 코드를 작성하는 것**이라고 생각합니다.

(이제부터는 제 아주 주관적인 생각을 정리한 글입니다. 반박 시 여러분들 말씀이 다 맞습니다!)

이라고 합니다.

![](https://blog.kakaocdn.net/dna/bLB4wB/btsIzn6Uie3/AAAAAAAAAAAAAAAAAAAAAAVmW9IG4rQFiotOgksj01bGJbwvCuLToX3fsJsmqsX0/img.jpg?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1753973999&allow_ip=&allow_referer=&signature=tU%2FoW%2B5Kn6Bt1q0ttiqATV0BibA%3D)
말로는 잘 이해가 안 되시죠? 그럼 자세히 설명해 보겠습니다.

예를 들어 동물이라는 데이터가 있습니다. 동물에는 여러 가지 종류가 있겠죠.

다리가 4개인 동물, 날개가 있는 동물, 지느러미가 있는 동물

이렇게 케이스별로 3가지 인터페이스로 나누고 동물이라는 공통점을 상속받아 추상화할 수 있습니다.

```
// 동물
public interface Animal {

}

// 다리가 4개인 동물
public interface FourLeggedAnimal extends Animal {

}

// 날개가 있는 동물
public interface WingedAnimal extends Animal {

}

// 지느러미가 있는 동물
public interface FinnedAnimal extends Animal {

}
```

동물의 상태를 생각해 보면 살아있는 상태 <-> 죽은 상태를 생각해 볼 수 있습니다.

여기서 생각해야 하는 부분은 동물의 상태는 모든 동물에게 있을 수 있습니다.

다리가 4개가 있던 날개가 있던 지느러미가 있던 살아있거나 죽어있을 수 있습니다.

그럼 동물의 공통점으로 들어가니 최상위인 Animal 인터페이스에 구현해야 합니다.

```
// 동물
public interface Animal {
    boolean isLive(); // 생사 상태
}
```

행위로는 먹기, 달리기, 날기, 헤엄치기를 생각해 볼 수 있습니다.

먹기는 모든 동물이 가능하기 때문에 최상위인 Animal에 구현해야 하고

달리기는 다리가 4인 동물에, 날기는 날개가 있는 동물에, 헤엄치기는 지느러미가 있는 동물에게 구현해야 합니다.

```
// 동물
public interface Animal {
    boolean isLive(); // 생사 상태
    void eat(Animal animal); // 먹기
}

// 다리가 4개인 동물
public interface FourLeggedAnimal extends Animal {
    void run(); // 달리기
}

// 날개가 있는 동물
public interface WingedAnimal extends Animal {
    void fly(); // 날기
}

// 지느러미가 있는 동물
public interface FinnedAnimal extends Animal {
    void swim(); // 헤엄치기
}
```

자 그럼 상태와 행위를 갖도록 추상화는 끝났으니 객체를 생성해 봅시다.

이때 각 행위들을 객체에 따라 구현해 줍니다.

* 호랑이가 빠르게 달릴 수 있습니다.
* 독수리는 높게 날 수 있습니다.
* 연어는 강을 거꾸로 헤엄칠 수 있습니다.

```
// 호랑이 객체
public class Tiger implements FourLeggedAnimal {
    @Override
    boolean isLive() {
    	return this.statue == LIVE;
    }
    @Override
    void eat(Animal animal) {
        animal.status == DEATH;
        System.out.println("다른 동물 잡아먹기!!");
    }
    @Override
    void run() {
        System.out.println("빠르게 달리기!!");
    }
}

// 독수리 객체
public class Eagle implements WingedAnimal {
    @Override
    boolean isLive() {
    	return this.statue == LIVE;
    }
    @Override
    void eat(Animal animal) {
        System.out.println("다른 동물 잡아먹기!!");
    }
    @Override
    void fly() {
        System.out.println("높게 날기!!");
    }
}

// 연어 객체
public class Salmon implements FinnedAnimal {
    @Override
    boolean isLive() {
    	return this.statue == LIVE;
    }
    @Override
    void eat(Animal animal) {
        System.out.println("다른 동물 잡아먹기!!");
    }
    @Override
    void swim() {
        System.out.println("강을 거꾸로 헤엄치기!!");
    }
}

Tiger tiget = new Tiget(); // 호랑이 객체 생성
Eagle eagle = new Eagle(); // 독수리 객체 생성
Salmon salmon = new Salmon(); // 연어 객체 생성
```

이렇게 추상화하여 상태와 행위를 갖춘 객체를 생성했습니다!

이렇게 만들어진 객체들로 상호작용을 하며 로직을 구성해야 합니다.

만약 독수리가 헤엄치는 연어를 먹고 있었는데 갑자기 호랑이가 나타나 달려와 독수리가 날아서 도망가고 호랑이가 연어를 먹는 로직이 있다고 생각해 봅시다...ㅎ

코드로 작성하면 요렇게 될 것입니다.

```
// 독수리가
Eagle eagle = new Eagle();

// 헤엄치는 연어를
Salmon salmon = new Salmon();
salmon.swim();

// 먹고 있었는데
eagle.eat(salmon);

//  갑자기 호랑이가 나타나 달려와
Tiger tiget = new Tiget();
tiget.run();

// 독수리가 날아서 도망가고
eagle.fly();

// 호랑이가 연어를 먹는다
tiget.eat(salmon);

salmon.isLive(); // false ...ㅠㅠ
```

이렇게 코드를 객체지향 프로그래밍으로 작성하게 되면 굳이 주석을 달지 않아도 코드만 보고 어떤 로직인지 한눈에 파악이 되지 않나요?

![](https://blog.kakaocdn.net/dna/WJwxa/btsIBC9Q7rQ/AAAAAAAAAAAAAAAAAAAAAG8x2PqVpnxbdUxYA_IUBZUBDH0gaZHVg6WJKiJHOc0R/img.jpg?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1753973999&allow_ip=&allow_referer=&signature=RmenQyYyO5jAi8%2FLmDI5R3Cjzyc%3D)아님 말고 
주의해야 할 점이 있습니다.

위에서 예를 들었을 때 호랑이는 빠르게 달릴 수 있습니다. 하지만 치타도, 표범도 빠르게 달릴 수 있죠

**생각 없이 코드를 작성할 때 자주 실수하는 부분이 객체가 중점이 되는 것이 아닌 달리는 기능이 중점이 돼버리고 맙니다.**

```
void 달리기(FourLeggedAnimal fourLeggedAnimal) {
    if (fourLeggedAnimal == 호랑이 || fourLeggedAnimal == 치타 || fourLeggedAnimal == 표범) {
        System.out.println("빠르게 달리기!!");
    } else {
        System.out.println("느리게 달리기!!");
    }
}
```

만약 이렇게 코드를 작성했다가 빠르게 달릴 수 있는 동물이 새로 생겼다면 해당 코드도 수정이 필요할 것입니다.

여기서 제가 처음에 말했던 체크 포인트가 늘어나는 것입니다.

추상화한 객체를 중심으로 코드를 작성하게 되면 호랑이인지, 치타인지, 표범인지 알 필요가 없게 됩니다.

```
public class 호랑이 implements FourLeggedAnimal {
    @Override
    void run() {
        System.out.println("빠르게 달리기!!");
    }
}

public class 치타 implements FourLeggedAnimal {
    @Override
    void run() {
        System.out.println("빠르게 달리기!!");
    }
}

public class 표범 implements FourLeggedAnimal {
    @Override
    void run() {
        System.out.println("빠르게 달리기!!");
    }
}

public class 거북이 implements FourLeggedAnimal {
    @Override
    void run() {
        System.out.println("느리게 달리기!!");
    }
}

void 달리기(FourLeggedAnimal fourLeggedAnimal) {
    fourLeggedAnimal.run();
}
```

또한 빠르게 달리는 객체가 추가되었을 때 다른 코드들은 건드릴 필요 없이 run 메서드만 구현 해준다면 로직이 실행되는데 문제가 없습니다.

만약 빠르게 달리기를 한 메서드로 사용하고 싶다면 FourLeggedAnimal를 상속받는 FastRunFourLeggedAnimal를 추상화하여 구현도 가능합니다.

```
public interface FastRunFourLeggedAnimal extends FourLeggedAnimal {
    default void run() {
        System.out.println("빠르게 달리기!!");
    }
}

public class 호랑이 implements FastRunFourLeggedAnimal {
    ...
}

public class 치타 implements FastRunFourLeggedAnimal {
    ...
}

public class 표범 implements FastRunFourLeggedAnimal {
    ...
}

호랑이.run(); // 빠르게 달리기!!
```

**항상 객체 지향 프로그래밍에서는 객체가 중점이 되어야 한다는 생각을 하며 코드를 작성해야 합니다.**

그래 이제 객체 지향 프로그래밍이 뭔지는 알겠어..!

여러 블로그나 유튜브를 찾아보면 도메인 로직과 비지니스 로직은 다음과 같다고 합니다.

> 소프트웨어 공학에서 도메인, 비즈니스라는 말은, '소프트웨어가 풀고자 하는 현실 세상의 문제'를 가리킨다.'도메인 로직'이나 '비즈니스 로직'이라고 말할 때는, 그 '현실 세상의 문제'를 해결하는 코드를 의미한다.   
> 도메인에 대한 해결책이나 설루션이라고 할 수 있다.

...
이번에도 말로는 잘 이해가 되지 않습니다..

우리가 어떠한 서비스를 개발할 때 목적이 있을 것입니다.

예를 들면 배민은 음식을 더욱 쉽고 빠르고 간편하게 배달받기 위해, 당근마켓은 주위에 있는 중고물품을 쉽게 판매하고 구매하기 위해 만들었을 것입니다.

**그 목적을 이루기 위한 작성한 로직을 비지니스 로직이라고 하고, 여러 도메인 로직과 상호작용해 구현됩니다.**

**위에 객체지향에서 설명한세 번째. 객체들 간의 상호작용을 통해 로직을 구성과 매우 비슷하다는 것을 알 수 있습니다.**

배민을 예로 들었을 때 음식을 더욱 쉽고 빠르고 간편하게 배달받기 위해

"장바구니에 음식을 담고 결제를 하고 주문이 완료되면 배달원을 매칭해 배달을 시작하고 완료한다."는 비지니스 로직이 될 것입니다.

```
// 장바구니에 음식을 담고
장바구니.담기(음식);

// 결제를 하고
결제(장바구니);
결제.완료();

// 주문이 완료되면
주문.생성(장바구니, 결제);
주문.완료();

// 배달원를 매칭해 배달을 시작하고 완료한다.
주문.배달원매칭(배달원);
주문.배달시작();
주문.배달완료();
```

여기서 도메인 로직을 생각해 봤을 때 주문은 당연히 결제가 정상적으로 이루어지지 않았다면 완료 처리를 해서는 안됩니다.

그리고 주문 완료 처리가 되었을 때만 배달원을 매칭 해야합니다.

```
public class 주문 {
		
    private 주문상태;
    private 장바구니;
    private 결제;
    private 배달원;
    
    void 생성(장바구니, 결제) {
        this.주문상태 = 준비;
        this.장바구니 = 장바구니;
        this.결제 = 결제;
    }
    
    void 완료() {
    	if (this.장바구니.결제금액 == this.결제.결제금액 && this.결제.상태 == 완료) {
            this.주문상태 = 완료;
        } else {
            throw new 주문 완료처리 불가();
        }
    }
    
    void 배달원매칭(배달원) {
    	if (this.주문상태 == 완료) {
            this.배달원 = 배달원;
        } else {
            throw new 배달원 매칭 불가();
        }
    }
    
}
```

이렇게 **특정 도메인에만 속한 로직들을 도메인 로직이라고 합니다.**

비지니스 로직에서는 도메인에 속해있는 세세한 사항들을 모두 구현된 것이 아닌 목적을 이루기 위한 로직만 존재하게 됩니다.

**도메인 로직과 비지니스 로직을 나누는 이유는 명확하게 관심사를 분리하기 위해서입니다.**만약에 저 도메인 로직들을 비지니스 로직에 작성한다고 생각해 보면 매우 복잡해지고 재사용이 불가할 것입니다.

각기 도메인에 대한 로직이 분리되어 있기 때문에 도메인에 대한 지식을 알기 쉽고 단위 테스트를 진행하기도 쉽습니다.

또한 비지니스 로직도 단순화되어 유지보수에도 용의 하게 됩니다.

물론 개발을 하며 이 모든 것을 지키지엔 정말 어렵습니다.

그래도 좋은 코드를 작성하기 위해선 기본적인 것들을 공부하고 이해하고 매 순간 고민하며 코드를 작성해야 합니다.

저도 100% 모두 지킬 수 없지만 한줄 한줄 작성하며 어떻게 하면 더욱 단순화하여 체크포인트를 줄일 수 있을까를 고민하며

오늘도 키보드를 두들기고 있습니다... 그럼 20000

진짜 힘들다
