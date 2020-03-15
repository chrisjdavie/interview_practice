/*
https://www.hackerrank.com/challenges/weather-observation-station-10/problem

Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
*/
SELECT DISTINCT city
FROM STATION
WHERE right(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u');