-- Problem: Group Sold Products By The Date
-- Link: https://leetcode.com/problems/group-sold-products-by-the-date/description/?envType=study-plan-v2&envId=top-sql-50


-- MySQL
select sell_date, count(distinct product) num_sold,
group_concat(distinct product order by product separator ',') products
from Activities group by sell_date order by sell_date;


-- PostgreSQL
select sell_date, count(distinct product) num_sold,
string_agg(distinct product, ',' order by product) products
from Activities group by sell_date order by sell_date;



/*
Notes:
    - GROUP_CONCAT (MySQL): Combines product names into one comma-separated string.
    - STRING_AGG (PostgreSQL): Same as GROUP_CONCAT, but for PostgreSQL.
    - Both GROUP_CONCAT and STRING_AGG support DISTINCT to remove duplicates.
    - You can order values inside the GROUP_CONCAT/STRING_AGG by using `ORDER BY` inside the function.
*/
