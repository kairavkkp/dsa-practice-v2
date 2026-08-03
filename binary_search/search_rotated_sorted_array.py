"""
Search in Rotated Sorted Array

There is an integer array `nums` sorted in ascending order (with distinct
values).

Prior to being passed to your function, `nums` is possibly rotated at an
unknown pivot index k (1 <= k < len(nums)) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-indexed). For example, [0, 1, 2, 4, 5, 6, 7] might be rotated at pivot
index 3 and become [4, 5, 6, 7, 0, 1, 2].

Given the array `nums` after the possible rotation and an integer
`target`, return the index of `target` if it is in `nums`, or -1 if it is
not in `nums`.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

Example 2:
    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1

Example 3:
    Input: nums = [1], target = 0
    Output: -1

Constraints:
    - 1 <= len(nums) <= 5000
    - -10^4 <= nums[i] <= 10^4
    - All values of nums are unique.
    - nums is an ascending array that is possibly rotated.
    - -10^4 <= target <= 10^4
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def run_tests():
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([5, 1, 3], 5, 0),
        ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),
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
Test 1: PASS | input=(nums=[4, 5, 6, 7, 0, 1, 2], target=0) | expected=4, got=4
Test 2: PASS | input=(nums=[4, 5, 6, 7, 0, 1, 2], target=3) | expected=-1, got=-1
Test 3: PASS | input=(nums=[1], target=0) | expected=-1, got=-1
Test 4: PASS | input=(nums=[5, 1, 3], target=5) | expected=0, got=0
Test 5: PASS | input=(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=8) | expected=4, got=4
"""
