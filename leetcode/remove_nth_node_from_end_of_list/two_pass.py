"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
from itertools import count
from typing import Optional

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count the number of nodes
        node = head.next
        for i in count():
            if not node:
                break
            node = node.next

        # remove the nth node
        if i-n == -1:
            head = head.next
        else:
            node = head
            for _ in range(i-n):
                node = node.next
            node.next = node.next.next

        return head


@pytest.mark.parametrize(
    "node_vals,nth_to_remove,expected_node_vals",
    (
        ([1,2,3,4,5], 2, [1,2,3,5]),
        ([1], 1, []),
        ([1,2], 1, [1]),
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

