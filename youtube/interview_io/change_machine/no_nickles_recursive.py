from typing import List
from unittest import TestCase


def num_coins(cents: int, coins: List[int]) -> int:

    total_num_coins = cents
    coin = coins[0]
    if coin == 1:
        return cents

    if cents < coin:
        total_num_coins = num_coins(cents, coins[1:])

    for num_this_coin in range(0, cents//coin + 1):
        tmp_cents = cents - num_this_coin*coin
        tmp_num_subs_coins = num_coins(tmp_cents, coins[1:])
        total_num_coins = min(
            [tmp_num_subs_coins + num_this_coin, total_num_coins])

    return total_num_coins


class TestNumCoins(TestCase):

    def test_33_us_coins(self):

        self.assertEqual(num_coins(33, [25, 10, 5, 1]), 5)

    def test_31_us_coins(self):

        self.assertEqual(num_coins(31, [25, 10, 5, 1]), 3)

    def test_31_no_nickles(self):

        self.assertEqual(num_coins(31, [25, 10, 1]), 4)

    def test_56_no_nickles(self):

        self.assertEqual(num_coins(56, [25, 10, 1]), 5)

    def test_one(self):

        self.assertEqual(num_coins(1, [1]), 1)
