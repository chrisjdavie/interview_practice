from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def _reverseKGroup(self, node: Optional[ListNode], node_m1: Optional[ListNode], k: int, k_count: int) -> tuple[Optional[ListNode], Optional[ListNode]]:
    
        next_k_group: Optional[ListNode] = None
        k_group_head: Optional[ListNode] = None
        if node is not None:
            if k_count > 1:
                k_group_head, next_k_group = self._reverseKGroup(node.next, node, k, k_count - 1)
            else:
                k_group_head = node
                next_k_group = node.next
            if k_group_head:
                node.next = node_m1
        return k_group_head, next_k_group

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        new_head, next_k_group = self._reverseKGroup(head, None, k, k)
        if new_head:
            head.next = next_k_group
            return new_head
        return head


@pytest.mark.parametrize(
    "initial_vals,k,expected_vals",
    (
        # ([1,2,3,4,5],2,[2,1,4,3,5]),
        # ([1,2,3,4,5],3,[3,2,1,4,5]),
        ([],2,[]),
        ([0,1],3,[0,1]),
        ([0,1,2],3,[2,1,0]),
        ([0,1,2,3],3,[2,1,0,3]),
        ([0,1,2,3],2,[1,0,3,2]),
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

