"""
LeetCode Problem #64: Minimum Path Sum
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/minimum-path-sum/

Problem:
--------
Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Constraints:
-----------
- `m == grid.length
- n == grid[i].length

Examples:
---------
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
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #64: Minimum Path Sum

    Approach: Dynamic Programming with space optimization
    - Use a 1D DP array where dp[j] represents the minimum path sum to reach cell (i, j).
    - For each cell, we can only come from above or from the left.
    - dp[j] = grid[i][j] + min(dp[j], dp[j-1])
    - Process row by row, updating the dp array in place.

    Time Complexity: O(m * n)
    Space Complexity: O(n) - using 1D array optimization

    Key Insights:
    1. Each cell can only be reached from above or from the left.
    2. The minimum path to any cell is the cell's value plus the minimum of paths from above and left.
    3. First row can only be reached from the left, first column only from above.
    4. We can optimize space from O(m*n) to O(n) by using a single row.
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Find the minimum path sum from top-left to bottom-right.

        Args:
            grid: 2D grid of non-negative integers

        Returns:
            Minimum sum of values along any path from top-left to bottom-right
        """
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


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 64,
    "name": "Minimum Path Sum",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['Array', 'Dynamic Programming', 'Matrix'],
    "url": "https://leetcode.com/problems/minimum-path-sum/",
    "companies": ["Amazon", "Google", "Microsoft", "Goldman Sachs", "Bloomberg", "Apple", "Facebook", "Adobe"],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(n)",
}
