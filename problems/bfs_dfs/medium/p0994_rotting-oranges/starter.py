"""
LeetCode Problem #994: Rotting Oranges
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/rotting-oranges/

Problem:
--------
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Constraints:
-----------
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2

Examples:
---------
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #994: Rotting Oranges

    Approach: Multi-source BFS
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    Key Insights:
    - Start BFS from all rotten oranges
    - Track time/levels of BFS
    - Count fresh oranges remaining
    - Return -1 if fresh oranges remain
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 994,
    "name": "Rotting Oranges",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Breadth-First Search', 'Matrix'],
    "url": "https://leetcode.com/problems/rotting-oranges/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
}