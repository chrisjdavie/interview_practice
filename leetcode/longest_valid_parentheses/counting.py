from typing import Iterable

import pytest


class Solution:

    def longestValidParentheses(self, s: str) -> int:

        def _one_pass(s_loc: Iterable[str], open_brace: str, close_brace: str) -> int:

            count_open: int = 0
            count_close: int = 0

            max_len: int = 0

            for brace in s_loc:
                if brace == open_brace:
                    count_open += 1
                if brace == close_brace:
                    count_close += 1
                if count_open == count_close:
                    max_len = max((max_len, count_open + count_close))
                if count_close > count_open:
                    count_open = 0
                    count_close = 0

            return max_len

        # ha, learnt about `reversed` and that it calcs on the fly, so doesn't use more memoty than using indicies
        return max(
            _one_pass(s, "(", ")"), # forwards
            _one_pass(reversed(s), ")", "("), # backwards
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
