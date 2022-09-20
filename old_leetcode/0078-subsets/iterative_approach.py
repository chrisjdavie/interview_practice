"""
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

The not-too Pythonic "class Solution" is a leetcode thing
"""
from typing import List, Tuple
from unittest import TestCase


class Solution:
    def subsets(self, nums: List[int]) -> List[Tuple[int]]:

        all_subsets = [[]]

        for n in nums:
            all_subsets += [a_set + [n] for a_set in all_subsets]

        return all_subsets


class TestSolution(TestCase):

    def test_example(self):

        solution = Solution()

        nums = [1, 2, 3]

        expected_output = [
            [3, ],
            [1, ],
            [2, ],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]
        actual_output = solution.subsets(nums)

        for ss in expected_output:
            self.assertIn(ss, actual_output)
