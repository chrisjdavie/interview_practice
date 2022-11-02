"""
This solution is *probably* more intuative from a code pov than first, but I'd argue
first is more intuative from the simplest solution pov
"""
import pytest


class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i_char, char in enumerate(strs[0]):
            for s in strs:
                if i_char == len(s) or s[i_char] != char:
                    return s[:i_char]
        return strs[0]

@pytest.mark.parametrize(
    "words,expected_prefix",
    (
        (["flower","flow","flight"],"fl"),
        (["dog","racecar","car"], ""),
        (["a", "a"], "a"),
        (["b", ""], ""),
    )
)
def test(words, expected_prefix):
    assert Solution().longestCommonPrefix(words) == expected_prefix

