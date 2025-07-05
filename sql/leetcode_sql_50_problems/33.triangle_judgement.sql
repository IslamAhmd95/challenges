-- Problem: Triangle Judgement
-- Link: https://leetcode.com/problems/triangle-judgement/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select *, 
(
    case 
        when x + y > z and x + z > y and z + y > x then 'Yes' else 'No'
    end
) as triangle
from Triangle;



/*
Notes:

-- Row-wise vs. Column-wise Computation in SQL

1- Row-wise (Per Row) -> Scalar Expressions:
    - Operations that apply to **each individual row**, using only that row’s own values.
    - No grouping, no aggregation → result is **one value per row**.
    - Examples of row-wise operations:
        SELECT salary * 0.1 AS bonus
        SELECT CASE WHEN age >= 18 THEN 'Adult' ELSE 'Minor' END AS category
    - These are called **scalar expressions**:
        - Scalar = single value (one value per row)
        - Computed using `CASE`, arithmetic, simple conditions.

2- Column-wise (Set Level) -> Aggregate Functions:
    - Operations that compute **one result over multiple rows** (over values from **one column** across the dataset or group).
    - Examples of column-wise aggregates:
        SELECT AVG(salary) FROM employees
        SELECT COUNT(DISTINCT product_id) FROM orders
    - Must use with `GROUP BY` if you want **per group** results, otherwise you get a **single result for the whole table**.

3- Window Functions -> Hybrid:
    - Compute values **over columns and multiple rows** but **preserve the original row structure** (don’t collapse rows like aggregates do).
    - Examples:
        ROW_NUMBER() OVER (PARTITION BY ...)
        SUM(sales) OVER (PARTITION BY region)
    - Window functions produce **one value per row** -> they feel row-wise but depend on **multiple rows** (window frame).


*/