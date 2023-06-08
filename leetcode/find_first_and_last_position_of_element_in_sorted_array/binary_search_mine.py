import pytest


MAX_ARRAY_LENGTH = 100000

class Solution:

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not len(nums):
            return [-1, -1]

        lo: int = 0
        hi: int = len(nums) - 1
        mid: int = (lo + hi)//2

        # find if the target is in nums
        for _ in range(MAX_ARRAY_LENGTH):
            if lo > mid:
                break
            if nums[mid] == target:
                break
            if nums[mid] < target:
                lo = mid + 1
            if nums[mid] > target:
                hi = mid - 1
            mid = (lo + hi)//2
        else:
            assert False

        if nums[mid] != target:
            return [-1, -1]

        lo: int = 0
        hi: int = mid
        mid_lhs: int = (lo + hi)//2
        # find lhs position
        for _ in range(MAX_ARRAY_LENGTH):
            if (mid_lhs == 0 and nums[mid_lhs] == target) or (nums[mid_lhs - 1] != target and nums[mid_lhs] == target):
                break
            if nums[mid_lhs] != target:
                lo = mid_lhs + 1
            else:
                hi = mid_lhs - 1
            mid_lhs = (lo + hi)//2
        else:
            assert False

        # find rhs position
        lo: int = mid
        hi: int = len(nums) - 1
        mid_rhs: int = (lo + hi)//2
        # find lhs position
        for _ in range(MAX_ARRAY_LENGTH):
            if len(nums) <= mid_rhs + 1 or (nums[mid_rhs + 1] != target and nums[mid_rhs] == target):
                break
            if nums[mid_rhs + 1] == target:
                lo = mid_rhs + 1
            else:
                hi = mid_rhs - 1
            mid_rhs = (lo + hi)//2
        else:
            assert False

        return [mid_lhs, mid_rhs]


@pytest.mark.parametrize(
    "nums,target,expected_result",
    (
        ([5,7,7,8,8,10], 8, [3, 4]), # leetcode test
        ([5,7,7,8,8,10], 6, [-1, -1]), # leetcode test
        ([], 0, [-1, -1]), # leetcode test
        ([1], 2, [-1, -1]), # rhs bounds
        ([1, 2, 3], 2, [1, 1]), # single value
        ([2, 2, 3], 2, [0, 1]), # lhs bound
        ([1, 2, 2], 2, [1, 2]), # rhs bound
        ([1, 2, 2, 3, 4], 2, [1, 2]), # rhs bound
        ([2, 2], 2, [0, 1]), # rhs bound
        ([1, 4], 4, [1, 1]), # failed leetcode test
    )
)
def test(nums, target, expected_result):
    print(nums, target)
    assert Solution().searchRange(nums, target) == expected_result
