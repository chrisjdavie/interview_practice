"""
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
import pytest


class Solution:

    def searchInsert(self, nums: list[int], target: int) -> int:

        lo: int = 0
        hi: int = len(nums)
        mid: int = (lo + hi)//2

        while lo < hi and nums[mid] != target:
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
            mid = (lo + hi)//2

        return mid


@pytest.mark.parametrize(
    "nums,target,expected_output",
    (
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 1, 0),
        ([1,3,5,6,9], 9, 4),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 7, 4),
        ([], 3, 0),
    )
)
def test(nums, target, expected_output):

    assert Solution().searchInsert(nums, target) == expected_output
