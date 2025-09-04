-- Problem: Product Sales Analysis
-- Link: https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50
-- my rate: easy

-- PostgreSQL
select P.product_name, S.year, S.price from sales S join product P on S.product_id = P.product_id;

-- MySQL
select P.product_name, S.year, S.price from sales S join product P on S.product_id = P.product_id;
