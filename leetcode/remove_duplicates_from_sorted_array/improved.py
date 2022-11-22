"""
Improved based on another solution - I don't think I've used itertools groupby before. Might have used the Pandas version though.

According to the documentation, this respects the memory requirements of the exercise,
but this does depend on the cPython implementation of groupby. But then all of these
requirements from the exercise rely on the cPython implementation of things, so that
might be more of a philosophical problem.

-------------------------

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from itertools import groupby

import pytest


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i, (k, _) in enumerate(groupby(nums)):
            nums[i] = k
        
        return i + 1


@pytest.mark.parametrize(
    "input_nums,expected_nums",
    (
        ([1,1,2],[1,2]),
        ([0,0,1,1,1,2,2,3,3,4],[0,1,2,3,4]),
    )
)
def test(input_nums, expected_nums):
    
    actual_len = Solution().removeDuplicates(input_nums)
    print(input_nums)
    for act_num, exp_num in zip(input_nums, expected_nums):
        assert act_num == exp_num
    assert actual_len == len(expected_nums)

