from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy: ListNode = ListNode(-1)
        dummy.next = head

        jump: Optional[ListNode] = dummy

        for _ in range(99):
            # check enough nodes for reversal
            broken: bool = False

            check_node: Optional[ListNode] = jump.next
            for _ in range(k):
                if not check_node:
                    broken = True
                    break         
                check_node = check_node.next
            if broken:
                break

            # swap node
            prev: Optional[ListNode] = check_node
            curr: Optional[ListNode] = jump.next

            for _ in range(k):
                curr.next, curr, prev = prev, curr.next, curr

            # stitch back into the previous k group, move jump point forward
            jump.next, jump = prev, jump.next

        return dummy.next


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
        print(val, actual_node.val)
        assert actual_node.val == val
        actual_node = actual_node.next
    assert actual_node == None

