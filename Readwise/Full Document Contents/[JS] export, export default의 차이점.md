# [JS] export, export default의 차이점

![rw-book-cover](https://velog.velcdn.com/images/mywonhyuni/post/4b60f61e-8a99-402e-8f3a-8ea22cc17549/image.png)

## Metadata
- Author: [[velog.io]]
- Full Title: [JS] export, export default의 차이점
- Category: #articles
- Document Tags:  #javascript 
- Summary: In JavaScript, `export` is used to export multiple items from a module, while `export default` is used to export a single item. To import multiple exported items, you need to use curly braces, but you can import a default export without them. This distinction helps organize code and clarify when a module contains one or multiple entities.
- URL: https://velog.io/@mywonhyuni/JS-export-export-default%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90

## Full Document
### 0. 개요

자바스크립트를 사용하다보면 라이브러리나 내가 만든 모듈을 만들고 가져올 때 **import/export** 를 자주 사용한다.  

그런데 무의식적으로 **export, export default** 를 번갈아 가며 사용할 때가 있다.  

이 전까진 단순히 **export default**는 **중괄호 {}** 없이 사용 가능하고 **export** 는 중괄호가 있어야 된다 정도만 알고 있었는데, 이번 기회에 어떤 경우에 어떻게 써야하는지 정확하게 알아보자.

들어가기 앞서 모듈은 크게 **두 종류**로 나뉜다.

1. 하나의 파일에 **복수의 함수가 있는 라이브러리 형태의 모듈**
2. 하나의 파일에 **하나의 개체 하나만 선언되어 있는 모듈**

요약하자면, 1번은 **export**, 2번은 **export default** 경우에 해당한다.

---

### 1. export

기본적으로 변수, 함수, 객체, 클래스 등을 내보낼 때 `export` 를 사용한다.

```

export let months = {
  일월: 'Jan',
  이월: 'Feb',
  삼월: 'Mar',
  사월: 'Apr',
  오월: 'May',
  육월: 'Jun',
  칠월: 'Jul'
}
```

반대로 무언가를 가져오고 싶다면 `import` 를 사용한다.

```
import {months} from './months.js'
console.log(months.일월) 
```

만약에, **하나의 파일에 `export` 된 여러 개의 요소들을 가져오려면 어떻게 해야할까?**

```

export function sayHi() { ... }
export function sayBye() { ... }
export function becomeSilent() { ... }
...
```

```
import {sayHi, sayBye, becomeSilent, ...} from './say.js';
```

이렇게 무수히 코드가 길어지는 것을 방지하기 위해 `as` 문법을 지원한다.

```
import \* as say from './say.js';

const hi = say.sayHi;
const bye = say.sayBye;
...
```

또는 직관적으로 코드를 이해하기 위해 이름 변경이 필요한 경우 개별로 import 또는 export에서 이름을 변환하여 사용할 수 있다.

```

export {sayHi as hi, sayBye as bye};

import \* as say from './say.js';
const hi = say.hi;
const bye = say.bye;
```

```

import {sayHi as hi, sayBye as bye} from './say.js';

const hi = say.hi;
const bye = say.bye;
```

---

### 2. export default

개요에서 설명했듯이 **export default** 는 하나의 파일에 개체 하나만 선언되어있는 모듈을 내보낼 때 많이 사용한다.

하지만, 이렇게 하나의 파일에 하나만 내보내다 보니 자연스레 **파일의 개수가 많아질 수 밖에 없다.**  

이건 단점이 아니다. 폴더 구조를 잘 짜고 탐색 기능을 활용하면 크게 문제는 되지 않는다.  

오히려 **'해당 모듈엔 개체가 하나만 있다'** 는 사실을 명확하게 나타내기 위해 사용한다.

```
const say = () => {...}

export default say
```

```
import say from './say.js';

```

다음과 같은 특징이 있다.

1. **'중괄호{} 가 없다.'**
2. **내보낸 모듈명을 `as` 문법없이 원하는 명칭으로 바꿔서 사용할 수 있다.**

2번은 상기 **export** 에서 `as` 를 사용하는 이유에 대해서 설명했던 것과 동일하게 좀 더 직관적인 이름을 사용하고 싶을 때 보통 바꿔서 import 하기도 한다.

```

export default say

import say from 'say.js';
import kwon from 'say.js';
```
