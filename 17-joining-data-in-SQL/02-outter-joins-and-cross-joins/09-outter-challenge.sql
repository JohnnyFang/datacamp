/*
Outer challenge

Now that you're fully equipped to use outer joins, try a challenge problem to test your knowledge!

In terms of life expectancy for 2010, determine the names of the lowest five countries and their regions.
Instructions
100 XP

    Select country name AS country, region, and life expectancy AS life_exp.
    Make sure to use LEFT JOIN, WHERE, ORDER BY, and LIMIT.
*/
-- Select fields
SELECT c.name as country, region, p.life_expectancy as life_exp
-- From countries (alias as c)
from countries as c
  -- Join to populations (alias as p)
  left join populations as p
    -- Match on country code
    on c.code=p.country_code
-- Focus on 2010
where year=2010
-- Order by life_exp
order by life_expectancy
-- Limit to 5 records
limit 5;
