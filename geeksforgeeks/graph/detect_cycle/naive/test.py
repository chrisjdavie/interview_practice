from unittest import TestCase

from run import detect_cycle, initialise_graph


class TestDetectCycle(TestCase):

    def test_raises_on_limit(self):

        edges = [(i, i+1) for i in range(201)]

        graph = initialise_graph(edges)

        with self.assertRaises(ValueError):
            detect_cycle(graph)

    def test_self_loop(self):

        edges = [(0, 1), (0, 0)]

        graph = initialise_graph(edges)

        self.assertEqual(detect_cycle(graph), True)

    def test_no_loop(self):

        edges = [(0, 1)]

        graph = initialise_graph(edges)

        self.assertEqual(detect_cycle(graph), False)

    def test_loop_two(self):

        edges = [(0, 1), (1, 0)]

        graph = initialise_graph(edges)

        self.assertEqual(detect_cycle(graph), True)

    def test_loop_rh_branch(self):

        edges = [(0, 1), (0, 2), (2, 2)]

        graph = initialise_graph(edges)

        self.assertEqual(detect_cycle(graph), True)

    def test_split(self):

        edges = [(0, 1), (0, 2), (1, 3), (2, 3)]

        graph = initialise_graph(edges)

        self.assertEqual(detect_cycle(graph), False)

    def test_loop_non_zero_index(self):

        edges = [(1, 2), (2, 1)]

        graph = initialise_graph(edges)

        self.assertEqual(detect_cycle(graph), True)

    def test_loop_two_graphs(self):

        edges = [(0, 1), (2, 3), (3, 2)]

        graph = initialise_graph(edges)

        self.assertEqual(detect_cycle(graph), True)

    def test_failing_example(self):

        edges = [(45, 16),  (54, 29),  (12, 41),  (36, 13),  (9, 31),  (49, 52),  (46, 53),  (22, 4),  (8, 11),  (35, 19),  (11, 54),  (22, 47),  (30, 37),  (42, 53),  (44, 47),  (54, 28),  (4, 47),  (59, 19),  (29, 35),  (32, 39),  (5, 23),  (32, 51),  (17, 55),  (57, 25),  (7, 31),  (46, 18),  (26, 8),  (6, 57),  (45, 50),  (51, 30),  (37, 47),  (60, 43),  (35, 59),  (1, 4)]

        graph = initialise_graph(edges)

        self.assertEqual(detect_cycle(graph), False)
