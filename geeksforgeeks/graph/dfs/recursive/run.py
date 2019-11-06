from collections import defaultdict, deque

from typing import Dict, List, Tuple


def initialise_graph(edges: List[Tuple[int]]) -> Dict[int, List[int]]:

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    return graph


def dfs(graph: Dict[int, List[int]], number_of_nodes: int) -> List[int]:

    return [-1]
