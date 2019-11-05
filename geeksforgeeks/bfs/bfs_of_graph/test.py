from unittest import TestCase

from run import initialise_graph, bfs


class TestExamples(TestCase):

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

    def test_more_nodes_than_edges(self):

        num_nodes = 6
        edges = [(0, 1)]

        graph = initialise_graph(edges)

        self.assertEqual(bfs(graph, num_nodes), [0, 1])

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
