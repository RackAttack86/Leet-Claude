# Problem 684: Redundant Connection

**Difficulty:** Medium
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/redundant-connection/)

## Problem Description

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

## Constraints

- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges
- The given graph is connected

## Examples

Example 1:
```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

Example 2:
```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

## Approaches

### 1. Union Find

**Time Complexity:** O(n * a(n))
**Space Complexity:** O(n)

```python
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    """
    Find the edge that can be removed to make the graph a tree.
    """
    n = len(edges)
    # Nodes are 1-indexed, so we need size n+1
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x: int, y: int) -> bool:
        """Returns False if x and y are already connected."""
        px, py = find(x), find(y)
        if px == py:
            return False  # Already connected
        # Union by rank
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True

    # Process edges and find the redundant one
    for a, b in edges:
        if not union(a, b):
            return [a, b]

    return []  # Should never reach here per problem constraints
```

**Why this works:**

1. Use Union Find
2. Process edges one by one
3. If an edge connects two already-connected nodes, it's redundant
4. Return the last such edge found (process in order)

## Key Insights

- Process edges one by one
- Use Union Find to track connectivity
- First edge that connects already-connected nodes is answer
- Return last such edge found

## Common Mistakes

- Not using 1-indexed arrays (nodes are 1 to n)
- Returning the first redundant edge instead of the last one in the input
- Forgetting that the problem wants the last valid answer

## Related Problems

- Redundant Connection II (685)
- Graph Valid Tree (261)

## Tags

Union Find, Graph
