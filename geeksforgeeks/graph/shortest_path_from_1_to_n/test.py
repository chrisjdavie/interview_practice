from unittest import TestCase

from run import initialise_and_run


class TestRun(TestCase):

    def test_example_0(self):

        self.assertEqual(initialise_and_run(9), 2)

    def test_example_1(self):

        self.assertEqual(initialise_and_run(4), 2)
