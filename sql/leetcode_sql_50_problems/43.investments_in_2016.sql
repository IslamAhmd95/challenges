-- Problem: Investments in 2016
-- Link: https://leetcode.com/problems/investments-in-2016/?envType=study-plan-v2&envId=top-sql-50



-- MySQL
with InsuranceAnalysis as
(
    select tiv_2016,
    count(*) over(partition by lat, lon) as location_count,
    count(*) over(partition by tiv_2015) as tiv_2015_count
    from Insurance
)
select round(sum(tiv_2016), 2) tiv_2016 from InsuranceAnalysis where location_count = 1 and tiv_2015_count > 1;


-- another solution
with unique_loc as 
(
    select lat, lon from Insurance group by lat, lon having count(*) = 1
),
multi_tiv_2015 as
(
    select tiv_2015 from Insurance group by tiv_2015 having count(*) > 1
)
select round(sum(Insurance.tiv_2016), 2) tiv_2016 from unique_loc join Insurance on Insurance.lat = unique_loc.lat and Insurance.lon = unique_loc.lon
join multi_tiv_2015
on Insurance.tiv_2015 = multi_tiv_2015.tiv_2015;



-- PostgreSQL
with InsuranceAnalysis as
(
    select tiv_2016,
    count(*) over(partition by lat, lon) as location_count,
    count(*) over(partition by tiv_2015) as tiv_2015_count
    from Insurance
)
select round(sum(tiv_2016::decimal), 2) tiv_2016 from InsuranceAnalysis where location_count = 1 and tiv_2015_count > 1;


-- another solution
with unique_loc as 
(
    select lat, lon from Insurance group by lat, lon having count(*) = 1
),
multi_tiv_2015 as
(
    select tiv_2015 from Insurance group by tiv_2015 having count(*) > 1
)
select round(sum(Insurance.tiv_2016::decimal), 2) tiv_2016 from unique_loc join Insurance on Insurance.lat = unique_loc.lat and Insurance.lon = unique_loc.lon
join multi_tiv_2015
on Insurance.tiv_2015 = multi_tiv_2015.tiv_2015;



/*
Notes:
    - The diff between MySQL & PostgreSQL is using (::decimal)
    - PostgreSQL won’t work for decimals without casting ➔ so using ::decimal is a must.
        - round(5)        -- returns 5 (no decimal, because it’s integer)
        - round(5.75)     -- returns 6
        - round(5.75, 1)  -- returns 5.8
*/