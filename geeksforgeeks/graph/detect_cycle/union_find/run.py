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

    return -1
