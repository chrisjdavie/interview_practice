import pytest


class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        len_longest_common_prefix = 0
        for chars in zip(*strs):
            if not all(chars[0] == c for c in chars[1:]):
                longest_common_prefix += chars[0]
            else:
                break
        return longest_common_prefix


@pytest.mark.parametrize(
    "words,expected_prefix",
    (
        (["flower","flow","flight"],"fl"),
        (["dog","racecar","car"], ""),
        (["ded", "dad"], "d"),
    )
)
def test(words, expected_prefix):
    assert Solution().longestCommonPrefix(words) == expected_prefix

