# Problem 743: Network Delay Time

**Difficulty:** Medium
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/network-delay-time/)

## Problem Description

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

## Constraints

- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique

## Examples

Example 1:
```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

Example 2:
```
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

Example 3:
```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```

## Approaches

### 1. Dijkstra's Shortest Path

**Time Complexity:** O(E log V)
**Space Complexity:** O(V + E)

```python
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    """
    Find minimum time for signal to reach all nodes from source k.
    """
    import heapq
    from collections import defaultdict

    # Build adjacency list
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # Dijkstra's algorithm
    dist = {k: 0}
    min_heap = [(0, k)]  # (distance, node)

    while min_heap:
        d, node = heapq.heappop(min_heap)

        # Skip if we've already found a shorter path
        if d > dist.get(node, float('inf')):
            continue

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    # Check if all nodes are reachable
    if len(dist) < n:
        return -1

    return max(dist.values())
```

**Why this works:**

1. Build adjacency list graph
2. Use Dijkstra's algorithm to find shortest paths from k
3. Return maximum of all shortest paths
4. Return -1 if any node is unreachable

## Key Insights

- Find shortest path to all nodes
- Use Dijkstra with min heap
- Answer is max of all shortest paths
- Return -1 if any node unreachable

## Common Mistakes

- Using BFS instead of Dijkstra (only works for unweighted graphs)
- Forgetting to check if all nodes are reachable
- Not handling 1-indexed nodes correctly

## Related Problems

- Cheapest Flights Within K Stops (787)
- Path with Maximum Probability (1514)

## Tags

Depth-First Search, Breadth-First Search, Graph, Heap (Priority Queue), Shortest Path
