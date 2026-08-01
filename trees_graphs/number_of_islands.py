"""
Number of Islands

Given an m x n 2D binary grid `grid` which represents a map of '1's (land)
and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:
    Input: grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    Output: 1

Example 2:
    Input: grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    Output: 3

Constraints:
    - m == len(grid)
    - n == len(grid[i])
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'.
"""

import copy
from typing import List


def dfs(grid, row, col):
    if (
        row < 0
        or col < 0
        or row >= len(grid)
        or col >= len(grid[row])
        or grid[row][col] != "1"
    ):
        return

    grid[row][col] = "0"
    dfs(grid, row - 1, col)
    dfs(grid, row + 1, col)
    dfs(grid, row, col - 1)
    dfs(grid, row, col + 1)


def num_islands(grid: List[List[str]]) -> int:
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "1":
                dfs(grid, row, col)
                count += 1

    return count


def run_tests():
    test_cases = [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
        ([["1"]], 1),
        ([["0"]], 0),
        ([["1", "0", "1", "0", "1"]], 3),
    ]

    for i, (grid, expected) in enumerate(test_cases, start=1):
        result = num_islands(copy.deepcopy(grid))
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} | input={grid} | expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=[['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']] | expected=1, got=1
Test 2: PASS | input=[['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']] | expected=3, got=3
Test 3: PASS | input=[['1']] | expected=1, got=1
Test 4: PASS | input=[['0']] | expected=0, got=0
Test 5: PASS | input=[['1', '0', '1', '0', '1']] | expected=3, got=3
"""
