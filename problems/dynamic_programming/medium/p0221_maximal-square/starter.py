"""
LeetCode Problem #221: Maximal Square
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/maximal-square/

Problem:
--------
Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, find the largest square containing only `1`'s and return its area.

Constraints:
-----------
- `m == matrix.length
- n == matrix[i].length
- matrix[i][j]` is `'0'` or `'1'`.

Examples:
---------
Example 1:
```

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

```

Example 2:
```

Input: matrix = [["0","1"],["1","0"]]
Output: 1

```

Example 3:
```

Input: matrix = [["0"]]
Output: 0

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #221: Maximal Square

    Approach: Dynamic Programming with space optimization
    - dp[i][j] represents the side length of the largest square with bottom-right corner at (i, j).
    - If matrix[i][j] == '1', then dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    - The answer is the maximum dp value squared.
    - Optimize space to O(n) using a single row.

    Time Complexity: O(m * n)
    Space Complexity: O(n) - using 1D array optimization

    Key Insights:
    1. A square at (i,j) can only extend if all three neighbors (top, left, top-left) can form squares.
    2. The size is limited by the smallest of the three neighbors.
    3. This is because any larger square would require all three directions to have equally large squares.
    4. We need to track the previous diagonal value when using 1D optimization.
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Find the area of the largest square containing only 1s.

        Args:
            matrix: 2D binary matrix of '0' and '1' characters

        Returns:
            Area of the largest square containing only 1s
        """
        pass



PROBLEM_METADATA = {
    "number": 221,
    "name": "Maximal Square",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['Array', 'Dynamic Programming', 'Matrix'],
    "url": "https://leetcode.com/problems/maximal-square/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Apple", "Bloomberg", "Uber", "Airbnb", "IBM"],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(n)",
}