from unittest import TestCase

from run import detect_cycle, initialise_graph


class TestDetectCycle(TestCase):

    def test_cycle(self):

        num_nodes = 3
        edges = [(0, 1), (1, 2), (2, 0)]

        graph = initialise_graph(edges)

        self.assertEqual(detect_cycle(graph, num_nodes), True)

    def test_not_cycle(self):

        num_nodes = 3
        edges = [(0, 1), (1, 2), (2, 0)]

        graph = initialise_graph(edges)

        self.assertEqual(detect_cycle(graph, num_nodes), True)
