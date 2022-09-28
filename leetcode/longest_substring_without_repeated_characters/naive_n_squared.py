"""
Given a string s, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
from unittest import TestCase

from parameterized import parameterized


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_substring = 0
        for i, _ in enumerate(s):
            seen_chars = set()
            for j, observed_char in enumerate(s[i:]):
                if observed_char in seen_chars:
                    if j > longest_substring:
                        longest_substring = j
                    break
                seen_chars.add(observed_char)
            else:
                # all characters are unique
                if j + 1 > longest_substring:
                    longest_substring = j + 1

        return longest_substring


class Test(TestCase):

    @parameterized.expand([
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("abc", 3),
    ])
    def test(self, input_string, expected_result):

        actual_result = Solution().lengthOfLongestSubstring(input_string)

        self.assertEqual(expected_result, actual_result)
