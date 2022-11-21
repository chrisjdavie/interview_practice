"""
Recursive solution - this is a much clearer solution. Probably the clearest.

It's also the slowest and most memory intensive, I'd guess because it keeps having to
do the work to create many methods for each calc.

I'd take clear, slow code over fast code, unless there's a good reason for the faster
code
"""

from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return f"<ListNode({self.val})>"


class Solution:

    def _shouldReverse(self, node: Optional[ListNode], k: int) -> bool:
        if k == 0: return True
        if node is None: return False

        return self._shouldReverse(node.next, k-1)

    def _reverse(self, node: ListNode, node_m1: Optional[ListNode], k: int) -> tuple[ListNode, Optional[ListNode]]:
        node_p1, node.next = node.next, node_m1

        if k > 1:
            return self._reverse(node_p1, node, k-1)
        # in this case, node_p1 is the head of the next k group
        return node, node_p1

    def reverseKGroup(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        if self._shouldReverse(node, k):
            # due to reversal, node is now the tail of this k group, and needs to be
            # tied to the next k group
            new_node, node.next = self._reverse(node, None, k)
            # reverse next k group
            node.next = self.reverseKGroup(node.next, k)
            return new_node
        return node


@pytest.mark.parametrize(
    "initial_vals,k,expected_vals",
    (
        ([1,2,3,4,5],2,[2,1,4,3,5]),
        ([1,2,3,4,5],3,[3,2,1,4,5]),
        ([],2,[]),
        ([0,1],3,[0,1]),
        ([0,1,2],3,[2,1,0]),
        ([0,1,2,3],3,[2,1,0,3]),
        ([0,1,2,3],2,[1,0,3,2]),
        ([0,1,2,3,4],2,[1,0,3,2,4]),
        ([0,1],1,[0,1]),
    )
)
def test(initial_vals, k, expected_vals):

    head = None
    if initial_vals:
        head = ListNode(initial_vals[0])
        node = head
        for val in initial_vals[1:]:
            node.next = ListNode(val)
            node = node.next

    actual_node = Solution().reverseKGroup(head, k)
    print()
    for val in expected_vals:
        print(val, actual_node.val, k)
        assert actual_node.val == val
        actual_node = actual_node.next
    assert actual_node == None

