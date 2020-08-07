from typing import List
from unittest import TestCase

from parameterized import parameterized


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind_zeros = 0
        ind_twos = len(nums) - 1

        for this_ind, num_replace in enumerate(nums):
            nums[this_ind] = 1

            while num_replace == 2:
                num_replace = nums[ind_twos]
                nums[ind_twos] = 2
                ind_twos -= 1

            if num_replace == 0:
                nums[ind_zeros] = 0
                ind_zeros += 1

            if ind_twos <= this_ind:
                break


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
        ([2, 2, 2, 1], [1, 2, 2, 2]),  # simplified regression 1
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([0, 2, 2, 2, 0, 2, 1, 1], [0, 0, 1, 1, 2, 2, 2, 2])  # regression 1
    ])
    def test_sorts(self, colors, expected_colors):

        solution = Solution()
        solution.sortColors(colors)

        self.assertEqual(
            colors, expected_colors
        )
