"""
the dynamic programing version is 40x faster than the naive version 
"""
import pytest


class Solution:

    @staticmethod
    def _matchChar(s_i: str, p_j: str) -> bool:
        if p_j == ".":
            return True
        else:
            return s_i == p_j

    def _isMatchInner(self, s: str, p: str, i_s: int, j_p: int) -> bool:
        if i_s == len(s) and j_p == len(p):
            return True
        if j_p == len(p):
            return False
        if len(p) - j_p > 1 and p[j_p + 1] == "*":
            if self._isMatch(s, p, i_s, j_p + 2):
                return True
            for i_letter in range(i_s, len(s)):
                if not self._matchChar(s[i_letter], p[j_p]):
                    break
                if self._isMatch(s, p, i_letter + 1, j_p + 2):
                    return True
        if i_s == len(s):
            return False
        return self._matchChar(s[i_s], p[j_p]) and self._isMatch(s, p, i_s+1, j_p+1)

    def _isMatch(self, s: str, p: str, i_s: int, j_p: int) -> bool:
        if (i_s, j_p) not in self._cache:
            self._cache[(i_s, j_p)] = self._isMatchInner(s, p, i_s, j_p)

        return self._cache[(i_s, j_p)]

    def isMatch(self, s: str, p: str) -> bool:
    
        self._cache: dict[tuple[int, int], bool] = {}
    
        return self._isMatch(s, p, 0, 0)


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

