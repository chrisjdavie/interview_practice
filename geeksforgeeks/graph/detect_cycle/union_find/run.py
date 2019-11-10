"""
Undirected graph, looking for cycle
"""
from collections import defaultdict
from copy import copy
from typing import DefaultDict, List, Set, Tuple

from queue import Queue


MAX_NUM_EDGES = 200


def initialise_graph(edges: List[Tuple[int]]) -> DefaultDict[int, List[int]]:

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    return graph


def detect_cycle(graph: DefaultDict[int, List[int]], num_nodes: int) -> bool:

    parent = [-1]*3

    def find(node):
        if parent[node] == -1:
            return node
        return find(parent[node])

    def union(l_node, r_node):
        l_set = find(l_node)
        r_set = find(r_node)
        parent[l_set] = r_set

    for u in range(num_nodes):
        for v in graph[u]:
            l = find(u)
            r = find(v)
            if l == r:
                return True
            union(l, r)

    return False
