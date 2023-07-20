"""
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

---------------------------

While this worked the first time, it kinda went a bit pear-shaped with corner cases I hadn't really considered, so I'm
trying again
"""
import pytest



class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:


        def _solve(i_start_cand: int, _target: int) -> list[list[int]]:
            results = []

            for i_cand, cand in enumerate(candidates[i_start_cand:]):
                for i_mult in range(1, _target//cand+1):
                    mult = i_mult*cand
                    if mult == _target:
                        results.append((i_mult)*[cand])
                    else:
                        for res in _solve(i_start_cand+i_cand+1, _target - mult):
                            results.append((i_mult)*[cand] + res)

            return results

        return _solve(0, target)


@pytest.mark.parametrize(
    "candidates,target,expected_combinations",
    (
        ([2], 1, []),
        ([2], 2, [[2],]),
        ([3], 6, [[3, 3],]),
        ([2, 3], 6, [[2, 2, 2], [3, 3]]),
        ([5,], 6, []),
        ([2, 4], 8, [[2, 2, 2, 2], [2, 2, 4], [4, 4]]),
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

