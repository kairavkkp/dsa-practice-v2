"""
Merge Two Sorted Lists

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
    Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
    Output: [1, 1, 2, 3, 4, 4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    - The number of nodes in both lists is in the range [0, 50].
    - -100 <= Node.val <= 100
    - Both list1 and list2 are sorted in non-decreasing order.
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


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    result = ListNode()
    tail = result

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return result.next


def run_tests():
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([5], [], [5]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ]

    for i, (values1, values2, expected) in enumerate(test_cases, start=1):
        list1 = build_linked_list(values1)
        list2 = build_linked_list(values2)
        result = linked_list_to_list(merge_two_lists(list1, list2))
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(list1={values1}, list2={values2}) | "
            f"expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=(list1=[1, 2, 4], list2=[1, 3, 4]) | expected=[1, 1, 2, 3, 4, 4], got=[1, 1, 2, 3, 4, 4]
Test 2: PASS | input=(list1=[], list2=[]) | expected=[], got=[]
Test 3: PASS | input=(list1=[], list2=[0]) | expected=[0], got=[0]
Test 4: PASS | input=(list1=[5], list2=[]) | expected=[5], got=[5]
Test 5: PASS | input=(list1=[1, 2, 3], list2=[4, 5, 6]) | expected=[1, 2, 3, 4, 5, 6], got=[1, 2, 3, 4, 5, 6]
"""
