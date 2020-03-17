from typing import List
from unittest import TestCase


def search(search_value, set_L):
    current_len = 0
    if search_value - 1 in set_L:
        current_len += 1
        set_L.remove(search_value - 1)
        current_len += search(search_value - 1, set_L)
    if search_value + 1 in set_L:
        current_len += 1
        set_L.remove(search_value + 1)
        current_len += search(search_value + 1, set_L)
    return current_len


def max_len_consecutive_nums(L: List[int]) -> int:
    if not L:
        return 0

    set_L = set(L)

    max_len = 0

    while set_L:
        current_len = 1
        start = set_L.pop()

        current_len += search(start, set_L)

        max_len = max([current_len, max_len])

    return max_len


class TestMaxLenConsecutiveNums(TestCase):

    def test_example_1(self):

        L = [5, 2, 99, 3, 4, 1, 100]

        max_len = max_len_consecutive_nums(L)

        self.assertEqual(max_len, 5)

    def test_zero_length(self):

        max_len = max_len_consecutive_nums([])

        self.assertEqual(max_len, 0)

    def test_works_final_loop(self):

        max_len = max_len_consecutive_nums([1, 2])

        self.assertEqual(max_len, 2)

    def test_works_replacement(self):

        max_len = max_len_consecutive_nums([1, 2, 4, 5, 6])

        self.assertEqual(max_len, 3)
