# Problem 200: Number of Islands

**Difficulty:** Medium
**Pattern:** Bfs Dfs
**Link:** [LeetCode](https://leetcode.com/problems/number-of-islands/)

## Problem Description

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'

## Examples

```
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Approaches

### 1. DFS Flood Fill

**Time Complexity:** O(m * n)
**Space Complexity:** O(m * n) for recursion/queue

```python
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # Mark as visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count
```

**Why this works:**
Iterate through each cell. When we find an unvisited land cell ('1'), increment the island count and use DFS to mark all connected land cells as visited (change to '0'). This ensures each island is counted exactly once.

## Key Insights

- DFS/BFS from each unvisited land cell
- Mark visited cells
- Count number of DFS/BFS calls
- Classic connected components problem

## Common Mistakes

- Not handling empty grid case
- Forgetting to mark cells as visited, causing infinite loops
- Using wrong comparison (grid values are strings '0' and '1', not integers)

## Related Problems

- Surrounded Regions
- Max Area of Island
- Number of Islands II

## Tags

Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
