"""
More in line with what the question was hoping I think, I do this without Python in builts

---------------------------------

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
import pytest

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, _ in enumerate(haystack):
            if i + len(needle) > len(haystack):
                break
            for j, (h_letter, n_letter) in enumerate(zip(haystack[i:], needle)):
                if h_letter != n_letter:
                    break
            else:
                return i
        return -1


@pytest.mark.parametrize(
    "haystack,needle,expected_ind",
    (
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("gggrouppppppppppppp", "group", 2),
        ("za", "a", 1),
        ("a", "aa", -1),
        ("zzzza", "aa", -1),
    )
)



































def test(haystack, needle, expected_ind):

    assert expected_ind == Solution().strStr(haystack, needle)

