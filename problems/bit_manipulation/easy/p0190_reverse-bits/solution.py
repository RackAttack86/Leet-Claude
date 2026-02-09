"""
LeetCode Problem #190: Reverse Bits
Difficulty: Easy
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/reverse-bits/

Problem:
--------
Reverse bits of a given 32 bits unsigned integer.

Constraints:
-----------
- The input must be a binary string of length 32

Examples:
---------
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #190: Reverse Bits

    Approach: Bit manipulation
    Time Complexity: O(1)
    Space Complexity: O(1)

    Key Insights:
    - Process each bit from right to left
    - Shift result left and add current bit
    - Use bitwise operations
    """

    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 190,
    "name": "Reverse Bits",
    "difficulty": "Easy",
    "pattern": "Bit Manipulation",
    "topics": ['Divide and Conquer', 'Bit Manipulation'],
    "url": "https://leetcode.com/problems/reverse-bits/",
    "companies": ['Apple', 'Amazon', 'Microsoft'],
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
}
