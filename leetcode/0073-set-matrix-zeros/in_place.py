from itertools import product, zip_longest
from pprint import pprint
from typing import Generator, List, Tuple
from unittest import TestCase

from parameterized import parameterized


def indicies_spiral(len_m, len_n) -> Generator[Tuple[int, int], None, None]:

    top_inds = iter(range(len_m + 1))

    ind_prev = next(top_inds)

    print(ind_prev, len_m + 1)

    yield(ind_prev, ind_prev)

    ind_prev = next(top_inds)

    for m in range(ind_prev):
        yield(m, ind_prev)

    # for n in range(ind_prev - 1):
    #     yield(ind_prev, n)


class Solution:

    PLACEHOLDER = -1

    @staticmethod
    def _set_col_row_placeholder(zero_row: int, zero_col: int, matrix: List[List[int]]) -> None:
        for i, _ in enumerate(matrix[0]):
            if matrix[zero_row][i] != 0:
                matrix[zero_row][i] = Solution.PLACEHOLDER
        for j, _ in enumerate(matrix):
            if matrix[j][zero_col] != 0:
                matrix[j][zero_col] = Solution.PLACEHOLDER

    @staticmethod
    def _placeholder_to_zero(matrix: List[List[int]]) -> None:
        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                if matrix[i][j] == Solution.PLACEHOLDER:
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
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
        )
    ])
    def test_examples(self, matrix, expected_matrix):

        Solution().setZeroes(matrix)

        self.assertEqual(matrix, expected_matrix)
