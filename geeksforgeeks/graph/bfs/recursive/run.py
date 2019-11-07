from collections import defaultdict
from typing import DefaultDict, List, Tuple
from queue import Queue


NODE_LIMIT = 200


def bfs(graph: DefaultDict[int, List[int]], num_nodes: int) -> List[int]:
    """
    Calling this a recursive approach isn't really a thing - it's replacing a loop with recursive
    tail call.

    I think this is how to do it, though
    """

    call_count = 0
    results = []
    visited = set()
    q = Queue()

    def _bfs(node: int):
        nonlocal call_count

        call_count += 1
        if call_count > NODE_LIMIT:
            raise ValueError(
                f"Exploration calls exceeded maximum number of nodes {NODE_LIMIT=}")

        results.append(node)

        for child_node in graph[node]:
            if child_node not in visited:
                visited.add(child_node)
                q.put(child_node)

        if q.empty():
            return

        _bfs(q.get_nowait())

    visited.add(0)
    _bfs(0)

    return results


def initialise_graph(edges: List[Tuple[int]]) -> DefaultDict[int, List[int]]:

    graph = defaultdict(list)

    for u, v in edges:
        # add directed edge from u to v
        graph[u].append(v)

    return graph
