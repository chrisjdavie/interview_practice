"""
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
        
        dummy: ListNode = ListNode(0, head)
        dummy.next = head
        node: ListNode = dummy
        while node.next and node.next.next:
            node_0 = node.next
            node_1 = node.next.next
            # swap the node after the pair
            node_0.next = node_1.next
            # swap the pair
            node_1.next = node_0
            node.next = node_1
            # set up for the next iteration
            node = node_0

        return dummy.next


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


