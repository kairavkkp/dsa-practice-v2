"""
Linked List Cycle

Given `head`, the head of a linked list, determine if the linked list has a
cycle in it.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the `next` pointer.
Internally, `pos` is used to denote the index of the node that the tail's
`next` pointer is connected to. Note that `pos` is not passed as a
parameter.

Return true if there is a cycle in the linked list. Otherwise, return
false.

Example 1:
    Input: head = [3, 2, 0, -4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail
    connects to the 1st node (0-indexed).

Example 2:
    Input: head = [1, 2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail
    connects to the 0th node.

Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

Constraints:
    - The number of nodes in the list is in the range [0, 10^4].
    - -10^5 <= Node.val <= 10^5
    - pos is -1 or a valid index in the linked list.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list_with_cycle(values: List[int], pos: int) -> Optional[ListNode]:
    if not values:
        return None

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


def has_cycle(head: Optional[ListNode]) -> bool:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


def run_tests():
    test_cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
        ([1, 2, 3, 4, 5], -1, False),
    ]

    for i, (values, pos, expected) in enumerate(test_cases, start=1):
        head = build_linked_list_with_cycle(values, pos)
        result = has_cycle(head)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(values={values}, pos={pos}) | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=(values=[3, 2, 0, -4], pos=1) | expected=True, got=True
Test 2: PASS | input=(values=[1, 2], pos=0) | expected=True, got=True
Test 3: PASS | input=(values=[1], pos=-1) | expected=False, got=False
Test 4: PASS | input=(values=[], pos=-1) | expected=False, got=False
Test 5: PASS | input=(values=[1, 2, 3, 4, 5], pos=-1) | expected=False, got=False
"""
