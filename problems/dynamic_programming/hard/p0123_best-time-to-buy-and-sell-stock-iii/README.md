# Problem 123: Best Time to Buy and Sell Stock III

**Difficulty:** Hard
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

## Constraints

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^5

## Examples

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

## Approaches

### 1. State Machine / DP with Four States

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0

    # Initialize states
    buy1 = float('-inf')   # cost of first purchase (negative represents spending)
    sell1 = 0              # profit after first complete transaction
    buy2 = float('-inf')   # effective cost after second purchase
    sell2 = 0              # profit after both transactions

    for price in prices:
        # Update in reverse order to use previous day's values
        sell2 = max(sell2, buy2 + price)
        buy2 = max(buy2, sell1 - price)
        sell1 = max(sell1, buy1 + price)
        buy1 = max(buy1, -price)

    return sell2
```

**Why this works:**

We model this as a state machine with 4 states tracking the maximum profit at each stage. buy1 tracks the minimum cost for first purchase, sell1 tracks profit after first transaction, buy2 tracks effective cost for second purchase (considering first profit), and sell2 tracks final profit after both transactions.

## Key Insights

1. We can model this as a state machine with 4 states (buy1, sell1, buy2, sell2).
2. buy1 tracks the minimum cost for first purchase (as negative profit).
3. sell1 tracks the maximum profit after first complete transaction.
4. buy2 tracks the minimum effective cost for second purchase (considering profit from first).
5. sell2 tracks the maximum profit after both transactions.
6. The order of updates matters - we update from sell2 backwards to buy1 to avoid using same day's values.

## Common Mistakes

1. Not understanding the state machine model
2. Updating states in the wrong order (would use same day's price twice)
3. Not handling the case where only one transaction is optimal

## Related Problems

- Best Time to Buy and Sell Stock
- Best Time to Buy and Sell Stock II
- Best Time to Buy and Sell Stock IV
