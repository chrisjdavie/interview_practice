# Hackerrank Advanced Select revisited

## New Companies

https://www.hackerrank.com/challenges/the-company

```
SELECT c.company_code, c.founder, COUNT(DISTINCT l.lead_manager_code), COUNT(DISTINCT s.senior_manager_code), COUNT(DISTINCT m.manager_code), COUNT(DISTINCT e.employee_code)
FROM Company c 
JOIN Lead_Manager l ON l.company_code = c.company_code 
JOIN Senior_Manager s ON s.company_code = c.company_code
JOIN Manager m ON m.company_code = c.company_code
JOIN Employee e ON e.company_code = c.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;
```

I did this alright, but forgot the interaction between GROUP BY and JOIN

## Type Of Triangle

https://www.hackerrank.com/challenges/what-type-of-triangle

```
SELECT
    CASE
        WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
        WHEN A = B AND B = C THEN 'Equilateral'
        WHEN A = B OR B = C OR C = A THEN 'Isosceles'
        ELSE 'Scalene'
    END
FROM TRIANGLES;
```

Think I might finally know how to CASE in SQL!
