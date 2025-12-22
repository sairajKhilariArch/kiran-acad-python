CREATE DATABasE capgemini;

use capgemini;

CREATE TABLE `capgemini`.`employee` (
  `id` INT NULL,
  `name` VARCHAR(45) NULL,
  `profile` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `salary` INT NULL,
  `age` INT NULL,
  `experience` INT NULL
  );

show tables;

insert into `employee` (`id`,`name`,`profile`,`email`,`salary`,`age`,`experience`) values (1,'rani','dev','rani@gmail.com',11000,43,27);

insert into `employee` (`id`,`name`,`profile`,`email`,`salary`,`age`,`experience`) values (2,'raj','test','raj@gmail.com',21000,33,17);

insert into `employee` (`id`,`name`,`profile`,`email`,`salary`,`age`,`experience`) values (3,'radha','test','radha@gmail.com',26000,38,21);

insert into `employee` (`id`,`name`,`profile`,`email`,`salary`,`age`,`experience`) values (4,'raj','dev','raj12@gmail.com',51000,32,12);

insert into `employee` (`id`,`name`,`profile`,`email`,`salary`,`age`,`experience`) values (5,'john','dev','john@gmail.com',51000,39,27);


select * from capgemini.employee;


alter table `employee` add column `branch_location` varchar(50) null;


select SUM(`salary`) as total_salary_expenses from `employee`;


select MAX(`salary`) as max_test_salary from `employee` where `profile` = 'test';


select avg(`experience`) as avg_experience from `employee`;


select `name` from `employee` where `salary` = (select MAX(`salary`) from `employee`);


select `name`, `experience` from `employee` where `salary` = (select MIN(`salary`) from `employee`);


select COUNT(*) as total_employees from `employee`;


select `name` from `employee` where `profile` = 'test' and `salary` > 25000;


set SQL_SAFE_updateS = 0;
update `employee` set `profile` = 'support' where `name` = 'Radha';
set SQL_SAFE_updateS = 1;


select distinct `salary` from `employee` order by `salary` desc limit 1 offset 1;


select distinct `salary` from `employee` order by `salary` asc limit 1 offset 1;


select AVG(`salary`) as avg_dev_salary from `employee` where `profile` = 'dev';


select `name`, `salary` from `employee`  where `experience` = (select MIN(`experience`) from `employee`);


select `name` from `employee`  where `age` = (select MIN(`age`) from `employee` where `salary` = (select MAX(`salary`) from `employee`));


delete from `employee`;
set SQL_SAFE_updateS = 1;





drop table employee;

