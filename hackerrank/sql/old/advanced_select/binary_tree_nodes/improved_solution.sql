/*
https://www.hackerrank.com/challenges/binary-search-tree-1/problem

You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.
*/
SELECT
    bst0.n, 
    CASE
        WHEN bst0.p IS NULL THEN "Root"
        WHEN EXISTS (
            SELECT TRUE
            FROM bst AS bst1 
            WHERE bst1.p = bst0.n) THEN "Inner"
        ELSE "Leaf"
    END
FROM bst AS bst0
ORDER by bst0.n
