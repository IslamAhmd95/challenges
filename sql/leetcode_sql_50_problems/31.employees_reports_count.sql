-- Problem: The Number of Employees Which Report to Each Employee
-- Link: https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select M.employee_id, M.name, count(E.employee_id) reports_count, round(avg(E.age)) average_age from employees M join employees E on M.employee_id = E.reports_to group by M.employee_id, M.name order by M.employee_id;



/*
Notes:


1️⃣ Self-Join:
- A self-join is when a table is joined to itself.
- In this problem, we join `employees` as managers (`M`) to `employees` as direct reports (`E`) using:
    ON M.employee_id = E.reports_to

2️⃣ COUNT(E.*) vs. COUNT(E.employee_id):
- Using COUNT(E.*) does **not work as expected** because:
  - In most SQL engines, `COUNT(*)` counts **all rows**, including those where columns might be NULL.
  - But when using `COUNT(column_name)`, only **non-NULL** values are counted.
- `COUNT(E.employee_id)` is correct because `employee_id` is assumed to be **NOT NULL** and gives the correct count of reports.

3️⃣ ROUND(AVG(E.age), 2) vs. ROUND(AVG(E.age)):
- If you use ROUND(number) without the second argument:
    - It rounds to the nearest whole number (integer).
    - It removes any decimal part → no decimals at all.
    - It doesn’t care if the number goes up or down—it just picks the closest integer.

*/