from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            head: ListNode = list1
            list1 = list1.next
        else:
            head: ListNode = list2
            list2 = list2.next

        node: Optional[ListNode] = head
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        if list2:
            node.next = list2

        return head


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
        ([1,2,3],[1,3,4],[1,1,2,3,3,4]),
        ([],[],[]),
        ([],[0], [0]),
    )
)
def test_leetcode(list1, list2, expected_merged_list):
    linked1: Optional[ListNode] = list_to_linked_list(list1)
    linked2: Optional[ListNode] = list_to_linked_list(list2)

    actual_node = Solution().mergeTwoLists(linked1, linked2)
    for val in expected_merged_list:
        assert val == actual_node.val
        actual_node = actual_node.next
    assert actual_node is None



@pytest.mark.parametrize(
    "list1,list2,expected_merged_list",
    (
        ([],[],[]),
        ([],[0],[0]),
        ([0],[],[0]),
        ([0],[1],[0,1]),
        ([1],[0],[0,1]),
        ([0,2],[1],[0,1,2]),
    )
)
def test_tdd(list1, list2, expected_merged_list):
    linked1: Optional[ListNode] = list_to_linked_list(list1)
    linked2: Optional[ListNode] = list_to_linked_list(list2)

    actual_node = Solution().mergeTwoLists(linked1, linked2)
    for val in expected_merged_list:
        assert val == actual_node.val
        actual_node = actual_node.next
    assert actual_node is None


