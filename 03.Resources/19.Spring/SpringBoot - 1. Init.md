---
type: Spring
archive: false
---
### Spring Initializr Generate

---

[https://start.spring.io/](https://start.spring.io/) → zip file

  

### Dependency

---

> Developer Tools

- Spring Dev Tool
- Lombok

> Web

- Spring Web

> Security

- Spring Security
- OAuth2 Client / OAuth2 Resource Server

> DataBase

- IBM DB2 / MS SQL Server / MySQL / Oracle / PostgreSQL Driver
- Spring Data JPA
- H2 Database

> I/O

- Validation

  

> 참고

[https://appleg1226.tistory.com/11?category=864243](https://appleg1226.tistory.com/11?category=864243)

[https://appleg1226.tistory.com/12?category=864243](https://appleg1226.tistory.com/12?category=864243)

  

### Swagger

---

> install

```Plain
# spring boot: 2.6.7 이상
implementation 'io.springfox:springfox-swagger2:3.0.0'
implementation 'io.springfox:springfox-swagger-ui:3.0.0'

# spring boot: 2.5.7, swagger: 2.9.2
implementation 'io.springfox:springfox-swagger2:2.9.2'
implementation 'io.springfox:springfox-swagger-ui:2.9.2'
```

  

> SwaggerConfig

```Java
@Configuration
@EnableSwagger2
@RequiredArgsConstructor
public class SwaggerConfig {

    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.any())
                .paths(PathSelectors.ant("/api/**"))
                .build();
    }

    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("ssafyland")
                .version("1.0.0")
                .description("ssafyland rest api")
                .build();
    }
}
```

  

### JPA

---

> Install

```Plain
plugins {
		// querydsl
		id "com.ewerk.gradle.plugins.querydsl" version "1.0.10"
}

dependencies {
		// jpa
		implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
		
		// querydsl
		implementation "com.querydsl:querydsl-jpa:${queryDslVersion}"
		implementation "com.querydsl:querydsl-apt:${queryDslVersion}"
}
```

  

> Spring Data JPA repository Bean 설정

```YAML
spring:
	jpa:
		database-platform: org.hibernate.dialect.MariaDB103Dialect
    show-sql: true
    properties:
      hibernate:
        format_sql: true
        hbm2ddl.auto: update
        implicit_naming_strategy: org.springframework.boot.orm.jpa.hibernate.SpringImplicitNamingStrategy
        physical_naming_strategy: org.springframework.boot.orm.jpa.hibernate.SpringPhysicalNamingStrategy
```

  

### Junit Test

---

> Test Class

```Java
@ExtendWith(SpringExtension.class)
@WebMvcTest(controllers = Controller.class)
public class ControllerTest {

	@Autowired
	private MockMvc mvc;

	@Test
	public void hello_to_return() throws Exception {
			String hello = "Hello";

			mvc.perform(get("/"))
				.andExpect(status().isOk())
				.andExpect(content().string(hello));
	}
}
```