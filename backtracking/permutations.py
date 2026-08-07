"""
Permutations

Given an array `nums` of distinct integers, return all the possible
permutations. You can return the answer in any order.

Example 1:
    Input: nums = [1, 2, 3]
    Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Example 2:
    Input: nums = [0, 1]
    Output: [[0, 1], [1, 0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]

Constraints:
    - 1 <= len(nums) <= 6
    - -10 <= nums[i] <= 10
    - All the integers of nums are unique.
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


def _normalize(all_perms: List[List[int]]):
    return sorted(tuple(p) for p in all_perms)


def run_tests():
    test_cases = [
        (
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
        ([], [[]]),
        ([1, 2], [[1, 2], [2, 1]]),
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = permute(nums)
        # order of permutations doesn't matter, but order within each does
        status = "PASS" if _normalize(result) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} | input={nums} | expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=[1, 2, 3] | expected=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], got=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
Test 2: PASS | input=[0, 1] | expected=[[0, 1], [1, 0]], got=[[0, 1], [1, 0]]
Test 3: PASS | input=[1] | expected=[[1]], got=[[1]]
Test 4: PASS | input=[] | expected=[[]], got=[[]]
Test 5: PASS | input=[1, 2] | expected=[[1, 2], [2, 1]], got=[[1, 2], [2, 1]]
"""
