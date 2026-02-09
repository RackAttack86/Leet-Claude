# Problem 121: Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Problem Description

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any
profit, return 0.

### Constraints

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

### Examples

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

## Approaches

### 1. One Pass Tracking Minimum Price

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
```

**Why this works:**

We track the minimum price seen so far as we iterate through the array. At each step, we calculate the potential profit if we were to sell at the current price (current price - minimum price seen). We keep track of the maximum profit found. This works because we need to buy before we sell, and we're always comparing the current price against the lowest price we've seen in the past.

## Key Insights

- Track minimum price seen so far
- Calculate profit at each step
- Update maximum profit
- Single pass solution

## Common Mistakes

- Forgetting to handle empty array
- Trying to sell before buying (not tracking the minimum correctly)
- Using O(n^2) brute force when O(n) is possible

## Related Problems

- Best Time to Buy and Sell Stock II
- Best Time to Buy and Sell Stock III
- Best Time to Buy and Sell Stock IV

## Tags

Array, Dynamic Programming
