import pytest

class Solution:

    def _isValid(self, s: str, i_lhs: int, i_rhs: int) -> bool:

        count_open: int = 0
        count_close: int = 0

        for brace in s[i_lhs:i_rhs]:
            if brace == "(":
                count_open += 1
            if brace == ")":
                count_close += 1
            # more closing braces than opening means this string isn't valid
            if count_close > count_open:
                break

        return count_open == count_close

    def longestValidParentheses(self, s: str) -> int:
        
        max_len: int = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self._isValid(s, i, j):
                    max_len = max((j - i, max_len))
        return max_len


@pytest.mark.parametrize(
    "braces,length_valid",
    (
        ("", 0),
        ("()", 2),
        ("(", 0),
        (")()", 2),
        ("())", 2),
        (")()(", 2),
        ("(()))()", 4)
    )
)
def test_longest_valid_parentheses(braces, length_valid):

    assert Solution().longestValidParentheses(braces) == length_valid
