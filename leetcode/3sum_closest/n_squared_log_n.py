"""
Made a failing test for excluded numbers
"""
import bisect
import csv
from collections import Counter
from itertools import combinations, combinations_with_replacement
from pathlib import Path
from typing import Optional

import pytest


class Solution:

    @staticmethod
    def _findNearest(nums: list[int], target: int, excluded_nums: Optional[set[int]] = None) -> int:
        """
        nums must be sorted
        """
        if excluded_nums is None:
            excluded_nums = {}

        i_high = bisect.bisect_left(nums, target)
        i_low = i_high - 1

        # handle excluded nums
        while i_low >= 0 and nums[i_low] in excluded_nums:
            i_low -= 1
        while i_high < len(nums) and nums[i_high] in excluded_nums:
            i_high += 1

        if i_low < 0:
            return nums[i_high]
        if i_high >= len(nums):
            return nums[i_low]
        if target - nums[i_low] > nums[i_high] - target:
            return nums[i_high]
        return nums[i_low]

    def threeSumClosest(self, nums: list[int], target: int) -> int:

        nums_counter = Counter(nums)
        nums_sorted = sorted(nums_counter.keys())

        closest = 10**5
        for num_0, num_1 in combinations_with_replacement(nums_sorted, 2):
            if num_0 == num_1 and nums_counter[num_0] < 2:
                continue

            excluded_nums = set()
            if nums_counter[num_0] < 2:
                excluded_nums.add(num_0)
            if nums_counter[num_1] < 2:
                excluded_nums.add(num_1)

            num_2 = self._findNearest(
                nums_sorted, 
                target - (num_0 + num_1),
                excluded_nums = excluded_nums
            )
            if abs(closest - target) > abs((trip_sum := num_0 + num_1 + num_2) - target):
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
        ([1, 0, 0, 0], 1, 1),
    )
)
def test_threeSumClosest(nums, target, expected_closest):
    assert Solution().threeSumClosest(nums, target) == expected_closest


@pytest.mark.parametrize(
    "target,nearest_expected",
    ((6,5),(10,11),(0,1),(14,13)),
)
def test_findNearest(target, nearest_expected):
    nums = [1,5,11,13]
    assert Solution._findNearest(nums, target) == nearest_expected


@pytest.mark.parametrize(
    "excluded_nums,target,expected_nearest",
    (({2}, 2, 1), ({1,2}, 2, 4))
)
def test_findNearest_excluded_nums(excluded_nums, target, expected_nearest):
    nums = [1, 2, 4, 5]
    assert Solution._findNearest(nums, target, excluded_nums) == expected_nearest


def test_findNearest_excluded_nums_many_low():
    excluded_nums = {0, 1, 2}
    target = 2
    nums = [0, 1, 2, 10, 99]
    assert Solution._findNearest(nums, target, excluded_nums) == 10


def test_findNearest_excluded_nums_many_high():
    excluded_nums = {97, 98, 99}
    target = 97
    nums = [0, 1, 97, 98, 99]
    assert Solution._findNearest(nums, target, excluded_nums) == 1

