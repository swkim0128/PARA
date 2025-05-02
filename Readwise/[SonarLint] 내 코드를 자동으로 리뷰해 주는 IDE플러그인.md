# [SonarLint] 내 코드를 자동으로 리뷰해 주는 IDE플러그인

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FxoMpj%2FbtqBp5yrIca%2FoVGZKCkO3vGUHL5N5zOVQk%2Fimg.png)

## Metadata
- Author: [[dev.yong]]
- Full Title: [SonarLint] 내 코드를 자동으로 리뷰해 주는 IDE플러그인
- Category: #articles
- Document Tags:  #sonarlint 
- Summary: SonarLint는 IDE 플러그인으로 코드 품질 문제를 식별하고 해결하는데 도움을 줍니다. 이 툴은 코드정적 분석을 통해 위험성이 있는 코드를 감지하고 보완합니다. SonarLint를 설치하면 코드 작성 중 발생한 문제를 실시간으로 알려주어 개발 작업에 집중할 수 있습니다.

## Full Document
[[Full Document Contents/[SonarLint] 내 코드를 자동으로 리뷰해 주는 IDE플러그인.md|See full document content →]]

## Highlights
- Sonar는 다음 7가지 품질 요소를 기준으로 코드의 품질을 구분한다.
  • Code Smells(Maintainability)
  • Bugs(Reliability)
  • Vulnerabilities(Security)
  • Coverage
  • Duplications
  • Size
  • Complexity ([View Highlight](https://read.readwise.io/read/01j2t3cy8nydnqdnck834b9xj8))
- **Code Smells(Maintainability)**
  심각한 이슈는 아니지만 베스트 프렉티스에서 사소한 이슈들로 모듈성(modularity), 이해가능성(understandability), 변경가능성(changeability), 테스트용의성(testability), 재사용성(reusability) 등이 포함된다.
  • Code Smells
  • Debt
  • Debt Ratio ([View Highlight](https://read.readwise.io/read/01j2t3d1vbxngfk4sw96tdq285))
- **Bugs(Reliability)**
  일반적으로 잠재적인 버그 혹은 실행시간에 예상되는 동작을 하지 않는 코드를 나타낸다. 
  • Code Smells
  • Debt
  • Debt Ratio ([View Highlight](https://read.readwise.io/read/01j2t3d3v4bwerc710xbvb43a4))
- **Vulnerabilities(Security)**
  해커들에게 잠재적인 약점이 될 수 있는 보안상의 이슈를 말한다. SQL 인젝션, 크로스 사이트 스크립팅과 같은 보안 취약성을 찾아낸다.
  • Code Smells
  • Debt
  • Debt Ratio ([View Highlight](https://read.readwise.io/read/01j2t3d5nmf5r6mb6kg7vrqgz6))
- **Duplications**
  코드 중복은 코드의 품질을 저해시키는 가장 큰 요인 중 하나이다.
  • Density
  • Duplicated Lines
  • Duplicated Blocks
  • Duplicated Files ([View Highlight](https://read.readwise.io/read/01j2t3d83j7phf03ydsdt98m33))
- **Unit Tests**
  단위테스트 커버리지를 통해 단위 테스트의 수행 정도와 수행한 테스트의 성공/실패 정보를 제공한다.
  Unit Test Coverage
  • Line Coverage : 구문 커버리지
  • Condition Coverage ; 조건 커버리지 ([View Highlight](https://read.readwise.io/read/01j2t3dad0az0h8dtssnvnc6cd))
- **Complexity**
  순환복잡도(Cyclomatic Complexity) 측정
  • 코드의 논리적인 흐름상에 존재하는 독립적인 선형 경로의 개수를 의미
  인지복잡도(Cognitive Complexity)  측정 ([View Highlight](https://read.readwise.io/read/01j2t3de4mvkjzz74vyqyf36n0))
