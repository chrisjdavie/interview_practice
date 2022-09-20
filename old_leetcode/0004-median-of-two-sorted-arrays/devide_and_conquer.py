from typing import List
from unittest import TestCase

from parameterized import parameterized


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        nums1_index_min: int = 0
        nums1_index_max: int = len(nums1) + len(nums2)
        nums1_l_index: int = 0
        nums1_r_index: int = len(nums1)
        
        nums2_index_min: int = 0
        nums2_index_max: int = lhs_index_max
        nums2_l_index: int = 0
        nums2_r_index: int = len(nums2)
        
        
    
        return 2.0


class TestFindMedianSortedArrays(TestCase):

    @parameterized.expand([
        ([1,2], [2], 2.0),
        ([1,2], [3,4], 2.5), # 
        ([0,0], [0,0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0)
    ])
    def test_examples(self, nums1: List[int], nums2: List[int], result: float):
        solution = Solution()
        self.assertEqual(
            solution.findMedianSortedArrays(nums1, nums2),
            result
        )


    def test_custom(self):
        nums1: List[int] = [0,1,3,7,9,12,14,18]
        nums2: List[int] = [2,3,5,8]
        result: float = 6.0
        
        solution = Solution()
        self.assertEqual(
            solution.findMedianSortedArrays(nums1, nums2),
            result
        )

