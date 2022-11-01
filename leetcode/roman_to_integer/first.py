import pytest


INTEGERS_NUMERALS: list[tuple[int, str]] = [
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


class Solution():

    def romanToInt(self, s: str) -> int:

        i_numeral = 0
        value = 0
        
        for val, val_numeral in INTEGERS_NUMERALS:
            while s.startswith(val_numeral, i_numeral):
                value += val
                i_numeral += len(val_numeral)

        return value


@pytest.mark.parametrize(
    "numeral,expected_int",
    [
        ("I", 1),
        ("II", 2),
        ("XIII", 13),
        ("XXII", 22),
        ("CM", 900),
        ("I", 1),
        ("VII", 7),
        ("XIII", 13),
        ("XXVII", 27),
        ("MDCXXVII", 1627),
        ("CIV", 104),
        ("CDIX", 409),
        ("MCMXCIV", 1994),
        ("LVIII", 58),
        ("CXLIII", 143),        
    ]
)
def test(numeral, expected_int):

    assert Solution().romanToInt(numeral) == expected_int

