"""
LeetCode Problem #50: Pow(x, n)
Difficulty: Medium
Pattern: Binary Search
Link: https://leetcode.com/problems/powx-n/

Problem:
--------
Implement pow(x, n), which calculates `x` raised to the power `n` (i.e., `x^n`).

Constraints:
-----------
- `-100.0
- 2^31
- n` is an integer.
- Either `x` is not zero or `n > 0`.
- 10^4

Examples:
---------
Example 1:
```

Input: x = 2.00000, n = 10
Output: 1024.00000

```

Example 2:
```

Input: x = 2.10000, n = 3
Output: 9.26100

```

Example 3:
```

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #50: Pow(x, n)

    Approach: Binary Exponentiation (Exponentiation by Squaring)
    Instead of multiplying x by itself n times (O(n)), we use the property:
    - x^n = (x^2)^(n/2) when n is even
    - x^n = x * (x^2)^((n-1)/2) when n is odd

    This allows us to halve the problem size at each step.
    For negative n, we compute 1 / x^(-n).

    Time Complexity: O(log n) - We halve n at each step
    Space Complexity: O(1) - Iterative approach uses constant space

    Key Insights:
    1. Use binary exponentiation to reduce from O(n) to O(log n)
    2. Handle negative exponent by computing 1/x^|n|
    3. Handle edge case where n = -2^31 (integer overflow when negating)
    4. When n is odd, multiply result by current x and reduce n by 1
    5. When n is even, square x and halve n
    """
    def myPow(self, x: float, n: int) -> float:
        pass



PROBLEM_METADATA = {
    "number": 50,
    "name": "Pow(x, n)",
    "difficulty": "Medium",
    "pattern": "Binary Search",
    "topics": ['Math', 'Recursion'],
    "url": "https://leetcode.com/problems/powx-n/",
    "companies": ["Facebook", "Amazon", "Google", "Microsoft", "Apple", "Bloomberg", "LinkedIn"],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}