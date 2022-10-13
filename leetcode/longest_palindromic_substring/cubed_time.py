"""
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

https://leetcode.com/problems/longest-palindromic-substring/
"""
from unittest import TestCase

from parameterized import parameterized


class Solution():

    @staticmethod
    def _isAPalindrome(i: int, j: int, s: str) -> bool:
        
        for i_l, i_r in zip(range(i, j+1), range(j, i-1, -1)):
            if s[i_l] != s[i_r]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:

        i_longest_palindrome = 0
        j_longest_palindrome = 0
        len_longest_palindrome = 1

        for i in range(len(s)):
            for j in range(i, len(s)):
                len_substring = j - i + 1
                if len_substring > len_longest_palindrome and self._isAPalindrome(i, j, s):
                    i_longest_palindrome = i
                    j_longest_palindrome = j
                    len_longest_palindrome = len_substring

        return s[i_longest_palindrome: j_longest_palindrome+1]

class TestSolution(TestCase):

    @parameterized.expand([
        (0, 0, True),
        (0, 1, False),
        (0, 2, True)
    ])
    def testIsAPalindrome(self, i, j, expected_output):

        solution = Solution()

        self.assertEqual(
            solution._isAPalindrome(i, j, "aba"),
            expected_output
        )

    @parameterized.expand([
        ("", ""),
        ("babad", "bab"),
        ("cbbd", "bb")
    ])
    def testLongestPalindrome(self, input, expected_output):

        self.assertEqual(
            Solution().longestPalindrome(input),
            expected_output
        )
