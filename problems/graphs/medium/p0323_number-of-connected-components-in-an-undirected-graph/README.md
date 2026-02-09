# Problem 323: Number of Connected Components in an Undirected Graph

**Difficulty:** Medium
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

## Problem Description

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

## Constraints

- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges

## Examples

Example 1:
```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

Example 2:
```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
```

## Approaches

### 1. Union Find

**Time Complexity:** O(E * a(n))
**Space Complexity:** O(n)

```python
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    """
    Count the number of connected components in the graph.
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
```

**Why this works:**

1. Use Union Find
2. Start with n components (each node is its own component)
3. For each edge, union the two nodes
4. Count remaining distinct roots

## Key Insights

- Start with n components
- Union connected nodes
- Count remaining distinct roots
- Classic Union Find application

## Common Mistakes

- Not initializing each node as its own component
- Forgetting path compression for efficiency
- Not decreasing component count when union is performed

## Related Problems

- Graph Valid Tree (261)
- Number of Islands (200)
- Friend Circles (547)

## Tags

Depth-First Search, Breadth-First Search, Union Find, Graph
