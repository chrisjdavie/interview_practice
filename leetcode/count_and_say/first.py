"""
https://leetcode.com/problems/count-and-say/description/

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

- countAndSay(1) = "1"
- countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
"""

import pytest


class Solution:

    def say(self, number: str) -> str:
        said: list[str] = []

        current_num: str = number[0]
        num_count: int = 1

        for num in number[1:]:
            if num != current_num:
                said.append(str(num_count))
                said.append(current_num)
                current_num: str = num
                num_count: int = 0
            num_count += 1

        said.append(str(num_count))
        said.append(current_num)

        return "".join(said)


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
