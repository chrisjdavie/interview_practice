# Aggregation SQL queries, hackerrank 

The 3rd subdomain in Hackerrank for SQL, practicing my SQL to get better and improve my chances at job interviews and to be able to go for interviews where strong SQL is needed.

https://www.hackerrank.com/domains/sql?filters%5Bstatus%5D%5B%5D=unsolved&filters%5Bsubdomains%5D%5B%5D=select&filters%5Bsubdomains%5D%5B%5D=advanced-select&filters%5Bsubdomains%5D%5B%5D=aggregation

## Revising Aggregations - The Count Function

https://www.hackerrank.com/challenges/revising-aggregations-the-count-function

Query a count of the number of cities in CITY having a Population larger than 100, 000. 

```
SELECT COUNT(*) FROM CITY WHERE POPULATION > 100000;
```

## Revising Aggregations - The Sum Function

https://www.hackerrank.com/challenges/revising-aggregations-sum/problem?isFullScreen=true

Query the total population of all cities in CITY where District is California. 

```
SELECT COUNT(*) FROM CITY WHERE POPULATION > 100000;
```

## Revising Aggregations - Averages

https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem?isFullScreen=true

Query the average population of all cities in CITY where District is California. 

```
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'California';
```

## Average Population

https://www.hackerrank.com/challenges/average-population/problem?isFullScreen=true

Query the average population for all cities in CITY, rounded down to the nearest integer.

```
SELECT FLOOR(AVG(POPULATION)) FROM CITY;
```

## Japan Population

https://www.hackerrank.com/challenges/japan-population/problem?isFullScreen=true

Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.

```
SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE = 'JPN';
```

## The Blunder

https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true

Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's `0` ` key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: actual - average monthly salaries), and round it up to the next integer.

```
SELECT CEILING(AVG(Salary) - AVG(CAST(REPLACE(CAST(Salary AS CHAR),'0','') AS DECIMAL))) FROM EMPLOYEES
```

## Top Earners

https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true

We define an employee's total earnings to be their salary * monthly worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as 2 space-separated integers.

```
SELECT salary*months AS total_earnings, COUNT(*)
FROM Employee
GROUP BY total_earnings
ORDER BY total_earnings DESC
LIMIT 1;
```

## Weather Observation Station 2

https://www.hackerrank.com/challenges/weather-observation-station-2/problem?isFullScreen=true

Query the following two values from the STATION table:

1. The sum of all values in LAT_N rounded to a scale of 2 decimal places.
2. The sum of all values in LONG_W rounded to a scale of 2 decimal places.

```
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) FROM STATION;
```

## Weather Observation Station 14

https://www.hackerrank.com/challenges/weather-observation-station-14/problem?isFullScreen=true

Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to 4 decimal places.

```
SELECT ROUND(LAT_N, 4) FROM STATION WHERE LAT_N < 137.2345 ORDER BY LAT_N DESC LIMIT 1;
```

## Weather Observation Station 15

https://www.hackerrank.com/challenges/weather-observation-station-15/problem?isFullScreen=true

Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to 4 decimal places.

```
SELECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N < 137.2345 ORDER BY LAT_N DESC LIMIT 1;
```

## Weather Observation Station 16

https://www.hackerrank.com/challenges/weather-observation-station-16/problem?isFullScreen=true

Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780. Round your answer to 4 decimal places.

```
SELECT ROUND(MIN(LAT_N), 4) FROM STATION WHERE LAT_N > 38.7780;
```

##  Weather Observation Station 17

https://www.hackerrank.com/challenges/weather-observation-station-17/problem?isFullScreen=true

Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. Round your answer to 4 decimal places.

```
SELECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N > 38.7780 ORDER BY LAT_N ASC LIMIT 1;
```

##  Weather Observation Station 18

https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true

Consider `P_1(a,b)` and `P_2(c, d)` to be two points on a 2D plane.

* `a` happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
* `b` happens to equal the minimum value in Western Longitude (LONG_W in STATION).
* `c` happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
* `d` happens to equal the maximum value in Western Longitude (LONG_W in STATION).

Query the Manhattan Distance between points `P_1` and `P_2` and round it to a scale of 4 decimal places.

```
SELECT ROUND(MAX(LAT_N) - MIN(LAT_N) + MAX(LONG_W) - MIN(LONG_W), 4) FROM STATION;
```

##  Weather Observation Station 19

https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true

Consider `P_1(a,b)` and `P_2(c, d)` to be two points on a 2D plane where `(a, b)` are the respective minimum and maximum values of Northern Latitude (LAT_N) and `(c, d)` are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the Euclidean Distance between points `P_1` and `P_2` and format your answer to display decimal digits.

```
SELECT ROUND(SQRT(POWER(MIN(LAT_N) - MAX(LAT_N), 2) + POWER(MIN(LONG_W) - MAX(LONG_W), 2)), 4) FROM STATION;
```
