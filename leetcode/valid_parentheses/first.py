"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    
https://leetcode.com/problems/valid-parentheses/
"""
import pytest

OPENING_CLOSING_PARENTHESES_MAP = {
    "(": ")",
    "{": "}",
    "[": "]",
}

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack: list[str] = []
        for letter in s:
            if letter in OPENING_CLOSING_PARENTHESES_MAP:
                parentheses_stack.append(letter)
            elif not parentheses_stack or letter != OPENING_CLOSING_PARENTHESES_MAP[parentheses_stack.pop()]:
                return False
        return not parentheses_stack


@pytest.mark.parametrize(
    "braces,expected_is_valid",
    (
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("[}(}", False),
        ("({})", True),
        (")", False),
        ("(", False),
    )
)
def test(braces, expected_is_valid):
    assert Solution().isValid(braces) == expected_is_valid

