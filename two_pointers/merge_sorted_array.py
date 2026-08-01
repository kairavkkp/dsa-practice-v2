"""
Merge Sorted Array

You are given two integer arrays `nums1` and `nums2`, sorted in
non-decreasing order, and two integers `m` and `n`, representing the number
of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing
order.

The final sorted array should not be returned by the function, but instead
be stored inside the array `nums1`. To accommodate this, `nums1` has a
length of m + n, where the first m elements denote the elements that
should be merged, and the last n elements are set to 0 and should be
ignored. `nums2` has a length of n.

Example 1:
    Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
    Output: [1, 2, 2, 3, 5, 6]
    Explanation: The arrays we are merging are [1, 2, 3] and [2, 5, 6].
    The result of the merge is [1, 2, 2, 3, 5, 6].

Example 2:
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].

Example 3:
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1]. Note that because m = 0, there are no
    elements in nums1. The 0 is only there to ensure the merge result can
    fit in nums1.

Constraints:
    - len(nums1) == m + n
    - len(nums2) == n
    - 0 <= m, n <= 200
    - 1 <= m + n <= 200
    - -10^9 <= nums1[i], nums2[j] <= 10^9
"""

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


def run_tests():
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ([2, 0], 1, [1], 1, [1, 2]),
    ]

    for i, (nums1, m, nums2, n, expected) in enumerate(test_cases, start=1):
        original = list(nums1)
        merge(nums1, m, nums2, n)
        status = "PASS" if nums1 == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(nums1={original}, m={m}, nums2={nums2}, n={n}) | "
            f"expected={expected}, got={nums1}"
        )


if __name__ == "__main__":
    run_tests()


"""
$ python merge_sorted_array.py 
Test 1: PASS | input=(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) | expected=[1, 2, 2, 3, 5, 6], got=[1, 2, 2, 3, 5, 6]
Test 2: PASS | input=(nums1=[1], m=1, nums2=[], n=0) | expected=[1], got=[1]
Test 3: PASS | input=(nums1=[0], m=0, nums2=[1], n=1) | expected=[1], got=[1]
Test 4: PASS | input=(nums1=[4, 5, 6, 0, 0, 0], m=3, nums2=[1, 2, 3], n=3) | expected=[1, 2, 3, 4, 5, 6], got=[1, 2, 3, 4, 5, 6]
Test 5: PASS | input=(nums1=[2, 0], m=1, nums2=[1], n=1) | expected=[1, 2], got=[1, 2]
"""
