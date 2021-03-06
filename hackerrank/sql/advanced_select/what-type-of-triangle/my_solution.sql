/*
https://www.hackerrank.com/challenges/what-type-of-triangle/problem

Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

- Equilateral: It's a triangle with 3 sides of equal length.
- Isosceles: It's a triangle with 2 sides of equal length.
- Scalene: It's a triangle with 3 sides of differing lengths.
- Not A Triangle: The given values of A, B, and C don't form a triangle.
*/
SELECT 
    IF(a + b <= c OR a + c <= b OR b + c <= a,
       "Not A Triangle",
       IF(a = b AND b = c,
         "Equilateral",
         IF(a = b OR a = c OR b = c,
            "Isosceles",
            "Scalene")))
FROM triangles;
