from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return ListNode(-1)


def list_to_linked_list(nums: list[int]) -> Optional[ListNode]:
    if not nums:
        return None
    head = ListNode(nums[0])
    node = head
    for val in nums[1:]:
        node.next = ListNode(val)
        node = node.next
    return head


@pytest.mark.parametrize(
    "list1,list2,expected_merged_list",
    (
        ([1,2,3],[1,3,4],[1,1,2,3,4,4]),
        ([],[],[]),
        ([],[0], [0]),
    )
)
def test(list1, list2, expected_merged_list):
    linked1: Optional[ListNode] = list_to_linked_list(list1)
    linked2: Optional[ListNode] = list_to_linked_list(list2)

    actual_node = Solution().mergeTwoLists(linked1, linked2)
    for val in expected_merged_list:
        assert val == actual_node.val
        actual_node == actual_node.next
    assert actual_node is None

