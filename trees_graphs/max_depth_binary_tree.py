"""
Maximum Depth of Binary Tree

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
    Input: root = [3, 9, 20, null, null, 15, 7]
    Output: 3

Example 2:
    Input: root = [1, null, 2]
    Output: 2

Example 3:
    Input: root = []
    Output: 0

Constraints:
    - The number of nodes in the tree is in the range [0, 10^4].
    - -100 <= Node.val <= 100
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


def max_depth(root: Optional[TreeNode]) -> int:
    def dfs(root):
        if not root:
            return 0

        left_depth = dfs(root.left)
        right_depth = dfs(root.right)

        return 1 + max(left_depth, right_depth)

    return dfs(root)


def run_tests():
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 4, None, None, None, 5], 4),
    ]

    for i, (values, expected) in enumerate(test_cases, start=1):
        root = build_tree(values)
        result = max_depth(root)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input={values} | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=[3, 9, 20, None, None, 15, 7] | expected=3, got=3
Test 2: PASS | input=[1, None, 2] | expected=2, got=2
Test 3: PASS | input=[] | expected=0, got=0
Test 4: PASS | input=[1] | expected=1, got=1
Test 5: PASS | input=[1, 2, 3, 4, None, None, None, 5] | expected=4, got=4
"""
