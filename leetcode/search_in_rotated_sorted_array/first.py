# https://leetcode.com/problems/search-in-rotated-sorted-array/
import bisect

import pytest

class Solution:

    @staticmethod
    def _find_pivot_index(nums: list[int]) -> int:
        if len(nums) <= 1:
            # single length array
            return 0
        if nums[0] < nums[-1]:
            # pivot is at zero, no need to search
            return 0
        i_0: int = 0
        i: int = 1
        while True:
            if i_0 + i < len(nums) and nums[i_0] < nums[i_0+i]:
                i *= 2
            else:
                i_0, i = i_0 + i//2, 1
                if nums[i_0] > nums[i_0+i]:
                    break
        return i_0 + 1

    def search(self, nums: list[int], target: int) -> int:

        pivot_index: int = self._find_pivot_index(nums)

        i_candidate: int = 0
        if target >= nums[0] and target <= nums[pivot_index-1]:
            i_candidate: int = bisect.bisect_left(nums, target, hi=pivot_index)
        if target >= nums[pivot_index] and target <= nums[-1]:
            i_candidate: int = bisect.bisect_left(nums, target, lo=pivot_index)

        if nums[i_candidate] == target:
            return i_candidate
        return -1



@pytest.mark.parametrize(
    "nums,pivot_index",
    (
        ([0],0),
        ([0,1],0),
        ([4,1,2],1),
        ([3,4,1,2],2),
        ([3,4,5,0,1],3),
        ([4,5,6,7,0,1,2], 4),
        ([3,4,5,6,7,1], 5),
    )
)
def test__find_pivot_index(nums,pivot_index):
    assert Solution._find_pivot_index(nums) == pivot_index



@pytest.mark.parametrize(
    "nums,target,expected_result",
    (
        ([4,5,6,7,0,1,2],0,4),
        ([4,5,6,7,0,1,2],5,1),
        ([4,5,6,7,0,1,2],3,-1),
        ([1],0,-1)
    )
)
def test_leetcode(nums,target,expected_result):
    assert Solution().search(nums, target) == expected_result
