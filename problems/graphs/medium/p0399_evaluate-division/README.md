# Problem 399: Evaluate Division

**Difficulty:** Medium
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/evaluate-division/)

## Problem Description

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the `j^th` query where you must find the answer for `Cj / Dj = ?`.

Return the answers to all queries. If a single answer cannot be determined, return `-1.0`.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

## Constraints

- `1
- equations[i].length == 2
- 1 i.length, Bi.length
- values.length == equations.length
- 0.0
- queries[i].length == 2
- 1 j.length, Dj.length
- Ai, Bi, Cj, Dj` consist of lower case English letters and digits.

## Examples

Example 1:
```

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
```

Example 2:
```

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

```

Example 3:
```

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

```

## Approaches

### 1. Graph with DFS - Build weighted directed graph

**Time Complexity:** O(Q * (V + E))
**Space Complexity:** O(V + E)

```python
def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """
    Evaluate division queries using graph traversal.
    """
    from collections import defaultdict

    # Build graph: graph[a][b] = a / b
    graph = defaultdict(dict)

    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1.0 / value

    def dfs(start: str, end: str, visited: set) -> float:
        """Find path from start to end, return product of edge weights."""
        # Start variable doesn't exist
        if start not in graph:
            return -1.0

        # Direct edge exists
        if end in graph[start]:
            return graph[start][end]

        visited.add(start)

        # Try all neighbors
        for neighbor, weight in graph[start].items():
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return weight * result

        return -1.0

    results = []
    for c, d in queries:
        if c not in graph or d not in graph:
            results.append(-1.0)
        elif c == d:
            results.append(1.0)
        else:
            results.append(dfs(c, d, set()))

    return results
```

**Why this works:**

Model the problem as a graph where:
- Each variable is a node
- Edge A -> B with weight w means A / B = w
- Edge B -> A with weight 1/w means B / A = 1/w

For query (C, D), find path from C to D and multiply edge weights.

## Key Insights

- a/b = 2 implies b/a = 0.5 (store both directions)
- a/c = (a/b) * (b/c) (multiply weights along path)
- If no path exists between variables, result is -1
- a/a = 1 only if 'a' exists in the graph

## Common Mistakes

- Forgetting to add reverse edges (b/a = 1/(a/b))
- Not handling the case where variable doesn't exist in graph
- Not handling self-division (a/a = 1)

## Related Problems

- Cheapest Flights Within K Stops (787)
- Network Delay Time (743)
