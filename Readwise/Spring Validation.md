# Spring Validation

![rw-book-cover](https://images.velog.io/velog.png)

## Metadata
- Author: [[velog.io]]
- Full Title: Spring Validation
- Category: #articles
- Document Tags:  #kotlin  #spring boot 
- Summary: Kotlin Spring Validation is important for ensuring that incoming requests contain valid data, preventing potential errors in processing. Hibernate Validator, a Jakarta Bean Validation implementation, is commonly used to validate data using annotations. Developers can enhance their validation process by defining custom annotations and messages for better error handling and internationalization.

## Full Document
[[Full Document Contents/Spring Validation.md|See full document content →]]

## Highlights
- `@Validated` 어노테이션을 Spring bean의 클래스나 메서드에 붙여주면, 파라미터나 리턴값을 검증할 수 있다. ([View Highlight](https://read.readwise.io/read/01jhspe727rwtbpc72yhde35mx))
- `@Validated`어노테이션이 붙은 Bean을 생성하면서 proxy를 만들고, 프록시가 `MethodValidationInterceptor`라는 인터셉터를 통해서 메서드가 실행될때 검증 로직을 실행한다. ([View Highlight](https://read.readwise.io/read/01jhspetdtdrg90wjkw7s9pz01))
- `MethodValidationInterceptor`에서는 검증에 실패하면 `ConstraintViolationException`을 throw한다. ([View Highlight](https://read.readwise.io/read/01jhsphz4pdfcdkzy00cq6hhhc))
