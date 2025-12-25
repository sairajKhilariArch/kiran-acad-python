CREATE TABLE `capgemini`.`emp_info` (
  `empid` INT NOT NULL,
  `name` varchar(50) ,
  `salary` int ,
  `department` varchar(50),
  `location` VARCHAR(45) ,
  PRIMARY KEY (`empid`));
  
  
  
  
INSERT INTO emp_info (empid, name, salary, department, location) 
VALUES (1, 'Anup', 10000, 'Dev', 'Pune');

INSERT INTO emp_info (empid, name, salary, department, location) 
VALUES (2, 'Rani', 26000, 'Dev', 'Pune');
INSERT INTO emp_info (empid, name, salary, department, location) 
VALUES (3, 'Jay', 18000, 'Dev', 'Pune');
INSERT INTO emp_info (empid, name, salary, department, location) 
VALUES (4, 'Vishal', 10000, 'Dev', 'Pune');
INSERT INTO emp_info (empid, name, salary, department, location) 
VALUES (5, 'Shinal', 10000, 'Dev', 'Pune');
INSERT INTO emp_info (empid, name, salary, department, location) 
VALUES (6, 'Rony', 10000, 'Dev', 'Pune');
INSERT INTO emp_info (empid, name, salary, department, location) 
VALUES (7, 'Pooja', 10000, 'Dev', 'Pune');
select 'name' from emp_info;



drop table emp_info;








11:17:07	insert into emp_info ('empid','name','salary','dapartment','location') values (1,'Anup',10000,'Dev','Pune')	Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''empid','name','salary','dapartment','location') values (1,'Anup',10000,'Dev','P' at line 1	0.00027 sec
