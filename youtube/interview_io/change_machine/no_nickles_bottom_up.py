from typing import List
from unittest import TestCase


def num_coins(cents: int, coins: List[int]) -> int:

    mem_num_coins = [i for i in range(cents + 1)]

    for mem_cents in range(cents + 1):
        for coin in coins:
            if mem_cents >= coin:
                cand_num_coins = mem_num_coins[mem_cents - coin] + 1
                mem_num_coins[mem_cents] = min(
                    mem_num_coins[mem_cents], cand_num_coins)

    return mem_num_coins[-1]


class TestNumCoins(TestCase):

    def test_0(self):

        self.assertEqual(num_coins(0, [1]), 0)

    def test_1(self):

        self.assertEqual(num_coins(1, [1]), 1)

    def test_2(self):

        self.assertEqual(num_coins(2, [2, 1]), 1)

    def test_2_more_coins(self):

        self.assertEqual(num_coins(5, [10, 5, 1]), 1)

    def test_failure(self):

        self.assertEqual(num_coins(6, [5, 1]), 2)

    def test_33_us_coins(self):

        self.assertEqual(num_coins(33, [25, 10, 5, 1]), 5)

    def test_31_us_coins(self):

        self.assertEqual(num_coins(31, [25, 10, 5, 1]), 3)

    def test_31_no_nickles(self):

        self.assertEqual(num_coins(31, [25, 10, 1]), 4)

    def test_56_no_nickles(self):

        self.assertEqual(num_coins(56, [25, 10, 1]), 5)
