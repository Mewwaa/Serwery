create database carRental;
use carRental;
create table CARS(`CAR_ID` int AUTO_INCREMENT UNIQUE primary key NOT NULL , `NAME`   varchar(45), `BRAND`  varchar(45), `HP`   int, `ENGINE_CAPACITY`   int, `MANUFACTURE_DATE`   date)AUTO_INCREMENT=1;
create table USER(`USER_ID` int AUTO_INCREMENT UNIQUE primary key   , `NAME`   varchar(45), `SURNAME`   varchar(45), `PESEL`   int)AUTO_INCREMENT=1;
create table RENTAL(`RENTAL_ID` int AUTO_INCREMENT UNIQUE primary key   , `CAR_ID` int references CARS (CAR_ID), `USER_ID` int references USER (USER_ID))AUTO_INCREMENT=1;
create table LEND_HISTORY(`CAR_ID` int references CARS (CAR_ID), `USER_ID` int references USER (USER_ID), `LEND_MONTH` varchar(45), `PUNISH_PRICE` int)AUTO_INCREMENT=1;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root'; flush privileges;
