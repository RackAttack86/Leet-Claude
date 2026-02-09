# Problem 322: Coin Change

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/coin-change/)

## Problem Description

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

### Constraints

- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

### Examples

**Example 1:**
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**
```
Input: coins = [2], amount = 3
Output: -1
```

## Approaches

### 1. Dynamic Programming (Unbounded Knapsack)

**Time Complexity:** O(amount * n) where n is number of coins
**Space Complexity:** O(amount)

```python
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

**Why this works:**

This is an unbounded knapsack problem. dp[i] represents the minimum number of coins needed to make amount i. For each amount, we try all coin denominations and take the minimum: dp[i] = min(dp[i], dp[i-coin] + 1). We initialize with infinity except dp[0] = 0.

## Key Insights

1. dp[i] = minimum coins to make amount i
2. dp[i] = min(dp[i], dp[i-coin] + 1) for each coin
3. Initialize dp with infinity except dp[0] = 0
4. Bottom-up DP is more efficient than top-down for this problem

## Common Mistakes

1. Not initializing dp[0] = 0
2. Forgetting to check if coin <= i before using it
3. Returning dp[amount] without checking if it's still infinity

## Related Problems

- Coin Change 2
- Minimum Cost For Tickets
- Perfect Squares

## Tags

Array, Dynamic Programming, BFS
