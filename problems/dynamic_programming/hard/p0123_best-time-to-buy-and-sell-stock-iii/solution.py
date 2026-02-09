"""
LeetCode Problem #123: Best Time to Buy and Sell Stock III
Difficulty: Hard
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Problem:
--------
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Constraints:
-----------
- `1

Examples:
---------
Example 1:
```

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

Example 2:
```

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

```

Example 3:
```

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #123: Best Time to Buy and Sell Stock III

    Approach: State Machine / DP with four states
    - Track four states representing the maximum profit at each stage:
      * buy1: Maximum profit after first buy (most negative cost)
      * sell1: Maximum profit after first sell
      * buy2: Maximum profit after second buy
      * sell2: Maximum profit after second sell
    - For each price, update all states based on the best action.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    1. We can model this as a state machine with 4 states (buy1, sell1, buy2, sell2).
    2. buy1 tracks the minimum cost for first purchase (as negative profit).
    3. sell1 tracks the maximum profit after first complete transaction.
    4. buy2 tracks the minimum effective cost for second purchase (considering profit from first).
    5. sell2 tracks the maximum profit after both transactions.
    6. The order of updates matters - we update from sell2 backwards to buy1 to avoid using same day's values.
    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate maximum profit with at most 2 transactions.

        Args:
            prices: List of daily stock prices

        Returns:
            Maximum profit achievable with at most 2 transactions
        """
        if not prices:
            return 0

        # Initialize states
        # buy1: cost of first purchase (negative represents spending money)
        buy1 = float('-inf')
        # sell1: profit after first complete transaction
        sell1 = 0
        # buy2: effective cost after second purchase (includes profit from first)
        buy2 = float('-inf')
        # sell2: profit after both transactions
        sell2 = 0

        for price in prices:
            # Update in reverse order to use previous day's values
            # Maximum profit after second sell
            sell2 = max(sell2, buy2 + price)
            # Maximum "profit" after second buy (includes first transaction's profit)
            buy2 = max(buy2, sell1 - price)
            # Maximum profit after first sell
            sell1 = max(sell1, buy1 + price)
            # Maximum "profit" after first buy (negative of cost)
            buy1 = max(buy1, -price)

        return sell2


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 123,
    "name": "Best Time to Buy and Sell Stock III",
    "difficulty": "Hard",
    "pattern": "Dynamic Programming",
    "topics": ['Array', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Bloomberg", "Apple", "Goldman Sachs", "Uber", "Adobe"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
