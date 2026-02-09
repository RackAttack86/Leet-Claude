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

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r: int, c: int, reachable: set, prev_height: int):
            if (r, c) in reachable:
                return
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if heights[r][c] < prev_height:
                return

            reachable.add((r, c))
            dfs(r + 1, c, reachable, heights[r][c])
            dfs(r - 1, c, reachable, heights[r][c])
            dfs(r, c + 1, reachable, heights[r][c])
            dfs(r, c - 1, reachable, heights[r][c])

        # DFS from Pacific borders (top and left)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])

        # DFS from Atlantic borders (bottom and right)
        for c in range(cols):
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # Return intersection
        return [[r, c] for r, c in pacific & atlantic]


# Metadata for tracking
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
