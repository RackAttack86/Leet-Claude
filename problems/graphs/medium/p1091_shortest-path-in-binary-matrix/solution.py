"""
LeetCode Problem #1091: Shortest Path in Binary Matrix
Difficulty: Medium
Pattern: Graphs
Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/

Problem:
--------
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Constraints:
-----------
- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1

Examples:
---------
Input: grid = [[0,1],[1,0]]
Output: 2

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #1091: Shortest Path in Binary Matrix

    Approach: BFS for shortest path
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)

    Key Insights:
    - BFS guarantees shortest path
    - 8 directions of movement
    - Mark visited cells
    - Return -1 if target unreachable
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Find shortest path from top-left to bottom-right in binary matrix.

        Args:
            grid: n x n binary matrix (0 = passable, 1 = blocked)

        Returns:
            Length of shortest clear path, or -1 if impossible

        Approach:
        1. Use BFS for shortest path
        2. 8-directional movement (including diagonals)
        3. Mark visited cells to avoid revisiting
        4. Return path length when reaching destination
        """
        from collections import deque

        n = len(grid)

        # Check if start or end is blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # Edge case: 1x1 grid
        if n == 1:
            return 1

        # 8 directions: up, down, left, right, and 4 diagonals
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        # BFS
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # Mark as visited

        while queue:
            row, col, length = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                # Check bounds and if cell is passable
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    if nr == n - 1 and nc == n - 1:
                        return length + 1

                    grid[nr][nc] = 1  # Mark as visited
                    queue.append((nr, nc, length + 1))

        return -1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 1091,
    "name": "Shortest Path in Binary Matrix",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Array', 'Breadth-First Search', 'Matrix'],
    "url": "https://leetcode.com/problems/shortest-path-in-binary-matrix/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
}
