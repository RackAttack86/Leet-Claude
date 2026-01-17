"""
LeetCode Problem #121: Best Time to Buy and Sell Stock
Difficulty: Easy
Pattern: Sliding Window
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem:
--------
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any
profit, return 0.

Constraints:
-----------
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Examples:
---------
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #121: Best Time to Buy and Sell Stock

    Approach: One pass tracking minimum price
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Track minimum price seen so far
    - Calculate profit at each step
    - Update maximum profit
    - Single pass solution
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 121,
    "name": "Best Time to Buy and Sell Stock",
    "difficulty": "Easy",
    "pattern": "Sliding Window",
    "topics": ["Array", "Dynamic Programming"],
    "url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Bloomberg", "Apple", "Goldman Sachs"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
