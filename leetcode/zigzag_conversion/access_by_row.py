from itertools import zip_longest
from typing import Iterator
from unittest import TestCase

from parameterized import parameterized


class Solution:

    @staticmethod
    def _characterIndicies(lenS: int, numRows: int) -> Iterator[int]:
        cycle = 2*numRows - 2
        for j in range(numRows):
            for i in range(0, lenS - j, cycle):
                yield i + j
                cand = (i + j) + cycle - j*2
                if j != 0 and j != numRows-1 and cand < lenS:
                    yield cand

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
    
        ret = []
        for i in self._characterIndicies(len(s), numRows):
            ret.append(s[i])
        return "".join(ret)


class TestSolution(TestCase):

    @parameterized.expand([
        (7, 4, [0, 6, 1, 5, 2, 4, 3]),
        (5, 3, [0, 4, 1, 3, 2]),
        (4, 2, [0, 2, 1, 3]),
        (3, 3, [0, 1, 2]),
    ])
    def testChacterIndicies(self, lenS, numRows, expected_indicies):

        for expected_index, actual_index in zip_longest(
                expected_indicies, 
                Solution()._characterIndicies(lenS, numRows)):
            self.assertEqual(expected_index, actual_index)

    @parameterized.expand([
        ("ABC", 1, "ABC"),
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ])
    def testConvert(self, s, numRows, expected_output):

        self.assertEqual(
            Solution().convert(s, numRows),
            expected_output
        )

