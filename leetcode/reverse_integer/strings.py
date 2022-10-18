import pytest

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        reversed = sign*int(str(abs(x))[::-1])
        if reversed > 2**31 - 1 or reversed < -2**31:
            return 0
        return reversed


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (123, 321), 
        (456, 654), 
        (-123, -321), 
        (8463847412, 0), 
        (-9463847412, 0)]
)
def test(test_input, expected):
    print(test_input)
    assert Solution().reverse(test_input) == expected

