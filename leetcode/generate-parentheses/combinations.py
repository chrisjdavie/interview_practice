from itertools import combinations
from typing import Iterator

import pytest


class Solution:

    @staticmethod
    def gen_all_combs(n: int) -> Iterator[str]:
        for indicies in combinations(range(2*n),n):
            parens: list[str] = ["("]*2*n
            for index in indicies:
                parens[index] = ")"
            yield "".join(parens)

    @staticmethod
    def _valid(parens: str) -> bool:
        count = 0
        for letter in parens:
            if letter == "(":
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return True

    def generateParenthesis(self, n: int) -> list[str]:
        return [comb for comb in self.gen_all_combs(n) if self._valid(comb)] 



@pytest.mark.parametrize(
    "n,expected_parenthesis",
    (
        (4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]),
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (2, ["()()", "(())"]),
        (1, ["()"]),
    )
)
def test(n, expected_parenthesis):
    actual_parenthesis = Solution().generateParenthesis(n)
    for exp in expected_parenthesis:
        assert exp in actual_parenthesis
    assert len(actual_parenthesis) == len(expected_parenthesis)


