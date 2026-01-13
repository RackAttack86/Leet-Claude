"""
LeetCode Problem #322: Coin Change
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/coin-change/

Problem:
--------
You are given an integer array coins representing coins of different denominations and an
integer amount representing a total amount of money. Return the fewest number of coins
that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1. You may assume that you have an infinite number of
each kind of coin.

Constraints:
-----------
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

Examples:
---------
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #322: Coin Change

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 322,
    "name": "Coin Change",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ["Array", "Dynamic Programming", "BFS"],
    "url": "https://leetcode.com/problems/coin-change/",
    "companies": ["Amazon", "Uber", "Bloomberg"],
    "time_complexity": "O(amount * n)",
    "space_complexity": "O(amount)",
}
