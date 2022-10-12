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

        self.numsA = nums1
        self.numsB = nums2

        i_mC = (len(self.numsA) + len(self.numsB)) // 2

        if not (len(self.numsA) + len(self.numsB)) % 2:
            return float(
                (
                    self._find_med(0, len(self.numsA) - 1, 0, len(self.numsB) - 1, i_mC)
                    + self._find_med(0, len(self.numsA) - 1, 0, len(self.numsB) - 1, i_mC - 1)
                ) / 2
            )

        return float(self._find_med(0, len(self.numsA) - 1, 0, len(self.numsB) - 1, i_mC))

    def _find_med(self, i_A_start: int, i_A_end: int, i_B_start: int, i_B_end: int, i_med_C: int) -> int:

        if i_A_start > i_A_end:
            return self.numsB[i_B_start + i_med_C]
        if i_B_start > i_B_end:
            return self.numsA[i_A_start + i_med_C]

        i_med_A = (i_A_end - i_A_start) // 2
        i_med_B = (i_B_end - i_B_start) // 2

        med_A = self.numsA[i_A_start + i_med_A]
        med_B = self.numsB[i_B_start + i_med_B]

        if i_med_A + i_med_B < i_med_C:
            if med_A < med_B:
                return self._find_med(i_A_start + i_med_A + 1, i_A_end, i_B_start, i_B_end, i_med_C - i_med_A - 1)
            else:
                return self._find_med(i_A_start, i_A_end, i_B_start + i_med_B + 1, i_B_end, i_med_C - i_med_B - 1)
        else:
            if med_A < med_B:
                return self._find_med(i_A_start, i_A_end, i_B_start, i_B_start + i_med_B - 1, i_med_C)
            else:
                return self._find_med(i_A_start, i_A_start + i_med_A - 1, i_B_start, i_B_end, i_med_C)


class TestfindMedianSortedArrays(TestCase):

    @parameterized.expand([
        ([], [1], 1.0),
        ([1], [], 1.0),
        ([1, 3], [2], 2.0),
        ([2], [1, 3], 2.0),
        ([1, 2], [3, 4, 5], 3),
        ([3, 4, 5], [1, 2], 3),
        ([1], [2], 1.5),
    ])
    def test(self, nums1, nums2, expected_result):
        import sys
        sys.setrecursionlimit(100)

        actual_result = Solution().findMedianSortedArrays(nums1, nums2)

        self.assertEqual(actual_result, expected_result)
