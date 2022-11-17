"""
I came accross this in a leetcode question - although I figured out how to reverse a
linked list, I hadn't seen this tidy way of doing it (and it took me a moment to understand)
so I figured I'd practice it a few times until I was sure it had gone in.
"""
from typing import Optional
from itertools import count

import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(ll: ListNode, ll_m1: Optional[ListNode] = None) -> ListNode:
    head = ll
    if ll.next:
        head = reverse(ll.next, ll)
    ll.next = ll_m1
    return head
    

@pytest.mark.parametrize(
    "linked_list,reversed",
    (
        ([0,1,2,3,4],[4,3,2,1,0]),
    )
)
def test(linked_list, reversed):
    
    head = ListNode(linked_list[0])
    node = head
    for val in linked_list[1:]:
        node.next = ListNode(val)
        node = node.next

    reversed_ll = reverse(head)
    
    for val in reversed:
        print(reversed_ll.val)
        assert val == reversed_ll.val
        reversed_ll = reversed_ll.next

    assert reversed_ll == None

