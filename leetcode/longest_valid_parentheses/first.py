import pytest

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        braces_stack: list[tuple[str, int]] = []
        complete_braces: list[tuple[int, int]] = []

        for i_brace, brace in enumerate(s):
            if braces_stack and braces_stack[-1][1] == "(" and brace == ")":
                i_open, _ = braces_stack.pop()
                complete_braces.append((i_open, i_brace))
            else:
                braces_stack.append((i_brace, brace))

        length: int = 0
        if complete_braces:
            i_open_prev, i_close_prev = complete_braces.pop()
            length = max((length, i_close_prev - i_open_prev + 1))
            for i_open, i_close in complete_braces[::-1]:
                if i_open_prev < i_open and i_close_prev > i_close: # encompass prev
                    pass
                elif i_close + 1 == i_open_prev: # adjacent to prev
                    i_open_prev = i_open
                else: # separate to prev
                    i_open_prev = i_open
                    i_close_prev = i_close
                length = max((length, i_close_prev - i_open_prev + 1))

        return length


@pytest.mark.parametrize(
    "braces,length_valid",
    (
        ("()", 2),
        ("(())", 4),
        ("(()", 2),
        ("())", 2),
        (")()())", 4),
        ("", 0),
        ("(()()", 4),
        ("())()", 2),
        ("()((())", 4)
    )
)
def test_longest_valid_parentheses(braces, length_valid):

    assert Solution().longestValidParentheses(braces) == length_valid
