-- Problem: List the Products Ordered in a Period
-- Link: https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/?envType=study-plan-v2&envId=top-sql-50


-- MySQL
select product_name, sum(unit) unit from
products p join orders o 
on p.product_id = o.product_id and 
date_format(order_date, '%Y-%m') = '2020-02'
group by p.product_id
having sum(unit) >= 100;


-- PostgreSQL
select product_name, unit from
(
    select p.product_id, product_name, sum(unit) unit from
    products p join orders o 
    on p.product_id = o.product_id and 
    to_char(order_date, 'YYYY-MM') = '2020-02'
    group by p.product_id, product_name
    having sum(unit) >= 100
);



/*
Notes:
    - PostgreSQL requires that every selected column is either:
        - In the GROUP BY, or
        - An aggregate function.
*/
