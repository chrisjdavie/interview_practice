"""
Undirected graph, looking for cycle
"""
from collections import defaultdict
from copy import copy
from typing import DefaultDict, List, Set, Tuple, Union

from queue import Queue


class Node:

    def __init__(self):

        self.parent: Union[None, Node] = None
        self.children: List[Node] = []

    def add_child(self, node):

        self.children.append(node)


def initialise_graph(edges: List[Tuple[int]]) -> List[Node]:

    graph = defaultdict(Node)
    for u, v in edges:
        graph[u].add_child(graph[v])

    return list(graph.values())


def detect_cycle(graph: List[Node], num_nodes: int) -> bool:

    def find(node: Node):
        if not node.parent:
            return node
        return find(node.parent)

    def union(l_node, r_node):
        l_top = find(l_node)
        r_top = find(r_node)
        l_top.parent = r_top

    for node in graph:
        for child_node in node.children:
            l = find(node)
            r = find(child_node)
            if l == r:
                return True
            union(l, r)

    return False
