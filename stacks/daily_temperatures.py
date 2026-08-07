"""
Daily Temperatures

Given an array of integers `temperatures` representing the daily
temperatures, return an array `answer` such that answer[i] is the number
of days you have to wait after the i-th day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0
instead.

Example 1:
    Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    Output: [1, 1, 4, 2, 1, 1, 0, 0]

Example 2:
    Input: temperatures = [30, 40, 50, 60]
    Output: [1, 1, 1, 0]

Example 3:
    Input: temperatures = [30, 60, 90]
    Output: [1, 1, 0]

Constraints:
    - 1 <= len(temperatures) <= 10^5
    - 30 <= temperatures[i] <= 100
"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    stack = []
    result = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    return result


def run_tests():
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([100], [0]),
        ([70, 70, 70, 70], [0, 0, 0, 0]),
    ]

    for i, (temperatures, expected) in enumerate(test_cases, start=1):
        result = daily_temperatures(temperatures)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input={temperatures} | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=[73, 74, 75, 71, 69, 72, 76, 73] | expected=[1, 1, 4, 2, 1, 1, 0, 0], got=[1, 1, 4, 2, 1, 1, 0, 0]
Test 2: PASS | input=[30, 40, 50, 60] | expected=[1, 1, 1, 0], got=[1, 1, 1, 0]
Test 3: PASS | input=[30, 60, 90] | expected=[1, 1, 0], got=[1, 1, 0]
Test 4: PASS | input=[100] | expected=[0], got=[0]
Test 5: PASS | input=[70, 70, 70, 70] | expected=[0, 0, 0, 0], got=[0, 0, 0, 0]
"""
