"""
LeetCode Problem #417: Pacific Atlantic Water Flow
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

Problem:
--------
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Constraints:
-----------
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5

Examples:
---------
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans:
[[0,4]: [0,4] -> Pacific Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
...

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to both oceans.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #417: Pacific Atlantic Water Flow

    Approach: DFS from ocean borders
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    Key Insights:
    - DFS from Pacific and Atlantic borders
    - Mark cells reachable from each ocean
    - Find intersection of both sets
    - Reverse thinking: ocean to cells
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 417,
    "name": "Pacific Atlantic Water Flow",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Array', 'Depth-First Search', 'Breadth-First Search', 'Matrix'],
    "url": "https://leetcode.com/problems/pacific-atlantic-water-flow/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
}