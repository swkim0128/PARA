# [Pandas] 5. 데이터 세기

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkCD2V%2Fbtq7snPa78r%2Ft3iyOZuxC8vl5FKnKPS7C1%2Fimg.png)

## Metadata
- Author: [[빅데희터]]
- Full Title: [Pandas] 5. 데이터 세기
- Category: #articles
- Summary: 01. 데이터 개수 세기 : count( ) 위의 데이터 프레임(df1)에서 각 columns별로 몇 개의 데이터가 들어있는지 확인하는 방법에 대해 알아보자. 〰️ 데이터 프레임에 count( )적용하기 df1.count() 위의 코드처럼 전체 데이터 프레임 df1에 .count( ) 를 적용하면 각 columns에 몇 개의 데이터가 있는지 알 수 있다. 이때 NaN값은 세지 않는다. 〰️ 특정 columns(series 형태)에 count( ) 적용하기 df1['Pclass'].count() count( )는 데이터 프레임뿐만 아니라, 시리즈(series) 형태인 경우에도 적용할 수 있다. 따라서 위의 코드처럼 특정 columns를 추출한 뒤, count( )를 적용하면 해당 column에 몇 개의 데..

## Full Document
[[Full Document Contents/[Pandas] 5. 데이터 세기.md|See full document content →]]

## Highlights
- **01. 데이터 개수 세기 : count( )**
  위의 데이터 프레임(df1)에서 각 columns별로 몇 개의 데이터가 들어있는지 확인하는 방법 ([View Highlight](https://read.readwise.io/read/01hf86fswh7x7fse9ag8yc42q3))
- df1.count() ([View Highlight](https://read.readwise.io/read/01hf866sw4ymz8ap7g6s9frrn3))
    - Note: dataFrame count 함수
- **특정 columns(series 형태)에 count( ) 적용하기**
  df1['Pclass'].count() ([View Highlight](https://read.readwise.io/read/01hf86g9s7yza9esjhsyka2q7e))
- **참고 : count( )와 size의 차이는?**
  . count( )와. size 모두 데이터 개수를 세어준다는 점이 같다. 하지만 약간의 차이점이 있는데 **count( )는 NaN값은 제외한 나머지 데이터들의 개수를 세어준다.** 반면 **size는 NaN도 포함하여 모든 데이터의 갯수를 세어준다**는 차이가 있다. (또한, size를 적용할 때는 뒤에 괄호( )를 붙이지 않는다.) ([View Highlight](https://read.readwise.io/read/01hf86gw7bhx7pmbd2cetmq2g8))
