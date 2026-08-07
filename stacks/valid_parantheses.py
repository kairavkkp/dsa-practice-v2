"""
Valid Parentheses

Given a string `s` containing just the characters '(', ')', '{', '}', '['
and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same
       type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Constraints:
    - 1 <= len(s) <= 10^4
    - s consists of parentheses only '()[]{}'.
"""


def is_valid(s: str) -> bool:
    stack = []
    pairs = {"}": "{", "]": "[", ")": "("}

    for char in s:
        if char in pairs.keys():
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0


def run_tests():
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]

    for i, (s, expected) in enumerate(test_cases, start=1):
        result = is_valid(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} | input={s!r} | expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()

"""
Test 1: PASS | input='()' | expected=True, got=True
Test 2: PASS | input='()[]{}' | expected=True, got=True
Test 3: PASS | input='(]' | expected=False, got=False
Test 4: PASS | input='([)]' | expected=False, got=False
Test 5: PASS | input='{[]}' | expected=True, got=True
"""
