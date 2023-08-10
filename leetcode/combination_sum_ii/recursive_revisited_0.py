from collections import Counter

import pytest


class Solution():

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        cands_count = sorted(Counter(candidates).items())

        def _solve(i_cand: int, _target: int) -> list[list[int]]:
            if _target == 0:
                return [[]]
            if i_cand >= len(cands_count) or _target < 0:
                return []

            cand: int = cands_count[i_cand][0]
            c_count: int = cands_count[i_cand][1]

            results = []

            for num_cand in range(c_count + 1):
                for res in _solve(i_cand + 1, _target - cand*num_cand):
                    results.append([cand]*num_cand + res)
            return results

        return _solve(0, target)


@pytest.mark.parametrize(
    "candidates,target,expected",
    (
        ([], 8, []),
        ([1], 1, [[1]]),
        ([1,2], 3, [[1,2]]),
        ([1,2], 2, [[2]]),
        ([1,2,3,5], 6, [[1,5], [1,2,3]]),
        ([1,1], 1, [[1]]),
        ([2,1], 3, [[1,2]]),
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
