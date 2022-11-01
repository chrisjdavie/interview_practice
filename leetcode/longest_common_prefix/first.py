import pytest


class Solution:

	def longestCommonPrefix(self, strs: list[str]) -> str:
	    return "~"


@pytest.mark.parametrize(
    "words,expected_prefix",
    (
        (["flower","flow","flight"],"fl"),
        (["dog","racecar","car"], ""),
    )
)
def test(words, expected_prefix):
    assert Solution().longestCommonPrefix(words) == expected_prefix

