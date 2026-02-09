"""
LeetCode Problem #286: Walls and Gates
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/walls-and-gates/

Problem:
--------
You are given an m x n grid rooms initialized with these three possible values.

-1: A wall or an obstacle.
0: A gate.
INF: Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Constraints:
-----------
- m == rooms.length
- n == rooms[i].length
- 1 <= m, n <= 250
- rooms[i][j] is -1, 0, or 2^31 - 1

Examples:
---------
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Input: rooms = [[-1]]
Output: [[-1]]
"""

from typing import List, Optional
from collections import deque


class Solution:
    """
    Solution to LeetCode Problem #286: Walls and Gates

    Approach: Multi-source BFS
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    Key Insights:
    - Start BFS from all gates simultaneously
    - Update distances level by level
    - Each cell visited once
    - Multi-source BFS is efficient
    """

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Modify rooms in-place with distance to nearest gate.
        """
        if not rooms or not rooms[0]:
            return

        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        # Add all gates to queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        # BFS from all gates simultaneously
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 286,
    "name": "Walls and Gates",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Breadth-First Search', 'Matrix'],
    "url": "https://leetcode.com/problems/walls-and-gates/",
    "companies": ['Amazon', 'Facebook', 'Google'],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
}
