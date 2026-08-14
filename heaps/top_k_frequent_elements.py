"""
Top K Frequent Elements

Given an integer array `nums` and an integer `k`, return the k most
frequent elements. You may return the answer in any order.

Example 1:
    Input: nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= len(nums) <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - k is in the range [1, the number of distinct elements in the array].
    - It is guaranteed that the answer is unique.
"""

from typing import List
from collections import Counter
import heapq


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    heap = []
    c = Counter(nums)

    for num, freq in c.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]


def run_tests():
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 4, 4, 6, 6, 7, 7, 7, 7], 2, [7, 4]),
        ([1, 2, 2, 3, 3, 3], 2, [3, 2]),
        ([5, 5, 5, 5, 1, 1, 2], 1, [5]),
    ]

    for i, (nums, k, expected) in enumerate(test_cases, start=1):
        result = top_k_frequent(nums, k)
        # order doesn't matter
        status = "PASS" if sorted(result) == sorted(expected) else "FAIL"
        print(
            f"Test {i}: {status} | input=(nums={nums}, k={k}) | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=(nums=[1, 1, 1, 2, 2, 3], k=2) | expected=[1, 2], got=[2, 1]
Test 2: PASS | input=(nums=[1], k=1) | expected=[1], got=[1]
Test 3: PASS | input=(nums=[4, 4, 4, 6, 6, 7, 7, 7, 7], k=2) | expected=[7, 4], got=[4, 7]
Test 4: PASS | input=(nums=[1, 2, 2, 3, 3, 3], k=2) | expected=[3, 2], got=[2, 3]
Test 5: PASS | input=(nums=[5, 5, 5, 5, 1, 1, 2], k=1) | expected=[5], got=[5]
"""
