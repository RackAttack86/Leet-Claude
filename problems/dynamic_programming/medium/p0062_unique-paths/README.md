# Problem 62: Unique Paths

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/unique-paths/)

## Problem Description

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

### Constraints

- 1 <= m, n <= 100

### Examples

**Example 1:**
```
Input: m = 3, n = 7
Output: 28
```

**Example 2:**
```
Input: m = 3, n = 2
Output: 3
Explanation: From top-left corner, there are 3 ways to reach bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

## Approaches

### 1. Dynamic Programming (Space Optimized)

**Time Complexity:** O(m * n)
**Space Complexity:** O(n)

```python
def uniquePaths(self, m: int, n: int) -> int:
    # Use 1D DP array
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[n - 1]
```

**Why this works:**

Each cell can only be reached from the cell above or the cell to the left. Therefore, the number of paths to any cell is the sum of paths from both directions: dp[i][j] = dp[i-1][j] + dp[i][j-1]. We can optimize space to O(n) by using a single row since we only need the previous row's values.

## Key Insights

1. dp[i][j] = dp[i-1][j] + dp[i][j-1]
2. Can optimize to 1D array
3. Math solution: C(m+n-2, m-1) using combinations
4. Each cell's paths = sum of paths from top and left

## Common Mistakes

1. Not initializing the first row and column correctly (all should be 1)
2. Using O(m*n) space when O(n) is sufficient
3. Forgetting that the robot can only move right or down

## Related Problems

- Unique Paths II (with obstacles)
- Minimum Path Sum
- Dungeon Game

## Tags

Math, Dynamic Programming, Combinatorics
