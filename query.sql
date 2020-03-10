
create database ordermanager;

create user 'elementarystudio'@'localhost' identified by 'YXFzd2RlZnI=';
grant all privileges on ordermanager.* to 'elementarystudio'@'localhost';
flush privileges;

use ordermanager;
show tables;

