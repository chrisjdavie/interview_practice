"""
Gives the right answer but takes way too long with the "long_heights" example.
"""
import csv
from pathlib import Path

import pytest


class Solution():

    def maxArea(self, heights: list[int]) -> int:

        max_vol = 0
        for i, height_i in enumerate(heights):
            for j, height_j in enumerate(heights[i+1:]):
                dist = j + 1
                vol = min(height_i, height_j)*dist
                max_vol = max(vol, max_vol)

        return max_vol


file_dir = Path(__file__).parent

with (file_dir/"long.csv").open("r") as csv_fh:
    long_heights = [int(val) for row in csv.reader(csv_fh) for val in row]

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

