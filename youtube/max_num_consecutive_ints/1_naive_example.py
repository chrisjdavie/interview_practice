from typing import List
from unittest import TestCase


def max_len_consecutive_nums(L: List[int]) -> int:
    if not L:
        return 0

    sorted_L = sorted(L)

    current_start = sorted_L[0]
    current_end = sorted_L[0]
    max_len = 0

    for num in sorted_L[1:]:
        if num == current_end + 1:
            current_end = num
        else:
            current_start = num
            current_end = num

        max_len = max([current_end - current_start + 1, max_len])

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
