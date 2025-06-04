-- Problem: Immediate Food Delivery II
-- Link: https://leetcode.com/problems/immediate-food-delivery-ii/description/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL & MySQL
with firstOrders as
(
    select *, row_number() over(partition by customer_id order by order_date asc) rn from Delivery
)
select 
round(avg(
    case
        when order_date = customer_pref_delivery_date then 1
        else 0
    end
) * 100.0, 2) immediate_percentage
from firstOrders where rn=1;



-- PostgreSQL solution
with firstOrders as
(
    select distinct on (customer_id) * from Delivery order by customer_id, order_date ASC
)
select 
round(avg(
    case
        when order_date = customer_pref_delivery_date then 1
        else 0
    end
) * 100.0, 2) immediate_percentage
from firstOrders;




