"""
Works but takes too long
"""
import csv
from pathlib import Path
from itertools import combinations

import pytest


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closest = 10**5
        for triplet in combinations(nums, 3):
            if abs(closest - target) > abs((trip_sum := sum(triplet)) - target):
                closest = trip_sum
        return closest


long_fpath = Path(__file__).parent / "long.csv"
with long_fpath.open("r") as long_fh:
    reader = csv.reader(long_fh)
    long_nums = [int(val) for val in next(reader)]
    long_target = int(next(reader)[0])


@pytest.mark.parametrize(
    "nums,target,expected_closest",
    (
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([10**3, 10**3, 10**3], 3*10**3 + 2, 3*10**3),
        ([-10**3, -10**3, -10**3], 10**4, -3*10**3),
        (long_nums, long_target, -2952),
    )
)
def test(nums, target, expected_closest):
    assert Solution().threeSumClosest(nums, target) == expected_closest

