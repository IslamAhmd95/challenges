-- Problem: Product Sales Analysis III
-- Link: https://leetcode.com/problems/product-sales-analysis-iii/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
with first_year_sales as
(select *, rank() over(PARTITION BY product_id order by year) rn from Sales)
select product_id, year first_year, sum(quantity) quantity, price from first_year_sales where rn = 1 group by product_id, year, price;

-- another solution
select Sales.product_id, Sales.year first_year, sum(quantity) as quantity, price from Sales join (select product_id, min(year) as year from sales group by product_id) sub on Sales.product_id = sub.product_id and Sales.year = sub.year group by Sales.product_id, Sales.year, price;



/*
Notes:
    - RANK() is better than ROW_NUMBER() because it includes all rows tied for the same first year.
    - MIN(year) is used to get the earliest year.
*/