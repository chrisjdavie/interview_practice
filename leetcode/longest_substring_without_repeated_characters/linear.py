"""
Given a string s, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
from typing import Iterator, Tuple
from unittest import TestCase

from parameterized import parameterized


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        chars_in_substring: set[str] = set()
        result = 0

        lhs_iterator: Iterator[Tuple[int, str]] = enumerate(s)
        rhs_iterator: Iterator[Tuple[int, str]] = enumerate(s)
        lhs_index, lhs_char = next(lhs_iterator)
        rhs_index, rhs_char = next(rhs_iterator)

        try:
            while True:
                if rhs_char not in chars_in_substring:
                    chars_in_substring.add(rhs_char)
                    rhs_index, rhs_char = next(rhs_iterator)
                else:
                    result = max(rhs_index - lhs_index, result)
                    chars_in_substring.remove(lhs_char)
                    lhs_index, lhs_char = next(lhs_iterator)
        except StopIteration:
            result = max(rhs_index - lhs_index + 1, result)

        return result


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
