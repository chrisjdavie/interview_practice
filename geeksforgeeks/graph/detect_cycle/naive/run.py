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


def detect_cycle(graph: DefaultDict[int, List[int]]) -> bool:

    node_count = 0

    def _detect_cycle(node: int, recursion_stack: Set[int]):
        nonlocal node_count
        node_count += 1

        recursion_stack.add(node)

        if node_count > MAX_NUM_EDGES:
            raise ValueError(f"Exceeded maximum number of edges {MAX_NUM_EDGES=}")

        for child_node in graph[node]:
            if child_node in recursion_stack:
                return True
            if _detect_cycle(child_node, copy(recursion_stack)):
                return True

        return False

    remaining = set(graph.keys())

    while remaining:
        recursion_stack = set()
        if _detect_cycle(remaining.pop(), recursion_stack):
            return True
        remaining.difference_update(recursion_stack)

    return False