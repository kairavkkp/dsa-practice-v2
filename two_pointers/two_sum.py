"""
Two Sum

Given an array of integers `numbers` and an integer `target`, return the
indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Indices are 0-based. You can return the answer in any order.

Example 1:
    Input: numbers = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: numbers[0] + numbers[1] = 2 + 7 = 9. Return [0, 1].

Example 2:
    Input: numbers = [2, 3, 4], target = 6
    Output: [0, 2]
    Explanation: numbers[0] + numbers[2] = 2 + 4 = 6. Return [0, 2].

Example 3:
    Input: numbers = [-1, 0], target = -1
    Output: [0, 1]
    Explanation: numbers[0] + numbers[1] = -1 + 0 = -1. Return [0, 1].

Constraints:
    - 2 <= len(numbers) <= 3 * 10^4
    - -1000 <= numbers[i] <= 1000
    - -1000 <= target <= 1000
    - Exactly one valid answer exists.
"""

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    seen = {}

    for i, n in enumerate(numbers):
        diff = target - n
        if diff in seen:
            return [i, seen[diff]]
        seen[n] = i

    return []


def run_tests():
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([2, 3, 4], 6, [0, 2]),
        ([-1, 0], -1, [0, 1]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [3, 4]),
        ([5, 25, 75], 100, [1, 2]),
    ]

    for i, (numbers, target, expected) in enumerate(test_cases, start=1):
        result = two_sum(numbers, target)
        # order doesn't matter per problem statement, so compare as sets
        status = "PASS" if sorted(result) == sorted(expected) else "FAIL"
        print(
            f"Test {i}: {status} | input={numbers}, target={target} | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=[2, 7, 11, 15], target=9 | expected=[0, 1], got=[1, 0]
Test 2: PASS | input=[2, 3, 4], target=6 | expected=[0, 2], got=[2, 0]
Test 3: PASS | input=[-1, 0], target=-1 | expected=[0, 1], got=[1, 0]
Test 4: PASS | input=[1, 2, 3, 4, 4, 9, 56, 90], target=8 | expected=[3, 4], got=[4, 3]
Test 5: PASS | input=[5, 25, 75], target=100 | expected=[1, 2], got=[2, 1]
"""
