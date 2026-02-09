"""
LeetCode Problem #323: Number of Connected Components in an Undirected Graph
Difficulty: Medium
Pattern: Graphs
Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Problem:
--------
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Constraints:
-----------
- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges

Examples:
---------
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #323: Number of Connected Components in an Undirected Graph

    Approach: Union Find or DFS
    Time Complexity: O(E * α(n)) for Union Find
    Space Complexity: O(n)

    Key Insights:
    - Start with n components
    - Union connected nodes
    - Count remaining distinct roots
    - Classic Union Find application
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 323,
    "name": "Number of Connected Components in an Undirected Graph",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Depth-First Search', 'Breadth-First Search', 'Union Find', 'Graph'],
    "url": "https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/",
    "companies": ['Amazon', 'Facebook', 'Google', 'LinkedIn'],
    "time_complexity": "O(E * α(n)) for Union Find",
    "space_complexity": "O(n)",
}