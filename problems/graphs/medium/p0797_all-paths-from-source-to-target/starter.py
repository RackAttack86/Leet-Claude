"""
LeetCode Problem #797: All Paths From Source to Target
Difficulty: Medium
Pattern: Graphs
Link: https://leetcode.com/problems/all-paths-from-source-to-target/

Problem:
--------
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Constraints:
-----------
- n == graph.length
- 2 <= n <= 15
- 0 <= graph[i][j] < n
- graph[i][j] != i (i.e., there will be no self-loops)
- All the elements of graph[i] are unique
- The input graph is guaranteed to be a DAG

Examples:
---------
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #797: All Paths From Source to Target

    Approach: DFS backtracking
    Time Complexity: O(2^V * V)
    Space Complexity: O(V)

    Key Insights:
    - Use DFS to explore all paths
    - Backtrack to find all possibilities
    - Add path when reaching target
    - DAG guarantees termination
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 797,
    "name": "All Paths From Source to Target",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Backtracking', 'Depth-First Search', 'Breadth-First Search', 'Graph'],
    "url": "https://leetcode.com/problems/all-paths-from-source-to-target/",
    "companies": ['Amazon', 'Google', 'Facebook'],
    "time_complexity": "O(2^V * V)",
    "space_complexity": "O(V)",
}