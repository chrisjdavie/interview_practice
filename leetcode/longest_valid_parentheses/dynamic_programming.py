from typing import Optional

import pytest


class Solution:

    def longestValidParentheses(self, s: str) -> int:

        dp_ind_open: list[int] = [None]*len(s)
        i_open: Optional[int] = None

        for i_close, brace in enumerate(s):
            if brace == ")":
                if dp_ind_open[i_close - 1] is not None:
                    i_open = dp_ind_open[i_close - 1] - 1
                else:
                    i_open = i_close - 1

                if i_open >= 0 and s[i_open] == "(":
                    if dp_ind_open[i_open - 1] is not None:
                        dp_ind_open[i_close] = dp_ind_open[i_open - 1]
                    else:
                        dp_ind_open[i_close] = i_open

        return max([0,] + [i_close - i_open + 1 for i_close, i_open in enumerate(dp_ind_open) if i_open is not None])


@pytest.mark.parametrize(
    "braces,length_valid",
    (
        ("", 0),
        ("()", 2),
        (")()", 2),
        ("(())", 4),
        ("()()", 4),
        ("(()())", 6),
        ("))", 0)
    )
)
def test_longestValidParentheses(braces, length_valid):

    assert Solution().longestValidParentheses(braces) == length_valid
