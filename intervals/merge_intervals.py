"""
Merge Intervals

Given an array of `intervals` where intervals[i] = [start_i, end_i], merge
all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.

Example 1:
    Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    Output: [[1, 6], [8, 10], [15, 18]]
    Explanation: Since intervals [1, 3] and [2, 6] overlap, merge them into
    [1, 6].

Example 2:
    Input: intervals = [[1, 4], [4, 5]]
    Output: [[1, 5]]
    Explanation: Intervals [1, 4] and [4, 5] are considered overlapping.

Constraints:
    - 1 <= len(intervals) <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i <= end_i <= 10^4
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Sort the intervals by first key
    intervals.sort(key=lambda obj: obj[0])

    result = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = result[-1][1]

        if start <= last_end:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result


def run_tests():
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[1, 4]], [[1, 4]]),
    ]

    for i, (intervals, expected) in enumerate(test_cases, start=1):
        result = merge(intervals)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input={intervals} | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=[[1, 6], [2, 6], [8, 10], [15, 18]] | expected=[[1, 6], [8, 10], [15, 18]], got=[[1, 6], [8, 10], [15, 18]]
Test 2: PASS | input=[[1, 5], [4, 5]] | expected=[[1, 5]], got=[[1, 5]]
Test 3: PASS | input=[[0, 4], [1, 4]] | expected=[[0, 4]], got=[[0, 4]]
Test 4: PASS | input=[[1, 4], [2, 3]] | expected=[[1, 4]], got=[[1, 4]]
Test 5: PASS | input=[[1, 4]] | expected=[[1, 4]], got=[[1, 4]]
"""
