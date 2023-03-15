import pytest


class Solution:

    def _isValid(self, s: str, i_start: int, i_end: int) -> bool:

        count_open: int = 0
        count_close: int = 0

        for brace in s[i_start:i_end]:
            if brace == "(":
                count_open += 1
            if brace == ")":
                count_close += 1
            if count_close > count_open:
                return False
        return count_open == count_close

    def longestValidParentheses(self, s: str) -> int:

        max_len: int = 0
        for i in range(0, len(s)):
            for j in range(i + 2, len(s) + 1, 2):
                if self._isValid(s, i, j):
                    max_len = max([max_len, j-i])
        return max_len


@pytest.mark.parametrize(
    "string,expected_length",
    [
        ("", 0),
        ("()", 2),
        ("(", 0),
        ("(())", 4),
        ("())", 2),
        ("(()", 2),
        (")()(", 2),
    ]
)
def test(string, expected_length):
    assert Solution().longestValidParentheses(string) == expected_length
