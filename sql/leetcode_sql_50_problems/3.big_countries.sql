-- Problem: Big Countries
-- Link: https://leetcode.com/problems/big-countries/description/?envType=study-plan-v2&envId=top-sql-50
-- my rate: easy

-- PostgreSQL
select name, population, area from World where area >= 3000000 or population >= 25000000;

-- MySQL
select name, population, area from World where area >= 3000000 or population >= 25000000;