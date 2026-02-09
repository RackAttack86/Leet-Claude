"""
LeetCode Problem #121: Best Time to Buy and Sell Stock
Difficulty: Easy
Pattern: Greedy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem:
--------
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

Constraints:
-----------
- `1

Examples:
---------
Example 1:
```

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```

Example 2:
```

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #121: Best Time to Buy and Sell Stock

    Approach: One-pass greedy approach. Track the minimum price seen so far
    and calculate the maximum profit at each step by comparing the current
    price minus the minimum price with the current maximum profit.

    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(1) - only using two variables

    Key Insights:
    1. We need to buy before we sell, so we track the minimum price seen so far
    2. At each position, the best profit is current price - minimum price so far
    3. We greedily update both minimum price and maximum profit as we iterate
    4. If prices are strictly decreasing, the answer is 0 (no profitable transaction)
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find the maximum profit from buying and selling stock once.

        Args:
            prices: List of stock prices where prices[i] is the price on day i

        Returns:
            Maximum profit achievable, or 0 if no profit is possible
        """
        pass



PROBLEM_METADATA = {
    "number": 121,
    "name": "Best Time to Buy and Sell Stock",
    "difficulty": "Easy",
    "pattern": "Greedy",
    "topics": ['Array', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
    "companies": ["Amazon", "Facebook", "Microsoft", "Google", "Apple", "Bloomberg", "Goldman Sachs", "Uber", "Adobe", "Morgan Stanley"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}