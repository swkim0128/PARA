# 자바 - List - ArrayList 뽀개기 - 2

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbHTxS4%2FbtsGBvFjhRX%2FauecVfUcOLPkgLnjvi8OFK%2Fimg.jpg)

## Metadata
- Author: [[신재은👩🏼‍💻]]
- Full Title: 자바 - List - ArrayList 뽀개기 - 2
- Category: #articles
- Document Tags:  #javascript 
- Summary: 이 글에서는 자바의 ArrayList를 사용하는 방법을 설명합니다. 초기화, 요소 추가, 수정, 삭제, 순회, 정렬, 변환 등 다양한 기능을 다룹니다. 특히, `toArray(new Integer[0])` 방식이 유용하다는 점을 강조합니다.

## Full Document
[[Full Document Contents/자바 - List - ArrayList 뽀개기 - 2.md|See full document content →]]

## Highlights
- • **유연성**: ArrayList의 크기를 사전에 알지 못하는 상황에서도 이 메서드를 안전하게 사용할 수 있다. 제공된 배열이 리스트의 크기보다 작으면, ArrayList는 내부적으로 새로운 배열을 생성하고, 정확한 크기의 새 배열을 반환한다.
  • **성능 최적화**: Java API 설계자들은 toArray(new Object[0]) (이 경우에는 new Integer[0])이 new Object[list.size()]보다 성능이 좋거나 최소한 같다는 것을 발견했다. 이는 JVM의 최적화 덕분으로, 작은 배열을 인자로 사용했을 때 더 빠르게 동작할 수 있다.
  • **간결성**: 이 방식은 코드를 간단하게 유지하면서도 타입 안정성을 보장한다. new Integer[0]은 명시적으로 Integer 타입의 배열임을 보여주며, 반환되는 배열도 Integer[] 타입이 된다. ([View Highlight](https://read.readwise.io/read/01jhf7d4zj1arxftm81bf20r15))
    - Note: list.toArray(new Integer[0])
