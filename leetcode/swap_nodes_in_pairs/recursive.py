"""
Recursive version is simpler to read perhaps, but a little trickier to think about when building.

Based on other's solutions - I didn't think about a recursive solution

-----------------------

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

https://leetcode.com/problems/swap-nodes-in-pairs/
"""
from typing import Optional

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(head.next.next)
        newHead.next = head
        return newHead


@pytest.mark.parametrize(
    "vals,expected_swapped",
    (
        ([1,2,3,4],[2,1,4,3]),
        ([],[]),
        ([1],[1]),
    )
)
def test_leetcode(vals, expected_swapped):

    head = None
    if vals:
        head = ListNode(vals[0])
        node = head
        for val in vals[1:]:
            node.next = ListNode(val)
            node = node.next
    
    swapped = Solution().swapPairs(head)
    
    for val in expected_swapped:
        assert val == swapped.val
        swapped = swapped.next
    assert swapped == None


