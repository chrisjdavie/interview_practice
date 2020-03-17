from unittest import TestCase


def num_coins(cents: int) -> int:

    total_num_coins = 0
    for coin in [25, 10, 5, 1]:
        total_num_coins += cents//coin
        cents %= coin
    return total_num_coins


class TestNumCoins(TestCase):

    def test_33(self):

        self.assertEqual(num_coins(33), 5)

    def test_31(self):

        self.assertEqual(num_coins(31), 3)
