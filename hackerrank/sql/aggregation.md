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
