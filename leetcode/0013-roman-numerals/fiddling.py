from unittest import TestCase

from parameterized import parameterized


NUMERAL_INT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:

        s_rev = s[::-1]
        running_total = NUMERAL_INT[s_rev[0]]

        for num_0, num_1 in zip(s_rev[:-1], s_rev[1:]):
            if NUMERAL_INT[num_0] <= NUMERAL_INT[num_1]:
                running_total += NUMERAL_INT[num_1]
            else:
                running_total = running_total - NUMERAL_INT[num_1]

        return running_total


class TestRomanToInt(TestCase):

    @parameterized.expand([
        ("I", 1),
        ("V", 5),
        ("II", 2),
        ("IV", 4),
        ("VI", 6),
        ("LV", 55),
        ("MCM", 1900),
        ("MCMXIV", 1914)
    ])
    def test_goes(self, NUMERAL_INT, integers):

        solution = Solution()
        self.assertEqual(solution.romanToInt(NUMERAL_INT), integers)

    # @parameterized.expand([
    #     ("III", 3),
    #     ("IV", 4),
    #     ("IX", 9),
    #     ("LVIII", 58),
    #     ("MCMXIV", 1994)
    # ])
    # def test_examples(self, NUMERAL_INT, integers):

    #     solution = Solution()

    #     self.assertEqual(solution.romanToInt(NUMERAL_INT), integers)
