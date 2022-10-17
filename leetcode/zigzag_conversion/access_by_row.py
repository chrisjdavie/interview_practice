from unittest import TestCase

from parameterized import parameterized


class Solution:

    def convert(self, s: str, numRows: int) -> str:
        return "~"


class TestSolution(TestCase):

    @parameterized.expand([
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ])
    def testConvert(self, s, numRows, expected_output):

        self.assertEqual(
            Solution().convert(s, numRows),
            expected_output
        )

