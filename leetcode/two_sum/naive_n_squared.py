"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List
from unittest import TestCase


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        return []


class TestSolution(TestCase):

    def test(self):

        nums = [2, 7, 11, 15]
        target = 9

        expected_output = [0, 1]
        actual_output = Solution().twoSum(nums, target)

        self.assertListEqual(expected_output, actual_output)
