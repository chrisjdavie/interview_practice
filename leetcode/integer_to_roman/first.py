import math

import pytest


# must be smallest to largest
INTEGERS_TO_NUMERALS = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}

EXCEPTIONS = {
    4: "IV",
    9: "IX",
    40: "XL",
    90: "XC",
    400: "CD",
    900: "CM",
}


class Solution:

    def _intToRoman(self, num: int, key_nums: list[int]) -> str:
        exception_numeral: str = ""   
        floor_div_numeral: str = ""
        remain_numeral: str = ""

        rank = 10**(math.floor(math.log10(num)))
        leading_num = (num//rank) * rank
        if leading_num in EXCEPTIONS:
            exception_numeral: str = EXCEPTIONS[leading_num]
            num -= leading_num

        this_key: int = key_nums.pop()

        floor_div: int = num//this_key
        remain: int = num%this_key

        remain_numeral: str = ""
        if remain:
            remain_numeral: str = self._intToRoman(remain, key_nums)

        floor_div_numeral = INTEGERS_TO_NUMERALS[this_key]*floor_div        

        return exception_numeral + floor_div_numeral + remain_numeral


    def intToRoman(self, num: int) -> str:
        return self._intToRoman(num, list(INTEGERS_TO_NUMERALS.keys()))


@pytest.mark.parametrize(
    "test_int,expected_roman",
    (
        (1,"I"),
        (7,"VII"),
        (13,"XIII"),
        (27,"XXVII"),
        (1627, "MDCXXVII"),
        (104, "CIV"),
        (409, "CDIX"),
        (1994, "MCMXCIV"),
        (58, "LVIII"),
        (143, "CXLIII"),
    )
)
def test(test_int, expected_roman):
    assert Solution().intToRoman(test_int) == expected_roman

