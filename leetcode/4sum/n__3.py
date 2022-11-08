"""
Using dicts, typical is O(N**3), think there's a worst-case O(N**4) cos there's the linear case when keys clash, but should be very unusual - dict key'd to integers
"""
import csv
from collections import Counter
from pathlib import Path
from itertools import combinations

import pytest


class Solution:

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        count_nums: Counter = Counter(nums)

        results = set()
        for comb in combinations(nums, 3):
            if (num_3 := (target - sum(comb))) in count_nums:
                cand_comb = tuple(sorted(comb + (num_3,)))
                count_comb = Counter(cand_comb)

                if all(val_count <= count_nums[val] for val, val_count in count_comb.items()):
                    results.add(cand_comb)
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

