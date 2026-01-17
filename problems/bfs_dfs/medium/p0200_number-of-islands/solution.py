"""
LeetCode Problem #200: Number of Islands
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/number-of-islands/

Problem:
--------
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.

Constraints:
-----------
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'

Examples:
---------
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #200: Number of Islands

    Approach: DFS or BFS
    Time Complexity: O(m * n)
    Space Complexity: O(m * n) for recursion/queue

    Key Insights:
    - DFS/BFS from each unvisited land cell
    - Mark visited cells
    - Count number of DFS/BFS calls
    - Classic connected components problem
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 200,
    "name": "Number of Islands",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ["Array", "Depth-First Search", "Breadth-First Search", "Union Find", "Matrix"],
    "url": "https://leetcode.com/problems/number-of-islands/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Bloomberg", "Apple"],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
}
