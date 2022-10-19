import pytest
import pytest

class Solution:

    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if not s:
            return 0
        
        result_str: str = "" 
        if (s[0] == "-" or s[0] == "+") and len(s) > 1 and s[1].isdigit():
            result_str = s[0]
            s = s[1:]

        for letter in s:
            if not letter.isdigit():
                 break
            result_str += letter

        result_int = int(result_str) if result_str else 0
        result_int = min(result_int, 2**31 - 1)
        result_int = max(result_int, -2**31)

        return result_int

@pytest.mark.parametrize(
    "test_input,expected", [
        ("1", 1),
        ("    22", 22),
        (".", 0),
        ("", 0),
        ("+32", 32),
        ("2147483648", 2**31 - 1),
        ("-2147483649", -2**31),
        ("+-12", 0),
        ("-+12", 0)
    ]
)
def test(test_input, expected):
    assert Solution().myAtoi(test_input) == expected

