"""
LeetCode Problem #48: Rotate Image
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/rotate-image/

Problem:
--------
You are given an `n x n` 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Constraints:
-----------
- `n == matrix.length == matrix[i].length
- 1000

Examples:
---------
Example 1:
```

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

```

Example 2:
```

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

```
"""

from typing import List, Optional
from collections import deque


class Solution:
    """
    Solution to LeetCode Problem #48: Rotate Image

    Approach: Two-step transformation: First transpose the matrix (swap rows and columns),
              then reverse each row. This achieves 90-degree clockwise rotation in-place.
    Time Complexity: O(n^2) - Visit each element twice (once for transpose, once for reverse)
    Space Complexity: O(1) - In-place modification, no extra space used

    Key Insights:
    - 90-degree clockwise rotation = Transpose + Reverse each row
    - 90-degree counter-clockwise rotation = Transpose + Reverse each column
    - Transpose swaps matrix[i][j] with matrix[j][i] for i < j
    - Alternative: 4-way swap rotating elements in groups of 4 (layer by layer)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        pass



PROBLEM_METADATA = {
    "number": 48,
    "name": "Rotate Image",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Math', 'Matrix'],
    "url": "https://leetcode.com/problems/rotate-image/",
    "companies": ["Amazon", "Google", "Microsoft", "Apple", "Facebook", "Bloomberg", "Adobe"],
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
}