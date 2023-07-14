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
