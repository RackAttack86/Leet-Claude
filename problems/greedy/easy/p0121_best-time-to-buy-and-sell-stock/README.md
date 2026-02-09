# Problem 121: Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## Examples

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

## Approaches

### 1. One-Pass Greedy

**Time Complexity:** O(n) - single pass through the array
**Space Complexity:** O(1) - only using two variables

```python
def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # Update minimum price seen so far
        min_price = min(min_price, price)
        # Calculate profit if we sell at current price
        current_profit = price - min_price
        # Update maximum profit
        max_profit = max(max_profit, current_profit)

    return max_profit
```

**Why this works:**
Track the minimum price seen so far and calculate the maximum profit at each step by comparing the current price minus the minimum price with the current maximum profit.

## Key Insights

1. We need to buy before we sell, so we track the minimum price seen so far
2. At each position, the best profit is current price - minimum price so far
3. We greedily update both minimum price and maximum profit as we iterate
4. If prices are strictly decreasing, the answer is 0 (no profitable transaction)

## Common Mistakes

1. Trying to find maximum and minimum without considering order (must buy before sell)
2. Not handling the case of empty array or single element
3. Using O(n^2) brute force instead of one-pass solution

## Related Problems

- 122. Best Time to Buy and Sell Stock II
- 123. Best Time to Buy and Sell Stock III
- 188. Best Time to Buy and Sell Stock IV
