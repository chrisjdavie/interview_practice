/*
https://www.hackerrank.com/challenges/weather-observation-station-7/submissions/code/147514201

Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
*/
SELECT DISTINCT city 
FROM station 
WHERE city LIKE '%a' OR city LIKE '%e' OR city LIKE '%i' OR city LIKE '%o' OR city LIKE '%u';
