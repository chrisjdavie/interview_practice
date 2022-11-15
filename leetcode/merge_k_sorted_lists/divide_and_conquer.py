"""
As is, it's O(k) space, as I'm using a new variable "new_lists" to store the interim solution. With some contortion you can reuse "lists", in the situation k >> n and it matters, but it's an uglier implementation.
"""
from typing import Optional

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def _mergeTwoLists(self, list_0: Optional[ListNode], list_1: Optional[ListNode]) -> Optional[ListNode]:
    
        dummy = ListNode()
    
        node = dummy
        while list_0 and list_1:
            if list_0.val < list_1.val:
                node.next = list_0
                list_0 = list_0.next
            else:
                node.next = list_1
                list_1 = list_1.next
            node = node.next
        
        if list_0:
            node.next = list_0
        if list_1:
            node.next = list_1

        return dummy.next

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) >= 2:
            new_lists: list[Optional[ListNode]] = [
                self._mergeTwoLists(list_0, list_1)
                for list_0, list_1 in zip(lists[::2], lists[1::2])
            ]
            if len(lists) % 2:
                new_lists.append(lists[-1])
            lists = new_lists

        return lists[0]


@pytest.mark.parametrize(
    "sorted_lists,expected_list",
    (
        ([[1,4,5],[1,3,4],[2,6]],[1,1,2,3,4,4,5,6]),
        ([],[]),
        ([[],[]],[]),
        ([[1,2,3]], [1,2,3]),
        ([[1,3,6],[2,3,4]], [1,2,3,3,4,6]),
        ([[],[1]], [1]),
        ([[1],[2],[3],[4]], [1,2,3,4]),
        ([[],[-1,5,11],[],[6,10]], [-1,5,6,10,11])
    )
)
def test_leetcode(sorted_lists, expected_list):
    
    linked_lists = []
    for sl in sorted_lists:
        head = None
        if sl:
            head = ListNode(sl[0])
        node = head
        for val in sl[1:]:
            new_node = ListNode(val)
            node.next = new_node
            node = new_node
        linked_lists.append(head)

    merged_node = Solution().mergeKLists(linked_lists)

    for val in expected_list:
        assert merged_node.val == val
        merged_node = merged_node.next
    assert merged_node == None

