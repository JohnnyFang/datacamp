SELECT c1.name AS city, c2.name AS country
FROM cities AS c1
INNER JOIN countries AS c2
ON c1.country_code = c2.code;


    -- Join the tables countries (left) and economies (right) aliasing countries AS c and economies AS e.
    -- Specify the field to match the tables ON.
    -- From this join, SELECT:
    --     c.code, aliased as country_code.
    --     name, year, and inflation_rate, not aliased.


-- 3. Select fields with aliases
SELECT c.code AS country_code, c.name, e.year, e.inflation_rate
FROM countries AS c
  -- 1. Join to economies (alias e)
  INNER JOIN economies as e
    -- 2. Match on code
    ON c.code = e.code;
