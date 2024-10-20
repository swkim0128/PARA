---
type: Database
archive: false
---
## SQL - alter

---

- column 추가
    
    ```SQL
    alter table table_name
    add column col1 int not null auto_increment first,
    add primary key(col1);
    
    -- 필드명 col1은 필드명 col2 다음에 새로 생깁니다.
    alter table table_name
    add column col1 varchar
    after col2;
    ```
    
    first, second, third, fourth, ..., last (mysql에서는 지원되지 않습니다.)
    

  

- 테이블 이름 변경 방법
    
    ```SQL
    alter table table_name1
    rename to table_name2;
    ```
    
      
    
- 열 이름 변경 방법
    
    ```SQL
    alter table table_name
    change column col1 col2 varchar(80)
    ...
    change column col3 col4 varchar(20);
    ```
    
    기존의 컬럼1을 컬럼2로 변경합니다.
    
    무자열을 숫자형 타입으로 변경하거나 길이를 80을 길이 20으로 변경하면 데이터의 일부분을 손실할 수 있습니다.
    
      
    
    ```SQL
    alter table table_name
    modify column col1 varchar(20);
    ```
    
    테이블의 컬럼 이름은 변경하지 않고 타입과 길이만 변경합니다.
    
      
    
- 열 삭제 방법
    
    ```SQL
    alter table table_name
    drop column col1;
    ```
    
      
    
- 기본 키 삭제 방법
    
    ```SQL
    alter table table_name
    drop primary key;
    -- auto_increment로 설정된 경우 오류가 발생합니다.
    
    alter table table_name
    modify column col1 int;
    
    alter table table_name
    drop primary key;
    --  2단계 명령어로 자동 증가를 취소 후 기본키를 삭제합니다.
    ```
    
      
    
- 기본 키 추가 방법
    
    ```SQL
    alter table table_name
    change column col1 col2 int not null auto_increment,
    add primary key(col1);
    
    -- 또는
    alter table table_name
    modify column col1 int not null auto_increment,
    add primary key(col1);
    ```
    

  

출처:

[https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=50after&logNo=220929419535](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=50after&logNo=220929419535)

  

## index

---

인덱스란 추가적인 쓰기 작업과 저장 공간을 활용하여 데이터베이스 테이블의 검색 속도를 향상시키기 위한 자료구조이다.

데이터베이스에서 테이블의 모든 데이터를 검색하면 시간이 오래 걸리기 때문에 데이터와 데이터의 위치를 포함한자료구조를 생성하여 빠르게 조회할 수 있도록 돕고 있다.

  

**B-Tree 인덱스 구조**

- 인덱스 탐색은 Root → branch → leaf → 디스크 저장소 순으로 진행됩니다.
- 인덱스의 두 번째 컬럼은 첫 번째 컬럼에 의존해서 정렬되어 있습니다.
- 디스크에서 읽는 것은 메모리에서 읽는 것 보다 성능이 훨씬 떨어집니다.
- 인덱스 갯수는 3~4개 정도가 적당합니다.

  

### index의 관리

---

dbms는 index를 항상 최신의 정렬된 상태로 유지해야 원하는 값을 빠르게 탐색할 수 있다. 그렇기 때문에 인덱스가 적용된 컬럼에 insert, update, delete가 수행된다면 각각 다음과 같은 연산을 추가적으로 해주어야 하며 그에 따른 오버헤드가 발생한다.

- insert : 새로운 데이터에 대한 인덱스를 추가함.
- delete : 삭제하는 데이터의 인덱스를 사용하지 않는다는 작업을 진행함.
- update : 기존의 인덱스를 사용하지 않음 처리하고, 갱신된 데이터에 대해 인덱스를 추가함.

  

### **인덱스(index)의 장점과 단점**

---

**장점**

- 테이블을 조회하는 속도와 그에 따른 성능을 향상시킬 수 있다.
- 전반적인 시스템의 부하를 줄일 수 있다.

**단점**

- 인덱스를 관리하기 위해 DB의 약 10%에 해당하는 저장공간이 필요하다.
- 인덱스를 관리하기 위해 추가 작업이 필요하다.
- 인덱스를 잘못 사용할 경우 오히려 성능이 저하되는 역효과가 발생할 수 있다.

  

### **인덱스(index)를 사용하면 좋은 경우**

---

- 규모가 작지 않은 테이블
- INSERT, UPDATE, DELETE가 자주 발생하지 않는 컬럼
- JOIN이나 WHERE 또는 ORDER BY에 자주 사용되는 컬럼
- 데이터의 중복도가 낮은 컬럼

  

### 인덱스 컬럼 기준

---

1개의 컬럼만 인덱스를 걸어야 한다면, 해당 컬럼은 카디널리티(Cardinality)가 가장 높은 것을 잡아야 한다는 점.

> 카디널리티(Cardinality)란 해당 컬럼의 중복된 수치를 나타냅니다.  
> 예를 들어 성별, 학년 등은 카디널리티가 낮다고 얘기합니다.  
> 반대로 주민등록번호, 계좌번호 등은 카디널리티가 높다고 얘기합니다.  

  

**여러 컬럼으로 인덱스 구성 시 기준**

결론적으로 여러 컬럼으로 인덱스를 잡는다면 카디널리티가 높은 순에서 낮은 순으로 구성하는 것이 더 성능이 뛰어납니다.

**여러 컬럼으로 인덱스 시 조건 누락**

조회 쿼리 사용 시 인덱스를 잡으려면 최소한 첫번 째 인덱스 조건은 조회조건에 포함되어야만 합니다.

첫 번째 인덱스 컬럼이 조회 쿼리에 없으면 인덱스를 타지 않는다는 점을 기억하시면 됩니다.

  

### index 생성, 삭제

---

```SQL
-- 인덱스 추가로 생성
create index idx on table_name (col1, col2, ..., colN);

-- 테이블 생성 시 인덱스 생성
create table `table_name` (
	...
	...
	index idx_name (col1, col2)
	-- or
	unique index idx_name (col1) -- 항상 유일 해야함.
);

-- 테이블에 추가
alter table table_name
add index idx_name (col1);

-- 인덱스 보기
show index from table_name;

-- 인덱스 삭제
alter table table_name drop index idx_name
```

  

### index 조회

---

```SQL
select col1, col2, ... colN
from idx_name
where table_name = 'table_name';
```

  

### index rebuild

---

인덱스를 리빌드하는 이유

인덱스 파일은 생성 후 insert, update, delete등을 반복하다보면 성능이 저하된다.

생성된 인덱스는 트리구조를 가지는데, 삽입, 수정, 삭제 등이 오랫동안 일어나다보면 트리의 한쪽이 무거워져 전체적으로 트리의 깊이가 깊어지기 때문이다.

```SQL
-- 인데스 리빌드
alter index idx_name rebuild;

-- 전체 인덱스 리빌드 쿼리문
SELECT 'ALTER INDEX '||INDEX_NAME||' REBUILD; 'FROM USER_INDEXES;
```

  

출처:

[https://mangkyu.tistory.com/96](https://mangkyu.tistory.com/96) [MangKyu's Diary]

[https://huskdoll.tistory.com/605](https://huskdoll.tistory.com/605)

[https://jojoldu.tistory.com/243](https://jojoldu.tistory.com/243)

[https://velog.io/@gillog/SQL-Index인덱스](https://velog.io/@gillog/SQL-Index%EC%9D%B8%EB%8D%B1%EC%8A%A4)

  

## view

---

뷰는 사용자에게 접근이 허용된 자료만을 제한적으로 보여주기 위해 하나 이상의 기본 테이블로부터 유도된 이름을 가지는 가상 테이블이다.

뷰는 저장장치 내에 물리적으로 존재하지 않지만 사용자에게 있는 것처럼 간주된다.

뷰는 데이터 보정작업, 처리과정 시험 등 임시적인 작업을 위한 용도로 활용된다.

뷰는 조인문의 사용 최소화로 사용상의 편의성을 최대화 한다.

  

### 뷰의 특징

---

뷰는 기본테이블로부터 유도된 테이블이기 때문에 기본 테이블과 같은 형태의 구조를 사용하며, 조작도 기본 테이블과 거의 같다.

뷰는 가상 테이블이기 때문에 물리적으로 구현되어 있지 않다.

데이터의 논리적 독립성을 제공할 수 있다.

필요한 데이터만 뷰로 정의해서 처리할 수 있기 때문에 관리가 용이하고 명령문이 간단해진다.

뷰를 통해서만 데이터에 접근하게 하면 뷰에 나타나지 않는 데이터를 안전하게 보호하는 효율적인 기법으로 사용할 수 있다.

기본 테이블의 기본키를 포함한 속성(열) 집합으로 뷰를 구성해야지만 삽입, 삭제, 갱신, 연산이 가능하다.

일단 정의된 뷰는 다른 뷰의 정의에 기초가 될 수 있다.

뷰가 정의된 기본 테이블이나 뷰를 삭제하면 그 테이블이나 뷰를 기초로 정의된 다른 뷰도 자동으로 삭제된다.

  

### **뷰(View)사용시 장 단점**

---

**장점**

논리적 데이터 독립성을 제공한다.

동일 데이터에 대해 동시에 여러사용자의 상이한 응용이나 요구를 지원해 준다.

사용자의 데이터관리를 간단하게 해준다.

접근 제어를 통한 자동 보안이 제공된다.

**단점**

독립적인 인덱스를 가질 수 없다.

ALTER VIEW문을 사용할 수 없다. 즉 뷰의 정의를 변경할 수 없다.

뷰로 구성된 내용에 대한 삽입, 삭제, 갱신, 연산에 제약이 따른다.

  

### 뷰(view)를 사용하는 이유

---

자주 쓰는 쿼리문을 안쓰고 테이블만 조회하면 된다.

보안에 유리하다.

뷰 테이블에 자료가 추가되는 것은 실체 테이블에 반영되지 않기 때문에 주의를 요한다.

  

### 뷰(view) 생성, 삭제

---

```SQL
-- 생성
create view view_name as select 구문;

create view view_name
as select col1, col2, ..., colN
from table_name
where condition;

-- * 여러 테이블의 칼럼을 모아서 (join) 하나의 테이블처럼 질의할 수 있음.

-- 삭제
drop view view_name;
```

  

### with check option / with read only option

---

**with check option**

- 조건 컬럼값을 변경하지 못하게 하는 옵션
    
    뷰를 정의하는 서브 쿼리문에 where 절을 추가하여 기본 테이블 중 특정 조건에 만족하는 로우(행)만으로 구성된 뷰를 생성할 수 있다.
    
    이때 where 절에 with check option을 기술하면 그 조건에 의해 기본 테이블에서 정보가 추출하는 것으로 조건에 사용되어진 컬럼 값은 뷰를 통해서는 변경이 불가능하다.
    
      
    

```SQL
create or replace view view_name
as select col1, col2, ..., colN
from table_name
where col1='' with check option;
```

  

**with read only**

- 기본 테이블의 어떤 컬럼에 대해서도 뷰를 통한 내용 수정을 불가능하게 만드는 옵션.

```SQL
create or replace view view_name
as select col1, col2, ..., colN
from table_name
where col1='' with read only;
```

  

출처:

[https://coding-factory.tistory.com/224](https://coding-factory.tistory.com/224)

[https://sassun.tistory.com/92](https://sassun.tistory.com/92)