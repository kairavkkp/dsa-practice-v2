"""
House Robber (Bottom-Up DP)

You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security
systems connected and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each
house, return the maximum amount of money you can rob tonight without
alerting the police.

Solve this iteratively (bottom-up), building up the answer from smaller
subproblems instead of top-down recursion with memoization.

Example 1:
    Input: nums = [1, 2, 3, 1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3
    (money = 3). Total amount you can rob = 1 + 3 = 4.

Example 2:
    Input: nums = [2, 7, 9, 3, 1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob
    house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
    - 1 <= len(nums) <= 100
    - 0 <= nums[i] <= 400
"""

from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) <= 1:
        return nums[0]

    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    return dp[n - 1]


def run_tests():
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([5], 5),
        ([2, 1, 1, 2], 4),
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = rob(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} | input={nums} | expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=[1, 2, 3, 1] | expected=4, got=4
Test 2: PASS | input=[2, 7, 9, 3, 1] | expected=12, got=12
Test 3: PASS | input=[5] | expected=5, got=5
Test 4: PASS | input=[2, 1, 1, 2] | expected=4, got=4
"""
