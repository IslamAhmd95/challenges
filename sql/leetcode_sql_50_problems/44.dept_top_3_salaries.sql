-- Problem: Department Top Three Salaries
-- Link: https://leetcode.com/problems/department-top-three-salaries/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
with high_earners as
(
    select *,
    dense_rank() over(partition by departmentId order by salary desc) as salary_rank
    from employee
)
select D.name as Department, H.name as employee, H.salary Salary from high_earners H join Department D on H.departmentId = D.id where salary_rank <= 3;


