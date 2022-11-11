"""
Back tracking version of the algorithm.

In terms of figuring out the problem, I did it and found a decent enough way. In terms of interviewing it would have been a disaster - I was very non-linear about it, thinking about combinations, then closure, then stacks and suffs, and stacks and suffs was the first I implemented.

The correct approach for interviewing would be - brute force with combinations, the stacks, and then closures
"""
import pytest


class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        
        solns = [("(", 1, 1),]
        
        for _ in range(2*n - 1):
            new_solns = []
            for pref, suff_count, spent in solns:
                if spent < n:
                    new_solns.append((
                        pref + "(",
                        suff_count + 1,
                        spent + 1
                    ))
                if suff_count:
                    new_solns.append((
                        pref + ")",
                        suff_count - 1,
                        spent
                    ))
            solns = new_solns
        return [s[0] for s in solns]


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

