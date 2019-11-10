from unittest import TestCase

from run import is_cyclic, initialise_graph, MAX_NUM_EDGES


class TestIsCyclic(TestCase):

    def test_raises_on_limit(self):

        edges = [(i, i+1) for i in range(MAX_NUM_EDGES + 1)]

        graph = initialise_graph(edges)

        with self.assertRaises(ValueError):
            is_cyclic(graph)

    def test_not_cyclic(self):

        edges = [(0, 1)]

        graph = initialise_graph(edges)

        self.assertEqual(is_cyclic(graph), False)

    def test_cyclic_simple(self):

        edges = [(0, 1), (1, 0)]

        graph = initialise_graph(edges)

        self.assertEqual(is_cyclic(graph), True)

    def test_cyclic_second(self):

        edges = [(0, 1), (0, 2), (2, 0)]

        graph = initialise_graph(edges)

        self.assertEqual(is_cyclic(graph), True)

    def test_not_cyclic_two_routes(self):

        edges = [(0, 1), (0, 2), (1, 2)]

        graph = initialise_graph(edges)

        self.assertEqual(is_cyclic(graph), False)

    def test_cyclic_different_start_number(self):

        edges = [(1, 2), (2, 1)]

        graph = initialise_graph(edges)

        self.assertEqual(is_cyclic(graph), True)

    def test_cyclic_two_graphs(self):

        edges = [(0, 1), (2, 3), (3, 2)]

        graph = initialise_graph(edges)

        self.assertEqual(is_cyclic(graph), True)
