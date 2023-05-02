# Basic Select SQL questions on hackerrank

Practising SQL, cos I'm a lot less confident in it and do worse on interviews on it than Python right now.

https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=select

I'm using MySQL unless I indicate otherwise in the question (sometimes the engine isn't running as expected, or the engine is misbehaving).

## Revising the Select Query

https://www.hackerrank.com/challenges/revising-the-select-query

> Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA. 

 `SELECT * FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION > 100000;`

## Revising the Select Query II

https://www.hackerrank.com/challenges/revising-the-select-query-2

> Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA. 

 `SELECT NAME FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION > 120000;`

## Select All

https://www.hackerrank.com/challenges/select-all-sql

> Query all columns (attributes) for every row in the CITY table.

 `SELECT * FROM CITY;`

## Select By ID

https://www.hackerrank.com/challenges/select-by-id

> Query all columns for a city in CITY with the ID 1661.

 `SELECT * FROM CITY WHERE ID = 1661;`

##  Japanese Cities' Attributes

https://www.hackerrank.com/challenges/japanese-cities-attributes

> Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

 `SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';`

## Japanese Cities' Names

https://www.hackerrank.com/challenges/japanese-cities-name

> Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN. 

 `SELECT NAME FROM CITY WHERE COUNTRYCODE = 'JPN';`

## Weather Observation Station 1

https://www.hackerrank.com/challenges/weather-observation-station-1

> Query a list of CITY and STATE from the STATION table. 

 `SELECT CITY, STATE FROM STATION;`

## Weather Observation Station 3

(2 is skipped, had a look at it, it's a chunk more complicated so probably why they put it later)

https://www.hackerrank.com/challenges/weather-observation-station-3

> Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer. 

 `SELECT DISTINCT CITY FROM STATION WHERE MOD(ID, 2) = 0;`

## Weather Observation Station 4

https://www.hackerrank.com/challenges/weather-observation-station-4

> Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table. 

 `SELECT (SELECT COUNT(CITY) FROM STATION) - (SELECT COUNT(DISTINCT CITY) FROM STATION);`

## Weather Observation Station 5

https://www.hackerrank.com/challenges/weather-observation-station-5

> Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically. 

```
SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY), CITY LIMIT 1;
SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC, CITY LIMIT 1;
```

(using DB2, the MySQL only supresses the headers for the first query, so the answer is not what hackerrank expects. If you ran MySQL in silent mode, I think this would work?)

## Weather Observation Station 6

https://www.hackerrank.com/challenges/weather-observation-station-6

> Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

**In all these answers, I played with cases and it seems MySQL is case insensitive for string matches in the engine being run by hackerrank. To make REGEXP case sensitive at least, cast the string to binary apparently...**

More pure SQL

```
SELECT DISTINCT CITY FROM STATION WHERE 
    CITY LIKE 'A%'
    OR CITY LIKE 'E%'
    OR CITY LIKE 'I%'
    OR CITY LIKE 'O%'
    OR CITY LIKE 'U%';
```

Using REGEX matching

 `SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[AEIOU]';`

Using SUBSTR and thinking about case sensitivity (didn't consider it cos names start with capital letters)

 `SELECT DISTINCT CITY FROM STATION WHERE SUBSTR(CITY, 1, 1) IN ('a', 'e', 'i', 'o', 'u');`

## Weather Observation Station 7

https://www.hackerrank.com/challenges/weather-observation-station-7

> Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

 `SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[aeiou]$';`

(You can also use the SUBSTR keyword, found in others submissions

( `SELECT DISTINCT(CITY) FROM STATION WHERE SUBSTR(REVERSE(CITY) , 1, 1) IN ('A', 'E', 'I', 'O', 'U');` )

## Weather Observation Station 8

https://www.hackerrank.com/challenges/weather-observation-station-8

> Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

 `SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[AEIOU].*[AEIOU]$';`

(Also, combine any of questions 6 and 7 above with the `AND` keyword)

## Weather Observation Station 9

https://www.hackerrank.com/challenges/weather-observation-station-9

> Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

Turns out you can stick `NOT` in front of `REGEXP`

 `SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '^[AEIOU]';`

I'd assume you can use `NOT` with any of the answers from question 6.

Also, negative `REGEXP` , which I'd forgotten how to do

 `SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^AEIOU]';`

## Weather Observation Station 10

https://www.hackerrank.com/challenges/weather-observation-station-10

> Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

 `SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP "[^AEIOU]$";`

## Weather Observation Station 11

https://www.hackerrank.com/challenges/weather-observation-station-11

> Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

 `SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP "^[AEIOU]" OR CITY NOT REGEXP "[AEIOU]$";`

Using regexp or ( `|` )

 `SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP "^[^AEIOU]|[^AEIOU]$";`

## Weather Observation Station 12

https://www.hackerrank.com/challenges/weather-observation-station-12

> Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

 `SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP "^[AEIOU]" AND CITY NOT REGEXP "[AEIOU]$";`

Using just regex (I got this wrong initially as I wanted an AND operator, but stack overflow pointed out that the AND operator is of course implicit in regex, which I of course kinda know but never thought about it like that)

 `SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP "^[^AEIOU].*[^AEIOU]$";`

## Higher Than 75 Marks

https://www.hackerrank.com/challenges/more-than-75-marks

> Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

 `SELECT NAME FROM STUDENTS WHERE MARKS > 75 ORDER BY SUBSTRING(NAME, -3), ID;`

## Employee Names

https://www.hackerrank.com/challenges/name-of-employees

> Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.

 `SELECT name FROM employee ORDER BY name;`

## Employee Salaries

https://www.hackerrank.com/challenges/salary-of-employees

> Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than $2000 per month who have been employees for less than 10 months. Sort your result by ascending employee_id.

 `SELECT name FROM employee WHERE salary > 2000 AND months < 10 ORDER BY employee_id;`
