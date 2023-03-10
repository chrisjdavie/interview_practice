import pytest

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        length: int = 0
        braces_stack: list[tuple[str, int]] = [-1]
        # set to -1 as start of potentially valid parentheses

        for i_brace, brace in enumerate(s):
            if brace == "(":
                braces_stack.append(i_brace)
            else:
                braces_stack.pop()
                if not braces_stack:
                    # reset on unclosed open
                    braces_stack.append(i_brace)
                else:
                    # closed parentheses, one of 
                    # - one before last open brace
                    # - unpaired open brace
                    # - start
                    length = max((length, i_brace - braces_stack[-1]))

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
