"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import List, Optional
from unittest import TestCase

from parameterized import parameterized


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_current = l1
        l2_current = l2
        result = []
        carry = 0

        while l1_current and l2_current:
            sum = l1_current.val + l2_current.val + carry
            current = sum%10
            carry = sum//10
            result.append(current)
            l1_current = l1_current.next
            l2_current = l2_current.next

        while l1_current:
            sum = l1_current.val + carry
            current = sum%10
            carry = sum//10
            result.append(current)
            l1_current = l1_current.next

        while l2_current:
            sum = l2_current.val + carry
            current = sum%10
            carry = sum//10
            result.append(current)
            l2_current = l2_current.next

        if carry:
            result.append(carry)

        return result


class TestSolution(TestCase):

    @staticmethod
    def linked_list_from_list(linked_list: Optional[List[int]]) -> Optional[ListNode]:
        if linked_list is None:
            return None

        l_0 = ListNode(linked_list[0])
        l_m1 = l_0
        for val in linked_list[1:]:
            list_node = ListNode(val)
            l_m1.next = list_node
            l_m1 = list_node

        return l_0

    @parameterized.expand([
        ([2,], [5,], [7,]),
        ([2, 4, 3], [5, 5, 4], [7, 9, 7]),
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([9,], [9,], [8, 1,]),
        ([9, 9,], None, [9, 9,]),
        ([9, 9,], [1,], [0, 0, 1,]),
        ([1,], [9, 9,], [0, 0, 1,]),
    ])
    def test(self, l1, l2, expected):

        l1_0 = self.linked_list_from_list(l1)
        l2_0 = self.linked_list_from_list(l2)

        expected_0 = self.linked_list_from_list(expected)
        actual_0 = Solution().addTwoNumbers(l1_0, l2_0)

        while expected_0 or actual_0:
            self.assertEqual(expected_0.val, actual_0.val)
