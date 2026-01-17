"""
LeetCode Problem #342: Power of Four
Difficulty: Easy
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/power-of-four/

Problem:
--------
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4^x.

Constraints:
-----------
- -2^31 <= n <= 2^31 - 1

Examples:
---------
Input: n = 16
Output: true

Input: n = 5
Output: false

Input: n = 1
Output: true
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #342: Power of Four

    Approach: Bit manipulation
    Time Complexity: O(1)
    Space Complexity: O(1)

    Key Insights:
    - Must be power of 2 first
    - Power of 4 has 1 bit at even position
    - Use (n & 0x55555555) != 0
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 342,
    "name": "Power of Four",
    "difficulty": "Easy",
    "pattern": "Bit Manipulation",
    "topics": ['Math', 'Bit Manipulation', 'Recursion'],
    "url": "https://leetcode.com/problems/power-of-four/",
    "companies": ['Google', 'Amazon'],
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
}
