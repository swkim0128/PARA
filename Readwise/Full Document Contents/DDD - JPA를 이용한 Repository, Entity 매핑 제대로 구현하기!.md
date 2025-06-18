# DDD - JPA를 이용한 Repository, Entity 매핑 제대로 구현하기!

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FXSxrB%2FbtrEDRwqVWP%2FKaSC0TdX81OnvhgL6S02Gk%2Fimg.png)

## Metadata
- Author: [[JaeHoney]]
- Full Title: DDD - JPA를 이용한 Repository, Entity 매핑 제대로 구현하기!
- Category: #articles
- Document Tags:  #ddd 
- Summary: This post explains how to properly implement repositories and entity mapping using JPA in domain-driven development. It covers topics like value collection mapping, using embedded IDs, and managing relationships between entities and value types. The author emphasizes best practices for handling data and entity relationships in JPA.
- URL: https://jaehoney.tistory.com/228

## Full Document
해당 포스팅은 **"도메인 주도 개발 시작하기"**라는 내용을 정리한 글입니다. 해당 도서는 아래 Link에서 확인할 수 있습니다.

-<http://www.yes24.com/Product/Goods/108431347>

##### 모듈 위치

리포지터리 인터페이스는 애그리거트와 같이 도메인 영역에 속하고, 리포지터리를 구현한 클래스는 인프라스트럭처 영역에 속한다. 이는 DIP에 따라 리포지터리의 구현 체를 인프라스트럭처 영역에 위치시켜서 인프라스트럭처 영역이 도메인 영역을 의존하도록 한다.

![](https://blog.kakaocdn.net/dn/XSxrB/btrEDRwqVWP/KaSC0TdX81OnvhgL6S02Gk/img.png)
![](https://blog.kakaocdn.net/dn/HciEI/btrEuV7Ubo6/jj80fW2aQx4gceTGnMNm51/img.png)
![](https://blog.kakaocdn.net/dn/bXbSR2/btrEDQ5k1SA/cPpfzW3Tc8JMMwromIEyCk/img.png)
![](https://blog.kakaocdn.net/dn/rpEXI/btrECAPilSW/0w6V4CPR6K1KP4OH7tdeAK/img.png)
![](https://blog.kakaocdn.net/dn/cExcGM/btrEF9i5iFk/SgSjzekck5Hz1pan7kdK50/img.png)
밸류 컬렉션을 별도 테이블로 매핑할 때는 @ElementCollection과 @CollectionTable을 함께 사용한다. 관련 매핑 코드는 다음과 같다.

```
@Entity
@Table(name = "purchase_order")
public class Order {
    ...
    @ElementCollection(fetch = FetchType.EAGER)
    @CollectionTable(
        name = "order_line",
        joinColumns = @JoinColumn(name = "order_number")
    )
    @orderColumn(name = "line_idx")
    private List<OrderLine> orderLines;
    ...
}

@Embeddable
public class OrderLine {
    @Embedded
    private ProductId productId;
    
    @Column(name = "price")
    private Money price;
    
    @Column(name = "quentity")
    private int quantity;
    ...
}
```

OrderLine의 매핑을 함께 표시했는데 OrderLine에는 List의 인덱스 값을 저장하기 위한 프로퍼티가 존재하지 않는다. List 타입 자체가 인덱스를 갖고 있기 때문이다. JPA는 @OrderColumn을 이용해서 지정한 칼럼에 리스트의 인덱스 값을 저장한다.

@CollectionTable은 밸류를 저장할 테이블을 지정한다. name 속성에는 테이블 이름, joinColumns 속성에는 외부키로 사용할 칼럼을 지정한다.

##### 밸류를 이용한 ID 매핑

식별자라는 의미를 부각시키기 위해 식별자 자체를 밸류 타입으로 만들 수 있다. 밸류 타입을 식별자로 매핑하면 @Id 대신 @EmbeddedId 애노테이션을 사용한다.

```
@Entity
@Table(name = "purchase_order")
public class Order {
    @EmbeddedId
    private OrderNo number;
    ...
}

@Embeddable
public class OrderNo implements Serializable {
    @Column(name = "order_number")
    private String number;
    ...
}
```

JPA에서 식별자 타입은 Serializable 타입이어야 하므로 식별자로 사용할 밸류 타입은 Serializable 인터페이스를 상속받는다.

밸류 타입으로 식별자를 구현할 때 얻을 수 있는 이점은 식별자에 기능을 추가할 수 있다는 점이다. 예를 들어, 주문 번호가 무언가 의미를 가진다면 해당 주문 번호를 사용한 동작을 밸류 타입 식별자에서 구현할 수 있다.

```
if (order.getNumber().is2ndGeneration()) {
    ...
}
```

##### 별도 테이블에 저장되는 밸류 매핑

게시글 데이터를 Article 테이블과 Article\_Content 테이블로 나눠서 저장한다고 가정하자. 두 엔터티는 1-1 연관으로 매핑할 수 있다.

Article\_Content는 별도의 엔터티로 생각할 수 있지만 Article의 내용을 담고 있는 밸류로 생각하는 것이 맞다. Article\_Content의 ID는 식별자이긴 하지만 Article 테이블의 데이터와 연결하기 위함이지 별도 식별자가 필요하지 않다.

이때는 밸류를 테이블과 매핑하기 위해 @SecondaryTable과 @AttributeOrverrides를 사용한다.

```
@Entity
@Table(name = "article")
@SecondaryTable(
    name = "article_content",
    pkJoinColumns = @PrimaryKeyJoinColumn(name = "id")
)
public class Article {
    @Id
    private Long id;
    ...
    @AttributeOverrides({
        @AttributeOverride(name = "content", column = @Column(table = "article_content")),
        @AttributeOverride(name = "contentType", column = @Column(table = "article_content"))
    })
    @Embedded
    private ArticleContent content;
    ...
}
```

결과적으로 Article을 조회할 때 ArticleContent도 함께 조회하게 된다. 만약 이런 결과를 원하지 않는다면 조인을 지연 로딩 방식으로 설정할 수 있다. 하지만 밸류를 엔터티로 만드는 것이므로 좋은 방법이 아니다.

이때는 조회 전용 쿼리를 따로 구현하는 것이 좋다.

##### 밸류 커넥션을 Entity로 매핑하기

개념적으로 밸류인데 구현 기술의 한계나 팀 표준 때문에 @Entity를 사용해야 할 때도 있다.

JPA는 @Embeddable 타입의 클래스 상속 매핑을 지원하지 않는다. 대신 @Entity를 이용한 상속 매핑으로 처리해야 한다. 엔티티로 관리되므로 식별자 필드가 필요하고 타입 식별(discriminator) 칼럼을 추가해야 한다.

예를 들어 제품의 업로드 방식에 따라 이미지 경로나 섬네일 제공 여부가 달라진다고 생각해보자. Image를 InternalImage와 ExternalImage 두 가지로 나눌 수 있다.

이때는 Image 클래스에 다음 설정을 사용한다.

* abstract class 사용
* @Inheritance 애노테이션 적용
* strategy 값으로 SINGLE\_TABLE 사용
* @DiscriminatorColumn 애노테이션을 이용하여 타입 구분용으로 사용할 칼럼 지정

```
@Entity
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name = "image_type")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Table(name = "image")
public abstract class Image {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "image_id")
    private Long id;

    @Column(name = "image_path")
    private String path;
    
    @Temporal(TemporalType.TIMESTAMP)
    @Column(name = "upload_time")
    private Date uploadTime;

    public Image(String path) {
    		this.path = path;
    		this.uploadTime = new Date();
    }

    protected String getPath() {
    	return path;
    }
    public Date getUploadTime(){
    	return uploadTime;
    }

    public abstract String getURL();
    public abstract boolean hasThumbnail();
    public abstract String getThumbnailURL();
}
```

이때 밸류인 Image를 @Entity로 매핑했으므로 상태 변경 메서드는 제공하지 않는다.

```
@Entity
@DiscriminatorValue("II")
public class InternalImage extends Image {
	...
}

@Entity
@DiscriminatorValue("EI")
public class ExternalImage extends Image {
	...
}
```

Image를 상속받은 클래스는 @Discriminator를 사용해서 매핑을 설정한다.

```
@Entity
@Table(name = "product")
public class Product {
    @EmbeddedId
    private ProductId id;
    
    ...

    @OneToMany(cascade = {CascadeType.PERSIST, CascadeType.REMOVE},
            orphanRemoval = true, fetch = FetchType.EAGER)
    @JoinColumn(name = "product_id")
    @OrderColumn(name = "list_idx")
    private List<Image> images = new ArrayList<>();
    
    ...

    public void changeImages(List<Image> newImages) {
        images.clear();
        images.addAll(newImages);
    }

    ...
}
```

Image가 @Entity이므로 목록을 담고 있는 Product는 @OneToMany를 사용해서 매핑을 처리한다.

Image는 밸류이므로 독자적인 라이프 사이클을 가지지 않고 Product에 완전히 의존한다. 따라서 Product를 저장할 때 함께 저장되고 삭제할 떄도 함께 삭제되도록 cascade 속성을 지정한다. 리스트에서 Image 객체를 제거하면 DB에서 함께 삭제되도록 orhanRemoval도 true로 설정한다.

##### Reference

* <https://incheol-jung.gitbook.io/docs/study/ddd-start/4-jpa>
* <http://www.yes24.com/Product/Goods/108431347>
