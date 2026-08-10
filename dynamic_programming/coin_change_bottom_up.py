"""
Coin Change (Bottom-Up DP)

You are given an integer array `coins` representing coins of different
denominations and an integer `amount` representing a total amount of
money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.

You may assume that you have an infinite number of each kind of coin.

Solve this iteratively (bottom-up), building up the answer for each amount
from 0 up to `amount`, instead of top-down recursion with memoization.

Example 1:
    Input: coins = [1, 2, 5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input: coins = [2], amount = 3
    Output: -1

Example 3:
    Input: coins = [1], amount = 0
    Output: 0

Constraints:
    - 1 <= len(coins) <= 12
    - 1 <= coins[i] <= 2^31 - 1
    - 0 <= amount <= 10^4
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


def run_tests():
    test_cases = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1, 3, 4], 6, 2),
        ([2, 5, 10, 1], 27, 4),
    ]

    for i, (coins, amount, expected) in enumerate(test_cases, start=1):
        result = coin_change(coins, amount)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(coins={coins}, amount={amount}) | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=(coins=[1, 2, 5], amount=11) | expected=3, got=3
Test 2: PASS | input=(coins=[2], amount=3) | expected=-1, got=-1
Test 3: PASS | input=(coins=[1], amount=0) | expected=0, got=0
Test 4: PASS | input=(coins=[1, 3, 4], amount=6) | expected=2, got=2
Test 5: PASS | input=(coins=[2, 5, 10, 1], amount=27) | expected=4, got=4
"""
