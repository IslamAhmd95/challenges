-- Problem: Employee Bonus
-- Link: https://leetcode.com/problems/employee-bonus/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL
select E.name, B.bonus from Employee E left join Bonus B on E.empId = B.empId where B.bonus is null or B.bonus < 1000;

-- MySQL
select E.name, B.bonus from Employee E left join Bonus B on E.empId = B.empId where B.bonus is null or B.bonus < 1000;