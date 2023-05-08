# https://leetcode.com/problems/search-in-rotated-sorted-array/
import pytest


class Solution:

    @staticmethod
    def _find_pivot_index(nums: list[int]) -> int:

        return -1

    def search(self, nums: list[int], target: int) -> int:

        return 0


@pytest.mark.parametrize(
    "nums,pivot_index",
    (
        ([4,1,2], 1),
    )
)
def test_find_pivot(nums, pivot_index):

    assert Solution._find_pivot_index(nums) == pivot_index


@pytest.mark.parametrize(
    "nums,target,expected_result",
    (
        ([0], 0, 0),
    ),
)
def test_search(nums, target, expected_result):
    assert Solution().search(nums, target) == expected_result
