import pytest

import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
    
        lhs_tens = math.floor(math.log10(x))
        rhs_tens = 1
        
        lhs_remainder = x
        rhs_remainder = x
        for i in range((lhs_tens+1)//2):
            lhs_digit = lhs_remainder//10**(lhs_tens-i)
            rhs_digit = rhs_remainder%10
            if lhs_digit != rhs_digit:
                return False
            lhs_remainder = lhs_remainder%10**(lhs_tens-i)
            rhs_remainder = rhs_remainder//10
        return True

@pytest.mark.parametrize(
    "test_number,expected",
    ((121, True), (123, False), (1221, True), (1234, False), (-121, False), (12, False), (0, True))
)
def test(test_number, expected):
    assert Solution().isPalindrome(test_number) == expected

