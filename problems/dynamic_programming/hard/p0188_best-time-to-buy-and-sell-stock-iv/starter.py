"""
LeetCode Problem #188: Best Time to Buy and Sell Stock IV
Difficulty: Hard
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Problem:
--------
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^th` day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions: i.e. you may buy at most `k` times and sell at most `k` times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Constraints:
-----------
- `1

Examples:
---------
Example 1:
```

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

```

Example 2:
```

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #188: Best Time to Buy and Sell Stock IV

    Approach: Dynamic Programming with state tracking
    - Generalize the Stock III solution to k transactions.
    - Track 2k states: buy[i] and sell[i] for each transaction i.
    - buy[i]: Maximum profit after i-th buy
    - sell[i]: Maximum profit after i-th sell
    - Optimization: If k >= n/2, we can make unlimited transactions (greedy approach).

    Time Complexity: O(n * k) or O(n) when k >= n/2
    Space Complexity: O(k)

    Key Insights:
    1. This is a generalization of Stock III (k=2 transactions).
    2. If k >= n/2, we can capture every profitable move (unlimited transactions case).
    3. For each transaction i: buy[i] = max(buy[i], sell[i-1] - price)
    4. For each transaction i: sell[i] = max(sell[i], buy[i] + price)
    5. The optimization for large k avoids TLE on edge cases.
    """
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        Calculate maximum profit with at most k transactions.

        Args:
            k: Maximum number of transactions allowed
            prices: List of daily stock prices

        Returns:
            Maximum profit achievable with at most k transactions
        """
        pass

    def _maxProfitUnlimited(self, prices: List[int]) -> int:
        """
        Calculate maximum profit with unlimited transactions (greedy approach).
        Capture every profitable price increase.
        """
        pass



PROBLEM_METADATA = {
    "number": 188,
    "name": "Best Time to Buy and Sell Stock IV",
    "difficulty": "Hard",
    "pattern": "Dynamic Programming",
    "topics": ['Array', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Bloomberg", "Goldman Sachs", "Apple", "Uber", "ByteDance"],
    "time_complexity": "O(n * k)",
    "space_complexity": "O(k)",
}