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

    Approach: Dynamic Programming (unbounded knapsack)
    Time Complexity: O(amount * n) where n is number of coins
    Space Complexity: O(amount)

    Key Insights:
    - dp[i] = minimum coins to make amount i
    - dp[i] = min(dp[i], dp[i-coin] + 1) for each coin
    - Initialize dp with infinity except dp[0] = 0
    - Bottom-up DP is more efficient than top-down
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


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
