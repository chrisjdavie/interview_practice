import pytest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

@pytest.mark.parametrize(
    "test_number,expected",
    ((121, True), (123, False))
)
def test(test_number, expected):
    assert Solution().isPalindrome(test_number) == expected

