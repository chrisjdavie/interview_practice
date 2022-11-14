import pytest


class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return [""]
        parens: list[str] = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    parens.append(f"({left}){right}")
        return parens


@pytest.mark.parametrize(
    "n,expected_parenthesis",
    (
        (4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]),
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (2, ["()()", "(())"]),
        (1, ["()"]),
        (0, [""]),
    )
)
def test(n, expected_parenthesis):
    actual_parenthesis = Solution().generateParenthesis(n)
    for exp in expected_parenthesis:
        assert exp in actual_parenthesis
    assert len(actual_parenthesis) == len(expected_parenthesis)

