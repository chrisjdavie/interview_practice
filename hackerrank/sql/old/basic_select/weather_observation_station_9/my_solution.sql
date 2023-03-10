/*
https://www.hackerrank.com/challenges/weather-observation-station-9/problem

Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
*/
SELECT DISTINCT city
FROM station
WHERE LOWER(SUBSTRING(city,1,1)) NOT IN ('a', 'e', 'i', 'o', 'u');
