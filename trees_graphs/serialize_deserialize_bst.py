"""
Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into
a sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in
the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree.
There is no restriction on how your serialization/deserialization
algorithm should work. You need to ensure that a binary search tree can be
serialized to a string, and this string can be deserialized to the
original tree structure.

The encoded string should be as compact as possible.

Example 1:
    Input: root = [2, 1, 3]
    Output: [2, 1, 3]

Example 2:
    Input: root = []
    Output: []

Constraints:
    - The number of nodes in the tree is in the range [0, 10^4].
    - 0 <= Node.val <= 10^4
    - The input tree is guaranteed to be a valid binary search tree.
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


def trees_equal(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (
        a.val == b.val and trees_equal(a.left, b.left) and trees_equal(a.right, b.right)
    )


def serialize(root: Optional[TreeNode]) -> str:
    result = []

    def dfs(root):
        if not root:
            result.append("N")
            return None

        result.append(str(root.val))
        _ = dfs(root.left)
        _ = dfs(root.right)

    dfs(root)
    return ",".join(result)


def deserialize(data: str) -> Optional[TreeNode]:
    values = iter(data.split(","))

    def build():
        val = next(values)
        if val == "N":
            return None

        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()


def run_tests():
    test_cases = [
        [2, 1, 3],
        [],
        [1],
        [5, 3, 6, 2, 4, None, 7],
        [10, 5, 15, 3, 7, 13, 18],
    ]

    for i, values in enumerate(test_cases, start=1):
        original = build_tree(values)
        data = serialize(original)
        result = deserialize(data)
        status = "PASS" if trees_equal(result, original) else "FAIL"
        print(f"Test {i}: {status} | input={values} | serialized={data!r}")


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=[2, 1, 3] | serialized='2,1,N,N,3,N,N'
Test 2: PASS | input=[] | serialized='N'
Test 3: PASS | input=[1] | serialized='1,N,N'
Test 4: PASS | input=[5, 3, 6, 2, 4, None, 7] | serialized='5,3,2,N,N,4,N,N,6,N,7,N,N'
Test 5: PASS | input=[10, 5, 15, 3, 7, 13, 18] | serialized='10,5,3,N,N,7,N,N,15,13,N,N,18,N,N'
"""
