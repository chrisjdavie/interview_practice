from typing import Iterable

import pytest


class Solution:

    def longestValidParentheses(self, s: str) -> int:

        def _one_pass(indicies: Iterable[int], open_brace: str, close_brace: str) -> int:

            count_open: int = 0
            count_close: int = 0

            max_len: int = 0

            for i_brace in indicies:
                if s[i_brace] == open_brace:
                    count_open += 1
                if s[i_brace] == close_brace:
                    count_close += 1
                if count_open == count_close:
                    max_len = max((max_len, count_open + count_close))
                if count_close > count_open:
                    count_open = 0
                    count_close = 0

            return max_len

        # passing the indicies here as doing s[::-1] creates a whole string in memory
        return max(
            _one_pass(range(len(s)), "(", ")"), # forwards
            _one_pass(range(len(s)-1, -1, -1), ")", "("), # backwards
        )


@pytest.mark.parametrize(
    "braces,expected_length",
    (
        ("", 0),
        ("()", 2),
        ("())", 2),
        (")()(", 2),
        ("(()))()", 4),
        ("(()", 2),
        ("(()())", 6) # redundant test, just to show it can
    )
)
def test_longest_valid_parentheses(braces, expected_length):

    assert Solution().longestValidParentheses(braces) == expected_length
