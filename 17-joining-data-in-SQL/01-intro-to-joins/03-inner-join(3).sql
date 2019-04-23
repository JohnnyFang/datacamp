-- The ability to combine multiple joins in a single query is a powerful feature of SQL, e.g:

SELECT *
FROM left_table
  INNER JOIN right_table
    ON left_table.id = right_table.id
  INNER JOIN another_table
    ON left_table.id = another_table.id;


        -- Inner join countries (left) and populations (right) on the code and country_code fields respectively.
        -- Alias countries AS c and populations AS p.
        -- Select code, name, and region from countries and also select year and fertility_rate from populations (5 fields in total).
        -- 4. Select fields
        -- 4. Select fields

select c.code, c.name, c.region, p.year, p.fertility_rate
  -- 1. From countries (alias as c)
  from countries as c
  -- 2. Join with populations (as p)
  inner join populations as p
    -- 3. Match on country code
    on c.code = p.country_code

    -- Instructions 2/3
    --     Add an additional inner join with economies to your previous query by joining on code.
    --     Include the unemployment_rate column that became available through joining with economies.
    --     Note that year appears in both populations and economies, so you have to explicitly use e.year instead of year as you did before.
    -- 6. Select fields
    SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
      -- 1. From countries (alias as c)
      FROM countries AS c
      -- 2. Join to populations (as p)
      INNER JOIN populations AS p
        -- 3. Match on country code
        ON c.code = p.country_code
      -- 4. Join to economies (as e)
      INNER JOIN economies AS e
        -- 5. Match on country code
        ON c.code = e.code;

    -- Instructions 3/3
    -- Scroll down the query result and take a look at the results for Albania from your previous query. Does something seem off to you?
    -- The trouble with doing your last join on c.code = e.code and not also including year is that e.g. the 2010 value for fertility_rate is also paired with the 2015 value for unemployment_rate.
    -- Fix your previous query: in your last ON clause, use AND to add an additional joining condition. In addition to joining on code in c and e, also join on year in e and p.

    -- 6. Select fields
    SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
      -- 1. From countries (alias as c)
      FROM countries AS c
      -- 2. Join to populations (as p)
      INNER JOIN populations AS p
        -- 3. Match on country code
        ON c.code = p.country_code
      -- 4. Join to economies (as e)
      INNER JOIN economies AS e
        -- 5. Match on country code and year
        ON c.code = e.code AND e.year = p.year;
