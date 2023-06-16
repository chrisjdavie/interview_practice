## Advanced Select SQL questions on hackerrank

Revisiting cos I got them wrong last time

## The PADS

https://www.hackerrank.com/challenges/the-pads

> 1. Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
> 2. Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:
>
> `There are a total of [occupation_count] [occupation]s.`
>
> where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.
>
> Note: There will be at least two entries in the table for each type of occupation.

```
SELECT CONCAT(Name, '(', SUBSTRING(Occupation, 1, 1), ')') FROM OCCUPATIONS ORDER BY Name;
SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.') FROM OCCUPATIONS GROUP BY Occupation ORDER BY COUNT(*), Occupation;`
```

## Type of Triangle

https://www.hackerrank.com/challenges/what-type-of-triangle

> Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:
>
> Equilateral: It's a triangle with 3 sides of equal length.
> Isosceles: It's a triangle with 2 sides of equal length.
> Scalene: It's a triangle with sides of differing lengths.
> Not A Triangle: The given values of A, B, and C don't form a triangle.

```
SELECT
    CASE
        WHEN A + B <= C OR B + C <= A OR C + B <= A THEN "Not A Triangle"
        WHEN A = B AND B = C THEN "Equilateral"
        WHEN A = B OR B = C OR A = C THEN "Isosceles"
        ELSE "Scalene"
    END
FROM TRIANGLES;
```
