# so I didn't come up with this on my own, thou perhaps if I had done
# the brute force approach first I would have, it's very similar
# to the check on a string
import pytest


class Solution:

    def longestValidParentheses(self, s: str) -> int:

        count_seq_open: int = 0
        count_seq_close: int = 0

        count_nested_open: int = 0
        count_nested_close: int = 0

        max_len: int = 0

        for brace in s:
            if brace == "(":
                count_nested_open += 1
                count_seq_open += 1

                if count_nested_close > 0:
                    count_nested_open = 0
                    count_nested_close = 0

            if brace == ")":
                count_nested_close += 1
                count_seq_close += 1
            print()
            print(count_nested_close, count_nested_open)
            if count_nested_close > count_nested_open:
                count_nested_open = 0
                count_nested_close = 0
                count_seq_open = 0
                count_seq_close = 0

            print(count_seq_close)
            max_len = max((2*count_nested_close, max_len))
            if count_seq_open >= count_seq_close:
                max_len = max((2*count_seq_close, max_len))

            if count_nested_open == count_nested_close:
                count_nested_open = 0
                count_nested_close = 0                

        return max_len


@pytest.mark.parametrize(
    "braces,length_valid",
    (
        ("", 0),
        ("()", 2),
        ("(", 0),
        (")", 0),
        (")()", 2),
        ("())(())", 4),
        ("())", 2),
        ("((())", 4),
        ("()((())", 4),
        ("()()", 4),
        ("(()()", 4),
        ("(()(((()", 2)
    )    
)
def test_longest_valid_parentheses(braces, length_valid):
    assert Solution().longestValidParentheses(braces) == length_valid
