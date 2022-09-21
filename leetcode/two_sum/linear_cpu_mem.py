"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import Dict, List
from unittest import TestCase

from parameterized import parameterized


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_index: Dict[int, int] = dict()

        for index, num in enumerate(nums):
            difference: int = target - num
            if difference in num_index:
                return [num_index[difference], index]
            num_index[num] = index

        return []


class TestSolution(TestCase):

    @parameterized.expand([
        ([9, 9], 9999, []),
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ])
    def test(self, nums, target, expected_output):

        actual_output = Solution().twoSum(nums, target)

        self.assertListEqual(expected_output, actual_output)

