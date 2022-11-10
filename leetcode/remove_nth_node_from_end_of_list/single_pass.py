"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Single pass solution, cos the page asks for that. But turns out, for their timing, single
pass is slower than double pass, but maybe for long linked lists that isn't the case.
"""
from typing import Optional

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_lhs = head
        for _ in range(n):
            node_lhs = node_lhs.next

        if node_lhs:
            node_rhs = head
            while node_lhs.next:
                node_rhs = node_rhs.next
                node_lhs = node_lhs.next
            node_rhs.next = node_rhs.next.next
        else:
            return head.next
        return head


@pytest.mark.parametrize(
    "node_vals,nth_to_remove,expected_node_vals",
    (
        ([1,2,3,4,5], 2, [1,2,3,5]),
        ([1], 1, []),
        ([1,2], 1, [1]),
        ([1,2], 2, [2]),
    )
)
def test(node_vals, nth_to_remove, expected_node_vals): 

    # build the linked list
    head = ListNode(node_vals[0])
    prev_node = head
    for val in node_vals[1:]:
        node = ListNode(val)
        prev_node.next, prev_node = node, node

    actual_node = Solution().removeNthFromEnd(head, nth_to_remove)

    for val in expected_node_vals:
        assert actual_node.val == val
        actual_node = actual_node.next
    assert actual_node is None

