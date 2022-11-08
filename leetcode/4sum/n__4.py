"""
As expected, n**4 direct solution takes too long
"""
import csv
from pathlib import Path
from itertools import combinations

import pytest


class Solution:

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        nums = sorted(nums)

        results: set[tuple[int]] = set()
        for comb in combinations(nums, 4):
            if sum(comb) == target:
                results.add(comb)
        return [list(res) for res in results]


long_csv_path = Path(__file__).parent/"long.csv"
with long_csv_path.open("r") as long_csv_fh:
    reader = csv.reader(long_csv_fh)
    long_nums = [int(num) for num in next(reader)]
    long_target = int(next(reader)[0])


@pytest.mark.parametrize(
    "nums,target,expected",
    (
        ([1,0,-1,0,-2,2],0,[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
        ([2,2,2,2,2],8,[[2,2,2,2]]),
        (long_nums,long_target,[]),
    )
)
def test(nums, target, expected):
    
    actual = Solution().fourSum(nums, target)
    
    for exp in expected:
        assert exp in actual
    assert len(expected) == len(actual)

