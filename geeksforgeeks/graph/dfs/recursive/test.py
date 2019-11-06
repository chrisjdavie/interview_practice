from unittest import TestCase

from run import dfs, initialise_graph


class TestDfs(TestCase):

    def test_example_1(self):

        N = 5
        edges = [(0, 1), (0, 2), (0, 3), (2, 4)]

        graph = initialise_graph(edges)

        self.assertEqual(dfs(graph, N), [0, 1, 2, 4, 3])

    def test_example_2(self):

        N = 4
        edges = [(0, 1), (1, 2), (0, 3)]

        graph = initialise_graph(edges)

        self.assertEqual(dfs(graph, N), [0, 1, 2, 3])

    def test_raises(self):

        N = 201
        edges = [(i, i+1) for i in range(201)]

        graph = initialise_graph(edges)

        with self.assertRaises(ValueError):
            dfs(graph, N)

    def test_circular(self):

        N = 2

        edges = [(0, 1), (1, 0)]

        graph = initialise_graph(edges)

        self.assertEqual(dfs(graph, N), [0, 1])

    def test_circular_above_trunk(self):

        N = 2

        edges = [(0, 1), (1, 2), (2, 1)]

        graph = initialise_graph(edges)

        self.assertEqual(dfs(graph, N), [0, 1, 2])
