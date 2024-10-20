---
type: Database
archive: false
---
## **join**

---

둘 이상의 테이블에서 데이터가 필요한 경우 테이블 조인이 필요.

일반적으로 조인 조건을 포함하는 where 절을 작성해야 한다.

조인 조건은 일반적으로 각테이블의 PK 및 FK로 구성됩니다.

  

join의 종류

- inner join
- outer join
    - left outer join
    - right outer join

  

join 조건의 명시에 따른 구분.

- natural join
- cross join(full join, cartesian join)

  

join시 주의

- 조인의 처리는 어느 테이블을 먼저 읽을지를 결정하는 것이 중요(처리할 작업량이 상당히 달라진다.)
- inner join : 어느 테이블을 먼저 읽어도 결과가 달라지지 않아 mysql 옵티마이저가 조인의 순서를 조절해서 다양한 방법으로 최적화를 수행할 수 있다.
- outer join : 반드시 outer가 되는 테이블을 먼저 읽어야 하므로 옵티마이저가 조인 순서를 선택할 수 없다.

  

### inner join

---

가장 일반적인 join의 종류이며 교집합이다.

동등 조인(uqui-join)이라고도 하며, N개의 테이블 조인 시 N - 1개의 조인 조건이 필요함.

```SQL
> select col1, col2, ..., colN
	from table1 inner join table2
	on table1.column = table2.column;

> select alias1.col1, alias1.col2, ..., alias2.colN
	from table1 as asias1 inner join table2 as alias2
	on alias1.column = alias2.column;
```

  

- on을 이용한 join 조건 지정.
    
    ![[Untitled 40.png|Untitled 40.png]]
    
      
    
- using을 이용한 join 조건 지정.
    
    ```SQL
    > select col1, col2, ..., colN
    	from table1 join table2
    	using (공통 column);
    ```
    
    ![[Untitled 1 18.png|Untitled 1 18.png]]
    

### natural join

---

```SQL
> select col1, col2, ..., colN
	from table1 natural join table2;
```

  

### outer join

---

left outer join, right outer join, full outer join으로 구분 됨.

어느 한쪽 테이블에는 해당하는 데이터가 존재하는데 다른 쪽 테이블에는 데이터가 존재하지 않을 경우 그 데이터가 검색되지 않는 문제점을 해결하기 위해 사용.

![[Untitled 2 17.png|Untitled 2 17.png]]

  

left outer join

- 왼쪽 테이블을 기준으로 join 조건에 일치 하지 않는 데이터까지 출력
    
    ```SQL
    > select col1, col2, ..., colN
    	from table1 left outer join table2
    	on or using;
    ```
    
      
    

right outrer join

- 오른쪽 테이블을 기준으로 join조건에 일치하지 않는 데이터까지 출력.

```SQL
> select col1, col2, ..., colN
	from table1 right outer join table2
	on or using;
```

  

full outer join

- 양쪽 테이블을 기준으로 join 조건에 일치하지 않는 데이터까지 출력.

```SQL
> select col1, col2, ... colN
	from table1 full outer join table2
	on or using
```

  

self join

- 같은 테이블끼리 join
- 모든 사원의 사번, 이름, 매니저사번, 매니저 이름

```SQL
select e.employee_id, e.first_name, m.employee_id, m.first_name
from employees e inner join employees m
on e.manager_id = m.employee_id;
```

  

None-Equi join

- table의 pk, fk가 아닌 일반 column을 join 조건으로 지정.
- 모든 사원의 사번, 이름, 급여, 급여 등급.

![[Untitled 3 16.png|Untitled 3 16.png]]