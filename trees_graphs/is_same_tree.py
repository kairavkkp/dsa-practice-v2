"""
Same Tree

Given the roots of two binary trees `p` and `q`, write a function to check
if they are the same or not.

Two binary trees are considered the same if they are structurally
identical, and the nodes have the same value.

Example 1:
    Input: p = [1, 2, 3], q = [1, 2, 3]
    Output: true

Example 2:
    Input: p = [1, 2], q = [1, null, 2]
    Output: false

Example 3:
    Input: p = [1, 2, 1], q = [1, 1, 2]
    Output: false

Constraints:
    - The number of nodes in both trees is in the range [0, 100].
    - -10^4 <= Node.val <= 10^4
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


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # If both None, then true
    if not p and not q:
        return True

    # if one of them is none then false
    if not p or not q:
        return False

    # if both exists but val differs then false
    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def run_tests():
    test_cases = [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
        ([1], [1], True),
    ]

    for i, (p_values, q_values, expected) in enumerate(test_cases, start=1):
        p = build_tree(p_values)
        q = build_tree(q_values)
        result = is_same_tree(p, q)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(p={p_values}, q={q_values}) | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=(p=[1, 2, 3], q=[1, 2, 3]) | expected=True, got=True
Test 2: PASS | input=(p=[1, 2], q=[1, None, 2]) | expected=False, got=False
Test 3: PASS | input=(p=[1, 2, 1], q=[1, 1, 2]) | expected=False, got=False
Test 4: PASS | input=(p=[], q=[]) | expected=True, got=True
Test 5: PASS | input=(p=[1], q=[1]) | expected=True, got=True
"""
