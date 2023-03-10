/*
https://www.hackerrank.com/challenges/binary-search-tree-1/problem

You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.
*/
SELECT
    n, 
    CASE
        WHEN root_node THEN "Root"
        WHEN inner_node THEN "Inner"
        ELSE "Leaf"
    END
FROM (
    SELECT 
        n, 
        n IN(SELECT n FROM bst WHERE p IS NULL) root_node,
        n IN(SELECT p FROM bst WHERE p IS NOT NULL) inner_node
    FROM bst) temp
ORDER BY n
