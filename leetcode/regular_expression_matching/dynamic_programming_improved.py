import pytest


class Solution:

    @staticmethod
    def _matchChar(s_i: str, p_j: str) -> bool:
        if p_j == ".":
            return True
        return s_i == p_j

    def isMatch(self, s: str, p: str) -> bool:

        _cache: dict[tuple[int, int], bool] = {}

        def _isMatch(i_s: int, j_p: int) -> bool:
            def _isMatchCacheEmpty(i_s: int, j_p: int) -> bool:
                if i_s == len(s) and j_p == len(p):
                    return True
                if j_p == len(p):
                    return False          
                if len(p) - j_p > 1 and p[j_p + 1] == "*":
                    if _isMatch(i_s, j_p + 2):
                        return True
                    if len(s) > i_s and self._matchChar(s[i_s], p[j_p]) and _isMatch(i_s + 1, j_p):
                        return True
                    return False
                if i_s == len(s):
                    return False 
                return self._matchChar(s[i_s], p[j_p]) and _isMatch(i_s + 1, j_p + 1)

            if (i_s, j_p) not in _cache:
                _cache[(i_s, j_p)] = _isMatchCacheEmpty(i_s, j_p)
            return _cache[(i_s, j_p)]

        return _isMatch(0, 0)

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

