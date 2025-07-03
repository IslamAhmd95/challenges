-- Problem: Customers Who Bought All Products
-- Link: https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select customer_id from Customer group by customer_id having count(distinct product_key) = (select count(*) from Product);



/*
Notes:
    - This subquery "(select count(*) from Product)" is a scalar subquery because it returns exactly one value
*/