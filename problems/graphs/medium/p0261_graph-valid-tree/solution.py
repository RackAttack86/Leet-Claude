"""
LeetCode Problem #261: Graph Valid Tree
Difficulty: Medium
Pattern: Graphs
Link: https://leetcode.com/problems/graph-valid-tree/

Problem:
--------
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Constraints:
-----------
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no self-loops or repeated edges

Examples:
---------
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #261: Graph Valid Tree

    Approach: Union Find or DFS
    Time Complexity: O(E)
    Space Complexity: O(n)

    Key Insights:
    - Valid tree has n-1 edges
    - Must be connected and acyclic
    - Use Union Find to detect cycles
    - Or DFS to check connectivity and cycles
    """

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Determine if the graph is a valid tree.

        Args:
            n: Number of nodes
            edges: List of edges [a, b]

        Returns:
            True if graph is a valid tree, False otherwise

        Approach:
        1. A valid tree has exactly n-1 edges
        2. Must be connected (all nodes reachable)
        3. Must be acyclic
        4. Use Union Find to detect cycles and check connectivity
        """
        # A tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # Union Find implementation
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x: int, y: int) -> bool:
            """Returns False if x and y are already connected (cycle detected)."""
            px, py = find(x), find(y)
            if px == py:
                return False  # Cycle detected
            # Union by rank
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        # Process all edges
        for a, b in edges:
            if not union(a, b):
                return False  # Cycle detected

        # If we have n-1 edges and no cycles, it's a valid tree
        return True


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 261,
    "name": "Graph Valid Tree",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Depth-First Search', 'Breadth-First Search', 'Union Find', 'Graph'],
    "url": "https://leetcode.com/problems/graph-valid-tree/",
    "companies": ['Amazon', 'Facebook', 'Google'],
    "time_complexity": "O(E)",
    "space_complexity": "O(n)",
}
