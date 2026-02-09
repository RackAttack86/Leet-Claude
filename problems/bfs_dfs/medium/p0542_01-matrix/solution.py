"""
LeetCode Problem #542: 01 Matrix
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/01-matrix/

Problem:
--------
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Constraints:
-----------
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- mat[i][j] is either 0 or 1
- There is at least one 0 in mat

Examples:
---------
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from typing import List, Optional
from collections import deque


class Solution:
    """
    Solution to LeetCode Problem #542: 01 Matrix

    Approach: Multi-source BFS
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    Key Insights:
    - Start BFS from all 0s simultaneously
    - Update distances level by level
    - Similar to walls and gates
    - BFS guarantees shortest distance
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat

        rows, cols = len(mat), len(mat[0])
        queue = deque()
        result = [[float('inf')] * cols for _ in range(rows)]

        # Add all 0s to queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    queue.append((r, c))

        # BFS from all 0s
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if result[nr][nc] > result[r][c] + 1:
                        result[nr][nc] = result[r][c] + 1
                        queue.append((nr, nc))

        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 542,
    "name": "01 Matrix",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Dynamic Programming', 'Breadth-First Search', 'Matrix'],
    "url": "https://leetcode.com/problems/01-matrix/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
}
