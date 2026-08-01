"""
Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA)
node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common
ancestor is defined between two nodes p and q as the lowest node in T that
has both p and q as descendants (where we allow a node to be a descendant
of itself)."

Example 1:
    Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
    Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a
    descendant of itself according to the LCA definition.

Example 3:
    Input: root = [2, 1], p = 2, q = 1
    Output: 2

Constraints:
    - The number of nodes in the tree is in the range [2, 10^5].
    - -10^9 <= Node.val <= 10^9
    - All Node.val are unique.
    - p != q
    - p and q will exist in the BST.
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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Locates the node with the given value, for building test inputs."""
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            continue
        if node.val == val:
            return node
        queue.append(node.left)
        queue.append(node.right)
    return None


def lowest_common_ancestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if not right:
        return left
    elif not left:
        return right
    else:
        return root


def run_tests():
    test_cases = [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 0, 5, 2),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 7, 9, 8),
    ]

    for i, (values, p_val, q_val, expected) in enumerate(test_cases, start=1):
        root = build_tree(values)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        result = lowest_common_ancestor(root, p, q)
        result_val = result.val if result else None
        status = "PASS" if result_val == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(root={values}, p={p_val}, q={q_val}) | "
            f"expected={expected}, got={result_val}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=(root=[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p=2, q=8) | expected=6, got=6
Test 2: PASS | input=(root=[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p=2, q=4) | expected=2, got=2
Test 3: PASS | input=(root=[2, 1], p=2, q=1) | expected=2, got=2
Test 4: PASS | input=(root=[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p=0, q=5) | expected=2, got=2
Test 5: PASS | input=(root=[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p=7, q=9) | expected=8, got=8
"""
