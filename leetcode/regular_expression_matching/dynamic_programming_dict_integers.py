import pytest

class Solution:

    def isMatch(self, text: str, pattern: str) -> bool:

        _match_cache: dict[tuple[int, int], bool] = {}

        def _isMatch(i_t: int, j_p: int) -> bool:

            def _isMatchCacheEmpty():
                if len(pattern) == j_p:
                    return len(text) == i_t

                first_match: bool = (
                    len(text) > i_t
                    and (pattern[j_p] == text[i_t] or pattern[j_p] == ".")
                )

                if len(pattern) > j_p + 1 and pattern[j_p + 1] == "*":
                    return _isMatch(i_t, j_p + 2) or (first_match and _isMatch(i_t + 1, j_p))

                return first_match and _isMatch(i_t + 1, j_p + 1)    

            if (i_t, j_p) not in _match_cache:
                _match_cache[(i_t, j_p)] = _isMatchCacheEmpty()
            return _match_cache[(i_t, j_p)]

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

