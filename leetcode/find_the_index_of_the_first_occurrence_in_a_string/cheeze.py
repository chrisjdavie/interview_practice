"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
import pytest

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


@pytest.mark.parametrize(
    "haystack,needle,expected_ind",
    (
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("gggrouppppppppppppp", "group", 2), 
    )
)
def test(haystack, needle, expected_ind):

    assert expected_ind == Solution().strStr(haystack, needle)

