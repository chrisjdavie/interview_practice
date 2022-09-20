from itertools import product, zip_longest
from pprint import pprint
from typing import Generator, List, Tuple, Optional
from unittest import TestCase

from parameterized import parameterized


class Solution:

    PLACEHOLDER = None

    @staticmethod
    def _set_col_row_placeholder(zero_row: int, zero_col: int, matrix: List[List[Optional[int]]]) -> None:
        for i, _ in enumerate(matrix[0]):
            if matrix[zero_row][i] != 0:
                matrix[zero_row][i] = Solution.PLACEHOLDER
        for j, _ in enumerate(matrix):
            if matrix[j][zero_col] != 0:
                matrix[j][zero_col] = Solution.PLACEHOLDER

    @staticmethod
    def _placeholder_to_zero(matrix: List[Optional[int]]) -> None:
        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                if matrix[i][j] == Solution.PLACEHOLDER:
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[Optional[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                if matrix[i][j] == 0:
                    self._set_col_row_placeholder(i, j, matrix)
        self._placeholder_to_zero(matrix)


class TestSetZeroes(TestCase):

    @parameterized.expand([
        ([[0]], [[0]]),
        ([[0, 1]], [[0, 0]]),
        ([[1]], [[1]]),
        ([[0],
          [1]],
         [[0],
          [0]]),
        ([[1, 2],
          [3, 0]],
         [[1, 0],
          [0, 0]]),
        ([[1, 2],
          [0, 4]],
         [[0, 2],
          [0, 0]]),
        ([[0, 0],
          [3, 4]],
         [[0, 0],
          [0, 0]]),
    ])
    def test_building(self, matrix, expected_matrix):

        Solution().setZeroes(matrix)

        self.assertEqual(matrix, expected_matrix)

    @parameterized.expand([
        (
            [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]],
            [[1, 0, 1],
             [0, 0, 0],
             [1, 0, 1]]
        ),
        (
            [[0, 1, 2, 0],
             [3, 4, 5, 2],
             [1, 3, 1, 5]],
            [[0, 0, 0, 0],
             [0, 4, 5, 0],
             [0, 3, 1, 0]]
        ),
        (
            [[-1], [2], [3]],
            [[-1], [2], [3]]
        )  # Regression, -1 as an input
    ])
    def test_examples(self, matrix, expected_matrix):

        Solution().setZeroes(matrix)

        self.assertEqual(matrix, expected_matrix)
