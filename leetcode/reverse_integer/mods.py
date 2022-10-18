import pytest

class Solution():
    def reverse(self, x: int) -> int:
                
        sign = 1 if x > 0 else -1

        tens = abs(x)
        sig_digits = []
        while tens > 0:
            sig_digits.append(tens%10)
            tens = tens//10

        result = 0
        for ten_power, digit in zip(range(len(sig_digits)-1, -1, -1), sig_digits):
            result += digit*10**ten_power
        result = sign*result
        if result >= 2**31 or result < -2**31:
            return 0
        return result

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (123, 321),
        (2345,5432),
        (-123, -321),
        (8463847412, 0),
        (9463847412, 0),
        (-9463847412, 0),
    ]
)
def test(test_input, expected):

    assert Solution().reverse(test_input) == expected

