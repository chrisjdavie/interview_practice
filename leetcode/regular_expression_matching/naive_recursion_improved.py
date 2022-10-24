import pytest

class Solution:

    @staticmethod
    def _matchChar(s_i: str, p_j: str) -> bool:
        if p_j == ".":
            return True
        else:
            return s_i == p_j

    def isMatch(self, s: str, p: str) -> bool:

        if not s and not p:
            return True
        if not p:
            return False          
        if len(p) > 1 and p[1] == "*":
            if self.isMatch(s, p[2:]):
                return True
            if s and self._matchChar(s[0], p[0]) and self.isMatch(s[1:], p):
                return True
            return False
        if not s:
            return False 
        return self._matchChar(s[0], p[0]) and self.isMatch(s[1:], p[1:])


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

