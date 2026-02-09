# Problem 64: Minimum Path Sum

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/minimum-path-sum/)

## Problem Description

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200

## Examples

Example 1:
```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum.
```

Example 2:
```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
```

## Approaches

### 1. Dynamic Programming with Space Optimization

**Time Complexity:** O(m * n)
**Space Complexity:** O(n)

```python
def minPathSum(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # Initialize dp array with first row
    dp = [0] * n
    dp[0] = grid[0][0]

    # Fill the first row - can only come from the left
    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]

    # Fill the rest of the grid row by row
    for i in range(1, m):
        # First column - can only come from above
        dp[0] += grid[i][0]

        for j in range(1, n):
            # Take minimum of coming from above (dp[j]) or from left (dp[j-1])
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

    return dp[n - 1]
```

**Why this works:**

We use a 1D DP array where dp[j] represents the minimum path sum to reach cell (i, j). For each cell, we can only come from above or from the left, so dp[j] = grid[i][j] + min(dp[j], dp[j-1]). We process row by row, updating the dp array in place.

## Key Insights

1. Each cell can only be reached from above or from the left.
2. The minimum path to any cell is the cell's value plus the minimum of paths from above and left.
3. First row can only be reached from the left, first column only from above.
4. We can optimize space from O(m*n) to O(n) by using a single row.

## Common Mistakes

1. Not initializing the first row and column correctly
2. Using O(m*n) space when O(n) is sufficient
3. Forgetting that minimum comes from comparing above and left paths

## Related Problems

- Unique Paths
- Unique Paths II
- Triangle
- Dungeon Game
