import pytest

class Solution:

    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def _search(target: int) -> int:
                
            lo: int = 0
            hi: int = len(nums)

            while lo < hi:
                mid: int = (lo + hi)//2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        lo: int = _search(target)
        if nums and nums[lo] == target:
            hi: int = _search(target + 1) - 1
            return [lo, hi]

        return [-1, -1]


@pytest.mark.parametrize(
    "nums,target,expected",
    (
        ([], 0, [-1,-1]), # from leetcode    
        ([1, 2, 3], 2, [1, 1]),
        ([1, 2, 2, 2, 3], 2, [1, 3]),
        ([5,7,7,8,8,10], 8, [3,4]), # from leetcode
        ([5,7,7,8,8,10], 6, [-1,-1]) # from leetcode
    )
)
def test(nums, target, expected):

    assert Solution().searchRange(nums, target) == expected
