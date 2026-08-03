"""
Binary Search

Given an array of integers `nums` which is sorted in ascending order, and
an integer `target`, write a function to search `target` in `nums`. If
`target` exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4.

Example 2:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1.

Constraints:
    - 1 <= len(nums) <= 10^4
    - -10^4 < nums[i], target < 10^4
    - All the integers in nums are unique.
    - nums is sorted in ascending order.
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def run_tests():
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 0),
    ]

    for i, (nums, target, expected) in enumerate(test_cases, start=1):
        result = search(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(nums={nums}, target={target}) | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=(nums=[-1, 0, 3, 5, 9, 12], target=9) | expected=4, got=4
Test 2: PASS | input=(nums=[-1, 0, 3, 5, 9, 12], target=2) | expected=-1, got=-1
Test 3: PASS | input=(nums=[5], target=5) | expected=0, got=0
Test 4: PASS | input=(nums=[5], target=-5) | expected=-1, got=-1
Test 5: PASS | input=(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target=1) | expected=0, got=0
"""
