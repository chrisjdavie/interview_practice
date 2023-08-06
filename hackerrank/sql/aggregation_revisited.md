# Aggregation SQL queries revisited, hackerrank

I got these wrong the first time, so this is me going through them again to make sure I've got it.

## Revising Aggregations - Averages

https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem?isFullScreen=true

Query the average population of all cities in CITY where District is California. 

```
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'California';
```

## The Blunder

https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true

Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's `0` ` key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: actual - average monthly salaries), and round it up to the next integer.

```
SELECT CEILING(AVG(Salary) - AVG(CAST(REPLACE(CAST(Salary AS CHAR),'0','') AS DECIMAL))) FROM EMPLOYEES;
```

## Top Earners

https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true

We define an employee's total earnings to be their salary * monthly worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as 2 space-separated integers.

```
SELECT salary*months total_earnings, COUNT(*)
FROM Employee
GROUP BY total_earnings
ORDER BY total_earnings DESC
LIMIT 1;
```

## Weather Observation Station 14

https://www.hackerrank.com/challenges/weather-observation-station-14/problem?isFullScreen=true

Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to 4 decimal places.

```
SELECT ROUND(MAX(LAT_N), 4) FROM STATION WHERE LAT_N < 137.2345;
```

## Weather Obervation Station 19

https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true

Consider `P_1(a,b)` and `P_2(c, d)` to be two points on a 2D plane where `(a, b)` are the respective minimum and maximum values of Northern Latitude (LAT_N) and `(c, d)` are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the Euclidean Distance between points `P_1` and `P_2` and format your answer to display decimal digits.

```
SELECT ROUND(SQRT(POWER(MIN(LAT_N) - MAX(LAT_N), 2) + POWER(MIN(LONG_W) - MAX(LONG_W), 2)), 4) FROM STATION;
```
