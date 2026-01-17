"""
LeetCode Problem #231: Power of Two
Difficulty: Easy
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/power-of-two/

Problem:
--------
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.

Constraints:
-----------
- -2^31 <= n <= 2^31 - 1

Examples:
---------
Input: n = 1
Output: true
Explanation: 2^0 = 1

Input: n = 16
Output: true
Explanation: 2^4 = 16

Input: n = 3
Output: false
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #231: Power of Two

    Approach: Bit manipulation trick
    Time Complexity: O(1)
    Space Complexity: O(1)

    Key Insights:
    - Power of 2 has exactly one bit set
    - Use n & (n-1) == 0 to check
    - Must also check n > 0
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 231,
    "name": "Power of Two",
    "difficulty": "Easy",
    "pattern": "Bit Manipulation",
    "topics": ['Math', 'Bit Manipulation', 'Recursion'],
    "url": "https://leetcode.com/problems/power-of-two/",
    "companies": ['Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
}
