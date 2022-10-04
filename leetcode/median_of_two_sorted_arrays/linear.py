"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

##############

This is the naive linear solver, and also lets me play with iterators a little cos that's fun
"""
from itertools import chain, repeat
from statistics import median
from typing import List
from unittest import TestCase

from parameterized import parameterized


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def zipped():
            nums1_iter = chain(iter(nums1), repeat(float("inf")))
            nums2_iter = chain(iter(nums2), repeat(float("inf")))

            next_1 = next(nums1_iter)
            next_2 = next(nums2_iter)        

            while next_1 != float("inf") or next_2 != float("inf"):
                if next_1 < next_2:
                    yield next_1
                    next_1 = next(nums1_iter)
                else:
                    yield next_2
                    next_2 = next(nums2_iter)

        return median(zipped())


class TestfindMedianSortedArrays(TestCase):

    @parameterized.expand([
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([1], [], 1.0),
        ([1, 2], [], 1.5),
    ])
    def test(self, nums1, nums2, expected_result):
        actual_result = Solution().findMedianSortedArrays(nums1, nums2)

        self.assertEqual(actual_result, expected_result)
