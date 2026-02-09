"""
LeetCode Problem #191: Number of 1 Bits
Difficulty: Easy
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/number-of-1-bits/

Problem:
--------
Write a function that takes an unsigned integer and returns the number of '1' bits it has
(also known as the Hamming weight).

Constraints:
-----------
- The input must be a binary string of length 32

Examples:
---------
Input: n = 00000000000000000000000000001011
Output: 3

Input: n = 00000000000000000000000010000000
Output: 1
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #191: Number of 1 Bits

    Approach: Brian Kernighan's algorithm
    Time Complexity: O(k) where k is number of 1 bits
    Space Complexity: O(1)

    Key Insights:
    - n & (n-1) removes rightmost 1 bit
    - Count how many times we can do this
    - Or use built-in bit_count()
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 191,
    "name": "Number of 1 Bits",
    "difficulty": "Easy",
    "pattern": "Bit Manipulation",
    "topics": ["Bit Manipulation"],
    "url": "https://leetcode.com/problems/number-of-1-bits/",
    "companies": ["Apple", "Microsoft", "Amazon"],
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
}