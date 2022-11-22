"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
import pytest


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
    
        prev_num: int = -101
        prev_ind: int = -1
    
        for num in nums:
            if num != prev_num:
                prev_ind += 1
                nums[prev_ind], prev_num = num, num

        return prev_ind + 1


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

