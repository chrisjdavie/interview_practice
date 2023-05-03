# https://leetcode.com/problems/search-in-rotated-sorted-array/
import pytest

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return -2


@pytest.mark.parametrize(
    "nums,target,expected_result",
    (
        ([4,5,6,7,0,1,2],0,4),
        ([4,5,6,7,0,1,2],3,-1),
        ([1],0,-1)
    )
)
def test_leetcode(nums,target,expected_result):
    assert Solution().search(nums, target) == expected_result
