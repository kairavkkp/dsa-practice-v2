"""
Climbing Stairs

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can
you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Constraints:
    - 1 <= n <= 45
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def run_tests():
    test_cases = [
        (2, 2),
        (3, 3),
        (1, 1),
        (4, 5),
        (5, 8),
    ]

    for i, (n, expected) in enumerate(test_cases, start=1):
        result = climb_stairs(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} | input={n} | expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=2 | expected=2, got=2
Test 2: PASS | input=3 | expected=3, got=3
Test 3: PASS | input=1 | expected=1, got=1
Test 4: PASS | input=4 | expected=5, got=5
Test 5: PASS | input=5 | expected=8, got=8
"""
