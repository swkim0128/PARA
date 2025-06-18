# DDD - 트랜잭션과 잠금을 관리하는 다양한 방법!

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbSZsx8%2FbtrHfR1nqBa%2F0qRYCPksfDlKQxbGdgSdM0%2Fimg.png)

## Metadata
- Author: [[TISTORY]]
- Full Title: DDD - 트랜잭션과 잠금을 관리하는 다양한 방법!
- Category: #articles
- Document Tags:  #ddd 
- Summary: The text discusses managing transactions and locks in domain-driven development, specifically focusing on how to handle changes to order aggregates by both operators and customers. It explains the challenges of maintaining consistency when multiple users modify the same order, and suggests using both preemptive and non-preemptive locks to prevent conflicts. Additionally, it highlights the importance of version control in ensuring that updates are only made when the data is current.
- URL: https://jaehoney.tistory.com/251

## Full Document
해당 포스팅은 **"도메인 주도 개발 시작하기"**라는 내용을 정리한 글입니다. 해당 도서는 아래 Link에서 확인할 수 있습니다.

-<http://www.yes24.com/Product/Goods/108431347>

##### 애그리거트와 트랜잭션

주문 애그리거트에 대해 운영자가 배송 준비 상태로 변경할 때 사용자는 배송지 주소를 변경하면 어떻게 될까?

다음 그림은 운영자와 고객이 동시에 한 주문 애그리거트를 수정하는 과정이다.

![](https://blog.kakaocdn.net/dn/bSZsx8/btrHfR1nqBa/0qRYCPksfDlKQxbGdgSdM0/img.png)
리포지토리는 트랜잭션마다 새로운 애그리거트 객체를 생성한다. 운영자 스레드와 고객 스레드에서는 개념적으로 동일하지만 물리적으로 서로 다른 애그리거트를 사용한다.

즉, 각 애그리거트는 서로의 객체에 영향을 주지 않는다. 고객 스레드 입장에서는 주문 애그리거트가 아직 배송 상태가 아니므로 배송지를 변경할 수 있게 된다. 이는 애그리거트의 일관성이 깨지는 것이다.

해당 문제를 해결하려면 아래 두 가지 방법이 있다.

* 운영자가 배송지 정보를 변경하고 커밋하는 동안 고객이 애그리거트를 수정하지 못하게 막는다.
* 운영자가 배송지 정보를 조회한 이후 고객이 정보를 변경하면 운영자가 애그리거트를 다시 조회한 후 수정하도록 한다.

위 두 가지 방법은 선점(Pessimistic) 잠금과 비선점(Optimistic) 잠금이라 부른다.

##### 선점 잠금

선점 잠금(Pessimistic Lock)은 먼저 애그리거트를 구한 스레드가 애그리거트 사용이 끝날 때까지 다른 스레드가 애그리거트를 수정하지 못하게 막는 방식이다.

![](https://blog.kakaocdn.net/dn/bGnEAS/btrHj0qQA64/JoVqkhRzFeUtRRoPMKyQB0/img.png)
선점 잠금은 DBMS가 제공하는 행단위 잠금을 사용해서 구현한다. 일반적으로 FOR UPDATE 문을 사용해서 특정 레코드에 한 커넥션만 접근할 수 있도록 처리한다.

선점 잠금 기능을 사용할 때는 교착 상태(dead lock)를 조심해야 한다. 예를 들어 스레드 A와 스레드 B가 서로 사용 중인 자원을 필요로 하는 경우이다. QueryHint를 사용해서 잠금 최대 대기 시간을 지정하는 것이 좋다.

```
public interface MemberRepository extends Repository<Member, MemberId> {
    
    @Lock(LockModeType.PESSIMISTIC_WRITE)
    @QueryHints({
        @QueryHint(name = "javax.persistence.lock.timeout", value = "2000")
    })
    @Query("select m from Member m where m.id = :id")
    Optional<Member> findByIdForUpdate(@Param("id") MemberId memberId);
    
}
```

해당 코드는 지정한 시간 이내 잠금을 구하지 못하면 익셉션을 발생시킨다.

##### 비 선점 잠금

선점 잠금으로 모든 트랜잭션 문제를 해결할 수는 없다. 아래의 예시를 보자.

![](https://blog.kakaocdn.net/dn/bTa1Jp/btrHj32xLBb/VLnQ3xYb36YDdRX1nbrmV1/img.png)
그림의 실행 순서를 요약하면 다음과 같다.

1. 운영자는 배송을 위해 주문 정보를 조회한다. 시스템은 정보를 제공한다.
2. 고객이 배송지 변경을 위해 변경 폼을 요청한다. 시스템은 변경 폼을 제공한다.
3. 고객이 새로운 배송지를 입력하고 폼을 전송해서 배송지를 변경한다.
4. 운영자가 1번에서 조회한 주문 정보를 기준으로 배송지를 정하고 배송 상태 변경을 요청한다.

문제는 운영자는 고객이 변경하기 전의 배송지 정보를 이용해서 배송 준비를 한 뒤에 배송 상태로 변경하게 된다. 즉, 배송 상태 변경 전에 배송지를 한 번 더 확인하지 않으면 운영자는 다른 배송지로 물건을 발송하게 된다.

이 문제는 서로 변경하려는 자원이 다르므로 선점 잠금 방식으로는 해결할 수 없다. 그래서 비선점 잠금을 사용한다. 비선점 잠금은 변경한 데이터를 실제 DBMS에 반영하는 시점에 변경 가능 여부를 확인하는 방법이다.

비선점 잠금을 구현하려면 애그리거트에 버전으로 사용할 숫자 타입 프로퍼티를 추가해야 한다. 애그리거트를 수정할 때마다 다음과 같은 쿼리를 사용한다.

```
UPDATE aggtable SET version = version + 1, colx = ?, coly = ?
WHERE aggid = ? and version = 현재 버젼
```

결과적으로 수정할 애그리거트의 버전이 현재 애그리거트의 버전과 동일한 경우에만 데이터를 수정하게 된다.

![](https://blog.kakaocdn.net/dn/plUhm/btrHjzgjdG2/Fg189oJK33909t6WuQGKek/img.png)
JPA는 버전을 이용한 비선점 잠금을 지원한다. @Version 애노테이션을 붙이고 버전을 저장할 칼럼을 추가하기만 하면 된다.

```
@Entity
@Table(name = "purchage_order")
public class Order {
    @EmbeddedId
    private OrderNo number;

    @Version
    private long version;
    
    ...
}
```

응용 서비스에서는 Version에 대해 알 필요가 없다. 기능 실행 과정에서 애그리거트 데이터가 변경되면 JPA는 트랜잭션 종료 시점에 비선점 잠금을 위한 쿼리를 실행한다.

쿼리가 실패하면 OptimisticLockFailureException이 발생한다. 표현 영역에서 해당 익셉션 처리를 구현할 수 있다.

```
@Controller
public class OrderController {
    ...
    @RequestMapping(value = "/changeShipping", method = RequestMethod.POST)
    public String changeShipping(ChangeShippingRequest changeReq) {
        try {
            changeShippingService.changeShipping(changeReq);
        } catch(OptimisticLockingFailureException ex) {
            // 누군가 먼저 같은 주문 애그리거트를 수정했으므로, 
            // 트랜잭션 충돌이 일어났다는 메시지를 보여준다. 
            ...
        }
}
```

###### 강제 버전 증가

JPA의 애그리거트는 루트 엔터티뿐만 아니라 다른 엔터티도 포함하고 있다. 문제는 루트가 아닌 다른 엔터티가 변경되면 버전이 갱신되지 않는다는 점이다. 애그리거트에 속한 엔터티가 변경 되었는데 애그리거트의 버전이 갱신되지 않는다는 점은 논리상 적절하지 않다.

JPA에서 이런 문제를 처리하려면 LockModeType.OPTIMISTIC\_FORCE\_INCREMENT를 사용해서 버전을 강제로 올려주면 된다.

```
public interface MemberRepository extends Repository<Member, MemberId> {
    
    @Lock(LockModeType.OPTIMISTTIC_FORCE_INCREMENT)
    @Query("select m from Member m where m.id = :id")
    Optional<Member> findByIdOptimisticLockMode(@Param("id") MemberId memberId);
    
}
```

##### 오프라인 선점 잠금

컨플루언스(Confluence)는 문서를 편집할 때 누군가 먼저 편집을 하는 중이면 다른 사용자가 문서를 수정하고 있다는 안내 문구를 보여준다.

만약 엄격하게 동시에 수정하는 것을 막고 싶었다면 누군가 수정 화면을 보고 있으면 수정 자체를 실행하지 못하게 해야 한다. 이때 필요한 것이 오프라인 선점 잠금(Offline Pessimistic Lock) 방식이다.

![](https://blog.kakaocdn.net/dn/B76DX/btrHly1Or6v/kSvTlW3arjWEdFryHrCwu1/img.png)
해당 방식은 변경 완료 시점에서 동시 변경을 막는 것이 아니라 여러 트랜잭션에 걸쳐 동시 변경을 막는다.

해당 기능을 사용하기 위해서는 잠금을 관리할 테이블이 필요하다.

```
create table locks (
    type varchar(255), 
    id varchar(255),
    lockid varchar(255),
    expiration_time datetime,
    primary key (type, id) 
) character set utf8;

create unique index locks_idx ON locks (lockid);
```

이제 해당 테이블에 잠금을 추가함으로 애그리거트를 잠그는 방식으로 구현하면 된다. 예를 들어 Order 루트 엔터티를 잠그려면 아래와 같은 쿼리를 실행하면 된다.

해당 방식은 Application Layer에서 구현해야 한다. 사용을 위해 아래의 4가지 기능을 제공해야 한다.

* 잠금 선점 시도 (try lock)
* 잠금 확인 (check lock)
* 잠금 해제 (release lock)
* 락 유효시간 연장 (extend lock expiration)

이는 LockManager라는 인터페이스가 수행할 수 있다.

```
public interface LockManager {
    LockId tryLock(String type, String id) throws LockException;
    void checkLock(LockId lockId) throws LockException;
    void releaseLock(LockId lockId) throws LockException;
    void extendLockExpiration(LockId lockId, long inc) throws LockException;
}
```

이후 LockData 엔터티를 만든다.

```
public class LockData {
    private String type;
    private String id;
    private String lockid;
    private long expirationTime;
   
    public LockData(String type, String id, String lockId, long expirationTime) {
        this.type = type;
        this.id = id;
        this.lockId = lockId;
        this.expirationTime= expirationTime;
    }

    public String getType() {
        return type;
    }

    public String getId() {
        return id;
    }

    public String getLockId() {
        return lockId;
    }

    public long getExpirationTime() {
        return expirationTime;
    }

    // 유효 시간이 지났는지 확인
    public boolean isExpired() {
        return expirationTime < System.currentTimeMillis();
    }
}
```

LockManager의 구현체를 JdbcTemplate을 이용하면 아래와 같이 구현할 수 있다.

```
@Component
public class SpringLockManager implements LockManager {
    private int lockTimeout = 5 * 60 * 1000;
    private DdbcTemplate jdbcTemplate;
    private RowMapper<LockData> lockDataRowMapper = (rs3 rowNum) ->
        new LockData(rs.getString(1), rs.getString(2),
                     rs.getString(3), rs.getTimestamp(4).getTime());
    @Transactional
    @Override
    public LockId tryLock(String type, String id) throws LockException {
        checkAlreadyLocked(type, id);
        LockId lockId = new LockId(UUID.randomUUID().toString());
        locking(type, id, lockId);
        return lockId;
    }

    private void checkAlreadyLocked(String type, String id) {
        List<LockData> locks = jdbcTemplate.query(
            "select * from locks where type = ? and id = ?",
            lockDataRowMapper, type, id);
        Optional<LockData> lockData = handleExpiration(locks);
        if (lockData.isPresent()) throw new AlreadyLockedException();
    }

    private Optional<LockData> handleExpiration(List<LockData> locks) {
        if (locks.isEmptyO) return Optional.empty();
        LockData lockData = locks.get(0);
        if (lockData.isExpired()) {
            jdbcTemplate.update(
                "delete from locks where type = ? and id = ?",
                lockData.getType(), lockData.getId());
            return Optional.empty();
        } else {
            return Optional.of(lockData);
        }
    }

    private void locking(String type. String id, LockId lockId) {
        try {
            int updatedCount = jdbcTemplate.update(
                "insert into locks values (?,?,?,?)",
                type, id, lockId.getValue(), new Timestamp(getExpirationTime()));
            if (updatedCount == 0) throw new LockingFailException();
        } catch (DuplicateKeyException e) {
            throw new LockingFailException(e);
        }
    }

    private long getExpirationTime() {
        return System.currentTimeMillis() + lockTimeout;
    }

    @Override
    public void checkLock(Lockid lockid) throws LockException {
        Optional<LockData> lockData = getLockData(lockid);
        if (!lockData.isPresent()) throw new NoLockException();
    }

    private Optional<LockData> getLockData(Lockid lockid) {
        List<LockData> locks = jdbcTemplate.query(
            "select * from locks where lockid = ?",
            lockDataRowMapper, lockid.getValue());
        return handleExpiration(locks);
    }

    @Transactional
    @Override
    public void extendLockExpiration(Lockid lockId, long inc) throws LockException {
        Optional<LockData> lockDataOpt = getLockData(lockid);
        LockData lockData =
            lockDataOpt.orElseThrow(() -> new NoLockException());
        jdbcTemplate.update(
            "update locks set expiration_time = ? where type = ? AND id = ?",
            new Timestamp(lockData.getTimestamp() + inc),
            lockData.getType(), lockData.getId());
    }

    @Transactional
    @Override
    public void releaseLock(LockId lockId) throws LockException {
        jdbcTemplate.update("delete from locks where lockid = ?", lockId.getValue());
    }

    @Autowired
    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }
}
```

해당 LockManager를 통해 원하는 지점에 잠금을 수행, 확인, 해제 등을 구현할 수 있다.

##### Reference

* <https://incheol-jung.gitbook.io/docs/study/ddd-start/8>
* <https://github-wiki-see.page/m/DDD-START/ONLINE-STUDY/wiki/CHAP08>

###### '[Programming](https://jaehoney.tistory.com/category/Programming) > [DDD](https://jaehoney.tistory.com/category/Programming/DDD)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [DDD - 이벤트란 무엇인가 ?! (+ 마이크로 서비스 간 트랜잭션 처리)](https://jaehoney.tistory.com/254) (0) | 2022.08.03 |
| [DDD - 바운디드 컨텍스트란 무엇인가 ?!](https://jaehoney.tistory.com/252) (0) | 2022.07.25 |
| [DDD - 도메인 서비스란 무엇인가 ?! (+ 다수의 애그리거트를 참조하는 방법)](https://jaehoney.tistory.com/248) (0) | 2022.07.14 |
| [DDD - 표현 영역과 응용 서비스! (+ 값 검증, 권한 검사, ...)](https://jaehoney.tistory.com/247) (6) | 2022.07.13 |
| [DDD - 응용 서비스 제대로 구현하기!](https://jaehoney.tistory.com/231) (0) | 2022.06.23 |
