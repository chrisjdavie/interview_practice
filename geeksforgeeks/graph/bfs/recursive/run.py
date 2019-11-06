from collections import defaultdict
from typing import DefaultDict, List, Tuple
from queue import Queue


def bfs(graph: DefaultDict[int, List[int]], num_nodes: int) -> List[int]:

    return [-1]


def initialise_graph(edges: List[Tuple[int]]) -> DefaultDict[int, List[int]]:

    graph = defaultdict(list)

    for u, v in edges:
        # add directed edge from u to v
        graph[u].append(v)

    return graph
