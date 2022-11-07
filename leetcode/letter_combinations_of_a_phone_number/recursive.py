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

    def dfs(self, words: list[str]) -> list[str]:
        if not words:
            return [""]

        lower = self.dfs(words[1:])
        
        results = []
        for letter in words[0]:
            for low_word in lower:
                results.append(letter + low_word)

        return results

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        words = [DIGITS_TO_LETTERS_MAP[digi] for digi in digits]

        return self.dfs(words)


@pytest.mark.parametrize(
    "digits,expected_combinations",
    (
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"]),
        ("3", ["d","e","f"]),
    )
)
def test(digits, expected_combinations):
    actual_combinations = Solution().letterCombinations(digits)
    for comb in expected_combinations:
        assert comb in actual_combinations
    assert len(actual_combinations) == len(expected_combinations)

