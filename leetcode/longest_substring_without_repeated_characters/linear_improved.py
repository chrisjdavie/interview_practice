"""
Given a string s, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
from collections import defaultdict
from typing import Iterator, Tuple
from unittest import TestCase

from parameterized import parameterized


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        current_start = 0
        longest_substring = 1
        last_seen_index = defaultdict(lambda: -1) # interestingly, using defaultdict makes this twice as long to run as {} in leetcode
        for i, letter in enumerate(s):
            if last_seen_index[letter] >= current_start:
                longest_substring = max(i - current_start, longest_substring)
                current_start = last_seen_index[letter] + 1
            last_seen_index[letter] = i

        return max(i - current_start + 1, longest_substring)


class Test(TestCase):

    @parameterized.expand([
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("aaabc", 3),
        ("", 0),
    ])
    def test(self, input_string, expected_result):

        actual_result = Solution().lengthOfLongestSubstring(input_string)

        self.assertEqual(expected_result, actual_result)
