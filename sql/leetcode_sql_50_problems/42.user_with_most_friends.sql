-- Problem: Friend Requests II: Who Has the Most Friends
-- Link: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
with all_users as 
(
select requester_id as id from RequestAccepted
union all
select accepter_id from RequestAccepted
)
select id, count(*) num from all_users group by id order by num desc limit 1;



/*
Notes:
    - Only the first alias "as id" matters for the result set.
    - You can skip the alias in the second SELECT—but for clarity, include it in the second select .
    - UNION ALL is faster than UNION since you don’t need to remove duplicates (which is correct here because friendships can appear multiple times).

*/