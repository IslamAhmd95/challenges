-- Problem: Not Boring Movies
-- Link: https://leetcode.com/problems/not-boring-movies/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL
select * from cinema where mod(id, 2) != 0 and description not like '%boring%' order by rating desc;


-- MySQL
select * from cinema where mod(id, 2) != 0 and description not like '%boring%' order by rating desc;
