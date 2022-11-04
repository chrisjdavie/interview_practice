from itertools import product

import pytest


DIGITS_TO_LETTERS_MAP = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        return [
            "".join(comb) for comb in product(
                *(DIGITS_TO_LETTERS_MAP[digi] for digi in digits)
            )
        ]


@pytest.mark.parametrize(
    "digits,expected_combinations",
    (
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"]),
    )
)
def test(digits, expected_combinations):
    actual_combinations = Solution().letterCombinations(digits)
    for comb in expected_combinations:
        assert comb in actual_combinations
    assert len(actual_combinations) == len(expected_combinations)

