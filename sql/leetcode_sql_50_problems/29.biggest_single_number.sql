-- Problem: Biggest Single Number
-- Link: https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select (select num from MyNumbers group by num having count(num) = 1 order by num desc limit 1) as num;


/*
Notes:

-- ➤ A scalar subquery returns a **single value** (one cell), not a table or multiple rows.
-- ➤ Scalar subqueries are typically used:
--    1. Inside a SELECT clause (to return one value)
--    2. Inside a (WHERE / HAVING) clauses (to compare with other values)

-- ✅ Examples:

SELECT (SELECT MAX(salary) FROM employees) AS highest_salary;

SELECT employee_id
FROM employees
WHERE (SELECT MAX(salary) FROM employees) > 50000;

-- ➤ Key Rules:
--    - The subquery **must return zero or one value** (zero rows → NULL, one row → value).
--    - If it returns **more than one row**, SQL will throw an error: 
--      "more than one row returned by a subquery used as an expression".
*/