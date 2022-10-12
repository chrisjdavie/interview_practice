"""
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

https://leetcode.com/problems/longest-palindromic-substring/
"""
from unittest import TestCase

from parameterized import parameterized


class Solution():

    def _isAPalindrome(self, i: int, j: int) -> bool:
        return False

    def longestPalindrome(self, s: str) -> str:

        self._s: str = s

        return "~"


class TestSolution(TestCase):

    @parameterized.expand([
        (0, 0, True),
        (0, 1, False),
        (0, 2, True)
    ])
    def testIsAPalindrome(self, i, j, expected_output):

        solution = Solution()
        solution._s = "aba"

        self.assertEqual(
            Solution()._isAPalindrome(i, j),
            expected_output
        )

    @parameterized.expand([
        ("babad", "bab"),
        ("cbbd", "bb")
    ])
    def test(self, input, expected_output):

        self.assertEqual(
            Solution().longestPalindrome(input),
            expected_output
        )
