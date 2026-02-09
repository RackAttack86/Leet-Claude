"""
LeetCode Problem #1162: As Far from Land as Possible
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/as-far-from-land-as-possible/

Problem:
--------
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Constraints:
-----------
- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1

Examples:
---------
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
"""

from typing import List, Optional
from collections import deque


class Solution:
    """
    Solution to LeetCode Problem #1162: As Far from Land as Possible

    Approach: Multi-source BFS
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)

    Key Insights:
    - Start BFS from all land cells
    - Find maximum distance to any water
    - BFS calculates distances correctly
    - Return -1 if all land or all water
    """

    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        # Add all land cells to queue
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))

        # If all land or all water
        if len(queue) == 0 or len(queue) == n * n:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        distance = -1

        while queue:
            size = len(queue)
            distance += 1
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1  # Mark as visited
                        queue.append((nr, nc))

        return distance


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 1162,
    "name": "As Far from Land as Possible",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Dynamic Programming', 'Breadth-First Search', 'Matrix'],
    "url": "https://leetcode.com/problems/as-far-from-land-as-possible/",
    "companies": ['Amazon', 'Google'],
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
}
