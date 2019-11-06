from collections import defaultdict

from typing import Dict, List, Tuple


MAX_NODES = 200


def initialise_graph(edges: List[Tuple[int]]) -> Dict[int, List[int]]:

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    return graph


class Count:

    def __init__(self):

        self._count = 0

    def inc(self):

        self._count += 1

    def __gt__(self, other: int):
        return self._count > other


def dfs(graph: Dict[int, List[int]], number_of_nodes: int) -> List[int]:

    results = []
    discovered = set()
    count = Count()

    def _dfs(node: int):

        if node in discovered:
            return
        discovered.add(node)

        count.inc()
        if count > MAX_NODES:
            raise ValueError(f"Exceeded node limit {MAX_NODES=}")

        results.append(node)

        for child_node in graph[node]:
            _dfs(child_node)

    _dfs(0)

    return results
