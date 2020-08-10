"""
This approach is the most straightforwards, but was discouraged by
leetcode
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
        counts = Counter(nums)
        new_nums = (i for i in [0, 1, 2] for _ in range(counts[i]))

        for i, n in enumerate(new_nums):
            nums[i] = n


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
