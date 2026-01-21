"""
LeetCode Problem #63: Unique Paths II
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/unique-paths-ii/

Problem:
--------
You are given an `m x n` integer array `grid`. There is a robot initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to `2 * 10^9`.

Constraints:
-----------
- `m == obstacleGrid.length
- n == obstacleGrid[i].length
- obstacleGrid[i][j]` is `0` or `1`.

Examples:
---------
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
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #63: Unique Paths II

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 63,
    "name": "Unique Paths II",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['Array', 'Dynamic Programming', 'Matrix'],
    "url": "https://leetcode.com/problems/unique-paths-ii/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
