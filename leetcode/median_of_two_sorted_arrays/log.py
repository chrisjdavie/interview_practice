"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

##############

This is the naive linear solver, and also lets me play with iterators a little cos that's fun
"""
from typing import List
from unittest import TestCase

from parameterized import parameterized


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        im3 = (len(nums1) + len(nums2)) // 2

        self.nums1 = nums1
        self.nums2 = nums2

        if not (len(self.nums1) + len(self.nums2)) % 2:
            return (
                self.findMed(0, len(self.nums1) - 1, 0, len(self.nums2) - 1, im3 - 1)
                + self.findMed(0, len(self.nums1) - 1, 0, len(self.nums2) - 1, im3)
            ) / 2
        return float(self.findMed(0, len(self.nums1) - 1, 0, len(self.nums2) - 1, im3))


    def findMed(self, i1_start: int, i1_end: int, i2_start: int, i2_end: int, im3: int) -> int:

        # print(i1_start, i1_end, i2_start, i2_end, im3)

        if i2_start > i2_end:
            return self.nums1[i1_start + im3]
        if i1_start > i1_end:
            return self.nums2[i2_start + im3]

        im1 = (i1_end - i1_start) // 2 # 0
        im2 = (i2_end - i2_start) // 2 # 0

        m1 = self.nums1[i1_start + im1] # 3
        m2 = self.nums2[i2_start + im2] # 2

        if im1 + im2 < im3:
            if m1 < m2:
                return self.findMed(i1_start + im1 + 1, i1_end, i2_start, i2_end, im3 - im1 - 1)
            else:
                return self.findMed(i1_start, i1_end, i2_start + im2 + 1, i2_end, im3 - im2 - 1)
        else:
            if m1 < m2:
                return self.findMed(i1_start, i1_end, i2_start, i2_start + im2 - 1, im3)
            else:
                return self.findMed(i1_start, i1_start + im1 - 1, i2_start, i2_end, im3)


class TestfindMedianSortedArrays(TestCase):

    @parameterized.expand([
        ([0], [1], 0.5),
        ([1, 2], [3], 2.0),
        ([1], [], 1.0),
        ([], [1], 1.0),
        ([2, 3], [1], 2.0),
        ([10, 12], [11, 13, 14], 12),
        ([1, 2], [3, 4], 2.5),
        ([1, 2], [], 1.5),
        ([1], [0,1,2], 1),
        ([0,1,2], [1], 1),
        ([1, 2], [3, 4], 2.5),
        ([1, 3], [2, 7], 2.5)
    ])
    def test(self, nums1, nums2, expected_result):
        import sys
        sys.setrecursionlimit(100)

        actual_result = Solution().findMedianSortedArrays(nums1, nums2)

        self.assertEqual(actual_result, expected_result)
