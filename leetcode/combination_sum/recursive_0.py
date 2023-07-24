"""
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

---------------------------

I decided not to do the obvious combinations implementations, might do it in a bit, it took me a moment to realise what I was trying to do is clearest
as a recursive solution. Would not have managed well in an interview situation with out 
"""
from collections import deque

import pytest


class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        def solve(target: int, cand_ind: int) -> list[list[int]]:

            results = []

            for cand in candidates[cand_ind:]:
                for i in range(1, target//cand + 1):
                    for res in solve(target - i*cand, cand_ind + 1):
                        results.append(i*[cand] + res)
                    if i*cand == target:
                        results.append(i*[cand])

            return results

        return solve(target, 0)


@pytest.mark.parametrize(
    "candidates,target,expected_combinations",
    (
        ([2], 1, []),
        ([2], 2, [[2]]),
        ([2], 4, [[2, 2]]),
        ([2, 4], 4, [[2, 2], [4]]),
        ([2, 3], 5, [[2, 3]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
    )
)
def test_unit(candidates, target, expected_combinations):

    result = Solution().combinationSum(candidates, target)

    for comb in expected_combinations:
        assert comb in result
    assert len(result) == len(expected_combinations)


@pytest.mark.parametrize(
    "candidates,target,expected_combinations",
    (
        ([2], 2, [[2]]),
        ([2,3], 7, [[2,2,3]]),
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2], 1, []),
    )
)
def test_leetcode(candidates, target, expected_combinations):

    result = Solution().combinationSum(candidates, target)

    for comb in expected_combinations:
        assert comb in result
    assert len(result) == len(expected_combinations)
