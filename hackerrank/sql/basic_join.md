# Basic join queries, hackerrank

The 3rd subdomain in Hackerrank for SQL, practicing my SQL to get better and improve my chances at job interviews and to be able to go for interviews where strong SQL is needed.

## Population Census

https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true

Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

Note: CITY. CountryCode and COUNTRY. Code are matching key columns.

```
SELECT SUM(CITY.POPULATION)
FROM CITY
JOIN COUNTRY ON
    CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Asia';
```

## African Cities

https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true

Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

Note: CITY. CountryCode and COUNTRY. Code are matching key columns.

```
SELECT CITY.NAME
FROM CITY
JOIN COUNTRY
    ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Africa';
```

## Average Population of Each Continent

https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true

Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY. Continent) and their respective average city populations (CITY. Population) rounded down to the nearest integer.

Note: CITY. CountryCode and COUNTRY. Code are matching key columns.

```
SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population))
FROM COUNTRY
JOIN CITY
    ON COUNTRY.Code = CITY.CountryCode
GROUP BY COUNTRY.Continent;
```

## The Report

https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true

Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

Write a query to help Eve.

```
SELECT
    CASE
        WHEN Grades.Grade >= 8 THEN Students.Name
        ELSE NULL
    END,
    Grades.Grade,
    Students.Marks
FROM Students
JOIN Grades
    ON Students.Marks BETWEEN Grades.Min_Mark AND Grades.Max_Mark
ORDER BY Grades.Grade DESC, Students.Name;
```

## Top Competitors

https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true

Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

```
SELECT Submissions.hacker_id, Hackers.name
FROM Challenges
JOIN Difficulty
    ON Challenges.difficulty_level = Difficulty.difficulty_level
JOIN Submissions
    ON Submissions.challenge_id = Challenges.challenge_id AND Submissions.score = Difficulty.score
JOIN Hackers
    ON Submissions.hacker_id = Hackers.hacker_id
GROUP BY Submissions.hacker_id, Hackers.name
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, Submissions.hacker_id;
```
