"""
LeetCode Problem #73: Set Matrix Zeroes
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/set-matrix-zeroes/

Problem:
--------
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place.

Constraints:
-----------
- `m == matrix.length
- n == matrix[0].length
- 2^31

Examples:
---------
Example 1:
```

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

```

Example 2:
```

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

```
"""

from typing import List, Optional
from collections import Counter, defaultdict, deque


class Solution:
    """
    Solution to LeetCode Problem #73: Set Matrix Zeroes

    Approach: Use the first row and first column as markers to track which rows/columns
              need to be zeroed. Use separate flags for whether the first row and first
              column themselves should be zeroed. This achieves O(1) space complexity.
    Time Complexity: O(m*n) - Two passes through the matrix
    Space Complexity: O(1) - Use matrix itself as storage for markers

    Key Insights:
    - First row and first column can serve as "marker arrays" instead of extra space
    - Need separate flags for first row/column since they're used as markers
    - Process: 1) Mark, 2) Zero inner cells, 3) Zero first row/column if needed
    - Process inner matrix first (1 to m-1, 1 to n-1), then handle first row/column
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        pass



PROBLEM_METADATA = {
    "number": 73,
    "name": "Set Matrix Zeroes",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Hash Table', 'Matrix'],
    "url": "https://leetcode.com/problems/set-matrix-zeroes/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Apple", "Bloomberg", "Oracle"],
    "time_complexity": "O(m*n)",
    "space_complexity": "O(1)",
}