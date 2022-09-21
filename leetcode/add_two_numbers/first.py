"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import List, Optional
from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return None


class TestSolution(TestCase):

    @staticmethod
    def linked_list_from_list(linked_list: List[int]) -> ListNode:

        l_0 = ListNode(linked_list[0])
        l_m1 = l_0
        for val in linked_list[1:]:
            list_node = ListNode(val)
            l_m1.next = list_node
            l_m1 = list_node

        return l_0


    def test(self):

        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        
        l1_0 = self.linked_list_from_list(l1)
        l2_0 = self.linked_list_from_list(l2)

        expected = [7, 0, 8]
        actual = Solution().addTwoNumbers(l1_0, l2_0)

        self.assertListEqual(expected, actual)
