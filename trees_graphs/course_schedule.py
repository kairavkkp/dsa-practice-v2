"""
Course Schedule

There are a total of `num_courses` courses you have to take, labeled from 0
to num_courses - 1. You are given an array `prerequisites` where
prerequisites[i] = [a_i, b_i] indicates that you must take course b_i first
if you want to take course a_i.

For example, the pair [0, 1] indicates that to take course 0 you have to
first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: num_courses = 2, prerequisites = [[1, 0]]
    Output: true
    Explanation: There are a total of 2 courses to take. To take course 1
    you should have finished course 0. So it is possible.

Example 2:
    Input: num_courses = 2, prerequisites = [[1, 0], [0, 1]]
    Output: false
    Explanation: There are a total of 2 courses to take. To take course 1
    you should have finished course 0, and to take course 0 you should also
    have finished course 1. So it is impossible.

Constraints:
    - 1 <= num_courses <= 2000
    - 0 <= len(prerequisites) <= 5000
    - prerequisites[i].length == 2
    - 0 <= a_i, b_i < num_courses
    - All the pairs prerequisites[i] are unique.
"""

from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    WHITE, GRAY, BLACK = 0, 1, 2
    graph = {i: [] for i in range(num_courses)}

    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = [WHITE] * num_courses

    def has_cycle(course):
        if state[course] == GRAY:
            # some course visiting
            return True

        if state[course] == BLACK:
            # some course already visited
            return False

        # as you are visiting
        state[course] = GRAY

        # check all prereqs if any of the course is having cycle
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True

        state[course] = BLACK
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False

    return True


def run_tests():
    test_cases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (5, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
        (3, [[0, 1], [1, 2], [2, 0]], False),
        (1, [], True),
    ]

    for i, (num_courses, prerequisites, expected) in enumerate(test_cases, start=1):
        result = can_finish(num_courses, prerequisites)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(num_courses={num_courses}, prerequisites={prerequisites}) | "
            f"expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=(num_courses=2, prerequisites=[[1, 0]]) | expected=True, got=True
Test 2: PASS | input=(num_courses=2, prerequisites=[[1, 0], [0, 1]]) | expected=False, got=False
Test 3: PASS | input=(num_courses=5, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]) | expected=True, got=True
Test 4: PASS | input=(num_courses=3, prerequisites=[[0, 1], [1, 2], [2, 0]]) | expected=False, got=False
Test 5: PASS | input=(num_courses=1, prerequisites=[]) | expected=True, got=True
"""
