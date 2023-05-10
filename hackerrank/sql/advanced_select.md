# Advanced Select SQL questions on hackerrank

## The PADS

https://www.hackerrank.com/challenges/the-pads

```
SELECT CONCAT(name, "(", SUBSTRING(occupation, 1, 1), ")") FROM occupations ORDER BY name; 
SELECT CONCAT("There are a total of ", COUNT(occupation), " ", LOWER(occupation), "s.") FROM occupations GROUP BY occupation ORDER BY COUNT(occupation), occupation; `
```

## Type of Triangle

https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true

```
SELECT
    CASE
        WHEN a + b <= c OR b + c <= a OR c + b <= a THEN "Not A Triangle"
        WHEN a = b AND b = c THEN "Equilateral"
        WHEN a = b OR b = c OR a = c THEN "Isosceles"
        ELSE "Scalene"
    END
FROM triangles;
```
