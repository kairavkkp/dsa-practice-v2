"""
Validate Binary Search Tree

Given the `root` of a binary tree, determine if it is a valid binary search
tree (BST).

A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than
      the node's key.
    - The right subtree of a node contains only nodes with keys greater
      than the node's key.
    - Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2, 1, 3]
    Output: true

Example 2:
    Input: root = [5, 1, 4, null, null, 3, 6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is
    4.

Constraints:
    - The number of nodes in the tree is in the range [1, 10^4].
    - -2^31 <= Node.val <= 2^31 - 1
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


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def dfs(root, low, high):
        if not root:
            return True
        if not low < root.val < high:
            return False

        return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)

    return dfs(root, float("-inf"), float("inf"))


def run_tests():
    test_cases = [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([], True),
        ([1], True),
        ([10, 5, 15, None, None, 6, 20], False),
    ]

    for i, (values, expected) in enumerate(test_cases, start=1):
        root = build_tree(values)
        result = is_valid_bst(root)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input={values} | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=[2, 1, 3] | expected=True, got=True
Test 2: PASS | input=[5, 1, 4, None, None, 3, 6] | expected=False, got=False
Test 3: PASS | input=[] | expected=True, got=True
Test 4: PASS | input=[1] | expected=True, got=True
Test 5: PASS | input=[10, 5, 15, None, None, 6, 20] | expected=False, got=False
"""
