# Problem 122: Best Time to Buy and Sell Stock II

**Difficulty:** Medium
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

## Problem Description

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

## Constraints

- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4

## Examples

Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
```

Example 2:
```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
```

## Approaches

### 1. Greedy: Sum All Positive Differences

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def maxProfit(self, prices: List[int]) -> int:
    profit = 0

    # Capture every upward movement
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit
```

**Why this works:**
Since we can make unlimited transactions, we should capture every upward movement in price. This is equivalent to buying before every price increase and selling immediately after.

## Key Insights

1. Capture every upward movement
2. Add profit whenever price increases
3. Multiple transactions allowed
4. Sum all positive price differences

## Common Mistakes

1. Trying to find optimal buy/sell points when simple greedy works
2. Overcomplicating with DP
3. Not realizing that capturing all increases is the same as optimal transactions

## Related Problems

- 121. Best Time to Buy and Sell Stock
- 123. Best Time to Buy and Sell Stock III
- 188. Best Time to Buy and Sell Stock IV

## Tags

Array, Dynamic Programming, Greedy
