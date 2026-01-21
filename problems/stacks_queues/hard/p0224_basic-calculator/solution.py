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

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def calculate(self, s: str) -> int:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 224,
    "name": "Basic Calculator",
    "difficulty": "Hard",
    "pattern": "Stacks Queues",
    "topics": ['Math', 'String', 'Stack', 'Recursion'],
    "url": "https://leetcode.com/problems/basic-calculator/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
