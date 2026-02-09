"""
LeetCode Problem #1135: Connecting Cities With Minimum Cost
Difficulty: Medium
Pattern: Graphs
Link: https://leetcode.com/problems/connecting-cities-with-minimum-cost/

Problem:
--------
There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1.

The cost is the sum of the connections' costs used.

Constraints:
-----------
- 1 <= n <= 10^4
- 1 <= connections.length <= 10^4
- connections[i].length == 3
- 1 <= xi, yi <= n
- xi != yi
- 0 <= costi <= 10^5

Examples:
---------
Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.

Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #1135: Connecting Cities With Minimum Cost

    Approach: Minimum Spanning Tree (Kruskal's or Prim's)
    Time Complexity: O(E log E)
    Space Complexity: O(V)

    Key Insights:
    - Sort edges by cost
    - Use Union Find to build MST
    - Add edge if it connects new components
    - Check if all nodes connected at end
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 1135,
    "name": "Connecting Cities With Minimum Cost",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Union Find', 'Graph', 'Minimum Spanning Tree'],
    "url": "https://leetcode.com/problems/connecting-cities-with-minimum-cost/",
    "companies": ['Amazon', 'Google'],
    "time_complexity": "O(E log E)",
    "space_complexity": "O(V)",
}