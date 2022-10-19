import pytest

class Solution:

    def myAtoi(self, s: str) -> int:
        leading_whitespace: bool = True
        
        result_str: str = ""
        for letter in s:
            if leading_whitespace:
                if letter == " ":
                    continue
                leading_whitespace = False

                # handling the unique case of the first letter being a sign
                if letter == "-" or letter == "+":
                    result_str += letter
                    continue
            if not letter.isdigit():
                 break
            result_str += letter

        if result_str and not result_str[-1].isdigit():
            result_str = ""

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

