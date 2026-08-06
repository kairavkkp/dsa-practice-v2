"""
Reorder List

You are given the head of a singly linked-list. The list can be
represented as:
    L0 -> L1 -> ... -> Ln-1 -> Ln

Reorder the list to be on the following form:
    L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

You may not modify the values in the list's nodes. Only nodes themselves
may be changed.

The reordering must be done in-place; you must not return anything, just
modify `head` in-place.

Example 1:
    Input: head = [1, 2, 3, 4]
    Output: [1, 4, 2, 3]

Example 2:
    Input: head = [1, 2, 3, 4, 5]
    Output: [1, 5, 2, 4, 3]

Constraints:
    - The number of nodes in the list is in the range [1, 5 * 10^4].
    - 1 <= Node.val <= 1000
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    head = None
    tail = None
    for val in values:
        node = ListNode(val)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def get_middle(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        t = curr.next
        curr.next = prev
        prev = curr
        curr = t

    return prev


def reorder_list(head: Optional[ListNode]) -> None:
    # Get middle of the list
    middle = get_middle(head)
    second = middle.next
    middle.next = None

    # Reverse the second list
    second = reverse_list(second)

    # Merge two lists
    result = ListNode()
    tail = result
    first = head
    while first and second:
        tail.next = first
        tail = tail.next
        first = first.next

        tail.next = second
        tail = tail.next
        second = second.next

    tail.next = first if first else second

    return result.next


def run_tests():
    test_cases = [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
    ]

    for i, (values, expected) in enumerate(test_cases, start=1):
        head = build_linked_list(values)
        reorder_list(head)
        result = linked_list_to_list(head)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input={values} | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=[1, 2, 3, 4] | expected=[1, 4, 2, 3], got=[1, 4, 2, 3]
Test 2: PASS | input=[1, 2, 3, 4, 5] | expected=[1, 5, 2, 4, 3], got=[1, 5, 2, 4, 3]
Test 3: PASS | input=[1] | expected=[1], got=[1]
Test 4: PASS | input=[1, 2] | expected=[1, 2], got=[1, 2]
Test 5: PASS | input=[1, 2, 3] | expected=[1, 3, 2], got=[1, 3, 2]
"""
