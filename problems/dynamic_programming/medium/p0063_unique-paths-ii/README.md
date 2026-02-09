# Problem 63: Unique Paths II

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/unique-paths-ii/)

## Problem Description

You are given an `m x n` integer array `grid`. There is a robot initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to `2 * 10^9`.

## Constraints

- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is 0 or 1

## Examples

Example 1:
```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

Example 2:
```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

## Approaches

### 1. Dynamic Programming with Space Optimization

**Time Complexity:** O(m * n)
**Space Complexity:** O(n)

```python
def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])

    # If start or end has obstacle, no path exists
    if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
        return 0

    # Initialize dp array for the first row
    dp = [0] * n
    dp[0] = 1

    # Fill the dp array row by row
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                # Obstacle - no paths through this cell
                dp[j] = 0
            elif j > 0:
                # Add paths from the left cell
                dp[j] += dp[j - 1]
            # Note: dp[j] already contains paths from above (previous row)

    return dp[n - 1]
```

**Why this works:**

We use a 1D DP array where dp[j] represents the number of unique paths to reach cell (i, j). For cells with obstacles, we set dp[j] = 0. For other cells, dp[j] = dp[j] + dp[j-1] (paths from above + paths from left). We process row by row, updating the dp array in place.

## Key Insights

1. If start or end cell has an obstacle, return 0 immediately.
2. For the first row and first column, once we hit an obstacle, all subsequent cells are unreachable.
3. For any cell with an obstacle, set paths to 0.
4. We can optimize space from O(m*n) to O(n) by using a single row.

## Common Mistakes

1. Not checking if start or end position has an obstacle
2. Forgetting to reset dp[j] to 0 when encountering an obstacle
3. Not handling the first row/column correctly with obstacles

## Related Problems

- Unique Paths
- Minimum Path Sum
- Dungeon Game
