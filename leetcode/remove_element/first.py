"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

https://leetcode.com/problems/remove-element/
"""
import pytest


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        ind_filtered: int = 0
        for n in nums:
            if n != val:
                nums[ind_filtered] = n
                ind_filtered += 1
        return ind_filtered


@pytest.mark.parametrize(
    "input_nums,val_remove,expected_nums",
    (
        ([3,2,2,3],3,[2,2]),
        ([0,1,2,2,3,0,4,2],2,[0,1,3,0,4]),
    )
)
def test(input_nums, val_remove, expected_nums):

    len_nums = Solution().removeElement(input_nums, val_remove)

    for act_num, exp_num in zip(input_nums, expected_nums):
        assert act_num == exp_num
    assert len_nums == len(expected_nums)

