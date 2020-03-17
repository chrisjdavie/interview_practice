from typing import List
from unittest import TestCase


def max_len_consecutive_nums(L: List[int]) -> int:

    max_len = 0
    set_L = set(L)

    while set_L:
        initial_val = set_L.pop()
        current_len = 1

        to_explore = set([initial_val])

        while to_explore:
            current_val = to_explore.pop()
            if current_val + 1 in set_L:
                set_L.remove(current_val + 1)
                to_explore.add(current_val + 1)
                current_len += 1
            if current_val - 1 in set_L:
                set_L.remove(current_val - 1)
                to_explore.add(current_val - 1)
                current_len += 1
        max_len = max([max_len, current_len])

    return max_len


class TestMaxLenConsecutiveNums(TestCase):

    def test_example_1(self):

        L = [5, 2, 99, 3, 4, 1, 100]

        max_len = max_len_consecutive_nums(L)

        self.assertEqual(max_len, 5)

    def test_single_sequence(self):

        L = [1, 2]

        self.assertEqual(max_len_consecutive_nums(L), 2)

    def test_zero_length(self):

        max_len = max_len_consecutive_nums([])

        self.assertEqual(max_len, 0)

    def test_works_final_loop(self):

        max_len = max_len_consecutive_nums([1, 2])

        self.assertEqual(max_len, 2)

    def test_works_replacement(self):

        max_len = max_len_consecutive_nums([1, 2, 4, 5, 6])

        self.assertEqual(max_len, 3)
