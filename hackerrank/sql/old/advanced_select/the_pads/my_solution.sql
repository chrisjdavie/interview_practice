/*
https://www.hackerrank.com/challenges/the-pads/problem

Generate the following two result sets:

1. Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).

2. Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:

    There are a total of [occupation_count] [occupation]s.

    where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.

Note: There will be at least two entries in the table for each type of occupation.
*/
SELECT CONCAT(name, '(', LEFT(occupation, 1), ')') name_init
FROM occupations
ORDER BY name;
SELECT CONCAT("There are a total of ", occ_count, " ", LOWER(occupation), "s.")
FROM (
    SELECT o0.occupation, COUNT(*) occ_count
    FROM occupations AS o0
        JOIN (
        SELECT DISTINCT occupation
        FROM occupations
    ) o1
        ON o0.occupation = o1.occupation
    GROUP BY o0.occupation
    ORDER BY occ_count, o0.occupation
) temp;

