"""
Normally, iterating using indicies rather that iterating on the objects
is less clear. But in the original solution (single_pass), there are
two indicies and one iterating over the list. This is inconsistent
and, to my eyes, less clear than this approach.

This method explicitally shows the "swapping" of items, and the
progression of the indicies, making it clearer what is going on
"""
from collections import Counter
from typing import List
from unittest import TestCase

from parameterized import parameterized


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind_zeros, ind_ones, ind_twos = 0, 0, len(nums) - 1
        while ind_ones <= ind_twos:
            if nums[ind_ones] == 0:
                nums[ind_zeros], nums[ind_ones] = nums[ind_ones], nums[ind_zeros]
                ind_zeros += 1
                ind_ones += 1
            elif nums[ind_ones] == 1:
                ind_ones += 1
            elif nums[ind_ones] == 2:
                nums[ind_ones], nums[ind_twos] = nums[ind_twos], nums[ind_ones]
                ind_twos -= 1

class TestSortColors(TestCase):

    @parameterized.expand([
        ([2, 2], [2, 2]),
        ([2, 2, 2], [2, 2, 2]),
        ([0, 1], [0, 1]),
        ([1, 0], [0, 1]),
        ([2, 1], [1, 2]),
        ([2, 0], [0, 2]),
        ([2, 2, 0], [0, 2, 2]),
        ([2, 1, 0], [0, 1, 2]),
        ([2, 2, 2, 1], [1, 2, 2, 2]),  # simplified regression 1,
        ([2, 2, 0, 1], [0, 1, 2, 2]),  # simplified regression 1,
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([0, 2, 2, 2, 0, 2, 1, 1], [0, 0, 1, 1, 2, 2, 2, 2])  # regression 1
    ])
    def test_sorts(self, colors, expected_colors):

        solution = Solution()
        solution.sortColors(colors)

        self.assertEqual(
            colors, expected_colors
        )
