"""
Reverse Linked List

Given the `head` of a singly linked list, reverse the list, and return the
reversed list.

Example 1:
    Input: head = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

Example 2:
    Input: head = [1, 2]
    Output: [2, 1]

Example 3:
    Input: head = []
    Output: []

Constraints:
    - The number of nodes in the list is in the range [0, 5000].
    - -5000 <= Node.val <= 5000
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


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        t = curr.next
        curr.next = prev
        prev = curr
        curr = t

    return prev


def run_tests():
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1]),
    ]

    for i, (values, expected) in enumerate(test_cases, start=1):
        head = build_linked_list(values)
        result = linked_list_to_list(reverse_list(head))
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input={values} | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=[1, 2, 3, 4, 5] | expected=[5, 4, 3, 2, 1], got=[5, 4, 3, 2, 1]
Test 2: PASS | input=[1, 2] | expected=[2, 1], got=[2, 1]
Test 3: PASS | input=[] | expected=[], got=[]
Test 4: PASS | input=[1] | expected=[1], got=[1]
Test 5: PASS | input=[1, 2, 3] | expected=[3, 2, 1], got=[3, 2, 1]
"""
