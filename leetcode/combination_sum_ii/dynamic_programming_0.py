from collections import Counter

import pytest


class Solution():

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        if target <= 0:
            return []

        dp: list[list[Counter[int,int]]] = [[] for _ in range(target)]

        cand_unique = sorted(set(candidates))
        for cand in cand_unique:
            if cand - 1 < len(dp):
                dp[cand - 1].append(Counter([cand]))

        cand_count = Counter(candidates)

        for i_targ in range(target):
            for cand in cand_unique:
                if i_targ >= cand:
                    for sol_prev in dp[i_targ - cand]:
                        if sol_prev[cand] < cand_count[cand] and cand >= max(sol_prev.keys()):
                                sol_i = sol_prev.copy()
                                sol_i[cand] += 1
                                dp[i_targ].append(sol_i)

        return [list(sol.elements()) for sol in dp[-1]]


@pytest.mark.parametrize(
    "candidates,target,expected",
    (
        ([], 8, []),
        ([1], 1, [[1]]),
        ([2], 2, [[2]]),
        ([1,2], 3, [[1,2]]),
        ([1,1], 2, [[1,1]]),
        ([2], 4, []),
        ([1,1,2], 2, [[1,1], [2]]),
        ([], -2, [])
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
