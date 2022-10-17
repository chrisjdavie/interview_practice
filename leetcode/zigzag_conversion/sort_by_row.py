from collections import defaultdict
from itertools import count, zip_longest
from typing import Iterator 
from unittest import TestCase

from parameterized import parameterized


class Solution:

    @staticmethod
    def inputCoords(numRows: int, lenS: int) -> Iterator[tuple[int, int]]:

        def cols_iterator(numRows: int) -> Iterator[int]:
            columns: Iterator[int] = count()
            while True:
                for i in range(numRows):
                    yield i
                for i in range(numRows-2, 0, -1):
                    yield i

        for res, _ in zip(cols_iterator(numRows), range(lenS)):
            yield res

    def convert(self, s: str, numRows: int) -> str:

        # sort coords
        letters_array: list[list[str]] = [[] for _ in range(len(s))]
        
        for i_row, letter in zip(self.inputCoords(numRows, len(s)), s):
            letters_array[i_row].append(letter)

        # assemble string
        return "".join("".join(row) for row in letters_array)


class TestConvert(TestCase):

    @parameterized.expand([
        (2, 1, [0]),
        (4, 4, [0, 1, 2, 3]),
        (5, 7, [0, 1, 2, 3, 4, 3, 2]),
        (4, 7, [0, 1, 2, 3, 2, 1, 0]),
        (3, 6, [0, 1, 2, 1, 0, 1]),
        (2, 5, [0, 1, 0, 1, 0]),
    ])
    def testInputCoords(self, numRows, lenS, expected_output):

        for expected_pair, actual_pair in zip_longest(
                expected_output,
                Solution.inputCoords(numRows, lenS)):
            self.assertEqual(expected_pair, actual_pair)

    @parameterized.expand([
        ("PAYPALISHIRING", 1, "PAYPALISHIRING"),
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ])
    def testConvert(self, s, numRows, expected_output):

        self.assertEqual(
            Solution().convert(s, numRows),
            expected_output
        )

