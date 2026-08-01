"""
Clone Graph

Given a reference of a node in a connected undirected graph, return a deep
copy (clone) of the graph.

Each node in the graph contains a value (int) and a list of its neighbors
(List[Node]).

    class Node:
        def __init__(self, val=0, neighbors=None):
            self.val = val
            self.neighbors = neighbors if neighbors is not None else []

Test case format:
    For simplicity, each node's value is the same as the node's index
    (1-indexed). The adjacency list is a list where adj_list[i] is a list
    of the values of node (i + 1)'s neighbors.

Example 1:
    Input: adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    Output: [[2, 4], [1, 3], [2, 4], [1, 3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node
    (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node
    (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node
    (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node
    (val = 3).

Example 2:
    Input: adjList = [[]]
    Output: [[]]
    Explanation: The graph consists of only one node with no neighbors.

Example 3:
    Input: adjList = []
    Output: []
    Explanation: The graph is empty.

Constraints:
    - The number of nodes in the graph is in the range [0, 100].
    - 1 <= Node.val <= 100
    - Node.val is unique for each node.
    - There are no repeated edges and no self-loops in the graph.
    - The graph is connected and all nodes can be visited starting from the
      given node.
"""

from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    if not adj_list:
        return None

    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbor_vals in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[v] for v in neighbor_vals]

    return nodes[1]


def graph_to_adj_list(node: Optional[Node]) -> List[List[int]]:
    if not node:
        return []

    visited = {}
    queue = deque([node])
    visited[node.val] = node

    while queue:
        current = queue.popleft()
        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = neighbor
                queue.append(neighbor)

    return [sorted(n.val for n in visited[val].neighbors) for val in sorted(visited)]


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if not node:
        return None

    visited = {}

    def dfs(n):
        if n in visited:
            return visited[n]

        clone = Node(n.val)
        visited[n] = clone

        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)


def run_tests():
    test_cases = [
        ([[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]),
        ([[]], [[]]),
        ([], []),
        ([[2], [1]], [[2], [1]]),
        ([[2, 3], [1, 3], [1, 2]], [[2, 3], [1, 3], [1, 2]]),
    ]

    for i, (adj_list, expected) in enumerate(test_cases, start=1):
        original = build_graph(adj_list)
        cloned = clone_graph(original)
        result = graph_to_adj_list(cloned)
        is_deep_copy = cloned is not original if adj_list else True
        status = "PASS" if result == expected and is_deep_copy else "FAIL"
        print(
            f"Test {i}: {status} | input={adj_list} | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=[[2, 4], [1, 3], [2, 4], [1, 3]] | expected=[[2, 4], [1, 3], [2, 4], [1, 3]], got=[[2, 4], [1, 3], [2, 4], [1, 3]]
Test 2: PASS | input=[[]] | expected=[[]], got=[[]]
Test 3: PASS | input=[] | expected=[], got=[]
Test 4: PASS | input=[[2], [1]] | expected=[[2], [1]], got=[[2], [1]]
Test 5: PASS | input=[[2, 3], [1, 3], [1, 2]] | expected=[[2, 3], [1, 3], [1, 2]], got=[[2, 3], [1, 3], [1, 2]]
"""
