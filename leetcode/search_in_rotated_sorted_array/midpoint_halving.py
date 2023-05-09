# https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
Having done the midpoint halving with both bisect (commented) and
done it manually, and in both cases it being a lot slower than
most solutions in leetcode, the answer is to do it in one pass,
rather than find the pivot - this makes sense, in that there's
some more complex logic that can handle both cases of finding
the pivot and searching, but it's much less clear, and this
works, so I'll stick with it like this.
"""
import bisect

import pytest


class Solution:

    @staticmethod
    def _find_pivot_index(nums: list[int]) -> int:

        lo = 0
        hi = len(nums) - 1

        if len(nums) == 1 or nums[lo] < nums[hi]:
            return 0

        while nums[lo + 1] > nums[lo]:
            mid = (lo + hi)//2
            if nums[mid] > nums[lo]:
                lo = mid
            else:
                hi = mid
        return lo + 1

    # def search(self, nums: list[int], target: int) -> int:

    #     pivot = self._find_pivot_index(nums)
    #     if nums[0] <= target and pivot != 0:
    #         index = bisect.bisect_left(nums, target, hi=pivot)
    #     else:
    #         index = bisect.bisect_left(nums, target, lo=pivot)

    #     if index < len(nums) and nums[index] == target:
    #         return index
    #     return -1

    def search(self, nums: list[int], target: int) -> int:

        pivot = self._find_pivot_index(nums)

        lo = 0
        hi = len(nums) - 1
        if nums[0] <= target and pivot != 0:
            hi=pivot
        else:
            lo=pivot

        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

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
def test_find_pivot(nums, pivot_index):

    assert Solution._find_pivot_index(nums) == pivot_index


@pytest.mark.parametrize(
    "nums,target,expected_result",
    (
        ([4, 5, 6, 1, 2, 3], 5, 1),
        ([4, 5, 6, 1, 2, 3], 2, 4),
        ([0], 0, 0),
        ([0], 1, -1),
        ([4,5,6,7,0,1,2],0,4),
        ([4,5,6,7,0,1,2],5,1),
        ([4,5,6,7,0,1,2],3,-1),
        ([1,3], 3, 1),
        ([3,1], 3, 0),
    ),
)
def test_search(nums, target, expected_result):
    assert Solution().search(nums, target) == expected_result
