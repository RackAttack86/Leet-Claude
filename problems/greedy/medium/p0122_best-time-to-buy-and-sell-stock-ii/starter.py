"""
LeetCode Problem #122: Best Time to Buy and Sell Stock II
Difficulty: Medium
Pattern: Greedy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Problem:
--------
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Constraints:
-----------
- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4

Examples:
---------
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #122: Best Time to Buy and Sell Stock II

    Approach: Greedy: sum all positive differences
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Capture every upward movement
    - Add profit whenever price increases
    - Multiple transactions allowed
    - Sum all positive price differences
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 122,
    "name": "Best Time to Buy and Sell Stock II",
    "difficulty": "Medium",
    "pattern": "Greedy",
    "topics": ['Array', 'Dynamic Programming', 'Greedy'],
    "url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}