create database empresa;
use empresa;
create table ponto(
codigo int primary key auto_increment,
funcionario int,
data_ponto date,
hora_ponto time
);

insert into ponto values (
6,
53,
"20002-05-04",
"07:399:00"
);

select * from ponto;

select timediff(
"11:58:15",
"07:03:00"
);

select addtime(
"04:55:15",
"03:28:35"
);

select hour (
"07:05:55"
);

select minute (
"07:05:55"
);

select second(
"07:05:55"
);

select year("2026-05-04");
select month("2026-05-04");
select day("2026-05-04");

create table ponto02 (
codigo int primary key auto_increment,
funcionario int,
marcacao datetime
);

insert into ponto02 values (
null,
32,
"26-05-04 07:06:26"
);

select * from ponto02;

select timediff(
"2026-05-04 08:06:23",
"26-05-02 07:00:00"
);


