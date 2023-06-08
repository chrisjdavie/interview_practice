"""
Turns out you can do this with way less code and more cleverness,
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/1054742/python-o-logn/,
but good cleverness, simplified solution

this is oddly close to my solution using inbuilts
"""
import pytest


class Solution():

    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def _search(_target: int) -> int:
            """
            returns the lhs most index for target
            """
            lo: int = 0
            hi: int = len(nums)
            while lo < hi:
                mid: int = (lo + hi)//2
                if nums[mid] < _target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        lo = _search(target)
        hi = _search(target+1)-1
        if lo <= hi:
            return [lo, hi]

        return [-1, -1]


@pytest.mark.parametrize(
    "nums,target,expected_result",
    (
        ([5,7,7,8,8,10], 8, [3, 4]), # leetcode test
        ([5,7,7,8,8,10], 6, [-1, -1]), # leetcode test
        ([], 0, [-1, -1]), # leetcode test
        ([1, 2, 3], 2, [1, 1]), # single value
    )
)
def test(nums, target, expected_result):

    assert Solution().searchRange(nums, target) == expected_result
