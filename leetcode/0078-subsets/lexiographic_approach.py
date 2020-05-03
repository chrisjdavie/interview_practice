"""
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

The not-too Pythonic "class Solution" is a leetcode thing

-------------------------

The powersets thing is perhaps most obviously shown via a binary
representation. This is very computer science-y though, not typically

"""
from typing import List, Tuple
from unittest import TestCase


class Solution:
    def subsets(self, nums: List[int]) -> List[Tuple[int]]:

        output = []

        n = len(nums)

        bit_shift = 1 << n
        for i in range(2**n):
            bitmask = bin(i | bit_shift)[3:]

            output.append(
                [num for bit, num in zip(bitmask, nums) if bit == "1"])

        return output


class TestSolution(TestCase):

    def test_example(self):

        solution = Solution()

        nums = [1, 2, 3]

        expected_output = [
            [3, ],
            [1, ],
            [2, ],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]
        actual_output = solution.subsets(nums)

        for ss in expected_output:
            self.assertIn(ss, actual_output)

# nth_bit = 1 << n
# for i in range(2**n):
#     # generate bitmask, from 0..00 to 1..11
#     bitmask = bin(i | nth_bit)[3:]


# n = 3

# for i in range(2**n, 2**(n + 1)):
#     # generate bitmask, from 0..00 to 1..11
#     bitmask = bin(i)[3:]
#     print(type(bitmask), type(bin(i)))
