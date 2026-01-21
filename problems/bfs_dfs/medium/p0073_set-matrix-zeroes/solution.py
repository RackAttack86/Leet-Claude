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

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 73,
    "name": "Set Matrix Zeroes",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Hash Table', 'Matrix'],
    "url": "https://leetcode.com/problems/set-matrix-zeroes/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
