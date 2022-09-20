"""
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

The not-too Pythonic "class Solution" is a leetcode thing

----------------

This solution is accurate, but it's not the approach they'd probably hope
for - there are a bunch of standard algorithms rather than recognising
that powersets are an iteration over combinations
"""
from itertools import combinations
from typing import List, Tuple
from unittest import TestCase


class Solution:
    def subsets(self, nums: List[int]) -> List[Tuple[int]]:
        all_subsets = []
        for i in range(len(nums) + 1):
            all_subsets += list(combinations(nums, i))
        return all_subsets


class TestSolution(TestCase):

    def test_example(self):
        """
        The example results provided by leetcode are typed 

        List[List[int]]

        but mine

        List[Tuple[int]]

        passes the tests
        """

        solution = Solution()

        nums = [1, 2, 3]

        expected_output = [
            (3,),
            (1,),
            (2,),
            (1, 2, 3),
            (1, 3),
            (2, 3),
            (1, 2),
            ()
        ]
        actual_output = solution.subsets(nums)

        for ss in expected_output:
            self.assertIn(ss, actual_output)
