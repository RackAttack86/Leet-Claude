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

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 289,
    "name": "Game of Life",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Matrix', 'Simulation'],
    "url": "https://leetcode.com/problems/game-of-life/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
