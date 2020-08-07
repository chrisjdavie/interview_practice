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

        for this_ind, this_num in enumerate(nums):
            # nums[this_ind] = 1

            if this_num == 0:
                nums[ind_zeros] = 0
                ind_zeros += 1
            elif this_num == 2:
                nums[ind_twos] = 2
                ind_twos -= 1


class TestSortColors(TestCase):

    @parameterized.expand([
        ([0, 1, 2], [0, 1, 2]),
        ([2, 0, 2], [0, 2, 2]),
        ([2, 1, 0], [0, 1, 2])
    ])
    def test_sorts(self, colors, expected_colors):

        solution = Solution()
        solution.sortColors(colors)

        self.assertEqual(
            colors, expected_colors
        )

    # def test_example(self):

    #     colors = [2, 0, 2, 1, 1, 0]

    #     expected_output = [0, 0, 1, 1, 2, 2]

    #     solution = Solution()
    #     solution.sortColors(colors)

    #     self.assertEqual(
    #         colors, expected_output
    #     )
