# Problem 797: All Paths From Source to Target

**Difficulty:** Medium
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/all-paths-from-source-to-target/)

## Problem Description

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

## Constraints

- n == graph.length
- 2 <= n <= 15
- 0 <= graph[i][j] < n
- graph[i][j] != i (i.e., there will be no self-loops)
- All the elements of graph[i] are unique
- The input graph is guaranteed to be a DAG

## Examples

Example 1:
```
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
```

Example 2:
```
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

## Approaches

### 1. DFS Backtracking

**Time Complexity:** O(2^V * V)
**Space Complexity:** O(V)

```python
def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    """
    Find all paths from node 0 to node n-1 in a DAG.
    """
    n = len(graph)
    target = n - 1
    result = []

    def dfs(node: int, path: List[int]) -> None:
        if node == target:
            result.append(path[:])
            return

        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()  # Backtrack

    dfs(0, [0])
    return result
```

**Why this works:**

1. Use DFS with backtracking
2. Start from node 0
3. When reaching node n-1, add current path to result
4. DAG guarantees no cycles, so no need for visited set

## Key Insights

- Use DFS to explore all paths
- Backtrack to find all possibilities
- Add path when reaching target
- DAG guarantees termination

## Common Mistakes

- Forgetting to make a copy of the path when adding to result
- Using visited set (not needed for DAG, could miss valid paths)
- Not including starting node in the path

## Related Problems

- Number of Paths with Max Score (1301)
- All Paths from Source Lead to Destination (1059)

## Tags

Backtracking, Depth-First Search, Breadth-First Search, Graph
