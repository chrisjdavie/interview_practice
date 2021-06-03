"""
I could have a graph built from Nodes explicitly, but I can't be bothered
It's less effort to just code up the dfs search using keys and dicts in the
one place I need it
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union


@dataclass
class Node:
    """
    A node in a Wardley Map
    """
    code: str
    dependencies: List[str]

    # these are things for exploring the tree
    neighbours: List[Node] = field(default_factory=list)
    first_caller: Optional[Node] = None


def graph_from_node_list(all_nodes: List[Node]) -> None:
    """
    Updates the Nodes to have neighbours and children
    """
    _code_node_map: Dict[str, Node] = {n.code: n for n in all_nodes}

    for a_node in all_nodes:
        for child_code in a_node.dependencies:
            child_node: Node = _code_node_map[child_code]
            child_node.neighbours.append(a_node)
            a_node.neighbours.append(child_node)
