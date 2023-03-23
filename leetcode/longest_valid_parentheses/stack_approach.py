import pytest


class Solution:

    def longestValidParentheses(self, s: str) -> int:

        return 0


@pytest.mark.parametrize(
    "braces,expected_length",
    (
        ("", 0),
        ("()", 2)
    )
)
def test_longestValidParentheses(braces, expected_length):

    assert Solution().longestValidParentheses(braces) == expected_length
