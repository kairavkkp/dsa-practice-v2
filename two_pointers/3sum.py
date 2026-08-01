"""
3Sum

Given an integer array `nums`, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and
nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1, 0, 1] and [-1, -1, 2].

Example 2:
    Input: nums = [0, 1, 1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0, 0, 0]
    Output: [[0, 0, 0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
    - 3 <= len(nums) <= 3000
    - -10^5 <= nums[i] <= 10^5
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()

    result = []
    n = len(nums)

    for i in range(len(nums) - 2):
        # Duplicate check
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif s < 0:
                left += 1
            else:
                right -= 1
    return result


def _normalize(triplets: List[List[int]]):
    return sorted(tuple(sorted(t)) for t in triplets)


def run_tests():
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = three_sum(nums)
        # order of triplets, and order within each triplet, doesn't matter
        status = "PASS" if _normalize(result) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} | input={nums} | expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()

"""
$ python 3sum.py
Test 1: PASS | input=[-4, -1, -1, 0, 1, 2] | expected=[[-1, -1, 2], [-1, 0, 1]], got=[[-1, -1, 2], [-1, 0, 1]]
Test 2: PASS | input=[0, 1, 1] | expected=[], got=[]
Test 3: PASS | input=[0, 0, 0] | expected=[[0, 0, 0]], got=[[0, 0, 0]]
Test 4: PASS | input=[-2, 0, 1, 1, 2] | expected=[[-2, 0, 2], [-2, 1, 1]], got=[[-2, 0, 2], [-2, 1, 1]]
Test 5: PASS | input=[0, 0, 0, 0] | expected=[[0, 0, 0]], got=[[0, 0, 0]]
"""
