"""
LeetCode Problem #67: Add Binary
Difficulty: Easy
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/add-binary/

Problem:
--------
Given two binary strings `a` and `b`, return their sum as a binary string.

Constraints:
-----------
- `1
- a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

Examples:
---------
Example 1:
```
Input: a = "11", b = "1"
Output: "100"

```

Example 2:
```
Input: a = "1010", b = "1011"
Output: "10101"

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #67: Add Binary

    Approach: Bit-by-bit addition with carry, simulating binary addition.
    We iterate from the rightmost bit of both strings, add corresponding
    bits along with carry, and build the result string from right to left.

    Time Complexity: O(max(m, n)) - where m and n are lengths of strings a and b
    Space Complexity: O(max(m, n)) - for storing the result string

    Key Insights:
    1. Binary addition: 0+0=0, 0+1=1, 1+0=1, 1+1=10 (0 with carry 1)
    2. At each position: sum = a_bit + b_bit + carry
       - result_bit = sum % 2
       - new_carry = sum // 2
    3. Process from right to left (least significant bit first)
    4. Don't forget the final carry if it exists
    5. Alternative: Use Python's built-in int(a, 2) + int(b, 2) then bin()
    """

    def addBinary(self, a: str, b: str) -> str:
        """
        Add two binary strings and return the sum as a binary string.
        """
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        # Process both strings from right to left
        while i >= 0 or j >= 0 or carry:
            # Get current bits (0 if index is out of bounds)
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            # Calculate sum and new carry
            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        # Reverse since we built from right to left
        return ''.join(reversed(result))


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 67,
    "name": "Add Binary",
    "difficulty": "Easy",
    "pattern": "Bit Manipulation",
    "topics": ['Math', 'String', 'Bit Manipulation', 'Simulation'],
    "url": "https://leetcode.com/problems/add-binary/",
    "companies": ["Facebook", "Amazon", "Microsoft", "Google", "Apple", "Bloomberg", "Adobe", "Uber"],
    "time_complexity": "O(max(m, n))",
    "space_complexity": "O(max(m, n))",
}
