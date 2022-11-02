"""
Naive n squared solution

Needed the optimisation of removing duplicates.

Initially I did this using itertools.combinations(nums_counter.keys(), repeat=2) instead
of itertools.product, but doing it with itertools.product moved the solution to less than
half the time
"""
import csv
from collections import Counter
from itertools import product
from pathlib import Path

import pytest


class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums_counter = Counter(nums)
        positives = {val for val in nums_counter.keys() if val > 0}
        negatives = {val for val in nums_counter.keys() if val < 0}

        solution = set()
        for pos, neg in product(positives, negatives):
            if (opp := -(pos + neg)) in nums_counter:
                if opp == pos or opp == neg:
                    if nums_counter[opp] < 2:
                        continue
                solution.add(tuple(sorted([neg, opp, pos])))

        if nums_counter[0] >= 3:
            solution.add((0,0,0))

        return [list(comb) for comb in solution]


long_nums_path = Path(__file__).parent / "long.csv"
long_soln_path = Path(__file__).parent / "long_solution.csv"

with long_nums_path.open("r") as nums_fh:
    long_nums = [int(val) for val in next(csv.reader(nums_fh))]

with long_soln_path.open("r") as soln_fh:
    long_soln = [[int(val) for val in row] for row in csv.reader(soln_fh)]

@pytest.mark.parametrize(
    "nums,expected_triplets",
    (
        ([0,1,1],[]),
        ([0,0,0],[[0,0,0]]),
        ([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]),
        ([0,0],[]),
        (long_nums, long_soln),
    )
)
def test(nums, expected_triplets):
    actual_triplets = Solution().threeSum(nums)
    actual_triplets_sorted = [sorted(trip) for trip in actual_triplets]

    for exp_trip in expected_triplets:
        assert exp_trip in actual_triplets_sorted
    assert len(expected_triplets) == len(actual_triplets)

