# Advanced Select hackerrank questions revisited cos I got them wrong last time

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
SELECT CONCAT(NAME, '(', SUBSTRING(OCCUPATION, 1, 1), ')') FROM OCCUPATIONS ORDER BY NAME;
SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(OCCUPATION), 's.' ) FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY COUNT(*), OCCUPATION;
```

## New Companies

https://www.hackerrank.com/challenges/the-company

> Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy: *image in URL*
>
> Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

My first go, once I read there were duplicate entries

```
SELECT Company.company_code, Company.founder, lead_manager_count.lead_manager_count, senior_manager_count.senior_manager_count, manager_count.manager_count, employee_count.employee_count
FROM Company
JOIN (
    SELECT COUNT(DISTINCT lead_manager_code) AS lead_manager_count, company_code FROM Lead_Manager GROUP BY company_code
) as lead_manager_count
ON Company.company_code = lead_manager_count.company_code
JOIN (
    SELECT COUNT(DISTINCT senior_manager_code) AS senior_manager_count, company_code FROM Senior_Manager GROUP BY company_code
) as senior_manager_count
ON Company.company_code = senior_manager_count.company_code
JOIN (
    SELECT COUNT(DISTINCT manager_code) AS manager_count, company_code FROM Manager GROUP BY company_code
) as manager_count
ON Company.company_code = manager_count.company_code
JOIN (
    SELECT COUNT(DISTINCT employee_code) AS employee_count, company_code FROM Employee GROUP BY company_code
) as employee_count
ON Company.company_code = employee_count.company_code
ORDER BY company_code;
```

After reading other solutions...

```
SELECT c.company_code, c.founder, COUNT(DISTINCT l.lead_manager_code), COUNT(DISTINCT s.senior_manager_code), COUNT(DISTINCT m.manager_code), COUNT(DISTINCT e.employee_code)
FROM Company c
JOIN Lead_Manager l
ON c.company_code = l.company_code
JOIN Senior_Manager s
ON c.company_code = s.company_code
JOIN Manager m
ON c.company_code = m.company_code
JOIN Employee e
ON c.company_code = e.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;
```

Which is much cleaner. I think I have a poor model in my head of what happens after join - looks like people see it as creating a single, giant table (which I guess it is). I also don't know why, if you use `GROUP BY` , you have to group by all the unique things selected by in the SELECT statement, it's interesting.
