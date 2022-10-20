import pytest

import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        tmp_x = x
        reversed_x = 0
        while tmp_x > 0:
            reversed_x = tmp_x%10 + reversed_x*10
            tmp_x = tmp_x//10

        return reversed_x == x


@pytest.mark.parametrize(
    "test_number,expected",
    ((121, True), (123, False), (1221, True), (1234, False), (-121, False), (12, False), (0, True))
)
def test(test_number, expected):
    assert Solution().isPalindrome(test_number) == expected

