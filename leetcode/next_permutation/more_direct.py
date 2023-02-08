from typing import Optional

import pytest


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:

        i_to_inc: int = -1

        # find the candidate to swap
        for i, (n, n_m1) in enumerate(zip(nums[::-1], nums[-2::-1])):
            if n_m1 < n:
                i_to_inc = len(nums)-i-2
                break

        if i_to_inc != -1:

            # find the number to swap with
            num_to_inc: int = nums[i_to_inc]
            i_swap: int = i_to_inc + 1
            num_swap: int = nums[i_swap]

            for i, n in enumerate(nums[i_to_inc + 1:]):
                if n <= num_swap and n > num_to_inc:
                    num_swap = n
                    i_swap = i_to_inc + 1 + i

            nums[i_to_inc], nums[i_swap] = nums[i_swap], nums[i_to_inc]

        # sort out the ordering of remaining numbers
        i_l: int = i_to_inc + 1
        i_r: int = len(nums) - 1

        while i_l < i_r:
            nums[i_l], nums[i_r] = nums[i_r], nums[i_l]
            i_l += 1
            i_r -= 1


@pytest.mark.parametrize(
    "nums,expected_next_perm",
    (
        ([1,1], [1,1]),
        ([1,5,7], [1,7,5]),
        ([1,2,3], [1,3,2]),
        ([3,2,1], [1,2,3]), # looping case
        ([1,1,5], [1,5,1]), # duplicates case
        ([1,2,1,3,1], [1,2,3,1,1]),
        ([1,5,7,6], [1,6,5,7]), # not a swap of adjacent numbers
        ([1,2,3,1,1], [1,3,1,1,2]),
        ([1,5,6,2,1], [1,6,1,2,5]),
        ([2,3,1,3,3], [2,3,3,1,3]), # regression - I *think* this is a case of me not thinking about where the equality should sit
    )
)
def test_nextPermutation(nums, expected_next_perm):

    Solution().nextPermutation(nums)
    assert nums == expected_next_perm
