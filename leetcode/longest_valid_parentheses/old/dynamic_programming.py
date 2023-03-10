# Bleh, so I've come up with a way to work this. But who knows if it's the sensible
# way, I'm not very good at bottom-up memoization
import pytest


class Solution:

    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        prev_lengths: list[int] = [0]*len(s)

        for i_close, brace in enumerate(s):
            if brace == ")":
                # calc i_open
                # nested braces "((()))"
                i_open = i_close - prev_lengths[i_close - 1] - 1
                if i_open >= 0 and s[i_open] == "(":
                    # adjacent braces "()()"
                    i_open -= prev_lengths[i_open - 1]
                    if s[i_open] == "(":
                        prev_lengths[i_close] = i_close - i_open + 1
        return max(prev_lengths)


@pytest.mark.parametrize(
    "braces,length_valid",
    (
        ("", 0),
        ("()", 2),
        ("(()", 2),
        (")()", 2),
        ("())(", 2),
        ("(())", 4),
        ("()()", 4),
        ("())()", 2),
        ("(()())", 6),
        (")", 0),
        ("())())", 2),
    )
)
def test_longest_valid_parentheses(braces, length_valid):

    assert Solution().longestValidParentheses(braces) == length_valid
