"""
Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between
1 and n times. For example, the array nums = [0, 1, 2, 4, 5, 6, 7] might
become:
    - [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times.
    - [0, 1, 2, 4, 5, 6, 7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time
results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array `nums` of unique elements, return the
minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [3, 4, 5, 1, 2]
    Output: 1
    Explanation: The original array was [1, 2, 3, 4, 5] rotated 3 times.

Example 2:
    Input: nums = [4, 5, 6, 7, 0, 1, 2]
    Output: 0
    Explanation: The original array was [0, 1, 2, 4, 5, 6, 7] and it was
    rotated 4 times.

Example 3:
    Input: nums = [11, 13, 15, 17]
    Output: 11
    Explanation: The original array was [11, 13, 15, 17] and it was
    rotated 4 times.

Constraints:
    - n == len(nums)
    - 1 <= n <= 5000
    - -5000 <= nums[i] <= 5000
    - All the integers of nums are unique.
    - nums is sorted and rotated between 1 and n times.
"""

from typing import List


def find_min(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


def run_tests():
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([2, 1], 1),
        ([5, 1, 2, 3, 4], 1),
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = find_min(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} | input={nums} | expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=[3, 4, 5, 1, 2] | expected=1, got=1
Test 2: PASS | input=[4, 5, 6, 7, 0, 1, 2] | expected=0, got=0
Test 3: PASS | input=[11, 13, 15, 17] | expected=11, got=11
Test 4: PASS | input=[2, 1] | expected=1, got=1
Test 5: PASS | input=[5, 1, 2, 3, 4] | expected=1, got=1
"""
