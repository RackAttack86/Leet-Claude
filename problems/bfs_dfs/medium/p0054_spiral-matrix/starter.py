"""
LeetCode Problem #54: Spiral Matrix
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/spiral-matrix/

Problem:
--------
Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

Constraints:
-----------
- `m == matrix.length
- n == matrix[i].length
- 100

Examples:
---------
Example 1:
```

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

```

Example 2:
```

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

```
"""

from typing import List, Optional
from collections import deque


class Solution:
    """
    Solution to LeetCode Problem #54: Spiral Matrix

    Approach: Use four boundary pointers (top, bottom, left, right) to track the current
              spiral layer. Traverse right, down, left, up in order, shrinking boundaries
              after each direction is completed. Continue until all elements are visited.
    Time Complexity: O(m*n) - Visit each element exactly once
    Space Complexity: O(1) - Excluding output array, only use constant extra space

    Key Insights:
    - Maintain four boundaries and shrink them as we complete each direction
    - Order of traversal: right -> down -> left -> up (repeat)
    - Must check boundary conditions after traversing down and up to handle single row/column
    - The spiral peels off layers from outside to inside
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass



PROBLEM_METADATA = {
    "number": 54,
    "name": "Spiral Matrix",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Matrix', 'Simulation'],
    "url": "https://leetcode.com/problems/spiral-matrix/",
    "companies": ["Amazon", "Google", "Microsoft", "Apple", "Facebook", "Bloomberg", "Uber", "Oracle"],
    "time_complexity": "O(m*n)",
    "space_complexity": "O(1)",
}