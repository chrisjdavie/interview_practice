import pytest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        for lhs, rhs in zip(str(x), str(x)[::-1]):
            if lhs != rhs:
                return False
        return True

@pytest.mark.parametrize(
    "test_number,expected",
    ((121, True), (123, False))
)
def test(test_number, expected):
    assert Solution().isPalindrome(test_number) == expected

