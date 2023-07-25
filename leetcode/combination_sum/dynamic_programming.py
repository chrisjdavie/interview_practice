"""
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

---------------------------

Reading other people's solutions, I didn't realise there was a bottom-up dynamic programming approach, and I'm fairly
weak at those, so I'll give it a shot
"""
import pytest



class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        dp: list[list[int]] = [[] for _ in range(target)]

        for i_t in range(target):
            for cand in candidates:
                if i_t == cand - 1:
                    dp[i_t].append([cand])
                if i_t - cand >= 0 and dp[i_t - cand]:
                    for r in dp[i_t - cand]:
                        if r[-1] <= cand:
                            dp[i_t].append(r + [cand])

        return dp[-1]


@pytest.mark.parametrize(
    "candidates,target,expected_combinations",
    (
        ([2], 1, []),
        ([2], 4, [[2, 2]]),
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


