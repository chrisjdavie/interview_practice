import pytest


class Solution:

    def _isMatch(self, text: str, pattern: str) -> bool:

        def _isMatchCacheEmpty():
            if not pattern:
                return not text

            first_match: bool = bool(text) and (pattern[0] == text[0] or pattern[0] == ".")

            if len(pattern) > 1 and pattern[1] == "*":
                return self._isMatch(text, pattern[2:]) or (first_match and self._isMatch(text[1:], pattern))

            return first_match and self._isMatch(text[1:], pattern[1:])
            
        if (text, pattern) not in self._match_cache:
            self._match_cache[text, pattern] = _isMatchCacheEmpty()
        return self._match_cache[text, pattern]

    def isMatch(self, text: str, pattern: str) -> bool:

        self._match_cache: dict[tuple[str, str], bool] = {}
        
        return self._isMatch(text, pattern)


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

