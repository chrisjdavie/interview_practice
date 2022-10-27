"""
Didn't figure this one out myself, had to read the provided solution.

I figured out the dominance relationship myself, but hadn't considered going left to right and right to left, using the widest solution, and considering that any future solution must have a higher height.

I don't know if I would have figured this out by staring at it, or how long that might have taken. I started at it for over an hour before looking at the solution.

I don't really know what these questions are for... ah well...
"""
import csv
from pathlib import Path

import pytest

class Solution():

    def maxArea(self, heights: list[int]) -> int:
    
        lhs_heights_iter = iter(enumerate(heights))
        rhs_heights_iter = iter(enumerate(heights[::-1]))

        largest_vol = 0
        lhs_ind, lhs_height = next(lhs_heights_iter)
        rhs_ind, rhs_height = next(rhs_heights_iter)

        while lhs_ind + rhs_ind < len(heights) - 1:

            largest_vol = max(
                largest_vol,
                (len(heights) - 1 - lhs_ind - rhs_ind)*min(lhs_height, rhs_height)
            )

            if lhs_height < rhs_height:
                lhs_ind, lhs_height = next(lhs_heights_iter)
            else:
                rhs_ind, rhs_height = next(rhs_heights_iter)

        return largest_vol


long_csv_path = Path(__file__).parent / "long.csv"
with long_csv_path.open("r") as long_csv_fh:
    long_heights = [int(val) for row in csv.reader(long_csv_fh) for val in row]

@pytest.mark.parametrize(
    "heights,expected_volume",
    (
        ([1, 1], 1),
        ([1,8,6,2,5,4,8,3,7], 49),
        (long_heights, 48762645),
    )
)
def test(heights, expected_volume):
    assert Solution().maxArea(heights) == expected_volume

