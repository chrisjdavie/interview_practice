"""
https://leetcode.com/problems/number-of-closed-islands/

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

The not-too Pythonic "class Solution" is a hackerrank thing
"""
from typing import List, Optional
from unittest import TestCase


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        row_length = len(grid)
        column_length = len(grid[0])

        visted: List[List[Optional[bool]]] = [
            [False for _ in range(column_length)] for _ in range(row_length)
        ]

        def is_an_island(row_num: int, col_num: int) -> bool:
            if visted[row_num][col_num]:
                return True
            visted[row_num][col_num] = True

            if grid[row_num][col_num] == 0:
                if row_num == 0 or row_num == row_length - 1 or col_num == 0 or col_num == column_length - 1:
                    return False
                return all([
                    is_an_island(row_num+1, col_num),
                    is_an_island(row_num, col_num+1),
                    is_an_island(row_num-1, col_num),
                    is_an_island(row_num, col_num-1)
                ])
            return True

        islands_count = 0
        for row_num in range(1, row_length-1):
            for col_num in range(1, column_length-1):
                if grid[row_num][col_num] == 0 and not visted[row_num][col_num]:
                    islands_count += is_an_island(row_num, col_num)

        return islands_count


class TestSolution(TestCase):

    def setUp(self):

        self.solution = Solution()

    def test_island(self):

        grid = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 1)

    def test_border_alone(self):

        grid = [
            [1, 0, 1],
            [1, 1, 1]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 0)

    def test_border_transmits(self):

        grid = [
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 0)

    def test_border_transmits_2(self):

        grid = [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 0)

    def test_two_islands(self):

        grid = [
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 2)

    def test_considers_joins(self):

        grid = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 1)

    def test_regression(self):

        grid = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 1, 1]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 0)

    def test_example_1(self):

        grid = [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 2)

    def test_example_2(self):

        grid = [
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 1)

    def test_example_3(self):

        grid = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 2)

    def test_failure_1(self):

        grid = [
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        ]

        self.assertEqual(self.solution.closedIsland(grid), 5)
