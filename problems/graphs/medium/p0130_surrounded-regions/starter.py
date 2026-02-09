"""
LeetCode Problem #130: Surrounded Regions
Difficulty: Medium
Pattern: Graphs
Link: https://leetcode.com/problems/surrounded-regions/

Problem:
--------
You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`, capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.

- Region: To form a region connect every `'O'` cell.

- Surround: The region is surrounded with `'X'` cells if you can connect the region with `'X'` cells and none of the region cells are on the edge of the `board`.

To capture a surrounded region, replace all `'O'`s with `'X'`s in-place within the original board. You do not need to return anything.

Constraints:
-----------
- `m == board.length
- n == board[i].length
- board[i][j]` is `'X'` or `'O'`.

Examples:
---------
Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]

Output: [["X"]]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #130: Surrounded Regions

    Approach: Border DFS/BFS - Mark cells connected to border as safe

    Instead of finding surrounded regions directly, we flip the problem:
    1. Find all 'O's connected to the border (these cannot be captured)
    2. Mark them temporarily with a different character
    3. All remaining 'O's are surrounded - convert them to 'X'
    4. Restore the border-connected cells back to 'O'

    Time Complexity: O(m * n) - visit each cell at most once
    Space Complexity: O(m * n) - recursion stack in worst case (all O's connected)

    Key Insights:
    - 'O' cells on the border can never be captured
    - Any 'O' connected to a border 'O' is also safe
    - Use DFS/BFS from border cells to mark safe regions
    - Remaining 'O's after marking are surrounded
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Capture all surrounded 'O' regions by converting them to 'X'.
        """
        pass



PROBLEM_METADATA = {
    "number": 130,
    "name": "Surrounded Regions",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Array', 'Depth-First Search', 'Breadth-First Search', 'Union-Find', 'Matrix'],
    "url": "https://leetcode.com/problems/surrounded-regions/",
    "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Bloomberg"],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
}