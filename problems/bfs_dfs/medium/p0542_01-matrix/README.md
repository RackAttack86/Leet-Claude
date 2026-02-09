# Problem 542: 01 Matrix

**Difficulty:** Medium
**Pattern:** Bfs Dfs
**Link:** [LeetCode](https://leetcode.com/problems/01-matrix/)

## Problem Description

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

## Constraints

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- mat[i][j] is either 0 or 1
- There is at least one 0 in mat

## Examples

```
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
```

## Approaches

### 1. Multi-source BFS

**Time Complexity:** O(m * n)
**Space Complexity:** O(m * n)

```python
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    if not mat or not mat[0]:
        return mat

    rows, cols = len(mat), len(mat[0])
    queue = deque()
    result = [[float('inf')] * cols for _ in range(rows)]

    # Add all 0s to queue
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                result[r][c] = 0
                queue.append((r, c))

    # BFS from all 0s
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if result[nr][nc] > result[r][c] + 1:
                    result[nr][nc] = result[r][c] + 1
                    queue.append((nr, nc))

    return result
```

**Why this works:**
Start BFS from all cells containing 0 simultaneously. As the BFS expands level by level, each cell gets updated with its distance to the nearest 0. BFS guarantees that the first time a cell is reached, it's via the shortest path.

## Key Insights

- Start BFS from all 0s simultaneously
- Update distances level by level
- Similar to walls and gates
- BFS guarantees shortest distance

## Common Mistakes

- Using DFS instead of BFS (doesn't guarantee shortest path)
- Starting BFS from 1s instead of 0s
- Not initializing non-zero cells to infinity

## Related Problems

- Walls and Gates
- Rotting Oranges

## Tags

Array, Dynamic Programming, Breadth-First Search, Matrix
