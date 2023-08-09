from collections import Counter

import pytest


class Solution:

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        cand_count = sorted(Counter(candidates).items())
        # cand_count = list(Counter(candidates).items()) # this breaks my tests, but leetcode says it's fine and a lot faster

        def _solve(i_cand: int, _target: int) -> list[list[int]]:
            if _target == 0:
                return [[]]
            if _target < 0 or i_cand == len(cand_count):
                return []

            results = []

            cand: int = cand_count[i_cand][0]
            count: int = cand_count[i_cand][1]

            for c in range(count + 1):
                for r in _solve(i_cand+1, _target-cand*c):
                    results.append([cand]*c + r)

            return results

        return _solve(0, target)


@pytest.mark.parametrize(
    "candidates,target,expected",
    (
        ([1], 1, [[1]]),
        ([1,2,3], 3, [[1,2], [3]]),
        ([1,2,7,1,5], 8, [[1,2,5],[1,7]]),
    )
)
def test_unit(candidates, target, expected):

    actual = Solution().combinationSum2(candidates, target)

    for e in expected:
        assert e in actual
    assert len(actual) == len(expected)


@pytest.mark.parametrize(
    "candidates,target,expected",
    (
        ([10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]]),
        ([2,5,2,1,2], 5, [[1,2,2],[5]]),
    )
)
def test_leetcode(candidates, target, expected):

    actual = Solution().combinationSum2(candidates, target)

    for e in expected:
        assert e in actual
    assert len(actual) == len(expected)
