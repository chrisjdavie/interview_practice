from unittest import TestCase

from parameterized import parameterized


class Solution():

    @staticmethod
    def _longestPalindromeFromIndicies(i: int, j: int, s: str) -> tuple[int, int]:

        # while i >= 0 and j < len(s):
        #     pass

        return (-1, -1)

    def longestPalindrome(self, s: str) -> str:
        return "~"


class TestSolution(TestCase):

    @parameterized.expand([
        (0, 0, (0, 0)),
        (1, 1, (0, 1)),
        (2, 2, (1, 2)),
        (3, 3, (3, 3)),
        (4, 4, (4, 4)),
    ])
    def testLongestPalindromeFromIndicies(self, i, j, expected_output):

        self.assertTupleEqual(
            Solution._longestPalindromeFromIndicies(i, j, "babad"),
            expected_output
        )


    @parameterized.expand([
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("", ""),
    ])
    def testLongestPalindrome(self, input_string, expected_output):

        self.assertEqual(
            expected_output,
            Solution().longestPalindrome(input_string)
        )


