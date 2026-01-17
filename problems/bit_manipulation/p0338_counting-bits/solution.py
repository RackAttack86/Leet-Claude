"""
LeetCode Problem #338: Counting Bits
Difficulty: Easy
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/counting-bits/

Problem:
--------
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Constraints:
-----------
- 0 <= n <= 10^5

Examples:
---------
Input: n = 2
Output: [0,1,1]
Explanation: 0 --> 0, 1 --> 1, 2 --> 10

Input: n = 5
Output: [0,1,1,2,1,2]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #338: Counting Bits

    Approach: Dynamic Programming with bit manipulation
    Time Complexity: O(n)
    Space Complexity: O(1) excluding output

    Key Insights:
    - ans[i] = ans[i >> 1] + (i & 1)
    - Each number's count relates to i/2
    - Or use ans[i] = ans[i & (i-1)] + 1
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 338,
    "name": "Counting Bits",
    "difficulty": "Easy",
    "pattern": "Bit Manipulation",
    "topics": ["Dynamic Programming", "Bit Manipulation"],
    "url": "https://leetcode.com/problems/counting-bits/",
    "companies": ["Amazon", "Google", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
