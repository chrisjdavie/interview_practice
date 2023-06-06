"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

----------------

I mean, the below is almost certainly not what they were hoping for, but also, I'd argue exactly how you should do it
in Python, unless you want it very fast, but then why Python?
"""
import bisect

import pytest


class Solution:

    def searchRange(self, nums: list[int], target: int) -> list[int]:

        lhs_ind = bisect.bisect_left(nums, target)
        if len(nums) <= lhs_ind or nums[lhs_ind] != target:
            return [-1, -1]

        rhs_ind = bisect.bisect_right(nums, target, lo=lhs_ind)
        return [lhs_ind, rhs_ind - 1]


@pytest.mark.parametrize(
    "nums,target,expected_result",
    (
        ([5,7,7,8,8,10], 8, [3, 4]), # leetcode test
        ([5,7,7,8,8,10], 6, [-1, -1]), # leetcode test
        ([], 0, [-1, -1]), # leetcode test
        ([1], 2, [-1, -1]), # rhs bounds
        ([1, 2, 3], 2, [1, 1]), # single value
    )
)
def test(nums, target, expected_result):

    assert Solution().searchRange(nums, target) == expected_result
