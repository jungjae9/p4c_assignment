# mydata가 있으면 삭제하고 없으면 다음 코드를 실행하는 코드
drop database if exists mydata;
create database mydata;
show databases;
# mydata 데이터베이스를 사용하겠다는 코드
use mydata;
#myproduct 테이블 생성, 기본키 mykey로 설정
create table myproduct(
	mykey int,
    productid text,
    price int,
    discount_price int,
    discount_percent int,
    delevery text,
    primary key(mykey)
);
#테이블 목록 보기 명령
show tables;
#테이블 삭제 명령
Drop table myproduct;
show tables;
create table myproduct(
	mykey int unsigned auto_increment,
    productid text,
    price int,
    discount_price int,
    discount_percent int,
    delevery text,
    primary key(mykey)
);
show tables;
#테이블 구조보기 명령
desc myproduct;
create table customer_db(
	no int not null,
    name char(20) not null,
    age tinyint,
    phone varchar(20),
    email varchar(30) not null,
    address varchar(50),
    primary key(no)
);
desc customer_db;
#customer_db 테이블에 model 컬럼 추가
alter table customer_db add column model varchar(10) not null;
#customer_db 테이블의 name 컬럼의 데이터형을 char에서 varchar로 바꿈
alter table customer_db modify column name varchar(20) not null;
#customer_db 테이블의 name 컬럼의 이름을 modelname으로 바꾸고 데이터형을 varchar(10)으로 바꿈 
alter table customer_db change column name modelname varchar(10);
# customer_db 테이블의 age 컬럼 삭제
alter table customer_db drop column age;
desc customer_db;
insert into customer_db values(1, 'jupyter', 'apple', 'naver', 'seoul', 'DIW');
#특정 필드에만 값 넣기
insert into customer_db(no, modelname, email, model) values(2, 'python', 'google', 'DUW');
insert into customer_db values(3, 'pyri', 'apple', 'naver', 'seoul', 'DIW-2');
insert into customer_db values(4, 'protoss', 'samsung', 'naver', 'ulsan', 'DrW-1');
insert into customer_db values(5, 'jug', 'saomi', 'naver', 'seoul', 'DIW-3');
insert into customer_db values(6, 'terran', 'samsung', 'naver', 'seoul', 'DIW');
insert into customer_db values(7, 'garen', 'apple', 'google', 'seoul', 'DIW-10');
insert into customer_db values(8, 'faker', 'samsung', 'naver', 'ulsan', 'DIW');
insert into customer_db values(9, 'anaconda', 'samsung', 'nate', 'seoul', 'DIW');
insert into customer_db values(10, 'tbs', 'samsung', 'nate', 'seoul', 'DIW');
select*from customer_db;
#특정 컬럼(modelname, email) 값만 읽기 
select modelname, email from customer_db;
# 특정 컬럼을 기준으로 정렬해서 읽으려면 order by를 씀. desc는 내림차순, asc는 오름차순
# no를 기준으로 내림차순 읽기
select * from customer_db order by no desc;
# 조건에 맞는 데이터만 검색할 때는 where 사용
# email이 google인 데이터만 검색
select * from customer_db where email = 'google';
# like를 활용한 부분 일치 검색
# modelname이 p로 시작하는 데이터 검색
select * from customer_db where modelname like 'p%';
# modelname에 p가 포함된 데이터 검색
select * from customer_db where modelname like '%p%';
# modelname이 p로 시작되고 뒤에 5글자가 붙는 경우 검색
select * from customer_db where modelname like 'p_____';
# 결과중 일부만 보고 싶을 때 limit 사용
# customer_db의 데이터 처음부터 5개만 가져오기
select * from customer_db limit 5;
# customer_db의 데이터 8번째부터 3개만 가져오기
select * from customer_db limit 7, 3;
# 조건 조합 위의 조건들을 조합해서 사용 가능, 조합 순서는 select from where order by limit
select model, modelname from customer_db where modelname like '%a%' order by model asc limit 2;
# update로 데이터 값 바꾸기
set sql_safe_updates = 0;
update customer_db set email = 'naver' where phone = 's%';
#delete를 이용해서 데이터 삭제
# customer_db 테이블에서 no의 값이 9인 데이터 삭제
delete from customer_db where no = 9;
select * from customer_db;