-- Problem: Movie Rating
-- Link: https://leetcode.com/problems/movie-rating/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
with top_user as
(select name from MovieRating MR join Users U on MR.user_id = U.user_id group by name order by count(rating) desc, name asc limit 1),
top_movie as
(select title from Movies M join MovieRating MR on M.movie_id = MR.movie_id and created_at >= '2020-02-01' and created_at < '2020-03-01' group by title order by avg(rating) desc, title asc limit 1)
select name as results from top_user
union all
select title from top_movie;


