"""
LeetCode Problem #909: Snakes and Ladders
Difficulty: Medium
Pattern: Graphs
Link: https://leetcode.com/problems/snakes-and-ladders/

Problem:
--------
You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to `n^2` in a Boustrophedon style starting from the bottom left of the board (i.e. `board[n - 1][0]`) and alternating direction each row.

You start on square `1` of the board. In each move, starting from square `curr`, do the following:

- Choose a destination square `next` with a label in the range `[curr + 1, min(curr + 6, n^2)]`.

- This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.

- If `next` has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to `next`.

- The game ends when you reach the square `n^2`.

A board square on row `r` and column `c` has a snake or ladder if `board[r][c] != -1`. The destination of that snake or ladder is `board[r][c]`. Squares `1` and `n^2` are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

- For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first move, your destination square is `2`. You follow the ladder to square `3`, but do not follow the subsequent ladder to `4`.

Return the least number of dice rolls required to reach the square `n^2`. If it is not possible to reach the square, return `-1`.

Constraints:
-----------
- `n == board.length == board[i].length
- board[i][j]` is either `-1` or in the range `[1, n^2]`.
- The squares labeled `1` and `n^2` are not the starting points of any snake or ladder.

Examples:
---------
Example 1:
```

Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

```

Example 2:
```

Input: board = [[-1,-1],[-1,3]]
Output: 1

```
"""

from typing import List, Optional
from collections import deque


class Solution:
    """
    Solution to LeetCode Problem #909: Snakes and Ladders

    Approach: BFS for Shortest Path with Coordinate Conversion

    Model the board as a graph where each square is a node.
    From square s, we can reach s+1 to s+6 (with snake/ladder teleportation).
    Use BFS to find minimum dice rolls (edges) to reach n^2.

    Key challenge: Convert square number to (row, col) in Boustrophedon pattern.

    Time Complexity: O(n^2) - visit each square at most once
    Space Complexity: O(n^2) - visited set and queue

    Key Insights:
    - Boustrophedon: odd rows (from bottom) go left-to-right, even go right-to-left
    - Only take snake/ladder once per roll (don't chain)
    - BFS guarantees minimum moves
    - Square 1 is at (n-1, 0), square n is at (n-1, n-1) or (n-1, 0) depending on n
    """

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Find minimum dice rolls to reach the last square.
        """
        n = len(board)
        target = n * n

        def get_board_value(square: int) -> int:
            """Convert square number (1-indexed) to board value."""
            # Convert to 0-indexed
            s = square - 1
            # Row from bottom (0-indexed from bottom)
            row_from_bottom = s // n
            # Actual row in board
            row = n - 1 - row_from_bottom
            # Column depends on direction (alternating)
            col_in_row = s % n
            if row_from_bottom % 2 == 0:
                # Left to right
                col = col_in_row
            else:
                # Right to left
                col = n - 1 - col_in_row
            return board[row][col]

        # BFS
        queue = deque([(1, 0)])  # (current_square, rolls)
        visited = {1}

        while queue:
            curr, rolls = queue.popleft()

            # Try all 6 dice outcomes
            for dice in range(1, 7):
                next_square = curr + dice

                if next_square > target:
                    continue

                # Check for snake or ladder
                board_val = get_board_value(next_square)
                if board_val != -1:
                    next_square = board_val

                # Reached the end
                if next_square == target:
                    return rolls + 1

                # Add to queue if not visited
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, rolls + 1))

        return -1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 909,
    "name": "Snakes and Ladders",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Array', 'Breadth-First Search', 'Matrix'],
    "url": "https://leetcode.com/problems/snakes-and-ladders/",
    "companies": ["Amazon", "Google", "Microsoft", "Goldman Sachs", "Apple"],
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
}
