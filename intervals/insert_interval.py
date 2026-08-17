"""
Insert Interval

You are given an array of non-overlapping `intervals` where
intervals[i] = [start_i, end_i] represent the start and the end of the
i-th interval and intervals is sorted in ascending order by start_i. You
are also given an interval `new_interval` = [start, end] that represents
the start and end of another interval.

Insert `new_interval` into `intervals` such that `intervals` is still
sorted in ascending order by start_i and intervals still does not have any
overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

Example 1:
    Input: intervals = [[1, 3], [6, 9]], new_interval = [2, 5]
    Output: [[1, 5], [6, 9]]

Example 2:
    Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        new_interval = [4, 8]
    Output: [[1, 2], [3, 10], [12, 16]]
    Explanation: Because new_interval = [4, 8] overlaps with
    [3, 5], [6, 7], [8, 10].

Constraints:
    - 0 <= len(intervals) <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i <= end_i <= 10^5
    - intervals is sorted by start_i in ascending order.
    - new_interval.length == 2
    - 0 <= start <= end <= 10^5
"""

from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    i = 0
    result = []
    n = len(intervals)

    # Phase 1: Append all intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Phase 2: Add overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)

    # Phase 3: All all remaining ones
    while i < n:
        result.append(intervals[i])
        i += 1
    return result


def run_tests():
    test_cases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
        ([], [5, 7], [[5, 7]]),
        ([[1, 5]], [2, 3], [[1, 5]]),
        ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
    ]

    for i, (intervals, new_interval, expected) in enumerate(test_cases, start=1):
        result = insert(intervals, new_interval)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(intervals={intervals}, new_interval={new_interval}) | "
            f"expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=(intervals=[[1, 3], [6, 9]], new_interval=[1, 5]) | expected=[[1, 5], [6, 9]], got=[[1, 5], [6, 9]]
Test 2: PASS | input=(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], new_interval=[3, 10]) | expected=[[1, 2], [3, 10], [12, 16]], got=[[1, 2], [3, 10], [12, 16]]
Test 3: PASS | input=(intervals=[], new_interval=[5, 7]) | expected=[[5, 7]], got=[[5, 7]]
Test 4: PASS | input=(intervals=[[1, 5]], new_interval=[1, 5]) | expected=[[1, 5]], got=[[1, 5]]
Test 5: PASS | input=(intervals=[[1, 5]], new_interval=[6, 8]) | expected=[[1, 5], [6, 8]], got=[[1, 5], [6, 8]]
"""
