"""
Remove Duplicates from Sorted Array

Given an integer array `nums` sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once. The
relative order of the elements should be kept the same. Then return the
number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be k. To get accepted,
you need to do the following things:
    - Change the array `nums` such that the first k elements of `nums`
      contain the unique elements in the order they were present in `nums`
      initially. The remaining elements of `nums` are not important, as is
      the size of `nums`.
    - Return k.

You must do this by modifying the input array in-place with O(1) extra
memory.

Example 1:
    Input: nums = [1, 1, 2]
    Output: 2, nums = [1, 2, _]
    Explanation: Your function should return k = 2, with the first two
    elements of nums being 1 and 2 respectively.

Example 2:
    Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
    Explanation: Your function should return k = 5, with the first five
    elements of nums being 0, 1, 2, 3, and 4 respectively.

Constraints:
    - 1 <= len(nums) <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - nums is sorted in non-decreasing order.
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


def run_tests():
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1], 1, [1]),
        ([1, 1, 1, 1], 1, [1]),
        ([-3, -1, 0, 0, 0, 3, 3, 3, 5], 5, [-3, -1, 0, 3, 5]),
    ]

    for i, (nums, expected_k, expected_prefix) in enumerate(test_cases, start=1):
        original = list(nums)
        k = remove_duplicates(nums)
        status = "PASS" if k == expected_k and nums[:k] == expected_prefix else "FAIL"
        print(
            f"Test {i}: {status} | input={original} | expected=(k={expected_k}, {expected_prefix}), "
            f"got=(k={k}, {nums[:k] if isinstance(k, int) else nums})"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=[1, 1, 2] | expected=(k=2, [1, 2]), got=(k=2, [1, 2])
Test 2: PASS | input=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4] | expected=(k=5, [0, 1, 2, 3, 4]), got=(k=5, [0, 1, 2, 3, 4])
Test 3: PASS | input=[1] | expected=(k=1, [1]), got=(k=1, [1])
Test 4: PASS | input=[1, 1, 1, 1] | expected=(k=1, [1]), got=(k=1, [1])
Test 5: PASS | input=[-3, -1, 0, 0, 0, 3, 3, 3, 5] | expected=(k=5, [-3, -1, 0, 3, 5]), got=(k=5, [-3, -1, 0, 3, 5])
"""
