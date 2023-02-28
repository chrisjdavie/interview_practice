# This is based on a leetcode solution I wouldn't have thought of myself,
# I hadn't thought about the left-right symmetry of braces, and thus
# you can go left to right and right to left

# I think this works due to the following considerations
# - the left-right symmetry; any logic with opening and closing braces going left to right, must apply the other way 
#       round when going from right to left
# - in a valid set of parentheses, every opening brace must have a closing brace
# - at the start of a valid set of parentheses, there will be either the start of the string or more closing braces 
#       than opening
# The logic below is an implementation of the above arguments
import pytest


class Solution:

    def longestValidParentheses(self, s: str) -> int:

        max_len: int = 0

        def _search(s_order: str, open_brace: str, close_brace: str) -> None:
            nonlocal max_len

            count_open: int = 0
            count_close: int = 0

            # left to right
            for brace in s_order:
                if brace == open_brace:
                    count_open += 1
                if brace == close_brace:
                    count_close += 1
                if count_open == count_close:
                    max_len = max((max_len, 2*count_close))
                if count_close > count_open:
                    count_open = 0
                    count_close = 0

        _search(s, "(", ")")
        _search(s[::-1], ")", "(")

        return max_len


@pytest.mark.parametrize(
    "braces,length_valid",
    (
        ("", 0),
        ("()", 2),
        ("(", 0),
        (")", 0),
        ("())(())", 4),
        ("(()))()", 4),
        ("()((())", 4),
    )    
)
def test_longest_valid_parentheses(braces, length_valid):
    assert Solution().longestValidParentheses(braces) == length_valid
