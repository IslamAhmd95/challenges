-- Problem: Project Employees I
-- Link: https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL
select project_id, round(avg(
    experience_years
), 2) average_years
from project p left join employee e on p.employee_id = e.employee_id group by project_id;


-- MySQL
select project_id, round(avg(
    experience_years
), 2) average_years
from project p left join employee e on p.employee_id = e.employee_id group by project_id;

