# Problem 785: Is Graph Bipartite

**Difficulty:** Medium
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/is-graph-bipartite/)

## Problem Description

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

## Constraints

- graph.length == n
- 1 <= n <= 100
- 0 <= graph[u].length < n
- 0 <= graph[u][i] <= n - 1
- graph[u] does not contain u
- All the values of graph[u] are unique
- If graph[u] contains v, then graph[v] contains u

## Examples

Example 1:
```
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
```

Example 2:
```
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
```

## Approaches

### 1. BFS/DFS with Coloring

**Time Complexity:** O(V + E)
**Space Complexity:** O(V)

```python
def isBipartite(self, graph: List[List[int]]) -> bool:
    """
    Determine if the graph is bipartite.
    """
    from collections import deque

    n = len(graph)
    color = [-1] * n  # -1 = uncolored, 0 or 1 = color

    for start in range(n):
        if color[start] != -1:
            continue  # Already colored

        # BFS to color this component
        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    # Assign opposite color
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # Same color as current node - not bipartite
                    return False

    return True
```

**Why this works:**

1. Try to 2-color the graph using BFS
2. Adjacent nodes must have different colors
3. If we find a conflict, graph is not bipartite
4. Handle disconnected components

## Key Insights

- Try to color graph with 2 colors
- Adjacent nodes must have different colors
- Use BFS or DFS to assign colors
- If conflict found, not bipartite

## Common Mistakes

- Not handling disconnected components
- Using wrong coloring scheme
- Forgetting to check if neighbor is already colored with same color

## Related Problems

- Possible Bipartition (886)
- Flower Planting With No Adjacent (1042)

## Tags

Depth-First Search, Breadth-First Search, Union Find, Graph
