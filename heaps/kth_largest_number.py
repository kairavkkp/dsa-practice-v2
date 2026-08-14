"""
Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the kth largest
element in the array.

Note that it is the kth largest element in sorted order, not the kth
distinct element.

Can you solve it without sorting? A heap is well suited for this.

Example 1:
    Input: nums = [3, 2, 1, 5, 6, 4], k = 2
    Output: 5

Example 2:
    Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
    Output: 4

Constraints:
    - 1 <= k <= len(nums) <= 10^5
    - -10^4 <= nums[i] <= 10^4
"""

from typing import List
import heapq


def find_kth_largest(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def run_tests():
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 10, 4, 3, 20, 15], 3, 10),
        ([2, 1], 2, 1),
    ]

    for i, (nums, k, expected) in enumerate(test_cases, start=1):
        result = find_kth_largest(nums, k)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(nums={nums}, k={k}) | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=(nums=[3, 2, 1, 5, 6, 4], k=2) | expected=5, got=5
Test 2: PASS | input=(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) | expected=4, got=4
Test 3: PASS | input=(nums=[1], k=1) | expected=1, got=1
Test 4: PASS | input=(nums=[7, 10, 4, 3, 20, 15], k=3) | expected=10, got=10
Test 5: PASS | input=(nums=[2, 1], k=2) | expected=1, got=1
"""
