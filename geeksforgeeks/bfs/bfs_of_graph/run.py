from collections import defaultdict
from typing import DefaultDict, List, Tuple
from queue import Queue


def bfs(graph: DefaultDict[int, List[int]], num_nodes: int) -> List[int]:

    result = []
    seen = defaultdict(bool)

    q = Queue()
    q.put(0)
    seen[0] = True

    while not q.empty():

        node_id = q.get()
        print(node_id, end=" ")
        result.append(node_id)

        for child_id in graph[node_id]:
            if not seen[child_id]:
                q.put(child_id)
                seen[child_id] = True

    return result


def initialise_graph(edges: List[Tuple[int]]) -> DefaultDict[int, List[int]]:

    graph = defaultdict(list)

    for u, v in edges:
        # add directed edge from u to v
        graph[u].append(v)

    return graph
