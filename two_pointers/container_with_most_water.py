"""
Container With Most Water

You are given an integer array `height` of length n. There are n vertical
lines drawn such that the two endpoints of the i-th line are (i, 0) and
(i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49
    Explanation: The lines at index 1 (height 8) and index 8 (height 7) form
    a container of width 7 and height min(8, 7) = 7, giving area 49.

Example 2:
    Input: height = [1, 1]
    Output: 1

Constraints:
    - 2 <= len(height) <= 10^5
    - 0 <= height[i] <= 10^4
"""

from typing import List


def max_area(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = float("-inf")

    while left < right:
        area = min(height[right], height[left]) * (right - left)
        max_area = max(area, max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


def run_tests():
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1, 2, 4, 3], 4),
    ]

    for i, (height, expected) in enumerate(test_cases, start=1):
        result = max_area(height)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input={height} | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=[1, 8, 6, 2, 5, 4, 8, 3, 7] | expected=49, got=49
Test 2: PASS | input=[1, 1] | expected=1, got=1
Test 3: PASS | input=[4, 3, 2, 1, 4] | expected=16, got=16
Test 4: PASS | input=[1, 2, 1] | expected=2, got=2
Test 5: PASS | input=[1, 2, 4, 3] | expected=4, got=4
"""
