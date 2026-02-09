"""
LeetCode Problem #172: Factorial Trailing Zeroes
Difficulty: Medium
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/factorial-trailing-zeroes/

Problem:
--------
Given an integer `n`, return the number of trailing zeroes in `n!`.

Note that `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`.

Constraints:
-----------
- `0

Examples:
---------
Example 1:
```

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

```

Example 2:
```

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

```

Example 3:
```

Input: n = 0
Output: 0

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #172: Factorial Trailing Zeroes

    Approach: Count Factors of 5

    Trailing zeroes are created by factors of 10 in n!.
    Since 10 = 2 * 5, we need pairs of factors 2 and 5.
    In any factorial, factors of 2 are always more abundant than factors of 5.
    So the count of trailing zeroes = count of factors of 5 in n!.

    To count factors of 5:
    - n/5 gives numbers divisible by 5 (each contributes one 5)
    - n/25 gives numbers divisible by 25 (each contributes an extra 5)
    - n/125 gives numbers divisible by 125 (each contributes yet another 5)
    - Continue until 5^k > n

    Time Complexity: O(log5(n)) - we divide n by increasing powers of 5
    Space Complexity: O(1) - only a counter variable used

    Key Insights:
    1. Trailing zeroes come from 10 = 2 * 5, and we always have more 2s than 5s
    2. Count factors of 5, not just multiples of 5 (25 has two 5s, 125 has three, etc.)
    3. Sum n/5 + n/25 + n/125 + ... until the divisor exceeds n
    4. This is equivalent to repeatedly dividing n by 5 and summing the quotients
    5. Example: 25! has 25/5 + 25/25 = 5 + 1 = 6 trailing zeroes
    """
    def trailingZeroes(self, n: int) -> int:
        """
        Count trailing zeroes in n! by counting factors of 5.
        """
        pass



PROBLEM_METADATA = {
    "number": 172,
    "name": "Factorial Trailing Zeroes",
    "difficulty": "Medium",
    "pattern": "Bit Manipulation",
    "topics": ['Math'],
    "url": "https://leetcode.com/problems/factorial-trailing-zeroes/",
    "companies": ["Bloomberg", "Microsoft", "Amazon", "Google", "Apple", "Facebook"],
    "time_complexity": "O(log5(n))",
    "space_complexity": "O(1)",
}