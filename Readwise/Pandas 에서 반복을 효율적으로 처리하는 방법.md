# Pandas 에서 반복을 효율적으로 처리하는 방법

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Ftistory_admin%2Fstatic%2Fimages%2FopenGraph%2Fopengraph.png)

## Metadata
- Author: [[Deepplay]]
- Full Title: Pandas 에서 반복을 효율적으로 처리하는 방법
- Category: #articles
- Document Tags:  #pandas  #python 
- Summary: Pandas 에서 반복을 효율적으로 처리하는 방법 Pandas 를 통해 데이터 프로세싱을 할 때 종종 해야할일은 행에 반복적으로 접근을 하면서 그 값을 조작하는 일이다. 예를 들어, missing value 가 0 으로 코딩이 되어있는데, 이를 다른 값으로 바꾸고 싶을 경우 또는 A 컬럼의 값이 missing 일 때, B 컬럼의 값을 수정하고 싶은 경우 등이 있다. 이러한 작업을 하기 위해서는 모든 행을 조회 하면서 값을 조회하고 수정하는 일이 필요하다. 이번 포스팅에서는 이러한 반복작업이 필요한 상황에서 어떤 방법이 가장 효율적일지에 대해 정리해보려고한다. 사용할 데이터 1) pd.iterrows() 가장 기본적이고 많이 사용하는 방법이 iterrows 함수를 이용하는 것이다. 하지만 iterrows ..

## Full Document
[[Full Document Contents/Pandas 에서 반복을 효율적으로 처리하는 방법.md|See full document content →]]

## Highlights
- 정리 
  • Default 방법으로 index 를 돌면서 set_value 와 get_value 를 호출하는 방법을 추천
  • 비교적 큰 데이터에셋에서 비교적 간단한 작업을 할 때, apply 함수가 가장 효율적 ([View Highlight](https://read.readwise.io/read/01heptx4exws99xsjh4ra5a5ts))
