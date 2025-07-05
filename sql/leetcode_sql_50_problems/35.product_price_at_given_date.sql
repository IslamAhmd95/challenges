-- Problem: Product Price at a Given Date
-- Link: https://leetcode.com/problems/product-price-at-a-given-date/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
with ordered_products as
(
select product_id, new_price, 
dense_rank() over(partition by product_id order by change_date desc) d_rank 
from products where change_date <= '2019-08-16'
)
,
all_products as 
(
    select product_id from products group by product_id
)
select p1.product_id, coalesce(p2.new_price, 10) price from all_products p1 left join ordered_products p2 on p1.product_id = p2.product_id and p2.d_rank = 1;


-- another solution
SELECT
p.product_id,
coalesce(
    (
        select new_price from products p2
        where p2.product_id = p.product_id and p2.change_date <= '2019-08-16'
        ORDER BY change_date DESC
        limit 1
    ), 10) as price
from 
(select DISTINCT product_id from products) p;