"""
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

https://leetcode.com/problems/longest-palindromic-substring/
"""
from itertools import zip_longest
from unittest import TestCase

from parameterized import parameterized


class Solution():

    @staticmethod
    def _generateIndex(len_s):
        for i in range(len_s):
            for j in range(len_s-i):
                yield (j, j + i)

    def longestPalindrome(self, s: str) -> str:

        i_longest_palindrome = 0
        j_longest_palindrome = 0
        len_longest_palindrome = 1

        is_palindrome = {}

        for i, j in self._generateIndex(len(s)):

            if (i + 1, j - 1) not in is_palindrome:
                is_palindrome[i, j] = s[i] == s[j]
            else:
                is_palindrome[i, j] = s[i] == s[j] and is_palindrome[i+1, j-1]

            len_substring = j - i + 1
            if len_substring > len_longest_palindrome and is_palindrome[i, j]:
                i_longest_palindrome = i
                j_longest_palindrome = j
                len_longest_palindrome = len_substring

        return s[i_longest_palindrome: j_longest_palindrome+1]


class TestSolution(TestCase):

    def test_index_generation(self):

        len_s = 3
        expected = [
            (0, 0),
            (1, 1),
            (2, 2),
            (0, 1),
            (1, 2),
            (0, 2)
        ]

        for pair_actual, pair_expected in zip_longest(Solution._generateIndex(len_s), expected):
            self.assertTupleEqual(pair_actual, pair_expected)


    @parameterized.expand([
        ("", ""),
        ("a", "a"),
        ("bb", "bb"),
        ("bab", "bab"),
        ("babad", "bab"),
        ("cbb", "bb"),
        ("cbbd", "bb")
    ])
    def testLongestPalindrome(self, input, expected_output):

        self.assertEqual(
            Solution().longestPalindrome(input),
            expected_output
        )
