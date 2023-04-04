import pytest


class Solution:

    def longestValidParentheses(self, s: str) -> int:

        max_len: int = 0
        opening_stack: list[int] = [-1] # -1 the starting point of current set of braces

        for ind, paren in enumerate(s):
            if paren == "(":
                opening_stack.append(ind)
            else:
                opening_stack.pop()
                if opening_stack:
                    max_len = max((ind - opening_stack[-1], max_len))
                else:
                    opening_stack.append(ind)

        return max_len


@pytest.mark.parametrize(
    "braces,expected_length",
    (
        ("", 0),
        ("()", 2),
        ("(()", 2),
        (")()", 2),
        ("(()))()", 4),
        ("(()())", 6)
    )
)
def test_longestValidParentheses(braces, expected_length):

    assert Solution().longestValidParentheses(braces) == expected_length
