"""
LeetCode Problem #289: Game of Life
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/game-of-life/

Problem:
--------
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: live (represented by a `1`) or dead (represented by a `0`). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies as if caused by under-population.
	
- Any live cell with two or three live neighbors lives on to the next generation.
	
- Any live cell with more than three live neighbors dies, as if by over-population.
	
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the `m x n` grid `board`. In this process, births and deaths occur simultaneously.

Given the current state of the `board`, update the `board` to reflect its next state.

Note that you do not need to return anything.

Constraints:
-----------
- `m == board.length
- n == board[i].length
- board[i][j]` is `0` or `1`.

Examples:
---------
Example 1:
```

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

```

Example 2:
```

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

```
"""

from typing import List, Optional
from collections import deque


class Solution:
    """
    Solution to LeetCode Problem #289: Game of Life

    Approach: Use intermediate states to encode transitions in-place. Use 2 for
              cells that were alive and will die, and 3 for cells that were dead
              and will become alive. This preserves original state while marking changes.
              After processing all cells, convert intermediate states to final values.
    Time Complexity: O(m*n) - Visit each cell once and check 8 neighbors
    Space Complexity: O(1) - In-place modification using intermediate states

    Key Insights:
    - Use extra states: 2 = alive->dead, 3 = dead->alive (encode both old and new state)
    - Original state can be recovered with value % 2 (both 0 and 2 give 0, 1 and 3 give 1)
    - Final state: 0->0, 1->1 if 2-3 neighbors, 2->0, 3->1
    - Check all 8 neighbors for each cell using direction vectors
    """

    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        # 8 directions: horizontal, vertical, and diagonal neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]

        def count_live_neighbors(row, col):
            count = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n:
                    # Count original live cells (1 or 2, since 2 means was alive)
                    if board[nr][nc] in (1, 2):
                        count += 1
            return count

        # First pass: mark transitions with intermediate states
        # 2 = alive -> dead, 3 = dead -> alive
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)

                if board[i][j] == 1:  # Currently alive
                    # Dies if < 2 or > 3 neighbors
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # Mark as alive -> dead
                else:  # Currently dead
                    # Becomes alive if exactly 3 neighbors
                    if live_neighbors == 3:
                        board[i][j] = 3  # Mark as dead -> alive

        # Second pass: convert intermediate states to final states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0  # Was alive, now dead
                elif board[i][j] == 3:
                    board[i][j] = 1  # Was dead, now alive


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 289,
    "name": "Game of Life",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Matrix', 'Simulation'],
    "url": "https://leetcode.com/problems/game-of-life/",
    "companies": ["Amazon", "Google", "Microsoft", "Dropbox", "Snapchat", "Two Sigma", "Bloomberg"],
    "time_complexity": "O(m*n)",
    "space_complexity": "O(1)",
}
