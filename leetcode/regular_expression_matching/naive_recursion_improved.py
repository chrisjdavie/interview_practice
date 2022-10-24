import pytest

class Solution:

    def isMatch(self, text: str, pattern: str) -> bool:

        if not pattern:
            return not text

        first_match: bool = bool(text) and (pattern[0] == text[0] or pattern[0] == ".")

        if len(pattern) > 1 and pattern[1] == "*":
            return self.isMatch(text, pattern[2:]) or (first_match and self.isMatch(text[1:], pattern))

        return first_match and self.isMatch(text[1:], pattern[1:])


@pytest.mark.parametrize(
    "test_string,pattern,expected",
    (
        ("a", "a", True),
        ("b", "a", False),
        ("aa", "ab", False),
        ("aa", "a*", True),
        ("ab", "a*", False),
        ("b", "a*b", True),
        ("b", "ba*", True),        
        ("ab", "a*b", True),
        ("aa", "a*b", False),
        ("ab", "a.*", True),
        ("z", ".", True),
        ("aa", "a", False),
        ("ab", ".*", True)
    )
)
def test(test_string, pattern, expected):
    assert Solution().isMatch(test_string, pattern) == expected

