"""
LeetCode Problem #371: Sum of Two Integers
Difficulty: Medium
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/sum-of-two-integers/

Problem:
--------
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Constraints:
-----------
- -1000 <= a, b <= 1000

Examples:
---------
Input: a = 1, b = 2
Output: 3

Input: a = 2, b = 3
Output: 5
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #371: Sum of Two Integers

    Approach: Bit manipulation (XOR and carry)
    Time Complexity: O(1)
    Space Complexity: O(1)

    Key Insights:
    - XOR gives sum without carry
    - AND gives carry positions
    - Shift carry left and repeat
    """

    def getSum(self, a: int, b: int) -> int:
        """
        Calculate the sum of two integers without using + or -.

        Use bit manipulation:
        - XOR (^) gives the sum without considering carry
        - AND (&) followed by left shift gives the carry
        - Repeat until there's no carry

        In Python, we need to handle negative numbers specially since
        Python integers have infinite precision. We use a 32-bit mask
        to simulate 32-bit integer overflow behavior.
        """
        # 32-bit mask to simulate 32-bit integer
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        # Keep iterating while there's a carry
        while b != 0:
            # Calculate sum without carry (XOR)
            # Calculate carry (AND shifted left)
            # Apply mask to handle Python's infinite precision
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # If result is negative in 32-bit representation (> MAX_INT),
        # convert it back to Python's negative number representation
        return a if a <= MAX_INT else ~(a ^ MASK)


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 371,
    "name": "Sum of Two Integers",
    "difficulty": "Medium",
    "pattern": "Bit Manipulation",
    "topics": ['Math', 'Bit Manipulation'],
    "url": "https://leetcode.com/problems/sum-of-two-integers/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
}
