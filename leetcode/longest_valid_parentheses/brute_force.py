import pytest

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return len(s)


@pytest.mark.parametrize(
    "braces,length_valid",
    (
        ("", 0),
        ("()", 2),
        ("(", 0)
    )
)
def test_longest_valid_parentheses(braces, length_valid):

    assert Solution().longestValidParentheses(braces) == length_valid
