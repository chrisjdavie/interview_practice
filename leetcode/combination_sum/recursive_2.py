"""
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

---------------------------

This was better the second time, but still wasn't super smooth, so try again until it is
"""

import pytest



class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        def _solve(ind_cand_start: int, _target: int) -> list[list[int]]:

            results: list[list[int]] = []

            for ind_cand, cand in enumerate(candidates[ind_cand_start:]):
                for i_mult in range(1, _target//cand + 1):
                    mult = i_mult*cand
                    if mult == _target:
                        results.append(i_mult*[cand])
                    else:
                        for r in _solve(ind_cand_start + ind_cand + 1, _target - mult):
                            results.append(i_mult*[cand] + r)

            return results

        return _solve(0, target)


@pytest.mark.parametrize(
    "candidates,target,expected_combinations",
    (
        ([2], 1, []),
        ([2], 2, [[2]]),
        ([3], 6, [[3, 3]]),
        ([2, 3], 6, [[2, 2, 2], [3, 3]]),
        ([2, 4], 8, [[2, 2, 2, 2], [2, 2, 4], [4, 4]])
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
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
        ([2], 1, []),
    )
)
def test_leetcode(candidates, target, expected_combinations):

    result = Solution().combinationSum(candidates, target)

    for comb in expected_combinations:
        assert comb in result
    assert len(result) == len(expected_combinations)


