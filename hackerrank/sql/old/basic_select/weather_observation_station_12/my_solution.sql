/*
https://www.hackerrank.com/challenges/weather-observation-station-12/problem

Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
*/
SELECT DISTINCT city
FROM station
WHERE LOWER(LEFT(city, 1)) NOT IN ('a', 'e', 'i', 'o', 'u')
    AND LOWER(RIGHT(city, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
