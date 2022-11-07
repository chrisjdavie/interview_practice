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
    
        words_to_combine = [DIGITS_TO_LETTERS_MAP[digi] for digi in digits]
        
        inds_words = [0]*len(words_to_combine)

        results = []
        i=0
        while True:
            results.append("".join(w[i] for i, w in zip(inds_words, words_to_combine)))
            for i, w in enumerate(words_to_combine):
                if inds_words[i] == len(w) - 1:
                    inds_words[i] = 0
                    i += 1
                else:
                    break
            else:
                break
            inds_words[i] += 1
            i=0

        return results

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

