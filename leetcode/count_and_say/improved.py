"""
I hadn't noticed this question was a reimplentation of Pythons `itertools.groupby`, so I'll do it using that

Inspired from others solutions
"""
from itertools import groupby

import pytest


class Solution:

    def say(self, number: str) -> str:

        return "".join(
            str(len(list(group))) + num for num, group in groupby(number)
        )


    def countAndSay(self, n: int) -> str:

        return_str: str = "1"

        for _ in range(n - 1):
            return_str: str = self.say(return_str)

        return return_str


@pytest.mark.parametrize(
    "number,expected_output",
    (
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("3322251", "23321511"),
    )
)
def test_say(number, expected_output):

    assert Solution().say(number) == expected_output


@pytest.mark.parametrize(
    "n,expected_output",
    (
        (1, "1"),
        (2, "11"),
        (3, "21"),
        (4, "1211"),
    )
)
def test_leetcode(n, expected_output):

    assert Solution().countAndSay(n) == expected_output

