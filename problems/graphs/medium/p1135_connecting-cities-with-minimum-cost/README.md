# Problem 1135: Connecting Cities With Minimum Cost

**Difficulty:** Medium
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)

## Problem Description

There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1.

The cost is the sum of the connections' costs used.

## Constraints

- 1 <= n <= 10^4
- 1 <= connections.length <= 10^4
- connections[i].length == 3
- 1 <= xi, yi <= n
- xi != yi
- 0 <= costi <= 10^5

## Examples

Example 1:
```
Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
```

Example 2:
```
Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.
```

## Approaches

### 1. Minimum Spanning Tree (Kruskal's Algorithm)

**Time Complexity:** O(E log E)
**Space Complexity:** O(V)

```python
def minimumCost(self, n: int, connections: List[List[int]]) -> int:
    """
    Find minimum cost to connect all cities.
    """
    # Sort connections by cost
    connections.sort(key=lambda x: x[2])

    # Union Find
    parent = list(range(n + 1))  # 1-indexed
    rank = [0] * (n + 1)

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> bool:
        """Returns True if union was performed."""
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True

    total_cost = 0
    edges_added = 0

    for city1, city2, cost in connections:
        if union(city1, city2):
            total_cost += cost
            edges_added += 1

            # We need n-1 edges to connect n cities
            if edges_added == n - 1:
                return total_cost

    # If we couldn't add n-1 edges, cities are not fully connected
    return -1
```

**Why this works:**

1. Sort edges by cost
2. Use Union Find to build MST
3. Add edge if it connects two different components
4. Stop when all cities are connected (n-1 edges added)

## Key Insights

- Sort edges by cost
- Use Union Find to build MST
- Add edge if it connects new components
- Check if all nodes connected at end

## Common Mistakes

- Forgetting that we need exactly n-1 edges for n nodes
- Not handling 1-indexed cities correctly
- Not checking if all cities can be connected

## Related Problems

- Min Cost to Connect All Points (1584)
- Find Critical and Pseudo-Critical Edges in MST (1489)

## Tags

Union Find, Graph, Minimum Spanning Tree
