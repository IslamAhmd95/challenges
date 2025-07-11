-- Problem: Employees Whose Manager Left the Company
-- Link: https://leetcode.com/problems/employees-whose-manager-left-the-company/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select employee_id from Employees 
where salary < 30000 
and manager_id is not null
and manager_id not in
(select employee_id from Employees)
order by employee_id;


-- another solution
select employee_id from Employees E1
where salary < 30000 and manager_id is not null and not exists
(select 1 from Employees E2 where E1.manager_id = E2.employee_id)
order by employee_id;



/*
Notes:
    - In SQL, NULL is not equal to anything—not even NULL itself.
    - Comparing anything to NULL (using =) results in UNKNOWN, not TRUE or FALSE.
    - Always use IS NULL or IS NOT NULL when dealing with potential NULLs.
    - When using NOT IN, be extra careful with NULLs in both the main query and the subquery.
*/

