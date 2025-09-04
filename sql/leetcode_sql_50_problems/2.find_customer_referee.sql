-- Problem: Find Customer Referee
-- Link: https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50
-- my rate: easy

-- PostgreSQL
select name from customer where referee_id is null or referee_id != 2;

-- MySQL
select name from Customer where referee_id is null or referee_id != 2;