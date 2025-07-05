-- Problem: Primary Department for Each Employee
-- Link: https://leetcode.com/problems/primary-department-for-each-employee/description/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL
with numbered_employees as
(
    select employee_id, department_id, 
    row_number() over
    (
        partition by employee_id order by primary_flag desc
    ) as rn
    from employee
)
select employee_id, department_id from numbered_employees where rn = 1;


-- MySQL
with ranked_departments as
(
select employee_id, department_id, 
row_number() over
(partition by employee_id order by 
    (
    case when primary_flag = 'Y' then 1 else 0 end
    ) desc
) as rn
from employee
)
select employee_id, department_id from ranked_departments where rn = 1;



-- MySQL & PostgreSQL  "less efficient"
with employee_flags_count as
(select employee_id, count(primary_flag) flags_count from employee group by employee_id)
select E.employee_id, E.department_id from employee E join employee_flags_count EF on E.employee_id = EF.employee_id and ((EF.flags_count > 1 and E.primary_flag = 'Y') or (EF.flags_count = 1));




/*
Notes:


-- ➕ Why use CASE in ORDER BY?
-- - In MySQL, sorting strings like 'Y' and 'N' using ORDER BY primary_flag DESC can be unreliable:
--     1. MySQL is **case-sensitive** by default → 'Y' ≠ 'y'
--     2. MySQL string ordering might differ from PostgreSQL.
--     3. If primary_flag contains NULLs, the behavior can be inconsistent.
-- - To ensure correct and predictable ordering → use a CASE expression to convert to numeric (1 or 0).

-- ➕ The CASE ensures:
--     primary_flag = 'Y' → gets 1 → sorted first (DESC)
--     any other value → gets 0 → sorted after

-- ➕ This method works reliably across both MySQL and PostgreSQL, and it's a good technique for safe ordering among databases


*/