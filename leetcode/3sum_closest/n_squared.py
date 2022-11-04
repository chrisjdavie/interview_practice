"""
This works, and I *think* I understand why it works, but it's def a new way of thinking
about how to use sorted numbers
"""
import csv
from pathlib import Path

import pytest


class Solution:

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closest = 10**5
        nums.sort()

        def range_val_gen(range_iter):
            for ind in range_iter:
                yield ind, nums[ind]        

        for i, num_i in enumerate(nums[:len(nums)-2]):
            small_to_large_iter = range_val_gen(range(i+1, len(nums)))
            large_to_small_iter = range_val_gen(range(len(nums)-1, i-1, -1))

            ind_s, num_s = next(small_to_large_iter)
            ind_l, num_l = next(large_to_small_iter)

            while ind_s < ind_l:
                sum_trip = num_i + num_s + num_l
                if sum_trip < target:
                    ind_s, num_s = next(small_to_large_iter)
                else:
                    ind_l, num_l = next(large_to_small_iter)

                if abs(target - sum_trip) < abs(target - closest):
                    closest = sum_trip

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
        (long_nums, long_target, -2952),
        ([-10**3, -10**3, -10**3], 10**4, -3*10**3),
    )
)
def test_threeSumClosest(nums, target, expected_closest):
    assert Solution().threeSumClosest(nums, target) == expected_closest


