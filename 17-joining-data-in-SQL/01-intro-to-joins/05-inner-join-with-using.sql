-- Inner join with using
--
-- When joining tables with a common field name, e.g.

SELECT *
FROM countries
  INNER JOIN economies
    ON countries.code = economies.code

-- You can use USING as a shortcut:

SELECT *
FROM countries
  INNER JOIN economies
    USING(code)

-- You'll now explore how this can be done with the countries and languages tables.

  -- Instructions
  --   Inner join countries on the left and languages on the right with USING(code).
  --   Select the fields corresponding to:
  --       country name AS country,
  --       continent name,
  --       language name AS language, and
  --       whether or not the language is official.
  --
-- Remember to alias your tables using the first letter of their names.

-- 4. Select fields
select c.name as country, continent, l.name as language, official
  -- 1. From countries (alias as c)
  from countries as c
  -- 2. Join to languages (as l)
  inner join languages as l
    -- 3. Match using code
    using(code)
