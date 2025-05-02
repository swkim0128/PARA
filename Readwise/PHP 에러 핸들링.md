# PHP 에러 핸들링

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmXLOH%2FbtshjeHrX65%2Fd2Q4YS3COD3EXYs5127IP0%2Fimg.png)

## Metadata
- Author: [[내 머리는 램인가봐]]
- Full Title: PHP 에러 핸들링
- Category: #articles
- Document Tags:  #php 
- Summary: PHP 에러 핸들링 PHP에는 error, fatal error, exception이 있다. 이름이 비슷한 error와 fatal error의 차이는 스크립트를 당장 중단하냐 마냐의 것이다. exception은 비교적 나중에 나온 것으로 다른 언어랑 비슷하게 예외를 던져서 try-catch로 핸들링할 수 있는 매커니즘이다. PHP는 버전이 올라감에 따라 error, fatal error의 상당 부분을 exception으로 다룰 수 있게 되었다. PHP의 에러 핸들링 방침은 exception으로 보인다. Error 다음은 PHP의 에러를 다루는 함수이다. set_error_handler('에러핸들러함수이름', E_ALL); trigger_error(msg, err_level); set_error_handl..

## Full Document
[[Full Document Contents/PHP 에러 핸들링.md|See full document content →]]

## Highlights
- set_error_handler 함수로 에러를 처리할 핸들러를 등록한다. ([View Highlight](https://read.readwise.io/read/01hckkt3cw2rdxab0s29pz6znb))
- trigger_error로 에러를 인위적으로 발생시킨다. ([View Highlight](https://read.readwise.io/read/01hckkt8qx25s5yapxscg2bh44))
- 이 에러는 set_error_handler로 등록한 사용자 정의 에러 핸들러에서 다룰 수 없다. ([View Highlight](https://read.readwise.io/read/01hckky4xqdckp174g9bme6qgz))
- E_ERROR, E_PARSE, E_CORE_ERROR, E_CORE_WARNING, E_COMPILE_ERROR, E_COMPILE_WARNING ([View Highlight](https://read.readwise.io/read/01hckky9m8kphgzhkj81cr8z98))
    - Note: set_error_handler로 등록한 사용자 정의 에러 핸들러에서 다룰 수 없는 에러들
- exception은 비교적 나중에 나온 것으로 다른 언어랑 비슷하게 예외를 던져서 try-catch로 핸들링할 수 있는 매커니즘이다. ([View Highlight](https://read.readwise.io/read/01hc1yy0h3fv9hzk87fvm4b8pf))
- error나 exception이 발생하면 사용자가 에러 리커버리를 시도할 수 있다. 이러한 시도를 권장하지 않을 수도 있겠지만, 시스템적으로 가능하다. fatal error는 이것이 불가능하고 그렇게 동작하지도 않는다. 이 에러가 발생했을 때, 핸들러를 등록하는 방법은 register_shutdown_function으로 등록하는 것 ([View Highlight](https://read.readwise.io/read/01hckkzxhxhkzykgv11gk81mfy))
- Fatal error는 스크립트가 바로 중단되는 에러 ([View Highlight](https://read.readwise.io/read/01hc1yyncy4catw1fa1yxrkeze))
