SELECT *
FROM left_table
INNER JOIN right_table
ON left_table.id = right_table.id;

--1/3
SELECT *
FROM cities

-- 2/3
SELECT *
FROM cities
  -- 1. Inner join to countries
  INNER JOIN countries
    -- 2. Match on the country codes
    ON cities.country_code = country.code;

-- 3/3
-- 1. Select name fields (with alias) and region
SELECT cities.name as city, countries.name as country, countries.region
FROM cities
  INNER JOIN countries
    ON cities.country_code = countries.code;
