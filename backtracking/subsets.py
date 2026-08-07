"""
Subsets

Given an integer array `nums` of unique elements, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.

Example 1:
    Input: nums = [1, 2, 3]
    Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Example 2:
    Input: nums = [0]
    Output: [[], [0]]

Constraints:
    - 1 <= len(nums) <= 10
    - -10 <= nums[i] <= 10
    - All the numbers of nums are unique.
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def _normalize(all_subsets: List[List[int]]):
    return sorted(tuple(sorted(s)) for s in all_subsets)


def run_tests():
    test_cases = [
        ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
        ([], [[]]),
        ([1, 2], [[], [1], [2], [1, 2]]),
        ([4, 5], [[], [4], [5], [4, 5]]),
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = subsets(nums)
        # order of subsets, and order within each subset, doesn't matter
        status = "PASS" if _normalize(result) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} | input={nums} | expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=[1, 2, 3] | expected=[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]], got=[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
Test 2: PASS | input=[0] | expected=[[], [0]], got=[[], [0]]
Test 3: PASS | input=[] | expected=[[]], got=[[]]
Test 4: PASS | input=[1, 2] | expected=[[], [1], [2], [1, 2]], got=[[], [1], [1, 2], [2]]
Test 5: PASS | input=[4, 5] | expected=[[], [4], [5], [4, 5]], got=[[], [4], [4, 5], [5]]
"""
