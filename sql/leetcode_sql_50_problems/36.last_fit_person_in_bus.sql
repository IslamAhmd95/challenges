-- Problem: Last Person to Fit in the Bus
-- Link: https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
with total_weight as
(
select person_name,
sum(weight) over(order by turn) weight_sum
from Queue
)
select person_name from total_weight where weight_sum <= 1000 order by weight_sum desc limit 1;
