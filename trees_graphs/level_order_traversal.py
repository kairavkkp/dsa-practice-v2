"""
Binary Tree Level Order Traversal

Given the `root` of a binary tree, return the level order traversal of its
nodes' values (i.e., from left to right, level by level).

Example 1:
    Input: root = [3, 9, 20, null, null, 15, 7]
    Output: [[3], [9, 20], [15, 7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Constraints:
    - The number of nodes in the tree is in the range [0, 2000].
    - -1000 <= Node.val <= 1000
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a LeetCode-style level-order list."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values):
            val = values[i]
            i += 1
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)

        if i < len(values):
            val = values[i]
            i += 1
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)

    return root


def level_order(root: Optional[TreeNode]) -> List[List[int]]:

    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        # Get levels
        levels = len(queue)
        level_values = []
        for _ in range(levels):
            node = queue.popleft()
            level_values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_values)

    return result


def run_tests():
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, None, 2, None, 3], [[1], [2], [3]]),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
    ]

    for i, (values, expected) in enumerate(test_cases, start=1):
        root = build_tree(values)
        result = level_order(root)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input={values} | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=[3, 9, 20, None, None, 15, 7] | expected=[[3], [9, 20], [15, 7]], got=[[3], [9, 20], [15, 7]]
Test 2: PASS | input=[1] | expected=[[1]], got=[[1]]
Test 3: PASS | input=[] | expected=[], got=[]
Test 4: PASS | input=[1, None, 2, None, 3] | expected=[[1], [2], [3]], got=[[1], [2], [3]]
Test 5: PASS | input=[1, 2, 3, 4, 5, 6, 7] | expected=[[1], [2, 3], [4, 5, 6, 7]], got=[[1], [2, 3], [4, 5, 6, 7]]
"""
