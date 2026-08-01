"""
Longest Repeating Character Replacement

You are given a string `s` and an integer `k`. You can choose any character
of the string and change it to any other uppercase English character. You
can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you
can get after performing the above operations.

Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form
    "AABBBBA". The substring "BBBB" has the longest repeating letters,
    which is 4.

Constraints:
    - 1 <= len(s) <= 10^5
    - s consists of only uppercase English letters.
    - 0 <= k <= len(s)
"""

from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    seen = defaultdict(int)
    left = 0
    max_l = float("-inf")

    for right in range(len(s)):
        char = s[right]
        seen[char] += 1
        max_freq = max(seen.values())
        s_l = right - left + 1

        while s_l - max_freq > k and left < len(s):
            seen[s[left]] -= 1
            left += 1

        max_l = max(max_l, right - left + 1)

    return max_l if max_l != float("-inf") else 0


def run_tests():
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("ABBB", 2, 4),
        ("AAAA", 0, 4),
        ("ABCDE", 1, 2),
    ]

    for i, (s, k, expected) in enumerate(test_cases, start=1):
        result = character_replacement(s, k)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test {i}: {status} | input=(s={s!r}, k={k}) | expected={expected}, got={result}"
        )


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input=(s='ABAB', k=2) | expected=4, got=4
Test 2: PASS | input=(s='AABABBA', k=1) | expected=4, got=4
Test 3: PASS | input=(s='ABBB', k=2) | expected=4, got=4
Test 4: PASS | input=(s='AAAA', k=0) | expected=4, got=4
Test 5: PASS | input=(s='ABCDE', k=1) | expected=2, got=2
"""
