---
type: Database
archive: false
---
(Structured Query Language), 관계형 데이터베이스 관리 시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어.

  

문장

INSERT  
UPDATE  
DELETE  

SELECT

CREATE  
ALTER  
DROP  
RENAME  

COMMIT  
ROLLBACK  

GRANT  
REVOKE  

설명

DML(Data Manipulation Language)이라 부르며, 개별적으로 Database 테이블에서 새로운 행을 입력하고, 기존의 행을 변경하고 제거한다.  
  

Database로부터 Data를 검색합니다. SELECT 역시 DML로 분류된다.

DDL(Data Definition Language)이라 부르며, 테이블로부터 데이터 구조를 생성, 변경, 제거한다.  
  
  

DML 명령문으로 수행한 변경을 관리한다.  
  

DCL(Data Control Language)이라 부르며, Database와 그 구조에 대한 접근 권한을 제공하거나 제거한다.

  

## DDL(Data Definition Language)

---

데이터베이스의 스키마를 정의, 생성, 수정하는 기능

create

drop

alter

데이터베이스 객체 생성

데이터베이스 객체 삭제

데이터베이스 객체 수정

**create**

```SQL
> create database 데이터베이스명;
> create database 데이터베이스명
	default character set 값
	collate 값;
```

alter

```SQL
> alter database 데이터베이스명
	default character set 값 collate 값;
```

drop

```SQL
> drop database 데이터베이스명;
```

  

### table 생성

---

```SQL
> create table table_name (
		column_name1 Type [optional attributes],
		column_name2 Type,
		...
		column_nameN Type,
	);
```

- optional attributes
    
    NOT NULL : 각 행은 해당 열의 값을 포함해야 하며 null 값은 허용되지 않음.
    
    DEFAULT value : 값이 전달되지 않을 때 추가되는 기본값 설정.
    
    UNSIGNED : Type이 숫자인 경우만 해당되며 숫자가 0 또는 양수로 제한됨.
    
    AUTO INCREMENT : 새 레코드가 추가 될 때마다 필드 값을 자동으로 1 증가시킴
    
    PRIMARY KEY : 테이블에서 행을 고유하게 식별하기 위해 사용. PRIMARY KEY 설정이 있는 열은 일반적으로 ID번호이며 AUTO INCREMENT와 같이 사용되는 경우가 많음.
    
      
    

### 제약 조건

---

컬럼에 저장될 데이터의 조건을 설정하는 것

제약조건을 설정하면 조건에 위배되는 데이터는 저장 불가

테이블 생성 시 컬럼에 직접 지정하거나 constraint로 지정, 또는 ALTER를 이용하여 설정 가능.

![[Untitled 3.png|Untitled 3.png]]

  

스키마 : 데이터베이스의 테이블에 저장될 데이터의 구조와 형식을 정의

## DML

---

데이터베이스의 테이블에 있는 내용을 직접 조작하는 기능(CRUD)

insert  
delete  
update  
select  

데이터베이스 객체에 데이터를 입력  
데이터베이스 객체에 데이터를 삭제  
데이터베이스 객체 안의 데이터를 수정  
데이터베이스 객체 안의 데이터 조회  

  

### INSERT

---

```SQL
> insert into table_name
	values(col_val1, col_val2, col_val3, ...);
> insert into table_name(col_name1, col_name2, ..., col_nameN)
	values(col_val1, col_val2, ..., col_valN);
> insert into table_name(col_name1, col_name2, ..., col_nameN)
	values (col_val1, col_val2, ..., col_valN),
				 (col_val1, col_val2, ..., col_valN);
```

  

### UPDATE

---

```SQL
> update table_name
	set col_name=col_val1, [col_name2 = col_val2, ..., col_nameN=col_valN]
	where conditions;
```

- where절의 조건에 만족하는 레코드의 값을 변경.
- 주의 : where절을 생략하면 모든 데이터가 바뀐다.

  

### DELETE

---

```SQL
> delete from table_name
	where conditions;
```

- where절의 conditions(조건)에 만족하는 레코드의 값을 삭제.
- 주의 : where절을 생략하면 모든 데이터가 삭제된다.

  

### SELECT

---

```SQL
-- select 구문 형식
SELECT * | {[ALL | DISTINCT] column | expression [alias], ...} [ INTO new_table ]
[ FROM table_source ] [ WHERE search_condition ]
[ GROUP BY group_by_expression ]
[ HAVING search_condition ]
[ ORDER BY order_expression [ ASC | DESC ]

-- 기본적인 형태
SELECT select_list
[ FROM table_source ] [ WHERE search_condition ]

-- * 원하는 열에서 중복된 데이터를 제외하고 필터링하고 싶을 때는 'DISTINCT'를 사용.
SELECT DISTINCT select_list
FROM table_source

-- select ... into ...
-- 조건에 맞는 기존 테이블의 열 내용을 새 테이블로 가져와 테이블로 만드는 것.
SELECT select_list [ INTO new_table ]
[ FROM table_source ] [ WHERE search_condition ]

-- group by
-- 그룹으로 묶어주는 역할
SELECT select_list
[ FROM table_source ] [ WHERE search_condition ]
[ GROUP BY group_by_expression ]
[ HAVING search_condition ]

-- order by 문
-- 조건에 맞는 열을 가져와 order by에 지정된 열을 기준으로 정렬.
-- 기본 정렬은 asc : 오름차순 정렬.
SELECT select_list
[ FROM table_source ] [ WHERE search_condition ]
[ ORDER BY order_expression [ ASC | DESC ]
```

select clause

*

ALL

DISTINCT

column

expression

alias

description

FROM 절에 나열딘 테이블에서 모든 열을 선택.

선택된 모든 행을 반환. ALL이 default (생략 가능)

선택된 모든 행 중에서 중복 행 제거

FROM 절에 나열된 테이블에서 지정된 열을 선택.

표현식은 값으로 인식되는 하나 이상의 값, 연산자 및 SQL 함수의 조합을 뜻함.

별칭

  

**alias, 사칙연산 (+, -, *, /), NULL Value**

![[Untitled 1 2.png|Untitled 1 2.png]]

  

**case exp1 when exp2 then exp3 [when exp4 then exp5 ... else exp6] end**

![[Untitled 2 2.png|Untitled 2 2.png]]

  

**Operators**

- BETWEEN
- LIKE
- IN
- AND, OR, NOT
- IS NULL, IS NOT NULL
- LIKE (whild card : %, _ )

특정 범위

같은 패턴

특정 값들

  

  

  

```SQL
-- BETWWEN
SELECT select_list
[ FROM table_source ] [ WHERE column BETWEEN A AND B ]

-- LIKE
SELECT select_list
[ FROM table_source ] [ WHERE column LIKE 'pattern' ]

-- IN
SELECT select_list
[ FROM table_source ] [ WHERE column IN 'list' ]

-- LIKE (이름의 끝에서 3번쨰 자리에 'x'가 들어간 사원의 사번, 이름 검색
select employee_id, first_name
from employees
where first_name like '%x__';
```

  

### MYSQL 내장함수

---

숫자 관련 함수

![[Untitled 3 2.png|Untitled 3 2.png]]

문자 관련 함수

![[Untitled 4.png]]

![[Untitled 5.png]]

날짜 관련 함수

![[Untitled 6.png]]

![[Untitled 7.png]]

논리 관련 함수

![[Untitled 8.png]]

그룹 함수

![[Untitled 9.png]]

  

### DCL

---

데이베이스의 테이블에 접근 권한이나 CRUD 권한을 정의하는 기능

grant

revoke

데이터베이스 객체에 권한 부여

이미 부여된 데이터베이스 객체 권한을 취소

  

### TCL(Transaction Control Language)

---

트랜잭션 제어어.

transaction이란 데이터베이스의 논리적 연산 단위.

start transaction

commit

rollback

commit, rollback이 나올 때까지 실행되는 모든 SQL

실행한 Query를 최종적으로 적용.

실행한 Query를 마지막 commit전으로 취소시켜 데이터를 복구

```SQL
use ssafydb;

start stransaction;

...
rollback;

...
commit;

...
savepoint f1;

...
rollback to f1;
```