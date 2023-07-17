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
