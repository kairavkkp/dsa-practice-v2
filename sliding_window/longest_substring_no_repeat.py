"""
Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without
repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and
    not a substring.

Constraints:
    - 0 <= len(s) <= 5 * 10^4
    - s consists of English letters, digits, symbols, and spaces.
"""


def length_of_longest_substring(s: str) -> int:
    max_l = 0
    left = 0
    seen = {}

    for right in range(len(s)):
        c = s[right]
        if c in seen and seen[c] >= left:
            left = seen[c] + 1

        seen[c] = right
        max_l = max(max_l, right - left + 1)

    return max_l


def run_tests():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("dvdf", 3),
    ]

    for i, (s, expected) in enumerate(test_cases, start=1):
        result = length_of_longest_substring(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} | input={s!r} | expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input='abcabcbb' | expected=3, got=3
Test 2: PASS | input='bbbbb' | expected=1, got=1
Test 3: PASS | input='pwwkew' | expected=3, got=3
Test 4: PASS | input='' | expected=0, got=0
Test 5: PASS | input='dvdf' | expected=3, got=3
"""
