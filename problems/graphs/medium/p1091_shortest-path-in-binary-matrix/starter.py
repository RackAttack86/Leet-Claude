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
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



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