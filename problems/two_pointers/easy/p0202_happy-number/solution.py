"""
LeetCode Problem #202: Happy Number
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/happy-number/

Problem:
--------
Write an algorithm to determine if a number `n` is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
	
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
	
- Those numbers for which this process ends in 1 are happy.

Return `true` if `n` is a happy number, and `false` if not.

Constraints:
-----------
- `1

Examples:
---------
Example 1:
```

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

```

Example 2:
```

Input: n = 2
Output: false

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #202: Happy Number

    Approach: Floyd's Cycle Detection (Slow and Fast Pointers)
    Time Complexity: O(log n) - number of digits decreases
    Space Complexity: O(1) - no extra space for cycle detection

    Key Insights:
    - The sequence will either end in 1 or enter a cycle
    - Use slow and fast pointers to detect cycles (like linked list cycle)
    - If fast pointer reaches 1, it's happy; if slow == fast, it's a cycle
    - Alternative: use a hash set to track seen numbers (O(log n) space)
    """

    def isHappy(self, n: int) -> bool:
        """
        Determine if a number is a happy number.

        Args:
            n: Positive integer to check

        Returns:
            True if n is a happy number, False otherwise
        """
        def get_next(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 202,
    "name": "Happy Number",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Hash Table', 'Math', 'Two Pointers'],
    "url": "https://leetcode.com/problems/happy-number/",
    "companies": ['Amazon', 'Google', 'Apple', 'Microsoft'],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}
