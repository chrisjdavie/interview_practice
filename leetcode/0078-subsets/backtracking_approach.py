"""
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

The not-too Pythonic "class Solution" is a leetcode thing

-------------------------------

Leetcode has a different solution using this approach. I think they're
confused, misunderstanding another explanation of how this works. This is a
recursive solution, that does include backtracking but doesn't discard
invalid solution.

Mine is also simpler, in every sense, than their solution.

I've included their solution below. It also shows an interesting comparison
between using generators and functions, I did not know their approach
(relies a lot on 'non-locals' but without generators, you'd need something
like that). I wonder if that's a more Java way of coding this up.
"""
from typing import List, Tuple
from unittest import TestCase


class Solution:
    def subsets(self, nums: List[int]) -> List[Tuple[int]]:

        def backtrack(candidate: List[int], start: int):

            yield candidate[:]

            for i, n in enumerate(nums[start:]):
                candidate.append(n)
                yield from backtrack(candidate, start + i + 1)
                candidate.pop()

        return list(backtrack([], 0))


"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
"""


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
        print(actual_output)
        for ss in expected_output:
            self.assertIn(ss, actual_output)
