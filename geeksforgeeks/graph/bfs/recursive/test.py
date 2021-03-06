from unittest import TestCase

from run import initialise_graph, bfs


class TestExamples(TestCase):

    def test_raises(self):

        N = 201
        edges = [(0, i+1) for i in range(N)]

        graph = initialise_graph(edges)

        with self.assertRaises(ValueError):
            bfs(graph, N)

    def test_example_1(self):

        num_nodes = 5
        edges = [(0, 1), (0, 2), (0, 3), (2, 4)]

        graph = initialise_graph(edges)

        self.assertEqual(bfs(graph, num_nodes), [0, 1, 2, 3, 4])

    def test_example_2(self):

        num_nodes = 3
        edges = [(0, 1), (0, 2)]

        graph = initialise_graph(edges)

        self.assertEqual(bfs(graph, num_nodes), [0, 1, 2])

    def test_circular(self):
        # it's a graph not a tree!

        num_nodes = 2
        edges = [(0, 1), (1, 0)]

        graph = initialise_graph(edges)

        self.assertEqual(bfs(graph, num_nodes), [0, 1])

    def test_circular_not_root(self):
        # it's a graph not a tree!

        num_nodes = 2
        edges = [(0, 1), (1, 2), (2, 1)]

        graph = initialise_graph(edges)

        self.assertEqual(bfs(graph, num_nodes), [0, 1, 2])

    def test_double_link(self):
        # it's a graph not a tree!

        num_nodes = 2
        edges = [(0, 1), (0, 2), (1, 3), (2, 3)]

        graph = initialise_graph(edges)

        self.assertEqual(bfs(graph, num_nodes), [0, 1, 2, 3])
