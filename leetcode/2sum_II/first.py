"""
Although I have solved this as part of 3-sum, I'm not sure I remember this particular version of the problem, so I'm doing it again.

I also want to think about this in relation to building a solution map - I don't think it's necessarily helpful for this case, but it seems like caching like that could help more complex versions

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
import pytest

class Solution:

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        return [-1]
        
        
@pytest.mark.parametrize(
    "numbers,target,expected",
    (
        ([2,7,11,15], 9, [1,2]),
        ([2,3,4], 6, [1,3]),
        ([-1,0], -1, [1,2]),
    )
)
def test(numbers, target, expected):
    assert Solution().twoSum(numbers, target) == expected

