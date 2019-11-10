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


def is_cyclic(graph: DefaultDict[int, List[int]]) -> bool:

    count: int = 0
    visited: Set[int] = set()

    def is_cyclic_one_graph(node: int, stack: set) -> None:
        nonlocal count
        count += 1
        if count > MAX_NUM_EDGES:
            raise ValueError(
                f"Exploration exceeded maximum number of edges {MAX_NUM_EDGES=}")

        visited.add(node)
        stack.add(node)

        for child_node in graph[node]:
            if child_node in stack:
                return True
            if is_cyclic_one_graph(child_node, copy(stack)):
                return True

        return False

    remaining_nodes: Set[int] = set(graph.keys())

    while remaining_nodes := remaining_nodes.difference(visited):
        if is_cyclic_one_graph(remaining_nodes.pop(), set()):
            return True

    return False
