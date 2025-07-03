-- Problem: Find Followers Count
-- Link: https://leetcode.com/problems/find-followers-count/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select user_id, count(follower_id) followers_count from Followers group by user_id order by user_id;