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
