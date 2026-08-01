"""
Minimum Window Substring

Given two strings `s` and `t` of lengths m and n respectively, return the
minimum window substring of `s` such that every character in `t`
(including duplicates) is included in the window. If there is no such
substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and
    'C' from string t.

Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

Constraints:
    - 1 <= len(s), len(t) <= 10^5
    - s and t consist of uppercase and lowercase English letters.
"""

from collections import defaultdict


def min_window(s: str, t: str) -> str:
    # Create Hashmap for t
    ht = defaultdict(int)
    for c in t:
        ht[c] += 1
    required = len(ht)

    # Iterate the string
    left = 0
    min_l = float("inf")
    min_start = 0
    formed = 0

    # Hashmap for s
    hs = defaultdict(int)

    for right in range(len(s)):
        char = s[right]
        hs[char] += 1

        if char in ht and hs[char] == ht[char]:
            formed += 1

        while formed == required:

            # Checking if min_l is reduced or not
            if right - left + 1 < min_l:
                min_l = right - left + 1
                min_start = left  # basically the substring will start from here as min_l is reduced

            # As we're expanding left, we need to remove chars from left and update hs
            left_char = s[left]
            hs[left_char] -= 1

            if left_char in ht and hs[left_char] < ht[left_char]:
                formed -= 1

            left += 1

    return "" if min_l == float("inf") else s[min_start : min_start + min_l]


def run_tests():
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("aa", "aa", "aa"),
        ("ab", "b", "b"),
    ]

    for i, (s, t, expected) in enumerate(test_cases, start=1):
        result = min_window(s, t)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(s={s!r}, t={t!r}) | expected={expected!r}, got={result!r}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=(s='ADOBECODEBANC', t='ABC') | expected='BANC', got='BANC'
Test 2: PASS | input=(s='a', t='a') | expected='a', got='a'
Test 3: PASS | input=(s='a', t='aa') | expected='', got=''
Test 4: PASS | input=(s='aa', t='aa') | expected='aa', got='aa'
Test 5: PASS | input=(s='ab', t='b') | expected='b', got='b'
"""
