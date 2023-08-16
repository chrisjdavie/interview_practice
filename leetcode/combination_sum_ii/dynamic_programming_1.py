"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""
from collections import Counter

import pytest


class Solution():

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        if not candidates:
            return []

        dp: list[list[list[int]]] = [[] for _ in range(target)]
        cand_uniq = set(candidates)
        cand_count = Counter(candidates)

        for cand in cand_uniq:
            if cand <= target:
                dp[cand-1].append([cand])

        for i_t in range(target):
            for cand in cand_uniq:
                if cand <= i_t:
                    for sol in dp[i_t-cand]:
                        if sol[-1] <= cand and Counter(sol)[cand] < cand_count[cand]:
                            dp[i_t].append(sol + [cand])

        return dp[-1]


@pytest.mark.parametrize(
    "candidates,target,expected",
    (
        ([], 8, []),
        ([1], 1, [[1]]),
        ([3], 3, [[3]]),
        ([2,3], 3, [[3]]),
        ([2,3], 5, [[2,3]]),
        ([2,3,4], 9, [[2,3,4]]),
        ([2,2,3], 4, [[2,2]]),
        ([2,2], 2, [[2]]),
        ([2,2,4,4], 8, [[2,2,4], [4,4]])
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

