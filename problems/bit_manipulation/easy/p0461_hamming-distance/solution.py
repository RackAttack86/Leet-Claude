"""
LeetCode Problem #461: Hamming Distance
Difficulty: Easy
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/hamming-distance/

Problem:
--------
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Constraints:
-----------
- 0 <= x, y <= 2^31 - 1

Examples:
---------
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ^   ^
The above arrows point to positions where bits are different.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #461: Hamming Distance

    Approach: XOR and count bits
    Time Complexity: O(1)
    Space Complexity: O(1)

    Key Insights:
    - XOR gives differing bits
    - Count 1s in XOR result
    - Use Brian Kernighan's algorithm
    """

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor:
            count += 1
            xor &= (xor - 1)  # Brian Kernighan's algorithm
        return count


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 461,
    "name": "Hamming Distance",
    "difficulty": "Easy",
    "pattern": "Bit Manipulation",
    "topics": ['Bit Manipulation'],
    "url": "https://leetcode.com/problems/hamming-distance/",
    "companies": ['Facebook', 'Amazon', 'Microsoft'],
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
}
