"""
Minimum Size Subarray Sum

Given an array of positive integers `nums` and a positive integer `target`,
return the minimal length of a subarray whose sum is greater than or equal
to `target`. If there is no such subarray, return 0 instead.

Example 1:
    Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
    Output: 2
    Explanation: The subarray [4, 3] has the minimal length under the
    problem constraint.

Example 2:
    Input: target = 4, nums = [1, 4, 4]
    Output: 1

Example 3:
    Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
    Output: 0

Constraints:
    - 1 <= target <= 10^9
    - 1 <= len(nums) <= 10^5
    - 1 <= nums[i] <= 10^4
"""

from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    if not nums:
        return 0

    left = 0
    s = 0
    min_l = float("inf")

    for right in range(len(nums)):
        s += nums[right]
        while s >= target:
            min_l = min(min_l, right - left + 1)
            s -= nums[left]
            left += 1

    return min_l if min_l != float("inf") else 0


def run_tests():
    test_cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (15, [1, 2, 3, 4, 5], 5),
        (6, [10, 2, 3], 1),
    ]

    for i, (target, nums, expected) in enumerate(test_cases, start=1):
        result = min_sub_array_len(target, nums)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(target={target}, nums={nums}) | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=(target=7, nums=[2, 3, 1, 2, 4, 3]) | expected=2, got=2
Test 2: PASS | input=(target=4, nums=[1, 4, 4]) | expected=1, got=1
Test 3: PASS | input=(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) | expected=0, got=0
Test 4: PASS | input=(target=15, nums=[1, 2, 3, 4, 5]) | expected=5, got=5
Test 5: PASS | input=(target=6, nums=[10, 2, 3]) | expected=1, got=1
"""
