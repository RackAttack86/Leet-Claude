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
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



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