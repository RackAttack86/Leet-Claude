"""
LeetCode Problem #201: Bitwise AND of Numbers Range
Difficulty: Medium
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/bitwise-and-of-numbers-range/

Problem:
--------
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Constraints:
-----------
- 0 <= left <= right <= 2^31 - 1

Examples:
---------
Input: left = 5, right = 7
Output: 4

Input: left = 0, right = 0
Output: 0

Input: left = 1, right = 2147483647
Output: 0
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #201: Bitwise AND of Numbers Range

    Approach: Find common prefix
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Key Insights:
    - AND of range is common binary prefix
    - Right shift both until they're equal
    - Left shift result to restore position
    """

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Find the bitwise AND of all numbers in the range [left, right].

        The key insight is that when we AND all numbers in a range, any bit
        position that changes (flips from 0 to 1 or 1 to 0) within the range
        will result in 0 at that position. Only the common prefix bits that
        remain the same across all numbers will survive.

        We find the common prefix by right-shifting both left and right until
        they are equal, then left-shift back by the same amount.
        """
        shift = 0
        # Find common prefix by right-shifting until left equals right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        # Left-shift to restore the position of the common prefix
        return left << shift


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 201,
    "name": "Bitwise AND of Numbers Range",
    "difficulty": "Medium",
    "pattern": "Bit Manipulation",
    "topics": ['Bit Manipulation'],
    "url": "https://leetcode.com/problems/bitwise-and-of-numbers-range/",
    "companies": ['Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}
