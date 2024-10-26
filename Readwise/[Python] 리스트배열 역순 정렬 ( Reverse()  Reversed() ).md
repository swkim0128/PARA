# [Python] 리스트/배열 역순 정렬 ( Reverse() / Reversed() )

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FuaXgH%2FbtqRgiDaXNB%2FqUsf2S9r04hecv4q8diqO0%2Fimg.png)

## Metadata
- Author: [[개발하는 사막여우]]
- Full Title: [Python] 리스트/배열 역순 정렬 ( Reverse() / Reversed() )
- Category: #articles
- Document Tags: [[python]] 
- Summary: 👀 파이썬의 역순 정렬 ( reverse() / reversed() ) 👀 1. list.reverse() : list 자체를 역순으로 정렬, 함수 반환값 None 값 2. reversed(list) : 역순 정렬된 list 새로운 변수에 할당 가능 파이썬의 리스트의 정렬함수에 sort와 sorted가 있듯이, 역순 정렬에는 reverse와 reversed가 있습니다. 공통적으로 두 함수 모두 배열에 대한 역순정렬 기능을 제공해주고, 이 두 함수의 차이점은 sort와 sorted의 차이점과 비슷합니다. 1. reverse() → list.reverse() 메모리 내의 배열 원소들을 직접 수정. 반환값은 None -> 따라서 rev = list.sort() 실행 시 rev에는 None값 저장됨. array..
- URL: https://dev-note-97.tistory.com/14

## Highlights
- [**1. reverse() → list.reverse()**](https://dev-note-97.tistory.com/14#--%--reverse--%--%E-%--%--%--list-reverse--)
  • **메모리 내의 배열 원소들을 직접 수정**.
  • 반환값은 None -> 따라서 **rev = list.sort() 실행 시 rev에는 None값 저장**됨. ([View Highlight](https://read.readwise.io/read/01hepx8tfmw629dfeasbvb2yez))
- [**2. reversed() **→** reversed(list)**](https://dev-note-97.tistory.com/14#--%--reversed--%C-%A-%E-%--%--%C-%A-reversed-list-)
  • **반환값이 배열값: 변수에 저장 가능!** 원래 변수는 수정되지 않음. ([View Highlight](https://read.readwise.io/read/01hepxbkwz0jb2h3y48me91pnd))
