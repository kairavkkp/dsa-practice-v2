"""
Combination Sum

Given an array of distinct integers `candidates` and a target integer
`target`, return a list of all unique combinations of candidates where the
chosen numbers sum to target. You may return the combinations in any
order.

The same number may be chosen from candidates an unlimited number of
times. Two combinations are unique if the frequency of at least one of the
chosen numbers is different.

Example 1:
    Input: candidates = [2, 3, 6, 7], target = 7
    Output: [[2, 2, 3], [7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used
    multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

Example 2:
    Input: candidates = [2, 3, 5], target = 8
    Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Example 3:
    Input: candidates = [2], target = 1
    Output: []

Constraints:
    - 1 <= len(candidates) <= 30
    - 2 <= candidates[i] <= 40
    - All elements of candidates are distinct.
    - 1 <= target <= 40
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


def _normalize(all_combos: List[List[int]]):
    return sorted(tuple(sorted(c)) for c in all_combos)


def run_tests():
    test_cases = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
        ([1], 2, [[1, 1]]),
        ([2, 4], 4, [[2, 2], [4]]),
    ]

    for i, (candidates, target, expected) in enumerate(test_cases, start=1):
        result = combination_sum(candidates, target)
        # order of combinations, and order within each combination, doesn't matter
        status = "PASS" if _normalize(result) == _normalize(expected) else "FAIL"
        print(
            f"Test {i}: {status} | input=(candidates={candidates}, target={target}) | "
            f"expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()


"""
Test 1: PASS | input=(candidates=[2, 3, 6, 7], target=7) | expected=[[2, 2, 3], [7]], got=[[2, 2, 3], [7]]
Test 2: PASS | input=(candidates=[2, 3, 5], target=8) | expected=[[2, 2, 2, 2], [2, 3, 3], [3, 5]], got=[[2, 2, 2, 2], [2, 3, 3], [3, 5]]
Test 3: PASS | input=(candidates=[2], target=1) | expected=[], got=[]
Test 4: PASS | input=(candidates=[1], target=2) | expected=[[1, 1]], got=[[1, 1]]
Test 5: PASS | input=(candidates=[2, 4], target=4) | expected=[[2, 2], [4]], got=[[2, 2], [4]]
"""
