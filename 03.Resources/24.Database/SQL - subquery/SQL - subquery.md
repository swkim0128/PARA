---
type: Database
archive: false
---
## 서브 쿼리 (Subquery)

---

서브쿼리란 다른 쿼리 내부에 포함되어 있는 select 문을 의미한다.

서브 쿼리를 포함하고 있는 쿼리를 외부 쿼리(outer query) 또는 메인 쿼리라고 부르며, 서브 쿼리는 내부 쿼리(inner query)라고도 부른다.

서브 쿼리는 비교 연산자의 오른쪽에 기술해야 하고 반드시 괄호로 감싸져 있어야만 한다.

  

### 서브 쿼리의 종류

---

중첩 서브 쿼리(Nested Subquery) where 문에 작성하는 서브 쿼리

1. 단일 행
2. 복수(다중) 행
3. 다중 컬럼

인라인 뷰(inline view) - from 문에 작성하는 서브 쿼리

스칼라 서브 쿼리 (Sclalar subquery) - select 문에 작성하는 서브 쿼리

  

### 서브 쿼리

---

주의 사항

- 서브쿼리는 반드시 ()로 감싸야 한다.
- 서브 쿼리는 단일 행 또는 다중 행 비교 연산자와 함께 사용된다.

  

서브 쿼리가 사용이 가능한 곳

- select
- from
- where
- having
- order by
- insert 문의 values
- update 문의 set

  

### 서브 쿼리 종류.

---

Nested Subquery - 단일 행

- 서브 쿼리의 결과가 단일행을 리턴.

  

Nested Subquery - 다중 행

- 서브 쿼리의 결과가 다중행을 리턴 : IN
    
    ![[Untitled 57.png|Untitled 57.png]]
    
      
    
- 서브 쿼리의 결과가 다중행을 리턴 : ANY
    
    ![[Untitled 1 35.png|Untitled 1 35.png]]
    
      
    
- 서브 쿼리의 결과가 다중행을 리턴 : ALL
    
    ![[Untitled 2 34.png|Untitled 2 34.png]]
    
      
    

Nested Subquery - 다중 열

- 서브 쿼리의 결과가 다중열을 리턴.
    
    ![[Untitled 3 33.png|Untitled 3 33.png]]
    
      
    

인라인 뷰(Inline View)

- FROM 절에 사용되는 서브 쿼리를 인라인 뷰(inline view) 라 한다.
- 서브 쿼리가 from절에 사용되면 뷰(view)처럼 결과가 동적으로 생성된 테이블로 사용 가능
- 임시적인 뷰이기 때문에 데이터베이스에는 저장되지 않는다.
- 동적으로 생성된 테이블이기 때문에 column을 자유롭게 참조 가능.
    
    ![[Untitled 4 29.png|Untitled 4 29.png]]
    
      
    

인라인 뷰(inline view) - TopN 질의

- 모든 사원의 사번, 이름, 급여를 출력.
    
    사원 정보를 급여순으로 정렬
    
    한 페이지당 5명이 출력
    
    현재 페이지가 3페이지라고 가정.
    
    ![[Untitled 5 26.png|Untitled 5 26.png]]
    
      
    

인라인 뷰(inline view) - limit 활용 (Mysql)

- 모든 사원의 사번, 이름, 급여를 출력.
    
    사원 정보를 급여순으로 정렬.
    
    한 페이지당 5명이 출력
    
    현재 페이지가 3페이지라고 가정
    
    ![[Untitled 6 23.png|Untitled 6 23.png]]
    
      
    

스칼라 서브 쿼리 (Scalar Subquery)

- select 절에 있는 서브 쿼리
- 한 개의 행만 반환
    
    직급 아이디가 IT_PROG인 사원의 사번, 이름, 직급 아이디, 부서이름
    
    ![[Untitled 7 20.png|Untitled 7 20.png]]
    
      
    
    60번 부서에 근무하느 사원의 사번, 이름, 급여, 부서번호, 60번부서의 평균 급여
    
    ![[Untitled 8 18.png|Untitled 8 18.png]]
    
      
    

서브 쿼리를 이용한 create

- employees table을 emp_copy라는 이름으로 복사(컬럼 이름 동일)
    
    ```SQL
    create table emp_copy
    select * from employees;
    ```
    
- employees table의 구조만 emp_blank라는 이름으로 생성(컬럼 이름 동일)
    
    ```SQL
    create table emp_blank
    select * from employees
    where 1 = 0;
    ```
    
- 50 번 부서의 사번(eid), 이름(name), 급여(sal), 부서번호(did)만 emp50이라는 이름으로 생성
    
    ![[Untitled 9 17.png|Untitled 9 17.png]]
    
      
    

서브 쿼리를 이용한 insert

- employees table에서 부서번호가 80인 사원의 모든 정보를 emp_blank에 insert.
    
    ![[Untitled 10 15.png|Untitled 10 15.png]]
    
      
    

서브 쿼리를 이용한 update

- employees table의 모든 사원의 평균 급여보다 적게 받는 emp50 table의 사원의 급여를 500 인상.
    
    ![[Untitled 11 13.png|Untitled 11 13.png]]
    
      
    

서브 쿼리를 이용한 delete

- employees table의 모든 사원의 평균 급여보다 적게 받는 emp50 table의 사원은 퇴사.
    
    ![[Untitled 12 12.png|Untitled 12 12.png]]