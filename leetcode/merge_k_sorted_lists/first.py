from dataclasses import dataclass, field
from queue import PriorityQueue
from typing import Optional

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


@dataclass(order=True)
class PrioritizedNode:
    val: int
    node: ListNode = field(default_factory=ListNode, compare=False)


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        return ListNode(-99)


@pytest.mark.parametrize(
    "sorted_lists,expected_list",
    (
        ([[1,4,5],[1,3,4],[2,6]],[1,1,2,3,4,4,5,6]),
        ([],[]),
        ([[]],[]),
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

