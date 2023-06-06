# Basic select questions I messed up first time

## Weather Observation Station 4

https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true

`SELECT COUNT(city) - COUNT(DISTINCT(city)) FROM station;`

## Weather Observation Station 6

https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true

`SELECT city FROM station WHERE city REGEXP "^[aeiou]";`

## Weather Observation Station 11

https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true

`SELECT DISTINCT city FROM station WHERE NOT city REGEXP "^[aeiou]" OR NOT city REGEXP "[aeiou]$";`

## Weather Observation Station 12

https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true

`SELECT DISTINCT city FROM station WHERE NOT city REGEXP "^[aeiou]" AND NOT city REGEXP "[aeiou]$";`

Note: The reason I got this wrong the first time cos I was doing AND in RegEx and I got it right here cos I did it in SQL, which is probably the clearer way, on balance

## Higher than 75 Marks

https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true

`SELECT name FROM students WHERE marks > 75 ORDER BY SUBSTRING(name, -3), id;`
