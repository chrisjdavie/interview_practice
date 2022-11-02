"""
Naive n cubed solution - works but is too slow
"""
import csv
from itertools import combinations
from pathlib import Path

import pytest


class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        solution = {
            tuple(sorted(comb)) for comb in combinations(nums, 3) if sum(comb) == 0
        }
        return [list(comb) for comb in solution]

@pytest.mark.parametrize(
    "nums,expected_triplets",
    (
        ([0,1,1],[]),
        ([0,0,0],[[0,0,0]]),
        ([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]),
    )
)
def test(nums, expected_triplets):
    actual_triplets = Solution().threeSum(nums)
    actual_triplets_sorted = [sorted(trip) for trip in actual_triplets]

    for exp_trip in expected_triplets:
        assert exp_trip in actual_triplets_sorted
    assert len(expected_triplets) == len(actual_triplets)

