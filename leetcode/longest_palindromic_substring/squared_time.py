from itertools import chain
from typing import Optional
from unittest import TestCase

from parameterized import parameterized


class Solution():

    @staticmethod
    def _longestPalindromeFromIndicies(i: int, j: int, s: str) -> Optional[tuple[int, int]]:

        i_longest = None
        j_longest = None

        for i, j in zip(range(i, -1, -1), range(j, len(s))):
            if s[i] != s[j]:
                break
            i_longest = i
            j_longest = j

        if i_longest is not None:
            return (i_longest, j_longest)
        return None

    def longestPalindrome(self, s: str) -> str:

        i_longest = 0
        j_longest = 0
        len_longest = 0

        for i, j in chain(zip(range(len(s)), range(len(s))), zip(range(len(s)-1), range(1,len(s)))):
            if inds := self._longestPalindromeFromIndicies(i, j, s):
                i_cand = inds[0]
                j_cand = inds[1]
                if j_cand - i_cand + 1 > len_longest:
                    i_longest = i_cand
                    j_longest = j_cand
                    len_longest = j_cand - i_cand + 1 

        return s[i_longest:j_longest+1]


class TestSolution(TestCase):

    @parameterized.expand([
        (0, 0, (0, 0)),
        (1, 1, (0, 2)),
        (2, 2, (1, 3)),
        (3, 3, (3, 3)),
        (4, 4, (4, 4)),
    ])
    def testLongestPalindromeFromIndiciesSameStart(self, i, j, expected_output):

        self.assertTupleEqual(
            Solution._longestPalindromeFromIndicies(i, j, "babad"),
            expected_output
        )

    @parameterized.expand([
        (0, 1, None),
        (1, 2, (1, 2)),
        (2, 3, None),
    ])
    def testLongestPalindromeFromIndiciesDiffStart(self, i, j, expected_output):

        self.assertEqual(
            Solution._longestPalindromeFromIndicies(i, j, "cbbd"),
            expected_output
        )

    @parameterized.expand([
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("", ""),
        ("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"),
    ])
    def testLongestPalindrome(self, input_string, expected_output):

        self.assertEqual(
            expected_output,
            Solution().longestPalindrome(input_string)
        )


