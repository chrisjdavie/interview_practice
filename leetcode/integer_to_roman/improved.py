"""
Improved based on other users examples - I missed a property of the "exceptions"
that allows all of these to be merged into one simply
"""
import math

import pytest


# must be largest to smallest
INTEGERS_TO_NUMERALS_REF: list[tuple[int, str]] = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


class Solution:

    def intToRoman(self, num: int) -> str:

        numeral = ""
        
        for value, val_numeral in INTEGERS_TO_NUMERALS_REF:
            floor_div: int = num//value
            # this works as the "exceptions" (CM, CD, XC, XL, IV) only ever have 1
            # possible repetition - eg, if you have 2900, the 2,000 is taken out by
            # the M, leaving a single M            
            numeral += val_numeral*floor_div
            num = num%value
            
        return numeral
        

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

