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

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Count the number of connected components in the graph.

        Args:
            n: Number of nodes
            edges: List of edges [a, b]

        Returns:
            Number of connected components

        Approach:
        1. Use Union Find
        2. Start with n components (each node is its own component)
        3. For each edge, union the two nodes
        4. Count remaining distinct roots
        """
        # Union Find implementation
        parent = list(range(n))
        rank = [0] * n
        components = n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x: int, y: int) -> bool:
            """Returns True if union was performed (nodes were in different components)."""
            px, py = find(x), find(y)
            if px == py:
                return False  # Already in same component
            # Union by rank
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        # Process all edges
        for a, b in edges:
            if union(a, b):
                components -= 1

        return components


# Metadata for tracking
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
