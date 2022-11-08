import csv
from collections import defaultdict, Counter
from pathlib import Path
from itertools import combinations

import pytest


class Solution:

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
    
        count_nums: Counter = Counter(nums)
        nums = [val for val, val_count in count_nums.items() for _ in range(min(4, val_count))]
        
        square_store: defaultdict[int, set[tuple[int, int]]] = defaultdict(set)
        
        results = set()
        for num_0, num_1 in combinations(nums, 2):
            sum_01 = num_0+num_1
            sum_23 = (target - sum_01)
            for num_2, num_3 in square_store[sum_23]:
                cand_comb = tuple(sorted([num_0, num_1, num_2, num_3]))
                if all(count_nums[val] >= count_comb for val, count_comb in Counter(cand_comb).items()):
                    results.add(cand_comb)
            square_store[sum_01].add(tuple(sorted((num_0, num_1))))

        return [list(comb) for comb in results]


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

