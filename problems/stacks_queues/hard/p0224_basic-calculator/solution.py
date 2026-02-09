"""
LeetCode Problem #224: Basic Calculator
Difficulty: Hard
Pattern: Stacks Queues
Link: https://leetcode.com/problems/basic-calculator/

Problem:
--------
Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

Constraints:
-----------
- `1
- s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
- s` represents a valid expression.
- '+'` is not used as a unary operation (i.e., `"+1"` and `"+(2 + 3)"` is invalid).
- '-'` could be used as a unary operation (i.e., `"-1"` and `"-(2 + 3)"` is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

Examples:
---------
Example 1:
```

Input: s = "1 + 1"
Output: 2

```

Example 2:
```

Input: s = " 2-1 + 2 "
Output: 3

```

Example 3:
```

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #224: Basic Calculator

    Approach: Stack-based evaluation with sign tracking
    - Use a stack to handle parentheses by saving current result and sign
    - Process digits to form numbers, apply current sign for +/-
    - When encountering '(', push current result and sign, reset for sub-expression
    - When encountering ')', pop and combine with saved result

    Time Complexity: O(n) - single pass through the string
    Space Complexity: O(n) - stack depth proportional to nesting level

    Key Insights:
    1. Only + and - operators, so we can track a running result with sign
    2. Parentheses require saving state - use stack to store (result, sign)
    3. Unary minus is handled by treating it as 0 - value
    4. Spaces can be skipped during processing
    5. The sign before a parenthesis affects the entire sub-expression
    """

    def calculate(self, s: str) -> int:
        """
        Evaluate a basic calculator expression with +, -, and parentheses.
        """
        stack = []
        result = 0
        num = 0
        sign = 1  # 1 for positive, -1 for negative

        i = 0
        while i < len(s):
            char = s[i]

            if char.isdigit():
                # Build multi-digit number
                num = num * 10 + int(char)
            elif char == '+':
                # Add previous number with its sign, prepare for next
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                # Add previous number with its sign, prepare for negative
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                # Save current state and reset for sub-expression
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                # Complete current sub-expression
                result += sign * num
                num = 0
                # Pop sign and previous result, combine
                result = stack.pop() * result  # Apply saved sign
                result += stack.pop()  # Add to saved result
            # Skip spaces

            i += 1

        # Don't forget the last number
        result += sign * num

        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 224,
    "name": "Basic Calculator",
    "difficulty": "Hard",
    "pattern": "Stacks Queues",
    "topics": ['Math', 'String', 'Stack', 'Recursion'],
    "url": "https://leetcode.com/problems/basic-calculator/",
    "companies": ["Google", "Amazon", "Facebook", "Microsoft", "Apple", "Bloomberg", "Uber", "Airbnb", "Roblox"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}
