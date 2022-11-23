"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 2**31 - 1, then return 231 - 1, and if the quotient is strictly less than -2**31, then return -2**31.
"""
import pytest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        negative: bool = (dividend > 0) is (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)

        running_total: int = 0
        count_total: int = 0 

        while (running_total < dividend) or (running_total > (dividend + divisor)):

            running_total -= divisor
            count_total -= 1

            climber: int = divisor
            count_climber: int = 1

            while (running_total + climber) < dividend:

                climber += climber
                count_climber += count_climber

            running_total += climber
            count_total += count_climber

            running_total += divisor
            count_total += 1

            faller: int = divisor
            count_faller: int = 1
        
            while (running_total - faller) > (dividend + divisor):

                faller += faller
                count_faller += count_faller

            running_total -= faller
            count_total -= count_faller

        if running_total != dividend:
            count_total -= 1

        if negative:
            count_total = -count_total
        return max(-2**31, min(count_total, 2**31 - 1))

@pytest.mark.parametrize(
    "dividend,divisor,expected_result",
    (
        (1, 1, 1),
        (1, 2, 0),
        (10, 3, 3),
        (12, 3, 4),
        (18, 3, 6),
        (7, -3, -2),
        (-7, 3, -2),
        (17, 1, 17),
        (-2147483648, -1, 2147483647),
        (-2147483649, 1, -2147483648),
    )
)
def test(dividend, divisor, expected_result):
    assert Solution().divide(dividend, divisor) == expected_result

