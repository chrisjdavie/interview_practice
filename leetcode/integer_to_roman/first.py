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

class Solution:

    def _intToRoman(self, num: int, key_nums: list[int]) -> str:
        this_key: int = key_nums.pop()
        denom: int = num//this_key
        remain: int = num%this_key
        remain_numeral: str = ""
        if remain:
            remain_numeral: str = self._intToRoman(remain, key_nums)
        return INTEGERS_TO_NUMERALS[this_key]*denom + remain_numeral


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
    )
)
def test(test_int, expected_roman):
    assert Solution().intToRoman(test_int) == expected_roman

