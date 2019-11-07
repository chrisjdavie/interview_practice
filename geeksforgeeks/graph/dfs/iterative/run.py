from collections import defaultdict

from typing import Dict, List, Tuple


def initialise_graph(edges: List[Tuple[int]]) -> Dict[int, List[int]]:

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    return graph


def dfs(graph: Dict[int, List[int]], number_of_nodes: int) -> List[int]:

    results = []
    stack = []
    limit = 200
    discovered = set()

    stack.append(0)

    for _ in range(limit):
        node = stack.pop()
        if node not in discovered:

            discovered.add(node)
            results.append(node)

            for child_node in graph[node][::-1]:
                if child_node not in discovered:
                    stack.append(child_node)

        if not stack:
            break

    else:
        raise ValueError(f"Exceeded node limit {limit=}")

    return results
