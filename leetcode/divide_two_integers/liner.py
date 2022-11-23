"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 2**31 - 1, then return 231 - 1, and if the quotient is strictly less than -2**31, then return -2**31.
"""
import pytest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        negative: bool = (dividend > 0) is not (divisor > 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        running_total = divisor
        running_count = 1

        while running_total < dividend:
            running_total += divisor
            running_count += 1

        if running_total != dividend:
            running_count -= 1

        if negative:
            return -running_count
        return running_count


@pytest.mark.timeout(10)
@pytest.mark.parametrize(
    "dividend,divisor,expected_result",
    (
        (10, 3, 3),
        (1, 2, 0),
        (12, 3, 4),
        (18, 3, 6),
        (7, -3, -2),
        (-7, 3, -2),
        (-2147483648, -1, 2147483648),
    )
)
def test(dividend, divisor, expected_result):
    assert Solution().divide(dividend, divisor) == expected_result

