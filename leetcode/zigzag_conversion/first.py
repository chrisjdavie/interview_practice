from itertools import count, zip_longest
from typing import Iterator 
from unittest import TestCase

from parameterized import parameterized


class Solution:

    @staticmethod
    def inputCoords(numRows: int, lenS: int) -> Iterator[tuple[int, int]]:

        def cols_iterator(numRows: int) -> Iterator[tuple[int, int]]:
            columns: Iterator[int] = count()
            while True:            
                this_column: int = next(columns)
                for i in range(numRows):
                    yield (i, this_column)
                for i in range(numRows-2, 0, -1):
                    yield (i, next(columns))       

        for res, _ in zip(cols_iterator(numRows), range(lenS)):
            yield res

    @staticmethod
    def outputCoords(numRows: int, lenS: int) -> Iterator[tuple[int, int]]:
        yield (-1, -1)

    def convert(self, s: str, numRows: int) -> str:
        return "~"


class TestConvert(TestCase):

    @parameterized.expand([
        (2, 1, [(0,0)]),
        (4, 4, [(0,0), (1,0), (2,0), (3,0)]),
        (5, 7, [(0,0), (1,0), (2,0), (3,0), (4,0), (3,1), (2,2)]),
        (4, 7, [(0,0), (1,0), (2,0), (3,0), (2,1), (1,2), (0,3)]),
        (3, 6, [(0,0), (1,0), (2,0), (1,1), (0,2), (1,2)]),
        (2, 5, [(0,0), (1,0), (0,1), (1,1), (0,2)]),
    ])
    def testInputCoords(self, numRows, lenS, expected_output):

        for expected_pair, actual_pair in zip_longest(
                expected_output,
                Solution.inputCoords(numRows, lenS)):
            self.assertEqual(expected_pair, actual_pair)

    @parameterized.expand([
        (2, 7, [(0,0), (0,3), (0,6), (1,0), (1, 2), (1, 3), (1, 5)]),
    ])
    def testOutputCoords(self, numRows, lenS, expected_output):
        
        for expected_pair, actual_pair in zip_longest(
                expected_output,
                Solution.outputCoords(numRows, lenS)):
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

