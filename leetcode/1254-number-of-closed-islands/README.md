https://leetcode.com/problems/number-of-closed-islands/

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

## A subtle bug

The solution requires that you don't revisit previously visited grid points, but you can visit them in two ways - either via the first "trying to find an island" stage, or figuring out if two bits of land are connected.

For this to work, it requires that all connected bits of land are visted, and marked as visited, when the island is first explored.

I had the following code

    return (
        is_an_island(row_num+1, col_num),
        and is_an_island(row_num, col_num+1),
        and is_an_island(row_num-1, col_num),
        and is_an_island(row_num, col_num-1)
    )

But, if an earlier call to `is_an_island` returned `False`, then the check would stop and the others wouldn't be evaluated. They therefore wouldn't be marked as visted and could be visited later. But as any visited gridpoints returned `True` (as it didn't matter in the correct implemenation), later revists of not-islands (those connected to the walls) would say visited not-islands were actually islands. The solution was therefore to ensure the exploration always occured using `any`.

    return all([
        is_an_island(row_num+1, col_num),
        is_an_island(row_num, col_num+1),
        is_an_island(row_num-1, col_num),
        is_an_island(row_num, col_num-1)
    ])
