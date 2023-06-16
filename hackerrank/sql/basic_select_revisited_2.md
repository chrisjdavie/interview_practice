# Basic Select SQL questions on hackerrank

## Weather Observation Station 4

> Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table. 

 `SELECT (SELECT COUNT(CITY) FROM STATION) - (SELECT COUNT(DISTINCT CITY) FROM STATION)`

https://www.hackerrank.com/challenges/weather-observation-station-4

## Weather Observation Station 6

> Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

 `SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[AEIOU]';`

## Weather Observation Station 11

https://www.hackerrank.com/challenges/weather-observation-station-11

> Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

 `SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '^[AEIOU]' OR CITY NOT REGEXP '[AEIOU]$';`

## Higher Than 75 Marks

https://www.hackerrank.com/challenges/more-than-75-marks

> Query the Name of any student in STUDENTS who scored higher than Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

``
